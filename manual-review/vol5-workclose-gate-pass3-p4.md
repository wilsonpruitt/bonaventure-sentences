# Vol V work-close gate — PASS 3 (cross-chunk boundary integrity), Pars IV

**Scope:** `bon-brev-p4-c1`…`-c10` — 10 chunks, printed pp. 241–252 (pdf 317–328; offset
`pdf = printed + 76`). Plus the incoming seam `p3-c11 → p4-c1` (**shared page 241**) and the
outgoing seam `p4-c10 → p5-c1` (**shared page 252**). A Pars III agent ran concurrently on
the p. 241 side and a Pars V agent takes the p. 252 side; **both seams are certified here
independently, from this side, by re-derivation — the double derivation is deliberate and
neither neighbour's finding was consulted.**

Run 2026-08-01, as pass 3 of the Breviloquium work-close gate (CLAUDE.md § "Polish-gate
cadence for Vols V–X", trigger 2 — work boundary, unconditional). Companion logs:
`vol5-workclose-gate-pass3-prol-p1.md`, `vol5-workclose-gate-pass3-p2.md`.
**Nothing was edited; no `KNOWN_TOTALS` entry changed; no git write command was run.**

Derived counts (not carried — each derived by a tool at the moment of citing):
**10 chunks, 89 apparatus entries** in scope (`re` walk of the ten `## Apparatus` sections).
The twelve printed pages in range carry, as read off the bands below,
10+6+9+7+9+9+8+8+8+9+7+6 = **96** notes; of these p. 241 nn. 1–2 belong to `p3-c11` and
p. 252 nn. 2–6 belong to `p5-c1`, so 96 − 2 − 5 = **89**. The two figures are independent
and they agree: **Pars IV owns exactly its share of its twelve pages — no note in the range
is unowned, none double-claimed, and no chunk in the range reaches outside it.**
Corpus-wide at the same moment, `check-vol5-apparatus.py` reports **79 chunks, 681 apparatus
entries — All checks passed**; `check-vol5-census.py` reports **79 on disk / 79 in ledger,
rosters agree**, 59 runovers (54 gutter-crossing, 5 page-crossing). **Exactly one of the
five page-crossing runovers falls in this scope — p. 246 n. 9** (the others are pp. 206,
212, 253, 277); it is re-derived on the plate below.

---

## Method actually used

1. **Gutters re-measured fresh on every page, no constant, no parity prediction.**
   `colcrop.py`'s **own** `measure_gutter` function was taken verbatim out of the tool's
   source and driven over **fourteen** independent row windows (45–92 %, 30–70 %, 50–80 %,
   55–90 %, 35–60 %, 60–88 %, 47–60 %, 70–92 %, 20–65 %, 25–55 %, 40–75 %, 65–90 %,
   33–85 %, 52–72 %), and in parallel a merged-band read that unites the two zero-ink runs
   either side of Quaracchi's printed centre rule (CLAUDE.md gutter rule 5) before taking
   the midpoint. **Run width is the confidence signal**: far above ~64 px or far below
   ~58 px was treated as a failure, not as a narrow gutter. Where windows disagreed, step
   (3) of the three-step method was used — the per-column ink profile was printed directly
   and the blank band and its ink island read off it. **No separate measuring algorithm was
   hand-rolled.** Every value CLAUDE.md documents for this range was re-derived from
   scratch; none was adopted.
2. **Body continuity established POSITIVELY from the next heading**, never from white space.
   For each of the eleven boundaries the raw djvu was walked to the receiving unit's
   `Cap. N.` / `PARS QUARTA` / `PARS QUINTA` heading and the ~12 lines immediately preceding
   it compared word-for-word against the prior chunk's Latin tail. **Every heading in the
   range was found in the raw** (all garbled to some degree — see the table); none had to be
   read off a band, and **none was corroborated from a running head.**
3. **Footers read off the 450 dpi bands, page by page** (bands-only rule — the Vol V raw has
   no footnote numerals). For each of pp. 241–252 the last footer entry of the **right**
   block was read at `n=6, scale 2.6` and its number compared against `KNOWN_TOTALS` in
   `tools/check-vol5-apparatus.py`. Additional bands were read where a seam or a block
   opening had to be settled: p. 241 L-5 and R-4, p. 251 L-5 and R-4, p. 252 L-5.

**What was NOT independently re-derived, stated plainly.** Block structure (from the bands)
and capitulum structure (from the heading positions plus chunk ownership) were both derived
directly here. **Anchor-COLUMN structure — which column each note's anchor stands in — was
not re-derived for every page**, because it requires reading the body bands of both columns
on all twelve leaves. Where CLAUDE.md and the `KNOWN_TOTALS` comments assert an anchor/block
divergence (pp. 244 and 245 as mirrors; p. 247's 4/4 block split against a Cap. VI/VII break
between nn. 5 and 6), **that claim is neither confirmed nor endorsed here.** It is not load
bearing for this pass: ownership is settled by capitulum, and capitulum ownership was
verified end-to-end and comes out contiguous and gapless on every page.

---

## Gutters measured

Adopted value = consensus of the surviving windows, cross-checked against the per-column ink
profile. "Chunk used" is the split re-derived here against the value recorded in that page's
chunk `transcription_status` — re-derived, not adopted.

| p. | adopted | sound windows (spread) | runs | chunk used | Δ |
|---|---|---|---|---|---|
| 241 | **1228** | 5 of 14 (all exactly 1228) | 60–61 px | 1228 | 0 |
| 242 | 1361 | 13 of 14 (1360–1362) | 61–63 px | 1361 | 0 |
| 243 | 1186 | 12 of 14 (1176–1190) | 51–63 px | 1186 | 0 |
| 244 | **1368** | 6 of 14 (1366–1373) | 59–63 px | 1367 | 1 |
| 245 | 1204 | 12 of 14 (1198–1209) | 50–62 px | 1201 | 3 |
| 246 | 1345 | 12 of 14 (1343–1346) | 60–64 px | 1345 | 0 |
| 247 | 1210 | **14 of 14** (1208–1211) | 60–64 px | 1209 | 1 |
| 248 | 1391 | 9 of 14 (1387–1398) | 54–74 px | 1391 | 0 |
| 249 | 1182 | **14 of 14** (1179–1185) | 55–62 px | 1182 | 0 |
| 250 | 1390 | 10 of 14 (1389–1390) | 63–64 px | 1390 | 0 |
| 251 | 1160 | **14 of 14** (1159–1161) | 60–64 px | 1160 | 0 |
| 252 | 1403 | 9 of 14 (1399–1404) | 54–61 px | 1403 | 0 |

**Maximum divergence between this pass's measurement and the split each chunk was actually
built on is 3 px** (p. 245), against a column width of ~1150 px. **No chunk in Pars IV can
have been built on a truncated or padded column.** Only p. 244 differs by even 1 px from the
CLAUDE.md-documented value (1368 here vs the documented 1367); the difference is inside the
window spread and immaterial to the crop.

### Measurements REJECTED, and the run widths that condemned them

- **p. 241 — `colcrop.py`'s bare default is the quiet failure this range is famous for.**
  The default (45–92 %) returns **1218 on a 39 px run**; seven further windows cluster at
  **1215–1218 on 39–45 px runs**. All rejected on run width. The five windows that stay
  above the ~58 px floor (30–70 %, 35–60 %, 47–60 %, 20–65 %, 25–55 %) return **1228 on
  60–61 px runs, with zero spread.** Settled at step (3): the 30–70 % ink profile shows a
  blank band **x = 1199–1258** with an ink island at **x = 1225–1232, peak ink 1088** —
  by far the most heavily inked centre rule in the range, which is exactly why it truncates
  the zero-ink run and drags the default 10 px low. Midpoint **1228**. *This is CLAUDE.md's
  own worked example and it reproduces exactly; it is re-derived here, not quoted.*
- **p. 244 — a LOUD failure, and the tool flags it.** The default returns **1346 on a 10 px
  run** (below the tool's own 15 px warning threshold); three further windows repeat 1346 on
  9–11 px runs. Two more blow out entirely: 47–60 % → **1259 on a 282 px run**, 70–92 % →
  **1244 on a 321 px run**. p. 244 is one of the two leaves CLAUDE.md names as a genuine
  *marginal-gloss* case (with p. 240), and moving the window up does escape it here: the six
  upper/middle windows agree at **1366–1373 on 59–63 px runs**. Ink profile at 30–70 %:
  blank 1339–1363, island 1364–1372 (peak 604), blank 1373–1397 → merged midpoint **1368**.
- **p. 245 — two windows blow out, and the default is under the floor.** 47–60 % → **1240 on
  a 312 px run**; 52–72 % → **1236 on a 233 px run**. Both rejected. The default's own value
  (1206) sits on a **56 px** run — under the ~58–60 px soundness floor, so it is *not*
  adopted on its own; it survives only as one of twelve concordant windows spanning
  1198–1209. The ink profile drifts with the window (45–92 %: band 1179–1234, island
  1200–1213, peak 143; 30–70 %: band 1173–1228, island 1197–1207, peak 101) — a *lightly*
  inked centre rule sitting off centre, the pp. 248/249 species in mild form. **Adopted 1204
  as the window consensus, not from any single profile.**
- **p. 248 — four windows rejected on run width**: 47–60 % (**1354 / 294 px**), 70–92 %
  (**1255 / 327 px**), 65–90 % (**1255 / 327 px**), 25–55 % (**1300 / 251 px**). The default
  returns 1391 on a **54 px** run — under the floor, so escalated to step (3): the 45–92 %
  ink profile shows blank **1365–1384**, island **1385–1394** (peak 92), blank **1395–1418**
  → merged band 1365–1418, **midpoint 1391**. The 30–70 % profile gives 1368–1424 → 1396.
  The nine surviving windows span 1387–1398; **1391 adopted**, agreeing with the value the
  chunk was built on.
- **p. 252 — the `PARS QUINTA` display heading destroys every upper window.** 25–55 % →
  **1245 on a 332 px run**, 47–60 % → **1288 / 284 px**, 70–92 % → **1285 / 296 px**. All
  rejected; this is CLAUDE.md rule 2's named case and it reproduces (the documented figure
  was "four upper windows at 1245–1257 on ~330 px runs" — measured fresh here as three
  windows at 1245–1288 on 284–332 px, the same species, slightly different window set). A
  fourth window, 20–65 %, returns the *right* value (1399) on a useless **27 px** run and is
  likewise not relied on. Nine body-row windows agree at **1399–1404**; the 45–92 % ink
  profile shows blank 1376–1398, island 1399–1405 (peak 428), blank 1406–1430 → midpoint
  **1403**.
- **p. 243 — the default is under the floor.** 45–92 % returns **1180 on a 50 px run**;
  55–90 % gives 1180 / 51 px. Neither is adopted alone. Twelve windows span 1176–1190 on
  51–63 px runs → **1186**.
- **p. 250 — four windows rejected**: 47–60 % (**1412 / 108 px**), 52–72 % (**1400 /
  111 px**), 65–90 % (**1422 / 108 px**), 70–92 % (**1379 / 273 px**). The ten survivors
  return 1389–1390 on 63–64 px runs, and the 30–70 % profile is textbook: blank 1359–1388,
  island **1389–1391** (peak 399), blank 1392–1421 → **1390**. A *centred*, cleanly printed
  centre rule — the pp. 250/251/253 configuration CLAUDE.md describes.
- **p. 246 — two windows rejected**: 70–92 % (**1275 / 200 px**), 52–72 % (**1300 /
  154 px**). Twelve survivors sit inside 3 px.
- **p. 242 — one window rejected**: 70–92 % → **1093 on a 16 px run**, a page-foot artefact
  ~270 px away from the true value. The other thirteen windows sit inside 2 px.
- **Parity is used nowhere.** It is remarked only after the fact that the odd/even clusters
  hold across pp. 241–252 — and that p. 251 (**1160**) and p. 252 (**1403**) are the two
  measurements CLAUDE.md cites as having burst the old parity bands in both directions.
  They are re-derived here on 60–64 px and 54–61 px runs respectively and both are sound.

---

## Boundary table

**Eleven boundaries: eleven mid-page, ZERO leaf crossings.** Pars IV is the first stretch of
the Breviloquium in which *every* boundary — including both pars transitions — falls inside
a printed page. `seam-screen.py --volume 5` independently sees exactly these eleven in the
range (71 mid-page corpus-wide, **0 tail-not-terminal suspects**); here, uniquely, it has no
blind spot, because there is no leaf crossing for it to miss. The page on which each
boundary falls was fixed from the raw's own running heads and quire signatures
(L45018 `PARS IV. C. I.` + sig 241 · L45186 sig 242 · L45331 head + L45334 sig 243 ·
L45480 head 244 · L45635 head + L45638 sig 245 · L45778 sig + L45781 head 246 · L45933 sig
247 · L46074 sig + L46077 head 248 · L46224 sig 249 · L46374 head 250 · L46517 head 251 ·
L46664 sig + L46667 head 252) — used only to locate a *page*, never to set a boundary.

| # | Prior → Receiving | Shared page | Body continuity — evidence | Footer split (page total) | Verdict |
|---|---|---|---|---|---|
| 0 | `p3-c11` → `p4-c1` | **p. 241 (mid-page)** — the incoming seam | `PARS QUARTA.` found **in the raw** at L45036 (subtitle `De incarnatione Verbi.` L45039, `Cap. 1.` L45042). `p3-c11`'s tail `…et *consummationem* sive finem habet in finali impoenitentia; … cui mediatori Domino nostro omnis *honor et gloria in saecula saeculorum. Amen*.` = raw L45024–45033 word for word, sitting **immediately** above the display heading with nothing between. The `Amen.`-shaped ending is corroborated by the following heading and **not accepted on its own** | p. 241 total **10**, split **2 / 8 by PARS, not by block**. Blocks split 5/5: L-5 band shows nn. 1–5 closing complete (n. 5 `Cfr. Ioan. 1, 3. et 14. Vide tom. III. pag. 30, nota 5…`) followed by the printer's signature `S. Bonav. — Tom. V.`; R-4 band shows the right block opening **NUMBERED at n. 6** (`Vide Bernard., Serm. 3. in Vigilia Nativit. Domini, n. 8…`), so **p. 241's gutter runover is NEGATIVE**. n. 2 (`Epist. I. Tim. 1, 17. Ibid. 2, 5: Unus et mediator Dei et hominum…`) is the doxology note on `p3-c11`'s last clause; n. 3 (`Cfr. III. Sent. d. 1. a. 2. q. 1. 3; d. 20. q. 1. 2. et 6.`) is Cap. I's first. Last entry of the right block is n. 10 (`Vide supra pag. 183, nota 3. — Edd., excepta 2, statum prioris excellentiae…`), **ending complete on the page with clear blank beneath** | **CLEAN** |
| 1 | `p4-c1` → `p4-c2` | p. 242 (mid-page, left col.) | `Cap. II.` found in the raw at L45217. c1 tail `…*sufficientissimus* satisfactor non est, nisi sit Deus pariter et homo: congruentissima fuit nostrae reparationi incarnatio Verbi, ut; … sic a culpa resurgeret per Verbum *incarnatum*.` = raw L45208–45215 | 2 / 4 (6); blocks 4/2 — L nn. 1–4 with **n. 4 broken off mid-word at `— Pro his ta-`**, R opening unnumbered with `men 1, 2, 3 cum pluribus codd.…` then nn. 5–6 (raw L45314/45317 confirms the mid-word break). Band's last entry n. 6 (`Secundum loquendi modum Damasc.; cfr. tom. III. pag. 268, nota 2. — Inferius pro inanimatio fere omnes codd. et 2 animatio.`), complete. Gutter runover positive, owned and logged by `p4-c2` | **CLEAN** |
| 2 | `p4-c2` → `p4-c3` | p. 243 (mid-page) | `Cap. III.` found in the raw at L45364. c2 tail `…hinc est, quod necessario fit *communicatio idiomatum*, nisi sit vocabulum, in quo aliqua repugnantia includatur; … in quibus instantia fertur contra regulam praehabitam propter causam praedictam.` = raw L45354–45362 | 3 / 6 (9); the capitulum break falls **inside the left block**. Band's last entry n. 9 (`Diffusius explicatur hoc III. Sent. d. 4. a. 1. q. 1. — Pro peracta P operata.`), complete | **CLEAN** |
| 3 | `p4-c3` → `p4-c4` | p. 244 (mid-page) | `Cah. IV.` (garbled `Cap. IV.`) found in the raw at L45518. c3 tail `…Et sic beatissima Virgo Maria mater fuit completissimo modo, ipsum Dei Filium concipiendo absque viro, fecundante Spiritu sancto. … iuxta quod conceptus ille mirabilis exigebat.` = raw L45509–45516 | 2 / 5 (7); blocks 3/4 — L nn. 1–3 with **n. 3 broken inside a square-bracketed lemma** at `pro a principio [2 cum aliquot`, R opening unnumbered `codd. a primo principio] Vat., 1 et 3 in principio…` then nn. 4–7 (raw L45616/45619 confirms). Band's last entry n. 7 (`Cfr. tom. II. pag. 330, nota 5. in fine.`), complete | **CLEAN** |
| 4 | `p4-c4` → `p4-c5` | p. 245 (mid-page) | `Cap. V.` found in the raw at L45676. c4 tail `…Decebat ductorem perfectum tunc se ostendere, cum esset opportunitas currendi ad bravium; … usque quo perveniamus *ad bravium felicitatis aeternae*.` = raw L45663–45674 | 4 / 5 (9). Band's last entry n. 9 (`B M N Q omittunt perfecte. Inferius edd. ipsam pro ipsum, quod habent L M N…`), complete. `p4-c5`'s ledger line is negative, i.e. no runover of its own on this leaf | **CLEAN** |
| 5 | `p4-c5` → `p4-c6` | p. 246 (mid-page) | `Cap. VI.` found in the raw at L45825. c5 tail `…connexi ad invicem per indivisibile vinculum caritatis. … secundum fontalem, radicalem et originalem plenitudinem omnis gratiae in Christo habitantis sicut in fonte.` = raw L45813–45823 | 5 / 4 (9). Band's last entry n. 9 (`Cfr. supra pag. 230, nota 5. — Post pauca pro *potest*`) **BREAKS OFF at the page foot** — the **page-crossing runover**, re-derived here on the plate. It resumes at the head of p. 247's left block (`A possunt, et habent pro habet…`), and `p4-c6` renders the two halves **joined** in `[^p246-9]`, which is the correct treatment. Logged once, on `p4-c6`'s ledger line; **not re-logged here** | **CLEAN** |
| 6 | `p4-c6` → `p4-c7` | p. 247 (mid-page) | `Cap. VII.` found in the raw at L46000. c6 tail `Postremo, quia sensus non est perceptivus rerum nisi ad obiecti praesentiam; hinc est, quod secundum cognitionem sensitivam non simul cognoscebat omnia, sed modo haec, modo illa, iuxta quod opportunum erat ad reparationem humani generis faciendam.` = raw L45993–45998 | 5 / 3 (8). Band's last entry n. 8 (`De hoc cap. vide III. Sent. d. 18. per totam et d. 17. a. 2. q. 1, ubi de oratione Christi.`), complete. **This is the page CLAUDE.md cites for a capitulum boundary falling inside a footer block; that claim rests on anchor-column data this pass did not re-derive and is neither confirmed nor endorsed** — ownership by capitulum (c6 nn. 1–5, c7 nn. 6–8) is verified and gapless either way | **CLEAN** |
| 7 | `p4-c7` → `p4-c8` | p. 248 (mid-page) | `C.\p. VIII.` (garbled `Cap. VIII.`) found in the raw at L46144. c7 tail `…nisi per meritum hominis-Dei, cui dicere possumus et debemus: *Omnia opera nostra operatus es in nobis, Domine*. Ipse, inquam, est Dominus, cui Propheta dicit: *Dixi Domino: Deus meus es tu, quoniam bonorum meorum non eges.*` = raw L46135–46142. **⚠ The running head is worthless here in BOTH directions and was used for neither purpose: the raw's head at L46077 reads `BREVILOQUII PARS IV. C. VI`, while CLAUDE.md records the band as reading `PARS IV. C. VIII`. Whichever the plate carries, the boundary is set from the `C.\p. VIII.` heading and from nothing else** | 5 / 3 (8). Band's last entry n. 8 (`Epist. I. Tim. 2, 5. — Vide III. Sent. d. 19. a. 2. q. 2, … proferuntur.`), complete. Gutter runover positive inside n. 5, owned and logged by `p4-c7` | **CLEAN** |
| 8 | `p4-c8` → `p4-c9` | p. 249 (mid-page) | `Cap. IX.` found in the raw at L46296. c8 tail `…voluntas *divina* iustitiam, voluntas *rationalis* obedientiam, voluntas *carnis* naturam »; ac per hoc non erat in Christo colluctatio et pugna, sed pacata ordinatio et tranquillitas ordinata.` = raw L46285–46294 | 6 / 2 (8). Band's last entry n. 8 (`Vide III. Sent. d. 20. q. 5. — Superius pro debet D E H debuit…`) complete, followed by the quire signature `32` — **which is not an entry**. Gutter runover positive inside n. 6, owned and logged by `p4-c8` | **CLEAN** |
| 9 | `p4-c9` → `p4-c10` | p. 250 (mid-page) | `Cap. X.` found in the raw at L46471. c9 tail `…hinc est, quod Christus non fuit homo in illo triduo, licet anima et caro essent unitae cum Verbo. Unde quia mors in *humana natura*… per medium efficacissimum liberatus.` = raw L46455–46469 | 9 / 0 (9) — **Cap. X opens on p. 250 and claims no note there**; `p4-c9` owns the whole register. Band's last entry n. 9 (`Epist. I. Cor. 15, 54. — Cfr. III. Sent. d. 19. a. 1. per totum. — Superius post mortua est A addit semper.`), complete. The zero-claim was verified positively from the ownership map, which runs 1–9 contiguous under `p4-c9`, and from the band, not inferred from `p4-c10`'s silence | **CLEAN** |
| 10 | `p4-c10` → `p5-c1` | **p. 252 (mid-page)** — the outgoing seam | `PARS aUINTA.` (garbled `Q`, which is why a `QUINTA` grep returns nothing) found **in the raw** at L46700, after the running head `BREVILOQUII PARS V. C. I.` (L46667) and signature `232`=252 (L46664). c10 tail `…quod *uni datur per Spiritum sermo sapientiae … dividens singulis, prout vult*, secundum suam liberalissimam providentiam et providentissimam largitatem.` = raw L46689–46697. **Independently corroborated on the plate that Cap. X carries over the leaf and was not written short at p. 251's foot:** p. 251's right column ends mid-sentence at `…sicut debitam servavit horam in *patiendo*⁷, sic in *resurgendo*, sic in` and the raw resumes at L46670 `ascendendo in caelum, sic in mittendo Spiritum sanctum…`. c10's `<!-- page 252 -->` marker is present | p. 252 total **6**, split **1 / 5 by PARS** — the most lopsided division in Pars IV. Blocks 3/3: L-5 band shows the left block opening **NUMBERED at n. 1** (`Epist. I. Cor. 12, 8-11. Vulgata hinc inde plura addit…`) and carrying nn. 1–3; R-5 shows nn. 4–6 with the last, n. 6 (`I M beatificativae.`), **ending complete with a large blank beneath**. n. 1 anchors on `prout vult` in Cap. X (`p4-c10`'s `[^p252-1]`); n. 2 (`Iac. 1, 17. — Seq. locus est Apoc. 22, 1…`) anchors in Pars V Cap. I | **CLEAN** |

