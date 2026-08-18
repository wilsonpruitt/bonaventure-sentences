# Collatio XV (`bon-hex-c15`) — plate scouting

Printed span **pp. 398–402** (PDF 474–478). Raw **L67795 → L68510**; `COLLATIO XVI.` at
**L68517**, which prints at the HEAD of p. 403 — so **XV closes at the foot of p. 402**, not on
p. 403 as the pre-run screen suggested. Both ends fixed on the band.

## Gutters (all measured; the `--skew` pre-run confirmed, not adopted blind)

| page | region | band | value | note |
|---|---|---|---|---|
| 398 | XV's two-column body, rows .55–.92 | 61–62 px windows, spread 2 px | **1321** | XIV's region (.07–.19) reads 1320 — the same gutter, measured twice |
| 399 | body .20–.90 | 1186–1246 (61 px), rule 1213–1219 centred | **1216** | spread 0 px across 24 windows |
| 400 | body .25–.85 | 1320–1374 (55 px), rule 1342–1353 centred | **1347** | screen said ~1345; the .17 and .68 slices were the front-matter/footer gap |
| 401 | body .20–.90 | 1151–1209 (59 px), rule 1176–1183 | **1180** | spread 2 px |
| 402 | body .15–.55 | 1346–1408 (63 px), rule 1375–1380 | **1377** | the .59 outlier is the body/footer gap — XV's body ends part-way down |

## p. 398 — the boundary leaf, structure fixed by row-ink profile

Rows: `COLLATIO XV.` 874–928 · subtitle 1005–1176 (three lines) · **Summarium 1270–2164
(16 lines, full measure)** · two-column body opens 2253 · footer rule ~2450 · register 2528–3375.

- **`COLLATIO XV.` carries NO apparatus anchor.** Fifteenth opening read; only `COLLATIO I.` has one.
- ⚠ **The raw's `quomodo'` at the end of subtitle line 1 is NOT an anchor.** Zoomed 10× at
  x 2280–2420, y 995–1060: a faint broken speck at x-height, not a superscript numeral.
  Recorded as a negative so the next reader does not re-litigate it.
- **The Summarium does NOT cross the leaf boundary** (c14's did — that was the first, and it was
  not the start of a pattern). It sits wholly on p. 398 and carries no anchor.
- **Summarium's last entry is `Quinto, secundum rationem quinarii, 28.`** — but the body is what
  gets counted.

### p. 398 footer — five notes, and the hand-off is confirmed at the band
`nn. 1–3` in the LEFT block, `nn. 4–5` in the RIGHT block. **nn. 1–2 are Collatio XIV's**
(Apoc. 1, 13 / Cfr. Exod. 26, 18) and are NOT re-claimed. **c15 owns nn. 3–5**:
- n. 3 — anchor in **L column**, ¶ 1, on *…semen iuxta genus suum ³*.
- n. 4 — anchor in **L column**, ¶ 1, on *…per Lamech ⁴*.
- n. 5 — anchor in **R column**, ¶ 2, on *…per Nemrod ⁵*.
So on this leaf the **block split (1–3 L) and the anchor split (3–4 L, 5 R) disagree**: the left
block overruns by one.

## p. 399 — 11 notes
Anchor split **nn. 1–5 L, nn. 6–11 R**; block split **nn. 1–3 L, nn. 4–11 R** — the left block
**underruns by two**. Body: ¶ 2 ends, ¶¶ 3–6 open in L (¶ 6 breaks at *per regem im-*), ¶ 6
completes and ¶¶ 7–9 run in R. ¶ 9 is the Epilogus of Pars I and closes cleanly at the column foot.
No runover in either block; both open numbered.

## p. 400 — 12 notes
Anchor split **nn. 1–7 L, nn. 8–12 R**, and the block split is the same; **n. 7 runs over the
gutter**, so the right block opens unnumbered. Body: ¶¶ 10–13 in L (¶ 13 breaks at *…delerentur
per*), ¶¶ 13–19 in R (¶ 19 breaks at *…de lignis tamen fa-*).
★ **p. 400 ¶ 18 carries a printed lacuna** — *octava aetas, scilicet* ***resurrect*** *, de qua* —
the type breaks off and a visible space stands before the comma. Verified at 10× on the band and
in the raw, which carries the identical gap. Flagged `[?]`; not supplied.

## p. 401 — 9 notes
Anchor split **nn. 1–5 L, nn. 6–9 R**; block split **nn. 1–4 L, runover + 5–9 R** — **n. 4 runs
over the gutter** and the left block therefore underruns the anchor split by one. Body: ¶ 19
closes and ¶¶ 20–22 open in L (¶ 22 breaks at *…de quo oritur, et*), ¶¶ 22–25 in R.
Furniture: `S. Bonav. — Tom. V.` under the left footer block, gathering signature `51` under the
right.

## p. 402 — 7 notes, and the collatio closes here
Block and anchor splits **coincide: nn. 1–3 L, nn. 4–7 R**. Body: ¶ 25 closes and ¶ 26 opens in L,
¶¶ 27–28 in R. **¶ 28 ends at *…si fieri potest, etiam electi.* and the body stops at ~57 % of the
leaf**, the footer register filling the rest.
⚠ **That white space is NOT what fixed the end.** The end is fixed from `COLLATIO XVI.` printed at
the **head of p. 403** — read on the plate, together with p. 403's own running head
`IN HEXAËMERON COLLATIO XVI.` — and corroborated editorially by p. 402 **n. 7**, which is Quaracchi
saying the comparison *continuatur in seq. collatione quoad senarium et septenarium.*

## Verification suite at build time
`check-vol5-apparatus.py` 105 chunks / 1,497 entries, no PENDING · `check-vol5-census.py` 105/105,
124 runovers (111 gutter-crossing, 13 page-crossing) · `polish-style-scan --volume 5` CLEAN ·
`check-live-flags.py vol5` 4 occurrences (2 flags, each mirrored) · `build-content.mjs` 2038/2038,
8 books · `build-citations.py` corpus QA **228, unchanged**, c15 contributing **76 records, zero
dangling, zero QA flags**.
