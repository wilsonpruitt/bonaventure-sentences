#!/usr/bin/env python3.11
"""Apparatus-count audit — for each chunk, count footer-glyph indicators in
the raw OCR slice for the chunk's bounds vs `[^N]:` apparatus definitions in
the chunk. Catches silent apparatus dropouts (the d.4 missing 14 page-95
entries / d.28 missing fn 3 / d.27 dropped fns 4,5,7 class of failure).

Heuristic: raw OCR footer notes typically begin with a numeral or a glyph
indicator: `1.`, `2.`, `^`, `*`, `'`, `"` at line start in the footer band.
We approximate footer footnote count by counting these markers in the raw
slice. This is noisy — running heads, page numbers, and inline marks all
contribute false positives. The tool is intended as a triage signal: a
chunk with significantly fewer apparatus defs than raw glyph indicators
deserves an eyes-on diff against the OCR footer.

Usage:
  python3.11 tools/audit-apparatus-count.py
  python3.11 tools/audit-apparatus-count.py --min-d 27 --max-d 27 --min-diff 3
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VOL1 = REPO / "vol1"
RAW_PT1 = REPO / "raw" / "bonaventure_vol1_raw.txt"
RAW_PT2 = REPO / "raw" / "bonaventure_vol1_pt2_raw.txt"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
APPARATUS_DEF_RE = re.compile(r"^\[\^[^\]]+\]:", re.MULTILINE)
APPARATUS_BLOCK_RE = re.compile(r"^## Apparatus\s*\n(.*)\Z", re.DOTALL | re.MULTILINE)
# Footer footnote indicators. Quaracchi footnote openers in the OCR follow
# three patterns:
#   1. Bare 1-2 digit + 2+ spaces:        `13  Restituimus`
#   2. Garbled glyph (1-3 punct chars):   `'*  Cap.`, `1»  Cap.`, `-"  Fide`
#   3. Lowercase roman numeral:           `i.  Cap.`, `iv  Vide`
# Body objections are also numbered (`1.  Augustinus`, `2.  Item,`) — they're
# distinguished by a *period* after the digit. So the pattern excludes
# digit-period openers via negative lookahead.
#
# Wave-5 (2026-05-09) tested against three apparatus rebuilds with known
# ground truth: 40/45, 36/36, 24/23 — close enough to ground truth to be
# a useful triage signal without forcing per-chunk eyes-on every flag.
# The previous regex `[\d]{1,2}\s*\.?\s+[A-Z]` matched body objections
# AND missed garbled openers, so it both over-flagged Tier-1 chunks and
# under-flagged genuine Tier-2 gaps (the wave-5 inverse-Lesson-8 trap).
FOOTER_NOTE_RE = re.compile(
    r"^\s*(?:\d{1,2}(?![.0-9])|[\W_]{1,3}|[ivx]{1,3}\.?)\s+[A-Z][a-zà-ÿ]",
    re.MULTILINE,
)


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    out: dict = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def count_apparatus_defs(text: str) -> int:
    m = APPARATUS_BLOCK_RE.search(text)
    block = m.group(1) if m else text
    return len(APPARATUS_DEF_RE.findall(block))


def raw_slice(distinctio: int, ls: int, le: int) -> str:
    if distinctio >= 24:
        raw = RAW_PT2.read_text(encoding="utf-8", errors="replace")
    else:
        raw = RAW_PT1.read_text(encoding="utf-8", errors="replace")
    lines = raw.splitlines()
    if ls < 1 or le > len(lines) + 5:
        return ""
    return "\n".join(lines[ls - 1 : min(le, len(lines))])


def estimate_footer_notes(slice_text: str) -> int:
    """Heuristic count of distinct footer-note openers in the slice."""
    return len(FOOTER_NOTE_RE.findall(slice_text))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-d", type=int, default=1)
    ap.add_argument("--max-d", type=int, default=48)
    ap.add_argument("--min-diff", type=int, default=5,
                    help="flag chunks where (footer_notes - apparatus_defs) >= this (default 5)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    rows = []
    for p in sorted(VOL1.glob("bon-sent-I-d*.md")):
        m = re.match(r"bon-sent-I-d(\d+)-", p.name)
        if not m:
            continue
        d = int(m.group(1))
        if not (args.min_d <= d <= args.max_d):
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        try:
            ls = int(fm.get("line_start", ""))
            le = int(fm.get("line_end", ""))
        except (ValueError, TypeError):
            continue
        slc = raw_slice(d, ls, le)
        if not slc:
            continue
        chunk_count = count_apparatus_defs(text)
        raw_count = estimate_footer_notes(slc)
        diff = raw_count - chunk_count
        status = fm.get("transcription_status", "")
        is_tier2 = status.lower().startswith("phase c tier 2 complete")
        flag = ""
        # The heuristic catches numbered body objections as false positives.
        # Two narrower signals are useful:
        #   1. chunk has 0 apparatus AND raw has many footer-like patterns
        #      (clear vestigial skeleton — d.8 legacy auto-chunked pattern)
        #   2. NOT-Tier-2 chunks with high diff (incomplete promotion)
        if chunk_count == 0 and raw_count >= 10:
            flag = "SKELETON-SUSPECT"
        elif not is_tier2 and diff >= args.min_diff:
            flag = "INCOMPLETE-SUSPECT"
        rows.append({
            "chunk": p.stem,
            "d": d,
            "raw_footer": raw_count,
            "chunk_apparatus": chunk_count,
            "diff": diff,
            "is_tier2": is_tier2,
            "flag": flag,
        })

    rows.sort(key=lambda r: -r["diff"])
    flagged = [r for r in rows if r["flag"]]

    lines = ["# Apparatus-Count Audit", ""]
    lines.append(f"Heuristic comparison of raw-OCR footer-note openers vs chunk `[^N]:` defs. Flag threshold: diff ≥ {args.min_diff}.")
    lines.append("")
    lines.append(f"**Flagged: {len(flagged)} chunks** (out of {len(rows)} audited).")
    lines.append("")
    lines.append("| Chunk | d | Raw footer | Chunk app | Diff | Flag |")
    lines.append("|---|---|---|---|---|---|")
    for r in rows[:60]:
        lines.append(f"| `{r['chunk']}` | {r['d']} | {r['raw_footer']} | {r['chunk_apparatus']} | {r['diff']:+d} | {r['flag'] or '—'} |")
    report = "\n".join(lines)

    if args.out:
        out_path = REPO / args.out
        out_path.write_text(report, encoding="utf-8")
        print(f"wrote {out_path}")
    else:
        print(report)

    if flagged:
        print(f"\n{len(flagged)} chunk(s) flagged for review:")
        for r in flagged[:20]:
            print(f"  {r['chunk']}: raw={r['raw_footer']} chunk={r['chunk_apparatus']} diff={r['diff']:+d}")
        sys.exit(1)


if __name__ == "__main__":
    main()
