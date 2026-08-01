# Vol V work-close gate — PASS 3 (cross-chunk boundary integrity), Pars V

**Scope:** `bon-brev-p5-c1` … `bon-brev-p5-c10` — 10 chunks, printed pp. 252–264
(pdf 328–340; offset `pdf = printed + 76`). Plus the **incoming** seam
`p4-c10 → p5-c1` (p. 252, **shared**, and the leaf on which `PARS QUINTA` opens)
and the **outgoing** seam `p5-c10 → p6-c1` (**leaf crossing** p. 264 → p. 265,
where `PARS SEXTA` opens at the HEAD of the leaf — the only pars in the work that
does). A Pars IV agent ran concurrently on the p. 252 side; the seam is certified
here **from the Pars V side, independently derived** — the double derivation is
deliberate.

Run 2026-08-01, as pass 3 of the Breviloquium work-close gate (CLAUDE.md
§ "Polish-gate cadence for Vols V–X", trigger 2 — work boundary, unconditional);
the pass-3 definition is CLAUDE.md § "Polish-blocker cadence" step 3. Companion
logs: `vol5-workclose-gate-pass3-prol-p1.md`, `-p2.md`, `-p3.md`.
**Nothing was edited; no `KNOWN_TOTALS` entry changed; no git write command run.**

Derived counts (not carried, derived at the moment of citing): **10 chunks, 98
apparatus entries** in scope (`re` walk of the ten `## Apparatus` sections).
That figure is **exactly** the sum of Pars V's share of the thirteen printed
pages' registers as read off the bands below —
5 (p. 252 nn. 2–6) + 9 + 6 + 10 + 6 + 9 + 7 + 9 + 7 + 9 + 7 + 8 + 6 = **98** —
so Pars V owns pp. 253–264 entire plus five of p. 252's six, and no note in the
range belongs to a chunk outside it. This **re-derives** the recorded "Pars V
closed with 98 entries" rather than quoting it.

Corpus-wide at the same moment, `check-vol5-apparatus.py` reports **79 chunks,
681 apparatus entries — All checks passed**; `check-vol5-census.py` reports
**79 on disk / 79 in ledger, rosters agree**, with **59 runovers across 79 chunks
(54 gutter-crossing, 5 page-crossing; 48 chunks positive, 31 negative)**. The
five page-crossers are pp. 206, 212, 246, **253**, 277 — **exactly one falls in
this scope, p. 253 n. 9**, and it is re-derived from the bands below.

---

## Method actually used

1. **Gutters re-measured fresh on every page, no constant, no parity prediction.**
   `colcrop.py`'s **own** `measure_gutter` profile function (lifted verbatim from
   the tool's source and called directly — no measuring script was hand-rolled),
   driven over **twelve** independent row windows per page: 45–92 %, 30–70 %,
   50–80 %, 35–60 %, 60–90 %, 47–60 %, 55–85 %, 40–75 %, 65–92 %, 32–52 %,
   70–90 %, 45–65 %. The function's low-ink run **already merges the two zero-ink
   runs either side of Quaracchi's printed centre rule** — `xs[0]`…`xs[-1]` spans
   the island — so the reported width *is* the merged band and its midpoint is the
   merged-band midpoint. Windows whose run fell outside a sound **50–78 px** were
   discarded. **The per-column ink profile (blank band, rule island, island peak)
   was printed for every one of the fifteen pages, including the pages where every
   window agreed** — that is how one learns *why* they agreed, and it costs
   nothing (CLAUDE.md gutter rule 5, last line).
   ⚠ This scope is where gutter rule 5 was identified, and the obstruction behaved
   exactly as it records: **the printed centre rule stands inside the blank band on
   all fifteen leaves. Its absence would have been the thing worth remarking; it
   was never absent.**
2. **Body continuity established POSITIVELY from the next heading**, never from
   white space (CLAUDE.md's `p2-c4` rule). The raw djvu
   (`raw/doctorisseraphic05bona_djvu.txt`) was walked to each receiving unit's
   heading and the ~12 lines immediately preceding it compared word-for-word
   against the prior chunk's Latin tail. **All twelve receiving headings were
   found in the raw** — none had to be read off the band, though six are garbled
   (`PARS aUINTA.` for PARS QUINTA, `C.\p. IV.`, `C.\p. VII.`, `Cai>. Vlll.`,
   `Cap. I.\.` for Cap. IX, `Cai'. .\.` for Cap. X). Raw line map:
   `PARS aUINTA` L46700 · Cap. I L46705 · II L46860 · III L47039 · IV L47257 ·
   V L47440 · VI L47624 · VII L47918 · VIII L48112 · IX L48249 · X L48412 ·
   `PARS SEXTA` L48612 (Pars VI Cap. I L48618).
   **Two headings were additionally confirmed directly on the band** because the
   seam mattered: `CAP. II.` at the head of p. 253's L-2 band, standing one line
   below `…num complementum ⁴`; and the full-width `PARS SEXTA. / De medicina
   sacramentali.` at the head of p. 265.
   **No boundary anywhere in this pass was set or corroborated from a running
   head.**
3. **Every printed page's footers read off the 450 dpi bands** (bands-only rule —
   the Vol V raw has no footnote numerals). For each of **pp. 252–264** both the
   **left** and the **right** footer blocks were read in full at `n=3, scale 1.8`,
   using that page's freshly measured split: the last numbered entry of the right
   block and its number, whether the right block opens numbered or with an
   unnumbered continuation, whether the left block opens numbered, the block split
   point, and the column position of every anchor visible in the same band.
   **p. 265's left block was read as well**, to close the outgoing leaf crossing
   from both sides. **Anchors, only anchors** — block structure, column structure
   and capitulum structure were kept as three independent things throughout, and
   on p. 252 a fourth (reading-order) structure had to be added. The raw was used
   for body prose only; its p. 264 footer block was counted once, as an
   independent cross-check, and never relied on.
4. Watched for the two named failure families — the **cascade-merge splice** (a
   tail that does not parse) and the **chunk written short at a column foot**.

---

## Gutters measured

Adopted value = merged-band midpoint, cross-checked against the consensus of the
surviving windows. "Chunk used" is the split recorded in that page's chunk
`## Notes` / `transcription_status`, **re-derived here rather than adopted**.

