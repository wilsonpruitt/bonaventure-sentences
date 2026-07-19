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

---

# ★★ 2026-07-19 — MEASURED IN VOLS II AND III. THE DEFECT REACHES BOTH. NOT EXONERATED.

This was run as step 3 of `vol4-defect-classes-and-vol1-3-tests.md`, in the hope it would clear
Vols II and III cheaply. **It did the opposite.** Both volumes show the same parity-alternating
gutter as Vol IV, and both were written against `colcrop.py`'s default split of **1660**.

Measured gutters (450 dpi, sample across each volume):

| vol | odd pages | even pages | default used | odd error | even error |
|---|---|---|---|---|---|
| **II** | ~1499–1568 (mean ≈1539) | ~1786–1890 (mean ≈1835) | 1660 | **≈121 px too far RIGHT** | ≈175 px too far LEFT |
| **III** | ~1496–1574 (mean ≈1533) | ~1632–1748 (mean ≈1697) | 1660 | **≈127 px too far RIGHT** | ≈37 px too far left (minor) |

**The direction matters more than the magnitude.** A split too far RIGHT means the R band begins
*inside* the right column and shaves the opening character(s) off every line — the **silent** mode.
A split too far LEFT clips the left column's line-*ends* — the loud mode writers notice and fix.

* **Vol II** suffers both: loud on even pages (likely caught and regenerated at the time), silent on odd.
* **Vol III** is almost entirely the **silent** mode. Its even pages are close enough to the default
  to be fine; its odd pages are consistently ~127 px too far right.

## Visual confirmation — Vol III p.601, cropped at the default 1660

Measurement only *predicts* clipping, so it was confirmed by eye. Every right-column line on that
page loses its opening character(s):

```
nomen caritatis   -> iomen caritatis      rationem virtutis -> ionem virtutis
sicut credere     -> icut credere         alii articuli     -> lii articuli
fides non est     -> ides non est         peccatore non est -> eccatore non est
perfectio virtutis-> ectio virtutis       credit, quia      -> redit, quia
quia errorem      -> uia errorem          sine alio         -> ine alio
```

**This is the silent failure in its pure form.** `ides non est in eis virtus` and `redit, quia non
omnia credit` still read as plausible Latin; a careful writer reconstructs them in good faith and
reports a clean run. Between 1 and 4 characters are lost per line.

## What this means

**Vols II and III are published, and Vol III is LIVE.** Every chunk in them whose source page was an
odd-numbered page was written from a band missing the first characters of every right-column line.
Most such losses reconstruct correctly from context. Some will not have.

**This is NOT a claim that specific text is wrong** — no Vol II/III chunk has been re-verified against
a correctly-cropped band yet. It is a claim that the *conditions* that produced the d.46 defect were
present throughout both volumes.

## Suggested next step — sample before scoping

Do **not** open a full re-verify on this. Take a handful of Vol III chunks whose pages are odd,
re-crop at the measured gutter, and diff the right-column line-openings against what the chunk says.
That establishes a *rate*. The rate decides whether this is a footnote or a campaign. Sizing the
sweep before knowing the rate would be guessing.

---

# ★★★ 2026-07-19 (later the same day) — RATE ESTABLISHED: **0 errors in 331 lines.** THE ALARM ABOVE IS OVERSTATED.

The section immediately above concluded that Vols II and III were compromised. **That conclusion was
wrong in its most important respect, and this section corrects it.** The measurement was right; the
inference from it was not.

## The mechanism: a mis-split MISFILES text, it does not DESTROY it

`colcrop.py` cuts the page into `L = 0 → split` and `R = split → width`. **Those two bands together
always cover the whole page.** Nothing is discarded. So when the split sits to the RIGHT of the true
gutter, the right column's opening characters do not vanish — **they appear at the right-hand edge of
the LEFT band.**

Verified directly on Vol III p.601, cropped at the bad split of 1660: the left band's right margin
carries a legible vertical strip reading `nomer`, `tionen`, `gere`, `sicut`, `alii`, `aliqui`,
`fides`, `peccat`, `fectio`, `deest`, `perat`, `tum;`, `sine`, `credit`, `quia`, `cendu`, `perfec`,
`tur an` — exactly the characters "missing" from the right band.

