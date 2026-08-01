# Vol V work-close gate — PASS 3 (cross-chunk boundary integrity), Pars VI

**Scope:** `bon-brev-p6-c1` … `bon-brev-p6-c13` — 13 chunks, printed pp. 265–280
(pdf 341–356; offset `pdf = printed + 76`). Plus the **incoming** seam
`p5-c10 → p6-c1` (**leaf crossing** p. 264 → p. 265) and the **outgoing** seam
`p6-c13 → p7-c1` (**leaf crossing** p. 280 → p. 281). A Pars V agent ran concurrently
on the p. 264 side; **that seam is certified here independently, from this side, by
re-derivation — the double derivation is deliberate and the neighbour's finding was
not consulted.**

**`PARS SEXTA` opens at a LEAF EDGE, at the head of p. 265 — the only pars in the
Breviloquium that does.** Both of this pars's outer boundaries are therefore leaf
crossings, and `seam-screen.py` is blind to both. Pars IV was the mirror case (eleven
boundaries, zero leaf crossings); Pars VI is the only pars whose *entire* interior is
mid-page while *both* its ends are leaf crossings.

Run 2026-08-01, as pass 3 of the Breviloquium work-close gate (CLAUDE.md § "Polish-gate
cadence for Vols V–X", trigger 2 — work boundary, unconditional). Companion logs:
`vol5-workclose-gate-pass3-prol-p1.md`, `-p2.md`, `-p3.md`, `-p4.md`; pass 1 is
`vol5-workclose-gate-pass1.md`.
**Nothing was edited; no `KNOWN_TOTALS` entry changed; no git write command was run.**

Derived counts, each derived by a tool at the moment of citing, none carried:

- **13 chunks, 110 apparatus entries** in Pars VI (`re` walk of the thirteen
  `## Apparatus` sections). Independently, the sixteen printed pages pp. 265–280 carry,
  as read off the bands below, 6+6+8+8+8+5+8+8+7+8+7+6+7+5+7+6 = **110** notes. The two
  figures are independent and they agree: **Pars VI owns exactly its sixteen pages
  entire — no note in the range is unowned, none double-claimed, and no Pars VI chunk
  reaches outside pp. 265–280.** (`p5-c10` owns `p263-7 … p264-6` and nothing on p. 265;
  `p7-c1` owns `p281-1 … p282-2` and nothing on p. 280.) The Pars VI close is recorded
  as 110 entries; that figure is **re-derived here, not quoted**, and it holds.
- Corpus-wide at the same moment, `check-vol5-apparatus.py` reports **79 chunks,
  681 apparatus entries — All checks passed**; `check-vol5-census.py` reports **79 on
  disk / 79 in ledger, rosters agree**, with **59 runovers across 79 chunks
  (54 gutter-crossing, 5 page-crossing; 48 chunks positive, 31 negative)**.
  **Exactly one of the five page-crossing runovers falls in this scope — p. 277 n. 7**
  (the others are pp. 206, 212, 246, 253); it is re-derived on the plate below and is
  **not re-logged here**.

---

## Method actually used

1. **Gutters re-measured fresh on every page, no constant, no parity prediction.**
   `colcrop.py`'s **own** `measure_gutter` function was taken verbatim out of the tool's
   source and driven over **fourteen** independent row windows (45–92 %, 30–70 %, 50–80 %,
   55–90 %, 35–60 %, 60–88 %, 47–60 %, 70–92 %, 20–65 %, 25–55 %, 40–75 %, 65–90 %,
   33–85 %, 52–72 %). The function's low-ink run already **merges the two zero-ink runs
   either side of Quaracchi's printed centre rule** — `xs[0]`…`xs[-1]` spans the island —
   so the reported width *is* the merged band and its midpoint the merged-band midpoint.
   In parallel the **per-column ink profile was printed directly** for every one of the
   eighteen leaves, at three windows each (45–92 %, 30–70 %, 25–55 %), giving the blank
   band, the ink island inside it and the island's peak ink. **Run width is the
   confidence signal:** windows outside a sound 50–75 px band were discarded, and runs
   under ~58 px were never adopted on their own. **No separate measuring algorithm was
   hand-rolled.**
   **Adoption rule, stated in advance:** the adopted value is the midpoint of the merged
   blank band from the **30–70 % ink profile** — the one window that survives on all
   eighteen leaves — cross-checked against the surviving-window consensus. Where the two
   differ they differ by ≤ 3 px on every leaf.
2. **Body continuity established POSITIVELY from the next heading**, never from white
   space (CLAUDE.md's `p2-c4` rule). For each of the fourteen boundaries the raw djvu
   (`raw/doctorisseraphic05bona_djvu.txt`) was walked to the receiving unit's
   `Cap. N.` / `PARS SEXTA` / `PARS SEPTIMA` heading, and the ~12 lines immediately
   preceding it compared word-for-word against the prior chunk's Latin tail.
   **All fifteen headings in range were found in the raw**; none had to be read off a
   band, and **none was corroborated from a running head.**
3. **Every printed page's footers read off the 450 dpi bands** (bands-only rule — the
   Vol V raw has no footnote numerals). For each of pp. 264–281 **both** the left and the
   right footer block were read at `n=4, scale 1.5` (band 3, the whole register): the last
   numbered entry of the right block and its number, whether the right block opens
   numbered or with an unnumbered continuation, whether the left block opens numbered,
   and the block split point. Ownership was then checked against `KNOWN_TOTALS` in
   `tools/check-vol5-apparatus.py` and against the chunks' own labels.
   **Anchors, only anchors** — block structure, column structure and capitulum structure
   were kept separate throughout.
4. Watched for the two named failure families — the **cascade-merge splice** (a tail that
   does not parse) and the **chunk written short at a column foot**.

**What was NOT independently re-derived, stated plainly.** Block structure (from the
bands), page totals (from the bands) and capitulum structure (from the heading positions
plus chunk ownership) were all derived directly here. **Anchor-COLUMN structure — which
column each note's anchor stands in — was not re-derived for every page**, because it
requires reading both body columns on all sixteen leaves. See `[?]` DOC-3 below: the
`KNOWN_TOTALS` comments for pp. 268, 269, 271, 272 and 273 make block-vs-anchor
divergence claims that rest on exactly that data, and **this pass neither confirms nor
contradicts them.** They are not load-bearing for boundary integrity: ownership is
settled by capitulum, and capitulum ownership comes out contiguous and gapless on every
one of the sixteen pages.

---

## Gutters measured

Adopted = 30–70 % merged-band midpoint (see the adoption rule above), cross-checked
against the surviving windows. "Chunk used" is the split recorded in that page's chunk
`transcription_status` — **compared against, never adopted from.**

| p. | adopted | sound windows / 14 (range, median) | runs | chunk used | Δ |
|---|---|---|---|---|---|
| 264 | **1364** | 7 (1364–1367, med 1367) | 53–62 px | 1365 | 1 |
| **265** | **1151** | 6 (1148–1156, med 1152) | 53–59 px | 1150 | 1 |
| 266 | **1420** | 13 (1418–1427, med 1424) | 53–63 px | 1422 | 2 |
| 267 | **1165** | **14** (1160–1167, med 1163) | 55–61 px | 1163 | 2 |
| 268 | **1372** | 8 (1372–1377, med 1375) | 51–74 px | 1370 | 2 |
| 269 | **1188** | 12 (1184–1188, med 1186) | 59–64 px | 1186 | 2 |
| 270 | **1372** | 13 (1371–1375, med 1373) | 59–64 px | 1373 | 1 |
| 271 | **1201** | **14** (1200–1204, med 1202) | 59–64 px | 1202 | 1 |
| 272 | **1324** | 8 (1324–1327, med 1326) | 60–64 px | 1326 | 2 |
| 273 | **1166** | **14** (1158–1170, med 1163) | 50–63 px | 1164 | 2 |
| 274 | **1402** | 12 (1402–1405, med 1403) | 56–63 px | 1403 | 1 |
| **275** | **1150** | 6 (1147–1154, med 1150) | 52–63 px | 1145 | **5** |
| 276 | **1392** | 10 (1392–1393, med 1392) | 61–63 px | 1392 | 0 |
| 277 | **1251** | **14** (1243–1253, med 1248) | 53–64 px | 1247 | 4 |
| 278 | **1348** | **14** (1347–1352, med 1348) | 56–62 px | 1351 | 3 |
| 279 | **1195** | **14** (1190–1197, med 1192) | 51–64 px | 1191 | 4 |
| **280** | **1331** | 5 (1330–1331, med 1331) | 61–62 px | 1331 | 0 |
| 281 | **1234** | **14** (1227–1235, med 1231) | 55–63 px | 1231 | 3 |

**Maximum divergence between this pass's measurement and the split each chunk was
actually built on is 5 px (p. 275)**, against a column width of ~1150 px and a
`colcrop.py` crop that carries a 60 px overlap on each side of the split.
**No chunk in Pars VI can have been built on a truncated or padded column.** The same
5 px is the maximum whether the adopted value is taken from the ink profile or from the
window median.

**The in-gutter obstruction — Quaracchi's printed centre rule — is present on all
eighteen leaves.** Every 30–70 % profile shows an ink island standing inside the blank
band, with peaks from 101 rows (p. 268, the lightest in range) to 1141 rows (p. 280, the
heaviest). **Its absence is what would have been worth remarking; it was never absent.**

### Measurements REJECTED, and the run widths that condemned them

- **p. 265 — `colcrop.py`'s bare default REJECTED, and this is the loudest failure in the
  range.** The default (45–92 %) returns **1121 on a 4 px run** — a quarter of the tool's
  own 15 px alarm threshold. Four further windows (50–80 %, 55–90 %, 60–88 %, 65–90 %)
  repeat **1121 on 4 px**, and 70–92 % gives **1117 on 12 px**; 47–60 % blows out the
  other way at **1299 on a 359 px run**. Eight of fourteen windows rejected. The six
  survivors sit at **1148–1156 on 53–59 px runs**. Ink profile: the 45–92 % window has a
  degenerate blank band x=1120–1123 with **no island at all** — the rule has swallowed the
  zero-ink run entirely in the lower body rows — while 30–70 % gives blank **1125–1178**
  with the rule at **1146–1159 (peak 539)** → midpoint **1151**, and 25–55 % gives
  1128–1184 with the rule at 1150–1160 → 1156. **Adopted 1151.**
  ⚠ Note the shape of this failure: p. 265 opens a pars, but the `PARS SEXTA` display
  heading sits *above* the 45 % floor and is **not** what breaks the measurement — the
  windows that fail here are the *lower* ones, and they fail because the centre rule inks
  heavily low on this leaf. **CLAUDE.md's gutter-rule 2 (display heading destroys the
  upper windows) did not fire on this pars opening; gutter-rule 5 (heavily inked rule
  truncates the run) did.** A pars opening does not automatically fail in the documented
  way, and the run width — not the window's position — is what decided it.
