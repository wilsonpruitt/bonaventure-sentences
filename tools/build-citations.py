#!/usr/bin/env python3.11
"""
build-citations.py — the opera-omnia citation extractor (INDEX-PLAN.md, Phase 0+).

Emits ONE ledger record per citation occurrence to index/citations.tsv. The scripture
index, the cross-reference index, the cited-by backlinks and the QA report are all
views over that single ledger — see tools/build-index-json.py.

FROZEN RULES THIS TOOL EMBODIES (do not "simplify" them away):
  * Derived, never hand-tagged. Zero writes under vol*/. Run it as often as you like.
  * Latin is the keying side. English bodies/apparatus are display-only and are NOT
    parsed — English punctuation drifts, Latin citation syntax is systematic.
  * Glob, never recurse: vol{N}/*.md only. vol1/_backup-*/ holds 538 stale files.
  * Never guess. A citation the parser cannot classify becomes a QA line, not a record
    with an invented target.
  * Census: the ledger's chunk roster must equal the vol*/ glob, asserted at exit
    (same pattern as tools/check-vol5-census.py).
  * Ruling 57 (C1, 2026-10-16): an `ibid. C, V` / `ibid. v. N` keeps its OWN
    coordinates and inherits only its BOOK (for `v. N`, book + chapter) — see
    resolve_coord_ibid(). Printed slips (C2) are filed as printed and annotated
    from PRINTED_SLIPS, never corrected. Capital `Ibid.` and body `ibidem` are
    NOT in scope (separately reported classes).

Usage:
    python3.11 tools/build-citations.py                     # all volumes
    python3.11 tools/build-citations.py --volumes 5         # pilot subset
    python3.11 tools/build-citations.py --volumes 1,5 --vol1-max-d 10
    python3.11 tools/build-citations.py --sample 50 --seed 7 > /dev/null
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS_JSON = os.path.join(ROOT, "tools", "scripture-books.json")
LEDGER = os.path.join(ROOT, "index", "citations.tsv")
QA_REPORT = os.path.join(ROOT, "manual-review", "citation-qa-report.md")
# NOT `citation-pilot-sample.md` — that is the FROZEN, hand-verified Phase 0 snapshot
# and must not be clobbered by a later `--sample` run.
SAMPLE_OUT = os.path.join(ROOT, "manual-review", "citation-sample-latest.md")

# Reused from tools/audit-style-formatting.py — apparatus labels are bare (`[^12]`,
# vols I-III) or page-qualified (`[^p210-1]`, vols IV-V). Both must parse.
LABEL_RE = r"[A-Za-z0-9-]+"
ANCHOR_RE = re.compile(rf"\[\^({LABEL_RE})\]")
APPARATUS_DEF_RE = re.compile(rf"^\[\^({LABEL_RE})\]:", re.MULTILINE)

ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
         "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12}
ROMAN_RE = r"(?:I{1,3}|IV|VI{0,3}|IX|XI{0,2}|X)"
BOOK_ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV"}

# A clause boundary resets the author-sigil lookback. Quaracchi separates independent
# segments of one note with an em-dash; `Cfr.`/`Vide` introduce a fresh citation.
# A colon is NOT a clause boundary here: it introduces quoted matter that still
# belongs to the author just named (`haec B. Albert. verba: *Dicunt quidam…* (I. Sent.
# d. 26. a. 10.)`). Splitting on it stranded the siglum and misfiled Albert's own
# distinction numbering as a Bonaventure self-reference.
CLAUSE_SPLIT_RE = re.compile(r"—|;|\bCfr\.|\bcfr\.|\bVide\b|\bvide\b")
# Within one author's citation CHAIN, `;` separates loci belonging to the same
# author (`Richard. a Med., hic a. 2. q. 3.; II. Sent. d. 23. a. 2. q. 1.; ibid. …`),
# so the chain lookback must not stop at it. `—`, `Cfr.` and `Vide` still start a
# fresh citation and do stop it.
CHAIN_SPLIT_RE = re.compile(r"—|\bCfr\.|\bcfr\.|\bVide\b|\bvide\b")


# --------------------------------------------------------------------------- config


def load_books():
    with open(BOOKS_JSON, encoding="utf-8") as fh:
        cfg = json.load(fh)

    abbrev_map, body_map, meta = {}, {}, {}
    for b in cfg["books"]:
        meta[b["key"]] = b
        for a in b.get("abbrev", []):
            abbrev_map[normalize_abbrev(a)] = b["key"]
        for f in b.get("body_forms", []):
            body_map[f] = b["key"]
    cfg["_abbrev_map"] = abbrev_map
    cfg["_body_map"] = body_map
    cfg["_meta"] = meta
    cfg["_author_sigla"] = sorted(cfg["authors"]["sigla"], key=len, reverse=True)
    return cfg


def normalize_abbrev(s: str) -> str:
    """Fold the variation that is punctuation-only, so `I Cor.` == `I. Cor.`."""
    s = s.strip().replace(".", " ")
    return re.sub(r"\s+", " ", s).strip().lower()


# ---------------------------------------------------------------------- chunk model


class Chunk:
    __slots__ = ("path", "cid", "volume", "book", "dist", "pars", "sectio", "art",
                 "quaestio", "ctype", "pages", "work", "division", "capitulum",
                 "latin_body", "scholion", "apparatus")

    def __init__(self, path):
        self.path = path
        raw = open(path, encoding="utf-8").read()
        fm = parse_frontmatter(raw)
        # Frontmatter ids are quoted (`id: "bon-brev-p5-c1"`). Strip them: an id
        # carrying literal quote characters can never match a target this tool
        # CONSTRUCTS (`bon-brev-p5-c6`), so work-relative refs silently resolved as
        # `forward` even when the chunk was already on disk.
        self.cid = (fm.get("id", "") or "").strip().strip('"').strip("'")
        self.volume = as_int(fm.get("volume"))
        self.book = as_int(fm.get("book"))
        self.dist = as_int(fm.get("distinctio"))
        self.pars = as_int(fm.get("pars"))
        self.sectio = as_int(fm.get("sectio"))
        self.art = as_int(fm.get("articulus"))
        self.quaestio = as_int(fm.get("quaestio"))
        self.ctype = (fm.get("type") or "").strip().strip('"')
        self.pages = parse_int_list(fm.get("printed_pages"))
        self.work = (fm.get("work") or "").strip().strip('"')
        self.division = as_int(fm.get("division"))
        self.capitulum = as_int(fm.get("capitulum"))
        body, schol, app = split_sections(raw)
        self.latin_body = body
        self.scholion = schol
        self.apparatus = app  # label -> Latin text of the entry


def parse_frontmatter(raw: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", raw, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if km:
            out[km.group(1)] = km.group(2).strip()
    return out


def as_int(v):
    if v is None:
        return None
    m = re.search(r"\d+", str(v))
    return int(m.group()) if m else None


def parse_int_list(v):
    if not v:
        return []
    return [int(x) for x in re.findall(r"\d+", str(v))]


def split_sections(raw: str):
    """Latin body, Latin scholion, and the **La.** half of each apparatus entry.

    Mirrors build-content.mjs's extractLanguageBlock: a `## Latin` block terminates
    only on a sentinel heading, and `### Scholion` (which MUST be last in the block,
    per CLAUDE.md's parser gotcha) takes everything to the block's end.
    """
    sentinel = r"^## (?:Latin|English|Apparatus|Notes|Scholion)\b|^---\s*$"

    def block(name):
        m = re.search(rf"^## {name}\s*$", raw, re.M)
        if not m:
            return ""
        rest = raw[m.end():]
        stop = re.search(sentinel, rest, re.M)
        return rest[: stop.start()] if stop else rest

    latin = block("Latin")
    schol = ""
    sm = re.search(r"^### Scholion\s*$", latin, re.M)
    if sm:
        schol = latin[sm.end():]
        latin = latin[: sm.start()]

    apparatus = {}
    app_block = block("Apparatus")
    # Entries run from one `[^label]:` def to the next.
    defs = list(APPARATUS_DEF_RE.finditer(app_block))
    for i, m in enumerate(defs):
        end = defs[i + 1].start() if i + 1 < len(defs) else len(app_block)
        entry = app_block[m.end(): end]
        # Keep only the Latin half. The **En.** line is display-only.
        la = re.search(r"\*\*La\.\*\*(.*?)(?=\*\*En\.\*\*|$)", entry, re.S)
        apparatus[m.group(1)] = (la.group(1) if la else entry).strip()
    return latin, schol, apparatus


# ------------------------------------------------------------------ corpus indexes


def build_indexes(chunks):
    by_locus = {}          # (book, dist, pars, sectio, art, q_or_type) -> cid
    by_dist = defaultdict(list)   # (book, dist) -> [(coords, cid)]
    by_page = defaultdict(list)   # (volume, printed_page) -> [cid]
    by_id = {}

    for c in chunks:
        by_id[c.cid] = c
        if c.book and c.dist:
            tail = c.quaestio if c.quaestio else c.ctype
            coords = (c.pars, c.sectio, c.art, tail)
            by_locus[(c.book, c.dist) + coords] = c.cid
            by_dist[(c.book, c.dist)].append((coords, c.cid))
        for p in c.pages:
            by_page[(c.volume, p)].append(c.cid)
    return by_locus, by_dist, by_page, by_id


# Which volumes are translated end-to-end. A physical-page ref into an INCOMPLETE
# volume is `forward` (it will resolve itself when that work is translated), not
# `dangling` (which asserts a defect). Vol V is 10 works of which only the
# Breviloquium is under way — most of its pages legitimately have no owner yet.
# ⭐ Vol V went True when its tenth and last work closed (2026-09-19); Vol VI
# opened the same day and is one pericope in, so nearly every page 1-634 has no
# owner yet and a ref into it must read `forward`, never `dangling`.
VOLUME_COMPLETE = {1: True, 2: True, 3: True, 4: True, 5: True, 6: False}


# ------------------------------------------------------------------ ordinal parsing


def parse_ordinal_run(words, ordinals):
    """'decimo octavo' == 'octavo decimo' == 18. Returns None if not a clean run."""
    vals = [ordinals[w.lower()] for w in words if w.lower() in ordinals]
    if not vals or len(vals) != len(words):
        return None
    if len(vals) == 1:
        return vals[0]
    if len(vals) == 2:
        tens = [v for v in vals if v >= 20 or v == 10]
        units = [v for v in vals if v < 10]
        if len(tens) == 1 and len(units) == 1:
            return tens[0] + units[0]
    return None


# ---------------------------------------------------------------------- scanners
# Each scanner yields dicts; the driver stamps chunk/section/anchor and resolves.


def clause_before(text, pos, window=300, splitter=CLAUSE_SPLIT_RE):
    seg = text[max(0, pos - window): pos]
    parts = splitter.split(seg)
    return parts[-1] if parts else seg


def governed_by_author(text, pos, sigla, chain=False):
    cl = clause_before(text, pos, window=500 if chain else 300,
                       splitter=CHAIN_SPLIT_RE if chain else CLAUSE_SPLIT_RE)
    return next((s for s in sigla if s in cl), None)


def scan_scripture_apparatus(text, cfg):
    """Form A/C: `Rom. 1, 20` · `Ps. 61, 12` · `I. Cor. 15, 54` · `Gen. 1` (chapter only)."""
    abbrev_map, meta = cfg["_abbrev_map"], cfg["_meta"]
    pat = re.compile(
        r"(?<![A-Za-zÀ-ÿ])((?:[IVX]{1,3}\.?\s+)?[A-Z][A-Za-z]{1,11}\.?)"
        r"\s*(\d{1,3})\s*(?:,\s*(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?)?"
    )
    for m in pat.finditer(text):
        key = abbrev_map.get(normalize_abbrev(m.group(1)))
        if not key:
            continue
        # `in Ioan.` = Augustine's tractates on John, not the gospel (INDEX-PLAN #4).
        pre = text[max(0, m.start() - 6): m.start()].lower()
        if pre.endswith("in ") or pre.endswith("super "):
            continue
        chap, verse = int(m.group(2)), (int(m.group(3)) if m.group(3) else None)
        # Abbreviations that collide with a non-scripture sense are admitted only in
        # their fully specified `C, V` form — see `require_verse` in scripture-books.json.
        if verse is None and meta[key].get("require_verse"):
            continue
        yield {
            "cls": "scripture",
            "sub": "apparatus-explicit",
            "book": key,
            "chapter": chap,
            "verse": verse,
            "verse_end": int(m.group(4)) if m.group(4) else None,
            "raw": m.group(0),
            "pos": m.start(),
            "conf": "A" if verse else "C",
            "over_chapters": chap > meta[key].get("chapters", 999),
        }


BOOK_UNNAMED_RE = re.compile(
    r"(?<![A-Za-z\u00c0-\u00ff])Libr\.\s*[IVX]{1,3}\.\s*\d{1,3}\s*,\s*\d{1,3}")


def scan_scripture_book_unnamed(text, cfg):
    """`Libr. II. 3, 1.` \u2014 a note that gives the BOOK NUMBER only, the book's NAME
    standing in the body (`dicitur in libro Machabaeorum`). Three are attested, all in
    the Collationes de septem donis, and the genre will keep producing them: a
    reportatio names its book aloud and the editor does not repeat it.

    It emits an UNRESOLVABLE record on purpose, as a barrier. Without it the citation
    is invisible to every scanner, and a following `ibid.` in the same note walks past
    it to the PREVIOUS note's verse and binds to the wrong BOOK \u2014 silently. Found at
    bon-don-c3 p. 472 n. 4, whose `ibid. 4, 23` (II Maccabees) was resolving to
    IV Kings 4:1, inherited from p. 472 n. 2. A wrong anchor is worse than none.

    `Libr. I. Reg. 12, 23` does NOT match: the book is named there, and the ordinary
    scripture scanner owns it.
    """
    for m in BOOK_UNNAMED_RE.finditer(text):
        yield {"cls": "scripture", "sub": "book-unnamed",
               "raw": m.group(0), "pos": m.start(), "conf": ""}


def scan_scripture_body(text, cfg):
    """Form B: `Ioannis decimo octavo` — ordinal chapter, verse supplied by the note."""
    body_map, meta, ordinals = cfg["_body_map"], cfg["_meta"], cfg["ordinals"]
    if not body_map:
        return
    forms = sorted(body_map, key=len, reverse=True)
    ow = "|".join(sorted(ordinals, key=len, reverse=True))
    # Two guards, both earned on the pilot sample:
    #  (1) a trailing letter-boundary — without it `actuum secundorum` ("of second
    #      acts") matched as `Actuum secundo` = Acts 2, because `secundo` is a prefix
    #      of `secundorum`;
    #  (2) CASE-SENSITIVE book forms. Several body forms are homographs of ordinary
    #      Latin nouns (`actuum`, `sapientiae`, `iob`), and Bonaventure sets a book
    #      name capitalised. Matching case-insensitively turns every such noun into a
    #      scripture citation.
    pat = re.compile(
        rf"(?<![A-Za-zÀ-ÿ])(?:ad\s+)?({'|'.join(map(re.escape, forms))})\s+"
        rf"((?:{ow})(?:\s+(?:{ow}))?)(?![A-Za-zÀ-ÿ])",
        re.IGNORECASE,
    )
    for m in pat.finditer(text):
        if not m.group(1)[0].isupper():
            continue
        key = body_map.get(m.group(1)) or body_map.get(m.group(1).capitalize())
        if not key:
            continue
        chap = parse_ordinal_run(m.group(2).split(), ordinals)
        if chap is None:
            continue
        yield {
            "cls": "scripture",
            "sub": "body-ordinal",
            "book": key,
            "chapter": chap,
            "verse": None,
            "verse_end": None,
            "raw": m.group(0),
            "pos": m.start(),
            "conf": "C",  # upgraded to B if an anchored `Vers. N` joins it
            "over_chapters": chap > meta[key].get("chapters", 999),
        }


LOCUS_TAIL = (
    r"(?:\s*p\.\s*(?P<pars>[IVX]+|\d+)\.?)?"
    r"(?:\s*sect\.\s*(?P<sectio>[IVX]+|\d+)\.?)?"
    r"(?:\s*a\.\s*(?P<art>\d+)\.?)?"
    r"(?:\s*(?P<qkind>q|dub|quaest|dubium)\.?\s*(?P<q>\d+)\.?)?"
)


def scan_sentences(text, cfg):
    """`II. Sent. d. 38. a. 1. q. 2` — logical cross-book locus (or an authority's)."""
    pat = re.compile(
        rf"(?:(?P<bk>{ROMAN_RE})\.?\s*)?Sent\.\s*d\.\s*(?P<dist>\d+)\.?{LOCUS_TAIL}"
    )
    for m in pat.finditer(text):
        author = governed_by_author(text, m.start(), cfg["_author_sigla"])
        d = m.groupdict()
        yield {
            "cls": "authority" if author else "crossref",
            "sub": "logical" if not author else f"authority:{author}",
            "book": ROMAN.get(d["bk"]) if d["bk"] else None,
            "dist": int(d["dist"]),
            "pars": roman_or_int(d["pars"]),
            "sectio": roman_or_int(d["sectio"]),
            "art": as_int(d["art"]),
            "q": as_int(d["q"]),
            "qkind": (d["qkind"] or "").rstrip("."),
            "raw": m.group(0).strip(),
            "pos": m.start(),
        }


SENT_LOCUS_RE = re.compile(
    rf"(?:(?P<bk>{ROMAN_RE})\.?\s*)?Sent\.\s*d\.\s*(?P<dist>\d+)\.?{LOCUS_TAIL}"
)
# Same shape, but introduced by a relative marker, so it carries NO book of its own
# (`bk` is absent -> the citing chunk's book is used).
REL_LOCUS_RE = re.compile(
    rf"\b(?:supra|infra)\.?\s*d\.\s*(?P<dist>\d+)\.?{LOCUS_TAIL}"
)


def last_locus_before(text, pos):
    """The most recent full `N. Sent. d. N …` locus before `pos`, or None.

    `ibid.` and a book-less `d. N` inherit from it. Without this a Vol V chunk's
    `ibid. d. 9. a. 1. q. 1` has no book to fall back on (work chunks carry no
    `book:` frontmatter) and every one reads as unresolvable.
    """
    # A locus inside a CLOSED parenthesis is an aside, not the chain's governor:
    #   `Cfr. de his II. Sent., in quo d. 17 …; d. 16. per totam (cfr. I. Sent. d. 3.
    #    p. II. a. 1. q. 1.), …; d. 25. p. I. …`
    # Here `d. 25` continues Book II; letting the parenthetical `I. Sent.` win moved
    # it to Book I. Skip any candidate whose parenthesis has already closed.
    spans = []
    depth, start = 0, None
    for i, ch in enumerate(text[:pos]):
        if ch == "(":
            if depth == 0:
                start = i
            depth += 1
        elif ch == ")" and depth:
            depth -= 1
            if depth == 0 and start is not None:
                spans.append((start, i))

    def parenthetical(q):
        return any(a < q < b for a, b in spans)

    # Inheritance follows the nearest preceding locus of ANY form. A `supra`/`infra
    # d. N` states the citing chunk's own book (bk=None -> falls back to it), and a
    # chain hanging off one — `explicat infra d. 45. a. 2. q. 1.; cfr. etiam d. 22.
    # …; d. 27. …` — must not reach past it to some far-earlier `III. Sent.`.
    last, last_is_rel = None, False
    for rx, is_rel in ((SENT_LOCUS_RE, False), (REL_LOCUS_RE, True)):
        for m in rx.finditer(text, 0, pos):
            if parenthetical(m.start()):
                continue
            if last is None or m.start() > last.start():
                last, last_is_rel = m, is_rel
    if not last:
        return None
    d = last.groupdict()
    d.setdefault("bk", None)
    d["_pos"] = last.start()
    d["_rel"] = last_is_rel
    return d


def author_between(text, start, end, sigla):
    """The author siglum (if any) named BETWEEN the inherited locus and this one.

    This is the discriminator for a citation chain that changes hands mid-note.
    `— B. Albert., hic a. 1. et d. 46. a. 11.` names a new author after the previous
    locus, so the continuation is Albert's. By contrast `Aristot., II Topic. c. 3 …,
    idem recurrit infra d. 8 … et d. 37 …` names its author BEFORE the locus the
    chain hangs off, so the continuation is still Bonaventure's own — the editors
    say *supra*/*infra* only of his work, never of another doctor's.
    """
    seg = text[start:end]
    hits = [(seg.rfind(s), s) for s in sigla if s in seg]
    hits = [h for h in hits if h[0] >= 0]
    return max(hits)[1] if hits else None


def scan_chain_continuation(text, cfg):
    """`Vide II. Sent. d. 2. p. II. a. 1. q. 1; d. 14. p. I. a. 1. q. 1.` — a chain
    that states `Sent.` ONCE and then lists further distinctions bare.

    Without this the second and later loci of every such chain are dropped: in the
    note above, two of three references were invisible to the ledger.
    """
    pat = re.compile(rf"(?<![.\w])d\.\s*(?P<dist>\d+)\.?{LOCUS_TAIL}")
    for m in pat.finditer(text):
        pre = text[max(0, m.start() - 14): m.start()]
        # Already owned by scan_sentences (`Sent. d. N`) or scan_relative
        # (`supra|infra|ibid d. N`).
        if re.search(r"Sent\.\s*$|(?:supra|infra|ibid)\.?\s*$", pre, re.I):
            continue
        prev = last_locus_before(text, m.start())
        if not prev:
            continue  # no governing book anywhere before it — never guess one
        # Governance is checked at the continuation's OWN position first: a chain can
        # start a new author mid-note (`— B. Albert., hic a. 1. et d. 46. a. 11.`),
        # where the inherited locus belongs to Bonaventure but the continuation does
        # not. Fall back to the inherited locus's governance.
        #
        # EXCEPT when the chain hangs off a `supra`/`infra` locus. The editors say
        # *supra*/*infra* only of Bonaventure's OWN work, never of another doctor's,
        # so such a chain is self-referential no matter which siglum stands nearby.
        # Without this, `Aristot., II Topic. c. 3 …, idem recurrit infra d. 8 … et
        # d. 37 …` and `S. Bonav. … in sensu S. Thom. ipse explicat infra d. 45 …;
        # d. 35. q. 2.` both lost real self-references to the authority class.
        author = author_between(text, prev["_pos"], m.start(), cfg["_author_sigla"])
        if author is None and not prev.get("_rel"):
            author = governed_by_author(text, prev["_pos"], cfg["_author_sigla"], chain=True)
        d = m.groupdict()
        yield {
            "cls": "authority" if author else "crossref",
            "sub": f"authority:{author}" if author else "chain-continuation",
            "book": ROMAN.get(prev["bk"]) if prev["bk"] else None,
            "dist": int(d["dist"]),
            "pars": roman_or_int(d["pars"]), "sectio": roman_or_int(d["sectio"]),
            "art": as_int(d["art"]), "q": as_int(d["q"]),
            "qkind": (d["qkind"] or "").rstrip("."),
            "raw": m.group(0).strip(), "pos": m.start(),
        }


# Ruling 57 (C1): the coordinates printed after a lower-case `ibid.` — `ibid. 41, 3`,
# `ibid. 1, 20-22`, `ibid. v. 11`, `ibid v. 22` (point dropped). Matched from just
# after the four letters `ibid`, so `ibidem` never qualifies. A bare number
# (`ibid. 54.`) is NOT matched: it may be a chapter or a verse, and guessing which
# is exactly what this ledger refuses to do — those stay with the bare-`ibid.` rule.
IBID_COORD_RE = re.compile(
    r"\.?\s*(?:v\.\s*(?P<v>\d{1,3})(?:\s*[-–]\s*(?P<vend>\d{1,3}))?"
    r"|(?P<c>\d{1,3})\s*,\s*(?P<cv>\d{1,3})(?:\s*[-–]\s*(?P<cvend>\d{1,3}))?)(?!\d)")


def scan_relative(text, cfg):
    """`supra d. 12` · `infra d. 43` · `ibid. d. 14` — same-book relative locus."""
    pat = re.compile(
        rf"\b(?P<rel>supra|infra|ibid|loc\. cit)\.?\s*(?:d\.\s*(?P<dist>\d+)\.?{LOCUS_TAIL})?"
    )
    for m in pat.finditer(text):
        d = m.groupdict()
        if not d["dist"]:
            if not d["rel"].lower().startswith(("loc", "ibid")):
                continue
            # `ibid. pag. 321, nota 4` inherits a TOME, not a locus — the page
            # scanner owns it. Emitting a locus record here duplicated the
            # preceding citation and pointed it at the wrong thing.
            if re.match(r"\.?\s*(?:pag|tom)\.", text[m.end(): m.end() + 8]):
                continue
            # Ruling 57 (C1): `ibid. 41, 3` / `ibid. v. 11` prints its OWN coordinates.
            # It is a scripture anaphor whose BOOK (and, for `v. N`, chapter) is
            # inherited and whose C:V is its own — never a Sentences inheritance, and
            # never a copy of the antecedent's verse. Resolved in resolve_anaphora().
            cm = (IBID_COORD_RE.match(text, m.start("rel") + 4)
                  if d["rel"] == "ibid" else None)
            if cm:
                yield {"cls": "crossref", "sub": "relative-bare", "dist": None,
                       "raw": text[m.start(): cm.end()].strip(), "pos": m.start(),
                       "rel": d["rel"], "ibid_coords": {
                           "chapter": as_int(cm.group("c")),
                           "verse": as_int(cm.group("v") or cm.group("cv")),
                           "verse_end": as_int(cm.group("vend") or cm.group("cvend")),
                           "kind": "v" if cm.group("v") else "cv"}}
                continue
            prev = (last_locus_before(text, m.start())
                    if d["rel"].lower().startswith("ibid") else None)
            if not prev:
                # Nothing to inherit — genuinely unresolvable, and recorded as such.
                yield {"cls": "crossref", "sub": "relative-bare", "dist": None,
                       "raw": m.group(0).strip(), "pos": m.start(), "rel": d["rel"]}
                continue
            # `ibid.` inherits the GOVERNANCE of the locus it inherits from, not just
            # its coordinates: `Richard. a Med. … II. Sent. d. 23 …; ibid. d. 24. a. 3.
            # q. 5` is still Richard's numbering, not Bonaventure's.
            inherited_author = governed_by_author(text, prev["_pos"], cfg["_author_sigla"], chain=True)
            yield {
                "cls": "authority" if inherited_author else "crossref",
                "sub": f"authority:{inherited_author}" if inherited_author else "relative-inherited",
                "rel": d["rel"],
                "book": ROMAN.get(prev["bk"]) if prev["bk"] else None,
                "dist": int(prev["dist"]),
                "pars": roman_or_int(prev["pars"]), "sectio": roman_or_int(prev["sectio"]),
                "art": as_int(prev["art"]), "q": as_int(prev["q"]),
                "qkind": (prev["qkind"] or "").rstrip("."),
                "raw": m.group(0).strip(), "pos": m.start(),
            }
            continue
        # `supra`/`infra` are intra-WORK relative — they always mean the citing
        # chunk's own book and must NOT inherit a book from a preceding citation.
        # (`infra d. 17. p. I. q. 4` in a Book I chunk, standing after a `III. Sent.`
        # reference, means Book I d. 17 — inheriting `III` made it read as dangling.)
        # `ibid. d. N` is the opposite: it explicitly points back at the last-named
        # book, which a Vol V work chunk has no `book:` of its own to supply.
        prev = last_locus_before(text, m.start()) if d["rel"].startswith("ibid") else None
        author = (governed_by_author(text, prev["_pos"], cfg["_author_sigla"], chain=True)
                  if prev else None)
        yield {
            "cls": "authority" if author else "crossref",
            "sub": f"authority:{author}" if author else "relative",
            "rel": d["rel"],
            "book": ROMAN.get(prev["bk"]) if prev and prev["bk"] else None,
            "dist": int(d["dist"]),
            "pars": roman_or_int(d["pars"]), "sectio": roman_or_int(d["sectio"]),
            "art": as_int(d["art"]), "q": as_int(d["q"]),
            "qkind": (d["qkind"] or "").rstrip("."),
            "raw": m.group(0).strip(), "pos": m.start(),
        }


def scan_page(text, cfg):
    """`supra pag. 120, nota 11` · `tom. III. pag. 773, nota 5` — physical-page locus."""
    pat = re.compile(
        # `tom\.?` — Quaracchi occasionally drops the abbreviating point (`bon-hex-c5`
        # p. 355 n. 1 `tom IV. pag. 107`); without it the tome was lost and the page
        # resolved into the CITING volume (mysterio Trinitatis work-close gate).
        rf"(?:\btom\.?\s+(?P<tom>{ROMAN_RE})\.?\s*)?"
        rf"(?:(?P<rel>supra|infra)\s+)?(?P<ibid>[Ii]bid\.?\s+)?pag\.\s*(?P<page>\d{{1,4}})"
        r"(?:\s*,\s*nota\s*(?P<nota>\d+))?"
    )
    # `(?![IVX])`: without it ROMAN_RE's first alternative takes the `I` of `IV`/`IX`
    # and stops, so `tom. IV. … pag. 103` inherited tome I (work-close gate, 2026-09-15).
    tom_lookback = re.compile(rf"\btom\.?\s+({ROMAN_RE})(?![IVX])\.?")
    book_lookback = re.compile(rf"({ROMAN_RE})\.?\s*Sent\.")
    for m in pat.finditer(text):
        d = m.groupdict()
        tom = ROMAN.get(d["tom"]) if d["tom"] else None
        if tom is None and d["ibid"]:
            # `Vide II. Sent. d. 2 …; cfr. ibid. pag. 321, nota 4` — `ibid.` points at
            # the tome of the last-named Sentences book, NOT at the citing volume.
            lb = book_lookback.findall(text[:m.start()])
            if lb:
                tom = ROMAN.get(lb[-1])
            else:
                # `… allatam tom. II. pag. 506, nota 3. Cfr. ibid. pag. 700, nota 1`
                # (bon-don-c2, p. 465 n. 2): `ibid.` can point back at a bare
                # `tom. N.` with no `Sent.` anywhere in the note. Without this the
                # tome falls through to the CITING volume and the reference is
                # reported as a forward reference inside Vol V, which is wrong.
                lb = tom_lookback.findall(text[:m.start()])
                if lb:
                    tom = ROMAN.get(lb[-1])
        if tom is None and not d["rel"]:
            # A bare `pag. 738, nota 4` inherits the `tom. N` named earlier in the same
            # note — Quaracchi states the tome once and then lists pages. Without this
            # lookback every such page is measured against the CITING volume and reads
            # as dangling. `supra pag.` is explicitly same-volume and never inherits.
            # `;` separates pages of the SAME stated tome (`tom. IV. pag. 102, nota 3;
            # pag. 103, nota 10` — `bon-qmt-q5-a2` p. 93 n. 2), so this lookback uses the
            # CHAIN splitter, which stops only at `—`, `Cfr.`, `Vide` (work-close gate,
            # 2026-09-15). Stopping at `;` sent such pages into the citing volume.
            lb = tom_lookback.findall(clause_before(text, m.start(), window=400,
                                                    splitter=CHAIN_SPLIT_RE))
            if lb:
                tom = ROMAN.get(lb[-1])
        yield {
            "cls": "crossref", "sub": "page",
            "tom": tom, "explicit_tom": bool(d["tom"]),
            "page": int(d["page"]), "nota": as_int(d["nota"]),
            "raw": m.group(0).strip(), "pos": m.start(),
        }


def scan_work(text, cfg):
    """`Breviloq. p. V. c. 6` · `Itiner. c. 1` — work-relative locus."""
    for entry in cfg["works"]["entries"]:
        for ab in entry["abbrev"]:
            pat = re.compile(
                re.escape(ab)
                + r"(?:\s*p\.\s*(?P<pars>[IVX]+|\d+)\.?)?"
                + r"(?:\s*(?:c|coll|q)\.\s*(?P<cap>\d+)\.?)?"
            )
            for m in pat.finditer(text):
                yield {
                    "cls": "crossref", "sub": "work",
                    "work": entry["slug"], "pattern": entry["chunk_pattern"],
                    "pars": roman_or_int(m.group("pars")),
                    "cap": as_int(m.group("cap")),
                    "raw": m.group(0).strip(), "pos": m.start(),
                }


def roman_or_int(v):
    if v is None:
        return None
    v = str(v).strip().rstrip(".")
    return ROMAN.get(v.upper(), as_int(v))


# ---------------------------------------------------------------------- resolution


def resolve_locus(rec, citing, by_locus, by_dist):
    """Logical/relative locus -> chunk id, with an honest resolution level."""
    book = rec.get("book") or citing.book
    dist = rec.get("dist")
    if book is None or dist is None:
        return "", "unresolvable"

    qkind = rec.get("qkind") or ""
    tail = rec.get("q")
    if qkind.startswith("dub"):
        # The corpus holds ONE `-dubia` chunk per distinction/pars carrying all its
        # dubia, so `dub. 4` names a unit INSIDE that chunk. Per the frozen rule
        # (granularity = chunk id) the number is display text on the link, not a
        # match coordinate — using it as one made every `dub. N` read as dangling.
        tail = "dubia"

    siblings = by_dist.get((book, dist), [])
    if not siblings:
        return "", "dangling"

    # A citation naming neither a question nor an article addresses the whole
    # distinction (`d. 2. per totam`). Stop there honestly rather than picking a chunk.
    if tail is None and rec.get("art") is None:
        return f"{BOOK_ROMAN.get(book, book)}:d{dist}", "distinctio"

    # Wildcard match: Quaracchi routinely OMITS a coordinate that is unambiguous in
    # the print — `IV. Sent. d. 15. p. I. q. 1` means p1-a1-q1, because that pars has
    # a single articulus. Treat every unstated coordinate as a wildcard and require a
    # UNIQUE survivor; more than one survivor is ambiguity, not a resolution.
    want = (rec.get("pars"), rec.get("sectio"), rec.get("art"), tail)
    hits = [cid for coords, cid in siblings
            if all(w is None or w == g for w, g in zip(want, coords))]
    if len(hits) == 1:
        return hits[0], "chunk"
    if len(hits) > 1:
        # An article named without a question addresses the whole article — the
        # article-level analogue of `d. N per totam`, not an ambiguity.
        level = "articulus" if tail is None else "ambiguous"
        return "+".join(sorted(hits)), level
    return "", "dangling"


def resolve_page(rec, citing, by_page):
    vol = rec.get("tom") or citing.volume
    ids = by_page.get((vol, rec["page"]), [])
    if len(ids) == 1:
        return ids[0], "chunk"
    if len(ids) > 1:
        return "+".join(ids), "page-multi"
    if not VOLUME_COMPLETE.get(vol, False):
        # The volume is only partly translated; this page has no owner YET.
        return f"tom{vol}:p{rec['page']}", "forward"
    return "", "dangling"


def resolve_work(rec, by_id):
    pat, pars, cap = rec["pattern"], rec.get("pars"), rec.get("cap")
    if cap is None:
        # A work named without a chapter (`Quaest. de scientia Christi`) addresses the
        # whole work — the work-level analogue of `d. N per totam`, not a failure.
        return f"work:{rec['work']}", "work"
    if "{pars}" in pat:
        if pars is None:
            return "", "unresolvable"
        cid = pat.format(pars=pars, cap=cap)
    else:
        cid = pat.replace("{cap}", str(cap)).replace("{coll}", str(cap)).replace(
            "{n}", str(cap)).replace("{q}", str(cap))
    if cid in by_id:
        return cid, "chunk"
    return cid, "forward"


# -------------------------------------------------------------------------- driver


def nearest_anchor(text, pos, window=60):
    m = ANCHOR_RE.search(text, pos, pos + window)
    return m.group(1) if m else ""


VERS_RE = re.compile(r"\bVers\.\s*(\d{1,3})")


# NOTE: Migne's anaphor set includes `Id.`/`Idem`; DO NOT port those two here. In
# Quaracchi's Latin `id` and `idem` are ordinary pronouns ("id est", "idem est"), and
# admitting them turned 88 anaphors into 823 in a 148-chunk pilot. Quaracchi's
# anaphoric forms are `Ibid.` and `loc. cit.` only.
def _closed_paren_spans(text, end):
    """(start, stop) of every parenthesis that has CLOSED before `end`."""
    spans, depth, start = [], 0, None
    for i, ch in enumerate(text[:end]):
        if ch == "(":
            if depth == 0:
                start = i
            depth += 1
        elif ch == ")" and depth:
            depth -= 1
            if depth == 0 and start is not None:
                spans.append((start, i))
    return spans


TARGET_BC_RE = re.compile(r"^(\S+) (\d+)")


def _book_chapter(target):
    m = TARGET_BC_RE.match(target or "")
    return (m.group(1), int(m.group(2))) if m else None


def _skip_as_antecedent(p):
    """Records a coordinate `ibid.` may not inherit from: an unresolved anaphor, or a
    BARE anaphor (rule 2 — a bare `ibid.` only copies, so inheriting through it
    drifts). A RESOLVED coordinate `ibid.` IS a valid antecedent: its chapter is its
    own (`Rom. 5, 12; ibid. 6, 23; ibid. v. 9` is Rom 6:9, not Rom 5:9)."""
    if p["subclass"] == "relative-bare":
        return True
    return bool(p["ibid_resolved"]) and not p.get("_coords")


# The printed slips of ruling 37/48 (C2 of ruling 57): Quaracchi's own wrong book,
# chapter or verse, transcribed as printed. The ledger FILES THEM AS PRINTED — the
# index is derived from the text and never emends it — and each gets a QA line
# naming the true passage, so the slip is visible rather than silently indexed.
# Keyed narrowly: (chunk, section, anchor label, filed target) must match EXACTLY ONE
# record; a stale or ambiguous entry is itself reported. Add a row only for a slip
# a chunk's Notes have recorded and a gate has ruled on.
PRINTED_SLIPS = [
    # chunk, section, anchor, target as filed, the passage meant, where recorded
    ("bon-sap-c1", "apparatus:p115-6", "p115-6", "Iob 6:2", "Iob 6:25",
     "ruling 37 — p. 115 n. 6 prints `Iob 6, 2`"),
    ("bon-sap-c3", "apparatus:p126-1", "p126-1", "Iob 24:19", "Iob 5:19",
     "ruling 57/C2 — p. 126 n. 1 prints `Iob 24, 19`"),
    ("bon-sap-c5", "latin_body", "p140-3", "Cor* 12:30", "1Cor 12:31",
     "ruling 57/C2 — body `ad Corinthios duodecimo` + n. 3 `Vers. 30`"),
    ("bon-sap-c11", "latin_body", "", "Prov 16", "Prov 24:16",
     "ruling 57/C2 — body p. 180 `Proverbiorum decimo sexto` (n. 9 gives 24, 16)"),
    ("bon-sap-c16", "latin_body", "p213-4", "Eccli 11:3", "Eccle 11:3",
     "ruling 48 — body p. 213 `Ecclesiastici undecimo` for Ecclesiastes"),
    ("bon-sap-c18", "latin_body", "p226-5", "Ezech 20:30", "Ezech 22:30",
     "ruling 48 — body p. 226 `Ezechielis vigesimo` + n. 5 `Vers. 30`"),
]


def apply_printed_slips(rows):
    """Annotate (never correct) the C2 printed slips. Returns QA-note tuples."""
    notes = []
    for cid, sec, lab, filed, meant, why in PRINTED_SLIPS:
        hits = [r for r in rows if r["chunk_id"] == cid and r["section"] == sec
                and r["anchor_label"] == lab and r["normalized_target"] == filed]
        if len(hits) == 1:
            notes.append((cid, sec, hits[0]["raw_text"],
                          f"printed slip, filed as printed at `{filed}`; the passage is "
                          f"`{meant}` ({why})"))
        else:
            notes.append((cid, sec, filed,
                          f"⚠ PRINTED_SLIPS entry matched {len(hits)} records (expected 1) "
                          f"— the table is stale; fix the entry, not the chunk"))
    return notes


def resolve_coord_ibid(i, r, chunk_rows, sections, cfg, qa):
    """Ruling 57 (C1). `ibid. C, V` takes the antecedent's BOOK and its own C:V;
    `ibid. v. N` the antecedent's book AND chapter and its own verse. The antecedent,
    in order of preference — and if none qualifies the record is LEFT UNRESOLVABLE,
    never guessed:

      (a) the nearest preceding SCRIPTURE locus in the SAME note, walking past a
          non-scripture or Sentences locus (`IV. Sent. d. 15 …; ibid. 5, 3` is not a
          Sentences reference: Sentences coordinates always carry `d.`). A locus inside
          a parenthesis that has closed is an aside and never governs (index rule 3).
          An author siglum named between that locus and the `ibid.` hands the chain
          to that author (index rule 5) — unresolvable. A `Libr. II. 3, 1` barrier
          (book named only in the body) stops the walk — unresolvable.
      (b) the BODY-ORDINAL join through the note's own anchor: `Vers. 21; ibid. 6, 3`
          — the note's first locus is the body's `<Book> <ordinal>`[^n], which is a
          body record, not a note record. One body book only; for `v. N` one chapter.
      (c) only when the `ibid.` OPENS its note (nothing numeric before it), the
          previous apparatus note's last citation, if it is scripture. A note that
          already has an uncaptured locus of its own (`Cap. 10, 4. Ibid. …`, `Vers.
          N; ibid. …` with no body join) is not allowed to reach across the boundary:
          that is how c12 p. 186 n. 2 became Ps 73:12 instead of Gen 6:3.
    """
    sec = r["section"]
    text = sections.get(sec) or ""
    pos = r["_order"][1]
    sigla = cfg["_author_sigla"]
    co = r["_coords"]
    spans = _closed_paren_spans(text, pos)
    # An author named inside a closed parenthesis is an aside too (`Comment. in Epist.
    # ad Rom. 7, 18. (inter opera S. Ambros.). Seq. locus est ibid. v. 22.`): mask
    # those spans before testing governance.
    atext = list(text)
    for a, b in spans:
        atext[a:b + 1] = " " * (b + 1 - a)
    atext = "".join(atext)
    ant, how = None, ""

    # (a) same note
    for j in range(i - 1, -1, -1):
        p = chunk_rows[j]
        if p["section"] != sec:
            break
        # A `loc. cit.` between the locus and the `ibid.` points somewhere the note
        # does not say (III d9 a1 q5 n. 4: `Psalm. 5, 8. — … loc. cit. v. 17. Cfr.
        # ibid. 6, 19` is I Cor 6:19, not Ps 6:19). The chain is unreadable: stop.
        if p["raw_text"].lower().startswith("loc"):
            r["_why"] = "a `loc. cit.` intervenes"
            return False
        if _skip_as_antecedent(p):
            continue
        ppos = p["_order"][1]
        if any(a < ppos < b for a, b in spans):
            continue
        if p["subclass"] == "book-unnamed":
            r["_why"] = "book named only in the body (`Libr. N.` barrier)"
            return False
        if p["class"] != "scripture":
            continue
        if author_between(atext, p["_end"], pos, sigla):
            r["_why"] = f"author `{author_between(atext, p['_end'], pos, sigla)}` named between"
            return False
        ant, how = p, "note"
        break

    if ant is None and sec.startswith("apparatus:"):
        who = author_between(atext, 0, pos, sigla)
        if who:
            r["_why"] = f"no scripture locus in the note; author `{who}` named before it"
            return False
        # (b) body-ordinal join
        label = sec.split(":", 1)[1]
        body = [p for p in chunk_rows if p["section"] == "latin_body"
                and p["subclass"] == "body-ordinal" and p["anchor_label"] == label]
        # `ibid. C, V` needs only the body's BOOK; `ibid. v. N` needs its chapter too.
        def join_key(p):
            bcj = _book_chapter(p["normalized_target"])
            if bcj is None:
                return None
            return bcj if co["kind"] == "v" else bcj[0]
        keys = {join_key(p) for p in body}
        if len(keys) == 1 and None not in keys:
            ant, how = body[0], "body"
        elif len(keys) > 1:
            r["_why"] = f"body join through [^{label}] names {len(keys)} different loci"
            return False
        # (c) the `ibid.` opens its note: inherit across the note boundary
        elif not re.search(r"\d", text[:pos]):
            for j in range(i - 1, -1, -1):
                p = chunk_rows[j]
                if not p["section"].startswith("apparatus:"):
                    break
                if p["raw_text"].lower().startswith("loc"):
                    r["_why"] = "opens its note; a `loc. cit.` precedes it"
                    return False
                if _skip_as_antecedent(p):
                    continue
                if p["class"] == "scripture" and p["subclass"] != "book-unnamed" \
                        and _book_chapter(p["normalized_target"]):
                    ant, how = p, "prev-note"
                else:
                    r["_why"] = "opens its note; the previous note's last citation is not scripture"
                    return False
                break
            if ant is None:
                r["_why"] = "no-antecedent"   # may still chain across chunks
                return False
        else:
            r["_why"] = "the note has a locus of its own the ledger did not capture"
            return False

    if ant is None:
        r["_why"] = r.get("_why") or "no scripture antecedent"
        return False
    return apply_coord_ibid(r, ant, how, cfg, qa)


def apply_coord_ibid(r, ant, how, cfg, qa, cross_chunk_prefix=""):
    bc = _book_chapter(ant["normalized_target"])
    if not bc:
        r["_why"] = "antecedent has no book"
        return False
    book, ach = bc
    co = r["_coords"]
    chap = ach if co["kind"] == "v" else co["chapter"]
    tgt = f"{book} {chap}:{co['verse']}"
    if co.get("verse_end"):
        tgt += f"-{co['verse_end']}"
    res = "verse"
    if chap > cfg["_meta"].get(book, {}).get("chapters", 999):
        res = "chapter-out-of-range"
        qa.append((r["chunk_id"], r["section"], r["raw_text"],
                   f"chapter {chap} exceeds {book}'s "
                   f"{cfg['_meta'][book].get('chapters')} — digit-confusion candidate"))
    r["class"] = "scripture"
    r["subclass"] = "anaphor->" + ant["subclass"].replace("anaphor->", "")
    r["normalized_target"] = tgt
    r["confidence"] = "B" if how == "body" else "A"
    r["resolution"] = res
    r["ibid_resolved"] = "cross-chunk" if cross_chunk_prefix else "yes"
    tag = {"body": "body: ", "prev-note": "prev note: "}.get(how, "")
    r["antecedent"] = (cross_chunk_prefix + tag + ant["raw_text"])[:60]
    r["_why"] = ""
    return True


def resolve_anaphora(chunk_rows, sections=None, cfg=None, qa=None):
    """Resolve bare `ibid.` / `loc. cit.` / `Id.` against the printed sequence.

    Ported from ~/patrologia `scripts/index-work.mjs` (Migne rule 9), which solved this
    first. The rules, and why each one matters here:

      1. **Document order is the only key.** An anaphor carries no target by nature, so
         it can be resolved at index time and never afterwards from the display string.
      2. **Resolve to the nearest preceding NON-anaphoric citation, walking past
         already-resolved anaphors** — otherwise a run of `ibid.`s chains onto itself
         and drifts.
      3. **An anaphor inherits its antecedent's BUCKET**, not just its target. A
         scripture `ibid.` is a scripture record; an `ibid.` after Augustine is an
         authority record and is correctly EXCLUDED rather than counted as a failure.
         This replaces guessing from surrounding words with reading the sequence.
      4. **The text is never rewritten.** `raw_text` keeps Quaracchi's `ibid.` verbatim;
         the inheritance is recorded in `ibid_resolved` / `antecedent`. It is an
         INFERENCE, not a correction, and must never read as an emendation of Quaracchi.
      5. **An anaphor with nothing before it is a real, countable failure** — reported,
         not hidden. It usually means a preceding citation failed to parse.

    Scoped to the chunk: an `ibid.` opening apparatus entry `[^16]` refers back to
    `[^15]`, which a per-entry lookback structurally cannot see. That blind spot was
    31% of this corpus's unresolved anaphora.
    """
    unresolved = 0
    for i, r in enumerate(chunk_rows):
        if r["subclass"] != "relative-bare":
            continue
        if r.get("_coords"):
            if sections is None or not resolve_coord_ibid(i, r, chunk_rows, sections, cfg, qa):
                unresolved += 1
            continue
        ant = None
        for j in range(i - 1, -1, -1):
            p = chunk_rows[j]
            if p["subclass"] != "relative-bare" and not p["ibid_resolved"]:
                ant = p
                break
        if ant is None:
            unresolved += 1
            continue
        r["class"] = ant["class"]
        r["subclass"] = f"anaphor->{ant['subclass']}"
        r["normalized_target"] = ant["normalized_target"]
        r["confidence"] = ant["confidence"]
        r["resolution"] = ant["resolution"]
        r["ibid_resolved"] = "yes"
        r["antecedent"] = ant["raw_text"][:60]
    return unresolved


def resolve_anaphora_across_chunks(chunks, per_chunk, cfg=None, qa=None):
    """Second pass: an `ibid.` opening a chunk's apparatus can point into the PREVIOUS
    chunk's footer, because a printed page's footnote register routinely splits across
    a chunk boundary ("per-page footer splits are the NORM" — repo CLAUDE.md).

    Deliberately narrow, so this reads a recorded fact instead of guessing an order:

      * **Apparatus entries only.** A scholion's or a running body's `ibid.` belongs to
        a different discourse; the previous chunk's scholion is a different scholion.
      * **Only when the two chunks SHARE a printed page** — that is what makes them one
        footnote register rather than two adjacent ones. Chunk order comes from
        `printed_pages`, which is recorded per chunk, not inferred from ids.
      * **Marked `cross-chunk`, not `yes`.** A cross-chunk inheritance is a weaker claim
        than a within-chunk one and must stay separately auditable.

    Measured on the full corpus: of 259 unresolved anaphora, 127 are in apparatus, and
    94 of those share a page with their predecessor. The other 165 are left alone.
    """
    order = {}
    for c in chunks:
        if c.pages:
            order.setdefault(c.volume, []).append(c)
    for v in order:
        order[v].sort(key=lambda c: (min(c.pages), c.cid))

    prev_of = {}
    for lst in order.values():
        for i in range(1, len(lst)):
            prev_of[lst[i].cid] = lst[i - 1]

    for c in chunks:
        prev = prev_of.get(c.cid)
        if not prev or not (set(c.pages) & set(prev.pages)):
            continue
        tail = None
        for r in reversed(per_chunk.get(prev.cid, [])):
            if not r["subclass"].startswith("relative-bare") and r["ibid_resolved"] != "cross-chunk":
                tail = r
                break
        if tail is None:
            continue
        for r in per_chunk.get(c.cid, []):
            if r["subclass"] != "relative-bare" or r["ibid_resolved"]:
                continue
            if not r["section"].startswith("apparatus:"):
                continue
            if r.get("_coords"):
                # Ruling 57: a coordinate `ibid.` crosses a chunk boundary only on the
                # same terms as a note boundary — it opened its note and found no
                # antecedent in this chunk at all — and only onto a scripture locus.
                if r.get("_why") == "no-antecedent":
                    if tail["class"] == "scripture" and tail["subclass"] != "book-unnamed":
                        apply_coord_ibid(r, tail, "prev-note", cfg, qa,
                                         cross_chunk_prefix=f"{prev.cid}: ")
                    else:
                        r["_why"] = "opens the chunk's first note; the previous chunk's last citation is not scripture"
                continue
            r["class"] = tail["class"]
            r["subclass"] = f"anaphor->{tail['subclass'].replace('anaphor->', '')}"
            r["normalized_target"] = tail["normalized_target"]
            r["confidence"] = tail["confidence"]
            r["resolution"] = tail["resolution"]
            r["ibid_resolved"] = "cross-chunk"
            r["antecedent"] = f"{prev.cid}: {tail['raw_text'][:48]}"

    return sum(1 for rs in per_chunk.values() for r in rs
               if r["subclass"] == "relative-bare" and not r["ibid_resolved"])


def extract(chunks, cfg, by_locus, by_dist, by_page, by_id):
    rows, qa = [], []
    per_chunk = {}
    scanners = (scan_scripture_apparatus, scan_scripture_book_unnamed,
                scan_scripture_body,
                scan_sentences, scan_chain_continuation, scan_relative,
                scan_page, scan_work)

    for c in chunks:
        # DOCUMENT ORDER is the resolution key for anaphora, so records are collected
        # per chunk and sorted before the `ibid.` pass runs. Apparatus entries arrive
        # from split_sections in file order, which is Quaracchi's printed order.
        sections = [("latin_body", c.latin_body), ("scholion", c.scholion)]
        # Translator's notes (`tr-` labels) are our voice, not Quaracchi's: never indexed
        # (ruling 24, Vol VI Ecclesiastes work-close gate, 2026-10-11).
        sections += [(f"apparatus:{lab}", txt) for lab, txt in c.apparatus.items()
                     if not lab.startswith("tr-")]
        chunk_rows = []

        for sec_i, (section, text) in enumerate(sections):
            if not text:
                continue
            is_app = section.startswith("apparatus:")
            app_label = section.split(":", 1)[1] if is_app else ""

            for scanner in scanners:
                # Body ordinals are a body phenomenon; apparatus never uses them.
                if scanner is scan_scripture_body and is_app:
                    continue
                for rec in scanner(text, cfg):
                    anchor = app_label if is_app else nearest_anchor(text, rec["pos"] + len(rec["raw"]))

                    # Tier B join: body chapter + anchor -> apparatus `Vers. N`.
                    if rec.get("sub") == "body-ordinal" and anchor and anchor in c.apparatus:
                        vm = VERS_RE.search(c.apparatus[anchor])
                        if vm:
                            rec["verse"] = int(vm.group(1))
                            rec["conf"] = "B"

                    if rec["sub"] == "book-unnamed":
                        tgt, res, conf = "", "unresolvable", ""
                    elif rec["cls"] == "scripture":
                        tgt = f"{rec['book']} {rec['chapter']}"
                        if rec.get("verse"):
                            tgt += f":{rec['verse']}"
                            if rec.get("verse_end"):
                                tgt += f"-{rec['verse_end']}"
                        res = "verse" if rec.get("verse") else "chapter"
                        if rec.get("over_chapters"):
                            res = "chapter-out-of-range"
                            qa.append((c.cid, section, rec["raw"],
                                       f"chapter {rec['chapter']} exceeds {rec['book']}'s "
                                       f"{cfg['_meta'][rec['book']].get('chapters')} — digit-confusion candidate"))
                        conf = rec["conf"]
                    elif rec["cls"] == "authority":
                        tgt, res, conf = "", "excluded", ""
                    elif rec["sub"] in ("logical", "relative", "relative-inherited",
                                        "chain-continuation"):
                        tgt, res = resolve_locus(rec, c, by_locus, by_dist)
                        conf = ""
                        if res == "dangling":
                            qa.append((c.cid, section, rec["raw"],
                                       "target locus does not exist — digit-confusion candidate"))
                    elif rec["sub"] == "relative-bare":
                        tgt, res, conf = "", "unresolvable", ""
                    elif rec["sub"] == "page":
                        tgt, res = resolve_page(rec, c, by_page)
                        conf = ""
                        if res == "dangling":
                            qa.append((c.cid, section, rec["raw"],
                                       f"no chunk owns printed page {rec['page']} "
                                       f"of tom. {rec.get('tom') or c.volume}"))
                    elif rec["sub"] == "work":
                        tgt, res = resolve_work(rec, by_id)
                        conf = ""
                    else:
                        continue

                    chunk_rows.append({
                        "chunk_id": c.cid, "volume": c.volume, "section": section,
                        "anchor_label": anchor, "class": rec["cls"],
                        "subclass": rec["sub"],
                        "raw_text": re.sub(r"\s+", " ", rec["raw"])[:120],
                        "normalized_target": tgt, "confidence": conf,
                        "resolution": res, "ibid_resolved": "",
                        "antecedent": "",
                        "_order": (sec_i, rec["pos"]),
                        "_end": rec["pos"] + len(rec["raw"]),
                        "_coords": rec.get("ibid_coords"),
                    })

        chunk_rows.sort(key=lambda r: r["_order"])
        resolve_anaphora(chunk_rows, dict(sections), cfg, qa)
        per_chunk[c.cid] = chunk_rows
        rows.extend(chunk_rows)

    unresolved_anaphora = resolve_anaphora_across_chunks(chunks, per_chunk, cfg, qa)
    return rows, qa, unresolved_anaphora


COLUMNS = ["chunk_id", "volume", "section", "anchor_label", "class", "subclass",
           "raw_text", "normalized_target", "confidence", "resolution",
           "ibid_resolved", "antecedent"]


def dedupe(rows):
    """One record per occurrence. Overlapping scanners (a `pag.` inside a `Sent.`
    tail, say) can both fire; keep the first, drop exact duplicates."""
    seen, out = set(), []
    for r in rows:
        k = (r["chunk_id"], r["section"], r["class"], r["subclass"],
             r["raw_text"], r["normalized_target"])
        if k in seen:
            continue
        seen.add(k)
        out.append(r)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--volumes", default="1,2,3,4,5,6",
                    help="volumes to EMIT records for. Resolution always indexes the "
                         "whole corpus — a vol5 cross-ref targets vols I-IV, so a "
                         "subset index would report the rest of the corpus as dangling.")
    ap.add_argument("--vol1-max-d", type=int, default=None,
                    help="pilot guard: only vol1 distinctions <= N")
    ap.add_argument("--out", default=LEDGER)
    ap.add_argument("--qa", default=QA_REPORT)
    ap.add_argument("--sample", type=int, default=0,
                    help="write N randomly sampled records to manual-review/ for hand-verification")
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()

    cfg = load_books()
    vols = [int(v) for v in args.volumes.split(",") if v.strip()]

    # Glob, never recurse — vol1/_backup-*/ holds 538 stale files (INDEX-PLAN.md).
    # ⛔ THE CORPUS RANGE IS DERIVED FROM VOLUME_COMPLETE, NEVER WRITTEN OUT.
    # It was once the literal (1, 2, 3, 4, 5), independent of --volumes: adding
    # a volume to the flag then emitted ZERO records for it, silently, because
    # no chunk of it was ever loaded into `corpus` to be filtered. The run
    # printed a clean summary with an UNCHANGED record total — the only tell.
    # Caught 2026-09-19 on Vol VI's first chunk. Resolution still always indexes
    # the WHOLE corpus, which is why this list is not `vols`.
    glob_ = __import__("glob").glob
    all_paths = [p for v in sorted(VOLUME_COMPLETE)
                 for p in sorted(glob_(os.path.join(ROOT, f"vol{v}", "*.md")))]
    corpus = [c for c in (Chunk(p) for p in all_paths) if c.cid]
    by_locus, by_dist, by_page, by_id = build_indexes(corpus)

    def in_scope(c):
        if c.volume not in vols:
            return False
        if c.volume == 1 and args.vol1_max_d is not None:
            return c.dist is not None and c.dist <= args.vol1_max_d
        return True

    chunks = [c for c in corpus if in_scope(c)]
    rows, qa, unresolved_anaphora = extract(chunks, cfg, by_locus, by_dist, by_page, by_id)
    rows = dedupe(rows)
    slip_notes = apply_printed_slips(rows)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write("\t".join(COLUMNS) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[c]).replace("\t", " ") for c in COLUMNS) + "\n")

    # ---- census assertion (tools/check-vol5-census.py pattern) -------------------
    roster_ledger = {r["chunk_id"] for r in rows}
    roster_disk = {c.cid for c in chunks}
    silent = sorted(roster_disk - roster_ledger)

    write_qa(args.qa, chunks, rows, qa, silent, cfg, vols, slip_notes)
    if args.sample:
        write_sample(rows, args.sample, args.seed)

    report(chunks, rows, qa, silent, unresolved_anaphora)
    coord = [r for r in rows if r.get("_coords")]
    print(f"coordinate ibid. (r.57): {len(coord)}  honoured "
          f"{sum(1 for r in coord if r['ibid_resolved'])}  left unresolvable "
          f"{sum(1 for r in coord if not r['ibid_resolved'])}")
    print(f"printed slips (r.57 C2) : {sum(1 for n in slip_notes if not n[3].startswith('⚠'))} "
          f"annotated, {sum(1 for n in slip_notes if n[3].startswith('⚠'))} stale")
    return 0


