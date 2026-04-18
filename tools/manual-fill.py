#!/usr/bin/env python3.11
"""Write a chunk skeleton from a manually-located raw-text range.

Use this when `chunk-fill.py` couldn't auto-anchor a missing chunk
(e.g. pt2 divisios with no DIVISIO TEXTUS marker, d.17 entirely missing,
running-head-corrupted boundaries).

Infers the chunk_id from --dist / --type / --pars / --articulus / --quaestio
unless --chunk-id is given explicitly. Refuses to overwrite existing chunks
unless --force is set.

Examples:
    # Missing divisio in pt2 d.30 — found in PDF at printed pp. 511-512 (pt2 line 10290-10330):
    python3.11 tools/manual-fill.py --part 2 --dist 30 --type divisio --lines 10290-10330

    # d.17 distinction entirely missing — create littera after locating real line range:
    python3.11 tools/manual-fill.py --part 1 --dist 17 --type littera --lines 55211-55307

    # Multi-pars divisio:
    python3.11 tools/manual-fill.py --part 2 --dist 43 --pars 2 --type divisio --lines 34100-34150

    # Explicit chunk id:
    python3.11 tools/manual-fill.py --part 1 --chunk-id bon-sent-I-d17-p1-a1-q1 --type quaestio --lines 55308-55650
"""
from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VOL1 = REPO / "vol1"
RAW_BY_PART = {
    1: REPO / "raw" / "bonaventure_vol1_raw.txt",
    2: REPO / "raw" / "bonaventure_vol1_pt2_raw.txt",
}


def parse_lines(s: str) -> tuple[int, int]:
    m = re.fullmatch(r"(\d+)\s*[-–]\s*(\d+)", s.strip())
    if not m:
        raise ValueError(f"--lines must be START-END (got {s!r})")
    a, b = int(m.group(1)), int(m.group(2))
    if a >= b:
        raise ValueError(f"--lines: START ({a}) must be < END ({b})")
    return a, b


def infer_chunk_id(dist: int, kind: str, pars: int | None, art: int | None, q: int | None) -> str:
    parts = [f"bon-sent-I-d{dist}"]
    if pars is not None:
        parts.append(f"p{pars}")
    if kind in ("littera", "divisio", "dubia"):
        parts.append(kind)
    elif kind == "quaestio":
        if art is None or q is None:
            raise ValueError("quaestio chunks need both --articulus and --quaestio")
        parts.append(f"a{art}-q{q}")
    else:
        raise ValueError(f"unknown --type: {kind}")
    return "-".join(parts)


def build_skeleton(chunk_id: str, dist: int, kind: str, pars: int | None,
                   art: int | None, q: int | None, line_start: int, line_end: int,
                   raw_lines: list[str], pdf_pages: str | None) -> str:
    body = "\n".join(raw_lines[line_start - 1:line_end]).strip()
    word_count = len(body.split())

    fm = [
        f'id: "{chunk_id}"',
        "volume: 1",
        "book: 1",
        f"distinctio: {dist}",
    ]
    if pars is not None:
        fm.append(f"pars: {pars}")
    if art is not None:
        fm.append(f"articulus: {art}")
    if q is not None:
        fm.append(f"quaestio: {q}")
    fm.extend([
        f"type: {kind}",
        f"line_start: {line_start}",
        f"line_end: {line_end}",
        f"word_count_latin: {word_count}",
    ])
    if pdf_pages:
        fm.append(f'pdf_pages_source: "{pdf_pages}"')
    fm.extend([
        f'transcription_status: "manual-fill {datetime.date.today()} (line range located by hand)"',
        "format_version: 1",
    ])

    return f"""---
{chr(10).join(fm)}
---

# {chunk_id}

## Latin

{body}

## English

[Translation pending]

## Apparatus

[Apparatus pending]

## Notes

[Notes pending]
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--part", type=int, choices=[1, 2], required=True)
    ap.add_argument("--dist", type=int, help="Distinction number (needed unless --chunk-id given)")
    ap.add_argument("--type", dest="kind", choices=["littera", "divisio", "dubia", "quaestio"], required=True)
    ap.add_argument("--pars", type=int, default=None)
    ap.add_argument("--articulus", type=int, default=None)
    ap.add_argument("--quaestio", type=int, default=None)
    ap.add_argument("--chunk-id", default=None, help="Override the auto-inferred id")
    ap.add_argument("--lines", required=True, help="Raw-text line range, e.g. 10290-10330")
    ap.add_argument("--pdf-pages", default=None, help="Printed-page range to record in frontmatter (e.g. 511-512)")
    ap.add_argument("--force", action="store_true", help="Overwrite if the file already exists")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    try:
        line_start, line_end = parse_lines(args.lines)
    except ValueError as e:
        sys.exit(f"ERROR: {e}")

    if args.chunk_id:
        chunk_id = args.chunk_id
        dist = args.dist
        if dist is None:
            m = re.search(r"-d(\d+)-", chunk_id)
            if not m:
                sys.exit("ERROR: cannot infer --dist from --chunk-id; pass --dist explicitly")
            dist = int(m.group(1))
    else:
        if args.dist is None:
            sys.exit("ERROR: --dist is required unless --chunk-id is given")
        try:
            chunk_id = infer_chunk_id(args.dist, args.kind, args.pars, args.articulus, args.quaestio)
        except ValueError as e:
            sys.exit(f"ERROR: {e}")
        dist = args.dist

    raw_path = RAW_BY_PART[args.part]
    text = raw_path.read_text(errors="replace")
    raw_lines = text.split("\n")  # line numbers are \n-indexed (matches auto-chunk's text[:pos].count("\n") + 1) — splitlines() also splits on form-feed and drifts
    if line_end > len(raw_lines):
        sys.exit(f"ERROR: line_end {line_end} exceeds raw-text length {len(raw_lines)}")

    out_path = VOL1 / f"{chunk_id}.md"
    if out_path.exists() and not args.force:
        sys.exit(f"ERROR: {out_path.name} already exists. Use --force to overwrite.")

    content = build_skeleton(
        chunk_id=chunk_id, dist=dist, kind=args.kind,
        pars=args.pars, art=args.articulus, q=args.quaestio,
        line_start=line_start, line_end=line_end,
        raw_lines=raw_lines, pdf_pages=args.pdf_pages,
    )

    print(f"Chunk id:    {chunk_id}")
    print(f"Line range:  {line_start}–{line_end} ({line_end - line_start + 1} lines)")
    print(f"Target:      {out_path.relative_to(REPO)}")
    preview = "\n".join(raw_lines[line_start - 1:line_start + 2])
    print(f"First lines: {preview[:200]!r}")

    if args.dry_run:
        print("\nDry-run — no file written.")
        return

    out_path.write_text(content)
    print(f"\nWrote {out_path.relative_to(REPO)}.")


if __name__ == "__main__":
    main()
