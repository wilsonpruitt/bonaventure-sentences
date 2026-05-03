#!/usr/bin/env python3.11
"""Fix chunk boundaries by re-splitting from raw text using semantic markers.

For a given distinction, this script:
1. Finds ALL semantic markers (DISTINCTIO, COMMENTARIUS, DIVISIO, ARTICULUS,
   QUAESTIO, DUBIA) in the raw text range
2. Filters out running heads (DIST. X. ART. I. QUAEST. I. format)
3. Computes correct boundary ranges for each chunk
4. Rewrites existing chunk files with corrected line_start/line_end/Latin body
5. Creates missing chunks (littera, divisio) as skeletons

Does NOT touch chunks that are already Tier 2 (transcription_status contains
"Tier 2"). Those were manually cleaned and their boundaries are correct.

Usage:
    python3.11 tools/boundary-fix.py 10             # fix d.10
    python3.11 tools/boundary-fix.py 10 --dry-run   # show what would change
    python3.11 tools/boundary-fix.py 10-23           # fix d.10 through d.23
    python3.11 tools/boundary-fix.py all             # fix all non-Tier-2 chunks
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw" / "bonaventure_vol1_raw.txt"
VOL1 = REPO / "vol1"

# ── Marker detection ──────────────────────────────────────────────────

# Running heads look like: DIST. X. ART. I. QUAEST. I.
RE_RUNNING_HEAD = re.compile(
    r"^\s*DIST\.\s+[IVXLC]+\.\s+(?:ART|P)\.\s+",
    re.MULTILINE,
)

# Real semantic markers
RE_DISTINCTIO = re.compile(r"^\s*DISTINCTIO\s+([IVXLC]+)", re.MULTILINE)
RE_COMMENTARIUS = re.compile(r"^\s*C[O0]MMENT[A\^]RIU[S8]\s+(?:IN|m)\s+[DM]", re.MULTILINE | re.IGNORECASE)
RE_DIVISIO = re.compile(r"^\s*DIVISIO\s+TEXTUS", re.MULTILINE | re.IGNORECASE)
RE_TRACTATIO = re.compile(r"^\s*TRACTATIO\s+QU", re.MULTILINE | re.IGNORECASE)
RE_ARTICULUS = re.compile(r"^\s*ARTI[CG]ULUS\s+([IVXLCn0-9]+|UNICUS)\b", re.MULTILINE)
RE_QUAESTIO = re.compile(r"^\s*QU[A^.\\flEI\[\(]{0,5}ST[IIOE\[\()\]]{0,4}\s+([IVXLCm0-9]+)\b", re.MULTILINE)
RE_DUBIA = re.compile(r"^\s*DUB(?:IA|IV)?\s+C[IimM]RC[AV]\s+L[IiT1][TK]", re.MULTILINE | re.IGNORECASE)
RE_SCHOLION = re.compile(r"^\s*[CS][CHI]OLIO[NK]", re.MULTILINE)
RE_PAGE_NUM = re.compile(r"^\s*(\d{3})\s*$", re.MULTILINE)

ROMAN = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
    "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13,
    "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19,
    "XX": 20, "XXI": 21, "XXII": 22, "XXIII": 23, "XXIV": 24, "XXV": 25,
    "UNICUS": 1, "m": 3,
}


OCR_ARABIC_TO_ROMAN = {
    "1": 1, "11": 2, "111": 3, "1V": 4, "lV": 4,
    "2": 2, "3": 3, "4": 4, "5": 5,
    "n": 2, "IL": 2, "lI": 2, "Il": 2,
}


def parse_roman(s: str) -> int | None:
    s = s.strip().replace(" ", "")
    if s in ROMAN:
        return ROMAN[s]
    if s in OCR_ARABIC_TO_ROMAN:
        return OCR_ARABIC_TO_ROMAN[s]
    try:
        n = int(s)
        if 1 <= n <= 50:
            return n
    except ValueError:
        pass
    return None


@dataclass
class Marker:
    line: int
    kind: str
    num: int | None = None
    raw: str = ""


@dataclass
class ChunkDef:
    chunk_id: str
    kind: str  # littera, divisio, quaestio, dubia
    start: int
    end: int
    dist: int
    art: int | None = None
    q: int | None = None
    pars: int | None = None


def line_of(text: str, pos: int) -> int:
    return text[:pos].count("\n") + 1


def is_running_head(text: str, pos: int) -> bool:
    """Check if the marker at `pos` is actually a running head."""
    line_start = text.rfind("\n", 0, pos) + 1
    line_end = text.find("\n", pos)
    if line_end == -1:
        line_end = len(text)
    line_text = text[line_start:line_end].strip()
    return bool(RE_RUNNING_HEAD.match(line_text))


def find_real_markers(text: str, start_line: int, end_line: int) -> list[Marker]:
    """Find semantic markers in a line range, excluding running heads."""
    lines = text.splitlines()
    # Convert line range to char positions
    char_start = sum(len(lines[i]) + 1 for i in range(start_line - 1)) if start_line > 1 else 0
    char_end = sum(len(lines[i]) + 1 for i in range(min(end_line, len(lines))))
    segment = text[char_start:char_end]
    offset = char_start

    markers = []

    for m in RE_DISTINCTIO.finditer(segment):
        line = line_of(text, offset + m.start())
        num = parse_roman(m.group(1))
        if num and not is_running_head(text, offset + m.start()):
            markers.append(Marker(line, "distinctio", num, m.group(0).strip()[:60]))

    for m in RE_COMMENTARIUS.finditer(segment):
        line = line_of(text, offset + m.start())
        markers.append(Marker(line, "commentarius", raw=m.group(0).strip()[:60]))

    for m in RE_DIVISIO.finditer(segment):
        line = line_of(text, offset + m.start())
        if not is_running_head(text, offset + m.start()):
            markers.append(Marker(line, "divisio", raw=m.group(0).strip()[:60]))

    for m in RE_TRACTATIO.finditer(segment):
        line = line_of(text, offset + m.start())
        markers.append(Marker(line, "tractatio", raw=m.group(0).strip()[:60]))

    for m in RE_ARTICULUS.finditer(segment):
        line = line_of(text, offset + m.start())
        if not is_running_head(text, offset + m.start()):
            num = parse_roman(m.group(1))
            markers.append(Marker(line, "articulus", num, m.group(0).strip()[:60]))

    for m in RE_QUAESTIO.finditer(segment):
        line = line_of(text, offset + m.start())
        if not is_running_head(text, offset + m.start()):
            num = parse_roman(m.group(1))
            if num:
                markers.append(Marker(line, "quaestio", num, m.group(0).strip()[:60]))

    for m in RE_DUBIA.finditer(segment):
        line = line_of(text, offset + m.start())
        if not is_running_head(text, offset + m.start()):
            markers.append(Marker(line, "dubia", raw=m.group(0).strip()[:60]))

    markers.sort(key=lambda m: m.line)

    # Dedup: if two same-kind markers within 20 lines, keep the second
    deduped = []
    i = 0
    while i < len(markers):
        m = markers[i]
        if i + 1 < len(markers):
            n = markers[i + 1]
            if n.kind == m.kind and n.num == m.num and (n.line - m.line) < 20:
                i += 1
                continue
        deduped.append(m)
        i += 1

    return deduped


def compute_section_chunks(
    prefix: str,
    dist_num: int,
    section_start: int,
    section_end: int,
    markers: list[Marker],
    pars: int | None = None,
) -> list[ChunkDef]:
    """Compute quaestio/dubia chunks for one section (pars or whole distinction)."""
    chunks = []
    cur_art = 1
    content_markers = []
    for m in markers:
        if m.line < section_start or m.line > section_end:
            continue
        if m.kind == "articulus":
            content_markers.append(("articulus", m.num or 1, m.line))
        elif m.kind == "quaestio":
            content_markers.append(("quaestio", m.num, m.line))
        elif m.kind == "dubia":
            content_markers.append(("dubia", None, m.line))

    i = 0
    while i < len(content_markers):
        kind, num, line = content_markers[i]
        next_line = content_markers[i + 1][2] if i + 1 < len(content_markers) else None

        if kind == "articulus":
            cur_art = num or cur_art
            i += 1
            continue
        elif kind == "quaestio":
            q_end = (next_line - 1) if next_line else section_end
            chunk_id = f"{prefix}-a{cur_art}-q{num}"
            chunks.append(ChunkDef(
                chunk_id, "quaestio", line, q_end, dist_num,
                art=cur_art, q=num, pars=pars,
            ))
        elif kind == "dubia":
            chunk_id = f"{prefix}-dubia"
            chunks.append(ChunkDef(
                chunk_id, "dubia", line, section_end, dist_num, pars=pars,
            ))
        i += 1

    return chunks


def compute_chunks(
    dist_num: int,
    dist_start: int,
    dist_end: int,
    markers: list[Marker],
) -> list[ChunkDef]:
    """Compute chunk definitions from markers."""
    vol_roman = "I"
    prefix = f"bon-sent-{vol_roman}-d{dist_num}"
    chunks = []

    commentarius = [m for m in markers if m.kind == "commentarius"]

    # Multi-pars detection: 2+ COMMENTARIUS sections = multi-pars
    is_multi_pars = len(commentarius) >= 2

    # Littera: from distinctio start to first commentarius (or first divisio)
    divisio_markers = [m for m in markers if m.kind == "divisio"]
    comm_start = commentarius[0].line if commentarius else None
    div_start = divisio_markers[0].line if divisio_markers else None
    littera_end = (comm_start or div_start or dist_end) - 1

    if littera_end > dist_start + 5:
        chunks.append(ChunkDef(f"{prefix}-littera", "littera", dist_start, littera_end, dist_num))

    if is_multi_pars:
        # Each COMMENTARIUS defines a pars
        for pi, comm in enumerate(commentarius):
            pars_num = pi + 1
            pars_prefix = f"{prefix}-p{pars_num}"
            pars_start = comm.line
            pars_end = commentarius[pi + 1].line - 1 if pi + 1 < len(commentarius) else dist_end

            # Divisio for this pars
            first_content = None
            for m in markers:
                if m.line > pars_start and m.line <= pars_end and m.kind in ("articulus", "quaestio"):
                    first_content = m.line
                    break
            if first_content:
                chunks.append(ChunkDef(
                    f"{pars_prefix}-divisio", "divisio",
                    pars_start, first_content - 1, dist_num, pars=pars_num,
                ))

            # Quaestiones for this pars
            chunks.extend(compute_section_chunks(
                pars_prefix, dist_num, pars_start, pars_end, markers, pars=pars_num,
            ))
    else:
        # Single-pars: original logic
        if comm_start:
            first_content = None
            for m in markers:
                if m.line > comm_start and m.kind in ("articulus", "quaestio"):
                    first_content = m.line
                    break
            if first_content:
                chunks.append(ChunkDef(
                    f"{prefix}-divisio", "divisio",
                    comm_start, first_content - 1, dist_num,
                ))

        chunks.extend(compute_section_chunks(
            prefix, dist_num,
            comm_start or dist_start, dist_end, markers,
        ))

    return chunks


def get_dist_ranges(text: str) -> dict[int, tuple[int, int]]:
    """Find all DISTINCTIO boundaries."""
    markers = []
    for m in RE_DISTINCTIO.finditer(text):
        line = line_of(text, m.start())
        num = parse_roman(m.group(1))
        if num and not is_running_head(text, m.start()):
            if not markers or markers[-1][0] != num or (line - markers[-1][1]) > 20:
                markers.append((num, line))

    # Dedup by number, keep first
    seen = {}
    for num, line in markers:
        if num not in seen:
            seen[num] = line

    sorted_dists = sorted(seen.items())
    ranges = {}
    for i, (num, start) in enumerate(sorted_dists):
        end = sorted_dists[i + 1][1] - 1 if i + 1 < len(sorted_dists) else len(text.splitlines())
        ranges[num] = (start, end)
    return ranges


def is_tier2(path: Path) -> bool:
    text = path.read_text()
    return "Tier 2" in text[:500]


def write_skeleton(chunk: ChunkDef, lines: list[str], dry_run: bool) -> str:
    """Write or update a chunk file."""
    path = VOL1 / f"{chunk.chunk_id}.md"
    latin_body = "\n".join(lines[chunk.start - 1:chunk.end]).strip()
    word_count = len(latin_body.split())

    # Check if file exists and is Tier 2
    if path.exists() and is_tier2(path):
        return f"  SKIP (Tier 2): {chunk.chunk_id}"

    meta_parts = [
        f'id: "{chunk.chunk_id}"',
        f"volume: 1",
        f"book: 1",
        f"distinctio: {chunk.dist}",
    ]
    if chunk.art is not None:
        meta_parts.append(f"articulus: {chunk.art}")
    if chunk.q is not None:
        meta_parts.append(f"quaestio: {chunk.q}")
    meta_parts.extend([
        f"type: {chunk.kind}",
        f"line_start: {chunk.start}",
        f"line_end: {chunk.end}",
        f"word_count_latin: {word_count}",
        f'transcription_status: "boundary-fixed {__import__("datetime").date.today()}"',
        "format_version: 1",
    ])
    frontmatter = "\n".join(meta_parts)

    content = f"""---
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

    action = "UPDATE" if path.exists() else "CREATE"
    if not dry_run:
        path.write_text(content)

    return f"  {action}: {chunk.chunk_id} (lines {chunk.start}-{chunk.end}, {word_count}w)"


