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
PREFIX_WORDS = {"de", "in", "contra", "super", "ad", "libr", "lib", "liber", "libri", "sive"}

# `in hunc locum` of an EXEGETE is his commentary on the Scripture verse in question
# (`Psalm. 102, 5 … Cfr. August., in hunc loc.` = the Enarrationes on Ps. 102). The
# book is the last Scripture reference in the note before the siglum; failing that,
# in a Scripture commentary, the book commented. The author's `exegesis` map (book key
# of tools/scripture-books.json -> work) gives the work. A scholastic's `hic` / `in
# hunc locum` is his commentary on the Sentences (`here`).
CHUNK_BOOK = {
    "ecclesiasten": "Eccle",
    "sapientiam": "Sap",
    "ioannem": "Ioan",
    "collationes-ioannem": "Ioan",
}
_SB = json.load(open(os.path.join(ROOT, "tools", "scripture-books.json"), encoding="utf-8"))["books"]
_VERSE_ABBR = sorted(((ab, b["key"]) for b in _SB for ab in b["abbrev"]), key=lambda x: -len(x[0]))
VERSE_REF_RE = re.compile(r"(?<![A-Za-z])(" + "|".join(
    r"\.?\s*".join(re.escape(p) for p in re.split(r"[.\s]+", ab) if p) for ab, _ in _VERSE_ABBR)
    + r")\.?\s*\d+\s*,\s*\d+")
_VERSE_KEY = {re.sub(r"[.\s]", "", ab): k for ab, k in _VERSE_ABBR}


def verse_book(text):
    """The book of the LAST Scripture reference (`Psalm. 102, 5`) in `text`."""
    last = None
    for m in VERSE_REF_RE.finditer(text):
        last = _VERSE_KEY.get(re.sub(r"[.\s]", "", m.group(1)))
    return last


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


