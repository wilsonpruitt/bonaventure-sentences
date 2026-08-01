# Vol V work-close gate — PASS 3 (cross-chunk boundary integrity), Pars VII

**Scope:** `bon-brev-p7-c1` … `bon-brev-p7-c7` — 7 chunks, printed pp. 281–291 (pdf
357–367; offset `pdf = printed + 76`). Plus the **incoming** seam `p6-c13 → p7-c1`
(**leaf crossing** p. 280 → p. 281, where `PARS SEPTIMA` opens at the HEAD of the leaf)
and **the work's terminus on p. 291, which has no outgoing seam at all.** A Pars VI agent
ran concurrently on the p. 280 side; the seam is certified here **from the Pars VII side,
independently derived, and no neighbour's finding was consulted** — the double derivation
is deliberate.

Run 2026-08-01, as pass 3 of the Breviloquium work-close gate (CLAUDE.md § "Polish-gate
cadence for Vols V–X", trigger 2 — work boundary, unconditional); the pass-3 definition is
CLAUDE.md § "Polish-blocker cadence" step 3. Companion logs:
`vol5-workclose-gate-pass3-prol-p1.md`, `-p2.md`, `-p3.md`, `-p4.md`, `-p5.md`.
**Nothing was edited; no `KNOWN_TOTALS` entry changed; no git write command was run.**

**This range is not shaped like the others.** Three of the seven capitula run longer than a
leaf, `p7-c4` spans three leaves and `p7-c7` spans four (pp. 288–291) — the longest unit in
the work — so "one capitulum, one leaf" was never this pars's shape. `p7-c7` is also the
only capitulum in the corpus with **no `Cap. N.` heading to close against**, and its end is
fixed here positively against the colophon (see the dedicated section).

Derived counts (not carried — each derived by a tool at the moment of citing):
**7 chunks, 84 apparatus entries** in scope (`re` walk of the seven `## Apparatus`
sections). The eleven printed pages in range carry, as read off the bands below,
5+7+6+10+8+8+9+6+10+7+8 = **84** notes, and **every one of them belongs to a Pars VII
chunk** — no note in the range is owned from outside it and no chunk in the range claims a
note outside it. The two figures are independent and they agree.

Corpus-wide at the same moment, `check-vol5-apparatus.py` reports **79 chunks, 681
apparatus entries — All checks passed**; `check-vol5-census.py` reports **79 on disk / 79
in ledger, rosters agree**, with **59 runovers across 79 chunks (54 gutter-crossing, 5
page-crossing; 48 chunks positive, 31 negative)**. The five page-crossing runovers are
pp. 206, 212, 246, 253, 277 — **none falls in this scope**, and that negative is
re-derived from the plate below on all eleven leaves.

---

## Method actually used

1. **Gutters re-measured fresh on every page, no constant, no parity prediction.**
   `colcrop.py`'s **own** `measure_gutter` function was lifted verbatim out of the tool's
   source and driven over **sixteen** independent row windows per page (45–92 %, 30–70 %,
   50–80 %, 35–60 %, 60–90 %, 47–60 %, 55–85 %, 40–75 %, 65–92 %, 32–52 %, 70–90 %,
   45–65 %, 20–65 %, 25–55 %, 10–45 %, 15–55 %). **No separate measuring algorithm was
   hand-rolled.** The function's low-ink run already spans the two zero-ink runs either
   side of Quaracchi's printed centre rule, so its reported width *is* the merged band and
   its midpoint the merged-band midpoint; in parallel the **per-column ink profile (blank
   band, rule island, island peak) was printed for every page at three separate row
   windows, including the pages where every window agreed.** Windows whose run fell outside
   a sound ~58–65 px were discarded — **run width is the confidence signal, not the value**
   — and where windows disagreed, step (3) of the frozen three-step method settled it off
   the profile.
   ⚠ **The Pars V finding governs this range twice over.** Six windows agreed on p. 260's
   wrong value because all six sat on the same corrupted 20 px run; **p. 284 and p. 291
   reproduce that failure exactly** — seven windows each, identical value, identical run,
   no warning from the tool. Consensus across windows that share a corrupted run is
   consensus about the corruption. It is recorded below as a rejection, not as evidence.
2. **Body continuity established POSITIVELY from the next heading**, never from white
   space (CLAUDE.md's `p2-c4` rule) — except at the terminus, where the colophon does that
   work. The raw djvu (`raw/doctorisseraphic05bona_djvu.txt`) was walked to each receiving
   unit's heading and the ~12 lines immediately preceding it compared word-for-word against
   the prior chunk's Latin tail. **All seven receiving headings AND the colophon were found
   in the raw**, four of them garbled. Raw line map:
   `PARS SEPTIMA` L50926 (+ subtitle L50929, `Cap. I.` L50932) · `Cm'. II.` L51127 ·
   `Cap. III.` L51298 · `' Ckv. IV.` L51487 · `Cap. V.` L51753 · `Cap. VI.` L51962 ·
   `Cap. VII.` L52148 · **`EXPLICIT BIIEVILOQUIUM FRATRIS BONAVENTURAE.` L52603.**
   Three headings were **additionally confirmed directly on the band** because the seam
   mattered: `Cap. VII.` at ~82 % of p. 288's right column, the full-width `PARS SEPTIMA`
   at the head of p. 281, and the colophon itself. **No boundary anywhere in this pass was
   set or corroborated from a running head.**
3. **Every printed page's footers read off the 450 dpi bands** (bands-only rule — the Vol V
   raw has no footnote numerals). For each of **pp. 280–291** the **whole register, both
   blocks, was read full-width in one crop** (rows 2540–3740 at 1.6×, from that page's
   freshly measured split): the last numbered entry of the right block and its number,
   whether the right block opens numbered or with an unnumbered continuation, whether the
   left block opens numbered, the block split point, and the presence or absence of the
   printer's signature and quire number. **Anchors, only anchors** — block structure,
   column structure and capitulum structure were kept as three independent things
   throughout. p. 280's register was read as well, to close the incoming leaf crossing from
   both sides. **p. 291 was additionally re-read at 600 dpi** (`pdftoppm -r 600 -f 367
   -l 367`) over n. 7's wedge of lost impression; that check was optional and is reported
   below.
4. Watched for the two named failure families — the **cascade-merge splice** (a tail that
   does not parse) and the **chunk written short at a column foot**. `p7-c7` at four leaves
   has the most interior column feet of any chunk in the work and was treated accordingly.

**What was NOT independently re-derived, stated plainly.** Block structure (from the bands)
and capitulum structure (from the heading positions plus chunk ownership) were both derived
here. **Anchor-COLUMN structure — which column each individual note's anchor stands in —
was re-derived only where a seam or a claim turned on it** (p. 288's six, and the
"Cap. VII's lines carry no anchor" claim). Where `KNOWN_TOTALS` asserts a per-note
anchor/block divergence on pp. 289–291 (the two consecutive one-note overruns, p. 290 n. 5
and p. 291 n. 4), **that claim is neither confirmed nor contradicted here** — it is not
load-bearing for this pass, because ownership on those three leaves is 0/N (all `p7-c7`'s)
and was verified end-to-end.

---

## Gutters measured

Adopted value = consensus of the surviving windows, cross-checked against the per-column ink
profile. "Chunk used" is the split recorded in that page's chunk `transcription_status`,
**re-derived here rather than adopted**.

| p. | adopted | sound windows / 16 (spread) | runs (px) | blank band → midpoint | rule island (peak rows @ x) | chunk used | Δ |
|---|---|---|---|---|---|---|---|
| 280 | **1331** | 9 (1330–1331, 1 px) | 61–62 | 1301–1361 → 1331 | 1328–1344 (1009 @ 1330) | 1331 | 0 |
| 281 | **1233** | 12 (1227–1236, 9 px) | 58–63 | 1206–1262 → 1234 | 1229–1239 (647 @ 1236) | 1231 | 2 |
| 282 | **1359** | 15 (1353–1364, 11 px) | 55–62 | 1332–1387 → 1359 | 1354–1365 (311 @ 1355) | 1357 | 2 |
| 283 | **1170** | 16 (1166–1174, 8 px) | 55–62 | 1143–1199 → 1171 | 1167–1175 (952 @ 1172) | 1169 | 1 |
| 284 | **1387** | 7 (1386–1388, 2 px) | 60–63 | 1356–1417 → 1386 | 1385–1388 (84 @ 1387) | 1386 | 1 |
| 285 | **1234** | 15 (1234–1235, 1 px) | 61–65 | 1203–1266 → 1234 | 1233–1236 (146 @ 1235) | 1234 | 0 |
| 286 | **1342** | **16 of 16** (1341–1343, 2 px) | 59–63 | 1313–1373 → 1343 | 1340–1344 (625 @ 1343) | 1342 | 0 |
| 287 | **1163** | 9 (1162–1163, 1 px) | 61–62 | 1133–1193 → 1163 | 1159–1164 (1288 @ 1163) | 1163 | 0 |
| 288 | **1347** | 13 (1346–1348, 2 px) | 61–65 | 1316–1379 → 1347 | 1345–1347 (464 @ 1346) | 1347 | 0 |
| 289 | **1217** | 15 (1213–1221, 8 px) | 56–65 | 1189–1246 → 1217 | 1213–1222 (170 @ 1220) | 1216 | 1 |
| 290 | **1365** | 11 (1364–1366, 2 px) | 62–65 | 1335–1396 → 1365 | 1363–1373 (302 @ 1366) | 1365 | 0 |
| 291 | **1166** | 9 (1163–1168, 5 px) | 58–63 | 1137–1197 → 1167 | 1165–1170 (785 @ 1168) | 1165 | 1 |

**Maximum divergence between this pass's measurement and the split each chunk was actually
built on is 2 px** (pp. 281 and 282), against a column width of ~1150 px. **No chunk in
Pars VII can have been built on a truncated or padded column.**

**Parity is used nowhere.** It is remarked only after the fact that the odd/even clusters
hold across pp. 280–291 — and that the two Pars III/IV measurements which refuted parity
(p. 251 = 1160 on the odd side, p. 252 = 1403 on the even) bracket everything here. Nothing
in this pass was predicted from a neighbour or from a page number.

### Measurements REJECTED, and the run widths that condemned them

- **p. 284 — SEVEN AGREEING WINDOWS, ALL WRONG. This is the p. 260 failure, reproduced.**
  The bare default (45–92 %) returns **1404 on a 21 px run**, and six further windows
  (50–80 % → 1405/24, 60–90 %, 55–85 %, 40–75 %, 65–92 %, 70–90 % → all **1404–1405 on
  21–24 px**) return the same value on the same corrupted run. Seven windows agree; not one
  trips the tool's own 15 px warning; **all seven are rejected on run width alone.** The
  45–92 % ink profile is the tell — band x = 1394–1414, **NO ISLAND AT ALL** — i.e. the
  "gutter" those windows found is a scrap of white *inside* the right column, not the
  gutter. One further window blows out the other way (47–60 % → **1279 on a 300 px run**)
  and one sits marginally high (45–65 % → 1391 on a **76 px** run, not relied on). The
  seven survivors agree at **1386–1388 on 60–63 px**; the 30–70 % profile gives band
  x = 1356–1417 with a **faintly** inked rule at x = 1385–1388 peaking only 84 rows →
  midpoint 1386, and the 15–55 % profile gives 1358–1417 → 1387. **1387 adopted**, one pixel
  from the value the chunk was built on. A 21 px run is the same species of nonsense as a
  300 px run.
- **p. 291 — the WORK'S LAST LEAF, and its default is a quiet sub-60 failure with SEVEN
  windows behind it.** 45–92 %, 30–70 %, 50–80 %, 60–90 %, 55–85 %, 40–75 % and 65–92 % all
  return **1159 on an identical 45 px run**. Rejected: 45 px is well under the ~58 px floor,
  and the profile shows why — the blank band at those rows is x = 1137–1181 with the ink
  island at **x = 1160–1178**, i.e. the rule sits hard against the band's right edge and
  truncates the zero-ink run. Nine windows survive at **1163–1168 on 58–63 px**; the 15–55 %
  profile opens the band to x = 1137–1197 (61 px) → midpoint **1167**, rule island
  1165–1170 peaking 785 rows. **1166 adopted; the 1159 default rejected.** ★ The chunk
  records the rule here printing as **two parallel islands** (x = 1160–1163 and 1166–1169);
  at the row windows profiled in this pass the two merge into one 1165–1170 island. The
  doubling is **neither confirmed nor contradicted** — it is a sub-pixel-scale claim about
  the sort, not about the split, and the split agrees to 1 px either way.
- **p. 281 — the `PARS SEPTIMA` display heading destroys the high window, exactly as rule 2
  predicts.** 10–45 % returns **1209 on a 114 px run** — the full-width display heading
  crosses the gutter over the upper page and there is no blank column run to find. Rejected.
  Three further windows fall under the floor (45–92 % → 1230/55, 30–70 % → 1234/57, 40–75 %
  → 1233/57) and are not adopted on their own. Twelve windows survive at **1227–1236 on
  58–63 px**; the 30–70 % profile gives band x = 1206–1262 → midpoint 1234 with the rule at
  1229–1239. **1233 adopted** as the window consensus, 2 px from the chunk's 1231 and
  immaterial to the crop.
- **p. 290 — five windows blow out and eleven are sound; the chunk's record says ALL
  SIXTEEN failed.** 35–60 % → **1318 on a 429 px run**, 47–60 % → **1322/438**, 32–52 % →
  **1317/430**, 70–90 % → **1250/293**, 45–65 % → **1283/357**. All five rejected. Eleven
  windows return **1364–1366 on 62–65 px**, and the 45–92 % profile gives band x = 1335–1396
  (62 px) → **1365.5**, rule island 1363–1373 peaking 302 rows, essentially centred.
  **1365 adopted — the value the chunk used, to half a pixel.** ★ `p7-c7`'s Notes state that
  *"all sixteen row windows blow out … not one survives."* **That does not reproduce with
  the standard sixteen-window set used across these gate logs** — eleven survive on sound
  runs. The chunk's window set was a different one (sixteen windows each 15 % of page
  height); the *value* is confirmed, the *generalisation* is not, and it is recorded below
  as documentation only.
- **p. 288 — the default's value survives but its provenance does not.** `colcrop.py`
  returns **1348 on a healthy-looking 61 px run**, yet three windows are in open disorder
  (47–60 % → **1304/175**, 70–90 % → **1232/293**, 45–65 % → **1298/163**). The thirteen
  survivors agree at 1346–1348 on 61–65 px and the 15–55 % profile settles it: band
  x = 1315–1378 (64 px) → midpoint **1346**, with an almost exactly centred rule at
  x = 1345–1347 peaking 464 rows. **1347 adopted.** The chunk's lesson holds and is
  re-derived: a sound default run can sit on a leaf whose windows disagree, and run width
  alone would not have caught it.
- **p. 289 — one window discarded** (47–60 % → **1176 on a 152 px run**). Fifteen survive at
  1213–1221 on 56–65 px, spread 8 px; profile band x = 1189–1246 → **1217**, with the rule
  island sitting **well left of the band centre** (1213–1222 against a 1189–1246 band) — the
  off-centre-rule species, which is why the spread is wider here than on its neighbours.
  **1217 adopted**, 1 px from the chunk's 1216.
- **p. 285 (47–60 % → 1209 on a 116 px run)** and **p. 282 (47–60 % → 1434 on a 214 px
  run)** — single blown-out windows, discarded. Both leaves are otherwise quiet.
- **p. 280 — the incoming-seam leaf, and it fails in the way a PART CLOSING fails.** Three
  windows return **1328 on a 30 px run** (45–92 %, 50–80 %, 40–75 %) and four blow out
  (60–90 % → 1222/243, 55–85 % → 1221/245, 65–92 % and 70–90 % → **1278/356**). All seven
  rejected. The cause is the one CLAUDE.md records for this leaf: Cap. XIII's body **ends
  early**, the leaf is bare from ~63 % to ~80 %, and the register sits at 80–89 %, so the
  default window straddles three ink geometries. Nine windows confined to the body agree at
  **1330–1331 on 61–62 px**, and the 15–55 % profile gives band x = 1300–1361 → midpoint
  **1330**, rule 1328–1344 peaking 1521 rows. **1331 adopted**, matching the value `p6-c13`
  used, and re-derived here independently of it.
- **p. 286 — nothing rejected, and that is worth recording.** All **sixteen** windows return
  1341–1343 on 59–63 px runs; the profile shows a heavily inked, exactly **centred** rule
  (x = 1340–1344, peak 625 rows) inside a 61 px band. The most confident measurement in the
  range, and the centre rule is present here as on every other leaf — its absence would have
  been the thing worth remarking, and it was never absent on any of the twelve leaves.
- **p. 287 — the default is under the floor and one window sits marginally wide.** 45–92 %
  returns **1160 on a 55 px run**, and 70–90 % returns 1153 on **68 px**; neither is adopted
  alone. Nine windows agree at **1162–1163 on 61–62 px**; profile band x = 1133–1193 →
  **1163**, against the **heaviest centre rule met anywhere in this quire** (island
  1159–1164, peaking 1288 rows). Narrow-run leaves here are heavy inking, not narrow
  gutters, exactly as gutter rule 5 says.

---

## Boundary table

**Seven boundaries in scope: SIX mid-page, ONE leaf crossing — plus the terminus, which is
not a seam at all.** `seam-screen.py --volume 5` sees only the mid-page class (it reports
**71 mid-page boundaries corpus-wide, 0 tail-not-terminal suspects**, of which **six fall in
this range** — pp. 282, 283, 284, 286, 287, 288). The leaf crossing p. 280 → p. 281 is
outside its denominator, and **the terminus is outside any tool's denominator, because there
is no receiving chunk to screen against** — which is precisely why it is swept by hand here
and why it is the single most load-bearing boundary in the work.

| # | Prior → Receiving | Shared page / crossing | Body continuity — evidence | Footer split (page total) | Verdict |
|---|---|---|---|---|---|
| 0 | `p6-c13` → `p7-c1` | **leaf crossing p. 280 → p. 281** — the incoming seam | `p6-c13` tail `…quia *quos Deus coniunxit non potest homo*, quantumcumque sit magnae potentiae, *separare*[^p280-6], cum ipsius Dei iudicio iudicandi remaneant universi.` = raw L50876–50888 word for word. Between it and the receiving heading the raw interleaves p. 280's marginal gloss (L50891–50894), p. 280's whole six-note footer (L50897–50917), p. 281's running head (L50920) and its folio (L50923) — **raw line order is not page order, and none of those was used.** `PARS SEPTIMA.` stands at L50926 with subtitle `Dc slali] finalis iudicii.` (L50929) and `Cap. I.` (L50932). **Confirmed on the band: the full-width display heading stands at the HEAD of p. 281, below the running head and nothing else.** ★ p. 280's body ends high and its lower page is largely blank — **that blank was not used as evidence** | p. 280 total **6**, **0/6 by PARS**: all six are `p6-c13`'s, none crosses. p. 281 total **5**, **0/5**: all five are `p7-c1`'s. Nothing crosses the pars boundary in either direction | **CLEAN** |
| 1 | `p7-c1` → `p7-c2` | p. 282 (mid-page, **left** col., ~51 % down) | `Cm'. II.` (garbled `Cap. II.`) found in the raw at L51127, with its two-line subtitle `De antecedenlibus ad iudieium, cuiusrnodi est / poenu purgatoria.` (L51129–51130). c1 tail `…Et quia una vox disceptationis terret culpabiles et assecurat innocentes; hinc est, quod una eius effigies iustos laetificabit et e contrario impios deterrebit.` = raw L51122–51125 | 2 / 5 (7). Left block nn. 1–4 with **n. 4 broken off at a dash**, `De hoc cap. vide IV. Sent. d. 20. p. I. per totam. —`; right block opens **UNNUMBERED** with `Pro *quibus sufficienter purgatis* P *a quibus sufficienter purgati*…` → **p. 282's own gutter POSITIVE**, logged once by `p7-c1`. n. 7 (`Libr. XXI. de Civ. Dei, c. 26. n. 4. — Paulo ante pro *levius* B Q et 2 *lenius*.`) ends complete with a large blank | **CLEAN** |
| 2 | `p7-c2` → `p7-c3` | p. 283 (mid-page, **left** col., ~65 % down) | `Cap. III.` found in the raw at L51298 with subtitle L51300–51301. c2 tail `…nec amplius puniri debeat spiritus iam purgatus.` = raw L51286–51296. ⚠ **The tail is a grammatically complete sentence and was treated as evidence of nothing** — the boundary is set from the heading below it | 3 / 3 (6). Left block nn. 1–4 with **n. 4 ending at `August., Enchirid. c. 109. n. 29.`**; right block opens **UNNUMBERED** with `Ibid. in Comment. a. 2. agitur de suffragiis Ecclesiae pro defunctis…` → **p. 283's own gutter POSITIVE**, logged once by `p7-c2` and **not re-logged here**. n. 6 (`Cap. 55. De praecedente cfr. IV. Sent. d. 15. p. II. — Superius voci *debitus* ex G H I K L M V ad iunximus *Deo*.`) ends complete | **CLEAN** |
| 3 | `p7-c3` → `p7-c4` | p. 284 (mid-page, **right** col., ~19 % down) | `' Ckv. IV.` (garbled `Cap. IV.`, and the reason a `Cap. IV` grep of the raw returns nothing here) found at L51487, with two-line subtitle L51489–51490. c3 tail `…cuius est in reatibus et poenis et suffragiis pondus attendere et numerum et mensuram[^p284-6].` = raw L51482–51485, the short line immediately above the heading | 6 / 4 (10). Left block nn. 1–5 ending **complete**; right block opens **NUMBERED at n. 6** (`Sap. 11, 21: Omnia in mensura et numero et pondere disposuisti.`) → **p. 284's own gutter NEGATIVE** — the only negative gutter test in the pars until p. 291. n. 10 (`Cfr. supra Prolog. § 2. et p. II. c. 4. in fine.`) ends complete with a large blank | **CLEAN** |
| 4 | `p7-c4` → `p7-c5` | p. 286 (mid-page, **left** col., ~15 % down) | `Cap. V.` found in the raw at L51753 with two-line subtitle L51755–51756. c4 tail `…et ideo in ipsius innovatione et glorificatione possunt dici omnia *innovari* et quodam modo *praemiari*.` = raw L51746–51751. ⚠ The raw interleaves p. 286's folio (`286`, L51740) and running head (L51743) **between** p. 285's footer and this tail — used for nothing | 1 / 7 (8). Left block nn. 1–4 with **n. 4 broken at a siglum run**, `Inferius pro *stipendiorum* I K L`; right block opens **UNNUMBERED** with `O P V *praemiorum*, D *praemiorum vel stipendiorum*…` → **p. 286's own gutter POSITIVE**, logged once by `p7-c4`. n. 8 (`Ioan. 5, 29: Et procedent qui bona fecerunt in resurrectionem vitae…`) ends complete | **CLEAN** |
| 5 | `p7-c5` → `p7-c6` | p. 287 (mid-page, **right** col., **three lines down**) | `Cap. VI.` found in the raw at L51962 — ⚠ **the raw scrambles this heading's surroundings badly**: it prints the subtitle as `De consequentibus ad iiidicium, / poena infernatis.` and displaces `''ut est` to L51968, four lines below. The heading itself is intact and the two-line subtitle `De consequentibus ad iudicium, sicut est / poena infernalis.` was read off the band. c5 tail `…necesse est, quod resurrectio non *seminalibus* nec *naturalibus* causis, sed *primordialibus* attribuatur, ut fiat secundum cursum mirabilem et supernaturalem et divinae imperium voluntatis.` = raw L51946–51959. **Position re-derived: the heading is the fourth line-group of the right column (rows 574–604 against a body running 361–3199), i.e. three body lines down — the chunk's record is exact** | 5 / 4 (9). Left block nn. 1–5 with **n. 5 broken mid-word** at `ex qua quae-`; right block opens **UNNUMBERED** with `dam supra pag. 216, nota 3. — Post *seminalibus* P addit *rationibus*.` → **p. 287's own gutter POSITIVE**, logged once by `p7-c5`. n. 9 ends complete with a large blank and **no printer's signature** | **CLEAN** |
| 6 | `p7-c6` → `p7-c7` | p. 288 (mid-page, **right** col., **~82 % down** — see the DOC flag) | `Cap. VII.` found in the raw at L52148 with one-line subtitle `De ijloria parailisi.` (L52150). c6 tail `…ut sic ex hac multiplicitate poenarum afflicti et *varie* et *acerbe* et *aeternaliter* crucientur, et *tormentorum fumus ascendat in saecula saeculorum*. Amen.` = raw L52133–52146. ⚠⚠ **This tail ends `Amen.` — the most boundary-looking end this work can print — and it was treated as evidence of nothing.** The heading below it is what closes Cap. VI, and it was read directly on the band as well as in the raw | 6 / 0 (6). Left block nn. 1–4 with **n. 4 broken ON A COLON, mid-citation**, at `Apoc. 14, 10: Cruciabitur igne et sulphure. Soph. 1, 12:`; right block opens **UNNUMBERED** with `Visitabo super viros defixos in faecibus suis. Cfr. supra c. 2.…` → **p. 288's own gutter POSITIVE**, logged once by `p7-c6`. n. 6 (`Vide supra pag. 180, nota 6. et pag. 224, nota 8.`) ends complete with a very large blank and no signature. **The five body lines of Cap. VII printed beneath its heading on this leaf carry NO superscript — verified directly on the band — so nothing is forwarded to `p7-c7`, whose first note is `p289-1`** | **CLEAN** |
| — | `p7-c7` → **nothing** | **p. 291 — THE WORK'S TERMINUS. No outgoing seam exists.** | See the dedicated section below | 8 / 0 (8). **Nothing forwarded** | **CLEAN** |

**7 boundaries swept (6 mid-page, 1 leaf crossing) + the terminus. 7 CLEAN + terminus
CLEAN, 0 DEFECT.**

**No tail in the range fails to parse** — all seven are grammatically complete Latin
sentences, and every one matches the raw word-for-word up to the receiving heading with
nothing standing between. `seam-screen.py --volume 5` independently returns **0
tail-not-terminal suspects** corpus-wide. **No cascade-merge signature anywhere.**

**No chunk was written short at a column foot.** Every unit's end was fixed from the NEXT
heading, or (at the terminus) from the colophon. Two boundaries in this range are exactly
the trap: `p7-c6`'s tail is `Amen.` and `p7-c7`'s tail is `…benedictus in saecula
saeculorum. Amen ⁸ ».` — a doxology closing a quoted prayer — and neither was accepted on
its own. The four-leaf `p7-c7` was checked at each of its interior column feet: p. 289's
left column ends inside n. 6's straddle region, p. 290's left column breaks after `vita
creata`, and in every case the body runs on and the chunk carries it.

---

## Footer accounting — every page re-read off the bands

| p. | left block | right block | plate's last numbered entry (band) | `KNOWN_TOTALS` | agree? | ownership |
|---|---|---|---|---|---|---|
| 280 | nn. 1–2 | opens **numbered** ³, nn. 3–6 | 6 (`Matth. 19, 6: Quod [ita etiam E K M] ergo Deus coniunxit, homo non separe`) | 6 | ✅ | all `p6-c13` — Pars VI's, listed only to close the crossing |
| 281 | nn. 1–3 + printer's signature `S. Bonav. — Tom. V.` | n. 3's **unnumbered** continuation, then nn. 4–5 + quire `36` | 5 (`Cfr. II. Cor. 5, 10. — Pro *iusti* Vat., 1 et 3 *boni*.`) | 5 | ✅ | all `p7-c1` |
| 282 | nn. 1–4 (n. 4 broken at a dash) | n. 4 cont. + nn. 5–7 | 7 (`Libr. XXI. de Civ. Dei, c. 26. n. 4. — Paulo ante pro *levius* B Q et 2 *lenius*.`) | 7 | ✅ | `c1` 1–2 · `c2` 3–7 |
| 283 | nn. 1–4 | n. 4 cont. + nn. 5–6 | 6 (`Cap. 55. De praecedente cfr. IV. Sent. d. 15. p. II. …`) | 6 | ✅ | `c2` 1–3 · `c3` 4–6 |
| 284 | nn. 1–5 | opens **numbered** ⁶, nn. 6–10 | 10 (`Cfr. supra Prolog. § 2. et p. II. c. 4. in fine.`) | 10 | ✅ | `c3` 1–6 · `c4` 7–10 |
| 285 | nn. 1–4 (n. 4 broken **mid-word** at `iu-`) | n. 4 cont. (`venescit.`) + nn. 5–8 | 8 (`Pro *quae amplius* B I K L T *quia amplius*.`) | 8 | ✅ | all `c4` |
| 286 | nn. 1–4 (n. 4 broken at a siglum run) | n. 4 cont. + nn. 5–8 | 8 (`Ioan. 5, 29: Et procedent qui bona fecerunt…`) | 8 | ✅ | `c4` 1 · `c5` 2–8 |
| 287 | nn. 1–5 (n. 5 broken **mid-word** at `quae-`) | n. 5 cont. + nn. 6–9 | 9 (`Respicitur Matth. 5, 26… et pro *summa* D *divina*, M *sua*.`) | 9 | ✅ | `c5` 1–5 · `c6` 6–9 |
| 288 | nn. 1–4 (n. 4 broken **on a colon**) | n. 4 cont. + nn. 5–6 | 6 (`Vide supra pag. 180, nota 6. et pag. 224, nota 8.`) | 6 | ✅ | all `c6` |
| 289 | nn. 1–6 (n. 6 broken **on a colon**) + printer's signature `S. Bonav. — Tom. V.` | n. 6 cont. + nn. 7–10 + quire `37` | 10 (`Vide supra c. 5. — Superius pro *plene beata* K O V *vere beata et plene*.`) | 10 | ✅ | all `c7` |
| 290 | nn. 1–5 (n. 5 broken at a **word boundary** after `vita creata`) | n. 5 cont. + nn. 6–7 | 7 (`Matth. 13, 43. … Pro *corporis*, cui permulti codd. *corporis tui*, *ut*.`) | 7 | ✅ | all `c7` |
| 291 | nn. 1–4, **n. 4 (`Matth. 22, 37.`) ending COMPLETE with a large blank and NO straddle** | opens **numbered** ⁵, nn. 5–8 | 8 (`Rom. 1, 25. Praecedens locus est Matth. 25, 21. — Textus originalis pro *est trinus* substituit *es trinus*.`) | 8 | ✅ | all `c7` — **THE WORK'S LAST REGISTER; nothing forwarded** |

**No page's true total differed from `KNOWN_TOTALS`.** The ownership map derived
independently from the chunks themselves is **contiguous 1..N on every one of pp. 281–291,
with zero duplicates and zero gaps**, and the split points match the bands exactly. No
register was dropped, none double-claimed, no page in scope is unowned.
`check-vol5-apparatus.py` reports the same pages as `1-N (N notes) ok`, but that script
checks totals *against* `KNOWN_TOTALS`, which is itself a hand-entered band read; **the
twelve band reads above are the independent check it cannot perform on itself.**

### Runovers, re-derived from the bands rather than adopted

**Positive gutter runovers in scope (nine):** p. 281 n. 3 · p. 282 n. 4 · p. 283 n. 4 ·
p. 285 n. 4 · p. 286 n. 4 · p. 287 n. 5 · p. 288 n. 4 · p. 289 n. 6 · p. 290 n. 5.
**Negative gutter tests (two), both confirmed on the band by a right block opening
numbered:** p. 284 (opens ⁶) and **p. 291 (opens ⁵)**.
**Positive page-crossing runovers in scope: NONE.** Twelve page-crossing tests were run and
**all twelve close NEGATIVE, each from both sides**: 280→281, 281→282, 282→283, 283→284,
284→285, 285→286, 286→287, 287→288, 288→289, 289→290, 290→291, and **291→292 (p. 292 is
blank paper)**. `check-vol5-census.py` independently places all five of the corpus's
page-crossing runovers (pp. 206, 212, 246, 253, 277) **outside this range**, which agrees.

The `manual-review/vol5-runover-ledger.tsv` lines for the seven chunks are
`p7-c1 p.281 n.3:gutter,p.282 n.4:gutter` · `p7-c2 p.283 n.4:gutter` · `p7-c3 -` ·
`p7-c4 p.285 n.4:gutter,p.286 n.4:gutter` · `p7-c5 p.287 n.5:gutter` ·
`p7-c6 p.288 n.4:gutter` · `p7-c7 p.289 n.6:gutter,p.290 n.5:gutter`. **Each runover is
logged exactly once, by the chunk that first reaches the leaf**; the nine positives above
match those nine ledger entries one for one, `p7-c3`'s negative is p. 284's genuine
negative, and **no runover a prior chunk already logged is re-logged by this pass.**

### Signatures, and what is not an entry

Two printer's signatures (`S. Bonav. — Tom. V.`, beneath p. 281's and p. 289's **left**
blocks) and two quire numbers (`36` beneath p. 281's right block, `37` beneath p. 289's)
stand inside the register area on these leaves. **Neither species is a footer entry**;
p. 281 would read as six notes and p. 289 as eleven to anyone counting block lines. The
eight-leaf cadence puts them on pp. 281 and 289, and it does — verified, not predicted.

