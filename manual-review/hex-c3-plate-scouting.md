# `bon-hex-c3` — Collatio III, plate scouting (2026-08-14)

Banked **before** the chunk is written, per the standing habit that made a terminal crash
cost nothing at the Itinerarium scholion. Everything here is read off the 450 dpi plates
unless marked otherwise.

## Span — pp. 342–348, ~32 numbered ¶¶

- **Collatio III opens at the FOOT of p. 342**, below Collatio II, with a full-width display
  heading, a two-line subtitle and the head of its Summarium. **There is no two-column body
  of Collatio III on p. 342 at all** — so that leaf needs no gutter for this chunk.
- **The Summarium runs across the page break**: it begins on p. 342 and continues at the head
  of p. 343 (*Item, quod ab actualissimo sint possibilia, 7-8. …*), still full measure, and
  closes at *Epilogus de clavi David, 32.* The body's ¶ 1 opens below it on p. 343.
- **It closes part-way down p. 348** at *…nos reducit in contemplationem caelestium et deinde
  supercaelestium.*, with `COLLATIO IV.` opening below it in the same leaf — the same shape as
  Collatio II's close. ⚠ **p. 348's running head already reads `IN HEXAËMERON COLLATIO IV.`**
  while Collatio III still fills most of the page. Third attestation in this work; never set a
  boundary from the running head.
- Raw **L59261 → L60214**.

## ✅ `COLLATIO III.` CARRIES NO APPARATUS ANCHOR — checked at magnification

`COLLATIO I.` carried anchor ¹ (the note on the work's title in the codices) and that is what
decided the collatio as the chunk unit. **Collatio III's heading carries none, and neither does
its Summarium**, and p. 342's seven-note register is exhausted by Collatio II's seven anchors.
The heading and subtitle print:

> **COLLATIO III.**
> De plenitudine intellectus, quatenus est clavis contemplationis
> per intellectum Verbi *increati, incarnati* et *inspirati*.

The in-place subtitle is the form that goes into the `WORKS` registry, not the volume index's.

## Gutters — measured; the tool's default REJECTED on two of six

Six leaves need a gutter (343–348); p. 342 does not, for this chunk. Every value below is the
**midpoint of the full zero-ink band** taken from the direct per-column profile, not the window
vote — the frozen step-3 method, because five of the six defaults came off sub-60 px runs.

| page | adopted | band | centre rule (island) | tool default | verdict |
|---|---|---|---|---|---|
| 343 | **1162** | 1132–1193 (62 px) | 1160–1164 | 1158 / 42 px run | **rejected, off by 4** |
| 344 | 1330 | 1304–1356 (53 px) | 1325–1335 | 1330 / 53 px run | confirmed |
| 345 | 1173 | 1148–1198 (51 px) | 1165–1175 | 1173 / 50 px run | confirmed |
| 346 | 1370 | 1344–1397 (54 px) | 1364–1378 | 1370 / 54 px run | confirmed |
| 347 | 1195 | 1165–1226 (62 px) | 1192–1197 | 1195 / 62 px run | confirmed |
| 348 | **1387** | 1358–1417 (60 px) | — | 1390 / 33 px run | **rejected, off by 3** |

- **★ p. 348 is the collatio-CLOSING leaf and it fails the standard window for the same reason a
  collatio-OPENING leaf does** — Collatio IV's display heading and Summarium cross the gutter at
  its foot, inside the default 45–92 % band. The sound reading came from **rows 10–50 %**, above
  them, where a clean 60 px zero-ink band stands. Expect this at every collatio close in this
  work, which is every leaf that also opens the next one.
- **★ Four of the six defaults were right on sub-60 px runs.** The rule holds as written: a
  narrow run is a trigger to profile, never a verdict either way.

## What the chunk inherits

**Nothing.** p. 342's register is closed and belongs entirely to Collatio II (verified at the c2
commit); Collatio III's first anchor falls on p. 343.

## Still to do when writing

- Read each of pp. 343–348's footer register off the bands; feed `KNOWN_TOTALS` a line per page.
- Check every page-foot joint for an unnumbered runover head — c2 had **two** page-crossing
  runovers, and this work's footers are the longest in the volume.
- Marginalia are dense; trim to the Marginalia list in `## Notes`.