def phrase_re(ab, extend=False):
    """`de Civ. Dei` -> points optional, spacing free, case-sensitive, whole words.

    extend=True (work titles, not sigla): a word the table abbreviates (`concup.`,
    `Evangel.`) also matches a LONGER abbreviation of the same word in a note
    (`concupisc.`, `Evangelist.`). Only words of 3+ letters that the table ends
    with a point are extended; full words stay exact."""
    toks = re.findall(r"[^.\s]+\.?", ab)
    key = next((i for i, t in enumerate(toks) if t.rstrip(".").lower() not in PREFIX_WORDS), 0)
    parts = []
    for i, tok in enumerate(toks):
        w = tok.rstrip(".")
        ext = extend and tok.endswith(".") and len(w) >= 3 and w[-1].isalpha()
        # The first significant word keeps its printed case (`Serm.` a title, `serm.`
        # a locus); the words after it are case-free (`de Gener. et Corrupt.`).
        # `De Bono coniugali` = `de Bono coniug.`: the prefix words are case-free too.
        free = extend and w.isalpha() and (i != key)
        core = "(?i:" + re.escape(w) + ")" if free else re.escape(w)
        parts.append(core + (r"[a-z]*" if ext else ""))
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
        self.title_rx = {ab: phrase_re(ab, True) for ab, _, _ in self.all_titles}
        sig = sorted(((s, a["id"]) for a in t["authors"] for s in a["sigla"]), key=lambda x: -len(x[0]))
        self.sigla = [(phrase_re(s), aid) for s, aid in sig]
        self.works = {}
        for a in t["authors"]:
            pairs = sorted(((ab, w) for w in a["works"] for ab in w["abbrev"]), key=lambda x: -len(x[0]))
            self.works[a["id"]] = [(phrase_re(ab, True), w) for ab, w in pairs]
        sp = sorted(t["same_passage"], key=len, reverse=True)
        self.same_re = re.compile(r"^\s*(?:" + "|".join(re.escape(x) for x in sp) + r")(?![A-Za-z])")
        # Where a scope must END although no author follows: the Lombard named as
        # the Master of the Sentences (`a Magistro Sententiarum (III. Sent. d. XVI.)`)
        # and Bonaventure's own Sentences (`S. Bonav., II. Sent. d. 2.`), else their
        # `Sent.` locus is taken as the preceding author's (S. Thomas's) Sentences.
        # A bare `Magistri` / `S. Bonav.` does NOT end a scope: the author's further
        # citations follow it (`Cfr. hic lit. Magistri, c. 2, et de Dono persev.`).
        self.stop_re = re.compile(r"(?<![A-Za-z])(?:Magistr(?:o|i|um)\s+Sententiar\w*|Magister\s+Sententiar\w*|"
                                  r"(?:S\.\s*)?Bonav\.(?=,?\s*(?:[IVX]+\.\s*)?Sent\.))")
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
    r"prosa|metr|p|a|art|d|dist|m|lect|reg|sent|tit|prop|propos)\.\s*[\dIVXL]|^\s*[IVXL]+\.\s*c\.|^\s*\d"
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
        st = table.stop_re.search(t, e, end)
        if st:
            end = st.start()
        scope = t[e:end]
        body = re.sub(r"^[\s,:]+", "", scope)
        a = table.authors[aid]
        raw = (t[s:end]).strip()[:140]
        base = {"chunk_id": cid, "volume": vol, "note": note, "author": aid, "raw": raw}

        sm = table.same_re.match(body)
        if not sm and re.fullmatch(r"\s*(?:et|,|;)?\s*", body) and i + 1 < len(hits):
            # `Petr. a Tar. et Richard. a Med., hic circa lit.`: the `hic` is both men's.
            nb = re.sub(r"^[\s,:]+", "", t[hits[i + 1][1]:])
            if table.same_re.match(nb):
                body, sm = nb, table.same_re.match(nb)
        if sm:
            loc = clean_locus(body[sm.end():])
            here, via = a.get("here", ""), "here"
            if citing_work in CHUNK_BOOK and here:
                # In a Scripture commentary a scholastic's `in hunc locum` is his
                # commentary on that book, never his Sentences commentary.
                here = ""
            if not here and a.get("exegesis"):
                if citing_work in CHUNK_BOOK:
                    # In a Scripture commentary the passage is the book commented,
                    # unless a verse stands in the siglum's own clause
                    # (`Psalm. 52, 10. Quem locum August., in hunc locum …`).
                    clause = re.split(r" — |\]|\)", t[:s])[-1][-60:]
                    bk = verse_book(clause) or CHUNK_BOOK[citing_work]
                else:
                    bk = verse_book(t[:s])
                if bk and a["exegesis"].get(bk):
                    here, via = a["exegesis"][bk], "here+verse"
            w = next((x for x in a["works"] if x["id"] == here), None)
            out.append({**base, "work": here, "pseudo": "true" if w and w.get("pseudo") else "",
                        "role": "same-passage", "book": "", "locus": loc,
                        "locus_key": locus_key(None, loc), "via": via})
            continue
        if a.get("here") and citing_work in CHUNK_BOOK and re.match(r"^\s*:", scope):
            # `Card. Hugo: «De caelo, non empyreo…»` in a Scripture commentary: his
            # postilla on this verse, quoted without a locus.
            out.append({**base, "work": a["here"], "pseudo": "", "role": "same-passage", "book": "",
                        "locus": "", "locus_key": "", "via": "here-quoted"})
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
                spurious = w.get("pseudo") or re.match(r"[^;—]{0,25}\bin append", body[we:stop], re.I)
                out.append({**base, "raw": re.sub(r"\s+", " ", span)[:140], "work": w["id"],
                            "pseudo": "true" if spurious else "",
                            "role": "cited", "book": book or "", "locus": loc,
                            "locus_key": locus_key(book, loc), "via": "title"})
                last_work[aid] = w
            continue
        if LOCUS_START.match(body) and not re.match(r"\s*1[4-9]\d\d\b", body):  # `ed. Basil. 1529` is Basel
            loc = clean_locus(body)
            # A siglum that itself names the work (`Decret. Gregor.`) takes its default.
            dw = a.get("default_work", "")
            # `default_if`: the default only for a locus of that shape (Alexander's
            # `p. IV. q. 8.` is his Summa; `d. 26.` would not be).
            if dw and a.get("default_if") and not re.match(a["default_if"], loc):
                dw = ""
            out.append({**base, "work": dw, "pseudo": "", "role": "cited", "book": "", "locus": loc,
                        "locus_key": locus_key(None, loc), "via": "default-work" if dw else "no-title"})
        # else: a mention in prose (`Augustinus dicit…`), not a citation.
    # `de Mirabilibus sacrae Script. (inter opera August.) c. 20`: the title comes
    # BEFORE its author, who is named only as the one among whose works it is
    # transmitted. The work of that author whose title ends at the parenthesis;
    # always pseudo (that is what `inter opera` says).
    have = {(r["author"], r["work"]) for r in out}
    for pm in INTER_OPERA_RE.finditer(t):
        aid = next((a for rx, a in table.sigla if rx.match(pm.group(1))), None)
        if not aid:
            continue
        pre = t[max(0, pm.start() - 80):pm.start()]
        best = None
        for rx, w in table.works[aid]:
            for m in rx.finditer(pre):
                if re.fullmatch(r"[\s.,]*", pre[m.end():]) and (best is None or m.start() < best[0]):
                    best = (m.start(), w)
        if best and (aid, best[1]["id"]) not in have:
            loc = clean_locus(t[pm.end():pm.end() + 60])
            bm = BOOK_BEFORE.search(pre[max(0, best[0] - 14):best[0]])
            book = roman(bm.group(1)) if bm else None
            out.append({"chunk_id": cid, "volume": vol, "note": note, "author": aid, "work": best[1]["id"],
                        "pseudo": "true", "role": "cited", "book": book or "", "locus": loc,
                        "locus_key": locus_key(book, loc), "via": "inter-opera",
                        "raw": re.sub(r"\s+", " ", pre[best[0]:] + t[pm.start():pm.end() + 20])[:140]})
            have.add((aid, best[1]["id"]))
    return out