**11 boundaries swept (11 mid-page, 0 leaf crossings). 11 CLEAN, 0 DEFECT.**

---

## Footer accounting — every page re-read off the band

| p. | plate's last numbered entry (band) | `KNOWN_TOTALS` | agree? | ownership |
|---|---|---|---|---|
| 241 | 10 (`Vide supra pag. 183, nota 3. — Edd., excepta 2, statum prioris excellentiae…`) | 10 | ✅ | `p3-c11` 1–2 · `p4-c1` 3–10 (split by PARS; blocks 5/5, R opens numbered at n. 6) |
| 242 | 6 (`Secundum loquendi modum Damasc.; cfr. tom. III. pag. 268, nota 2.`) | 6 | ✅ | `c1` 1–2 · `c2` 3–6; n. 4 crosses the gutter mid-word |
| 243 | 9 (`Diffusius explicatur hoc III. Sent. d. 4. a. 1. q. 1.`) | 9 | ✅ | `c2` 1–3 · `c3` 4–9; n. 5 crosses the gutter |
| 244 | 7 (`Cfr. tom. II. pag. 330, nota 5. in fine.`) | 7 | ✅ | `c3` 1–2 · `c4` 3–7; n. 3 crosses the gutter inside a bracketed lemma |
| 245 | 9 (`B M N Q omittunt perfecte…`) | 9 | ✅ | `c4` 1–4 · `c5` 5–9; no runover |
| 246 | 9 (`Cfr. supra pag. 230, nota 5. — Post pauca pro potest` — **breaks off**) | 9 | ✅ | `c5` 1–5 · `c6` 6–9; **n. 9 is the page-crossing runover onto p. 247** |
| 247 | 8 (`De hoc cap. vide III. Sent. d. 18. per totam et d. 17. a. 2. q. 1…`) | 8 | ✅ | `c6` 1–5 · `c7` 6–8; left block opens with p. 246 n. 9's tail |
| 248 | 8 (`Epist. I. Tim. 2, 5. — Vide III. Sent. d. 19. a. 2. q. 2…`) | 8 | ✅ | `c7` 1–5 · `c8` 6–8; n. 5 crosses the gutter |
| 249 | 8 (`Vide III. Sent. d. 20. q. 5…`) + quire signature `32` | 8 | ✅ | `c8` 1–6 · `c9` 7–8; n. 6 crosses the gutter |
| 250 | 9 (`Epist. I. Cor. 15, 54. — Cfr. III. Sent. d. 19. a. 1. per totum.`) | 9 | ✅ | all `c9`; Cap. X opens here and claims none; n. 3 crosses the gutter |
| 251 | 7 (`Secundum Glossam Bedae in Marc. 15, 33…`) | 7 | ✅ | all `c10`; n. 4 crosses the gutter, splitting `Enarrat.` / `in Ps. 149, 6` |
| 252 | 6 (`I M beatificativae.`) | 6 | ✅ | `c10` 1 · `p5-c1` 2–6; **Pars IV ends here, nothing forwarded** |

