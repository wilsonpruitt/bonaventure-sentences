# `bon-hex-c5` — Collatio V: plate scouting

Banked before the chunk is written, per the standing rule that plate work is committed
ahead of the prose so a crash costs nothing. Plates re-extracted 2026-08-15 (pp. 353–360);
they had been deleted at the shakedown gate's pass 4.

## Span — FIXED POSITIVELY, pp. 353–359

- **Collatio V opens BELOW Collatio IV on p. 353**: display heading `COLLATIO V.`, subtitle,
  full-measure `SUMMARIUM`, then ¶ 1 in two columns in the bottom fifth of the leaf.
- **`COLLATIO VI.` opens at the HEAD of p. 360** — verified on the band (running head
  `IN HEXAËMERON COLLATIO VI.`, then the display heading, subtitle and Summarium). p. 359's
  two columns both end level at ~72 % with ¶ 33's *…nisi anima sit purgata⁷.*
- **So the c5 | c6 boundary is a LEAF EDGE** — the second boundary of that shape in this work
  (after 335 | 336), and the fifth boundary overall. **c5 forwards c6 nothing.**
- Raw: `COLLATIO V.` at **L60965**, `COLLATIO VI.` at **L62017**. Leaf tops in the raw:
  354 = L61021 · 355 = L61186 · 356 = L61354 · 357 = L61526 · 358 = L61693 · 359 = L61864 ·
  360 = L62014.

## The heading carries NO anchor

`COLLATIO V.` and its subtitle carry no apparatus anchor, as II, III and IV did not.
`COLLATIO I.` remains the only one that does. (Checked on the band, not inferred.)

Subtitle, in place: *De prima visione tractatio secunda, quae est de tertio radio sive de
veritate morum, et de sapientia contemplationis.* — to be registered in
`WORKS.hexaemeron.divisions` as the chunk lands.

## Gutters — all seven measured, five defaults rejected or refined

`colcrop` defaults were sub-60 px on **six of seven** leaves, so every one went to the
direct per-column ink profile (band edges + the centre-rule island, midpoint adopted).

| page | default (run) | band | rule island | **adopted** |
|---|---|---|---|---|
| 353 (c4's region, rows .06–.39) | 1181 / 1 px ⚠ | 1151–1209 (59) | 1176–1183 | **1180** |
| 354 | 1347 / 54 px | 1320–1375 (56) | 1343–1353 | **1347** |
| 355 | 1184 / 49 px | 1153–1209 (57) | 1177–1186 | **1181** |
| 356 | 1401 / 58 px | 1373–1431 (59) | 1398–1407 | **1402** |
| 357 | 1233 / 58 px | 1204–1263 (60) | 1230–1236 | **1233** |
| 358 | 1373 / 49 px | 1348–1398 (51) | 1365–1381 | **1373** |
| 359 | 1151 / 63 px | 1120–1182 (63) | 1148–1153 | **1151** |

- **★ p. 353's whole-page default is worthless — 1 px — and the reason is now measured, not
  guessed: the leaf stacks FOUR regions in three measures** (c4's two columns, the full-measure
  heading + subtitle, the full-measure Summarium, then c5's two columns). A profile over
  rows .50–.75 lands entirely inside the Summarium and returns no gutter at all (min ink 48,
  no low-ink run anywhere between x 1050 and 1350). **This is the region-not-page rule
  (frozen at `bon-itin-c7`, p. 313) in its most extreme form yet** — here the middle region
  has no gutter to return. c5's own columns on p. 353 share c4's measure, **1180**.
- p. 355's default was 3 px high (1184 against a band midpoint of 1181), on a 49 px run with
  the heaviest rule island of the set (peak 747). Sub-60 rule fired and was right again.

## Registers, read off the 450 dpi footer bands

### p. 353 — 4 notes; block 2 L / 2 R; anchors 3 c4 / **1 c5**
The split promised by the hand-off, **verified independently**: n. 4 is the LAST note of the
RIGHT block, and it is c5's — its anchor is ¹⁴ on c5 ¶ 1's *et divisit lucem a tenebris⁴*.
nn. 1–3 are `bon-hex-c4`'s and are NOT re-claimed here.

- **n. 4** — *Gen. 1, 4. — Quae immediate post afferuntur exposita sunt in collat. 4.*
  (`Gen. 1, 4` confirmed at magnification; the raw's `Cen. 1, i.` is the usual serif `1`/`4`
  noise.)

### p. 354 — 10 notes; block 5 L / 5 R; anchors 5 L / 5 R — **they coincide**
One gutter runover: **n. 5 fills the foot of the left block and continues in the right block**,
opening unnumbered at *communem vitam, scil. in seriosis.* Left column ends *…scilicet
verecundiam*, right column opens *et nemesin* — that is the column division, and anchors
1–5 stand above it.

Digits settled at magnification: **`pag. 19, nota 7`** (n. 1 — the leading glyph is a serif
`1`, not a `4`; agrees with the raw) · `Exod. 19, 3` / `24, 12` / `Hebr. 12, 20` /
`Exod. 19, 13` (n. 3 — and Heb 12:20 is *bestia enim quae tetigerit montem lapidabitur*,
which is the quoted text, so the join is corroborated) · `II. Ethic. c. 7` … `III. c. 6.`
(n. 4) · `n. 11` (n. 5, the raw's flattened `H`) · `pag. 174, nota 3` (n. 7 — raw `17i`) ·
`IV. Ethic. c. 1` and `III. Ethic. c. 10-12` (n. 7) · `c. 35. n. 77` and `Luc. 9, 3` (n. 9) ·
`III. Oracul. 29` (n. 10).
