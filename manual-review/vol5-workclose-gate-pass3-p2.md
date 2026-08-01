# Vol V work-close gate — PASS 3 (cross-chunk boundary integrity), Pars II

**Scope:** `bon-brev-p2-c1`…`-c12` — 12 chunks, printed pp. 219–230 (pdf 295–306; offset
`pdf = printed + 76`). Plus the incoming seam `p1-c9 → p2-c1` (p. 218 → p. 219) and the
outgoing seam `p2-c12 → p3-c1` (p. 230 → p. 231); the receiving side of the outgoing seam
belongs to the Pars III agent and is **certified here from this side only**.

Run 2026-08-01, as pass 3 of the Breviloquium work-close gate (CLAUDE.md § "Polish-gate
cadence for Vols V–X", trigger 2 — work boundary, unconditional). Companion log for the
prologue and Pars I: `vol5-workclose-gate-pass3-prol-p1.md`. **Nothing was edited; no
`KNOWN_TOTALS` entry changed; no git write command was run.**

Derived counts (not carried): **12 chunks, 89 apparatus entries** in scope (`re` walk of
the twelve `## Apparatus` sections at the moment of writing). That figure is exactly the
sum of the twelve printed pages' registers as read off the bands below
(5+6+7+5+9+8+7+9+9+9+8+7 = 89), so Pars II owns its twelve pages entire — no note in the
range belongs to a chunk outside it, and no chunk inside it reaches outside the range.
Corpus-wide at the same moment, `check-vol5-apparatus.py` reports **79 chunks, 681
apparatus entries — All checks passed**; `check-vol5-census.py` reports **79 on disk / 79
in ledger, rosters agree**, with 59 runovers (54 gutter-crossing, 5 page-crossing).
**None of the five page-crossing runovers falls in pp. 219–230** — they are pp. 206, 212,
246, 253, 277 — so no register in this scope spills across a leaf.

---

## Method actually used

1. **Gutters re-measured fresh on every page, no constant, no parity prediction** —
   `colcrop.py`'s own `measure_gutter` profile, driven over **eight** independent row
   windows (45–92 %, 30–70 %, 50–80 %, 55–90 %, 35–60 %, 60–88 %, 47–60 %, 70–92 %), and
   in parallel a merged-band read that unites the two zero-ink runs on either side of
   Quaracchi's printed centre rule (CLAUDE.md gutter rule 5) before taking the midpoint.
   **Run width is the confidence signal**: a run far above ~64 px or far below ~58 px was
   treated as a failure, not as a narrow gutter. No separate measuring script was
   hand-rolled — the tool's own profile function was called directly.
2. **Body continuity established POSITIVELY from the next heading**, never from white
   space (CLAUDE.md's `p2-c4` rule, which was *earned in this very scope*). For each of the
   thirteen boundaries the raw djvu was walked to the receiving unit's `Cap. N.` /
   `PARS TERTIA` heading, and the ~12 lines immediately preceding it compared word-for-word
   against the prior chunk's Latin tail.
3. **Footers read off the 450 dpi bands, page by page** (bands-only rule — the Vol V raw
   has no footnote numerals). For each of pp. 219–230, and for p. 218 to settle the
   incoming seam, the last footer entry of the **right** block was read at `n=6, scale 2.6`
   and its number compared against `KNOWN_TOTALS` in `tools/check-vol5-apparatus.py`. Where
   the block structure or the ownership split was not obvious from that band alone (pp. 218,
   224, 228) the band above it was read as well.

---

## Gutters measured

Adopted value = merged-band consensus across the surviving windows. "Chunk used" is the
split_x recorded in that page's chunk `transcription_status`, re-derived here rather than
adopted.

| p. | adopted | sound windows (spread) | runs | chunk used | Δ |
|---|---|---|---|---|---|
| 218 | 1377 | **1 of 8** (see below) | 59 px | 1379¹ | 2 |
| 219 | 1170 | 6 of 8 (1166–1177) | 52–58 px | 1171 | 1 |
| 220 | 1379 | 4 of 8 (1375–1382) | 59–62 px | 1380 | 1 |
| 221 | 1229 | 8 of 8 (1220–1231) | 59–73 px | 1233 | 4 |
| 222 | 1319 | 6 of 8 (1315–1319) | 65–73 px | 1319 | 0 |
| 223 | 1243 | 7 of 8 (1235–1248) | 60–79 px | 1241 | 2 |
| 224 | 1310 | 7 of 8 (1306–1317) | 59–76 px | 1314 | 4 |
| 225 | 1210 | 8 of 8 (1206–1215) | 55–63 px | 1207 | 3 |
| 226 | 1335 | 5 of 8 (1333–1339) | 65–79 px | 1333 | 2 |
| 227 | 1211 | 7 of 8 (1207–1216) | 57–64 px | 1211 | 0 |
| 228 | 1365 | 8 of 8 (1361–1368) | 56–64 px | 1365 | 0 |
| 229 | 1222 | 8 of 8 (1217–1226) | 55–63 px | 1222 | 0 |
| 230 | 1359 | **2 of 8** (1353–1359) | 61–75 px | 1361 | 2 |

¹ p. 218 is the Pars I closing leaf and belongs to the companion log; measured here only to
certify the incoming seam from this side. Its value is re-derived independently and agrees
with that log's 1379 to 2 px.

**Maximum divergence between this pass's measurement and the split each chunk was actually
built on is 4 px** (pp. 221 and 224), against a column width of ~1150 px. **No chunk in
Pars II can have been built on a truncated or padded column.**

### Measurements REJECTED, and why

- **p. 219 — `PARS SECUNDA` display heading.** The 47–60 % window returned **1323 on a
  388 px run** and the 35–60 % window 1210 on a 127 px run. Both windows land on the
  full-width part heading that crosses the gutter and destroys the blank column run — the
  named CLAUDE.md rule-2 case, and one of the four pages it names by number. Six body-only
  windows agree at 1166–1177 on 52–58 px runs.
- **p. 230 — the page-foot blank, not a gutter.** Five of eight windows blew out with runs
  of **179, 197, 308, 378 and 378 px**. Pars II *closes* on this leaf, so the body column
  ends high and any window reaching the foot swallows the white space beneath it and
  reports a wide, meaningless "run". Only the two windows confined to the upper body
  (30–70 %, 35–60 %) are sound: 1358/61 px and 1359/63 px. Note this is the *measurement*
  analogue of the `p2-c4` trap — the same blank paper corrupts the gutter reading and the
  boundary inference, and it must be rejected in both.
- **p. 218 — same cause, more severe.** Seven of eight windows returned runs of 107–463 px.
  Only the 30–70 % window is sound (1377, 59 px). Reported for completeness; the page
  belongs to the prol/Pars I scope.
- **p. 226 — page-foot blank again.** The 60–88 % and 70–92 % windows returned raw values
  of 1227 and 1222 on **274 px and 285 px runs**, some 110 px away from the true value;
  merged reads of 1122 and 1132 are equally spurious. Five upper-body windows agree at
  1333–1339 on 65–79 px runs.
- **p. 220 — three windows drift off a sound-looking value.** 70–92 % merged to 1201 on a
  199 px run, 60–88 % to 1404 on 102 px, 47–60 % to 1362 on 93 px. All rejected on run
  width; the four surviving windows sit inside 7 px.
- **p. 221 — `colcrop.py`'s bare default is one of the quiet failures.** The default
  (45–92 %) returns **1233 on a 46 px run**, below the ~60 px suspicion floor that
  CLAUDE.md rule 3 exists to catch. The merged-band read over all eight windows gives
  1220–1231 on 59–73 px runs → **1229**. The chunk was built on the 1233 default. The 4 px
  difference is immaterial to the crop, but the *provenance* is worth recording: p. 221 is
  the page whose default should not have been adopted unexamined.
- **Parity is used nowhere.** It is only remarked after the fact that the odd/even clusters
  happen to hold across pp. 219–230 — which is exactly what CLAUDE.md warns is true right
  up until it isn't (pp. 221/222/223 are the retired model's own counter-examples, and they
  are in this scope).

---

## Boundary table

**Thirteen boundaries: eleven mid-page, two leaf crossings.** `seam-screen.py --volume 5`
sees the eleven mid-page ones (and 71 corpus-wide, 0 tail-not-terminal suspects); it is
structurally incapable of seeing the two leaf crossings, which are precisely the seams
where a forwarded note goes missing.

| # | Prior → Receiving | Shared page / crossing | Body continuity — evidence | Footer split (page total) | Verdict |
|---|---|---|---|---|---|
| 0 | `p1-c9` → `p2-c1` | **leaf crossing** p. 218 → p. 219 | Heading `PARS SECUNDA.` found **in the raw** at L41501 (with `Cap. I` at L41510). The twelve lines above it are p. 218's *footer register*, not body — the raw runs body→footer→running head→next page. `p1-c9`'s tail `…Ipsi gloria in saecula saeculorum. Amen.` is therefore the last body on p. 218, corroborated by the following display heading and **not** accepted on the strength of its `Amen.`-shaped ending | p. 218 total **7**, all `p1-c9`'s. Read on the band: the right block carries nn. 6–7; n. 7 (`Rom. 11, 33-36. Cfr. I. Sent. d. 41. a. 1. q. 2. — Paulo superius pro munus gratiae…gratiam.`) **ends complete on p. 218**, with clear blank beneath. p. 219's left block opens at n. 1 (`Sap. 11, 21.`). **Nothing forwarded** | **CLEAN** |
| 1 | `p2-c1` → `p2-c2` | p. 219 (mid-page) | `Cap. If.` (= Cap. II) found in the raw at L41614. c1 tail `…est enim *pondus* inclinatio ordinativa[^p219-3]. — Et haec quidem generaliter dicta sunt de omni creatura, sive corporea, sive incorporea, sive ex utrisque composita, sicut est natura humana.` = raw L41604–41612 word for word | 3 / 2 (5); blocks split 3/2 with **n. 3 running over the gutter** (L block ends `…Pondus enim est impetus quidam cuiusque rei velut conan-`, R block resumes `tis ad locum suum. Cfr. supra p. I. c. 6.`) — already logged in the ledger, not re-logged here | **CLEAN** |
| 2 | `p2-c2` → `p2-c3` | p. 220 (mid-page) | `Cac. III.` (garbled `Cap. III.`) found in the raw at L41753. c2 tail `…et qui praecesserunt, et etiam qui secuti sunt beatum Augustinum.` = raw L41749–41751 | 5 / 1 (6); band's last entry is n. 6 (`Vide II. Sent. d. 2. p. II. a. 1. q. 1; d. 14. p. I. a. 1. q. 1. … Inferius pro sensibilis C materialis.`), which is c3's `[^p220-6]` | **CLEAN** |
| 3 | `p2-c3` → `p2-c4` | p. 221 (mid-page) | `Cap. IV.` found in the raw at L41887. c3 tail `…ut suo modo suum repraesentet principium.` = raw L41884–41885 | 3 / 4 (7); band's last entry is n. 7 (`Cfr. Rom. 8, 19. seqq., et tom. II. pag. 421, nota 4.`). n. 5 is the Greek zodiac note (`ζῴδιον` / `ζωή`) | **CLEAN** |
| 4 | `p2-c4` → `p2-c5` | p. 222 (mid-page) | `C.\p. V.` (garbled `Cap. V.`) found in the raw at L42018. c4 tail `…ut, sicut *anima* modo ratione corporis et status meriti nunc est in terris, sic aliquando *corpus* ratione animae et status praemii sit in caelis.` = raw L42011–42016, sitting **immediately** above the heading. **This is the re-derivation of the original `p2-c4` truncation defect: the chunk is now whole** (see the dedicated section below) | 2 / 3 (5); band's last entry is n. 5 (`Gen. 1, 1. — Seq. locus est ibid. v. 2. — Aliquanto inferius post elevata H P Q S addunt significatur.`). n. 2 is the long *Additamentum*, running over the gutter and rejoined in c4 | **CLEAN** |
| 5 | `p2-c5` → `p2-c6` | **p. 224** (mid-page — note the shared page is 224, not 223) | `Cap. VI.` found in the raw at L42319. c5 tail `…et sic ex praedictis apparet sufficientia et veritas Scripturae in diversis opinionibus Sanctorum, scilicet Augustini et aliorum, quae sibi non contradicunt, cum verae sint, si recte intelligantur.` = raw L42313–42317 — which in the raw sits **after** p. 223's footer register and after the running head `BREVILOQUII PARS II. C. VI. VII.` and signature `224`, i.e. **at the head of p. 224's left column**. c5's `<!-- page 224 -->` marker is present and correctly placed | p. 223 total **9**, all c5's — band's last entry n. 9 (`De quo supra in Prologo § 2. — In seq. propositione tangitur opinio Augustini…quae sibi pro qui sibi.`), matching raw L42297–42304 | **CLEAN** |
| 6 | `p2-c6` → `p2-c7` | p. 224 (mid-page) | `Cap. VII.` found in the raw at L42393. c6 tail `…ideo *stabilitatem* habet post electionem in electo sive in bono, sive in malo. — Et hae conditiones ipsam generalem conditionem supernorum spirituum generaliter comitantur.` = raw L42388–42392 | 7 / 1 (8); blocks split **5 / 3** (L nn. 1–5, R nn. 6–8) while the capitulum boundary falls at 7/8 — so **the boundary lies inside the right footer block**, the p. 247 shape. Band's last entry is n. 8 (`August., III. de Lib. Arb. c. 15. n. 44 … Superius post amandum A addit summum bonum, et O bonum incommutabile.`), whose subject matter (the fall of the angels) is Cap. VII's, confirming ownership by anchor and not by block | **CLEAN** |
| 7 | `p2-c7` → `p2-c8` | p. 225 (mid-page) | `Cap. VIH.` (crossbar-less `Cap. VIII.`) found in the raw at L42532. c7 tail `…quod tamen iuste Deus modo permittit ad vindictam malefactorum, laudem vero bonorum, sicut apparebit per finale iudicium.` = raw L42526–42530 | 4 / 3 (7); band's last entry is n. 7 (`Cfr. supra pag. 224, nota 7. — Mox pro immutabilitatem I immutabilem…converterentur sive.`) + signature `29`. **Quaracchi's own `Cfr. supra pag. 224, nota 7` independently corroborates that p. 224 carries at least seven notes** | **CLEAN** |
| 8 | `p2-c8` → `p2-c9` | p. 226 (mid-page) | `Cap. IX.` found in the raw at L42707. c8 tail `…Ordo autem denominari debet ab eo quod « excellentius accepit in munere[^p226-5] ».` = raw L42702–42705 | 5 / 4 (9); band's last entry is n. 9 (`Secundum Dionys., de Caelest. Hierarch. c. 4. § 3, c. 8. § 2. et de Ecclesiast. Hierarch. c. 5. § 4…`). c8's own note records that the **left** block carries all five of nn. 1–5 although n. 5 anchors in the right column — block extent and anchor column diverge, as CLAUDE.md says they routinely do | **CLEAN** |
| 9 | `p2-c9` → `p2-c10` | p. 227 (mid-page) | `Cap. X.` found in the raw at L42913. c9 tail `…consurgit integritas libertatis, quae est principium meriti, vel demeriti, secundum electionem boni, vel mali.` = raw L42906–42911 | 9 / 0 (9) — **Cap. X opens on p. 227 and claims no note there**. Band's last entry is n. 9 (`Libr. III. Hypognosticon (inter opera August.), c. 5. n. 7: Cum de libero arbitrio agimus… — P omittit certe.`), which is c9's `[^p227-9]` at `Ait enim`. The zero-claim was verified positively on the band, not inferred from c10's silence | **CLEAN** |
| 10 | `p2-c10` → `p2-c11` | **p. 229** (mid-page) | `Cap. XI.` found in the raw at L43152. c10 tail `…a *regimine* vero *divinae providentiae* sicut interius conservante et exterius protegente.` = raw L43147–43149 — which sits after the running head `PARS II. C. XI.` and signature `229`, i.e. **at the head of p. 229**. c10's `<!-- page 229 -->` marker is present. Corroborated on the band: p. 228's right column ends mid-sentence at `…nente et suscipiente, a *ligno* autem *vitae* sicut a` | p. 228 total **9**, all c10's — band's right block carries nn. 7–9, n. 7 running over the gutter (R resumes `hominem rectum. Cfr. supra pag. 225, nota 1.`), last entry n. 9 (`Libr. VIII. de Gen. ad lit. c. 4. n. 8: Erat ei ergo in lignis ceteris alimentum…`). pp. 227 and 229 contribute nothing to c10 | **CLEAN** |
| 11 | `p2-c11` → `p2-c12` | **p. 230** (mid-page) | `Cap. XII.` found in the raw at L43308. c11 tail `…Ex quo manifeste colligitur, quod si cecidit, hoc non fuit nisi ex culpa sua, quia obedire contempsit.` = raw L43301–43305 — after the running head `BREVILOQUII PARS II. C. XII.`, i.e. **at the head of p. 230**. c11's `<!-- page 230 -->` marker is present, and its `[^p230-1]` anchor (`sicut se ipsum`) sits in that carried-over sentence | p. 229 total **8**, all c11's — band's last entry n. 8 (`Edd., excepta 2, rectitudo synderesis. Superius voci adiutorium B praefigit beneficium sive.`) = raw L43296–43297. p. 230 splits 1 / 6 | **CLEAN** |
| 12 | `p2-c12` → `p3-c1` | **leaf crossing** p. 230 → p. 231 (Pars III opens) | `PARS TERTIA.` found **in the raw** at L43443 (`Cap. I.` at L43448), after p. 230's footer register, the running head `PARS III. C. I. n.` and signature `231`. c12 tail `…quod non facit, nisi consideret et attendat ruinam humanae naturae.` = raw L43400–43404, the last body on p. 230. **The boundary is set from the display heading, never from the large blank at the foot of p. 230** | p. 230 total **7**. Band: the right block's last entry is n. 7 (`Hugo a S. Vict., loc. cit.: Postquam autem tenebrae peccati in illam [animam] intraverunt… deinde pro amittit edd., excepta 2, amisit, quae etiam in fine cap. cum uno alteroque cod. diligenter.`) and it **terminates on the page**, with a large blank beneath — confirmed independently in the raw (the entry closes at L43434, before the p. 231 running head). `p3-c1` opens its own register at `[^p231-1]`. **Nothing forwarded into p. 231** | **CLEAN** |

**13 boundaries swept (11 mid-page, 2 leaf crossings). 13 CLEAN, 0 DEFECT.**

---

## Footer accounting — every page re-read off the band

| p. | plate's last numbered entry (band) | `KNOWN_TOTALS` | agree? | ownership |
|---|---|---|---|---|
| 218 | 7 (`Rom. 11, 33-36. Cfr. I. Sent. d. 41. a. 1. q. 2.`) | 7 | ✅ | all `p1-c9`; nothing forwarded |
| 219 | 5 (`Gen. 1, 1. — Seq. locus est ibid. v. 6; tertius v. 9…`) | 5 | ✅ | `c1` 1–3 · `c2` 4–5 (blocks 3/2; n. 3 crosses the gutter) |
| 220 | 6 (`Vide II. Sent. d. 2. p. II. a. 1. q. 1…`) | 6 | ✅ | `c2` 1–5 · `c3` 6 |
| 221 | 7 (`Cfr. Rom. 8, 19. seqq., et tom. II. pag. 421, nota 4.`) | 7 | ✅ | `c3` 1–3 · `c4` 4–7 |
| 222 | 5 (`Gen. 1, 1. — Seq. locus est ibid. v. 2.`) | 5 | ✅ | `c4` 1–2 · `c5` 3–5; n. 2 = the *Additamentum*, crosses the gutter |
| 223 | 9 (`De quo supra in Prologo § 2.`) | 9 | ✅ | all `c5` |
| 224 | 8 (`August., III. de Lib. Arb. c. 15. n. 44`) | 8 | ✅ | `c6` 1–7 · `c7` 8 (blocks 5/3 — boundary inside the right block) |
| 225 | 7 (`Cfr. supra pag. 224, nota 7.`) + signature `29` | 7 | ✅ | `c7` 1–4 · `c8` 5–7 |
| 226 | 9 (`Secundum Dionys., de Caelest. Hierarch. c. 4. § 3`) | 9 | ✅ | `c8` 1–5 · `c9` 6–9 (left block carries all of 1–5 though n. 5 anchors right) |
| 227 | 9 (`Libr. III. Hypognosticon…c. 5. n. 7`) | 9 | ✅ | all `c9`; Cap. X opens here and claims none |
| 228 | 9 (`Libr. VIII. de Gen. ad lit. c. 4. n. 8`) | 9 | ✅ | all `c10`; n. 7 crosses the gutter |
| 229 | 8 (`Edd., excepta 2, rectitudo synderesis.`) | 8 | ✅ | all `c11` |
| 230 | 7 (`Hugo a S. Vict., loc. cit.: Postquam autem tenebrae peccati…`) | 7 | ✅ | `c11` 1 · `c12` 2–7; **Pars II ends here, nothing forwarded** |

**No page's true total differed from `KNOWN_TOTALS`. No register was dropped, none
double-claimed, no page in scope unowned.** `check-vol5-apparatus.py` independently reports
`p.219 … p.230` each as `1-N (N notes) ok` — no interior GAP, no trailing PENDING — but
that script's totals are checked *against* `KNOWN_TOTALS`, which is itself a hand-entered
band read; **the twelve band reads above are the independent check it cannot perform on
itself.**

Digit reads worth recording (both confusion classes are live on these leaves): p. 221 n. 7
prints `tom. II. pag. 421` — the `1`/`4` class, settled by the run of digits around it;
p. 224 n. 8 prints `c. 15. n. 44` and `II. c. 19. n. 53`, a `1`/`4` and a `3`/`5` decision
one clause apart; p. 227 n. 6 prints `tom. III. pag. 579, nota 9`. **No transcription
change follows from any of them** — the chunks already carry these readings.

---

## The `p2-c4` failure, re-derived

`p2-c4` is the original instance of the "chunk written short at a column foot" bug, and it
is in this scope. Its own `## Notes` records the repair. **That record was not adopted; the
chunk was re-derived from the raw:**

- c4's Latin runs from `Cap. IV.` (raw L41887) to a tail that matches raw L42011–42016
  word for word, and the `C.\p. V.` heading stands at L42018 with nothing between.
- The paragraph the first version dropped is present: `Et propterea indubitanter verum est`
  (raw L42005) occurs in the chunk, as does `non fatum seu vis positionis siderum`.
- Both apparatus entries for p. 222 are present and correctly labelled (`[^p222-1]`,
  `[^p222-2]`), and the page break `<!-- page 222 -->` is in place.
- p. 222's register totals 5 on the band, split 2/3 between c4 and c5 with no gap.

**`p2-c4` is whole.** No trace of the truncation survives.

One caution about the record rather than the text, per the CLAUDE.md rule that a structural
generalisation is the least reliable line in any `## Notes`: c4's `transcription_status`
says *"the closing paragraph on p.222 had been truncated"* while its `## Notes` narrates
the wrong inference as having been made about **p. 221's** right column. Both sentences are
defensible readings of the same event (the bad inference was drawn at p. 221's foot; the
text lost was p. 222's), but they are not the same sentence, and only the per-note data —
re-derived above — settles it. Recorded, not repaired.

---

## `[?]` flags

**Zero `[?]` flags in Pars II.** All twelve chunks match `\[?\]` only in the boilerplate
phrase "No `[?]` flags" inside their own `## Notes`; there is no inline flag in any Latin
or English body, and none in any apparatus entry.

One observation is raised **as a documentation `[?]`, not a text defect** — see below.

---

## `[?]` DOC-1 — four chunks' declared raw-line ranges do not bracket their bodies

`transcription_status` on `p2-c5`, `-c6`, `-c7` and `-c8` cites raw line ranges that do not
match where those chunks' bodies actually sit in `raw/doctorisseraphic05bona_djvu.txt`:

| chunk | declared range | true body range (between headings) |
|---|---|---|
| `p2-c5` | 42022–42200 | 42023–**42317** (Cap. V L42018 → Cap. VI L42319) |
| `p2-c6` | 42213–42320 | **42323–42392** (Cap. VI L42319 → Cap. VII L42393) |
| `p2-c7` | 42332–42450 | **42397–42530** (Cap. VII L42393 → Cap. VIII L42532) |
| `p2-c8` | 42462–42706 | **42536–42705** (Cap. VIII L42532 → Cap. IX L42707) |

`p2-c8`'s is explicable and probably deliberate — its status string says the raw for that
opening was cascade-degraded past use and served only for anchor positions and marginalia
order, so `L42462–42706` reads as the raw *region consulted* (including p. 225's footer
register), not the body. The other three drift without explanation, and `p2-c5`'s declared
end falls **117 lines short of its own tail**.

**The bodies themselves are complete.** Every substantive passage in the raw between
L42200 and L42317 was checked against `p2-c5` individually and is present — `subtiles et
incorruptibiles`, `Collocantur etiam ratione virtutis et influentiae`, `caelum … non est
essentialiter frigidum`, `scientia salutaris`, `sublimitatem Scripturae non decebat prorsus
reticere`, `per septenarium dierum` (the last three found only after allowing for the
chunk's italic asterisks, which defeat a naive grep — worth knowing for anyone repeating
this check). Likewise `p2-c6`'s body carries `quatuor sunt attributa`, `perspicacitas in
discernendo`, `intellectum deiformem` and its `stabilitatem` clause.

So this is a **provenance-string inaccuracy, not a boundary or content defect**. It is
recorded here because a future pass that trusts these ranges to bound a re-read will read
the wrong lines — and because `p2-c5`'s understated end is exactly the shape a genuine
truncation would leave in the record. **Do not repair it in this pass.**

---

## Disposition

**PASS 3 CLEAN for Pars II. Zero defects, zero repairs, no chunk edited, `KNOWN_TOTALS`
unchanged, no git write command run.** One `[?]` DOC-1 raised against four
`transcription_status` strings (documentation only; the bodies are verified complete).

**Certified to the Pars III agent, from this side of the p. 230 → p. 231 seam:**

1. p. 230's register totals **7**, and its last entry — n. 7, the Hugo of St Victor note on
   the *oculus contemplationis* — **ends complete on p. 230**, verified on the 450 dpi right
   footer band and independently in the raw (closes at L43434, before the p. 231 running
   head). **Nothing is forwarded into p. 231.**
2. p. 230's notes divide `c11` 1 · `c12` 2–7. Pars II claims **no note on p. 231** and no
   note anywhere above p. 230.
3. `p2-c12`'s body ends at `…nisi consideret et attendat ruinam humanae naturae.`
   (raw L43400–43404), the last body text on p. 230. The large blank beneath it on the
   plate is **footer-register space, not a boundary signal** — the boundary is set from the
   `PARS TERTIA.` display heading at raw L43443.
4. Consequently `p3-c1` correctly opens its own p. 231 register at `[^p231-1]`, and its
   incoming hand-off is **empty**. Per CLAUDE.md, that is a claim to re-derive, not a fact
   to adopt.
5. **p. 231 opens a pars, so its gutter measurement will fail on any window touching the
   `PARS TERTIA` display heading** — the same failure this pass logged on p. 219. Profile
   the body rows only, and reject any run far outside ~58–64 px.