def report(chunks, rows, qa, silent, unresolved_anaphora=0):
    scrip = [r for r in rows if r["class"] == "scripture"]
    cross = [r for r in rows if r["class"] == "crossref"]
    auth = [r for r in rows if r["class"] == "authority"]

    print(f"chunks scanned          : {len(chunks)}")
    print(f"ledger records          : {len(rows)}")
    print(f"  scripture             : {len(scrip)}")
    print(f"  crossref              : {len(cross)}")
    print(f"  authority (excluded)  : {len(auth)}")
    if scrip:
        tiers = Counter(r["confidence"] for r in scrip)
        tot = len(scrip)
        print("  scripture confidence  : " + "  ".join(
            f"{t}={tiers.get(t,0)} ({tiers.get(t,0)/tot:.0%})" for t in ("A", "B", "C")))
    if cross:
        res = Counter(r["resolution"] for r in cross)
        tot = len(cross)
        print("  crossref resolution   : " + "  ".join(
            f"{k}={v} ({v/tot:.0%})" for k, v in res.most_common()))
    within = sum(1 for r in rows if r["ibid_resolved"] == "yes")
    cross = sum(1 for r in rows if r["ibid_resolved"] == "cross-chunk")
    still = sum(1 for r in rows if r["subclass"] == "relative-bare" and not r["ibid_resolved"])
    print(f"  anaphora resolved     : {within} within-chunk + {cross} cross-chunk"
          f"  (unresolved: {still})")
    print(f"QA flags                : {len(qa)}")
    print(f"chunks with no citation : {len(silent)}")


