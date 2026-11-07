#!/usr/bin/env python3
"""Authorities extractor (SITE-PLAN Phase 4). Deterministic, table-driven.

Reads the LATIN half of every Quaracchi apparatus entry (translator's `tr-`
notes excluded) and emits one record per authority citation, normalized
through tools/authorities.json:

    chunk_id  volume  note  author  work  pseudo  role  book  locus  locus_key  via  raw

Conventions (frozen at the pilot; repo CLAUDE.md § "Authorities conventions"):
  * Only names in the table are authorities. Editions, manuscripts and the
    Lombard's Sentences are never records; Bonaventure is never an authority.
  * An author's SCOPE runs from his siglum to the next author's siglum or the
    next em dash. Works are matched only inside their own author's scope, and
    case-sensitively (a capitalized abbreviation is a title; a lowercase one is
    a locus: `Serm. 362` vs `in Ps. 118, serm. 13`).
  * role = `same-passage` when the scope opens `hic` / `in hunc locum` (the
    doctor on this same passage); otherwise `cited`.
  * `loc. cit.` / `ibid.` inherit the author's last work in the same chunk.
  * A scope with a locus but no known title is an AUTHOR-LEVEL record
    (`work` empty): residue for the table, never guessed.
  * The locus is kept as printed; `locus_key` is a sortable digit sequence.

Usage:
    python3.11 tools/build-authorities.py --slice pilot --out manual-review/authorities-pilot-records.tsv
    python3.11 tools/build-authorities.py            # whole corpus -> index/authorities.tsv
"""
from __future__ import annotations

import argparse
import collections
import glob
import importlib.util
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TABLE = os.path.join(ROOT, "tools", "authorities.json")
OUT = os.path.join(ROOT, "index", "authorities.tsv")
COLUMNS = ["chunk_id", "volume", "note", "author", "work", "pseudo", "role", "book",
           "locus", "locus_key", "via", "raw"]

ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}

# In a Scripture commentary, an exegete's `in hunc locum` means his own commentary
# on the book being commented, when the table has one (Jerome, Hugh of St Victor
# on Ecclesiastes). Otherwise the record stays same-passage with no work.
HERE_BY_WORK = {
    "ecclesiasten": "in-ecclesiasten",
    "sapientiam": "in-sapientiam",
    "ioannem": "in-ioannem",
    "collationes-ioannem": "in-ioannem",
}


def roman(s):
    s = s.upper()
    if not s or any(c not in ROMAN for c in s):
        return None
    n = 0
    for i, c in enumerate(s):
        v = ROMAN[c]
        n += -v if i + 1 < len(s) and ROMAN[s[i + 1]] > v else v
    return n


def load_bc():
    spec = importlib.util.spec_from_file_location("bc", os.path.join(ROOT, "tools", "build-citations.py"))
    bc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bc)
    return bc


def phrase_re(ab):
    """`de Civ. Dei` -> points optional, spacing free, case-sensitive, whole words."""
    parts = [re.escape(p) for p in re.split(r"[.\s]+", ab) if p]
    body = r"\.?\s*".join(parts)
    return re.compile(r"(?<![A-Za-z])" + body + (r"\.?" if ab.endswith(".") else "") + r"(?![A-Za-z])")


class Table:
    def __init__(self, path=TABLE):
        t = json.load(open(path, encoding="utf-8"))
        self.authors = {a["id"]: a for a in t["authors"]}
        # Body name forms, for the body join (`Augustinus in libro Confessionum[^4]`).
        self.body = sorted(((n, a["id"]) for a in t["authors"] for n in a.get("body", [])),
                           key=lambda x: -len(x[0]))
        self.body_re = re.compile(r"(?<![A-Za-z])(" + "|".join(re.escape(n) for n, _ in self.body) + r")(?![A-Za-z])")
        self.body_of = {n: aid for n, aid in self.body}
        # Every title in the table, for a note that names a work but no author.
        self.all_titles = sorted(((ab, a["id"], w) for a in t["authors"] for w in a["works"] for ab in w["abbrev"]
                                  if len(ab) >= 6), key=lambda x: -len(x[0]))
        self.title_rx = {ab: phrase_re(ab) for ab, _, _ in self.all_titles}
        sig = sorted(((s, a["id"]) for a in t["authors"] for s in a["sigla"]), key=lambda x: -len(x[0]))
        self.sigla = [(phrase_re(s), aid) for s, aid in sig]
        self.works = {}
        for a in t["authors"]:
            pairs = sorted(((ab, w) for w in a["works"] for ab in w["abbrev"]), key=lambda x: -len(x[0]))
            self.works[a["id"]] = [(phrase_re(ab), w) for ab, w in pairs]
        sp = sorted(t["same_passage"], key=len, reverse=True)
        self.same_re = re.compile(r"^\s*(?:" + "|".join(re.escape(x) for x in sp) + r")(?![A-Za-z])")
        an = sorted(t["anaphora"], key=len, reverse=True)
        self.ana_re = re.compile(r"^\s*(?:" + "|".join(re.escape(x) for x in an) + r")")


