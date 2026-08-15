# Vol V — *Collationes in Hexaëmeron*: SHAKEDOWN GATE (2026-08-14)

The first of this work's three gates, fired at the close of **Collatio IV** per the frozen
cadence (a shakedown at the first structural seam ~15–25 printed pages in). Scope:
**`bon-hex-c1` … `bon-hex-c4`, printed pp. 329–353, 25 leaves, 130 numbered paragraphs.**

**Result: ZERO corpus defects.** Every finding below is a measurement, a checked negative, or a
pre-existing issue in another volume that this gate authorises no edit to.

---

## Pass 1 — `[?]` flag resolution: NOTHING TO RESOLVE, verified not assumed

`grep -n "\[?\]" vol5/bon-hex-*.md` returns exactly four hits, **one per chunk, and every one of
them is the frontmatter prose declaring the absence** (*"zero [?] flags"*). No inline flag stands
in any body, apparatus entry or `## Notes` across the four chunks. Recorded as a checked negative,
as at the Itinerarium and *de reductione* gates.

## Pass 2 — style/formatting audit, full corpus

`polish-style-scan.py` over all 2,028 chunks: **vol5 CLEAN (94 files).** Corpus-wide it reports
**10 PAIR issues across 5 chunks, all pre-existing and all in Vols III–IV** —
`bon-sent-III-d31-a3-q3` (defs 1–3), `III-d32-a1-q2` (13, 14), `III-d5-a2-q4` (11),
`IV-d14-p2-a2-q1` (15, 17), `IV-d16-p2-a2-q2` (6). This is the known **J4 class-B residue**
(orphaned defs), identical to what the Itinerarium gate found. **Recorded, deliberately NOT fixed:
this gate authorises no edit under `vol3/` or `vol4/`.**

## Pass 3 — boundary integrity sweep

**Three interior chunk boundaries, counted by hand** (`seam-screen.py` is structurally blind to
them, and in this work it would also mistake a collatio opening for a page joint):

| boundary | shape | register |
|---|---|---|
| c1 \| c2 | **leaf edge** — Collatio I ends part-way down p. 335's right column, Collatio II opens at the head of p. 336 | p. 335's 9 notes all c1's; p. 336's 8 all c2's |
| c2 \| c3 | **mid-leaf** — Collatio III's heading + Summarium stand below Collatio II on p. 342 | **all 7 of p. 342 are c2's** |
| c3 \| c4 | **mid-leaf** — same shape on p. 348 | **all 7 of p. 348 are c3's** |
| (c4 \| c5) | **mid-leaf, and the next collatio's BODY begins on the leaf** (p. 353) | **4 notes SPLIT 3 / 1** — nn. 1–3 c4's, n. 4 forwarded to c5 |

★★ **THE BOUNDARY LEAF'S REGISTER FOLLOWS THE BODY, NOT THE HEADING — and the four boundaries so
far take three different shapes.** Where the next collatio contributes only a heading and a
Summarium (pp. 342, 348), it claims **none** of the leaf's notes, because neither carries an
anchor. Where its body actually begins on the leaf (p. 353), the register **splits**. Where the
boundary falls at a leaf edge (335 | 336), each leaf is wholly owned. **Do not infer the next
boundary's shape from the last one; read the anchors.**

★ **A NEW MECHANICAL CHECK THIS WORK MAKES POSSIBLE, and it passed:** the collationes carry
Quaracchi's numbered paragraphs, so a dropped paragraph is detectable without the plate. All four
chunks run **1..N with no gaps — 39 · 34 · 32 · 25 = 130 paragraphs — and the Latin and English
paragraph sequences are identical in every chunk.** The Sentences chunks have nothing like this;
use it at every later Hexaëmeron gate.

**Every page's register is contiguous 1..N**, with no gap, no double-claim and no unowned page
across pp. 329–353, agreeing with `KNOWN_TOTALS` on all twenty-five leaves. Ten gutter-crossing
runovers and **two page-crossing** (p. 331 n. 7 → 332, p. 340 n. 9 → 341, p. 341 n. 10 → 342 —
three, counting c2's pair), each rendered joined in the note it belongs to and logged once.

## Pass 4 — disk

`raw/vision/vol5/` (28 plates, 85 MB) and `/tmp/colcrop/` (374 MB) deleted — **~459 MB reclaimed.**
Both are fully regenerable from the gitignored PDF via `extract-pages.py` + `colcrop.py`.
⚠ **Re-extract before any later plate work; the vol5 plates are gone again.**

---

## Verification suite at the gate

`check-vol5-apparatus.py` **94 chunks / 1,096 entries**, all passed (p. 353 correctly reported as a
legitimate PENDING, not a GAP) · `check-vol5-census.py` rosters agree **94/94**, 94 runovers across
94 chunks (84 gutter-crossing, 10 page-crossing) · `polish-style-scan --volume 5` **CLEAN** ·
`build-content.mjs` **2027/2027, 8 books** · `build-citations.py` corpus QA total **228, unchanged**
by any of the four chunks.

## What the shakedown was for — the conventions it tested

- **The Summarium is rendered, not trimmed** (c1's precedent): correct, and the parser handles it.
  ⚠ But **twice now the Summarium has disagreed with the body** — c2's ¶ 34 is printed and
  unsummarised, and c3's synopsis gives the hierarch five properties where the body gives six.
  **It is a finding aid, never a count.**
- **The collatio is the chunk unit**: confirmed by p. 347 n. 5, Quaracchi's own map of the work
  (visions 1–4 → collationes 4-7, 8-12, 13-19, 20-23; the fifth and sixth never treated).
- **The heading's anchor is not a rule**: `COLLATIO I.` carries one; II, III and IV do not.
- **The gutter defaults cannot be trusted at a collatio opening OR close** — both leaves carry
  full-width matter crossing the gutter. Nine of twenty-five defaults were rejected.