### Digit, siglum and plate reads verified on the band

Both confusion classes are live across these leaves and neither dominates. Re-confirmed
**directly on the band** rather than quoted: p. 283 n. 6 `Cap. 55.` and `IV. Sent. d. 15.
p. II.` (the `3`/`5` and `1`/`4` classes one clause apart) · p. 286 n. 5 `I. Phys. text. 81.
(c. 9.)` — **the digit `p7-c5` corrected from the `p7-c4` hand-off's `84`, confirmed here on
the plate** · p. 289 n. 2 `XII. de Gen. ad lit. c. 35. n. 68.` and `tom. III. pag. 585` ·
p. 290 n. 7 `Matth. 13, 43` / `Matth. 22, 30` / `I. Cor. 15, 44` / `Sap. 5, 16` / `Ps. 36,
39` / `Ps. 16, 15` / `Ps. 35, 9` — a seven-locus chain, every numeral sound · p. 291 n. 2
`Ps. 81, 6` and `Ioan. 10, 34` · p. 291 n. 8 `Rom. 1, 25` and `Matth. 25, 21`. On sigla:
p. 289 n. 6-cont. prints **`C D F G H`** and p. 291 n. 5 **`H Q`** — two-upright `H` in
both, in alphabetical-order runs; **no single bare upright was read as `H` anywhere in the
range.** **No transcription change follows from any of these — every one is already correct
in the chunk**, which is the point worth recording.