| p. | adopted | sound windows / 12 (spread) | runs (px) | blank band → midpoint | rule island (peak rows @ x) | chunk used | Δ |
|---|---|---|---|---|---|---|---|
| 251 | **1160** | 12 (1159–1161, 2 px) | 61–64 | 1130–1190 → 1160 | 1157–1163 (943 @ 1160) | 1160 | 0 |
| 252 | **1403** | 9 (1399–1405, 6 px) | 54–59 | 1376–1430 → 1403 | 1399–1405 (428 @ 1404) | 1403 | 0 |
| 253 | **1250** | 11 (1244–1253, 9 px) | 57–66 | 1221–1280 → 1250 | 1246–1274 (159 @ 1250) | 1250 | 0 |
| 254 | **1356** | 10 (1349–1359, 10 px) | 51–61 | 1332–1382 → 1357 | 1333–1363 (311 @ 1361) | 1357 | 1 |
| 255 | **1206** | 12 (1203–1214, 11 px) | 52–62 | 1181–1232 → 1206 | 1199–1216 (287 @ 1204) | 1200/1204 | 2–6 |
| 256 | **1355** | 11 (1350–1356, 6 px) | 54–62 | 1329–1382 → 1355 | 1335–1358 (787 @ 1351) | 1355 | 0 |
| 257 | **1202** | 9 (1193–1210, 17 px) | 52–61 | 1176–1228 → 1202 | 1193–1208 (245 @ 1197) | 1197/1202 | 0–5 |
| 258 | **1412** | 8 (1406–1416, 10 px) | 52–62 | 1390–1441 → 1415 | 1408–1417 (496 @ 1412) | 1412 | 0 |
| 259 | **1142** | 10 (1130–1145, 15 px) | 50–60 | 1118–1168 → 1143 | 1136–1151 (383 @ 1141) | ~1141 | ≤2 |
| 260 | **1397** | **3** (1396–1397, 1 px) | 61–62 | 1367–1427 → 1397 | 1397–1402 (431 @ 1398) | 1398 | 1 |
| 261 | **1232** | 11 (1231–1232, 1 px) | 61–64 | 1201–1263 → 1232 | 1218–1247 (614 @ 1232) | 1232 | 0 |
| 262 | **1321** | 12 (1320–1322, 2 px) | 61–63 | 1291–1351 → 1321 | 1305–1324 (732 @ 1321) | 1321 | 0 |
| 263 | **1195** | 11 (1191–1198, 7 px) | 55–61 | 1168–1223 → 1195 | 1171–1220 (886 @ 1195) | 1195 | 0 |
| 264 | **1366** | **5** (1364–1367, 3 px) | 53–63 | 1341–1393 → 1367 | 1345–1378 (241 @ 1365) | 1365 | 1 |
| 265 | **1151** | 5 (1148–1154, 6 px) | 54–61 | 1125–1178 → 1151 | 1146–1159 (539 @ 1151) | 1151 | 0 |

**Maximum divergence between this pass's measurement and the split each chunk was
actually built on is 6 px** (p. 255), against a column width of ~1150 px. **No
chunk in Pars V can have been built on a truncated or padded column.**

### Measurements REJECTED, and why

- **p. 260 — `colcrop.py`'s bare default REJECTED, and this is the page the rule
  was written from.** The 45–92 % body window returns **1386 on a 20 px run**, and
  *five* further lower windows (50–80 %, 60–90 %, 55–85 %, 40–75 %, 65–92 %) return
  the identical 1386 on the identical 20 px run — six agreeing windows, all wrong,
  and none of them tripping the tool's own 15 px warning. Three upper windows
  (30–70 %, 35–60 %, 32–52 %) agree at **1396–1397 on 61–62 px runs**, and the
  30–70 % ink profile gives blank band x = 1367–1427 with a heavily inked rule at
  x = 1397–1402 peaking 431 rows on x = 1398 → **midpoint 1397**. Adopted 1397.
  This re-derives, from scratch and without consulting it, the value CLAUDE.md
  records (`default 1386 on a 20 px run, rejected; true 1398, found by forking the
  windows against a 60 px run`), to **1 px**. The narrow run is *positively
  diagnostic*: the rule printed heavily on this leaf and truncated the zero-ink run
  outright. **Six windows agreeing is not evidence; run width is.**
- **p. 263 — one window discarded, and it is the documented one.** The 47–60 %
  window returns **1349 on a 375 px run** against a true 1195 — a 154 px error.
  `Cap. X.` opens ~55 % down p. 263's right column, squarely inside that window,
  floods one side and drags the apparent centre. Eleven windows survive at
  1191–1198 on 55–61 px runs; profile band 1168–1223 → **1195**. Re-derived
  independently of CLAUDE.md's note, which it confirms exactly.
- **p. 252 — three windows discarded (the part-opening leaf).** 47–60 % → 1288 on
  a **284 px** run; 32–52 % → 1299 on a **439 px** run; 70–90 % → 1285 on a
  **296 px** run. All three straddle the full-width `PARS QUINTA` display heading,
  which crosses the gutter and destroys the blank-column run. Nine body windows
  agree at **1399–1405 on 54–59 px runs**; profile band 1376–1430 with the rule at
  1399–1405 → **1403**. Adopted 1403 — **the widest gutter in the volume, and one
  of the two measurements that killed the parity model, here re-derived rather than
  adopted.**
- **p. 251 — nothing rejected, and this is the point.** All **twelve** windows
  return 1159–1161 on 61–64 px runs; profile band 1130–1190 with a perfectly
  centred rule at 1157–1163 peaking 943 rows on x = 1160 → **1160**. The narrowest
  gutter in the volume is also the most confident measurement in this pass. Its
  companion outlier p. 252 at 1403 sits on the facing leaf. **Two adjacent leaves,
  243 px apart, both sound: parity reasoning is not merely retired, it is refuted
  on this pair.**
