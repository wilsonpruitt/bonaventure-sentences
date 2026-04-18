#!/usr/bin/env python3.11
"""Relabel auto-chunked -dup{N} chunks to pars form -p{N}-.

For each distinction with multiple COMMENTARIUS markers in the raw text,
this tool:
  1. Finds the pars boundaries (COMMENTARIUS start lines)
  2. Reads all chunks for that distinction
  3. Assigns each chunk to a pars based on which COMMENTARIUS range it
     falls into
  4. Renames chunks to include `-p{N}-` and strips `-dup{K}` suffix
  5. Updates `id:` frontmatter to match new filename

Conservative rules:
  - littera chunks always stay as `d{D}-littera` (no pars, appears before
    first COMMENTARIUS)
  - If a distinction has only 1 COMMENTARIUS, no renaming happens
  - If no chunks for this distinction have -dup suffix, skip (already
    single-pars or manually labeled)

Usage:
    python3.11 tools/pars-relabel.py --part 2 --dry-run
    python3.11 tools/pars-relabel.py --part 2             # writes changes
    python3.11 tools/pars-relabel.py --part 2 --dist 27   # only d.27
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

RE_DISTINCTIO = re.compile(
    r"^\s*DISTINCTIO\S*\s+([IVXLCivxlc]+(?:\s*[IVXLCivxlc])*)\b",
    re.MULTILINE,
)
RE_COMMENTARIUS = re.compile(r"^\s*COMMENTARIUS\s+IN\s+D", re.MULTILINE | re.IGNORECASE)
RE_DIVISIO_LINE = re.compile(r"^(?P<line>.*\bDIVISIO\s+TEXTUS.*)$", re.MULTILINE)
# A running head looks like `DIST. XXX. ...` or `DIST. XXX. P. II. ...`
RE_RUNNING_HEAD = re.compile(r"\bDIST\.\s*[IVXLCivxlc]+", re.IGNORECASE)

ROMAN = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
    "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13,
    "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19,
    "XX": 20, "XXI": 21, "XXII": 22, "XXIII": 23, "XXIV": 24, "XXV": 25,
    "XXVI": 26, "XXVII": 27, "XXVIII": 28, "XXIX": 29, "XXX": 30,
    "XXXI": 31, "XXXII": 32, "XXXIII": 33, "XXXIV": 34, "XXXV": 35,
    "XXXVI": 36, "XXXVII": 37, "XXXVIII": 38, "XXXIX": 39, "XL": 40,
    "XLI": 41, "XLII": 42, "XLIII": 43, "XLIV": 44, "XLV": 45,
    "XLVI": 46, "XLVII": 47, "XLVIII": 48,
}


def parse_roman(s: str) -> int | None:
    s = s.strip().replace(" ", "").upper()
    if s in ROMAN:
        return ROMAN[s]
    trailing = len(s) - len(s.rstrip("L"))
    for n in range(1, trailing + 1):
        variant = s[:-n] + "I" * n
        if variant in ROMAN:
            return ROMAN[variant]
    return None


@dataclass
class Chunk:
    path: Path
    chunk_id: str
    dist: int
    line_start: int
    line_end: int
    frontmatter: str  # raw string between --- markers
    body: str

    @property
    def is_littera(self) -> bool:
        return self.chunk_id.endswith("-littera")

    @property
    def dup_num(self) -> int:
        m = re.search(r"-dup(\d+)$", self.chunk_id)
        return int(m.group(1)) if m else 1


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
    dist = int(fm.get("distinctio", 0))
    if not dist:
        return None
    return Chunk(
        path=path,
        chunk_id=path.stem,
        dist=dist,
        line_start=int(fm.get("line_start", 0)),
        line_end=int(fm.get("line_end", 0)),
        frontmatter=fm_text,
        body=body,
    )


def find_pars_boundaries(text: str) -> dict[int, list[int]]:
    """Return {dist_num: [comm_line1, comm_line2, ...]} with COMMENTARIUS lines per dist."""
    dist_markers = []
    for m in RE_DISTINCTIO.finditer(text):
        line = text[:m.start()].count("\n") + 1
        num = parse_roman(m.group(1))
        if num:
            dist_markers.append((num, line))
    seen = set()
    unique = []
    for num, line in dist_markers:
        if num not in seen:
            unique.append((num, line))
            seen.add(num)

    dist_ranges: dict[int, tuple[int, int]] = {}
    for i, (num, start) in enumerate(unique):
        end = unique[i + 1][1] - 1 if i + 1 < len(unique) else 10**9
        dist_ranges[num] = (start, end)

    # Pars boundaries in pt2 are marked by DIVISIO TEXTUS (not COMMENTARIUS as in pt1).
    # Exclude running-head lines that start with `DIST. XXX.`
    divisio_lines: list[int] = []
    for m in RE_DIVISIO_LINE.finditer(text):
        line_content = m.group("line")
        if RE_RUNNING_HEAD.search(line_content):
            continue  # running head like "DIST. XXXV. DIVISIO TEXTUS."
        line_num = text[:m.start()].count("\n") + 1
        divisio_lines.append(line_num)

    pars_boundaries: dict[int, list[int]] = {}
    for num, (ds, de) in dist_ranges.items():
        these = sorted([l for l in divisio_lines if ds <= l <= de])
        pars_boundaries[num] = these
    return pars_boundaries


def assign_pars(chunk_line: int, comm_lines: list[int]) -> int:
    """Given a chunk start line and sorted COMMENTARIUS lines, return pars (1-based)."""
    pars = 1
    for i, cl in enumerate(comm_lines):
        if chunk_line >= cl:
            pars = i + 1
    return pars


def rename_chunk(chunk: Chunk, pars: int) -> tuple[str, str]:
    """Return (new_id, new_frontmatter). Strips -dup suffix, inserts -p{pars}- after d{D}-."""
    old_id = chunk.chunk_id
    stripped = re.sub(r"-dup\d+$", "", old_id)
    new_id = re.sub(rf"^(bon-sent-I-d{chunk.dist})-", rf"\1-p{pars}-", stripped)

    lines = chunk.frontmatter.splitlines()
    new_lines = []
    seen_pars = False
    for line in lines:
        if line.startswith("id:"):
            new_lines.append(f'id: "{new_id}"')
        elif line.startswith("pars:"):
            new_lines.append(f"pars: {pars}")
            seen_pars = True
        else:
            new_lines.append(line)
    if not seen_pars:
        inserted = False
        out = []
        for line in new_lines:
            out.append(line)
            if not inserted and line.startswith("distinctio:"):
                out.append(f"pars: {pars}")
                inserted = True
        new_lines = out
    return new_id, "\n".join(new_lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--part", type=int, choices=[1, 2], required=True)
    ap.add_argument("--dist", type=int, help="Only process this distinction")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    raw_path = RAW_BY_PART[args.part]
    text = raw_path.read_text(errors="replace")
    pars_map = find_pars_boundaries(text)

    dist_range = (24, 48) if args.part == 2 else (1, 23)
    dists = [args.dist] if args.dist else range(dist_range[0], dist_range[1] + 1)

    all_chunks = []
    for f in sorted(VOL1.glob("bon-sent-I-d*-*.md")):
        c = load_chunk(f)
        if c and c.dist in dists:
            all_chunks.append(c)

    by_dist: dict[int, list[Chunk]] = {}
    for c in all_chunks:
        by_dist.setdefault(c.dist, []).append(c)

    renames: list[tuple[Path, Path, str]] = []

    for d in sorted(by_dist):
        chunks = by_dist[d]
        has_dups = any(re.search(r"-dup\d+$", c.chunk_id) for c in chunks)
        if not has_dups:
            continue

        max_pars = max(c.dup_num for c in chunks)
        pars_lines = pars_map.get(d, [])
        corroboration = f"{len(pars_lines)} real DIVISIO TEXTUS" if pars_lines else "no DIVISIO TEXTUS"
        print(f"\nd.{d}: {max_pars} pars inferred from -dup suffix ({corroboration} in raw text)")

        for c in sorted(chunks, key=lambda x: (x.line_start or 0, x.dup_num)):
            if c.is_littera:
                print(f"  keep {c.chunk_id} (littera)")
                continue
            pars = c.dup_num
            new_id, new_fm = rename_chunk(c, pars)
            if new_id == c.chunk_id:
                continue
            new_path = c.path.parent / f"{new_id}.md"
            renames.append((c.path, new_path, new_fm + "\n---\n" + c.body))
            print(f"  {c.chunk_id}  →  {new_id}")

    if not renames:
        print("\nNo changes needed.")
        return

    print(f"\n{len(renames)} renames queued.")
    if args.dry_run:
        print("Dry-run — no files written.")
        return

    collisions = [n for _, n, _ in renames if n.exists()]
    if collisions:
        print("\nERROR: target paths already exist:")
        for c in collisions:
            print(f"  {c}")
        sys.exit(1)

    for old, new, content in renames:
        new.write_text("---\n" + content)
        old.unlink()
    print(f"Wrote {len(renames)} renamed chunks.")


if __name__ == "__main__":
    main()