**Items already adjudicated, confirmed here for ownership and anchoring only, NOT
re-adjudicated:**
- **p. 282 n. 4's lemma `purgatis` against the body's `expurgatis`** — the third of the
  work's three standing `[?]` flags, resolved in pass 1 of this gate (reading certain, plate
  wrong, not emended). The band confirms the entry's continuation prints `Pro *quibus
  sufficienter purgatis* P *a quibus sufficienter purgati*`; n. 4 is owned by `p7-c2`,
  anchored in Cap. II, and its runover is logged once by `p7-c1`. Nothing further is said
  about the reading.
- **p. 283's faded scan streak** (right column, photographic) — the streak is visible on the
  band; the register reads clean through it and all six entries are legible. Recorded, not
  flagged.
- **p. 284's `de Cura pro mortuis agenda`** for the received *gerenda* — transcribed as
  printed. Recorded, not flagged.
- **p. 287 n. 9's `(F *novissimum quadrantem*)`** — an apparent null variant. **Confirmed on
  the band exactly as recorded**: the note prints `…donec reddas novissimum quadrantem (F
  *novissimum quadrantem*).` Quaracchi's own, transcribed as printed. Recorded, not flagged.
- **The two `forward` citation classifications** — p. 288 n. 6's `pag. 180` (*De perfectione
  evangelica*) and p. 289 n. 6's `Quaest. de scientia Christi, q. 4.` Both were read on the
  band in the entries above and both are correct behaviour that self-resolves as the corpus
  grows. **They are NOT dangling refs** and are not re-raised.

---

## p. 291 n. 7 — the wedge of lost impression, re-checked at 600 dpi

`p7-c7` records a two-line wedge of lost impression in p. 291 n. 7, eating the end of
`sit plenu[m].`, the initial of `[M]ulti codd.` and the `[origin]` of `[origin]alis`;
examined at 6× and 14×, the paper reported bare rather than faint, with all three
restorations determinate from matter printed elsewhere on the same leaf. **The gate's
optional 600 dpi re-check was run** (`pdftoppm -r 600 -f 367 -l 367`, 3428 × 5097 px) and
the region cropped at 1.6× on top of that. **The finding holds in every particular:**

- The plate reads `⁷ Ioan. 16, 24: Petite et accipietis, ut gaudium vestrum / sit plenu␣␣␣␣
  ␣␣␣ulti codd. et 2 *sit in te plenum*. Inferius textus / ␣␣␣␣alis propositiones *Deus
  verax* et *Peto, Domine*, transpo- / nit ita ut quae hic est prima, ibi sit secunda.`
- **The gaps are bare paper, not faint ink.** At 600 dpi there is no residual stroke, no
  broken serif and no ghosting anywhere in either gap — the surrounding letters print at
  full density right up to the gap edge and resume at full density after it. This is lost
  impression (a slipped or under-inked sort), not a faded scan.
- **All three restorations are determinate from the same leaf.** `sit plenum.` is the
  formula the same note then quotes twice more and the body prints three times in the
  adjacent paragraph; `[M]ulti codd.` is Quaracchi's standard opener, and a partial
  descender of the `M` survives at the gap's right edge; `[origin]alis` is fixed by
  `Inferius textus` immediately before it and by **n. 8 on the same leaf, which prints
  `Textus originalis pro *est trinus* substituit *es trinus*.`**

**No `[?]` is warranted and none is raised.** This is recorded so that the next agent to
meet the leaf has a second, higher-resolution derivation rather than a sentence to quote —
and because no further agent is scheduled to look at it.

---

## The terminus — how p. 291's end was fixed, and what closes the Breviloquium

**This is the one boundary in the work that no heading can confirm.** `p7-c7` is the only
capitulum with no successor, so the standard method — walk to the next `Cap. N.` — has
nothing to walk to. It was fixed positively, from three independent directions, and **the
large blank paper below p. 291's register was used as evidence for nothing.**

1. **The colophon, read directly on the band.** p. 291's left column ends mid-sentence at
   `…tantumdem pro singulis, quantum` and its right column ends at `Deus *benedictus in
   saecula saeculorum. Amen* ⁸ ».` **Immediately beneath both columns, spanning the full
   measure and centred, the plate prints `EXPLICIT BREVILOQUIUM FRATRIS BONAVENTURAE.`** The
   printed vertical column rule stops above it; the horizontal footnote rule follows below
   it. Read on a full-width band at 1.6× (rows 2540–3740 of the 450 dpi leaf) — **not
   inferred, seen.**
2. **The colophon survives in the raw**, garbled, at **L52603**:
   `EXPLICIT   BIIEVILOQUIUM   FRATRIS   BONAVENTURAE.` (the `R` flattened to `II`, the
   chronic raw failure this corpus documents). It stands three lines below `…benedictus
   insaecula saeculorum. Amen^».` (L52600), which matches `p7-c7`'s tail word for word. The
   raw and the band agree, derived separately.
3. **Corroborated forward, on the plate.** **p. 292 is BLANK.** Measured, not eyeballed: at
   450 dpi p. 292 carries **1,942 ink pixels out of 9.83 M (0.0002 of the leaf)**, and
   exactly **one** image row anywhere on it has more than five ink pixels — a single speck
   at row 2897. Against it, p. 290 carries 405,497 and p. 291 carries 648,833. There is no
   text on p. 292 of any kind. **p. 293 carries a full-page display half-title** reading
   `SERAPHICI DOCTORIS / SANCTI BONAVENTURAE / ITINERARIUM MENTIS IN DEUM`, with ink confined
   to rows 1373–1871 — read directly. So pp. 291–293 are accounted for as colophon leaf,
   blank verso, and the next work's half-title, and the work map's printed 293 for the
   *Itinerarium* is confirmed on the plate.
4. **The register closes clean.** p. 291's total is **8**, matching `KNOWN_TOTALS`; **all
   eight are `p7-c7`'s**; the left block ends **complete** at n. 4 (`Matth. 22, 37.`) with a
   large blank and no straddle, the right block opens **numbered** ⁵ (so p. 291's own gutter
   test is NEGATIVE), and n. 8 ends complete with a very large blank tail and no signature.
   **Nothing is forwarded, and there is nowhere for anything to be forwarded to.**
5. **`Amen` was used for nothing.** `p7-c7`'s tail is `…benedictus in saecula saeculorum.
   Amen ⁸ ».` — a doxology closing a quoted Anselmian prayer, and the most
   boundary-shaped ending in the work. It is the colophon three lines beneath it, and not
   the `Amen`, that closes the capitulum, Pars VII and the Breviloquium. The running heads
   on pp. 289–291 all read `PARS VII. C. VII.` and are correct **only because the unit they
   name is the last one and cannot be overrun** — they were used for nothing, here as
   everywhere else in this pass.

**Nothing anywhere in the corpus is left PENDING or forwarded past p. 291.**
`check-vol5-apparatus.py` — which exists precisely to distinguish a legitimately forwarded
PENDING note from a real interior gap — reports **All checks passed** over all 79 chunks and
681 entries, with p. 291 as `1-8 (8 notes) ok` and no pending state anywhere.

---

## The two named failure families

- **Cascade-merge splice (a tail that does not parse).** None. All seven prior-chunk tails
  parse as complete Latin and every one matches the raw word-for-word up to the receiving
  heading, with nothing standing between. `seam-screen.py --volume 5` independently returns
  **0 tail-not-terminal suspects** corpus-wide.
- **Chunk written short at a column foot.** None — and this range is where the trap is
  worst. `p7-c7` alone has eight interior column feet across four leaves, `p7-c4` has six
  across three, and **two of the seven boundaries hand the pass a grammatically complete
  tail** (`p7-c2`'s `…spiritus iam purgatus.` and `p7-c6`'s `Amen.`). Every one was closed
  from the next heading. The two leaves where blank paper most invites the `p2-c4` error —
  **p. 280**, whose body stops at ~63 % with a bare third beneath it, and **p. 291**, whose
  register ends barely half-way down the leaf — were both resolved positively, the first
  from the `PARS SEPTIMA` display heading at the head of p. 281 and the second from the
  colophon.
- **The break shapes in this range, catalogued for the record**, all of them *footer-entry*
  and *column* breaks falling **inside** chunks and never at a unit boundary: mid-word
  (p. 285 n. 4 `iu-`/`venescit`, p. 287 n. 5 `quae-`/`dam`), **on a colon mid-citation**
  (p. 288 n. 4 `Soph. 1, 12:`, p. 289 n. 6 `c. 36. n. 80 :`), at a dash (p. 282 n. 4), at a
  word boundary (p. 290 n. 5 after `vita creata`), and inside a siglum run (p. 286 n. 4
  after `I K L`). **A grammatically complete tail was treated as evidence of nothing at any
  boundary in this pass.**

---

## The raw's grade, given per page and per region

- **Body prose, pp. 281–291:** broadly usable and every one of the seven receiving headings
  plus the colophon survives in it, though four are garbled (`Cm'. II.`, `' Ckv. IV.`,
  `BIIEVILOQUIUM`, and Cap. VI's surroundings). It was used as a cross-check only; where the
  band and the raw disagreed the band won.
- **One region degrades sharply and is worth naming:** the raw around **Cap. VI's heading**
  (L51962–51968) does not merely garble the subtitle, it **breaks it apart and displaces
  `''ut est` four lines below the heading**, so a reader taking raw line order as page order
  would reconstruct a two-line subtitle that the plate does not print.
- **The raw also interleaves running heads and folios *between* a page's footer and the tail
  belonging to the next page** — attested here at L50920–50923 (p. 281's head and folio
  sitting between p. 280's footer and the `PARS SEPTIMA` heading) and at L51740–51743
  (p. 286's). A trap for anyone taking raw line order as page order, and it was avoided.
- **Footers: numeral-less, as the frozen rule says, and this range shows it plainly.**
  p. 280's six entries open in the raw as `'` · `^` · `'` · `"` · `°` · `'` — six notes, six
  punctuation glyphs, not one numeral. **All twelve registers in this pass were read from
  the bands and from nothing else.**