- **p. 264 — the bare default is *near* right but its run is not sound, and seven
  windows blow out.** Default 1367 on a **53 px** run. The 50–80 %, 47–60 %,
  60–90 %, 40–75 %, 65–92 %, 70–90 % and 45–65 % windows return 1253–1342 on runs
  of **216–434 px** — because **both body columns END at ~66 % of page height**
  (Pars V closes here), so those windows profile blank paper below the text and the
  "gutter" they find is the whole white lower page. Five upper windows agree at
  1364–1367 on 53–63 px runs; profile band 1341–1393, island 1345–1378 peaking
  241 rows on x = 1365 → adopted **1366**. **This is a failure mode the CLAUDE.md
  rules do not yet name: not a heading crossing the gutter, but a column that
  simply stops. Expect it at every work and part CLOSING, as rule 2 predicts it at
  every opening.**
- **p. 265 — the bare default is a LOUD failure.** 45–92 %, 50–80 %, 60–90 %,
  55–85 % and 65–92 % all return **1121 on a 4 px run** (and 70–90 % returns 1117
  on 12 px) — five agreeing windows under the tool's own warning threshold. Five
  upper windows agree at 1148–1154 on 54–61 px; profile band 1125–1178, rule
  1146–1159 peaking 539 rows on x = 1151 → **1151**. Confirms `p6-c1`'s record.
- **p. 259 (47–60 %, 374 px), p. 254 (47–60 % 174 px, 70–90 % 295 px), p. 256
  (47–60 %, 293 px), p. 261 (32–52 %, 334 px), p. 253 (47–60 %, 195 px)** —
  discarded on blown-out runs. **In total 23 of the 180 windows in this scope were
  discarded, 20 of them for runs FAR ABOVE the sound band (174–439 px) and 3 for
  runs far below (4–20 px). A run of 375 px is the same species of nonsense as a
  run of 20 px.**
- **pp. 257, 259 — narrow but sound, not rejected.** Several windows on each fall
  to 50–53 px. Nine and ten windows respectively survive, spreads are 17 and 15 px,
  and in both the merged-band midpoint sits within 1–2 px of the rule island's own
  centre. The narrowness is the rule inking, not a narrow gutter.

No parity reasoning was used anywhere.

---

## Boundary table

**Eleven boundaries in scope: TEN mid-page, ONE leaf crossing.** Pars V is the
most seam-dense pars of the Breviloquium and the one with the fewest leaf
crossings — every capitulum but the last begins on the same leaf its predecessor
ends on. `seam-screen.py --volume 5` sees only the mid-page class (it reports
**71 mid-page boundaries corpus-wide, 0 tail-not-terminal suspects**, of which
**ten fall in this range** — pp. 252, 253, 254, 256, 257, 258, 260, 261, 262,
263); the single leaf crossing is outside its denominator, which is why it is
swept by hand here.