**No page's true total differed from `KNOWN_TOTALS`.** The ownership map derived from the
chunks themselves is **contiguous 1..N on every one of pp. 240–253, with zero duplicates and
zero gaps** — so no register was dropped, none double-claimed, and no page in scope is
unowned. `check-vol5-apparatus.py` reports the same pages as `1-N (N notes) ok`, but that
script checks totals *against* `KNOWN_TOTALS`, which is itself a hand-entered band read;
**the twelve band reads above are the independent check it cannot perform on itself.**

The `manual-review/vol5-runover-ledger.tsv` lines for the ten chunks are
`c1 -` · `c2 p.242 n.4:gutter` · `c3 p.243 n.5:gutter` · `c4 p.244 n.3:gutter` · `c5 -` ·
`c6 p.246 n.9:page` · `c7 p.248 n.5:gutter` · `c8 p.249 n.6:gutter` · `c9 p.250 n.3:gutter` ·
`c10 p.251 n.4:gutter`. **Each runover is logged exactly once, by the chunk that owns the
note** — the double-count the ledger exists to prevent does not occur here, and the one
page-crossing runover in the range (p. 246 n. 9) is logged by `p4-c6` and is *not* re-logged
by this pass.

### Digit and siglum reads verified on the plate

Both confusion classes are live across these leaves, and several readings CLAUDE.md lists as
consolidated Pars III–IV corrections were re-confirmed **directly on the band** rather than
quoted: p. 241 n. 9 `c. 55. n. 110` (the `3`/`5` class) · p. 242 n. 5 `pag. 205` · p. 250
n. 9 `I Cor. 15, 54` · p. 249 n. 7 `Marc. 15, 28` · p. 251 n. 1 `pag. 395` (raw `39-3`) and
`Eph. 4, 8` (raw `l, 8`) · p. 251 n. 4 `Eccli. 21, 4` and `Ps. 149, 6. n. 12` · p. 251 n. 7
`pag. 463` / `pag. 458` / `horarum 36`. On sigla: p. 251 n. 4's run prints **`H I O Q V`**
where the raw flattens it to `IIIOQV` — the alphabetical-order rule decides it, and the
chunk carries `H I O Q V` correctly; p. 247 n. 6's `F H L` and p. 248 n. 6's `B H` are the
same two-upright case. **No transcription change follows from any of these — every one of
them is already correct in the chunk**, which is the point worth recording.

