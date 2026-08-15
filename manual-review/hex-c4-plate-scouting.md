# `bon-hex-c4` — Collatio IV, plate scouting (2026-08-14)

Banked **before** the chunk is written, per the standing habit.

## Span — pp. 348–353, ~25 numbered ¶¶

- **Collatio IV opens at the FOOT of p. 348**, below Collatio III, with a full-width display
  heading, a one-line subtitle and the head of its Summarium. As at p. 342, **no two-column
  body of it stands on that leaf**, so p. 348 needs no gutter for this chunk.
- **It closes part-way down p. 353**, where `COLLATIO V.` opens below it. Confirmed by profile
  rather than by eye: p. 353's rows 8–40 % carry a clean two-column band, while rows 45–98 %
  have **no gutter at all** (minimum ink 73 across the whole window) — that is the full-width
  heading-and-Summarium of Collatio V occupying the lower half.
- Raw **L60214 → L60965**; paragraphs run to **¶ 25**.
- ⚠ The running heads run ahead again: p. 353's reads `IN HEXAËMERON COLLATIO V.` while
  Collatio IV still fills its upper half. Fourth attestation in this work.

## ✅ `COLLATIO IV.` CARRIES NO APPARATUS ANCHOR — checked at magnification

Read on the full-width crop of p. 348: the heading and its subtitle print clean, with no
superscript. The subtitle is

> **COLLATIO IV.**
> De visione prima, quae est intelligentiae per naturam inditae, tractatio prima.

**So of the four collationes opened so far, only `COLLATIO I.` carries an anchor.** That is now
the pattern rather than the exception — but it is checked at each opening, never assumed, since
c1's anchor is what decided the collatio as the chunk unit in the first place.

## Gutters — measured; the tool's default REJECTED on one of five

p. 348 needs none for this chunk. Every value is the midpoint of the full zero-ink band from the
direct per-column profile.

| page | adopted | band | tool default | verdict |
|---|---|---|---|---|
| 349 | 1211 | 1180–1242 (63 px) | 1211 / 63 px | confirmed |
| 350 | 1348 | 1318–1379 (62 px) | 1348 / 62 px | confirmed |
| 351 | 1188 | 1161–1216 (56 px) | 1188 / 56 px | confirmed |
| 352 | **1349** | 1319–1380 (62 px) | 1353 / 54 px run | **rejected, off by 4** |
| 353 | **1180** | 1152–1210 (59 px), rows 8–40 % | 1181 / **1 px** run | see below |

- **★★ p. 353 is the second attestation of c3's finding, and it is now a rule: A COLLATIO-CLOSING
  LEAF FAILS THE DEFAULT WINDOW BECAUSE THE NEXT COLLATIO'S DISPLAY HEADING AND SUMMARIUM CROSS
  THE GUTTER AT ITS FOOT.** The default came off a **1 px** run — the narrowest reading the tool
  has ever returned in this volume — and landed on 1181 against a true 1180. **It was right by
  one pixel and by luck; the profile is what settles it.** Take the reading from the upper rows
  at every collatio close.
- ★ p. 352's default is the ordinary sub-60 px failure: a 54 px run, wrong by 4 px.

## What the chunk inherits

**Nothing.** p. 348's register is closed and belongs entirely to Collatio III (verified at the c3
commit); Collatio IV's first anchor falls on p. 349.

## Still to do when writing

- Read each of pp. 349–353's footer register off the bands; feed `KNOWN_TOTALS` a line per page.
- Check every page-foot joint for an unnumbered runover head.
- ⚠ **The shakedown gate for this work fires at the close of this collatio** — the first of three,
  and the deploy rides with it.