| # | Prior → Receiving | Shared page / crossing | Body continuity — evidence | Footer split (page total) | Verdict |
|---|---|---|---|---|---|
| 1 | `p4-c10` → `p5-c1` | p. 252 (mid-page) — **the Pars IV/V seam** | p4-c10 tail `…dividens singulis, prout vult[^p252-1], secundum suam liberalissimam providentiam et providentissimam largitatem.` = raw L46695–46697, the last lines of Cap. X; `PARS aUINTA.` at L46700 with only blank lines between, then `De gratia Spiritus sancti.` L46702 and `Cap. I.` L46705. Confirmed on the band: Cap. X's tail runs across the TOP of the left column (9 lines, ending `…diversorum mem-`) and then the TOP of the right column (10 lines, ending `…largitatem.`), and the full-width display heading stands **below both**. `Amen`-less, and not accepted on its own — the display heading fixes it | **1 / 5 (6).** See the dedicated section below | **CLEAN** |
| 2 | `p5-c1` → `p5-c2` | p. 253 (mid-page, **left** col.) | c1 tail `…in quo ad modum circuli intelligibilis consistit omnium spirituum rationalium complementum[^p253-4].` = raw L46857–46858, immediately above `Cap. II.` (L46860) + `De gratia, in quantum iuvat ad bonum meritorium.` (L46862). **Also confirmed directly on the band**: `num complementum ⁴` is the line above `CAP. II.` at the head of p. 253's L-2 band | 4 / 5 (9). Blocks **6/3** (left nn. 1–6, n. 6 `B C E I M T meritum.` complete; right opens **numbered** ⁷ → gutter NEGATIVE), anchors 4/5 — the block line stands **two notes below** the anchor line, and the capitulum line coincides with the ANCHOR line. n. 9 **breaks off mid-word at the page foot** (`Gen. 15, 1: Ego [Deus] pro-`) → p. 253 → p. 254 POSITIVE page-crossing runover | **CLEAN** |
| 3 | `p5-c2` → `p5-c3` | p. 254 (mid-page, **right** col.) | c2 tail `…gloriam aeternam merito non tantum *congrui*, sed etiam *condigni* mereri facit gratia septiformis.` = raw L47035–47037, immediately above `Cap. III.` (L47039) | 4 / 2 (6). Left block opens **UNNUMBERED** with p. 253 n. 9's tail (`tector tuus sum et merces tua magna nimis. — Mox pro *et propria* 1 *ex propria*…`) — **closing p. 253 → p. 254 POSITIVE, the halves meeting exactly where Gen. 15, 1 requires, at `pro-` / `tector`** (logged once on `p5-c2`'s ledger line; **not re-logged here**) — then nn. 1–3, n. 3 breaking inside an editorial lemma on `…cum pluribus codd. *condigni*`; right block opens **UNNUMBERED** with `pro *digni*; subinde pro…` → p. 254 gutter runover POSITIVE. n. 6 closes complete | **CLEAN** |
| 4 | `p5-c3` → `p5-c4` | p. 256 (mid-page, **left** col., two lines down) | c3 tail `…exercendo nos in operibus perfectae virtutis secundum donum ipsius gratiae septiformis.` = raw L47254–47255, immediately above `C.\p. IV.` (L47257). ⚠ The raw interleaves p. 257's folio (`236`, a 5→3 misread) and running head at L47248–47251 **between** the footer of p. 256 and this tail — the boundary was set from the `C.\p. IV.` heading, never from the head | 6 / 0 (6). p. 256's register is **undivided and entirely Cap. IV's**: Cap. III's two surviving lines at the head of the left column carry **no anchor** — verified negatively on the band. Blocks 4/2 (left n. 4 `Cfr. III. Sent. d. 34. p. I. a. 1. q. 1.` complete; right opens **numbered** ⁵ → NEGATIVE); anchors 3/3, so the left block over-runs the column division by one | **CLEAN** |
| 5 | `p5-c4` → `p5-c5` | p. 257 (mid-page, **left** col.) | c4 tail `…et una nihilominus gratia sufficit ad informationem et gratificationem habituum diversorum[^p257-1].` = raw L47436–47438, immediately above `Cap. V.` (L47440) | 1 / 8 (9). Blocks 5/4, anchors 3/6, capitulum line between nn. 1 and 2 — **three lines, three positions**. Left block ends complete at n. 5 (`Phil. 2, 15. Cfr. III. Sent. lit. Magistri, d. XXXV. c. 1.`) followed by the printer's signature **`S. Bonav. — Tom. V.`**; right opens **numbered** ⁶ → NEGATIVE; n. 9 (`Edd. *expediendam*.`) closes complete, with the quire signature **`33`** below it. **Neither signature is an entry: the register is NINE, and a reader counting block lines would reach ten** | **CLEAN** |
| 6 | `p5-c5` → `p5-c6` | p. 258 (mid-page, **top of right** col.) | c5 tail `…quia lux cognitionis vehementer expedit *ad dirigendos pedes in viam rectam*[^p258-4].` = raw L47620–47621, immediately above `Cap. VI.` (L47624) | 4 / 3 (7). Blocks **2/5** against anchors **4/3** — the block break stands **two notes above** the anchor break, because n. 2 is a single entry (Origen + Hugh of St Victor + Gregory) filling most of the left block. **Block extent is a function of entry LENGTH, not anchor count.** The capitulum line coincides with the ANCHOR line. Left block ends complete (`…cubico pro cubito (contra Vulgatam).`); right opens **numbered** ³ → NEGATIVE | **CLEAN** |
| 7 | `p5-c6` → `p5-c7` | p. 260 (mid-page, **left** col.) | c6 tail `…nemini datur, nisi ei qui se exercet ad illam; ideo deinceps consideranda sunt exercitia meritorum.` = raw L47913–47916, immediately above `C.\p. VII.` (L47918) | **4 / 3 (7).** See the dedicated section below | **CLEAN** |
| 8 | `p5-c7` → `p5-c8` | p. 261 (mid-page, **right** col.) | c7 tail `…qui duodecim lapides de Iordanis alveo extraxerunt ad altare dominicum construendum[^p261-5].` = raw L48108–48110, immediately above `Cai>. Vlll.` (L48112) | 5 / 4 (9). Blocks 5/4, anchors 4/5, capitulum line between nn. 5 and 6 — **three lines, three positions, the exact mirror of p. 260**: there the capitulum line sits ON the anchor break, here ON the block break. The dissenting note is n. 5, whose anchor is on Cap. VII's LAST line in the RIGHT column while its entry prints in the LEFT block — and it does **not** run over: left block ends complete at n. 5 (`…substituit *aedificatione*.`), right opens **numbered** ⁶ → NEGATIVE. n. 9 closes complete (`…excepta 2, *quatuor tanquam*.`) | **CLEAN** |
| 9 | `p5-c8` → `p5-c9` | p. 262 (mid-page, **foot of left / head of right** col.) | c8 tail `…eruntque omnia per amorem communia communione ordinata et ordinatione connexa et connexione indissolubiliter alligata.` = raw L48244–48246, immediately above `Cap. I.\.` (= Cap. IX, L48249) + `De exercitio gratiae respectu agendorum, praeceptorum et consiliorum.` (L48251). **Confirmed on the band**: that sentence is the last line of p. 262's LEFT column, and the `Cap. IX` heading stands at the very TOP of the right column | 3 / 4 (7). Blocks 3/4, anchors 3/4 (n. 3's anchor `iuxta quod Dominus orat³` visibly LEFT; n. 4 `Exod. 31, 18.` anchored on `digito Dei` in Cap. IX, RIGHT), capitulum line between nn. 3 and 4 — **ALL THREE LINES COINCIDE**, with no dissenting note on the leaf. Left ends complete (`…perperam *Quae universitas*.`), right opens **numbered** ⁴ → NEGATIVE | **CLEAN** |
| 10 | `p5-c9` → `p5-c10` | p. 263 (mid-page, **right** col., ~55 % down) | c9 tail `…ac per hoc non solum iustitiam continent *sufficientem*, verum etiam *abundantem*[^p263-6], secundum quod competit perfectioni evangelicae legis et exercitationi gratiae perficientis.` = raw L48405–48410, immediately above `Cai'. .\.` (= Cap. X, L48412) | 6 / 2 (8). Blocks 4/4 and anchors 4/4 **coincide**, but the CAPITULUM line falls between nn. 6 and 7 — two notes below both, because Cap. X opens INSIDE the right column. The split falls **inside n. 4**, broken **mid-word** at `…nocumenta E P T W *damna*. Sub-` / `inde pro *ad iustitiae necessitatem*…` → p. 263 gutter runover POSITIVE (logged on `p5-c10`'s line, not re-logged here). n. 8 (`Iac. 1, 17. — Inferius non pauci codd. omittunt *miseriam*.`) closes complete | **CLEAN** |
| 11 | `p5-c10` → `p6-c1` | **leaf crossing** p. 264 → p. 265 | c10 tail `…adiuvante nihilominus septiformi medicina Sacramentorum divinitus ad reparationem humani generis statutorum.` = raw L48575–48582, followed by p. 264's six-entry footer register (L48585–48603), the running head `PARS VI. c. r.` (L48606), the folio `26S` (= 265, L48609), and then `PARS SEXTA.` (L48612). **The white space filling the lower third of p. 264 was NOT used as evidence.** See the dedicated section below | 6 / 0 (6). Nothing forwarded | **CLEAN** |

**11 boundaries swept (10 mid-page, 1 leaf crossing). 11 CLEAN, 0 DEFECT.**

**No tail in the range fails to parse** — every one of the eleven is a
grammatically complete sentence, and `seam-screen.py` independently reports 0
tail-not-terminal suspects corpus-wide. No cascade-merge signature anywhere.
**No chunk was written short at a column foot**: every unit's end was fixed from
the NEXT heading, and the two leaves where blank paper most invites the `p2-c4`
error — p. 257 (left column ending high under a five-note block plus the
printer's signature) and p. 264 (both columns stopping at ~66 % of page height,
the whole lower third blank) — were resolved from the heading, positively, in
both cases correctly.

---

## Footer accounting — every page re-read off the bands

| p. | left block | right block | plate's last numbered entry (band) | `KNOWN_TOTALS` | agree? | ownership (by anchor) |
|---|---|---|---|---|---|---|
| 252 | nn. 1–3 | nn. 4–6 | 6 (`I M *beatificativae*.`) | 6 | ✅ | `p4-c10` 1 · `p5-c1` 2–6 |
| 253 | nn. 1–6 | nn. 7–9 | 9 (`Psalm. 15, 2: Dixi Domino… — Gen. 15, 1: Ego [Deus] pro-`) **breaks off** | 9 | ✅ | `c1` 1–4 · `c2` 5–9 |
| 254 | n. 9-cont. + nn. 1–3 (n. 3 broken) | n. 3 cont. + nn. 4–6 | 6 (`De his quatuor requisitis vide IV. Sent. d. 17. p. I. per totam.`) | 6 | ✅ | `c2` 1–4 · `c3` 5–6 |
| 255 | nn. 1–8 (n. 8 broken at a full stop) | n. 8 cont. + nn. 9–10 | 10 (`…Superius voci *voluntatem* ex G I K M O Q praefiximus *Dei*.`) | 10 | ✅ | all `c3` |
| 256 | nn. 1–4 | nn. 5–6 | 6 (`Ab August., II. de Gen. contra Manich. c. 10. n. 14…`) | 6 | ✅ | all `c4` |
| 257 | nn. 1–5 + printer's signature | nn. 6–9 + quire signature `33` | 9 (`Edd. *expediendam*.`) | 9 | ✅ | `c4` 1 · `c5` 2–9 |
| 258 | nn. 1–2 | nn. 3–7 | 7 (`Psalm. 24, 10. … cfr. Magister II. Sent. d. XXX. c. 7.`) | 7 | ✅ | `c5` 1–4 · `c6` 5–7 |
| 259 | nn. 1–5 (n. 5 broken at `G substituit *quam* pro`) | n. 5 cont. + nn. 6–9 | 9 (`Gal. 5, 22. seq.`) | 9 | ✅ | all `c6` |
| 260 | nn. 1–3 (n. 3 broken at `…ubi in textu verba`) | n. 3 cont. + nn. 4–7 | 7 (`…Inferius pro *improbandae* O Q *improbitate* (plures codd. *improbatae*).`) | 7 | ✅ | `c6` 1–3 · `c7` 4–7 |
| 261 | nn. 1–5 | nn. 6–9 | 9 (`Cfr. III. Sent. d. 27. a. 1. q. 1-3. et dub. 1. — …*quatuor tanquam*.`) | 9 | ✅ | `c7` 1–5 · `c8` 6–9 |
| 262 | nn. 1–3 | nn. 4–7 | 7 (`Respicitur Rom. 8, 15. et Gal. 4, 24. seqq. — Inferius pro *documentorum* E *mandatorum*.`) | 7 | ✅ | `c8` 1–3 · `c9` 4–7 |
| 263 | nn. 1–4 (n. 4 broken **mid-word** at `Sub-`) | n. 4 cont. + nn. 5–8 | 8 (`Iac. 1, 17. — Inferius non pauci codd. omittunt *miseriam*.`) | 8 | ✅ | `c9` 1–6 · `c10` 7–8 |
| 264 | nn. 1–3 | nn. 4–6 | 6 (`Psalm. 118, 164.`) | 6 | ✅ | all `c10` |

**No page's true total differed from `KNOWN_TOTALS`. No register was dropped,
none double-claimed, and no page in scope is unowned** — an independent walk of
every `[^pNNN-N]:` definition across all 79 vol5 chunks returns, for pp. 252–264,
an unbroken 1..N on every page with the ownership split shown above, exactly
matching the bands. The raw's own p. 264 footer block, counted independently as
a cross-check, also gives **six** — but the bands are the authority and the raw
was not relied on.

**Runover ledger, re-derived from the bands rather than adopted.**
Positive **gutter** runovers in scope: **p. 254 n. 3, p. 255 n. 8, p. 259 n. 5,
p. 260 n. 3, p. 263 n. 4** — five. Positive **page-crossing** runovers: **p. 253
n. 9** — one, and the only one of the corpus's five that falls in this scope.
Negative and confirmed negative on the band (right block opens numbered):
**pp. 252, 253, 256, 257, 258, 261, 262, 264**. Negative page-crossing tests,
each closed from **both** sides: p. 252 → 253, p. 254 → 255, p. 255 → 256,
p. 256 → 257, p. 257 → 258, p. 258 → 259, p. 259 → 260, p. 260 → 261,
p. 261 → 262, p. 262 → 263, p. 263 → 264, **p. 264 → 265**. Each positive is
logged exactly once on its own chunk's ledger line; **no double-count, and no
runover a prior chunk already logged is re-logged here.**

**Digit and siglum reads worth recording** (both confusion classes are live on
these leaves, and neither dominates — CLAUDE.md's warning holds):
- **p. 264 n. 1 — the `1`/`4` class, twice in one line.** The plate prints
  `Cfr. IV. Sent. d. 15. p. II. a. 2. q. 3. … ibid. d. 45. a. 3. q. 1. seqq.`
  where the raw gives `d. 1-5` and `il. i.5`. The chunk carries **both** correct.
  The two numerals `15` and `45` stand nine words apart in the same entry — the
  same "a true 1 and a true 4 touching" configuration CLAUDE.md names as the
  disambiguator.
- **p. 253 n. 2 — `edd. 1, 3`, not `codd. 1, 3`.** The chunk was corrected
  mid-pars by `p5-c3` on stroke count; **the band confirms `edd.`**, and both the
  Latin and the English (`editions 1 and 3 add *beatitudinis*`) now render it so.
  The correction held and is right.
- **Siglum runs read on the bands, all in alphabetical order and all with `H` as
  two uprights**: `E H I K M S` (p. 255 n. 9), `G I K M O Q` (p. 255 n. 10),
  `I K L M O V` (p. 258 n. 2), `C H K` (p. 259 n. 3), `G H` (p. 259 n. 4),
  `I K L M O P` (p. 259 n. 5-cont.), `C K L M O P T` (p. 260 n. 3-cont.),
  `G I K O` (p. 262 n. 6), `E P T W` (p. 263 n. 4), `D F G M U` (p. 264 n. 3),
  `A B C H` and `I K L O U` (p. 265 n. 2). **No single bare upright was read as
  `H` anywhere.**
- **p. 261's two truncated line-ends confirmed independently.** The foot of
  p. 261's right column prints `quae per illud idonea su` and `Quoniam igitur
  nobiscum ad beatitudin` — final letters lost on the plate, not in the raw and
  not in the transcription. `p5-c8`'s `## Notes` records this; **it was
  re-derived here from the band, not adopted**, and it is right.

**No transcription change follows from any of these** — the chunks already carry
the correct readings, which is what this pass was checking.

---

## The p. 252 seam into Pars V — read with particular care

p. 252 is shared between `bon-brev-p4-c10` (Pars IV, Cap. X) and
`bon-brev-p5-c1` (Pars V, Cap. I), and it is the most structurally awkward leaf
in the Breviloquium so far, because **the full-width `PARS QUINTA` display
heading divides the page horizontally, so the leaf has FOUR reading regions, not
two columns.** The band gives the order unambiguously:

1. **L-upper** — Cap. X's tail, 9 lines, `…ascendendo in caelum, sic in mittendo
   Spiritum sanctum…` down to `…et quia diversa membra debent esse in corpore
   perfecto et diversorum mem-`;
2. **R-upper** — Cap. X's tail continues, 10 lines, `-brorum diversa officia…`
   down to `…dividens singulis, **prout vult¹**, secundum suam liberalissimam
   providentiam et providentissimam largitatem.`;
3. the **full-width** `PARS QUINTA. / De gratia Spiritus sancti.` heading;
4. **L-lower** — `Cap. I. / De gratia, in quantum est donum divinitus datum.` and
   Cap. I's opening, down to `…acceptabilem facit; propter`;
5. **R-lower** — Cap. I continues, `quod donum huiusmodi…` to `…sic immediate
   manet ab ipso Dei *similitudo*, quae`.

**Register 6, dividing 1 / 5 by pars — the most lopsided division in the work.**
Blocks **3 / 3** (left nn. 1–3, right nn. 4–6). Anchors, read on the bands:

| n. | anchor | region |
|---|---|---|
| 1 | `dividens singulis, prout vult¹` | **R-upper** (Cap. X — Pars IV) |
| 2 | `quod descendit a Patre luminum²` | L-lower |
| 3 | `quod animam purgat, illuminat et perficit³` | L-lower |
| 4 | `gratia gratum faciens recte dicitur et debuit appellari⁴` | R-lower |
| 5 | `capacem beatitudinis aeternae⁵` | R-lower |
| 6 | `conformem beatissimae⁶ Trinitati` | R-lower |

**So n. 1's anchor stands in the RIGHT column while its entry prints FIRST in the
LEFT footer block.** This is not an over-run: the footer register follows
**reading order**, and in reading order n. 1 is first on the page. Below the
display heading the block line and the anchor line then coincide exactly
(nn. 2–3 left, nn. 4–6 right). **The consequence for this corpus is a general
one: on a leaf carrying a full-width display heading, "which column is the anchor
in" is not a well-formed question, and the anchor sequence is not monotone in x.
This is the fourth independent structure CLAUDE.md's "block, column, capitulum
are three independent things" rule does not yet name.** It affects no
transcription; it affects how the leaf must be described.

**What I certify about the p. 252 seam, from the Pars V side, independently:**

1. `p4-c10`'s tail is the last body of Pars IV and is contiguous with the
   `PARS aUINTA` display heading in the raw (L46697 → L46700), with nothing
   between but blank lines, and the band confirms the heading stands immediately
   below the two column-tops.
2. p. 252's register totals **6**, matching `KNOWN_TOTALS`, and divides **1
   (`p4-c10`) / 5 (`p5-c1`)** by anchor. All six entries were compared word for
   word against the two blocks.
3. **The p. 251 → p. 252 page-crossing test is NEGATIVE, closed from this side:**
   p. 252's left block opens **numbered** ¹ (`Epist. I. Cor. 12, 8-11. Vulgata
   hinc inde plura addit.`).
4. **p. 252's own gutter test is NEGATIVE:** the left block ends complete at n. 3
   (`Cfr. supra pag. 225, nota 6.`) and the right block opens **numbered** ⁴
   (`Cfr. II. Sent. d. 26. q. 1. seq. — A pluribus codd., ut B C I M, omittitur
   *dicitur et*.`).
5. **The p. 252 → p. 253 test is NEGATIVE:** p. 252's right block ends complete at
   n. 6 (`I M *beatificativae*.`) and p. 253's left block opens **numbered** ¹.
   `KNOWN_TOTALS` records that this test "is NOT run — p.253 is not imaged — and
   is forwarded to p5-c1". **It was run here, on both sides, and it closes
   negative.** Neither the printer's nor a quire signature falls on p. 252.
6. Gutter **1403**, re-derived from nine sound windows and the per-column ink
   profile, against three windows destroyed by the display heading.

---

## p. 260 — the 4/3-vs-3/4 question, settled from the plate

CLAUDE.md records that `p5-c6`'s per-note hand-off correctly placed p. 260 n. 4's
anchor in the LEFT column, while its own prose summary — and the comment it wrote
into `KNOWN_TOTALS` — claimed the anchors divided **3/4** and that "all three
lines coincide for the first time in Pars V". **The plate supports the 4/3
reading. The 3/4 reading is wrong, and the three lines do not coincide.**

Read directly on p. 260's L-2 band, the left column's last five lines are:

> …in *credendis*, cuiusmodi sunt articuli fidei; secundo, in *diligendis*,
> cuiusmodi sunt illa quae spectant ad ordinem diligendi; tertio, in
> *exsequendis*, cuiusmodi sunt praecepta legis divinae; quarto in *postulandis*,
> **cuiusmodi sunt petitiones orationis dominicae ⁴.**
> De *articulis* autem *fidei* haec tenenda sunt, quod licet per fidem
> astringamur credere plurima, …

**Anchor ⁴ is plainly in the LEFT column**, on `petitiones orationis dominicae`,
inside Cap. VII's opening paragraph and six lines below the `Cap. VII.` heading —
which itself stands about two-thirds down the same left column. Therefore:

- **anchors 4 / 3** — nn. 1–4 LEFT, nn. 5–7 RIGHT (nn. 5–7 on `fundamenta`,
  `universalis`, `obsequium Christi`, all in the right column);
- **blocks 3 / 4** — left block nn. 1–3, n. 3 breaking at `…ubi in textu verba`;
  right block opening **unnumbered** with `Dionysii de raptu in caliginem et
  excessum…` then nn. 4–7;
- **capitulum line between nn. 3 and 4** — n. 3's anchor (`in odorem unguentorum
  tuorum curremus³`) is Cap. VI's last paragraph, n. 4's is Cap. VII's first.

**Three lines, three positions.** And note the geometry the wrong summary
obscured: **n. 3's anchor is Cap. VI's, in the left column, but its entry runs
over the gutter and completes inside a right block that carries four of Cap.
VII's notes** — which is exactly why a careless reading of the *blocks* would
report 3/4 anchors. The `KNOWN_TOTALS` comment as it now stands is **correct**:
it was amended by `p5-c7` and it records the 4/3 division, the three distinct
lines, and the explicit withdrawal of the "all three coincide" claim. Nothing
needs changing.

**And the withdrawn claim's *substance* can now be placed, which `p5-c8`
declined to do because it had not re-derived pp. 252–259.** This pass has
re-derived every anchor split in Pars V from the bands, so the derivation is
available:

| p. | blocks | anchors | capitulum line | coincidence |
|---|---|---|---|---|
| 252 | 3/3 | 1 R-upper, 2–3 L, 4–6 R | pars line after n. 1 | none (4-region leaf) |
| 253 | 6/3 | 4/5 | after n. 4 | capitulum = anchor |
| 254 | 3/3 (inside n. 3) | 3/3 | after n. 4 | block = anchor |
| 255 | 8/2 | 6/4 | — (none on leaf) | — |
| 256 | 4/2 | 3/3 | at column head, no note | — |
| 257 | 5/4 | 3/6 | after n. 1 | none |
| 258 | 2/5 | 4/3 | after n. 4 | capitulum = anchor |
| 259 | 5/4 | 4/5 | — (none on leaf) | — |
| **260** | **3/4** | **4/3** | **after n. 3** | **none** |
| 261 | 5/4 | 4/5 | after n. 5 | capitulum = block |
| **262** | **3/4** | **3/4** | **after n. 3** | **ALL THREE** |
| 263 | 4/4 | 4/4 | after n. 6 | block = anchor |
| 264 | 3/3 | 2/4 | — (none on leaf) | — |

**The first leaf in Pars V on which all three lines coincide is p. 262, not
p. 260** — and the mechanism is the one `p5-c8` gave: on p. 262 the capitulum
boundary *is* the column boundary (Cap. VIII ends at the foot of the left column,
Cap. IX opens at the head of the right), so the three structures are measured
against one physical line. **This is offered as a derivation, not as a
`KNOWN_TOTALS` amendment; nothing was edited.** It is recorded here so that the
next agent who wants the fact has a derivation to check rather than a sentence to
quote.

---

## The p. 264 → p. 265 leaf edge — the only leaf crossing in Pars V

**Certified from both sides.**

1. **Pars V's last line.** p. 264's right column ends `…adiuvante nihilominus
   septiformi medicina Sacramentorum divinitus ad reparationem humani generis
   statutorum.` — read on the band, matching raw L48575–48582 word for word.
   **Both** of p. 264's columns stop at ~66 % of page height and the lower third
   of the leaf is blank. **That blank was not used as evidence** (CLAUDE.md's
   `p2-c4` rule); it did, however, wreck seven of the twelve gutter windows, which
   is how it made itself known.
2. **Pars VI's opening, fixed positively.** The full-width `PARS SEXTA. / De
   medicina sacramentali.` display heading stands at the **HEAD of p. 265**, below
   the running head and nothing else — read directly on p. 265's L-0 band. Below
   it, `Cap. I. / De Sacramentorum origine.` and the opening
   `Postquam actum est de Trinitate Dei, de creatura mundi, de corruptela peccati,
   de incarnatione Verbi et gratia Spiritus sancti; iam nunc sexto agendum est de
   medicina sacramentali.` — **the opener itself enumerates Partes I–V as
   completed**, which is independent internal confirmation that Pars V has ended
   and that nothing of it stands on p. 265. **This breaks the precedent of PARS
   QUARTA and PARS QUINTA, both of which opened part-way down a leaf; it is the
   only pars in the Breviloquium to open at a leaf edge.**
3. **Register.** p. 264's total is **6**, matching `KNOWN_TOTALS`, and **all six
   are `p5-c10`'s**. n. 6 (`Psalm. 118, 164.`) closes complete on the page.
   **Nothing is forwarded.**
4. **The page-crossing test is NEGATIVE, closed from both sides**: p. 264's right
   block ends complete at n. 6, and p. 265's left block opens **numbered** ¹
   (`Isidor., VI. Etymolog. c. 19. n. 40. Vide tom. III. pag. 895, nota 5. …`).
5. **The signatures stand on p. 265, not p. 264** — the printer's `S. Bonav. —
   Tom. V.` below p. 265's left block (read on the band). Neither is an entry and
   neither is counted. `KNOWN_TOTALS`'s note on this point is confirmed.
6. p. 265's register (6) is `p6-c1`'s entire and belongs to the Pars VI log; it
   was read here only far enough to close the crossing.

---

## Observations (no defect, no repair, nothing edited)

1. **Pars V is the pars with the fewest leaf crossings and the most mid-page
   seams** — 10 mid-page against 1 crossing, where Pars III ran 9 against 3. Every
   capitulum boundary in Pars V except the last falls inside a printed page. This
   is the shape CLAUDE.md predicts ("per-page footer splits are the NORM"), here
   in its most extreme instance in the work.
2. **`[?]` flags in scope: ZERO.** All ten chunks' `## Notes` record `No [?]
   flags`, and a grep for live inline `[?]` markers in `vol5/bon-brev-p5-*`
   returns none — the eleven hits are the "No `[?]` flags" sentences themselves
   plus three prose mentions of readings that *could* have carried one
   (`p5-c1` on `edd. 1, 3`, `p5-c8` on p. 261's truncated line-ends, `p5-c10` on
   p. 264 n. 1's `d. 15`/`d. 45`). **The recorded "Pars V closed with 98 entries
   and zero `[?]` flags" is re-derived and holds on both halves.**
3. **A gutter failure mode the rules do not yet name: a column that STOPS.**
   Rule 2 covers a full-width heading crossing the gutter at a work/part
   *opening*. p. 264 is the mirror — a part *closing*, where both body columns end
   at ~66 % of page height and every window reaching below that profiles blank
   paper, returning 216–434 px "runs". Seven of twelve windows failed this way on
   p. 264. **Expect it at every work and part closing in Vols V–X, and note that
   the failure is silent in the same way rule 3's quiet failures are: the returned
   values (1253–1342) are not absurd on their face.**
4. **Six agreeing windows can all be wrong (p. 260).** Rule 3 says run width is
   the confidence signal, not the value; p. 260 shows that *window agreement* is
   not a confidence signal either. Six windows returned an identical 1386 on an
   identical 20 px run. Only three windows were right. **Agreement among windows
   that share a failure mode is agreement about the failure.**
5. **The raw-quality grade, given per page and per region as required.** Body
   prose in pp. 252–264 is broadly usable and every one of the twelve receiving
   headings survives in it, though six are garbled. Two regions degrade sharply:
   p. 260's Cap. VI closing (L47906 `laolia. .  ■,•!••  .  .`) and the whole of
   p. 263's body from L48400, where bracket-substitutions swamp the line
   (`ex tri[)lici radicc`, `co)i.?(7«t evangclica`, `sii/licirnlrni , \ •`).
   **Footers are, as always in Vol V, numeral-less and were read only from the
   bands.** The raw also interleaves p. 257's folio and running head *between*
   p. 256's footer and the tail belonging to p. 257 (L47245–47255) — a trap for
   anyone taking raw line order as page order.
6. **The `<!-- page N -->` convention behaves here as in Pars III** — markers
   round to paragraph boundaries in both directions, applied uniformly across all
   ten chunks, so an anchor's page label need not match its enclosing marker
   region. The ownership table above is derived from the **labels and the bands**,
   not from the markers.

---

## `[?]`-grade flags I would raise

**One, and it is documentation only.**

**`[?] tools/check-vol5-apparatus.py`, the `KNOWN_TOTALS` comment for p. 252.**
The comment states: *"The p.252 -> p.253 test is NOT run — p.253 is not imaged —
and is forwarded to p5-c1."* p. 253 **is** now imaged, the test **was** run in
this pass from both sides, and it **closes NEGATIVE** (p. 252's right block ends
complete at n. 6 `I M beatificativae.`; p. 253's left block opens numbered ¹).
The comment is therefore stale rather than wrong — it describes a pending test
that has since been discharged, and a reader would take it as an open item. `p5-c1`'s
own `## Notes` do close it; the comment beside `KNOWN_TOTALS` was never updated to
match. **No corpus text is affected, no chunk is wrong, no count moves.** Suggested
repair for whoever owns the file: replace the last sentence of the p. 252 entry with
`The p.252 -> p.253 test is CLOSED NEGATIVE by p5-c1 (p.252 R block ends complete at
n.6, p.253 L block opens NUMBERED at n.1).`

For the record, the **p. 260 comment is NOT a flag**: it was already corrected by
`p5-c7`, it now states the 4/3 division and withdraws the coincidence claim, and
**the plate agrees with it in every particular**. The defect CLAUDE.md records
lives in `p5-c6`'s prose summary, which the corrected comment already
supersedes.

---

## Disposition

**PASS 3 CLEAN for Pars V. Zero corpus defects, zero repairs, no chunk edited,
`KNOWN_TOTALS` unchanged, no git write command run.**

- **11 boundaries swept — 10 mid-page, 1 leaf crossing — all CLEAN.**
- **98 apparatus entries re-derived** across 10 chunks, exactly matching the sum
  of the thirteen pages' band-read registers; every page's total matches
  `KNOWN_TOTALS`; ownership runs 1..N on every page with no gap, no double claim
  and no unowned note.
- **Six runovers re-derived** (five gutter: pp. 254 n. 3, 255 n. 8, 259 n. 5,
  260 n. 3, 263 n. 4; one page-crossing: p. 253 n. 9), each logged exactly once,
  none double-counted; twelve page-crossing tests closed NEGATIVE from both sides.
- **The shared p. 252 seam is certified clean from the Pars V side, independently
  derived**: register 6, dividing 1/5 by pars; `p4-c10` owns n. 1 whose anchor
  stands in the RIGHT column of the upper region while its entry prints first in
  the LEFT block (reading order, not over-run); both the incoming and the outgoing
  page-crossing tests close NEGATIVE; gutter 1403 on nine sound windows.
- **The p. 264 → p. 265 leaf edge is certified clean from both sides**: Pars V
  closes at `…generis statutorum.` ~66 % down p. 264's right column, fixed
  positively from the full-width `PARS SEXTA` heading at the HEAD of p. 265 and
  corroborated by Pars VI's own opening recapitulation of Partes I–V; p. 264's
  register is 6, all `p5-c10`'s, n. 6 complete, nothing forwarded; p. 265's left
  block opens numbered.
- **The p. 260 anchor split is 4/3, blocks 3/4, capitulum line between nn. 3 and
  4 — three lines, three positions.** The plate supports the corrected reading
  now standing in `KNOWN_TOTALS`, not the withdrawn 3/4 summary. The first Pars V
  leaf on which all three lines coincide is **p. 262**.
- **One `[?]`-grade flag is raised, and it is documentation only** (a stale
  "test not run" sentence in `KNOWN_TOTALS`'s p. 252 comment). It affects no
  chunk and blocks nothing.