- **One prior finding about the raw is confirmed, not merely repeated.** `p7-c4` withdrew
  its predecessor's claim that p. 284's footer is absent from the raw. **The withdrawal is
  right:** p. 284 n. 10 stands in the raw at **L51565** (`" Cfr. supra Prolog. § 2. el p. II.
  c. 4. in line.`), matching the band. The predecessor's claim was false and the withdrawal
  stands.

---

## `[?]` flags

**Zero live `[?]` flags in Pars VII.** A grep of all seven chunks returns 22 hits, and
**every one of them is `## Notes` or `transcription_status` prose** — the boilerplate "ZERO
new `[?]` flags" sentences and the roll-forward of the standing three. **There is no inline
flag in any Latin body, any English body, or any apparatus entry in the range.**

The work's three standing flags — p. 271 n. 2's `minus, aptae`, p. 272 n. 6's out-of-range
`Col. 6, 12`, and p. 282 n. 4's lemma `purgatis` — arrive at the gate as the polish docket.
**Only the third falls in this scope, and it was resolved in pass 1 of this same gate**;
it is confirmed above for ownership and anchoring only. The other two are Pars VI's and are
neither re-derived nor commented on here — **this log's silence about them is not
endorsement.**

Two flags are raised by this pass, and **both are documentation only. Neither affects any
chunk's text, any count, any ownership or any boundary verdict. Do not repair anything in
this pass.**