- **p. 275 — the bare default REJECTED.** 45–92 % returns **1127 on an 18 px run**; six
  further windows repeat the same false cluster (50–80 % 1128/20, 55–90 % 1127/19,
  60–88 % 1123/26, 70–92 % 1123/26, 65–90 % 1123/26, 40–75 % 1131/19) and 33–85 % returns
  **1130 on a 14 px run** — below the tool's own threshold. Eight rejected. The 45–92 %
  profile is degenerate (band 1119–1136, island a single column, peak 3); the 30–70 %
  profile gives blank **1124–1176**, rule at **1142–1157 (peak 352)** → **1150**. Six
  survivors span 1147–1154 on 52–63 px. **Adopted 1150** — 5 px from the 1145 the chunk
  was built on, the largest divergence in the pars and still immaterial.
- **p. 280 — the bare default REJECTED.** 45–92 % returns **1328 on a 30 px run**, and
  three further windows (50–80 %, 40–75 %, 33–85 %) repeat 1328/30. Five more blow out
  entirely: 55–90 % **1225 / 236 px**, 60–88 % **1222 / 243 px**, 70–92 % **1278 / 356 px**,
  65–90 % **1278 / 356 px**, 52–72 % **1340 / 346 px**. Nine of fourteen rejected — the
  worst attrition in the pars. The five survivors agree at **1330–1331 on 61–62 px**, and
  the 30–70 % profile gives blank **1301–1361** with the rule at **1328–1344, peak 1009**
  → **1331**. This is the most heavily inked centre rule in the range and it is *why* the
  lower windows pinch to 30 px. **Adopted 1331**, agreeing exactly with the chunk.
- **p. 264 — seven windows rejected on blown-out runs**: 50–80 % (**1342 / 370 px**),
  47–60 % (**1342 / 370 px**), 52–72 % (**1323 / 409 px**), 70–92 % (**1298 / 434 px**),
  65–90 % (**1253 / 343 px**), 40–75 % (**1275 / 236 px**), 60–88 % (**1315 / 216 px**).
  A far-above-band run is the same species of failure as a far-below-band one. Seven
  survivors span 1364–1367 on 53–62 px; profile 30–70 % gives 1335–1394 → **1364**.
- **p. 272 — six windows rejected**: 60–88 %, 70–92 % and 65–90 % all return **1224 on
  ~271 px**; 35–60 % and 47–60 % return **1347 on 106 px**; 33–85 % returns 1317 on a
  **43 px** run. Eight survivors sit inside 3 px (1324–1327) on 60–64 px runs.
- **p. 276 — four windows rejected**: 47–60 % (**1432 / 145 px**), 65–90 %
  (**1437 / 154 px**), 70–92 % (**1352 / 325 px**), 52–72 % (**1403 / 85 px**). The ten
  survivors are the tightest in the pars — a 1 px spread (1392–1393) on 61–63 px runs.
- **p. 274 — two windows rejected**: 47–60 % (**1275 / 322 px**), 70–92 %
  (**1261 / 341 px**). Twelve survivors inside 3 px.
- **p. 269 — two windows rejected**: 47–60 % (**1277 / 372 px**), 70–92 %
  (**1225 / 146 px**). Twelve survivors inside 4 px.
- **p. 268 — one window rejected outright** (47–60 %, **1432 / 185 px**), and **six
  further windows, including the bare default, return 1374 on a 49 px run** — under the
  ~58 px trust floor, so not adopted on their own. They are, however, within 2 px of the
  eight sound windows (1372–1377) and of the profile (1372). p. 268 also carries the
  *lightest* centre rule in the range (peak 161 at 30–70 %), which is why its runs are
  long and its measurement easy.
- **p. 270 — one window rejected**: 70–92 % (**1287 / 238 px**).
- **pp. 266, 273, 279 — no window blown out, but the bare default sits under the floor**
  (1425 / 53 px, 1161 / 54 px, 1191 / 51 px respectively). In each case it survives only
  as one of thirteen/fourteen concordant windows; none was adopted alone.
- **pp. 267, 271, 277, 278, 281 — 14 of 14 windows sound.** p. 271 and p. 278 are the
  textbook leaves: spreads of 4 and 5 px on runs of 59–64 and 56–62 px.
- **Parity is used nowhere.** It is remarked only after the fact that the odd/even
  clusters happen to hold across pp. 264–281.

---

## Boundary table