# The editors reporting a WITNESS's reading (`licet falso alleget libr. IV. Phys.`,
# `Vat. citat …`) is apparatus criticus, not an authority citation.
WITNESS_RE = re.compile(
    r"(?:\b(?:cod|codd|ed|edd|Vat|mss)\.?\b[^.;—]{0,50}\b(?:allegat|alleget|allegant|citat|citant|legit|legunt)\b"
    r"|\bfalso\s+alleg)[^.;—]{0,25}$"
)
LOCUS_START = re.compile(
    r"^\s*(?:(?:l|lib|libr)\.\s*)?(?:[IVXL]+\.?\s+)?(?:c|cap|n|q|qq|tr|tract|serm|epist|ep|homil|hom|text|"
    r"prosa|metr|p|a|art|d|dist|m|lect|reg|sent|tit)\.\s*[\dIVXL]|^\s*[IVXL]+\.\s*c\.|^\s*\d"
)
BOOK_BEFORE = re.compile(r"(?:(?:l|lib|libr)\.\s*)?\b([IVXL]+)\.?\s*$")
TOKEN = re.compile(r"\b(?:[a-z]+\.)?\s*(\d+|[IVXL]+)\b")


def locus_key(book, locus):
    nums = [] if book is None else [book]
    for m in re.finditer(r"(?<![A-Za-z])(\d+|[IVXL]+)(?![A-Za-z])", locus):
        v = m.group(1)
        nums.append(int(v) if v.isdigit() else roman(v))
    return ".".join(str(n) for n in nums[:5] if n is not None)


# A locus is read token by token from the title's end and stops at the first
# thing that is not a locus: prose (`ubi agit…`), a quotation (`:`), a new
# clause. Tokens: `c. 19.`, `n. 24`, `text. 34.`, `q. 23.`, `p. I.`, `§ 1`,
# bare numbers and verse pairs (`1, 1`), ranges, `seq./seqq.`, `et`, a
# parenthesized alternative numbering (`(IV. c. 29.)`), and stock phrases.
LOCUS_TOK = re.compile(
    r"\s*(?:"
    r"(?:[a-z]{1,8}\.|§|Fen|(?:Cap|Text|Quaest|Serm|Tract|Epist|Homil|Libr?|Lib|Q|C)\.)\s*(?:\d+|[IVXL]+)(?:\s*[-–]\s*\d+)?\.?"
    r"|(?:c|cap|tract|tr)\.\s*de\s+[A-Z][a-z]+(?:\s+[a-z]+){0,2}\.?"      # c. de Differentia / tract. de Distributione
    r"|[IVXL]+,(?=\s*n\.)"                                                 # Tractat. VII, n. 6
    r"|(?:Prosa|prosa|Metr\.|metr\.|Metrum|metrum|Homil\.|Serm\.|Epist\.|Ep\.|Lect\.|Quaest\.|Qu\.)\s*(?:\d+|[IVXL]+)\.?"
    r"|\d+(?:\s*[-–]\s*\d+)?\.?"
    r"|[IVXL]+\.?(?=\s*(?:c|n|q|a|text|tr|m|p)\.)"
    r"|\((?:[^()]{1,30})\)\.?"
    r"|et(?=\s+(?:\d|[a-z]{1,8}\.\s*\d|\())"
    r"|seqq?\.|per totam|in fine|in princ(?:ipio|\.)|circa (?:finem|medium|initium|princ\.)|ad finem|initio|q\. unic\."
    r"|[,]"
    r")"
)


