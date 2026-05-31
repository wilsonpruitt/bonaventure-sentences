#!/usr/bin/env python3.11
"""Crop a Quaracchi two-column page into readable bands.

Usage: python3.11 tools/colcrop.py vol2 43 [split_x] [n_bands] [scale]
Writes /tmp/colcrop/<vol>-p<NNN>-<col>-<i>.png
"""
import sys, os
from PIL import Image

vol = sys.argv[1]
page = int(sys.argv[2])
split_x = int(sys.argv[3]) if len(sys.argv) > 3 else 1660
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