**Fourteen boundaries in scope: TWELVE mid-page, TWO leaf crossings.**
`seam-screen.py --volume 5` reports **71 mid-page boundaries corpus-wide, 0
tail-not-terminal suspects**, and sees exactly the twelve mid-page boundaries in this
range (pp. 266, 267, 268, 269, 270, 271, 272, 273, 275, 276, 277, 279). **Both leaf
crossings are outside its denominator**, which is why they are swept by hand here.

Raw line map (headings located, boundaries set from them and from nothing else):
`PARS SEXTA` L48612 (subtitle L48615) · Cap. I L48618 · II L48781 · III L48926 ·
IV L49078 · V L49233 (`C.\p. V.`) · VI L49425 · VII L49561 (`C.\i>. VII.`) ·
VIII L49709 (`Cap. VIH.`) · IX L49860 · X L50129 · XI L50318 (`Cai'. \l.`) ·
XII L50468 (`C.\p. XII.`) · XIII L50667 · `PARS SEPTIMA` L50926 (subtitle L50929) ·
Cap. I L50932.

⚠ **Both pars headings are un-garbled in this raw** — a plain `grep "PARS  SEXTA"` and
`grep "PARS  SEPTIMA"` each return one hit. This is the **opposite** of the Pars IV/V
seam, where the raw prints `PARS aUINTA` and a `QUINTA` grep returns nothing. Do not
generalise either way: three of the thirteen capitulum headings here are garbled
(`C.\p. V.`, `C.\i>. VII.`, `Cap. VIH.`, `Cai'. \l.`, `C.\p. XII.` — five, in fact),
and **Cap. XI is the worst: its heading prints `Cai'. \l.`, so no plausible `XI` grep
finds it.** It was reached by walking down from Cap. X and reading the subtitle
`Dc intcgritale unctionis cxlrcinue.` (L50320) beside it.