def clean_locus(s):
    pos, last = 0, 0
    while True:
        m = LOCUS_TOK.match(s, pos)
        if not m or m.end() == pos:
            break
        pos = m.end()
        if m.group(0).strip(" ,"):
            last = pos
    return re.sub(r"\s+", " ", s[:last]).strip(" ,").strip()[:80]


def extract_entry(text, table, last_work, cid, vol, note, citing_work=""):
    t = re.sub(r"\s+", " ", text.replace("*", "")).strip()
    # Author mentions, longest siglum first, non-overlapping.
    hits, taken = [], []
    for rx, aid in table.sigla:
        for m in rx.finditer(t):
            if any(m.start() < e and s < m.end() for s, e in taken):
                continue
            taken.append((m.start(), m.end()))
            hits.append((m.start(), m.end(), aid))
    hits.sort()
    out = []
    for i, (s, e, aid) in enumerate(hits):
        nxt = hits[i + 1][0] if i + 1 < len(hits) else len(t)
        dash = t.find(" — ", e)
        end = min(nxt, dash) if dash != -1 else nxt
        scope = t[e:end]
        body = re.sub(r"^[\s,:]+", "", scope)
        a = table.authors[aid]
        raw = (t[s:end]).strip()[:140]
        base = {"chunk_id": cid, "volume": vol, "note": note, "author": aid, "raw": raw}

        sm = table.same_re.match(body)
        if sm:
            loc = clean_locus(body[sm.end():])
            here = a.get("here", "")
            if not here and citing_work in HERE_BY_WORK:
                want = HERE_BY_WORK[citing_work]
                if any(w["id"] == want for w in a["works"]):
                    here = want
            out.append({**base, "work": here, "pseudo": "", "role": "same-passage",
                        "book": "", "locus": loc, "locus_key": locus_key(None, loc), "via": "here"})
            continue
        am = table.ana_re.match(body)
        if am:
            w = last_work.get(aid)
            loc = clean_locus(body[am.end():])
            out.append({**base, "work": w["id"] if w else "", "pseudo": "true" if w and w.get("pseudo") else "",
                        "role": "cited", "book": "", "locus": loc, "locus_key": locus_key(None, loc),
                        "via": "anaphor" if w else "anaphor-unresolved"})
            continue

        found, used = [], []
        for rx, w in table.works[aid]:
            for m in rx.finditer(body):
                if any(m.start() < ue and us < m.end() for us, ue in used):
                    continue
                used.append((m.start(), m.end()))
                found.append((m.start(), m.end(), w))
        found.sort(key=lambda x: x[0])
        if found:
            off = len(scope) - len(body)
            for j, (ws, we, w) in enumerate(found):
                if WITNESS_RE.search(t[:e + (len(scope) - len(body)) + ws]):
                    continue
                stop = found[j + 1][0] if j + 1 < len(found) else len(body)
                if j + 1 < len(found):  # the next work's own book numeral is not this locus
                    nb = BOOK_BEFORE.search(body[max(we, stop - 14):stop])
                    if nb:
                        stop = max(we, stop - 14) + nb.start()
                bm = BOOK_BEFORE.search(body[max(0, ws - 14):ws])
                book = roman(bm.group(1)) if bm else None
                bstart = (max(0, ws - 14) + bm.start()) if bm else ws
                loc = clean_locus(body[we:stop])
                span = t[s:e] + " … " + body[bstart:we] + (" " + loc if loc else "") if j or bstart > 2 \
                    else t[s:e] + " " + body[bstart:we] + (" " + loc if loc else "")
                # `Serm. 177. in Appendice`: the Maurists' appendix of spurious works.
                spurious = w.get("pseudo") or re.match(r"[^;—]{0,25}\bin Append", body[we:stop])
                out.append({**base, "raw": re.sub(r"\s+", " ", span)[:140], "work": w["id"],
                            "pseudo": "true" if spurious else "",
                            "role": "cited", "book": book or "", "locus": loc,
                            "locus_key": locus_key(book, loc), "via": "title"})
                last_work[aid] = w
            continue
        if LOCUS_START.match(body):
            loc = clean_locus(body)
            # A siglum that itself names the work (`Decret. Gregor.`) takes its default.
            dw = a.get("default_work", "")
            out.append({**base, "work": dw, "pseudo": "", "role": "cited", "book": "", "locus": loc,
                        "locus_key": locus_key(None, loc), "via": "default-work" if dw else "no-title"})
        # else: a mention in prose (`Augustinus dicit…`), not a citation.
    return out