def fix_distinction(dist_num: int, text: str, lines: list[str], dist_ranges: dict, dry_run: bool) -> list[str]:
    if dist_num not in dist_ranges:
        return [f"  ERROR: d.{dist_num} not found in raw text"]

    d_start, d_end = dist_ranges[dist_num]
    markers = find_real_markers(text, d_start, d_end)

    results = [f"d. {dist_num}: {len(markers)} markers in lines {d_start}-{d_end}"]
    for m in markers:
        results.append(f"    {m.kind:15s} {m.num or '':>3} @ line {m.line}: {m.raw}")

    chunks = compute_chunks(dist_num, d_start, d_end, markers)
    results.append(f"  → {len(chunks)} chunks computed")

    for chunk in chunks:
        result = write_skeleton(chunk, lines, dry_run)
        results.append(result)

    return results


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("range", help="Distinction(s): '10', '10-23', or 'all'")
    ap.add_argument("--dry-run", action="store_true", help="Show plan without writing")
    args = ap.parse_args()

    text = RAW.read_text(errors="replace")
    lines = text.splitlines()
    dist_ranges = get_dist_ranges(text)

    if args.range == "all":
        dists = sorted(dist_ranges.keys())
    elif "-" in args.range:
        lo, hi = args.range.split("-")
        dists = list(range(int(lo), int(hi) + 1))
    else:
        dists = [int(args.range)]

    mode = "DRY RUN" if args.dry_run else "FIXING"
    print(f"{mode} boundaries for d.{dists[0]}–d.{dists[-1]} ({len(dists)} distinctions)\n")

    for d in dists:
        results = fix_distinction(d, text, lines, dist_ranges, args.dry_run)
        for r in results:
            print(r)
        print()

    if args.dry_run:
        print("(dry run — no files written)")


if __name__ == "__main__":
    main()