| # | Prior → Receiving | Shared page / crossing | Body continuity — evidence | Footer split (page total) | Verdict |
|---|---|---|---|---|---|
| 0 | `p5-c10` → `p6-c1` | **LEAF CROSSING p. 264 → p. 265** — the incoming seam | `PARS SEXTA.` found **in the raw** at L48612, subtitle `De medicina sacraniciilali.` L48615, `Cap. I.` L48618. `p5-c10`'s tail `…ut sic, septies in die laudantes nomen Domini et orantes, impetremus gratiam septiformem virtutum, donorum et beatitudinum, qua vincamus septiformem pugnam vitiorum capitalium et perveniamus ad septiformem coronam dotum gloriosarum, adiuvante nihilominus septiformi medicina Sacramentorum divinitus ad reparationem humani generis statutorum.` = raw L48570–48582 word for word — the **last body line of p. 264**. Between it and the display heading stand only p. 264's footer register (L48585–48603), the running head `PARS VI. c. r.` (L48606) and the folio `26S`=265 (L48609). **The running head was used for neither purpose**; the boundary is set from `PARS SEXTA` alone | p. 264 total **6**, **all six `p5-c10`'s**; p. 265 total **6**, **all six `p6-c1`'s**. Band-read: p. 264's right block's last entry is n. 6 (`Psalm. 118, 164.`) and it **closes complete with clear blank beneath — nothing forwarded into p. 265**; p. 265's left block opens **NUMBERED** at n. 1 (`Isidor., VI. Etymolog. c. 19. n. 40. Vide tom. III. pag. 895, nota 5. …`). **Page-crossing runover NEGATIVE, closed from both sides** | **CLEAN** |
| 1 | `p6-c1` → `p6-c2` | p. 266 (mid-page) | `Cap. II.` found in the raw at L48781 (subtitle L48783). c1 tail `…hinc est, quod dicuntur Sacramenta, quasi medicamenta sanctificantia. … ita ut merito dici debeant Sacramenta.` = raw L48766–48779, immediately above the heading | 1 / 5 (6). Blocks 3/3: L nn. 1–3 with **n. 3 breaking at a comma** (`…quae lectio potius videtur esse vitium editionis,`), R opening **UNNUMBERED** (`quam, relictis codicibus, non satis consulte ipsi secuti sumus…`) → **gutter runover POSITIVE at n. 3**, owned and logged by `p6-c2`. Last entry n. 6 (`Plurimi codd. et 2 perperam perfectos… in libertate spiritus ambulare permittit.`), complete | **CLEAN** |
| 2 | `p6-c2` → `p6-c3` | p. 267 (mid-page) | `Cap. III.` at raw L48926 (subtitle L48927). c2 tail `…hinc est, quod passio Christi immediatius sanctificat Sacramenta temporis legis novae et pleniori gratia in eis redundat. … sicut imperfectum reducit et praeparat ad perfectum.` = raw L48910–48924 | 2 / 6 (8). Blocks 4/4: L nn. 1–4, **n. 4 breaking after `— Superius post *reparativum* Vat.,`**, R opening **UNNUMBERED** (`1 et 3 addunt et curativum nostrorum morborum, nonnulli codd. scilicet.`) → **gutter runover POSITIVE at n. 4**, logged by `p6-c3`. Last entry n. 8 (`Cantic. 6, 3. et 9.`), complete | **CLEAN** |
| 3 | `p6-c3` → `p6-c4` | p. 268 (mid-page) | `Cap. IV.` at raw L49078 (subtitle L49080). c3 tail `…Unde quia baptismus est ingredientium, confirmatio pugnantium, eucharistia vires resumentium, poenitentia resurgentium, extrema unctio exeuntium, ordo novos milites introducentium, matrimonium novos milites praeparantium; patet ex his sufficientia et ordo medicamentorum sacramentalium et armorum.` = raw L49062–49076 | 1 / 7 (8). Blocks 4/4: L nn. 1–4. **★ NOTE THE FORM — this is the pars's textbook case of a complete-looking tail that is not an ending:** n. 4's left half reads `Ioan. 14, 6. — Superius pro *beatificantia* A S *beneficia.*` and **ends at a full stop**, yet the right block opens **UNNUMBERED** with `Subinde pro *repararetur* 2 cum pluribus codd. *reparetur*, et E *perveniatur* pro *perveniretur*.` — a further clause of the same entry. **Gutter runover POSITIVE at n. 4**, logged by `p6-c4`. Last entry n. 8 (`Matth. 4, 17. et Marc. 1, 14. seq. — Ioan. 2, 1. seqq. — Matth. 19, 4. seqq.`), complete | **CLEAN** |
| 4 | `p6-c4` → `p6-c5` | p. 269 (mid-page) | `C.\p. V.` (garbled `Cap. V.`) at raw L49233 (subtitle L49235). c4 tail `…eucharistiam vero, comparando se grano frumenti et conficiendo et dando discipulis, imminente passione, Sacramentum corporis et sanguinis sui. — Et ideo haec tria Sacramenta per Christum distincte et integre debuerunt institui et in lege veteri multipliciter figurari tanquam Sacramenta substantialia novi testamenti et propria legislatoris, Verbi scilicet incarnati.` = raw L49217–49231 | 2 / 6 (8). Blocks 4/4: L nn. 1–4, **n. 4 breaking MID-WORD** at `ubi de in-`, R opening **UNNUMBERED** (`tentione; d. 5. a. 1. et 2, ubi de ministro baptismi…`) → **gutter runover POSITIVE at n. 4**, logged by `p6-c5`. Last entry n. 8 (`Vat., 1 et 3 mediis.`), complete | **CLEAN** |
| 5 | `p6-c5` → `p6-c6` | p. 270 (mid-page) | `Cap. VI.` at raw L49425 (subtitle L49427). c5 tail `…Magis ergo, quia pro Ecclesiae honore atque unitate pugnamus, non tribuamus haereticis quidquid apud eos eius agnoscimus, sed eos arguentes doceamus, quod ex unitate habent nec valere ad salutem, nisi ad eandem venerint unitatem ».` = raw L49409–49423 | 2 / 3 (5). Blocks 4/1: L nn. 1–4, **n. 4 breaking inside a quotation** at `quod « baptismus sit *fundamentum* omnium`, R opening **UNNUMBERED** (`Sacramentorum », et quod « ante susceptionem baptismi…`) → **gutter runover POSITIVE at n. 4**, logged by `p6-c6`. Last entry n. 5 (`Ed. 1 servare… Inferius pro ex hoc I K L M in hoc.`), complete. p. 270 carries the **smallest register in Pars VI** | **CLEAN** |
| 6 | `p6-c6` → `p6-c7` | p. 271 (mid-page) | `C.\i>. VII.` (garbled `Cap. VII.`) at raw L49561 (subtitle L49563). c6 tail `…nec Sacramenta tria praedicta, quae hos imprimunt, ex causa aliqua iterantur, et gravis de facto iterantibus debet poena imponi propter divini contumeliam Sacramenti; licet alia quatuor ex causis diversis possint sine sui contumelia iterari.` = raw L49545–49559 | 4 / 4 (8). Blocks 4/4: L nn. 1–4 with n. 4 (`Cfr. tom. IV. pag. 146, nota 7. — Inferius pro *sui*, quod C E T omittunt, multi codd. *sua*, 2 *alia*.`) **closing complete**, and R opening **NUMBERED at n. 5** (`C I K L M O V cuiuslibet…`) → **p. 271's own gutter runover NEGATIVE**, tested from the band. Last entry n. 8 (`Aristot., I. de Caelo et mundo, text. 32. (c. 4.) et III. de Anima, text. 45. (c. 9.) docet, quod Deus et natura nihil faciunt frustra neque deficiunt in necessariis.`), complete. **This is the leaf carrying the pass-1-resolved n. 2 — see the dedicated section below** | **CLEAN** |
| 7 | `p6-c7` → `p6-c8` | p. 272 (mid-page) | `Cap. VIH.` (garbled `Cap. VIII.`) at raw L49709 (subtitle L49711). c7 tail `…hinc est, quod utrique exorcizari debent ad expulsionem potestatis contrariae, utrique etiam catechizari: adulti, ut, expulsa caligine erroris, informentur ad fidem; parvuli vero, ut sciant patrini, quid eos debeant edocere, ne pro humano defectu impediatur baptismatis Sacramentum, quominus habeat finem suum.` = raw L49693–49707 | 7 / 1 (8). Blocks 5/3: L nn. 1–5, **n. 5 breaking mid-word-pair** at `Vat., 1 et 3 addunt *seu*`, R opening **UNNUMBERED** (`*diaphaneitate*. Mox pro *et etiam* plures codd., inter quos L M V Z, *et similiter*.`) → **gutter runover POSITIVE at n. 5**, logged by `p6-c7` and rendered joined in `[^p272-5]`. Last entry n. 8 (`Vide IV. Sent. d. 7. per totam… Post *crucis* aliqui codd. addunt *et*.`), complete. **This is the leaf carrying the pass-1-resolved n. 6 — see below** | **CLEAN** |
| 8 | `p6-c8` → `p6-c9` | p. 273 (mid-page) | `Cap. IX.` at raw L49860 (subtitle L49862). c8 tail `…Non enim potest crucis gloria libere praedicari, si crucis poena et ignominia formidetur, iuxta quod sanctus dicebat Andreas: « Ego, si crucis ignominiam expavescerem, crucis gloriam non praedicarem ».` = raw L49844–49858 | 6 / 1 (7). Blocks 5/2: L nn. 1–5, **n. 5 breaking on a siglum run** at `Subinde pro *propulsandam* I M O V` (followed by the printer's signature `S. Bonav. — Tom. V.`, **which is not an entry**), R opening **UNNUMBERED** (`*propellendam*, L *repellendam*, et pro *potestativa* P *episcopi*, W *pontificum*.`) → **gutter runover POSITIVE at n. 5**, logged by `p6-c8`. Last entry n. 7 (`E K addunt *enim*… Subinde post *circumscriptibiliter* Vat., 1 et 3 addunt *nec localiter*.`), complete, followed by the quire signature `35` | **CLEAN** |
| — | *(no boundary on p. 274)* | — | `p6-c9` spans p. 273 n. 7 → p. 275 n. 4 and **owns all eight of p. 274** — the only leaf in Pars VI wholly inside one chunk | 0 / 8 (8), all `p6-c9`. Blocks 5/3: L nn. 1–5, **n. 5 breaking at a dash** (`…ut nos redimeret etc. —`), R opening **UNNUMBERED** → **gutter runover POSITIVE at n. 5**, logged by `p6-c9`. Last entry n. 8 (`Secundum August., in Ioan. Evang. tr. 26. n. 17… Vat., 1 et 3 cum uno alteroque cod. in qua.`), complete | **CLEAN** |
| 9 | `p6-c9` → `p6-c10` | p. 275 (mid-page) | `Cap. X.` at raw L50129 (subtitle L50131). c9 tail `…ut tam ipsi sacerdotes conficientes quam etiam suscipientes percipiant gratiae donum, per quam purgentur, illuminentur, perficiantur, reficiantur, vivificentur et in ipsum Christum per excessivum amorem ardentissime transferantur.` = raw L50113–50127 | 4 / 3 (7). Blocks 4/3: L nn. 1–4, **n. 4 breaking at a word boundary** (`qui etiam inferius cum`), R opening **UNNUMBERED** (`nonnullis aliis codd. pro *excessivum* substituunt *excellentissimum*…`) → **gutter runover POSITIVE at n. 4**, logged by `p6-c9`. Last entry n. 7 (`A addit *tantum*, Vat., 1 et 3 *solum*… edd., excepta 2, *convertibilis*.`), complete with blank paper beneath | **CLEAN** |
| 10 | `p6-c10` → `p6-c11` | p. 276 (mid-page) | `Cai'. \l.` (= `Cap. XI.`, badly garbled — **no `XI` grep finds it**) at raw L50318, subtitle `Dc intcgritale unctionis cxlrcinue.` L50320. c10 tail `…ut sic tanquam veri Dei iudices ligandi et solvendi integram possideant potestatem, per quam impoenitentes feriant et compescant rebelles, et nihilominus absolvant et reconcilient Deo et sanctae matri Ecclesiae veraciter poenitentes.` = raw L50302–50316. **The heading was reached by walking down from Cap. X, not by grep** | 5 / 1 (6). Blocks 3/3: L nn. 1–3, **n. 3 breaking at `ubi sub hoc triplici`**, R opening **UNNUMBERED** (`respectu explicantur diversae definitiones poenitentiae. — Superius pro *medicamentum*…`) → **gutter runover POSITIVE at n. 3**, logged by `p6-c10`. Last entry n. 6 (`De hoc cap. vide IV. Sent. d. 23. per totam.`), complete with blank paper beneath | **CLEAN** |
| 11 | `p6-c11` → `p6-c12` | p. 277 (mid-page, **right column**) | `C.\p. XII.` (garbled `Cap. XII.`) at raw L50468, subtitle `De inlegritate ordinis.` L50470. c11 tail `…in dante, quia illud ab episcopis, hoc autem a sacerdotibus quibuscumque. Et haec omnis diversitas a fine procedit, quia, sicut claruit, diversitas in finibus proximis diversitatem introducit in his quae ad fines illos habent finaliter ordinari.` = raw L50452–50466. **Independently corroborated on the plate:** the `De integritate ordinis` subtitle and `De Sacramento ordinis haec in summa tenenda sunt…` stand at the **head of p. 277's right column**, visible on the R band | 6 / 1 (7). Blocks 4/3: L nn. 1–4 with n. 4 (`Cfr. supra pag. 273, nota 4.`) **closing complete**, R opening **NUMBERED at n. 5** → **p. 277's own gutter runover NEGATIVE**. Last entry n. 7 (`Ut dicit Magister Sententiarum, IV. Sent. d. XXIV. c. 13… — De hoc cap. cfr. IV. Sent. d. 24.`) — **BREAKS OFF at the page foot; this is the page-crossing runover** (see below) | **CLEAN** |
| — | *(no boundary on p. 278)* | — | `p6-c12` spans p. 277 n. 7 → p. 279 n. 1 and **owns all five of p. 278** | 0 / 5 (5), all `p6-c12`. **The left block opens with an INHERITED UNNUMBERED continuation** — `et 25. — P hic et infra *ordinando*. Inferius post *episcopatus* F bene addit *archiepiscopatus*…`, which completes p. 277 n. 7's `…cfr. IV. Sent. d. 24.` → **p. 277 → p. 278 page-crossing runover POSITIVE, closed from BOTH sides.** Logged once, by `p6-c12`, as `p.277 n.7:page`; **not re-logged here.** Then L nn. 1–2, **n. 2 breaking at `— De perfectione`**, R opening **UNNUMBERED** (`numeri senarii cfr. I. Sent. d. 2. q. 4. scholion…`) → **p. 278's own gutter runover POSITIVE at n. 2**, also logged by `p6-c12`. Last entry n. 5 (`Cfr. supra Quaest. de perfectione evang. q. 4. a. 3.`), complete | **CLEAN** |
| 12 | `p6-c12` → `p6-c13` | p. 279 (mid-page) | `Cap.  XIII.` at raw L50667, subtitle `Dc intcgritate mutrimonii.` L50669. c12 tail `…et hoc ab episcopis, quibus propter sui eminentiam reservatur dispensatio ordinum, confirmatio per impositionem manuum, consecratio monialium et abbatum et dedicatio ecclesiarum; quae propter sui celebritatem non debent dispensari nisi ab his qui habent praeeminentiam potestatis.` = raw L50656–50665. The folio marker `279` stands at L50653, **above** the tail — used only to locate the page, never to set the boundary | 1 / 6 (7). Blocks 3/4: L nn. 1–3, **n. 3 breaking inside a parenthesis** at `(praeter impedimentum *aetatis*, quod includitur secundum`, R opening **UNNUMBERED** (`Bonav., IV. Sent. d. 36. Divis. textus, in impedimento *conditionis*) duo alia adiunguntur:` + the two hexameter lines) → **gutter runover POSITIVE at n. 3**, logged by `p6-c12` (the chunk that first reached the leaf); **`p6-c13` must not, and does not, re-log it.** Last entry n. 7 (`Cfr. IV. Sent. d. 26. a. 2. q. 2. et d. 31. a. 2. q. 1. in corp.`), complete with blank paper beneath | **CLEAN** |
| 13 | `p6-c13` → `p7-c1` | **LEAF CROSSING p. 280 → p. 281** — the outgoing seam | `PARS SEPTIMA.` found **in the raw** at L50926, subtitle `Dc slali] finalis iudicii.` L50929, `Cap. I.` L50932. c13 tail `…Sed nunquam debet nec potest matrimonium, quod legitime introductum est, annullare, quia *quos Deus coniunxit non potest homo*, quantumcumque sit magnae potentiae, *separare*, cum ipsius Dei iudicio iudicandi remaneant universi.` = raw L50880–50888 — the **last body line of p. 280**. Between it and the display heading stand a marginal-gloss block (L50891–50894), p. 280's footer register (L50897–50917), the running head `PARS VII. C. I.` (L50920) and the folio `281` (L50923). **⚠ p. 280's body ends with a very large blank tail below it** — the `p2-c4` trap in its purest form — **and that blank was used as evidence of nothing.** The boundary is set from `PARS SEPTIMA` alone | p. 280 total **6**, **all six `p6-c13`'s**; p. 281 total **5**, **all five `p7-c1`'s**. See the dedicated section below | **CLEAN** |

**14 boundaries swept (12 mid-page, 2 leaf crossings). 14 CLEAN, 0 DEFECT.**

---

## Footer accounting — every page re-read off the bands

| p. | left block | right block | plate's last numbered entry (band) | `KNOWN_TOTALS` | agree? | ownership (by anchor) |
|---|---|---|---|---|---|---|
| 264 | … | nn. 4–6 | 6 (`Psalm. 118, 164.`) | 6 | ✅ | all `p5-c10`; **nothing forwarded** |
| 265 | nn. 1–2 + sig. `S. Bonav. — Tom. V.` | nn. 3–6 | 6 (`Ut docet Magister Sententiarum, IV. Sent. d. I. c. 5. … Fide D E I K M N et 2 substituimus potentiam pro gratiam.`) + quire `34` | 6 | ✅ | all `p6-c1`; L opens numbered, R opens numbered → **both tests negative** |
| 266 | nn. 1–3 (n. 3 broken) | n. 3 cont. + nn. 4–6 | 6 (`Plurimi codd. et 2 perperam perfectos… ambulare permittit.`) | 6 | ✅ | `c1` 1 · `c2` 2–6 |
| 267 | nn. 1–4 (n. 4 broken) | n. 4 cont. + nn. 5–8 | 8 (`Cantic. 6, 3. et 9.`) | 8 | ✅ | `c2` 1–2 · `c3` 3–8 |
| 268 | nn. 1–4 (n. 4 broken **after a full stop**) | n. 4 cont. + nn. 5–8 | 8 (`Matth. 4, 17. et Marc. 1, 14. seq. — Ioan. 2, 1. seqq. — Matth. 19, 4. seqq.`) | 8 | ✅ | `c3` 1 · `c4` 2–8 |
| 269 | nn. 1–4 (n. 4 broken mid-word) | n. 4 cont. + nn. 5–8 | 8 (`Vat., 1 et 3 mediis.`) | 8 | ✅ | `c4` 1–2 · `c5` 3–8 |
| 270 | nn. 1–4 (n. 4 broken in a quotation) | n. 4 cont. + n. 5 | 5 (`Ed. 1 servare… in hoc.`) | 5 | ✅ | `c5` 1–2 · `c6` 3–5 |
| 271 | nn. 1–4 (n. 4 complete) | nn. 5–8 (opens numbered) | 8 (`Aristot., I. de Caelo et mundo, text. 32. … neque deficiunt in necessariis.`) | 8 | ✅ | `c6` 1–4 · `c7` 5–8 |
| 272 | nn. 1–5 (n. 5 broken) | n. 5 cont. + nn. 6–8 | 8 (`Vide IV. Sent. d. 7. per totam… addunt et.`) | 8 | ✅ | `c7` 1–7 · `c8` 8 |
| 273 | nn. 1–5 (n. 5 broken) + sig. | n. 5 cont. + nn. 6–7 | 7 (`E K addunt enim… nec localiter.`) + quire `35` | 7 | ✅ | `c8` 1–6 · `c9` 7 |
| 274 | nn. 1–5 (n. 5 broken at a dash) | n. 5 cont. + nn. 6–8 | 8 (`Secundum August., in Ioan. Evang. tr. 26. n. 17… in qua.`) | 8 | ✅ | all `c9` |
| 275 | nn. 1–4 (n. 4 broken) | n. 4 cont. + nn. 5–7 | 7 (`A addit tantum… convertibilis.`) | 7 | ✅ | `c9` 1–4 · `c10` 5–7 |
| 276 | nn. 1–3 (n. 3 broken) | n. 3 cont. + nn. 4–6 | 6 (`De hoc cap. vide IV. Sent. d. 23. per totam.`) | 6 | ✅ | `c10` 1–5 · `c11` 6 |
| 277 | nn. 1–4 (n. 4 complete) | nn. 5–7 (opens numbered) | 7 (`Ut dicit Magister Sententiarum, IV. Sent. d. XXIV. c. 13… d. 24.` — **breaks off**) | 7 | ✅ | `c11` 1–6 · `c12` 7; **n. 7 is the page-crossing runover onto p. 278** |
| 278 | p. 277 n. 7's tail + nn. 1–2 (n. 2 broken) | n. 2 cont. + nn. 3–5 | 5 (`Cfr. supra Quaest. de perfectione evang. q. 4. a. 3.`) | 5 | ✅ | all `c12` |
| 279 | nn. 1–3 (n. 3 broken in a parenthesis) | n. 3 cont. + nn. 4–7 | 7 (`Cfr. IV. Sent. d. 26. a. 2. q. 2. et d. 31. a. 2. q. 1. in corp.`) | 7 | ✅ | `c12` 1 · `c13` 2–7 |
| 280 | nn. 1–2 (n. 2 complete) | nn. 3–6 (opens numbered) | 6 (`Matth. 19, 6: Quod [ita etiam E K M] ergo Deus coniunxit, homo non separe`) | 6 | ✅ | all `c13`; **Pars VI ends here** |
| 281 | nn. 1–3 (n. 3 broken at `Cfr. su-`) + sig. | n. 3 cont. + nn. 4–5 | 5 | 5 | ✅ | all `p7-c1`; **L opens NUMBERED → nothing forwarded from p. 280** |

**No page's true total differed from `KNOWN_TOTALS`.** The ownership map derived from the
chunks themselves is **contiguous 1..N on every one of pp. 265–280, with zero duplicates
and zero gaps** — and it abuts exactly on both sides (`p5-c10` stops at `p264-6`,
`p7-c1` starts at `p281-1`). `check-vol5-apparatus.py` reports the same pages as
`1-N (N notes) ok`, but that script checks totals *against* `KNOWN_TOTALS`, which is
itself a hand-entered band read; **the eighteen band reads above are the independent
check it cannot perform on itself.**

### Runover ledger, re-derived from the bands rather than adopted

Positive in scope, each logged **exactly once**, by the chunk that owns the note:
`p6-c2` p.266 n.3:gutter · `p6-c3` p.267 n.4 · `p6-c4` p.268 n.4 · `p6-c5` p.269 n.4 ·
`p6-c6` p.270 n.4 · `p6-c7` p.272 n.5 · `p6-c8` p.273 n.5 · `p6-c9` p.274 n.5 **and**
p.275 n.4 · `p6-c10` p.276 n.3 · `p6-c12` **p.277 n.7:page**, p.278 n.2, p.279 n.3.
Negative and confirmed negative on the band (right block opens numbered):
`p6-c1` (p. 265) · `p6-c11` (p. 277) · `p6-c13` (p. 280).
**Twelve runovers in Pars VI — eleven gutter-crossing and one page-crossing** — matching
`manual-review/vol5-runover-ledger.tsv` line for line. The one page-crossing runover is
`p.277 n.7`, one of the five `check-vol5-census.py` reports corpus-wide, and it is
**logged by `p6-c12` and not re-logged by this pass.**

All nine page-crossing tests inside the pars (265→266 … 279→280) are **NEGATIVE except
277→278**, and each was closed from **both** sides — the prior page's right block ending
complete *and* the next page's left block opening numbered. The two seam tests
(264→265, 280→281) are likewise negative and likewise closed from both sides.

---

## The two pass-1-resolved notes — ownership and anchoring, NOT re-adjudicated

CLAUDE.md and the gate brief are explicit: `manual-review/vol5-workclose-gate-pass1.md`
settled both of these at 600 dpi as **PLATE-DEFECT — the reading is certain, the text is
wrong, nothing is emended.** **This pass does not re-open either disposition.** What it
checks is the thing a forwarded flag actually endangers: that the note is **owned once**
and **anchored right**, across every seam it was carried over.

### p. 271 n. 2 — `E F G H minus, aptae ponunt et`

- **On the band (p. 271 L-3, 450 dpi):** the entry stands as the **second note of the
  LEFT block**, reading `² Pro *videlicet*, quod edd. et pauci codd. omittunt, E F G H
  minus, aptae ponunt *et*. Inferius pro *incredulis* D P substituunt *infidelibus*.`
  The comma after `minus` and the `-ae` of `aptae` are both visible at 450 dpi, as pass 1
  found them at 600. **Recorded, not re-adjudicated.**
- **OWNERSHIP — correct and unique.** p. 271's register divides `p6-c6` nn. 1–4 /
  `p6-c7` nn. 5–8 by anchor, and n. 2 falls in `p6-c6`'s share. `grep -l "^\[\^p271-2\]:"`
  over `vol5/` returns **exactly one file**, `bon-brev-p6-c6.md`. The flag was *forwarded*
  through `p6-c7`, `p6-c8` and `p6-c11` — and all three carry it **as narrative prose in
  `## Notes` only**, with no `[^p271-2]` definition and no anchor. **The note is not
  double-logged anywhere.**
- **ANCHORING — correct.** The `[^p271-2]` marker stands in `p6-c6`'s Latin at
  `…secundum quem habet fieri distinctio in populo christiano, videlicet[^p271-2] in acie
  ecclesiasticae hierarchiae…`, i.e. **immediately after the very word the note's lemma
  quotes** (`Pro *videlicet*…`). The English mirrors it. Three occurrences of the token in
  the file = Latin anchor + English anchor + definition, which is exactly right.

### p. 272 n. 6 — `Respicitur Col. 6, 12.`

- **On the band (p. 272 R-3, 450 dpi):** the entry is the **second numbered entry of the
  RIGHT block** — the block opens with n. 5's unnumbered continuation `diaphaneitate. Mox
  pro et etiam…`, and n. 6 follows. It reads `⁶ Respicitur Col. 6, 12. — Praecedens
  sententia, quae etiam paulo inferius recurrit, est Magistri Sent., II. Sent. d. XXX.
  c. 9. Cfr. Hugo S. Vict., Sum. Sent. tr. 3. c. 11. et I. de Sacram. p. VII. c. 31. —
  Superius pro *pronum* ex I K L O Q V substituimus *pronam*, F vero post *reddit*
  supplet *hominem*.` **Recorded, not re-adjudicated.**
- **The plate's own control is on the same band:** n. 7, one entry below, reads
  `Col. 1, 13: Qui eripuit nos de potestate tenebrarum et transtulit in regnum Filii
  dilectionis suae.` — the same three sorts, a genuine Colossians citation. Consistent
  with pass 1's finding that the fault is the book name, not the digits.
- **OWNERSHIP — correct and unique.** p. 272 divides `p6-c7` nn. 1–7 / `p6-c8` n. 8, and
  n. 6 falls in `p6-c7`'s share. `grep -l "^\[\^p272-6\]:"` returns **exactly one file**,
  `bon-brev-p6-c7.md`. The flag was forwarded through `p6-c8`, `p6-c11` and onward as far
  as `p7-c3` — again **as `## Notes` prose only**, never as a second definition.
  **Not double-logged.**
- **ANCHORING — correct.** The `[^p272-6]` marker stands at `…redigit etiam in diabolicam
  servitutem et in potestatem principis tenebrarum[^p272-6]` — the clause whose sense
  requires Ephes. 6:12 — and the note's second lemma (`Superius pro *pronum* … *pronam*`)
  points back to `pronam quodam modo reddit` earlier in the same sentence, which is where
  `p6-c7`'s Latin has it. `[^p272-7]` is separately anchored at the *second* occurrence of
  `principis tenebrarum`, in the next paragraph, matching the plate's own repetition.
  Both anchors are right, and they are not confused with one another.

**Verdict on both: correctly OWNED, correctly ANCHORED, logged exactly once, and
carried forward without duplication across four and six downstream chunks respectively.
Neither disposition was re-opened.**

### Also confirmed still correctly NOT flagged

`p6-c8`'s `apparatus:p273-6` dangling `tom. I. pag. 155` was read on the p. 273 R band:
the entry is `⁶ *Passio S. Andreae*, apud Surium, Histor. seu vit. Sanctor., tom. XI.
pag. 745, § 4; et apud Galland. Biblioth. (tom. I. pag. 155, c. 4.)…`. **The tome is
GALLAND's *Bibliotheca*, not Quaracchi's Tomus I** — a citation-parser limitation, and
the transcription is right. **Not a defect; not to be "fixed."**

---

## The p. 264 → p. 265 leaf edge — the pars opening, read with particular care

**`PARS SEXTA` is the only pars in the Breviloquium that opens at a leaf edge.** The
consequences all held:

1. **Body.** `p5-c10`'s tail (raw L48570–48582) is the last body text of p. 264 and runs
   to a full stop with the doxology-shaped `…ad reparationem humani generis statutorum.`
   **That full stop is corroborated by the `PARS SEXTA` display heading at L48612 and by
   nothing else** — not by the `Amen`-shape, not by the running head `PARS VI. c. r.`
   (L48606) which names Pars VI on a page that is entirely Pars V's, and not by the
   folio.
2. **Registers.** p. 264 totals **6**, all `p5-c10`'s; p. 265 totals **6**, all
   `p6-c1`'s. p. 264's right block closes complete at n. 6 (`Psalm. 118, 164.`) with clear
   blank beneath, and p. 265's left block opens **numbered** at n. 1 (`Isidor., VI.
   Etymolog. c. 19. n. 40. Vide tom. III. pag. 895, nota 5. …`). **Page-crossing runover
   NEGATIVE, closed from both sides. Nothing crosses this leaf edge in either direction.**
3. **p. 265's own gutter is also NEGATIVE** — its right block opens numbered at n. 3
   (`Cfr. supra p. III. c. 3.`) — so p. 265 carries **no runover at all**, matching
   `p6-c1`'s ledger line of `-`.
4. **The printer's signature `S. Bonav. — Tom. V.` sits at the foot of p. 265's LEFT
   block, and the quire number `34` at the foot of its right block.** Neither is an entry
   and neither was counted. There is no signature on p. 264.
5. **Gutter: p. 265 is 1151, not the tool's default 1121.** The default sits on a **4 px**
   run — the loudest gutter failure in the whole of Pars VI — and five windows repeat it.
   **Anyone re-cropping p. 265 must re-profile; the default is worthless there.** Note
   that the failure is in the *lower* windows, not the upper ones, so the documented
   "display heading destroys the measurement" remedy (move the window up) is the right
   move here for the accidental reason, not the documented one.

---

## The p. 280 → p. 281 seam into Pars VII

1. **Body.** `p6-c13`'s tail (raw L50880–50888) is the last body text of Pars VI, ending
   `…cum ipsius Dei iudicio iudicandi remaneant universi.` **Below it p. 280 carries a
   very large blank tail** — the `p2-c4` trap in its purest form, and a page where a
   careless reader could equally have concluded that the chapter ended early. **The
   blank was used as evidence of nothing**; the boundary is set from the `PARS SEPTIMA`
   display heading at raw L50926 and its subtitle `Dc slali] finalis iudicii.` at L50929.
2. **Registers.** p. 280 totals **6**, all `p6-c13`'s; p. 281 totals **5**, all
   `p7-c1`'s. `p6-c13` claims nothing on p. 281 and `p7-c1` claims nothing on p. 280 —
   **this seam divides 6 / 5 with no shared page and no shared note.**
3. **p. 280's own gutter is NEGATIVE** — left block nn. 1–2, n. 2 closing complete
   (`…et pro *consequens* 2 cum D ponit *communis*.`), right block opening **NUMBERED**
   at n. 3 (`Cfr. supra pag. 240, nota 5.`).
4. **★ The page-crossing test at the pars boundary is NEGATIVE, and proving it required
   care, because p. 280's last entry is textually incomplete.** n. 6 reads, in full,
   `Matth. 19, 6: Quod [ita etiam E K M] ergo Deus coniunxit, homo non separe` — **and
   stops: no final `t` on *separet*, no closing period** — with clear blank paper beneath
   it on the band. A truncated last entry is exactly the signature of a runover, so the
   test was closed **from the other side**: **p. 281's left block opens NUMBERED at n. 1**
   (`Cfr. Matth. 16, 27; 25, 31; Apoc. 22, 12; ibid. 20, 15. de libro vitae.`), and
   p. 281's own first runover is its n. 3, which breaks at `Cfr. su-` and resumes in
   p. 281's *own* right block. **Nothing is forwarded from p. 280 into p. 281. The
   truncation is a defect in Quaracchi's forme, not a runover** — independently
   re-derived here, and agreeing with the disposition `p6-c13` records and pass 1 lists
   as closed.
5. **Gutter: p. 280 is 1331** — nine of fourteen windows rejected, the default among them
   (1328 on a **30 px** run) because the centre rule inks more heavily on this leaf than
   on any other in the range (peak 1009–1141 rows). The five sound windows agree to 1 px
   and the profile confirms them. **The chunk was built on 1331 and that is right.**
6. **What `p6-c13` forwards to `p7-c1`: nothing.** pp. 279 and 280 are fully consumed by
   Pars VI. `p7-c1`'s incoming hand-off is empty — and per CLAUDE.md that too is a claim
   to re-derive rather than a fact to adopt, which is what the ownership walk above does.

---

## The two named failure families

- **Cascade-merge splice (a tail that does not parse).** None. All fourteen prior-chunk
  tails parse as complete Latin and every one matches the raw word-for-word up to the
  receiving heading, with nothing standing between but blank lines, footer registers,
  running heads and folios. `seam-screen.py --volume 5` independently returns **0
  tail-not-terminal suspects** corpus-wide.
- **Chunk written short at a column foot.** None. Every unit's end was set from the next
  heading, found in the raw in all fourteen cases. The two places where the trap is live
  are the two leaf crossings, and **both were closed positively**: p. 264's body runs to
  the foot and the next unit's heading stands at the head of p. 265; p. 280's body ends
  **high, with a large blank tail**, and the next unit's heading stands at the head of
  p. 281 — the blank proved nothing and was not used.
- **A grammatically complete tail was treated as evidence of nothing at any boundary.**
  Pars VI supplies the sharpest attestation in the corpus so far, and it is in a *footer*
  rather than a body: **p. 268 n. 4's left half ends at a full stop** (`…A S *beneficia.*`)
  **and yet continues across the gutter** with `Subinde pro *repararetur*…`. Had the
  block break been read as an entry break, p. 268 would have counted nine notes instead of
  eight. The other eleven gutter breaks in the pars fall mid-word (p. 269 `in-`/`tentione`),
  inside a quotation (p. 270 `fundamentum` / `Sacramentorum »`), inside a parenthesis
  (p. 279 `secundum` / `Bonav., IV. Sent. d. 36.`), on a siglum run (p. 273
  `I M O V` / `propellendam`), on a dash (p. 274), on a comma (pp. 266, 267) and inside a
  single word-pair (p. 272 `seu` / `diaphaneitate`).

---

## `[?]` flags

**One live inline `[?]` in Pars VI**, and it is a documented plate defect, not an open
ambiguity:

- **`bon-brev-p6-c13`, `[^p280-6]`** — `…homo non separe`**`[?]`** in the Latin and
  `…let not man separ`**`[?]`** in the English. This is the truncated last entry described
  at item 4 of the p. 280 seam section above. `manual-review/vol5-workclose-gate-pass1.md`
  lists it as **already closed** as a PLATE-DEFECT (the other three flags "convert … now
  CLOSED, joining p. 280 n. 6's `homo non separe`"), and the chunk's own `## Notes`
  records the page-crossing test that proves it is not a runover. **The inline marker
  standing in the transcription is the correct treatment of a defective forme — it is not
  an unresolved flag, and it must not be "repaired" into `separet`.** I re-derived the
  page-crossing test independently and it holds. **Nothing edited.**

