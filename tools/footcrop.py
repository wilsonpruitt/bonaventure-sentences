#!/usr/bin/env python3.11
"""Crop a leaf's FOOTER REGISTER into left/right bands at high magnification.

    python3.11 tools/footcrop.py <page> <split_x> [row_lo] [row_hi] [scale] [volume]

    python3.11 tools/footcrop.py 372 1339 0.775 0.90 2.1

Writes /tmp/colcrop/<vol>-p<NNN>-F{L,R}.png, capped under the API's image limit.

WHY THIS IS NOT `colcrop.py`. colcrop slices the whole leaf into N equal bands,
which is right for reading a body column and wrong for reading a register: the
footer is a small fraction of the leaf, so an equal band shows it small, and the
apparatus is the one thing in this corpus that MUST be read large. In Vol V the
raw has no footnote numerals at all — **every apparatus entry is a hand-read off
a 450 dpi band** — so magnification is not a convenience.

★ THE RULE THIS SERVES, paid for at the Hexaemeron mid-work gate (2026-08-15):
**an apparatus entry is never transcribed from a whole-page read.** The single
defect that gate found across 152 entries was the single entry that had been
read at ⅓-scale (an English half silently normalising Quaracchi's `Dictae
salutis`). Every entry read at 1.7–2.2× was clean. Use 2.0× or better.

⚠ `split_x` is PASSED IN, not measured here, and that is deliberate: the footer
block is narrower than the column, so profiling the footer rows returns a
meaningless band (attested: 149 px on p. 313). Take the split from the BODY
region — `tools/gutter-profile.py` — and let this pad generously either side.

⚠ Finding row_lo: the footer rule sits above the register. If you do not know
where it falls, profile the leaf's ink by row first; the register is the dense
block below the blank gap. Footers here run long — a single Additamentum can
fill most of a leaf — so start higher than you expect.
"""
import os
import sys

from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_BYTES = 3_400_000  # ~4.7 MB base64 — under the 5 MB cap


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    page = int(sys.argv[1])
    split = int(sys.argv[2])
    lo = float(sys.argv[3]) if len(sys.argv) > 3 else 0.74
    hi = float(sys.argv[4]) if len(sys.argv) > 4 else 0.95
    scale = float(sys.argv[5]) if len(sys.argv) > 5 else 2.0
    vol = sys.argv[6] if len(sys.argv) > 6 else "vol5"

    src = os.path.join(REPO, "raw", "vision", vol, f"p-{page:03d}.png")
    if not os.path.exists(src):
        sys.exit(f"no plate at {src}\n"
                 f"  extract it first: python3.11 tools/extract-pages.py "
                 f"--volume {vol} --pages {page} --dpi 450")

    im = Image.open(src)
    W, H = im.size
    y0, y1 = int(H * lo), int(H * hi)
    outdir = "/tmp/colcrop"
    os.makedirs(outdir, exist_ok=True)

    cols = {"FL": (0, min(split + 90, W)), "FR": (max(split - 90, 0), W)}
    for name, (x0, x1) in cols.items():
        crop = im.crop((x0, y0, x1, y1))
        crop = crop.resize((int(crop.width * scale), int(crop.height * scale)),
                           Image.LANCZOS)
        outp = os.path.join(outdir, f"{vol}-p{page:03d}-{name}.png")
        crop.save(outp)
        while os.path.getsize(outp) > MAX_BYTES and min(crop.size) > 200:
            crop = crop.resize((int(crop.width * .85), int(crop.height * .85)),
                               Image.LANCZOS)
            crop.save(outp)
        eff = crop.width / (x1 - x0)
        flag = "   ⚠ shrunk below 1.5× — crop fewer rows and read in two passes" if eff < 1.5 else ""
        print(f"{outp}  {crop.size}  {os.path.getsize(outp) // 1024} KB  "
              f"effective {eff:.2f}×{flag}")


if __name__ == "__main__":
    main()
