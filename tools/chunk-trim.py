#!/usr/bin/env python3.11
"""Trim chunks whose line_end overshoots into the next semantic section.

Reads `vol1/boundary-audit-pt{N}.json` (or runs the audit internally) to
find every chunk that "contains" an embedded QUAESTIO / ARTICULUS /
DUBIA / COMMENTARIUS marker past its legitimate start. Trims line_end
to (first such marker - 1) and rewrites the Latin body from raw text.

Safe heuristic: only trims if the new length is >= 30 lines (otherwise
the chunk is probably misplaced entirely and needs manual triage).

Usage:
    python3.11 tools/chunk-trim.py --part 2 --dry-run
    python3.11 tools/chunk-trim.py --part 2
    python3.11 tools/chunk-trim.py --part 1 --dry-run
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VOL1 = REPO / "vol1"
RAW_BY_PART = {
    1: REPO / "raw" / "bonaventure_vol1_raw.txt",
    2: REPO / "raw" / "bonaventure_vol1_pt2_raw.txt",
}

MARKER_PATTERNS = [
    # Must stay in sync with auto-chunk-volume.py / chunk-fill.py / boundary-audit.py.
    ("COMMENTARIUS", re.compile(r"^[ \t]*C[O0]MMENT[AE][REI]{1,3}[US8]{1,2}\s+IN\s+D", re.MULTILINE)),
    ("ARTICULUS", re.compile(r"^[ \t]*ARTI[CGI]U[L1I]U[S8]\s+([IVXLC1ivxlc]+|U[Ii]?N[IL]?[CG]U[S8])\b", re.MULTILINE)),
    ("QUAESTIO", re.compile(r"^[ \t]*Q[UIJij1][A^.flEIJij]{0,6}STIO\s+([IVXLC1ivxlcm]+)\b", re.MULTILINE)),
    ("DUBIA", re.compile(r"^[ \t]*(?:DUB(?:IA)?[.\s]|DIST\.[^\n]*\bDUBIA\b)", re.MULTILINE)),
]
RE_RUNNING_HEAD = re.compile(r"\bDIST\.\s*[IVXLCivxlc]+", re.IGNORECASE)


@dataclass
class Chunk:
    path: Path
    chunk_id: str
    line_start: int
    line_end: int
    kind: str
    frontmatter: str
    body: str


def load_chunk(path: Path) -> Chunk | None:
    text = path.read_text()
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not m:
        return None
    fm_text, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_text.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    try:
        line_start = int(fm.get("line_start", 0))
        line_end = int(fm.get("line_end", 0))
    except ValueError:
        return None
    if not line_start or not line_end:
        return None
    # Never touch manually-cleaned chunks — raw-text rewrite would destroy the Tier-2 Latin.
    if "Tier 2" in fm.get("transcription_status", ""):
        return None
    return Chunk(
        path=path, chunk_id=path.stem,
        line_start=line_start, line_end=line_end,
        kind=fm.get("type", ""),
        frontmatter=fm_text, body=body,
    )


def find_markers(text: str) -> list[tuple[int, str]]:
    """Return sorted list of (line_num, kind) for semantic markers, ignoring running heads."""
    markers = []
    lines = text.split("\n")  # must match line-num counting (\n-based)
    for kind, pattern in MARKER_PATTERNS:
        for m in pattern.finditer(text):
            line_num = text[:m.start()].count("\n") + 1
            line_content = lines[line_num - 1] if line_num - 1 < len(lines) else ""
            if RE_RUNNING_HEAD.search(line_content):
                continue
            markers.append((line_num, kind))
    markers.sort()
    return markers


def first_interior_marker(chunk: Chunk, markers: list[tuple[int, str]]) -> int | None:
    """Find the first marker strictly after chunk.line_start that would indicate a new section.
    Skips the marker closest to line_start (that's the chunk's own opening marker)."""
    candidates = [(ln, k) for ln, k in markers
                  if chunk.line_start < ln <= chunk.line_end]
    if not candidates:
        return None
    first_ln, _ = candidates[0]
    # Check if this first candidate is really the chunk's own marker (within 5 lines)
    if first_ln - chunk.line_start <= 5:
        # It's the chunk's own marker; look for the NEXT one
        if len(candidates) >= 2:
            return candidates[1][0]
        return None
    return first_ln


def rewrite_body(body: str, old_start: int, old_end: int, new_end: int, raw_lines: list[str]) -> str:
    """Replace the Latin block's content with lines[old_start-1:new_end]."""
    latin_block = "\n".join(raw_lines[old_start - 1:new_end]).strip()
    pattern = re.compile(
        r"(## Latin\s*\n)(.*?)(\n## English|\n## Apparatus|\n## Notes|$)",
        re.DOTALL,
    )
    m = pattern.search(body)
    if not m:
        return body
    return body[:m.start(2)] + "\n" + latin_block + "\n" + body[m.end(2):]


def update_frontmatter(fm: str, new_end: int) -> str:
    out = []
    replaced = False
    for line in fm.splitlines():
        if line.startswith("line_end:"):
            out.append(f"line_end: {new_end}")
            replaced = True
        else:
            out.append(line)
    if not replaced:
        out.append(f"line_end: {new_end}")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--part", type=int, choices=[1, 2], required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-remaining", type=int, default=30, help="Skip trim if result would be shorter than this many lines")
    args = ap.parse_args()

    raw_path = RAW_BY_PART[args.part]
    text = raw_path.read_text(errors="replace")
    raw_lines = text.split("\n")  # must match line-num counting (\n-based)
    markers = find_markers(text)

    dist_range = (24, 48) if args.part == 2 else (1, 23)

    trims = []
    for f in sorted(VOL1.glob("bon-sent-I-d*-*.md")):
        c = load_chunk(f)
        if not c:
            continue
        fm = dict(line.split(":", 1) for line in c.frontmatter.splitlines() if ":" in line)
        try:
            dist = int(fm.get("distinctio", " 0").strip())
        except ValueError:
            continue
        if not (dist_range[0] <= dist <= dist_range[1]):
            continue

        interior = first_interior_marker(c, markers)
        if not interior:
            continue
        new_end = interior - 1
        if new_end <= c.line_start:
            print(f"  SKIP {c.chunk_id}: would leave empty range")
            continue
        new_len = new_end - c.line_start + 1
        if new_len < args.min_remaining:
            print(f"  SKIP {c.chunk_id}: trim would leave only {new_len} lines — manual review")
            continue
        trims.append((c, new_end))

    if not trims:
        print("No trimmable chunks.")
        return

    print(f"\n{len(trims)} chunks to trim:")
    for c, new_end in trims:
        old_len = c.line_end - c.line_start + 1
        new_len = new_end - c.line_start + 1
        print(f"  {c.chunk_id}: {c.line_start}–{c.line_end} ({old_len} lines) → {c.line_start}–{new_end} ({new_len} lines)")

    if args.dry_run:
        print("\nDry-run — no files written.")
        return

    for c, new_end in trims:
        new_fm = update_frontmatter(c.frontmatter, new_end)
        new_body = rewrite_body(c.body, c.line_start, c.line_end, new_end, raw_lines)
        c.path.write_text(f"---\n{new_fm}\n---\n{new_body}")
    print(f"\nWrote {len(trims)} trimmed chunks.")


if __name__ == "__main__":
    main()