def write_qa(path, chunks, rows, qa, silent, cfg, vols, slip_notes=()):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("# Citation QA report\n\n")
        fh.write("> Generated by `tools/build-citations.py` — **derived, do not hand-edit.**\n")
        fh.write(f"> Volumes scanned: {', '.join(map(str, vols))}. "
                 f"{len(chunks)} chunks, {len(rows)} ledger records.\n\n")

        fh.write("## Dangling and out-of-range citations\n\n")
        fh.write("Each line is a citation whose target should exist and does not, or a "
                 "scripture chapter beyond the book's length. Per CLAUDE.md these are "
                 "**digit-confusion candidates** (the 1/4 and 3/5 classes) — settle each "
                 "off the 450 dpi band, never off the raw.\n\n")
        if qa:
            fh.write("| Chunk | Section | Raw | Problem |\n|---|---|---|---|\n")
            for cid, sec, raw, why in sorted(qa):
                fh.write(f"| `{cid}` | {sec} | `{raw}` | {why} |\n")
        else:
            fh.write("_None._\n")

        # NOTE THE ANAPHORA THAT DID NOT RESOLVE — a count is not a defect list.
        una = [r for r in rows
               if r["subclass"] == "relative-bare" and not r["ibid_resolved"]]
        fh.write("\n## Unresolved anaphora (`ibid.` / `loc. cit.` with no antecedent)\n\n")
        fh.write("An anaphor carries no target of its own, so it is resolved from the "
                 "printed sequence or not at all. These found nothing to point at.\n\n"
                 "**Most are a SCOPE boundary, not a parser gap** (checked by hand on a "
                 "sample): they point at a patristic or philosophical work — `Aug. loc. "
                 "cit. c. 4. … ibid. c. 5.`, a note on Victorinus citing Porphyry — and "
                 "this ledger deliberately does not record non-Sentences authority "
                 "works. There is nothing to inherit because the antecedent was never "
                 "captured, by design. **They would resolve for free if the deferred "
                 "authorities index is ever built.** Read the list for the minority that "
                 "point at scripture or a Sentences locus; those are real parser gaps.\n\n")
        fh.write("Two classes are deliberately NOT chained across a chunk boundary: an "
                 "anaphor in a **scholion or running body** (a different discourse from "
                 "the previous chunk's), and one whose predecessor **shares no printed "
                 "page** (no common footnote register). Chaining either would be "
                 "inference, not reading.\n\n")
        if una:
            byvol = defaultdict(list)
            for r in una:
                byvol[r["volume"]].append(r)
            fh.write(f"**{len(una)} total** — "
                     + " · ".join(f"vol {v}: {len(rs)}" for v, rs in sorted(byvol.items()))
                     + "\n\n| Chunk | Section | Raw |\n|---|---|---|\n")
            for r in sorted(una, key=lambda r: (r["volume"], r["chunk_id"], r["section"])):
                fh.write(f"| `{r['chunk_id']}` | {r['section']} | `{r['raw_text']}` |\n")
        else:
            fh.write("_None._\n")

        fh.write("\n## Printed slips filed as printed (ruling 57, C2 override table)\n\n")
        fh.write("Quaracchi's own wrong book, chapter or verse, transcribed as printed "
                 "(rulings 37/48). The ledger indexes the text as printed and never "
                 "emends it; each slip is listed here with the passage meant. Source: "
                 "`PRINTED_SLIPS` in `tools/build-citations.py`.\n\n")
        if slip_notes:
            fh.write("| Chunk | Section | Raw | Note |\n|---|---|---|---|\n")
            for cid, sec, raw, why in slip_notes:
                fh.write(f"| `{cid}` | {sec} | `{raw}` | {why} |\n")
        else:
            fh.write("_None._\n")

        coord_un = [r for r in rows if r.get("_coords") and not r["ibid_resolved"]]
        fh.write("\n## Coordinate `ibid.` left unresolvable (ruling 57, C1)\n\n")
        fh.write("An `ibid. C, V` / `ibid. v. N` keeps its own coordinates and takes only "
                 "its BOOK (for `v. N`, book and chapter) from an antecedent. These found "
                 "no antecedent the rules allow, and are left unresolvable rather than "
                 "guessed. They also appear in the anaphora list above.\n\n")
        if coord_un:
            fh.write("| Chunk | Section | Raw | Why |\n|---|---|---|---|\n")
            for r in sorted(coord_un, key=lambda r: (r["volume"], r["chunk_id"], r["section"])):
                fh.write(f"| `{r['chunk_id']}` | {r['section']} | `{r['raw_text']}` | "
                         f"{r.get('_why') or ''} |\n")
        else:
            fh.write("_None._\n")

        fh.write("\n## Chunks contributing no citation record\n\n")
        fh.write("Expected for short divisio/littera chunks; a quaestio here is worth a look.\n\n")
        fh.write("\n".join(f"- `{c}`" for c in silent) if silent else "_None._")
        fh.write("\n")