A grep for `[?]` across the other twelve Pars VI chunks' Latin, English and Apparatus
sections returns **zero** hits; the remaining occurrences in the pars are `## Notes` prose
(the boilerplate flag inventory, and the forwarded narratives of the two pass-1 flags).

Two documentation flags are raised. Both affect no corpus text and block nothing.

### `[?]` DOC-3 — five `KNOWN_TOTALS` block-vs-anchor claims rest on data this pass did not re-derive

The `KNOWN_TOTALS` comment block for pp. 268–273 carries a structural narrative — that
pp. 268, 269 and 271 run "4/4 blocks against 3/5 anchors," that p. 272's 5/3 "coincides"
where its neighbours did not, that p. 273's three lines fall "in three different places."
Every one of those claims depends on **anchor-COLUMN** data, which this pass deliberately
did not re-derive (§ Method). **Nothing here contradicts them, and nothing here confirms
them.** They are recorded as *unverified by this pass*, so that a later reader does not
mistake this log's silence for endorsement — CLAUDE.md's rule that a structural
generalisation is the least reliable line in any `## Notes` applies to them exactly. The
arithmetic that *does* matter for boundary integrity — page totals, capitulum ownership,
contiguity, runover polarity — is re-derived above and is clean on all eighteen pages.
**Do not repair anything on this account.**