The standing instruction has always been to read **Left column top→bottom, then Right**. A writer
following it sees both halves. The same logic holds in the other direction: a split too far LEFT
pushes the left column's line-*endings* into the start of the R band, equally recoverable.

## The empirical rate

Eight Vol III pages sampled across the whole volume (pp. 101, 139, 243, 413, 451, 561, 601, 687),
each re-cropped at its own measured gutter and diffed line-opening by line-opening against the
published chunk:

| page | chunk | lines examined | clipping errors |
|---|---|---|---|
| 101 | III-d4-a1-q2 | 31 + scholion | 0 |
| 139 | III-d5-a2-q4 | 48 | 0 |
| 243 | III-d11-divisio / a1-q1 | 33 | 0 |
| 413 | III-d19-dubia | 32 | 0 |
| 451 | III-d22-a1-q1 | 50 | 0 |
| 561 | III-d26-a1-q3 | 34 | 0 |
| 601 | III-d27-a1-q4 | 45 | 0 |
| 687 | III-d31-a2-q3 | 58 | 0 |
| **total** | | **331** | **0** |

p.601 is the decisive case: it is the page whose bad crop was confirmed by eye, and **every one of
its nine known clip-risk words is correct in the published chunk** — `nomen`, `rationem`, `sicut`,
`alii`, `fides`, `peccatore`, `perfectio`, `credit`, `quia`. The writers reconstructed correctly
because the characters were in front of them in the other band.

## Verdict

**No sweep is warranted.** The gutter-parity defect is a working nuisance — it makes bands awkward to
read and it wastes writer effort — not a corruption of the published text. Vols II and III do not
need re-verification on this account.

**What remains true:** measuring the gutter per page is still the right procedure for new work
(d.48–d.50), because it removes the reconstruction burden rather than relying on writers to notice a
stray strip. But it is a quality-of-work improvement, not a data-integrity fix.

## Incidental finding — a different, small, pre-existing class

The same eight pages turned up **five apparatus/citation misreads** unrelated to cropping, roughly
0.5 per page, all in notes rather than body text:

* p.101 scholion III — printed `t. IV. q. 32.` → chunk `l. IV. q. 32.` (*tomus* read as *liber*)
* p.413 note 5 — printed `Eccli. 15, 14` → chunk `Eccli. 13, 14` (15:14 is the correct locus for *in manu consilii sui*)
* p.601 apparatus — printed `habent bis diligat` → chunk `habent his diligat`
* p.687 scholion II — printed `a. 4` twice → chunk `a. 1` twice
* p.243 — the marginal rubric `Pro parte negativa.` is not carried

Low severity (none touch Bonaventure's argument) but real, and a rate of ~0.5/page across a published
volume is worth a decision separately from the crop question. One sampler declined to call a sixth
(`codd. R U` vs `K U`) as genuinely ambiguous at 450 dpi — correct discipline.

## Measured gutters — d.49 range, pp.997–1032 (2026-07-19)

Measured per page with the snippet above and all bands regenerated at the measured value
(`colcrop.py vol4 <page> <gutter> 3 1.15`). The parity pattern holds exactly as in d.46–d.48:
**odd ≈1581–1670, even ≈2037–2138.** `colcrop.py`'s default 1880 sits between the clusters and is
wrong for every page in this range.

```
997:1619  998:2131  999:1601  1000:2098 1001:1620 1002:2090 1003:1594 1004:2096
1005:1631 1006:2052 1007:1634 1008:2077 1009:1619 1010:2080 1011:1581 1012:2077
1013:1661 1014:2087 1015:1601 1016:2118 1017:1608 1018:2093 1019:1670 1020:2042
1021:1616 1022:2138 1023:1616 1024:2108 1025:1648 1026:2136 1027:1642 1028:2080
1029:1645 1030:2037 1031:1630 1032:2121
```

p.999-R-0 spot-verified: no first-character clipping, marginalia (`Solvitur.`, `Aliter.`) captured.

**⚠ Eight pages measured with a very narrow blank run** — the columns nearly abut, so the detected
gutter rests on few pixels: **p.999 (3px), p.1021 (4px), p.1011 (5px), p.1015 (6px), p.1027 (8px),
pp.1010/1023 (10px), p.1024 (12px)**. All centres fall inside the expected parity cluster and p.999
verified clean by eye, so they are being used as measured — but if a writer reports a band on one of
these looking clipped, re-measure that page rather than guessing a split.
