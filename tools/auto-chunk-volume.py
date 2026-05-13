#!/usr/bin/env python3.11
"""Auto-chunk a Bonaventure volume into per-quaestio skeleton files.

Reads the raw pdftotext output, finds DISTINCTIO / QUAESTIO / ARTICULUS /
DUBIA boundaries, and writes one .md skeleton per logical unit into
vol{N}/. Each skeleton has Latin body + [Translation pending] placeholder.

OCR is noisy — this script uses broad regexes and deduplication heuristics.
Chunk boundaries WILL need human review before translation, but this gets
~80-90% of boundaries right and creates the file scaffolding.

Usage:
    python3.11 tools/auto-chunk-volume.py 2          # chunk vol 2
    python3.11 tools/auto-chunk-volume.py 2 --dry-run # show boundaries only
    python3.11 tools/auto-chunk-volume.py 1 --part 2  # chunk vol 1 pt 2

After running: review boundaries in the generated chunks, fix any that
look wrong, then run build-task-packet.py or translate-batch.py.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Broad OCR-tolerant patterns. pdftotext output contains common substitutions:
#   O→0, S→8, R→E (or AEI→EIU), I↔1, UNICUS→UiNICUS / UNIGUS, TEXTUS→TE.XTUS, etc.
# Tested against pt1 and pt2 raw; see tools/raw-ocr-notes for variants observed.
RE_DISTINCTIO = re.compile(
    # Tolerant of OCR substitutions in 'DISTINCTIO':
    #   DISTING(TIO)   — C→G (d.17 line 51999: 'DISTINGTIO XVII.')
    #   DiSTINCTIO     — case mangle (d.23 line 69303 running head)
    #   DISTmCTIO      — IN→m ligature mangle (vol2 d.II line 4264: 'DISTmCTIO 11.')
    # Roman numeral allows U-for-I substitution (XVIU=XVIII at d.18 line 56737)
    # and digit substitution (vol2 d.II: '11.' = II).
    # Leading whitespace must also accept \f (form feed) — pdftotext emits \f as
    # the page-break sentinel at the start of a fresh page, and clean DISTINCTIO
    # headers in vol2 frequently sit on the first line of a new page
    # (vol2 d.17 line 28812, d.20 line 33403, d.34 line 55782).
    r"^[ \t\f]*D[Ii]ST[Im]N?[CG]?TIO\S*\s+([IVXLCUivxlcu0-9]+(?:\s*[IVXLCUivxlcu0-9])*)\b",
    re.MULTILINE,
)
RE_COMMENTARIUS = re.compile(
    # C[O0]MMENT[AE][RE]?(IU|III)[S8] — covers COMMENTARIUS, C0MMENTARIU8, C0MMENTAEIU8,
    # COMMENTAEIUS, C0MMENTARIII8. Requires "IN D" suffix (the distinction ref).
    r"^[ \t\f]*C[O0]MMENT[AE][REI]{1,3}[US8]{1,2}\s+(?:IN|m)\s+D",
    re.MULTILINE,
)
RE_DIVISIO = re.compile(
    # DIV[IT]SIO TE[.]?XTUS — covers DIVISIO, DIVTSIO; TEXTUS clean or OCR'd
    # TE.XTUS / TEXTIIS (II→U) / TKXTUS (E→K, d.43 line 34161).
    # Anchored to line-start with anti-DIST lookahead so running heads like
    # 'DIST. XVII. P. 1. DIVISIO TEXTIIS.' (line 52600) don't false-positive.
    r"^[ \t\f]*(?!DIST[.\s])(?:.*\b)?D[IL]V[ITJ]SIO\s+T[EK]\.?XT[UI]{1,3}[S8]",
    re.MULTILINE,
)
RE_QUAESTIO = re.compile(
    # OCR variants observed in pt1. The clean form is "QUAESTIO N.":
    #   QUAESTIO / QU.ESTIO / QU^STIO / QU.flSTIO / QUAEST.
    #   OUAESTIO     (d.16 q3 — Q→O substitution, line 51432)
    #   QIIAESTIO    (d.18 q3 — U→I,           line 57811)
    #   QLWESTIO     (d.17 p2-q2 — UA→LW,      line 55481)
    #   QUAFSTK)     (d.18 q5 — AES→AFS, IO→K), line 58354)
    #   gl!.\ESTIO   (d.17 p1-q3 — Q→gl, U→l!, line 53715)
    # Match strategy: alternation of (Q|O|gl)-led prefix + tolerant middle + STIO/STK)
    # ending. The roman/digit number after is captured as group(1).
    r"^[ \t\f]*['`]?(?:"                                   # optional stray apostrophe (OCR noise, e.g. d.40 a4-q1 line 29733)
        r"[QO][UIJij1lL][A^.flUVWFEIJij\\n]{0,6}"        # Q/O-led with tolerant middle (incl U from 'QIUESTIO', V from 'QU.VESTIO')
        r"(?:S[Tnr][I1li]?[O0]|STK\))"                    # ending: STIO clean; S[Tnr][I1li]?[O0] covers OCR T→n/r and dropped-I or lowercase-i variants; STK) for d.18 q5
        r"|gl[!.\\]+\\?ESTIO"                             # gl!.\ESTIO style
    r")\s+([IVXLC1lijm\[]+)\]?(?=\W|$)",                  # number may be bracket-prefixed or 'm' (OCR for III); allow non-word boundary
    re.MULTILINE,
)
RE_ARTICULUS = re.compile(
    # ARTI[CG]ULUS + roman / digit-garbled roman / UNICUS variants (UiNICUS, UNIGUS, UiNIGUS)
    r"^[ \t\f]*ARTI[CGI]U[L1I]U[S8]\s+([IVXLC1]+|U[Ii]?N[IL]?[CG]U[S8])\b",
    re.MULTILINE,
)
RE_DUBIA = re.compile(
    # Section-start matcher. Catches:
    #   "DUBIA CIRCA LITTERAM MAGISTRI" + OCR variants (DHBIA U→H d.17 p2 56632;
    #   DUBL\ d.23 71288 — the BIA→BL\ mangle)
    #   "DUB. I." / "DUB. 1." / "DrB. I." / "DUB. L." / "DuB. I." (lowercase u, d.31)
    #   / "DlB. I." (lowercase l → looks like Dl, d.31 sub-dubia variant)
    # NOT a running head like "DIST. XXII. DUBIA." (false-positive at line 68722):
    # we require either a CIRCA-ish word after DUBIA on the same line, or that
    # the line not start with DIST.
    # NOT: "DUB. II." / "DUB. III." — those are internal sub-dubia.
    # NOTE: sub-dubia in d.31 p2 use OCR garbles `DuB. IV.`, `DlB. 11.`, `DuB. vni.`
    #       (`vni.` = OCR for VIII). They live inside a single dubia chunk and are
    #       not separately matched here, but if a future tool needs to enumerate
    #       sub-dubia for audit, account for these variants.
    r"^[ \t\f]*(?!DIST[.\s])"
    r"(?:.*\bD[UHL][IH]?B[IL][A\\]\b|D[ruUlL][bB][.\s]+[I1L]\b[^IVX])",
    re.MULTILINE,
)
RE_PARS = re.compile(
    r"^[ \t\f]*PARS\s+(I{1,3}|PRIMA|SECUNDA)\b",
    re.MULTILINE | re.IGNORECASE,
)
# Vol II has NO standalone `PARS PRIMA/SECUNDA` headings — pars info lives only
# in running heads like `DIST. II. P. I. ART. I. QUAEST. I.` or `DIST. II. P. II. ...`.
# This regex picks up running heads with the P. {I|II|1|2} component so we can
# infer the P.I → P.II transition line within each distinction.
RE_RUNHEAD_PARS = re.compile(
    r"^[ \t\f]*DIST\.?\s*[IVXLCUivxlcu0-9]+\.?\s*P\.?\s*(I{1,3}|1|2|II)\.",
    re.MULTILINE,
)

ROMAN = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
    "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
    "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15,
    "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19, "XX": 20,
    "XXI": 21, "XXII": 22, "XXIII": 23, "XXIV": 24, "XXV": 25,
    "XXVI": 26, "XXVII": 27, "XXVIII": 28, "XXIX": 29, "XXX": 30,
    "XXXI": 31, "XXXII": 32, "XXXIII": 33, "XXXIV": 34, "XXXV": 35,
    "XXXVI": 36, "XXXVII": 37, "XXXVIII": 38, "XXXIX": 39, "XL": 40,
    "XLI": 41, "XLII": 42, "XLIII": 43, "XLIV": 44, "XLV": 45,
    "XLVI": 46, "XLVII": 47, "XLVIII": 48, "XLIX": 49, "L": 50,
    "UNICUS": 1,
}


def parse_roman(s: str) -> int | None:
    s = s.strip().replace(" ", "").upper()
    # OCR digit/bracket substitutions for I/II/III: "1"/"11"/"111" or "[1"/"[11"
    # (a leading "[" is sometimes misread of a leading "I", so '[11' = III).
    s = s.replace("[", "1")
    if s in ("1", "11", "111"):
        return len(s)
    # Vol II ALSO has 4-digit digit-mangle: "1111" = IV (rare; safeguard).
    if s == "1111":
        return 4
    # OCR ligature: small-caps "III." sometimes scanned as a single "m" glyph
    # (observed at d.23 a1-q3 line 70027: 'QIUESTIO m.'). Quaestio numbers in
    # the Sentences never exceed ~10, so M=1000 is never legitimate here.
    if s == "M":
        return 3
    # UNICUS OCR variants: UiNICUS, UNIGUS, UiNIGUS, UINICUS etc. all mean UNICUS (=1).
    if re.fullmatch(r"U[I]?N[IL]?[CG]U[S8]", s):
        return 1
    if s in ROMAN:
        # Single "L" alone is almost always OCR-misread "I"; quaestio numbers never go that high.
        if s == "L":
            return 1
        return ROMAN[s]
    # OCR fallback: lowercase-l was misread as I, then .upper() turned it into L.
    # Try replacing 1..N trailing Ls with Is — least aggressive first.
    trailing = len(s) - len(s.rstrip("L"))
    for n in range(1, trailing + 1):
        variant = s[:-n] + "I" * n
        if variant in ROMAN:
            return ROMAN[variant]
    # OCR fallback: trailing U is sometimes a misread of double-I (II) or final I.
    # Observed: "XVIU" for XVIII (d.18 line 56737). Try U→II first, then U→I.
    if s.endswith("U"):
        for replacement in ("II", "I"):
            variant = s[:-1] + replacement
            if variant in ROMAN:
                return ROMAN[variant]
    return None


@dataclass
class Marker:
    line: int
    kind: str  # distinctio, commentarius, divisio, quaestio, articulus, dubia, pars
    num: int | None = None
    raw: str = ""


@dataclass
class Chunk:
    chunk_id: str
    start: int
    end: int
    kind: str
    distinctio: int
    pars: int | None = None
    articulus: int | None = None
    quaestio: int | None = None


def find_markers(text: str) -> list[Marker]:
    markers = []

    for m in RE_DISTINCTIO.finditer(text):
        line = text[:m.start()].count("\n") + 1
        num = parse_roman(m.group(1))
        if num:
            markers.append(Marker(line, "distinctio", num, m.group(0).strip()))

    for m in RE_COMMENTARIUS.finditer(text):
        line = text[:m.start()].count("\n") + 1
        markers.append(Marker(line, "commentarius", raw=m.group(0).strip()))

    for m in RE_DIVISIO.finditer(text):
        line = text[:m.start()].count("\n") + 1
        markers.append(Marker(line, "divisio", raw=m.group(0).strip()))

    for m in RE_ARTICULUS.finditer(text):
        line = text[:m.start()].count("\n") + 1
        num = parse_roman(m.group(1))
        markers.append(Marker(line, "articulus", num, m.group(0).strip()))

    for m in RE_QUAESTIO.finditer(text):
        line = text[:m.start()].count("\n") + 1
        num = parse_roman(m.group(1))
        if num:
            markers.append(Marker(line, "quaestio", num, m.group(0).strip()))

    for m in RE_DUBIA.finditer(text):
        line = text[:m.start()].count("\n") + 1
        markers.append(Marker(line, "dubia", raw=m.group(0).strip()))

    markers.sort(key=lambda m: m.line)
    return markers


def dedupe_markers(markers: list[Marker], lines: list[str]) -> list[Marker]:
    """Remove running-head duplicates: if two markers of the same kind
    appear within 30 lines, keep only the second (the real header).

    RULE: when a Quaracchi page begins a new section, the page-top running
    head and the actual section break are *both* labeled identically (e.g.
    ``DISTINCTIO XVIII`` appears once as the page header and once again,
    a few lines down, as the real distinction title). The second occurrence
    is always the real break — the first is just typesetting.

    Empirical case: d.18 has ``DISTINCTIO XVIU.`` (OCR'd) at line 56737
    followed by content from the prior distinction (DUB. IV of d.17), then
    the real ``DISTINCTIO XVIII.`` at line 56764. Treating the first as
    the boundary swallows ~27 lines of d.17 dubia into d.18's littera.

    Same pattern applies to QUAESTIO and DUBIA markers when a question
    or dubia section spans a page break.
    """
    result = []
    i = 0
    while i < len(markers):
        m = markers[i]
        # Look ahead for a duplicate within 30 lines
        if i + 1 < len(markers):
            n = markers[i + 1]
            if n.kind == m.kind and n.num == m.num and (n.line - m.line) < 30:
                # Skip the first one (running head), keep the second
                i += 1
                continue
        result.append(m)
        i += 1
    return result


def find_distinctio_ranges(markers: list[Marker], total_lines: int) -> list[tuple[int, int, int]]:
    """Return (distinctio_num, start_line, end_line) for each distinction."""
    dist_markers = [m for m in markers if m.kind == "distinctio"]

    # Dedupe: when the same DISTINCTIO number appears multiple times, prefer
    # the LAST nearby occurrence (running-head pattern, ~30 lines apart). For
    # far-apart duplicates (body references in scholion footnotes or end-of-vol
    # index entries — e.g. pt2 has 'DISTINCTIO XLVI' both at line 39073 (real)
    # and line 44627 (index), keep the FIRST occurrence as the real break.
    DEDUP_WINDOW = 100
    seen = {}
    unique = []
    for m in dist_markers:
        if m.num not in seen:
            seen[m.num] = m
            unique.append(m)
        else:
            prev = seen[m.num]
            if (m.line - prev.line) <= DEDUP_WINDOW:
                # Nearby duplicate — running head followed by real heading.
                # Replace earlier with later (the real section break).
                idx = unique.index(prev)
                unique[idx] = m
                seen[m.num] = m
            # else: far-apart duplicate (body reference / index) — keep first.

    ranges = []
    for i, m in enumerate(unique):
        start = m.line
        end = unique[i + 1].line - 1 if i + 1 < len(unique) else total_lines
        ranges.append((m.num, start, end))
    return ranges


def find_pars_split_line(text: str, start: int, end: int) -> int | None:
    """Inspect running heads inside a distinction range and return the first
    line where P. II content begins, or None if the distinction is single-pars.

    Vol II lacks standalone PARS PRIMA/SECUNDA headers — pars information
    is only carried in running heads like `DIST. II. P. I. ART. I.` and
    `DIST. II. P. II. ART. I.`. We find the first P.{II|2} running head; the
    p1/p2 boundary lies just before it.
    """
    # Re-scan with line filter
    region = "\n".join(text.split("\n")[start - 1:end])
    p1_lines: list[int] = []
    p2_lines: list[int] = []
    for m in RE_RUNHEAD_PARS.finditer(region):
        rel_line = region[:m.start()].count("\n")
        abs_line = start + rel_line
        pars_raw = m.group(1).upper()
        if pars_raw in ("I", "1"):
            p1_lines.append(abs_line)
        elif pars_raw in ("II", "2"):
            p2_lines.append(abs_line)
    if not p2_lines or not p1_lines:
        return None
    # P.II split = first P.II running head
    return min(p2_lines)


def chunk_distinction(
    dist_num: int,
    start: int,
    end: int,
    markers: list[Marker],
    vol: int,
    book: int,
    text: str | None = None,
) -> list[Chunk]:
    """Split a distinction range into chunks based on sub-markers."""
    sub = [m for m in markers if start <= m.line <= end and m.kind != "distinctio"]

    # Detect pars split (vol II uses running-head pars; vol I uses explicit PARS markers).
    pars_split = find_pars_split_line(text, start, end) if text else None

    def pars_for_line(line: int) -> int | None:
        if pars_split is None:
            return None
        return 1 if line < pars_split else 2

    def labeled_prefix(line: int) -> str:
        p = pars_for_line(line)
        if p is None:
            return f"bon-sent-{roman_vol(vol)}-d{dist_num}"
        return f"bon-sent-{roman_vol(vol)}-d{dist_num}-p{p}"

    prefix = f"bon-sent-{roman_vol(vol)}-d{dist_num}"
    chunks = []

    # Find key sub-boundaries
    commentarius_lines = [m.line for m in sub if m.kind == "commentarius"]
    divisio_lines = [m.line for m in sub if m.kind == "divisio"]
    quaestio_markers = [m for m in sub if m.kind == "quaestio"]
    articulus_markers = [m for m in sub if m.kind == "articulus"]
    dubia_lines = [m.line for m in sub if m.kind == "dubia"]

    # If there's a commentarius, everything before it is littera
    littera_end = commentarius_lines[0] - 1 if commentarius_lines else None
    if littera_end and littera_end > start + 5:
        lp = labeled_prefix(start)
        chunks.append(Chunk(f"{lp}-littera", start, littera_end, "littera", dist_num, pars=pars_for_line(start)))

    # If no quaestio markers at all, treat entire commentary as one chunk
    if not quaestio_markers:
        comm_start = commentarius_lines[0] if commentarius_lines else start
        lp = labeled_prefix(comm_start)
        chunks.append(Chunk(f"{lp}-commentary", comm_start, end, "commentary", dist_num, pars=pars_for_line(comm_start)))
        return chunks

    # Build quaestio chunks: each quaestio runs until the next quaestio or dubia or end
    # Track current articulus
    cur_art = 1
    art_map: dict[int, int] = {}  # line -> articulus num
    for am in articulus_markers:
        art_map[am.line] = am.num or 1

    # Merge all sub-boundaries for sequencing
    boundaries: list[tuple[int, str, int | None]] = []
    for m in sub:
        if m.kind == "commentarius":
            boundaries.append((m.line, "commentarius", None))
        elif m.kind == "divisio":
            boundaries.append((m.line, "divisio", None))
        elif m.kind == "articulus":
            boundaries.append((m.line, "articulus", m.num))
        elif m.kind == "quaestio":
            boundaries.append((m.line, "quaestio", m.num))
        elif m.kind == "dubia":
            boundaries.append((m.line, "dubia", None))
    boundaries.sort(key=lambda x: x[0])

    # Walk boundaries and create chunks
    cur_art = 1
    cur_pars: int | None = pars_for_line(start)
    divisio_start = None
    i = 0
    while i < len(boundaries):
        line, kind, num = boundaries[i]
        next_line = boundaries[i + 1][0] if i + 1 < len(boundaries) else end + 1

        # Reset articulus counter when crossing the pars boundary
        new_pars = pars_for_line(line)
        if new_pars != cur_pars:
            cur_pars = new_pars
            cur_art = 1

        lp = labeled_prefix(line)

        if kind == "commentarius":
            # Commentarius intro — might include divisio
            pass
        elif kind == "divisio":
            # Divisio textus — runs until next articulus or quaestio
            chunks.append(Chunk(f"{lp}-divisio", line, next_line - 1, "divisio", dist_num, pars=cur_pars))
        elif kind == "articulus":
            cur_art = num or cur_art
        elif kind == "quaestio":
            q_end = next_line - 1
            chunk_id = f"{lp}-a{cur_art}-q{num}"
            chunks.append(Chunk(
                chunk_id, line, q_end, "quaestio", dist_num,
                pars=cur_pars, articulus=cur_art, quaestio=num,
            ))
        elif kind == "dubia":
            # End at the next section boundary (not end-of-distinction) so multi-pars
            # distinctions don't have the dubia swallow the next pars.
            chunks.append(Chunk(f"{lp}-dubia", line, next_line - 1, "dubia", dist_num, pars=cur_pars))
        i += 1

    return chunks


def roman_vol(vol: int) -> str:
    return {1: "I", 2: "II", 3: "III", 4: "IV"}[vol]


def book_for_vol(vol: int) -> int:
    return vol


def build_skeleton(chunk: Chunk, lines: list[str], vol: int) -> str:
    latin_body = "\n".join(lines[chunk.start - 1:chunk.end]).strip()
    word_count = len(latin_body.split())

    meta_parts = [
        f'id: "{chunk.chunk_id}"',
        f"volume: {vol}",
        f"book: {book_for_vol(vol)}",
        f"distinctio: {chunk.distinctio}",
    ]
    if chunk.articulus is not None:
        meta_parts.append(f"articulus: {chunk.articulus}")
    if chunk.quaestio is not None:
        meta_parts.append(f"quaestio: {chunk.quaestio}")
    meta_parts.extend([
        f"type: {chunk.kind}",
        f"line_start: {chunk.start}",
        f"line_end: {chunk.end}",
        f"word_count_latin: {word_count}",
        f'transcription_status: "auto-chunked {__import__("datetime").date.today()}"',
        "format_version: 1",
    ])
    frontmatter = "\n".join(meta_parts)

    return f"""---
{frontmatter}
---

# {chunk.chunk_id}

## Latin

{latin_body}

## English

[Translation pending]

## Apparatus

[Apparatus pending]

## Notes

[Notes pending]
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("volume", type=int, help="Volume number (1–4)")
    ap.add_argument("--part", type=int, default=None, help="Part number (for vol 1)")
    ap.add_argument("--dry-run", action="store_true", help="Show boundaries only, don't write files")
    ap.add_argument("--force", action="store_true", help="Overwrite existing chunk files")
    ap.add_argument("--min-dist", type=int, default=None, help="Ignore distinctions below this number (filters ghost tail matches)")
    args = ap.parse_args()

    vol = args.volume
    suffix = f"_pt{args.part}" if args.part else ""
    raw_path = REPO / "raw" / f"bonaventure_vol{vol}{suffix}_raw.txt"
    out_dir = REPO / f"vol{vol}"
    out_dir.mkdir(exist_ok=True)

    if not raw_path.exists() or raw_path.stat().st_size == 0:
        print(f"ERROR: {raw_path} missing or empty. Run fetch-volume.py first.", file=sys.stderr)
        sys.exit(1)

    text = raw_path.read_text(errors="replace")
    lines = text.split("\n")  # must match line-num counting in find_markers (text[:m.start()].count("\n") + 1)
    total_lines = len(lines)
    print(f"Volume {vol}{suffix}: {total_lines} lines, {len(text.split())} words")

    markers = find_markers(text)
    markers = dedupe_markers(markers, lines)
    print(f"Found {len(markers)} markers after dedup")

    dist_ranges = find_distinctio_ranges(markers, total_lines)
    if args.min_dist is not None:
        before = len(dist_ranges)
        dist_ranges = [r for r in dist_ranges if r[0] >= args.min_dist]
        if before != len(dist_ranges):
            print(f"Filtered {before - len(dist_ranges)} distinctions below d.{args.min_dist}")
    print(f"Found {len(dist_ranges)} distinctions")

    all_chunks = []
    for dist_num, d_start, d_end in dist_ranges:
        chunks = chunk_distinction(dist_num, d_start, d_end, markers, vol, book_for_vol(vol), text=text)
        all_chunks.extend(chunks)

    id_seen: dict[str, int] = {}
    duplicates: list[str] = []
    for c in all_chunks:
        base = c.chunk_id
        n = id_seen.get(base, 0) + 1
        id_seen[base] = n
        if n > 1:
            c.chunk_id = f"{base}-dup{n}"
            duplicates.append(c.chunk_id)

    print(f"\nTotal chunks: {len(all_chunks)}")
    if duplicates:
        print(f"  duplicate IDs suffixed (-dup2/3/...): {len(duplicates)} — flag for pars relabeling")
    print(f"  littera: {sum(1 for c in all_chunks if c.kind == 'littera')}")
    print(f"  divisio: {sum(1 for c in all_chunks if c.kind == 'divisio')}")
    print(f"  quaestio: {sum(1 for c in all_chunks if c.kind == 'quaestio')}")
    print(f"  dubia: {sum(1 for c in all_chunks if c.kind == 'dubia')}")
    print(f"  commentary: {sum(1 for c in all_chunks if c.kind == 'commentary')}")

    if args.dry_run:
        print("\n--- Chunk list (dry run) ---")
        for c in all_chunks:
            print(f"  {c.chunk_id}: lines {c.start}-{c.end} ({c.end - c.start + 1} lines)")
        return

    written = 0
    skipped = 0
    for chunk in all_chunks:
        path = out_dir / f"{chunk.chunk_id}.md"
        if path.exists() and not args.force:
            skipped += 1
            continue
        content = build_skeleton(chunk, lines, vol)
        path.write_text(content)
        written += 1

    print(f"\nWrote {written} files to {out_dir.relative_to(REPO)}/")
    if skipped:
        print(f"Skipped {skipped} existing files (use --force to overwrite)")

    # Write manifest for the batch runner
    manifest = {
        "volume": vol,
        "part": args.part,
        "chunks": [
            {
                "id": c.chunk_id,
                "file": f"vol{vol}/{c.chunk_id}.md",
                "kind": c.kind,
                "distinctio": c.distinctio,
                "lines": c.end - c.start + 1,
            }
            for c in all_chunks
        ],
    }
    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"Wrote manifest: {manifest_path.relative_to(REPO)}")


if __name__ == "__main__":
    main()