### `[?]` DOC-P7-1 — the recorded position of the `Cap. VII.` heading on p. 288 is wrong, in three places

`bon-brev-p7-c6`'s `transcription_status` and its `## Notes` both place the `Cap. VII.`
heading and its one-line subtitle **"at ~60 % of p. 288's RIGHT column"**, and `p7-c7`'s
Notes repeat the figure. **Measured here from the leaf's own ink profile, it stands at
~82 %.** Derivation: p. 288's right column (x = 1372…2451 at the adopted split 1347) runs
from the first body line-group at row 341 to the last at row 2887; the `Cap. VII.` heading is
the line-group at rows **2424–2453** (ink 750, the short-line signature every centred heading
in this quire shows), followed by the subtitle at 2529–2569 and five body lines. (2424 − 341)
/ (2887 − 341) = **81.8 %.**

Related and in the same place: both files say **"the four lines of Cap. VII printed beneath
its heading"**, and `KNOWN_TOTALS`'s p. 288 comment repeats it. **There are five**, read
directly off the band: `De gloria autem caelesti hoc in summa tenen- / dum est, quod in ipsa
est praemium substantiale, / consubstantiale et accidentale. Praemium, inquam, /
substantiale consistit in visione, fruitione et tentione / unius summi boni, scilicet Dei,
quem Beati videbunt`.