### `[?]` DOC-4 — the `KNOWN_TOTALS` gutter note for p. 271 says one window blows out; I measured none

The comment for p. 271 records that the leaf fails "on its own showing — ONE window blows
out (15–35 % → 1271 on a …)". My fourteen-window sweep of p. 271 found **no window
outside the sound band at all**: all fourteen returned 1200–1204 on 59–64 px runs, and
p. 271 is one of the five cleanest leaves in the pars. **This is not a contradiction** —
15–35 % is not one of my fourteen windows, and a window that high on the page can easily
land on the running head. It is recorded only so that the comment's "p. 271 is a
difficult leaf" impression is not carried forward: **on body-row windows p. 271 is easy,
and the value 1202 the chunk used is right to within 1 px.** No edit is proposed.

---

## Observations (no defect, no repair, nothing edited)

1. **Pars VI is the corpus's cleanest pars for footer-block regularity and its least
   regular for gutter measurement.** Every one of the sixteen registers matched
   `KNOWN_TOTALS` on the first band read, and every block split was unambiguous. Against
   that, three of the eighteen leaves (pp. 265, 275, 280) return a bare default that is
   **flatly unusable** — runs of 4, 18 and 30 px — and on p. 265 the default is wrong by
   30 px. **The two properties are unrelated, and a pass that measured only the pages
   where it expected trouble would have missed all three**, because none of them is a
   pars opening in the documented sense and none carries a mid-column `Cap. N.` heading in
   the default band.
