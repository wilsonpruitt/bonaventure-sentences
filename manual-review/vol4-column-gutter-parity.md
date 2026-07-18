# Vol IV column-gutter drift is PAGE-PARITY, not per-page noise

**Found 2026-07-18, during the d.46 run.** This supersedes the ad-hoc "regenerate at 2120 or 1620 if
a band looks clipped" advice in `CLAUDE.md` and in the d.45/d.46 session-setup notes.

## The finding

`colcrop.py vol4 <page>` defaults to a column split of **x≈1880**. That value is wrong for **every
page measured in d.46 (pp. 953–968)**. The true gutter alternates by printed-page parity:

| parity | measured gutter | what the 1880 default does |
|---|---|---|
| **odd** pages (953, 955, 957 …) | **≈1480–1580** | split is ~300–400px too far RIGHT → the R band starts *inside* the right column, cutting **the right column's opening characters on every line**; the L band carries a slab of the right column's start |
| **even** pages (954, 956, 958 …) | **≈2135–2200** | split is ~250–320px too far LEFT → the L band loses **~8 characters per line off the left column's line-ends** |

1880 sits almost exactly between the two clusters, so it is never right — it merely fails
differently depending on parity. Measured values for pp. 953–968:

```
953:1481  954:2197  955:1549  956:2135  957:1490  958:2201  959:1558  960:2193
961:1495  962:2167  963:1577  964:2178  965:1480  966:2170  967:1532  968:2179
```

## Why this is dangerous, not merely annoying

The even-page failure is loud: text visibly runs off the band, and writers noticed and regenerated.
**The odd-page failure is silent.** Losing the first character or two of a right-column line usually
still yields readable Latin, so a careful writer reconstructs it into something plausible and
reports "no `[?]` flags" in good faith. Three of the four d.46 batch-1 writers reported clean runs
on pages that were, in fact, clipped.

This is the same species of defect as the `DISTmCTIO` littera truncations: an error that produces a
*well-formed but wrong* result, and therefore survives every audit we run. The three guard-rail
audits (paraphrase / headers / apparatus-count) cannot see it — the chunk has the right number of
headers, the right number of apparatus entries, and prose that reads fine.

## Measuring the gutter (do this per page, before dispatching writers)

Run this over the extracted 450 dpi page images; it finds the widest near-blank vertical run in the
middle 40% of the page:

```python
from PIL import Image
import glob, re
Image.MAX_IMAGE_PIXELS = None
for f in sorted(glob.glob('raw/vision/vol4/*.png')):
    page = re.search(r'(\d{3})', f.split('/')[-1]).group(1)
    im = Image.open(f).convert('L'); w, h = im.size
    top, bot = int(h*0.12), int(h*0.80)
    bw = im.crop((0, top, w, bot)).point(lambda p: 255 if p < 140 else 0)
    px = bw.load(); H = bot - top; step = 4
    lo, hi = int(w*0.30), int(w*0.70)
    cols = {x: sum(1 for y in range(0, H, step) if px[x, y]) for x in range(lo, hi)}
    thr = max(1, int(0.01*(H/step)))
    runs, s = [], None
    for x in range(lo, hi):
        if cols[x] <= thr:
            if s is None: s = x
        elif s is not None:
            runs.append((x-s, s, x)); s = None
    if s is not None: runs.append((hi-s, s, hi))
    runs.sort(reverse=True)
    print(f"p.{page} gutter≈{(runs[0][1]+runs[0][2])//2}")
```

Then regenerate every page at its own measured gutter before dispatching any writer:

```bash
python3.11 tools/colcrop.py vol4 <page> <measured_gutter> 3 1.15
```

## Standing instruction for d.47–d.50 (and any Vol IV re-verify)

1. Extract the page range at 450 dpi.
2. **Measure the gutter for every page** with the snippet above.
3. Regenerate all bands at the per-page measured value.
4. Only then dispatch writers — and tell them the bands are already correct so they do not
   re-crop at a guessed split.

## Open question for the d.41–d.50 decade gate

**Earlier distinctions were almost certainly written against mis-split bands.** The d.45 session
regenerated 6 pages ad hoc at 2120/1620 — consistent with fighting this alternation without having
diagnosed it, and leaving the odd-page (silent) case largely unaddressed. Circumstantial
corroboration: while verifying d.46's littera, a writer reading p.953 at a corrected split found two
apparent misreads in the already-committed `bon-sent-IV-d45-dubia.md` apparatus —
`[^p953-6]` reads *nota 3* where the band shows **nota 5**, and `[^p953-7]` reads *d. 33. q. 1.*
where the band shows **d. 35. q. 4.**

Neither has been corrected; both are logged here for the gate. **Pass 3 of the d.41–d.50 gate should
add a gutter-parity re-check** over the decade's odd pages, in the same spirit as adding the
distinction-header seam after the `DISTmCTIO` class was found. Whether the sweep should extend back
into d.1–d.40 is an owner decision — it is a large scope and the defect is invisible to the audits,
so it needs sampling first to establish a rate.
