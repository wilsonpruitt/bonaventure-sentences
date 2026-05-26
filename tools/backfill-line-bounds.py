#!/usr/bin/env python3.11
"""Backfill missing line_start/line_end frontmatter on already-Tier-2 chunks
by parsing the raw line range out of the transcription_status string.

Targets the 10 chunks flagged by tools/audit-formatting.py with
"missing required keys: ['line_end', 'line_start']" in d.26+.
Idempotent: skip if both fields already present.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VOL1 = REPO / "vol1"

# Range pattern, e.g. "raw lines 11595–11718", "raw lines 3219–3274 of pt2",
# "(raw/bonaventure_vol1_pt2_raw.txt lines 3219–3274)".
RANGE_RE = re.compile(r"lines?\s+(\d+)[–—\-](\d+)")

CANDIDATES = [
    # Original d.26+ targets (2026-05-08).
    "bon-sent-I-d26-divisio.md",
    "bon-sent-I-d27-p1-divisio.md",
    "bon-sent-I-d27-p2-divisio.md",
    "bon-sent-I-d28-divisio.md",
    "bon-sent-I-d29-divisio.md",
    "bon-sent-I-d30-a1-q1.md",
    "bon-sent-I-d30-a1-q2.md",
    "bon-sent-I-d30-a1-q3.md",
    "bon-sent-I-d31-p1-a1-q1.md",
    "bon-sent-I-d37-p1-dubia.md",
    # d.1-d.3 backfill (2026-05-09 — 9 chunks with explicit `lines NNN-NNN`
    # in their transcription_status). The audit-formatting tool flagged 26
    # d.1-d.4 chunks as missing line bounds; these 9 are auto-parseable.
    # The other 17 lack a parseable range in their status and are deferred
    # to Task 9 (the per-chunk Tier-2 promotion pass), where each chunk's
    # line range will be located by grepping for its distinctive header.
    "bon-sent-I-d1-a1-q1.md",
    "bon-sent-I-d1-divisio.md",
    "bon-sent-I-d2-a1-q1.md",
    "bon-sent-I-d2-a1-q2.md",
    "bon-sent-I-d2-a1-q3.md",
    "bon-sent-I-d2-a1-q4.md",
    "bon-sent-I-d2-divisio.md",
    "bon-sent-I-d2-dubia.md",
    "bon-sent-I-d3-p1-divisio.md",
]

def backfill(path: Path) -> str:
    txt = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.DOTALL)
    if not m:
        return "no-frontmatter"
    fm = m.group(1)
    if re.search(r"^line_start:", fm, re.MULTILINE) and re.search(r"^line_end:", fm, re.MULTILINE):
        return "already-present"
    status_match = re.search(r"^transcription_status:\s*\"(.+)\"\s*$", fm, re.MULTILINE)
    if not status_match:
        return "no-status"
    rng = RANGE_RE.search(status_match.group(1))
    if not rng:
        return "no-range-in-status"
    start, end = int(rng.group(1)), int(rng.group(2))
    # Insert line_start/line_end right before format_version
    insertion = f"line_start: {start}\nline_end: {end}\n"
    new_fm = re.sub(r"(^format_version:)", insertion + r"\1", fm, count=1, flags=re.MULTILINE)
    if new_fm == fm:
        new_fm = fm + "\n" + insertion.rstrip()
    new_txt = "---\n" + new_fm + "\n---\n" + txt[m.end():]
    path.write_text(new_txt)
    return f"backfilled {start}-{end}"

def main() -> int:
    for name in CANDIDATES:
        p = VOL1 / name
        if not p.exists():
            print(f"  SKIP {name}: not found")
            continue
        print(f"  {name}: {backfill(p)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
