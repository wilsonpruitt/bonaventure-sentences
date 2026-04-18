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

# Broad OCR-tolerant patterns
RE_DISTINCTIO = re.compile(
    r"^\s*DISTINCTIO\S*\s+([IVXLCivxlc]+(?:\s*[IVXLCivxlc])*)\b",
    re.MULTILINE,
)
RE_COMMENTARIUS = re.compile(
    r"^\s*COMMENTARIUS\s+IN\s+D",
    re.MULTILINE | re.IGNORECASE,
)
RE_DIVISIO = re.compile(
    r"DIVISIO\s+TEXTUS",
    re.MULTILINE | re.IGNORECASE,
)
RE_QUAESTIO = re.compile(
    r"^\s*Q[UIJij1][A^.flEIJij]{0,6}STIO\s+([IVXLCivxlc]+)\b",
    re.MULTILINE,
)
RE_ARTICULUS = re.compile(
    r"^\s*ARTI[CG]ULUS\s+([IVXLC]+|UNICUS)\b",
    re.MULTILINE,
)
RE_DUBIA = re.compile(
    r"^\s*DUB(?:IA)?\s",
    re.MULTILINE,
)
RE_PARS = re.compile(
    r"^\s*PARS\s+(I{1,3}|PRIMA|SECUNDA)\b",
    re.MULTILINE | re.IGNORECASE,
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
    if s in ROMAN:
        return ROMAN[s]
    # OCR fallback: lowercase-L was misread as I, then .upper() turned it into L.
    # Try replacing 1..N trailing Ls with Is — least aggressive first.
    trailing = len(s) - len(s.rstrip("L"))
    for n in range(1, trailing + 1):
        variant = s[:-n] + "I" * n
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
    appear within 30 lines, keep only the second (the real header)."""
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

    # Dedupe: if same distinctio number appears multiple times, keep first
    seen = {}
    unique = []
    for m in dist_markers:
        if m.num not in seen:
            seen[m.num] = m
            unique.append(m)
        else:
            # Keep the one that's further in the text (more likely the real one)
            pass

    ranges = []
    for i, m in enumerate(unique):
        start = m.line
        end = unique[i + 1].line - 1 if i + 1 < len(unique) else total_lines
        ranges.append((m.num, start, end))
    return ranges


def chunk_distinction(
    dist_num: int,
    start: int,
    end: int,
    markers: list[Marker],
    vol: int,
    book: int,
) -> list[Chunk]:
    """Split a distinction range into chunks based on sub-markers."""
    sub = [m for m in markers if start <= m.line <= end and m.kind != "distinctio"]

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
        chunks.append(Chunk(f"{prefix}-littera", start, littera_end, "littera", dist_num))

    # If no quaestio markers at all, treat entire commentary as one chunk
    if not quaestio_markers:
        comm_start = commentarius_lines[0] if commentarius_lines else start
        chunks.append(Chunk(f"{prefix}-commentary", comm_start, end, "commentary", dist_num))
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
    divisio_start = None
    i = 0
    while i < len(boundaries):
        line, kind, num = boundaries[i]
        next_line = boundaries[i + 1][0] if i + 1 < len(boundaries) else end + 1

        if kind == "commentarius":
            # Commentarius intro — might include divisio
            pass
        elif kind == "divisio":
            # Divisio textus — runs until next articulus or quaestio
            chunks.append(Chunk(f"{prefix}-divisio", line, next_line - 1, "divisio", dist_num))
        elif kind == "articulus":
            cur_art = num or cur_art
        elif kind == "quaestio":
            q_end = next_line - 1
            chunk_id = f"{prefix}-a{cur_art}-q{num}"
            chunks.append(Chunk(
                chunk_id, line, q_end, "quaestio", dist_num,
                articulus=cur_art, quaestio=num,
            ))
        elif kind == "dubia":
            chunks.append(Chunk(f"{prefix}-dubia", line, end, "dubia", dist_num))
            i += 1
            continue
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
        chunks = chunk_distinction(dist_num, d_start, d_end, markers, vol, book_for_vol(vol))
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