# A note opening with a bare locus or a bare title (no siglum): the author is in
# the BODY, at the note's anchor (the Scripture index's tier-B join, applied to
# authorities). `Libr. X. c. 33. n. 50` · `Lib. I. c. 23.` · `Quaest. 30` ·
# `De Div. Nom. c. 4. § 15` · `Libr. I. Cur Deus homo, c. 20.`
# Only a real LOCUS opening qualifies (a known title is checked separately in
# implicit_entry). A generic "capitalized word + point" opening was tried and
# rejected at the pilot: it admitted `Vat.`, `Multi codd.`, `Exod. 3, 14`.
IMPLICIT_RE = re.compile(
    r"^(?:(?:Libr?|Lib|In libr|Ex)\.?\s*)?(?:[IVXL]+\.?\s*)?(?:c|cap|n|q|quaest|text|tr|tract|serm|epist|homil|p)\.\s*\d"
    r"|^(?:Libr?|Lib|In libr)\.\s",
    re.I)
LEAD_RE = re.compile(r"^(?:(?:Libr?|Lib|In libr|Ex)\.?\s*)?(?:(?P<b>[IVXL]+|\d{1,2})\.?\s+)?", re.I)
ORDINALS = json.load(open(os.path.join(ROOT, "tools", "scripture-books.json"), encoding="utf-8"))["ordinals"]
ORD_RE = re.compile(r"(?<![A-Za-z])(" + "|".join(sorted((re.escape(k) for k in ORDINALS), key=len, reverse=True)) + r")(?![A-Za-z])", re.I)


STOP = {"de", "et", "in", "ad", "contra", "super", "liber", "libri", "sive", "secundum"}


def prose_title_re(la):
    """`De civitate Dei` -> matches `de Civitate Dei`, `in libro de civitate Dei`;
    `Confessiones` -> `Confessionum`. Each significant word by its stem, so the
    inflected forms of running prose match (a body names a work in the genitive
    or ablative: `in libro Confessionum`, `in Enchiridio`)."""
    words = [w for w in re.sub(r"\(.*?\)", "", la).split() if w.lower() not in STOP and len(w) > 2]
    if not words:
        return None
    stems = [re.escape(w[:max(4, len(w) - 3)]) + r"[a-z]*" for w in words[:3]]
    return re.compile(r"(?<![A-Za-z])" + r"\s+(?:\w+\s+){0,2}".join(stems), re.I)


def anchor_window(c, label, width=220):
    for text in (c.latin_body or "", c.scholion or ""):
        k = text.find(f"[^{label}]")
        if k != -1:
            w = re.sub(r"\[\^[^\]]+\]|<!--.*?-->|[*_#>]", " ", text[max(0, k - width):k])
            return re.sub(r"\s+", " ", w)
    return ""