def write_sample(rows, n, seed):
    rnd = random.Random(seed)
    picked = rnd.sample(rows, min(n, len(rows)))
    picked.sort(key=lambda r: (r["chunk_id"], r["section"]))
    os.makedirs(os.path.dirname(SAMPLE_OUT), exist_ok=True)
    with open(SAMPLE_OUT, "w", encoding="utf-8") as fh:
        fh.write("# Citation pilot — hand-verification sample\n\n")
        fh.write(f"> Generated by `--sample {n} --seed {seed}`. **Verdicts are blank: "
                 "fill them by reading each row against its own chunk file.** The frozen, "
                 "hand-verified Phase 0 snapshot is `citation-pilot-sample.md`.\n\n")
        fh.write("| # | Chunk | Section | Anchor | Class | Raw | Target | Conf | Resolution | Verdict |\n")
        fh.write("|---|---|---|---|---|---|---|---|---|---|\n")
        for i, r in enumerate(picked, 1):
            fh.write(f"| {i} | `{r['chunk_id']}` | {r['section']} | {r['anchor_label']} | "
                     f"{r['subclass']} | `{r['raw_text']}` | `{r['normalized_target']}` | "
                     f"{r['confidence']} | {r['resolution']} |  |\n")
    print(f"sample written          : {SAMPLE_OUT} ({len(picked)} records)")


if __name__ == "__main__":
    sys.exit(main())
