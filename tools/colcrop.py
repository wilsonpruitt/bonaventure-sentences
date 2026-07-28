#!/usr/bin/env python3.11
"""Crop a Quaracchi two-column page into readable bands.

Usage: python3.11 tools/colcrop.py vol2 43 [split_x|auto] [n_bands] [scale]
Writes /tmp/colcrop/<vol>-p<NNN>-<col>-<i>.png

split_x may be `auto` (or omitted for vol5, where auto is the default) to
measure the gutter from the image instead of trusting a constant. See
measure_gutter() for why the measurement is restricted to the body rows.
"""
import sys, os
from PIL import Image


def measure_gutter(im, lo_frac=0.42, hi_frac=0.60,
                   row_lo=0.45, row_hi=0.92, thresh=110):
    """Locate the inter-column gutter as the lowest-ink column band.

    Restricted to the BODY ROWS (row_lo..row_hi of page height) on purpose.
    A page that opens a work, a part, or a distinction carries a full-width
    display heading that crosses the gutter; profiling the whole page height
    then returns no usable blank run at all (Vol V pp. 201, 219). Footer
    registers and running heads are excluded for the same reason.

    Returns (split_x, run_width). A run_width under ~15 px means the
    measurement FAILED — do not use it; re-measure over a narrower row
    window and confirm visually. Quaracchi gutters alternate by page parity,
    so a value far outside the volume's parity cluster is also suspect.
    """
    import numpy as np
    a = np.asarray(im.convert("L"))
    H, W = a.shape
    sub = a[int(H * row_lo):int(H * row_hi), :]
    ink = (sub < thresh).sum(axis=0)
    lo, hi = int(W * lo_frac), int(W * hi_frac)
    seg = ink[lo:hi]
    m = seg.min()
    xs = [lo + i for i, v in enumerate(seg) if v <= m + 1]
    return (xs[0] + xs[-1]) // 2, xs[-1] - xs[0] + 1


vol = sys.argv[1]
page = int(sys.argv[2])
_arg = sys.argv[3] if len(sys.argv) > 3 else None
# vol5 pages are 2571 px wide at 450 dpi — the 1660 default sits deep inside
# the right column, padding L with gutter+right text and truncating R. Never
# let a constant stand in for a measurement on this volume.
if _arg is None:
    split_x = "auto" if vol == "vol5" else 1660
elif _arg == "auto":
    split_x = "auto"
else:
    split_x = int(_arg)
n = int(sys.argv[4]) if len(sys.argv) > 4 else 3
scale = float(sys.argv[5]) if len(sys.argv) > 5 else 1.8

src = f"raw/vision/{vol}/p-{page:03d}.png"
im = Image.open(src)
W, H = im.size
outdir = "/tmp/colcrop"
os.makedirs(outdir, exist_ok=True)

# Anthropic API rejects any image whose base64 payload exceeds 5 MB
# (messages.N.content.M: 400). base64 inflates ~1.37x, so cap the PNG on
# disk at MAX_BYTES; shrink-to-fit if an upscaled band would blow past it.
MAX_BYTES = 3_600_000  # ~4.9 MB once base64-encoded — safely under the 5 MB cap

def save_under_cap(crop, outp):
    crop.save(outp)
    while os.path.getsize(outp) > MAX_BYTES and min(crop.size) > 200:
        crop = crop.resize((int(crop.width * 0.85), int(crop.height * 0.85)), Image.LANCZOS)
        crop.save(outp)
    return crop

if split_x == "auto":
    split_x, run = measure_gutter(im)
    flag = "  ⚠ WEAK RUN — verify visually before trusting" if run < 15 else ""
    print(f"measured gutter: split_x={split_x} (low-ink run {run} px, "
          f"page {W}x{H}){flag}")

cols = {"L": (0, min(split_x + 60, W)), "R": (max(split_x - 60, 0), W)}
band_h = H // n
overlap = 220
for cname, (x0, x1) in cols.items():
    for i in range(n):
        y0 = max(0, i * band_h - overlap)
        y1 = min(H, (i + 1) * band_h + overlap)
        crop = im.crop((x0, y0, x1, y1))
        nw = int(crop.width * scale)
        nh = int(crop.height * scale)
        crop = crop.resize((nw, nh), Image.LANCZOS)
        outp = f"{outdir}/{vol}-p{page:03d}-{cname}-{i}.png"
        crop = save_under_cap(crop, outp)
        print(outp, crop.size, f"{os.path.getsize(outp)//1024} KB")