**Nothing load-bearing moves.** The five lines were checked for superscripts at band scale
and **carry no anchor of any kind**, so the empty hand-off from `p7-c6` to `p7-c7` is correct
as recorded, p. 288's register of six is `p7-c6`'s entire, and `p289-1` is rightly `p7-c7`'s
first note. This is recorded because the position sentence is exactly the class CLAUDE.md
names as the least reliable line in any `## Notes` — a structural generalisation written
once, quoted forward twice, and never re-derived — and because a later reader who takes
"~60 %" as the leaf's geometry would look for Cap. VI's close in the wrong half of the
column. **For calibration, the pass re-derived the other four heading positions too, and
they are sound:** p. 287's `Cap. VI.` is "three lines down the right column" — exact;
p. 286's `Cap. V.` measures 15 % against a recorded ~20 %; p. 284's `Cap. IV.` measures 19 %
against a recorded ~22 %; p. 282's `Cap. II.` measures 51 % against a recorded ~40 %. Only
p. 288's is off by more than about ten points, and it is off by twenty-two.

### `[?]` DOC-P7-2 — `p7-c7`'s "all sixteen row windows failed" on p. 290 does not reproduce

`bon-brev-p7-c7`'s Notes state of p. 290 that *"**all sixteen** row windows swept at 15 %
height blow out to runs of 208–452 px, scattering across 1239–1427; **not one survives**"*,
and draw a lesson from it ("total window disorder around a default that is right to half a
pixel"). **Swept with the sixteen-window set used across these gate logs, eleven of sixteen
windows survive on sound 62–65 px runs and agree within 2 px (1364–1366); five blow out
(1318/429, 1322/438, 1317/430, 1250/293, 1283/357).**

**The value is confirmed** — 1365, and the ink profile agrees to half a pixel (band
x = 1335–1396 → 1365.5, rule 1363–1373 centred). **The generalisation is not.** The two
sweeps used different window sets, so this is not a contradiction of fact; it is a
demonstration that a sentence of the form "not one survives" is a property of the window set
that produced it and does not travel. Recorded so the *lesson* attached to it — "abandon the
windows outright on this leaf" — is not quoted forward as a property of p. 290.

---

## Observations (no defect, no repair, nothing edited)

1. **Pars VII is the shallowest-seamed pars of the work: seven chunks over eleven leaves,
   six mid-page boundaries and one leaf crossing.** Pars V ran ten chunks over thirteen
   leaves with eleven boundaries. Three capitula here exceed a leaf and `p7-c7` spans four —
   so the "capitula are sub-page units, per-page footer splits are the norm" shape that holds
   across Partes I–VI **does not hold at the work's close**: five of the eleven leaves
   (285, 288, 289, 290, 291) have a register owned **entire** by a single chunk.
2. **The gutter failure modes in this range are all previously named, and two of them are
   the quiet kind.** p. 281 is rule 2's display-heading case (a part opening); p. 280 is the
   part-*closing* case that Pars V found on p. 264 and CLAUDE.md now records for p. 280;
   pp. 284 and 291 are the p. 260 case — **a corrupted run that seven independent windows
   agree on.** Nothing new was met. **What is worth carrying is the frequency**: two of the
   twelve leaves in this pass produced a seven-window false consensus, where Pars V found one
   in fifteen.
3. **The centre rule stands inside the blank band on all twelve leaves.** Its absence would
   have been the thing worth remarking; it was never absent. Its inking varies from 84 rows
   (p. 284, and that faintness is exactly why p. 284's default fails a different way — the
   windows find a scrap of white inside the right column instead) to 1521 rows (p. 280) and
   1288 (p. 287).
4. **`p7-c7` is the largest single hand-read in the volume — 25 apparatus entries across
   three registers, with nothing inherited to check against.** The chunk records that it read
   pp. 289–291 twice each for that reason. **All three registers are re-derived here as a
   third read and all three match**, which is the strongest independent evidence available
   that the empty-hand-off condition did not cost anything.
5. **The `<!-- page N -->` markers behave here as elsewhere** — they round to paragraph
   boundaries in both directions, so an anchor's page label need not match its enclosing
   marker region. The ownership table above is derived from **the labels and the bands**, not
   from the markers.

---

## Disposition

**PASS 3 CLEAN for Pars VII, and for the close of the Breviloquium. Zero corpus defects,
zero repairs, no chunk edited, `KNOWN_TOTALS` unchanged, no git write command run.**

- **7 boundaries swept — 6 mid-page, 1 leaf crossing — all CLEAN, plus the terminus, CLEAN.**
- **84 apparatus entries re-derived** across 7 chunks, exactly matching the sum of the eleven
  pages' band-read registers; every page's total matches `KNOWN_TOTALS`; ownership runs 1..N
  on every page with no gap, no double claim and no unowned note.
- **Eleven runover tests re-derived on the plate** — nine positive gutter runovers
  (pp. 281, 282, 283, 285, 286, 287, 288, 289, 290) and two negative (pp. 284, 291) — each
  logged exactly once on its own chunk's ledger line, none double-counted, none re-logged
  here. **Twelve page-crossing tests, all NEGATIVE, each closed from both sides.**
- **The p. 280 → p. 281 seam is certified clean from the Pars VII side, independently
  derived**: it is a **leaf crossing**, not a shared page — Pars VI closes on p. 280 with all
  six of its notes and the full-width `PARS SEPTIMA` display heading stands at the HEAD of
  p. 281, below the running head and nothing else. p. 281's register of five is `p7-c1`'s
  entire; **its left block opens numbered ¹, so nothing crosses from p. 280**, and p. 280's
  right block opens numbered ³, so p. 280 has no gutter runover either. p. 280 n. 6's
  truncated `homo non separe` is therefore **confirmed from this side to be a plate defect
  and not a runover** — the far-side test is negative. p. 280's gutter is **1331**, not the
  tool's default 1328 on a 30 px run; p. 281's is **1233**, and any window reaching above
  ~45 % of that leaf is destroyed by the display heading.
- **The terminus is certified from three independent directions**: the full-width centred
  colophon `EXPLICIT BREVILOQUIUM FRATRIS BONAVENTURAE.` printed across both columns beneath
  p. 291's body (read on the band, and present in the raw at L52603 as `BIIEVILOQUIUM`);
  **p. 292 measured BLANK** (1,942 ink px, 0.0002 of the leaf, one row above threshold);
  and p. 293's `ITINERARIUM MENTIS IN DEUM` display half-title. The `Amen` before the
  colophon was used for nothing.
- **Nothing is left forwarded or PENDING past p. 291** — p. 291's left block ends complete at
  n. 4, its right block opens numbered ⁵ and ends complete at n. 8, and
  `check-vol5-apparatus.py` passes over all 79 chunks with no pending state anywhere.
- **p. 291 n. 7's wedge of lost impression re-checked at 600 dpi**: bare paper, not faint
  ink; all three restorations determinate from the same leaf; **no `[?]` warranted.**
- **Two `[?]`-grade flags raised, both documentation only** — DOC-P7-1 (the `Cap. VII.`
  heading stands at ~82 % of p. 288's right column, not ~60 %, and it is followed by five
  lines not four; recorded in three places) and DOC-P7-2 (`p7-c7`'s "all sixteen windows
  failed" on p. 290 does not reproduce; the value is confirmed, the generalisation is not).
  Neither affects a chunk, a count, an ownership or a boundary. **Neither blocks anything.**
