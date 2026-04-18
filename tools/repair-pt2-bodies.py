#!/usr/bin/env python3.11
"""Repair pt2 chunk Latin bodies.

The pipeline had a counting-mismatch bug: frontmatter line_start/line_end were
computed with `\\n`-counting (text[:pos].count("\\n") + 1), but body extraction
used `text.splitlines()`. Because the raw text contains form-feed characters,
`splitlines()` produces more rows than split("\\n"), so chunks' Latin bodies
drifted 100–140 lines before their actual semantic anchors.

This script re-extracts each pt2 chunk's Latin body using split("\\n") at the
existing \\n-indexed line_start/line_end — the line numbers are already correct;
only the body content needs refreshing.

Safe to re-run: it only rewrites the `## Latin` section and leaves English,
Apparatus, Notes untouched. Tier-2 chunks that have a populated English section
are skipped by default to avoid disturbing manual translations (override with
--include-tier2).
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VOL1 = REPO / "vol1"
RAW_PT2 = REPO / "raw" / "bonaventure_vol1_pt2_raw.txt"


def load_chunks(dist_range: tuple[int, int]) -> list[Path]:
    paths = []
    for p in sorted(VOL1.glob("bon-sent-I-d*.md")):
        m = re.match(r"bon-sent-I-d(\d+)-", p.name)
        if not m:
            continue
        d = int(m.group(1))
        if dist_range[0] <= d <= dist_range[1]:
            paths.append(p)
    return paths


def parse_frontmatter(text: str) -> tuple[dict, str, str]:
    """Return (fm_dict, fm_raw_block_with_delimiters, body_after_frontmatter)."""
    m = re.match(r"^(---\n(.*?)\n---\n)(.*)$", text, re.DOTALL)
    if not m:
        raise ValueError("no frontmatter")
    fm_block = m.group(1)
    fm_body = m.group(2)
    rest = m.group(3)
    fm = {}
    for line in fm_body.splitlines():
        mm = re.match(r"(\w+):\s*(.+?)\s*$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2)
    return fm, fm_block, rest


def replace_latin_body(rest: str, new_latin: str) -> str:
    """Replace content between `## Latin` and the next top-level section
    (`## English` / `## Apparatus` / `## Notes` / end-of-file).
    Preserves section ordering and everything outside `## Latin`.
    """
    pat = re.compile(
        r"(## Latin\s*\n)(.*?)(\n## (?:English|Apparatus|Notes)|\Z)",
        re.DOTALL,
    )
    m = pat.search(rest)
    if not m:
        raise ValueError("no ## Latin section found")
    return rest[:m.start(2)] + "\n" + new_latin + "\n" + rest[m.end(2):]


def is_tier2(rest: str) -> bool:
    """Heuristic: Tier-2 chunks have non-placeholder content after `## English`."""
    m = re.search(r"## English\s*\n(.*?)(?:\n## |\Z)", rest, re.DOTALL)
    if not m:
        return False
    eng = m.group(1).strip()
    return bool(eng) and "[Translation pending]" not in eng


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dist-min", type=int, default=24)
    ap.add_argument("--dist-max", type=int, default=48)
    ap.add_argument("--include-tier2", action="store_true",
                    help="Also repair chunks that already have English translations")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", type=str, help="Repair only this chunk id (e.g. bon-sent-I-d30-a1-q1)")
    args = ap.parse_args()

    text = RAW_PT2.read_text(errors="replace")
    nl_lines = text.split("\n")
    print(f"Raw text: {len(nl_lines)} \\n-lines ({len(text.splitlines())} splitlines lines)")

    paths = load_chunks((args.dist_min, args.dist_max))
    if args.only:
        paths = [p for p in paths if p.stem == args.only]
        if not paths:
            raise SystemExit(f"no chunk matches --only {args.only!r}")
    print(f"Candidates: {len(paths)}")

    stats = {"rewritten": 0, "skipped_tier2": 0, "skipped_no_lines": 0, "errors": 0}
    for p in paths:
        try:
            original = p.read_text()
            fm, fm_block, rest = parse_frontmatter(original)
            ls = fm.get("line_start")
            le = fm.get("line_end")
            if not ls or not le:
                stats["skipped_no_lines"] += 1
                continue
            ls_i, le_i = int(ls), int(le)

            if not args.include_tier2 and is_tier2(rest):
                stats["skipped_tier2"] += 1
                print(f"  skip (Tier-2): {p.name}")
                continue

            new_body = "\n".join(nl_lines[ls_i - 1:le_i]).rstrip()
            # Update word_count to reflect new body
            wc = len(new_body.split())
            new_fm_block = re.sub(
                r"(word_count_latin:\s*)\d+",
                lambda m: f"{m.group(1)}{wc}",
                fm_block,
            )
            new_rest = replace_latin_body(rest, new_body)
            new_text = new_fm_block + new_rest
            if new_text == original:
                print(f"  unchanged: {p.name}")
                continue
            if args.dry_run:
                print(f"  would rewrite: {p.name} (wc {fm.get('word_count_latin')} → {wc})")
            else:
                p.write_text(new_text)
                print(f"  rewrote: {p.name} (wc {fm.get('word_count_latin')} → {wc})")
            stats["rewritten"] += 1
        except Exception as e:
            print(f"  ERROR {p.name}: {e}")
            stats["errors"] += 1

    print("\nSummary:", stats)


if __name__ == "__main__":
    main()