One further plate fact, transcribed as printed and correctly so: **p. 251 n. 4 prints
`(graece ῥομφαία]` — an opening parenthesis closed by a square bracket.** That is
Quaracchi's own compositor error; it was checked on the 450 dpi band (p. 251 R-4) rather
than assumed, and `p4-c10` reproduces it exactly. **Quaracchi is never silently emended, so
this is right as it stands — no `[?]` is warranted, and it should not be "fixed" by a later
pass that meets it without this note.**

---

## The two named failure families

- **Cascade-merge splice (a tail that does not parse).** None. All eleven prior-chunk tails
  parse as complete Latin and every one matches the raw word-for-word up to the receiving
  heading, with nothing standing between. `seam-screen.py --volume 5` independently returns
  **0 tail-not-terminal suspects** corpus-wide.
- **Chunk written short at a column foot.** None. Every unit's end was set from the next
  heading, found in the raw in all eleven cases. The one place where the trap is live —
  `p4-c10` at the foot of p. 251, where the register is deep and the body column ends
  high — was closed **positively from the plate**: p. 251's right column ends *mid-sentence*
  at `sic in`, the text resumes at the head of p. 252, and the chunk carries it.
- **CLAUDE.md's Pars IV breakage catalogue re-derived.** The three consecutive capitula
  breaking on a stranded preposition, and the two breaks where both halves read as complete
  sentences, are **footer-entry and column breaks, not unit boundaries** — they fall inside
  chunks, not between them, and none of them coincides with any of the eleven boundaries
  above. Attested here directly: the mid-word break `— Pro his ta-` / `men` (p. 242 n. 4),
  the break inside a bracketed lemma `[2 cum aliquot` / `codd.` (p. 244 n. 3), the break
  splitting a work's title `Enarrat.` / `in Ps. 149, 6` (p. 251 n. 4), and the mid-word
  scriptural break `Non mea vo-` / `luntas` inside `p4-c8` (raw L46281/46284). **A
  grammatically complete tail was treated as evidence of nothing at any boundary in this
  pass.**