2. **`<!-- page N -->` markers stand at the BREAK, not at a paragraph boundary, in this
   pars** — `p6-c1` says so explicitly for `<!-- page 266 -->` and the same treatment runs
   through `p6-c13`. This is the `p5-c6`…`p5-c10` convention continued, applied uniformly,
   and it is not drift. Recorded because it is easy to misread as a mis-assignment at a
   seam; the ownership table above is derived from the apparatus **labels** and the bands,
   never from the markers.
3. **Raw-quality grade, given per page and per region as required.** Body quality
   **degrades sharply from p. 275 onward**: L48570–49710 (pp. 264–269) reads as clean
   continuous prose, while L50250–50320 (p. 276) is heavily mangled (`[` for `p`,
   `iurisdictio` → `iurisdiclio`, `gladium` → `(jladium`, marginalia spliced into the
   body at L50259–50263 and L50278–50280). **Cap. XI's heading is the casualty**: it prints
   `Cai'. \l.` where Cap. X three leaves earlier prints a clean `Cap. X.` The **footers**
   are, as always in Vol V, numeral-less throughout and were read only from the bands —
   no footer grade is given because the raw's footer text was never relied on.
4. **Digit and siglum reads seen on the bands and confirmed already correct in the
   chunks** (no transcription change follows from any of them, which is the point):
   p. 264 n. 6 `Psalm. 118, 164` · p. 265 n. 1 `pag. 895` and `c. 19. n. 40` · p. 267 n. 3
   `pag. 203` · p. 268 n. 1 `Eph. 5, 32` · p. 269 n. 1 `Act. 1, 5` · p. 271 n. 4
   `pag. 146` · p. 272 n. 6 `d. XXX. c. 9` and `p. VII. c. 31` · p. 273 n. 6 `tom. XI.
   pag. 745` / `tom. I. pag. 155` · p. 274 n. 8 `tr. 26. n. 17` · p. 277 n. 7 `d. XXIV.
   c. 13` beside `d. 24.` (**the same distinction written both ways inside one entry** —
   a useful internal control on the roman/arabic reading) · p. 278 n. 3 `pag. 225` and
   `pag. 195` · p. 279 n. 1 `pag. 643` and n. 2 `pag. 684`. On sigla: p. 271 n. 2's
   `E F G H` (alphabetical order decides the two-upright final sort), p. 268 n. 1's
   `I L O V`, p. 272 n. 6's `I K L O Q V`, p. 275 n. 6's `K R`, p. 279 n. 6's `D G H`.
