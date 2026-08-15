#!/usr/bin/env python3.11
"""Steps 2 and 3 of the frozen Vol V gutter method, on one leaf or one REGION of it.

    python3.11 tools/gutter-profile.py <page> [row_lo] [row_hi] [volume]

    python3.11 tools/gutter-profile.py 372              # whole-leaf body window
    python3.11 tools/gutter-profile.py 372 0.04 0.20    # ONE region of a shared leaf

`colcrop.py` performs step 1 — it reports a measured `split_x` and the width of
the low-ink run it found. **Run width is the confidence signal, not the value.**
When the run is under ~60 px, or far above it, or the value sits off its
neighbours, the frozen method says re-profile over several row windows (step 2)
and, when those disagree, read the per-column ink profile directly and take the
band's midpoint (step 3). This does both and prints them together.

WHY THE ROW WINDOW IS AN ARGUMENT — the rule this tool exists to serve:
**a gutter is a property of a REGION, not of a page** (frozen at `bon-itin-c7`,
p. 313). A leaf where one unit ends and the next begins stacks regions in
different measures, and `colcrop`'s default 45–92 % window straddles them and
returns a value belonging to neither. In the Hexaemeron this is routine, not
exceptional: p. 353 (four regions, and the middle one — a full-measure Summarium
— has NO gutter at all), p. 368 (default 1380 on a 5 px run against a true 1356),
p. 372 (default 1311 on a 2 px run against a true 1339, the leaf both closing one
collatio and opening the next). **Pass the rows of the region you are
transcribing.**

Reading the output: a trustworthy answer looks like a 58–64 px band whose windows
agree within a few px, with a narrow ink island at its centre — that island is
Quaracchi's printed column rule, and it is on essentially every leaf. A wide or
ragged island means the window has caught text, so narrow the rows.
"""
import os
import sys

import numpy as np
from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# colcrop.py has no __main__ guard and so cannot be imported. This is its
# measure_gutter() verbatim — same profile, same thresholds. If colcrop's
# measurement ever changes, change it here too.
def measure_gutter(im, lo_frac=0.42, hi_frac=0.60,
                   row_lo=0.45, row_hi=0.92, thresh=110):
    a = np.asarray(im.convert("L"))
    H, W = a.shape
    sub = a[int(H * row_lo):int(H * row_hi), :]
    ink = (sub < thresh).sum(axis=0)
    lo, hi = int(W * lo_frac), int(W * hi_frac)
    seg = ink[lo:hi]
    m = seg.min()
    xs = [lo + i for i, v in enumerate(seg) if v <= m + 1]
    return (xs[0] + xs[-1]) // 2, xs[-1] - xs[0] + 1


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    page = int(sys.argv[1])
    row_lo = float(sys.argv[2]) if len(sys.argv) > 2 else 0.45
    row_hi = float(sys.argv[3]) if len(sys.argv) > 3 else 0.92
    vol = sys.argv[4] if len(sys.argv) > 4 else "vol5"

    src = os.path.join(REPO, "raw", "vision", vol, f"p-{page:03d}.png")
    if not os.path.exists(src):
        sys.exit(f"no plate at {src}\n"
                 f"  extract it first: python3.11 tools/extract-pages.py "
                 f"--volume {vol} --pages {page} --dpi 450")
    im = Image.open(src)
    print(f"p.{page}  rows {row_lo}-{row_hi}  ({vol})")

    # --- step 2: window consensus
    vals = []
    for lo in [row_lo + k * 0.03 for k in range(8)]:
        for hi in [row_hi - k * 0.06 for k in range(3)]:
            if hi - lo < 0.12:
                continue
            x, run = measure_gutter(im, row_lo=lo, row_hi=hi)
            vals.append((x, run))
    xs = [v[0] for v in vals]
    print("  windows: " + " ".join(f"{x}/{run}px" for x, run in vals))
    print(f"  spread: {min(xs)}-{max(xs)} ({max(xs) - min(xs)} px), "
          f"median {sorted(xs)[len(xs) // 2]}")

    # --- step 3: direct per-column ink profile
    a = np.asarray(im.convert("L"))
    H, W = a.shape
    ink = (a[int(H * row_lo):int(H * row_hi), :] < 110).sum(axis=0)
    lo, hi = int(W * 0.40), int(W * 0.62)
    nonzero = ink[ink > 0]
    thr = max(3, int(np.median(nonzero) * 0.05)) if len(nonzero) else 3
    low = [x for x in range(lo, hi) if ink[x] <= thr]
    if not low:
        print(f"  NO low-ink column anywhere in {lo}-{hi} (thr={thr}).")
        print("  This region has no gutter — it is probably full-measure matter "
              "(a Summarium, a display heading). Profile a different region.")
        return
    runs, cur = [], [low[0]]
    for x in low[1:]:
        if x == cur[-1] + 1:
            cur.append(x)
        else:
            runs.append(cur)
            cur = [x]
    runs.append(cur)
    # Drop specks before merging. A single stray low-ink column far outside the
    # band — one pixel of white between two letters — otherwise anchors the
    # merge and reports "too far apart" on a leaf whose gutter is perfectly
    # clean. Attested on p. 372 at x=1129, 180 px from the real band.
    runs = [r for r in runs if len(r) >= 5] or runs
    runs.sort(key=len, reverse=True)
    top = sorted(runs[:2], key=lambda r: r[0])
    print(f"  low-ink runs (thr={thr}): "
          + " ".join(f"{r[0]}-{r[-1]}({len(r)})" for r in top))
    band0, band1 = top[0][0], top[-1][-1]
    if band1 - band0 >= 130:
        print("  runs too far apart to merge — inspect individually; the window "
              "is probably catching text on one side.")
        return
    print(f"  BAND {band0}-{band1} ({band1 - band0 + 1} px)  "
          f"midpoint -> {(band0 + band1) // 2}")
    island = [x for x in range(band0, band1 + 1) if ink[x] > thr]
    if island:
        peak = int(max(ink[island[0]:island[-1] + 1]))
        width = island[-1] - island[0] + 1
        note = "  <-- WIDE: the window is catching text, narrow the rows" if width > 14 else ""
        print(f"  ink island (centre rule) {island[0]}-{island[-1]} "
              f"({width} px), peak {peak}{note}")


if __name__ == "__main__":
    main()