---

## `[?]` flags

**Zero `[?]` flags in Pars IV.** All ten chunks match `[?]` only inside the boilerplate
`**No `[?]` flags.**` sentence in their own `## Notes` (`p4-c3` additionally uses the token
once to say a supplied reading is *not* a flag). There is no inline flag in any Latin body,
any English body, or any apparatus entry in the range.

One flag is raised here, and it is a documentation flag, not a text defect.

### `[?]` DOC-2 — three structural generalisations in `KNOWN_TOTALS` rest on data this pass could not re-derive

The `KNOWN_TOTALS` comment block for pp. 244–251 is unusually rich, and most of it is
verified above. But three of its claims are of exactly the kind CLAUDE.md names as the least
reliable line in any `## Notes` — *"the first COINCIDENCE page in Pars IV"* (p. 245),
*"a TRUE COINCIDENCE PAGE"* (p. 246), *"the widest three-line spread yet"* (p. 250) — and
all three depend on **anchor-column** data (which column each note's anchor stands in),
which this pass deliberately did not re-derive. Related: the pp. 244/245 "exact mirrors"
claim and the p. 247 "boundary inside the right block" claim rest on the same data.

**Nothing here contradicts them.** They are recorded as *unverified by this pass* rather
than confirmed, so that a later reader does not mistake this log's silence for endorsement —
and because the `p5-c6`/`p5-c7` failure CLAUDE.md documents is precisely a scoped per-note
hand-off being right while the narrative summary beside it was wrong. The ownership
arithmetic that *does* matter for boundary integrity — capitulum ownership, contiguity,
totals — is re-derived above and is clean on all twelve pages. **Do not repair anything in
this pass.**

---

## Disposition

**PASS 3 CLEAN for Pars IV. Zero defects, zero repairs, no chunk edited, `KNOWN_TOTALS`
unchanged, no git write command run.** One documentation flag (`[?]` DOC-2) raised against
three `KNOWN_TOTALS` generalisations; the bodies, boundaries and registers are verified
complete.

**Certified to the Pars III agent, from this side of the p. 241 seam:**

1. p. 241's register totals **10**, re-derived on the bands; the left block carries nn. 1–5
   closing complete (plus the printer's signature `S. Bonav. — Tom. V.`, which is not an
   entry), the right block opens **numbered at n. 6**, so **p. 241 has no gutter runover**,
   and n. 10 ends complete on the page — **nothing is forwarded into p. 242**.
2. The register divides **`p3-c11` nn. 1–2 · `p4-c1` nn. 3–10**, by PARS and not by block.
   n. 2 is the `I Tim. 1, 17` doxology note on Cap. XI's closing clause; n. 3 is Cap. I's
   first note. Pars IV claims **no note on p. 240** and none above it.
3. `p3-c11`'s body ends at `…omnis honor et gloria in saecula saeculorum. Amen.`
   (raw L45024–45033), the last body text before the `PARS QUARTA.` display heading at
   raw L45036. The boundary is set from that heading, never from the `Amen.`
4. **p. 241's gutter is 1228, not the tool's default 1218.** The default sits on a 39 px run
   and is a quiet failure; the heavily-inked centre rule (island 1225–1232, peak ink 1088)
   is what truncates the run. Anyone re-cropping p. 241 must re-profile, not accept the
   default.

**Certified to the Pars V agent, from this side of the p. 252 seam:**

1. p. 252's register totals **6**, blocks 3/3. The left block opens **numbered at n. 1**
   (`Epist. I. Cor. 12, 8-11.`), so **nothing is forwarded from p. 251 into p. 252**; the
   right block's last entry, n. 6 (`I M beatificativae.`), **ends complete on p. 252** with
   a large blank beneath, so **nothing is forwarded into p. 253** either.
2. The register divides **`p4-c10` n. 1 only · `p5-c1` nn. 2–6**, by PARS. n. 1 anchors on
   `prout vult` in Cap. X; n. 2 (`Iac. 1, 17.`) anchors in Pars V Cap. I. Pars IV claims
   **no note on p. 253** and none below p. 252 n. 1. `p5-c1`'s incoming hand-off is
   therefore exactly `p.252 nn. 2–6` — and per CLAUDE.md that is a claim to re-derive, not
   a fact to adopt.
3. `p4-c10`'s body runs across the top of both columns of p. 252 and ends at
   `…secundum suam liberalissimam providentiam et providentissimam largitatem.`
   (raw L46689–46697), immediately above the `PARS QUINTA` display heading at raw L46700.
   **Note the raw prints it `PARS aUINTA.` — a `QUINTA` grep of the raw returns nothing at
   all**, which is a trap worth knowing before concluding the heading is absent.
4. **p. 252 opens a pars, so its gutter measurement fails on any window touching the
   `PARS QUINTA` display heading**: three upper windows returned 1245–1288 on **284–332 px**
   runs, and a fourth returned the right value on a useless 27 px run. Profile the body rows
   only; nine of them agree at 1399–1404, and the ink profile (blank 1376–1430, island
   1399–1405) gives **1403**. Reject any run far outside ~58–64 px.