def implicit_entry(c, label, text, table, last_work):
    t = re.sub(r"\s+", " ", text.replace("*", "")).strip()
    lead = LEAD_RE.match(t)
    if not IMPLICIT_RE.match(t) and not any(table.title_rx[ab].match(t[lead.end():]) for ab, _, _ in table.all_titles):
        return []
    b = lead.group("b")
    book = (int(b) if b.isdigit() else roman(b)) if b else None
    rest = t[lead.end():]
    # 1. the title, if the note gives one, and which authors own it
    title = None
    for ab, aid, w in table.all_titles:
        m = table.title_rx[ab].match(rest)
        if m:
            title = (m, ab)
            break
    owners = {aid for ab, aid, w in table.all_titles if title and ab == title[1]}
    # 2. the author named in the body just before the anchor (the nearest one)
    names = table.body_re.findall(anchor_window(c, label))
    body_author = table.body_of[names[-1]] if names else None
    aid, via = None, None
    if body_author and (not owners or body_author in owners):
        aid, via = body_author, ("body-join+note-title" if title else "body-join")
    elif len(owners) == 1:
        aid, via = next(iter(owners)), "unique-title"
    if not aid:
        return []
    a = table.authors[aid]
    work, loc_from = None, rest
    if title and aid in owners:
        for rx, w in table.works[aid]:
            m = rx.match(rest)
            if m:
                work, loc_from = w, rest[m.end():]
                break
    if not work and via == "body-join":
        # The work named in the body, after the author's name (`Augustinus in libro Confessionum`).
        win = anchor_window(c, label)
        k = win.rfind(names[-1])
        after = win[k:] if k != -1 else win
        best = None
        for w in a["works"]:
            rxs = [phrase_re(x) for x in w.get("prose", [])] + [prose_title_re(w["la"])]
            for rx in rxs:
                for m in (rx.finditer(after) if rx else ()):
                    # the title NEAREST the anchor: `in sermone de Fide … Idem in sexto libro de Trinitate[^n]`
                    if best is None or m.start() > best[0]:
                        best = (m.start(), m.end(), w)
        if best:
            work, via = best[2], "body-join+title"
            if book is None:  # `in libro septimo de Trinitate` · `in secundo Metaphysicae`
                near = after[max(0, best[0] - 30):best[1] + 15]
                om = ORD_RE.search(near)
                if om:
                    book = ORDINALS[om.group(1).lower()]
    if not work and re.match(r"^\s*(?:loc\.\s*cit|ibid)", rest, re.I):
        work = last_work.get(aid)
    loc = clean_locus(loc_from)
    if work:
        last_work[aid] = work
    if work and not loc and via == "body-join+title":
        loc = clean_locus(rest)  # the work came from the body; the note is all locus
    return [{"chunk_id": c.cid, "volume": c.volume, "note": label, "author": aid,
             "work": work["id"] if work else "", "pseudo": "true" if work and work.get("pseudo") else "",
             "role": "cited", "book": book or "", "locus": loc, "locus_key": locus_key(book, loc),
             "via": via, "raw": ((names[-1] + " … ") if names else "") + t[:110]}]


def in_pilot(c):
    if c.volume == 1 and c.dist is not None and 1 <= c.dist <= 10:
        return True
    return c.cid.startswith(("bon-brev-", "bon-eccl-"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slice", choices=["pilot", "all"], default="all")
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--residue", default="", help="write unresolved (author, scope) strings here")
    args = ap.parse_args()

    bc = load_bc()
    table = Table()
    paths = [p for v in sorted(bc.VOLUME_COMPLETE) for p in sorted(glob.glob(os.path.join(ROOT, f"vol{v}", "*.md")))]
    chunks = [c for c in (bc.Chunk(p) for p in paths) if c.cid]
    if args.slice == "pilot":
        chunks = [c for c in chunks if in_pilot(c)]

    rows, entries = [], 0
    for c in chunks:
        last_work = {}
        for lab, txt in c.apparatus.items():
            if lab.startswith("tr-"):
                continue
            entries += 1
            got = extract_entry(txt, table, last_work, c.cid, c.volume, lab, c.work)
            if not got:
                got = implicit_entry(c, lab, txt, table, last_work)
            rows.extend(got)

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write("\t".join(COLUMNS) + "\n")
        for r in rows:
            fh.write("\t".join(str(r.get(k, "")).replace("\t", " ") for k in COLUMNS) + "\n")

    via = collections.Counter(r["via"] for r in rows)
    role = collections.Counter(r["role"] for r in rows)
    withwork = sum(1 for r in rows if r["work"])
    sp_nowork = sum(1 for r in rows if not r["work"] and r["role"] == "same-passage")
    print(f"chunks {len(chunks)} · apparatus entries {entries} · authority records {len(rows)}")
    print(f"  to a work: {withwork} ({withwork / max(1, len(rows)):.1%}) · same passage, no commentary in "
          f"table: {sp_nowork} · author only (residue): {len(rows) - withwork - sp_nowork}")
    print(f"  via: {dict(via)}")
    print(f"  role: {dict(role)}")
    top = collections.Counter(r["author"] for r in rows).most_common(12)
    print("  authors: " + " · ".join(f"{a} {n}" for a, n in top))
    if args.residue:
        res = collections.Counter((r["author"], re.sub(r"\d+", "N", r["raw"].split(",", 1)[-1][:40]).strip())
                                  for r in rows if not r["work"] and r["role"] != "same-passage")
        with open(args.residue, "w", encoding="utf-8") as fh:
            for (a, s), n in res.most_common():
                fh.write(f"{n}\t{a}\t{s}\n")
        print(f"  residue: {len(res)} distinct author-level strings -> {args.residue}")


if __name__ == "__main__":
    raise SystemExit(main())