INTER_OPERA_RE = re.compile(r"\((?:inter opera|in append\w*\.?\s*(?:serm\.\s*)?)\s*(?:S\.\s*)?([A-Z][a-z]+\.?)[^)]{0,30}\)", re.I)


# A note opening with a bare locus or a bare title (no siglum): the author is in
# the BODY, at the note's anchor (the Scripture index's tier-B join, applied to
# authorities). `Libr. X. c. 33. n. 50` · `Lib. I. c. 23.` · `Quaest. 30` ·
# `De Div. Nom. c. 4. § 15` · `Libr. I. Cur Deus homo, c. 20.`
# Only a real LOCUS opening qualifies (a known title is checked separately in
# implicit_entry). A generic "capitalized word + point" opening was tried and
# rejected at the pilot: it admitted `Vat.`, `Multi codd.`, `Exod. 3, 14`.
IMPLICIT_RE = re.compile(
    r"^(?:(?:Libr?|Lib|In libr|Ex)\.?\s*)?(?:[IVXL]+\.?\s*)?(?:c|cap|n|q|quaest|text|tr|tract|serm|epist|homil|p|prop|propos)\.\s*\d"
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


def after_anchor(c, label, width=70):
    """The few words right AFTER the anchor, up to the quotation or the clause:
    `Augustinus decimo quarto[^n] de Civitate Dei, quod «…»` · `Hieronymus[^n] super Matthaeum`."""
    for text in (c.latin_body or "", c.scholion or ""):
        k = text.find(f"[^{label}]")
        if k != -1:
            w = re.sub(r"\[\^[^\]]+\]|<!--.*?-->|[*_#>]", " ", text[k + len(label) + 3:k + len(label) + 3 + width])
            w = re.split(r"[«:;»\"]|\bquod\b|\bdicens\b|\bait\b|\bdicit\b", w)[0]
            return re.sub(r"\s+", " ", w)
    return ""


# `in eodem libro` / `ibidem` / `in eodem` after the name: the author's last work in this chunk.
SAME_WORK_RE = re.compile(r"\b(?:in\s+eodem(?:\s+libro)?|ibidem|eodem\s+libro)\b")


_BODY_RX = {}


def body_abbrev_re(ab):
    """A table abbreviation read in running Latin: `de Lib. arb.` -> `de Libero Arbitrio`,
    `Poster.` -> `Posteriorum`. The first significant word must be capitalized as printed
    and have 4+ letters (so `Ep.`, `Serm.` never fire on prose, and `confessio` /
    `prior` in lower case never match `Confess.` / `Prior.`); the rest is case-free;
    abbreviated words extend to the full word."""
    if ab in _BODY_RX:
        return _BODY_RX[ab]
    toks = re.findall(r"[^.\s]+\.?", ab)
    key = next((i for i, t in enumerate(toks) if t.rstrip(".").lower() not in PREFIX_WORDS), None)
    rx = None
    if key is not None and len(re.sub(r"[^A-Za-z]", "", toks[key])) >= 4 and toks[key][0].isupper():
        parts = []
        for i, tok in enumerate(toks):
            w = tok.rstrip(".")
            if not re.fullmatch(r"[A-Za-zë]+", w):
                parts.append(re.escape(w))
                continue
            ext = r"[a-zë]*" if tok.endswith(".") else ""
            if i == key:
                parts.append(re.escape(w[0]) + "(?i:" + re.escape(w[1:]) + ")" + ext)
            else:
                parts.append("(?i:" + re.escape(w) + ")" + ext)
        rx = re.compile(r"(?<![A-Za-z])" + r"\.?\s*".join(parts) + r"(?![A-Za-z])")
    _BODY_RX[ab] = rx
    return rx


def prose_re(x):
    """A `prose` form, case-free (`octoginta trium Quaestionum` = `Octoginta trium …`)."""
    if x not in _BODY_RX:
        _BODY_RX[x] = re.compile(phrase_re(x).pattern, re.I)
    return _BODY_RX[x]


def body_title(a, text):
    """The work of author `a` named in running Latin in `text`, nearest its END (the
    longest at a tie: `de Generatione animalium` over `de Generatione`), with span."""
    best = None
    for w in a["works"]:
        rxs = [prose_re(x) for x in w.get("prose", [])] + [body_abbrev_re(x) for x in w["abbrev"]] \
            + [prose_title_re(w["la"])]
        for rx in rxs:
            for m in (rx.finditer(text) if rx else ()):
                if best is None or m.start() > best[0] or (m.start() == best[0] and m.end() > best[1]):
                    best = (m.start(), m.end(), w)
    return best


# Between the author's name and the anchor, a pointer to the Lombard's own text or to
# another place in Bonaventure (`et habetur in littera`, `sicut supra`): the note then
# gives the Lombard's chapter, not this author's locus.
XREF_RE = re.compile(r"\b(?:habetur|habitum est|dictum (?:fuit|est)|ostensum est|supra|infra|in littera|"
                     r"distinctione|manifestabitur)\b")
# A note giving a Scripture verse (`Cap. 14, 12.` · `Vers. 23.`) cites the Bible.
VERSE_RE = re.compile(r"^(?:Cap\.\s*)?\d+\s*,\s*\d+|^Vers\.")
PAGE_REF_RE = re.compile(r"^P\.\s*\d+,\s*not\.\s*\d+\.\s*")


def stands_as_title(after):
    """Is what follows a matched title consistent with its being a TITLE? A locus,
    `loc. cit.`, a book numeral, punctuation, or the end of a sentence: yes. A prose
    word (`Distinctionem ipsam inter…`, `Canon Missae, ubi…`) or the title going on
    (`De Fide et operibus`): no."""
    a = after.lstrip()
    if not a or a[0] in ",;:([":
        return True
    if a[0] == ".":
        nxt = a[1:].lstrip()
        return not nxt or nxt[0].isupper() or nxt[0].isdigit()
    if clean_locus(a):
        return True
    m = re.match(r"([A-Za-z]+)", a)
    if not m:
        return True
    w = m.group(1)
    return w.lower() in {"loc", "ibid", "in", "seq", "seqq"} or bool(re.fullmatch(r"[IVXLC]+", w))


def implicit_entry(c, label, text, table, last_work):
    t = re.sub(r"\s+", " ", text.replace("*", "")).strip()
    t = PAGE_REF_RE.sub("", t)  # `P. 878, not. 8. Libr. III. c. 10.` (a Bonelli cross-page)
    lead = LEAD_RE.match(t)
    rest = t[lead.end():]
    win = anchor_window(c, label)
    names = table.body_re.findall(win)
    body_author = table.body_of[names[-1]] if names else None

    def own_title(aid, s):
        for rx, w in table.works[aid]:
            m = rx.match(s)
            if m:
                return w, m
        return None, None

    # A note opening with `Libr. 83 Quaest.` is not book 83: retry without the numeral.
    bare = re.sub(r"^(?:Libr?|Lib|In libr)\.?\s*", "", t, flags=re.I)
    # `Libr. II. (sive de Dono perseverantiae) c. 22.`: the note's own alternative title.
    rest = re.sub(r"^\((?:sive|seu|vel)\s+([^()]{3,60})\)\s*", r"\1 ", rest)
    opens_title = any(table.title_rx[ab].match(rest) for ab, _, _ in table.all_titles) or \
        (body_author and (own_title(body_author, rest)[0] or own_title(body_author, bare)[0]))
    if not IMPLICIT_RE.match(t) and not opens_title:
        return []
    b = lead.group("b")
    book = (int(b) if b.isdigit() else roman(b)) if b else None
    # 1. the title, if the note gives one, and which authors own it
    title = None
    for ab, aid, w in table.all_titles:
        m = table.title_rx[ab].match(rest)
        if m:
            title = (m, ab)
            break
    # Every author with a title that matches HERE (`In Hexaem.` is Bede's and Basil's).
    owners = {aid for ab, aid, w in table.all_titles if title and table.title_rx[ab].match(rest)}
    # 2. the author named in the body just before the anchor (the nearest one)
    aid, via = None, None
    if body_author and (not owners or body_author in owners):
        aid, via = body_author, ("body-join+note-title" if title else "body-join")
    elif body_author and (own_title(body_author, rest)[0] or own_title(body_author, bare)[0]):
        # The note's title is ALSO one of the body author's own works (a shorter
        # abbreviation another author owns at full length): the body author.
        aid, via = body_author, "body-join+note-title"
    elif len(owners) == 1 and stands_as_title(rest[title[0].end():]):
        # A title only one author owns, standing as a title: a locus follows it, or
        # nothing does (`Distinctionem ipsam inter…` is prose, not Alan's `Distinct.`).
        # When the body names someone else, the note is Quaracchi correcting the
        # attribution (`Isidorus[^n]` · `Libr. XXXI. Moral.`): attribution follows
        # Quaracchi (R2).
        aid, via = next(iter(owners)), "unique-title"
    if not aid:
        return []
    a = table.authors[aid]
    work, loc_from = None, rest
    # The note's own title, matched against THIS author's works (any length: `Phys.`).
    w, m = own_title(aid, rest)
    if not w:
        w, m = own_title(aid, bare)
        if w:
            book, rest = None, bare
    if not w and aid == body_author:
        # The title further on in the note's first clause: `Tract. 27. in Ioan. Evang. n. 5`.
        head = re.split(r" — |;", t)[0][:70]
        # Only when NOTHING but a locus precedes the title (not `Cap. 7. Cfr. … de Trin.`).
        def locus_only(pre):
            pre = re.sub(r"^(?:Libr?|Lib)\.?\s*", "", pre).strip(" ,.")
            return len(clean_locus(pre)) >= len(pre) - 1
        hits = sorted(((mm.start(), -len(mm.group(0)), w2, mm) for rx, w2 in table.works[aid]
                       for mm in [rx.search(head)] if mm and mm.start() > 0 and locus_only(head[:mm.start()])),
                      key=lambda x: x[:2])
        if hits:
            w, mm = hits[0][2], hits[0][3]
            work, loc_from = w, (head[:mm.start()] + " " + head[mm.end():]).strip()
            w = None
            via = "body-join+note-title"
    if w:
        work, loc_from = w, rest[m.end():]
        if via == "body-join":
            via = "body-join+note-title"
    # A bracketed title inside the note: `Cap. 20. n. 28 [de Trin. IV]`.
    if not work:
        bm = re.search(r"\[([^\]]{3,40})\]", t)
        if bm:
            for rx, w2 in table.works[aid]:
                mm = rx.search(bm.group(1))
                if mm:
                    work = w2
                    nb = re.search(r"\b([IVXL]+)\b", bm.group(1)[mm.end():])
                    if nb and book is None:
                        book = roman(nb.group(1))
                    via = "body-join+note-title" if via.startswith("body-join") else via
                    break
    if not work and via == "body-join":
        k = win.rfind(names[-1])
        before = win[k:] if k != -1 else win
        aft = after_anchor(c, label)
        best = body_title(a, before)
        near = None
        if best:
            near = before[max(0, best[0] - 30):best[1] + 15]
        else:
            best = body_title(a, aft)  # `Augustinus decimo quarto[^n] de Civitate Dei`
            if best:
                near = before[-40:] + " " + aft[:best[1] + 15]
        if best:
            work, via = best[2], "body-join+title"
            if book is None:  # `in libro septimo de Trinitate` · `in secundo Metaphysicae`
                om = ORD_RE.search(near)
                if om:
                    book = ORDINALS[om.group(1).lower()]
        elif SAME_WORK_RE.search(before + " " + aft) and last_work.get(aid):
            work, via = last_work[aid], "body-join+same-work"
    if not work and re.match(r"^\s*(?:loc\.\s*cit|ibid)", rest, re.I):
        work = last_work.get(aid)
    if not work and via.startswith("body-join"):
        k = win.rfind(names[-1]) if names else -1
        between = win[k + len(names[-1]):] if k != -1 else ""
        if XREF_RE.search(between) or VERSE_RE.match(t):
            return []
    loc = clean_locus(loc_from)
    if work:
        last_work[aid] = work
    if work and not loc and via.startswith("body-join+") and via != "body-join+note-title":
        loc = clean_locus(rest)  # the work came from the body; the note is all locus
    return [{"chunk_id": c.cid, "volume": c.volume, "note": label, "author": aid,
             "work": work["id"] if work else "", "pseudo": "true" if work and work.get("pseudo") else "",
             "role": "cited", "book": book or "", "locus": loc, "locus_key": locus_key(book, loc),
             "via": via, "raw": ((names[-1] + " … ") if names else "") + t[:110]}]


EDITORIAL_PREFIX_RE = re.compile(r"\*?\[Quaracchi p\.\s*\d+\s*footer entry \d+[.:]?\]\*?\s*")
EDITORIAL_FLAG_RE = re.compile(r"\[[^\]]*(?:OCR|\?)[^\]]*\]")
EDITORIAL_RE = re.compile(r"OCR|ambiguities log|Editorial note|\bmarker\b|not preserved|Continuation of|\bAnchor on\b|tier2")


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

    rows, entries, editorial = [], 0, 0
    for c in chunks:
        last_work = {}
        for lab, txt in c.apparatus.items():
            if lab.startswith("tr-"):
                continue
            entries += 1
            # This edition's own placeholders are not Quaracchi's apparatus: a
            # `[Quaracchi p. N footer entry N.]` prefix is stripped, an inline `[?: …]`
            # flag removed, and an entry that is OUR note (`OCR-bled … see
            # ambiguities log`, `Editorial note.`) yields no record.
            txt = EDITORIAL_PREFIX_RE.sub("", txt)
            txt = EDITORIAL_FLAG_RE.sub("", txt)
            if EDITORIAL_RE.search(txt):
                editorial += 1
                continue
            got = extract_entry(txt, table, last_work, c.cid, c.volume, lab, c.work)
            # A note that OPENS with a bare locus or title (no siglum first) cites the
            # author named in the body, whatever else it cites further on
            # (`Cap. 29. … ex August. de Agone christiano`): both are records.
            flat = re.sub(r"\s+", " ", txt.replace("*", "")).strip()
            if not any(rx.match(flat) for rx, _ in table.sigla):
                imp = implicit_entry(c, lab, txt, table, last_work)
                have = {(r["author"], r["work"]) for r in got}
                got = imp + [r for r in got] if not imp or (imp[0]["author"], imp[0]["work"]) not in have else got
                if imp:
                    # The note goes on in the SAME author's voice: further titles with no
                    # siglum are his (`Libr. X. c. 3. …; XII. de Gen. ad lit. c. 31.`).
                    # Read the note as if it opened with his siglum; keep only works
                    # the join did not already give.
                    sig = table.authors[imp[0]["author"]]["sigla"][0]
                    more = extract_entry(sig + " " + flat, table, dict(last_work), c.cid, c.volume, lab, c.work)
                    have = {(r["author"], r["work"]) for r in got}
                    for r in more:
                        if r["work"] and r["author"] == imp[0]["author"] and (r["author"], r["work"]) not in have \
                                and r["via"] == "title":
                            r["via"] = "body-join+continued"
                            r["raw"] = r["raw"].replace(sig + " ", "", 1)
                            got.append(r)
                            have.add((r["author"], r["work"]))
            # A title repeated in the same note with no locus adds nothing.
            seen = {(r["author"], r["work"]) for r in got if r["locus"]}
            got = [r for r in got if r["locus"] or (r["author"], r["work"]) not in seen or not r["work"]]
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
    print(f"chunks {len(chunks)} · apparatus entries {entries} (editorial placeholders skipped: {editorial})"
          f" · authority records {len(rows)}")
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
