#!/usr/bin/env python3.11
"""Backfill line_start/line_end for the 17 d.3-d.4 chunks Task 8 deferred.

Their transcription_status strings don't carry explicit `lines NNN-NNN`,
so ranges were located by grepping raw OCR for canonical structural
headers (DIVISIO TEXTUS, TRACTATIO QUAESTIONUM, ARTICULUS, QUAESTIO,
DUBIA) and bracketing each chunk between adjacent markers.

Idempotent: skip if both fields already present. Run once, then delete
or leave alongside backfill-line-bounds.py for the audit log.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VOL1 = REPO / "vol1"

# (filename, line_start, line_end) — see resolution log for derivation.
RANGES = [
    # d.3 pars 1
    ("bon-sent-I-d3-p1-a1-q1.md", 19050, 19635),
    ("bon-sent-I-d3-p1-a1-q2.md", 19636, 20073),
    ("bon-sent-I-d3-p1-a1-q4.md", 20302, 20562),
    ("bon-sent-I-d3-p1-dubia.md", 20563, 21005),
    # d.3 pars 2
    ("bon-sent-I-d3-p2-divisio.md", 21006, 21034),
    ("bon-sent-I-d3-p2-a1-q1.md", 21035, 21367),
    ("bon-sent-I-d3-p2-a1-q2.md", 21368, 21663),
    ("bon-sent-I-d3-p2-a1-q3.md", 21664, 22244),
    ("bon-sent-I-d3-p2-a2-q1.md", 22245, 22680),
    ("bon-sent-I-d3-p2-a2-q2.md", 22681, 22913),
    ("bon-sent-I-d3-p2-dubia.md", 23056, 23296),
    # d.4
    ("bon-sent-I-d4-littera.md", 23297, 23486),
    ("bon-sent-I-d4-divisio.md", 23487, 23583),
    ("bon-sent-I-d4-a1-q1.md", 23584, 23973),
    ("bon-sent-I-d4-a1-q3.md", 24233, 24413),
    ("bon-sent-I-d4-a1-q4.md", 24414, 24633),
    ("bon-sent-I-d4-dubia.md", 24634, 25060),
]


def backfill(path: Path, start: int, end: int) -> str:
    txt = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.DOTALL)
    if not m:
        return "no-frontmatter"
    fm = m.group(1)
    if re.search(r"^line_start:", fm, re.MULTILINE) and re.search(r"^line_end:", fm, re.MULTILINE):
        return "already-present"
    insertion = f"line_start: {start}\nline_end: {end}\n"
    new_fm = re.sub(r"(^format_version:)", insertion + r"\1", fm, count=1, flags=re.MULTILINE)
    if new_fm == fm:
        new_fm = fm + "\n" + insertion.rstrip()
    new_txt = "---\n" + new_fm + "\n---\n" + txt[m.end():]
    path.write_text(new_txt)
    return f"backfilled {start}-{end}"


def main() -> int:
    for name, start, end in RANGES:
        p = VOL1 / name
        if not p.exists():
            print(f"  SKIP {name}: not found")
            continue
        print(f"  {name}: {backfill(p, start, end)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