5. **`p6-c9` is the only Pars VI chunk spanning three printed pages** (p. 273 n. 7 →
   p. 275 n. 4) and it owns p. 274 entire — the pars's only wholly-owned leaf besides
   p. 278 (`p6-c12`). Both were checked for the "no boundary here" claim positively: no
   `Cap. N.` heading falls on either leaf in the raw.

---

## Disposition

**PASS 3 CLEAN for Pars VI. Zero defects, zero repairs, no chunk edited, `KNOWN_TOTALS`
unchanged, no git write command run.**

- **14 boundaries swept — 12 mid-page, 2 leaf crossings — 14 CLEAN, 0 DEFECT.**
- **110 apparatus entries re-derived two independent ways** (chunk walk; sixteen band
  reads) and the two figures agree. Ownership is contiguous 1..N on all sixteen pages,
  with no gap, no duplicate, and exact abutment on both seams.
- **Twelve runovers, each logged exactly once**; the single page-crossing runover in
  range (p. 277 n. 7) is `p6-c12`'s and was **not** re-logged.
- **The p. 264 → p. 265 leaf edge is certified clean from the Pars VI side,
  independently derived**: both registers close complete, both tests negative from both
  sides, nothing crosses, and the boundary rests on the `PARS SEXTA` heading found in the
  raw at L48612 — never on the running head, which names Pars VI on a page wholly Pars V's.
- **The p. 280 → p. 281 seam into Pars VII is certified clean**: 6 / 5 with no shared
  page, p. 280 n. 6's textually truncated `homo non separe` proved **not** to be a
  runover by p. 281's numbered opening, and p. 280's large blank tail used as evidence of
  nothing.
- **The two pass-1-resolved notes (p. 271 n. 2, p. 272 n. 6) are correctly OWNED and
  correctly ANCHORED**, each defined exactly once, each anchored at the word its lemma
  quotes, and each forwarded across four and six downstream chunks as `## Notes` prose
  only — **no double-logging anywhere.** Neither disposition was re-opened.
- **Two documentation flags raised** (`[?]` DOC-3, `[?]` DOC-4) and **one live inline
  `[?]` recorded** (`[^p280-6]`, a closed plate defect). None affects any corpus text;
  none blocks anything.
