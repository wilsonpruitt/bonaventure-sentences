# Vol V work-close gate — PASS 3 (cross-chunk boundary integrity), Pars III

**Scope:** `bon-brev-p3-c1` … `bon-brev-p3-c11` — 11 chunks, printed pp. 231–241
(pdf 307–317; offset `pdf = printed + 76`). Plus the **incoming** seam
`p2-c12 → p3-c1` (leaf crossing p. 230 → p. 231) and the **outgoing** seam
`p3-c11 → p4-c1` (p. 241, shared). The incoming seam is certified here from the
Pars III side independently of the Pars II agent's own derivation — the double
derivation is deliberate.

Run 2026-08-01, as pass 3 of the Breviloquium work-close gate (CLAUDE.md
§ "Polish-gate cadence for Vols V–X", trigger 2 — work boundary, unconditional);
the pass-3 definition is CLAUDE.md § "Polish-blocker cadence" step 3.
**Nothing was edited; no `KNOWN_TOTALS` entry changed; no git write command run.**

Derived counts (not carried): **11 chunks, 81 apparatus entries** in scope (`re`
walk of the eleven `## Apparatus` sections at the moment of citing).
Corpus-wide, `check-vol5-apparatus.py` reports **79 chunks, 681 apparatus
entries — All checks passed**; `check-vol5-census.py` reports **79 on disk / 79
in ledger, rosters agree**, with **59 runovers across 79 chunks (54 gutter-crossing,
5 page-crossing; 48 chunks positive, 31 negative)**. None of the five
page-crossing runovers falls in pp. 231–241.

---

## Method actually used

1. **Gutters re-measured fresh on every page, no constant, no parity prediction.**
   `colcrop.py`'s own `measure_gutter` profile, read over **twelve** independent
   row windows per page (45–92 %, 30–70 %, 50–80 %, 35–60 %, 60–90 %, 47–60 %,
   55–85 %, 40–75 %, 65–92 %, 32–52 %, 70–90 %, 45–65 %). The function's low-ink
   run already **merges the two zero-ink runs either side of Quaracchi's printed
   centre rule** — `xs[0]`…`xs[-1]` spans the island — so the reported run width
   *is* the merged band and its midpoint is the merged-band midpoint. Windows
   whose run fell outside a sound 50–75 px were discarded; the per-column ink
   profile (blank band, rule island, island peak) was printed for every page,
   including the pages where the windows agreed.
   ⚠ Pars III's leaves carry mid-column `Cap. N.` headings, and they behaved
   exactly as CLAUDE.md gutter-rule 2 predicts: **48 of the 144 windows blew out**
   (runs of 96–437 px), and the blow-outs cluster on the pages where a capitulum
   opens mid-column. Forking the windows and discarding the blown-out ones left a
   tight consensus on every page.
2. **Body continuity established POSITIVELY from the next heading**, never from
   white space (CLAUDE.md's `p2-c4` rule). The raw djvu
   (`raw/doctorisseraphic05bona_djvu.txt`) was walked to each receiving unit's
   heading and the ~12 lines immediately preceding it compared word-for-word
   against the prior chunk's tail. **All twelve receiving headings were found in
   the raw** — none had to be read off the band, though several are garbled
   (`C.\p. II.`, `C.\p. V.`, `Cai>. VII.`, `C.\p. VIII.`, `Cap. LX.` for Cap. IX,
   `C.\p. X.`). Raw line map: `PARS TERTIA` L43443 · Cap. I L43448 · II L43542 ·
   III L43675 · IV L43797 · V L43929 · VI L44077 · VII L44228 · VIII L44323 ·
   IX L44488 · X L44642 · XI L44861 · `PARS QUARTA` L45036.
3. **Every printed page's footers read off the 450 dpi bands** (bands-only rule —
   the Vol V raw has no footnote numerals). For each of pp. 230–241 both the
   **left and the right** footer blocks were read at `n=3, scale 1.8` (the whole
   register, not just its foot): the last numbered entry of the right block and
   its number, whether the right block opens numbered or with an unnumbered
   continuation, the block split point, and the column position of the anchors
   visible in the same band. The raw was used for body prose only, and its footer
   blocks only as a cross-count.
4. Watched for the two named failure families — the **cascade-merge splice** (a
   tail that does not parse) and the **chunk written short at a column foot**.

### Gutters measured

| p. | adopted `split_x` | windows kept / 12 | run (px) | spread (px) | blank band → midpoint | rule island (peak rows) |
|---|---|---|---|---|---|---|
| 230 | **1359** | 4 | 60–63 | 4 | 1332–1391 → 1361 | 1357–1364 (304) |
| 231 | **1194** | 11 | 52–63 | 9 | 1168–1220 → 1194 | 1186–1200 (360) |
| 232 | **1337** | 11 | 60–63 | 2 | 1308–1367 → 1337 | 1335–1341 (1436) |
| 233 | **1211** | 12 | 52–62 | 9 | 1186–1237 → 1211 | 1205–1219 (346) |
| 234 | **1340** | 4 | 62–64 | 3 | 1310–1372 → 1341 | 1335–1371 (133) |
| 235 | **1210** | 11 | 56–63 | 8 | 1182–1238 → 1210 | 1204–1216 (266) |
| 236 | **1331** | 9 | 61–62 | 1 | 1301–1361 → 1331 | 1329–1333 (638) |
| 237 | **1209** | 11 | 59–72 | 10 | 1180–1238 → 1209 | 1205–1213 (556) |
| 238 | **1338** | 3 | 62 | 0 | 1308–1369 → 1338 | 1336–1340 (465) |
| 239 | **1200** | 9 | 62–65 | 2 | 1169–1231 → 1200 | 1199–1203 (267) |
| 240 | **1338** | 4 | 60–64 | 2 | 1309–1368 → 1338 (30–70 % window) | 1336–1343 (340) |
| 241 | **1228** | 5 | 60–62 | 1 | 1199–1258 → 1228 (30–70 % window) | 1225–1232 (1088) |

**The in-gutter obstruction is present on all twelve leaves** — the printed centre
rule, per CLAUDE.md gutter-rule 5. Its absence is what would have been worth
remarking; it was never absent.

**Measurements rejected, and why.**

- **p. 240 — `colcrop.py`'s bare default rejected.** The 45–92 % body window (and
  five other lower windows) returned **1362 on a 13 px run** — under the tool's own
  15 px warning threshold, so this is the *loud* failure. Four upper windows
  (30–70 %, 35–60 %, 32–52 %, 45–65 %) agree at **1337–1339 on 60–64 px runs**, and
  the 30–70 % ink profile puts a centred rule at x=1336–1343 inside a blank band
  x=1309–1368 → midpoint **1338**. Adopted 1338. This is the genuine
  marginal-gloss-set-low case (CLAUDE.md names pp. 240 and 244), where moving the
  window **up** is the correct remedy.
- **p. 241 — `colcrop.py`'s bare default rejected.** Default **1218 on a 39 px
  run**; six lower windows all sit at 1215–1218 on 39–45 px runs. Five upper
  windows agree at **1228–1229 on 60–62 px runs**, and the 30–70 % profile gives
  band 1199–1258 with a heavily inked rule at 1225–1232 (peak 1088 rows) →
  midpoint **1228**. Adopted 1228. This re-derives, from scratch and without
  consulting it, the value CLAUDE.md records for p. 241 (`default 1218 on a 39 px
  run, true 1228`).
- **48 individual windows discarded across the twelve pages** on blown-out runs
  (96–437 px). The worst offenders are the leaves where a capitulum opens
  mid-column: p. 234 lost **eight** of twelve windows (runs 96–437 px, values
  spread 1241–1357) and p. 238 lost **nine** (runs 137–437 px, values spread
  1264–1386). On both, the surviving windows agreed to ≤ 3 px. A far-above-band
  run is the same species of failure as a far-below-band one.
- **p. 231, p. 233 — narrow but sound.** Both returned runs of 52–56 px in several
  windows, below the comfortable 58–64 px band. Neither was rejected: eleven and
  twelve windows respectively survive, spreads are 9 px, and in both cases the
  merged-band midpoint coincides with the rule island's own centre (p. 231 band
  centre 1194 / island centre 1193; p. 233 band centre 1211 / island centre 1212).
  The narrowness is the rule inking heavily, not a narrow gutter — CLAUDE.md
  gutter-rule 5, last bullet.
- **p. 231 is a part-opening leaf** (full-width `PARS TERTIA` display heading) and
  did **not** suffer the p. 201 / p. 219 / p. 252 failure mode: the body-rows
  windows returned healthy runs because the display heading sits above the 45 %
  floor. Worth recording as a counter-example — a part opening does not
  *automatically* destroy the measurement.

No parity reasoning was used anywhere. (Post hoc: the odd/even clusters happen to
hold across pp. 230–241, at ~1194–1211 odd and ~1331–1359 even. This is an
observation after the fact and is not evidence for the retired parity model.)

---

## Boundary table

**Twelve boundaries in scope: nine mid-page, three leaf crossings.**
`seam-screen.py --volume 5` sees only the mid-page class (it reports 71 mid-page
boundaries corpus-wide, 0 tail-not-terminal suspects, of which nine fall in this
range) — the three leaf crossings are outside its denominator, which is precisely
why they are swept by hand here.

| # | Prior → Receiving | Shared page / crossing | Body continuity — evidence | Footer split (page total) | Verdict |
|---|---|---|---|---|---|
| 1 | `p2-c12` → `p3-c1` | **leaf crossing** p. 230 → p. 231 | p2-c12 tail `…quod non facit, nisi consideret et attendat ruinam humanae naturae.` = raw L43404, the last body line of p. 230; p. 230's footer register follows (L43407–43434), then the running head + folio, then `PARS TERTIA / De corruptela peccati / Cap. I.` (raw L43443–43448). **Heading found in the raw, un-garbled.** The `Amen`-less but complete-looking end of Pars II is corroborated by the following display heading, not accepted on its own | p. 230 total **7**; band-read: right block holds nn. 6–7, n. 7 (`Hugo a S. Vict., loc. cit.: Postquam autem tenebrae peccati…cum uno alteroque cod. diligenter.`) **closes complete on the page — nothing forwarded into p. 231**; p. 231's register restarts at n. 1. Ownership on p. 230 is `p2-c11` n. 1 · `p2-c12` nn. 2–7 | **CLEAN** |
| 2 | `p3-c1` → `p3-c2` | p. 231 (mid-page, right col.) | c1 tail `…Apparet etiam, quae sit mali origo, et quid sit mali subiectum.` = raw L43540, immediately above `C.\p. II.` (L43542) + `De primorum parentum tentatione.` (L43544); c2 opens `Ad intelligendum autem, qualiter corruptela peccati introivit in mundum…` = L43546. Contiguous, nothing between | 6 / 1 (7). Left block nn. 1–3 (n. 3 closes complete, `I. Sent. d. 3. p. I. dub. 3.`), right block opens **numbered** ⁴ → runover NEGATIVE. Blocks 3/4, column anchors 3/4 — they coincide; the capitulum break falls **inside the right block**, between nn. 6 and 7 | **CLEAN** |
| 3 | `p3-c2` → `p3-c3` | p. 232 (mid-page, right col.) | c2 tail `…secundum quae tria attenditur omnis tentationis origo, sive a mundo, sive a carne, sive a diabolo.` = raw L43673, immediately above `Cap. III.` (L43675) | 7 / 2 (9). Left block nn. 1–5 (n. 5 closes complete, `…pro magnae edd. cum pluribus codd. maximae.`), right block opens **numbered** ⁶ → NEGATIVE. Blocks 5/4, column anchors 5/4 — coincide; capitulum break **inside the right block**, between nn. 7 and 8 (two notes below the block break) | **CLEAN** |
| 4 | `p3-c3` → `p3-c4` | p. 233 (mid-page) | c3 tail `…cecidit miserabiliter *infra se* a statu innocentiae et gratiae ad statum culpae et miseriae.` = raw L43794, immediately above `Cap. IV.` (L43797) | 3 / 2 (5). **Left block over-runs.** Left block holds nn. 1–**4** with n. 4 broken across the gutter; right block opens **unnumbered** (`Inferius pro *resolutionis in cinerem* R *incinerationis*…`) then n. 5, which closes complete + printer's signature `30`. Gutter runover POSITIVE at n. 4 — already logged once on `p3-c3`'s ledger line, **not re-logged here**; `p3-c4` renders it joined, verified word-for-word against both blocks | **CLEAN** |
| 5 | `p3-c4` → `p3-c5` | p. 234 (mid-page, left col.) | c4 tail `…ut sic « dedecus peccati non esset sine decore iustitiae[^p234-2] ».` = raw L43927, immediately above `C.\p. V.` (L43929) | 2 / 7 (9). **Left block under-runs by one.** Blocks 3/6 (n. 3 `De his agitur hic et 2 seqq. capp.` closes complete; right opens **numbered** ⁴ → NEGATIVE), but **column anchors divide 4/5** — Cap. V opens in the *left* column and its nn. 3–4 (`…tertio modus curationis³`, `natura filius irae⁴`) are both above the column foot, while n. 5 (`poena mitissima⁵`) opens the right column. Capitulum break (2 | 3) therefore falls **inside the left block**. Right block nn. 4–9, n. 9 (`B homo.`) complete | **CLEAN** |
| 6 | `p3-c5` → `p3-c6` | p. 235 (mid-page, left col.) | c5 tail `…Ut enim eos reduceret ad medium, abundantius declinavit ad extremum.` = raw L44075, immediately above `Cap. VI.` (L44077) | 1 / 6 (7). Blocks 2/5; **column anchors also 2/5** (n. 2 `…natura corrupta corrumpit personam²` closes Cap. VI's first paragraph, still in the left column) — they coincide, and the capitulum break (1 | 2) falls **inside the left block**. Gutter runover POSITIVE at n. 2, broken at a word boundary (`…in Adam, et natura` / `egens facta omnes personas…`) — logged on `p3-c6`'s ledger line; rendered joined | **CLEAN** |
| 7 | `p3-c6` → `p3-c7` | **leaf crossing** p. 235 → p. 236 | c6 tail `…quod « peccatum originale non transmittit ad posteros propagatio, sed libido ».` = raw L44175, the last body line of p. 235 (confirmed on the band: it is the last line of p. 235's right column); p. 235's footer register follows, then folio `236` + running head `BREVILOQUII PARS III. C. VII. VIII.`, then `Cai>. VII.` (L44228). **The white space below p. 235's right column was not used as evidence** — the boundary is set from the `Cap. VII.` heading at the head of the next leaf | p. 235 total **7**; n. 7 (`Potius Fulgentius in libro de Fide ad Petrum, c. 2. n. 16 Cfr. supra pag. 170, nota 3.`) **closes complete — nothing forwarded into p. 236**; p. 236's register restarts at n. 1 | **CLEAN** |
| 8 | `p3-c7` → `p3-c8` | p. 236 (mid-page, right col.) | c7 tail `…ut conciperetur et nasceretur ille, de quo ipse procedebat[^p236-6] ».` = raw L44321, immediately above `C.\p. VIII.` (L44323) | 6 / 1 (7). Blocks 4/3, column anchors 4/3 — coincide; capitulum break (6 | 7) falls **inside the right block**. Gutter runover POSITIVE at n. 4, broken at a word boundary (`…pro *motus autem* substituunt *actus*` / `*autem sive motus*, et subinde…`) — logged on `p3-c7`'s line; c8 inherits only n. 7 (`Vers. 14. seq.: Unusquisque vero tentatur etc.`), verified against the band | **CLEAN** |
| 9 | `p3-c8` → `p3-c9` | p. 237 (mid-page, right col.) | c8 tail `…secundum explanationem Doctoris praecipui, scilicet Augustini, duodecimo de Trinitate[^p237-9].` = raw L44486, immediately above `Cap. LX.` (= Cap. IX, L44488) + `De origine et distinctione capitalium peccatorum.` (L44490) | **9 / 0 (9).** Capp. VIII **and** IX both sit on p. 237, yet **all nine notes are Cap. VIII's and Cap. IX claims none** — confirmed on the band: the right block's last entry is n. 9 (`Cap. 12. n. 17. seq.`), which is c8's `[^p237-9]`, and c9 carries no p. 237 label. **Left block under-runs by three**: blocks 3/6 (n. 3 closes complete, right opens **numbered** ⁴ → NEGATIVE), but anchor ⁶ (`…non tamen directe est *contra* legem⁶`) is still in the **left** column, so column anchors divide 6/3 | **CLEAN** |
| 10 | `p3-c9` → `p3-c10` | p. 238 (mid-page, right col.) | c9 tail `…respectu quorum dicuntur peccata capitalia, quasi capita, ex quibus alia manant quam plurima.` = raw L44640, immediately above `C.\p. X.` (L44642). On the band, `CAP. X.` + `De origine et qualitate peccatorum poenalium.` open p. 238's right column | 7 / 1 (8). Blocks 4/4 and column anchors 4/4 — coincide, the split falling **inside** n. 4 (broken **mid-word**, `Amor ergo… fu-` / `giens quod ei adversatur, timor est.`). Gutter runover POSITIVE at n. 4, logged on `p3-c9`'s line. n. 8 (`Edd., excepta 2, cum paucis codd. *poenae*.`) is c10's, anchored `sunt poena⁸ peccati` in the right column, and closes the page complete | **CLEAN** |
| 11 | `p3-c10` → `p3-c11` | **leaf crossing** p. 239 → p. 240 | c10 tail `…Et sic patet, quomodo, pro quanto et quare aliquid simul dicatur *peccatum* et *poena peccati*.` = raw L44807, the last body line of p. 239 (confirmed on the band as the last line of p. 239's right column); p. 239's footer register follows, then folio `240` + running head, then `Cap. XI.` (L44861) at the head of p. 240's left column. Again the boundary is set from the heading, not from the white space below p. 239's right column | p. 239 total **9**, **all nine Cap. X's**; n. 9 (`Edd., excepta 2, *dicitur respectu praecedentis culpae*.`) **closes complete — nothing forwarded into p. 240**; p. 240's register restarts at n. 1 | **CLEAN** |
| 12 | `p3-c11` → `p4-c1` | p. 241 (mid-page, **left** col.) — **the Pars III/IV seam** | c11 tail `…cui mediatori Domino nostro omnis *honor et gloria in saecula saeculorum. Amen*[^p241-2].` = raw L45033, immediately above `PARS QUARTA` (L45036) + `De incarnatione Verbi.` (L45039) + `Cap. 1.` (L45042). The `Amen.`-shaped ending is corroborated by the following full-width display heading, **not** accepted on its own | **2 / 8 (10).** See the dedicated section below | **CLEAN** |

**12 boundaries swept (9 mid-page, 3 leaf crossings). 12 CLEAN, 0 DEFECT.**

No tail in the range fails to parse (no cascade-merge signature), and no chunk
was written short at a column foot: every one of the three leaf crossings and
both blank-paper-looking column feet inside the pars (p. 231 right column ending
at `…poena inflicta⁷` with white space below, p. 233 left column ending high
under a tall footer register) was resolved from the **next heading**, and in every
case the unit did continue past the white space exactly as the `p2-c4` rule warns.

---

## Footer accounting — every page re-read off the bands

| p. | left block | right block | plate's last numbered entry (band) | `KNOWN_TOTALS` | agree? | ownership (by anchor) |
|---|---|---|---|---|---|---|
| 230 | … | nn. 6–7 | 7 (`Hugo a S. Vict., loc. cit.` … `cum uno alteroque cod. diligenter.`) | 7 | ✅ | `p2-c11` 1 · `p2-c12` 2–7; nothing forwarded |
| 231 | nn. 1–3 | nn. 4–7 | 7 (`De his tribus agitur in hoc et 2 seqq. capp.; … de actuali c. 8-11.`) | 7 | ✅ | `c1` 1–6 · `c2` 7 |
| 232 | nn. 1–5 | nn. 6–9 | 9 (`Partis II. c. 11. — Inferius post *sed* edd. …`) | 9 | ✅ | `c2` 1–7 · `c3` 8–9 |
| 233 | nn. 1–4 (n. 4 broken) | n. 4 cont. + n. 5 | 5 (`Boeth., IV. de Consol. prosa 6` … `quam laetari in damno aequitatis.`) + signature `30` | 5 | ✅ | `c3` 1–3 · `c4` 4–5 |
| 234 | nn. 1–3 | nn. 4–9 | 9 (`B *homo*.`) | 9 | ✅ | `c4` 1–2 · `c5` 3–9 |
| 235 | nn. 1–2 (n. 2 broken) | n. 2 cont. + nn. 3–7 | 7 (`Potius Fulgentius in libro de Fide ad Petrum, c. 2. n. 16 Cfr. supra pag. 170, nota 3.`) | 7 | ✅ | `c5` 1 · `c6` 2–7; nothing forwarded |
| 236 | nn. 1–4 (n. 4 broken) | n. 4 cont. + nn. 5–7 | 7 (`Vers. 14. seq.: Unusquisque vero tentatur etc.`) | 7 | ✅ | `c7` 1–6 · `c8` 7 |
| 237 | nn. 1–3 | nn. 4–9 | 9 (`Cap. 12. n. 17. seq.`) | 9 | ✅ | all `c8`; Cap. IX opens here and claims none |
| 238 | nn. 1–4 (n. 4 broken mid-word) | n. 4 cont. + nn. 5–8 | 8 (`Edd., excepta 2, cum paucis codd. *poenae*.`) | 8 | ✅ | `c9` 1–7 · `c10` 8 |
| 239 | nn. 1–4 (n. 4 broken) | n. 4 cont. + nn. 5–9 | 9 (`Edd., excepta 2, *dicitur respectu praecedentis culpae*.`) | 9 | ✅ | all `c10`; nothing forwarded |
| 240 | nn. 1–4 (n. 4 broken at punctuation) | n. 4 cont. + nn. 5–9 | 9 (`Edd. cum aliquot codd. praefigunt *peccatis*.`) | 9 | ✅ | all `c11` |
| 241 | nn. 1–5 + signature | nn. 6–10 | 10 (`Vide supra pag. 183, nota 3.` … `Deus factus est similis homini etc.`) + signature `31` | 10 | ✅ | `c11` 1–2 · `p4-c1` 3–10 |

**No page's true total differed from `KNOWN_TOTALS`. No register was dropped,
none double-claimed, and no page in scope is unowned.** The raw's own footer
blocks, counted independently as a cross-check, agree on p. 230 (7), p. 235 (7)
and p. 239 (9) — but the bands are the authority and the raw was not relied on.

**Runover ledger, re-derived from the bands rather than adopted.** Positive
gutter runovers in scope: **p. 233 n. 4, p. 235 n. 2, p. 236 n. 4, p. 238 n. 4,
p. 239 n. 4, p. 240 n. 4** — six, exactly the six lines the ledger carries for
`p3-c3`, `p3-c6`, `p3-c7`, `p3-c9`, `p3-c10`, `p3-c11`. Negative and confirmed
negative on the band (right block opens numbered): **pp. 230, 231, 232, 234, 237,
241**. **No page-crossing runover anywhere in pp. 231–241**, consistent with
`check-vol5-census.py`'s five page-crossers (pp. 206, 212, 246, 253, 277), none of
which is in range. Each positive is logged exactly once; no double-count.

**Digit and siglum reads worth recording** (both confusion classes are live on
these leaves, as CLAUDE.md warns, and neither dominates):
p. 231 n. 1 `II. Sent. d. 25.` — the raw prints `d. 23`, the band prints 25;
p. 231 n. 5 `c. 19. n. 53` and `de Vera Relig. c. 14. n. 27` and `pag. 188` — all
serif `1`s that print like `4`; p. 238 n. 2 `Eccli. 10, 15` (the raw's `10, 13`);
p. 241 n. 9 `de Vera Relig. c. 16. n. 30. seqq. et c. 55. n. 110` — the `55` and
the `110` both print in the `3`/`5` and `1`/`4` serifs and are correct in the
chunk. **No transcription change follows from any of these** — the chunks already
carry the correct readings, which is what this pass was checking.

---

## The p. 241 seam into Pars IV — read with particular care

p. 241 is shared between `bon-brev-p3-c11` (Pars III, Cap. XI) and
`bon-brev-p4-c1` (Pars IV, Cap. I), and it is the one page in the range where
**three divisions all fall in different places**:

- **Capitulum/pars division: after n. 2.** nn. 1–2 anchor in Cap. XI's closing
  paragraph — n. 1 (`Vide supra c. 9. — Inferius post *a qua* edd. addunt *quidem
  impoenitentia finali*, L M V autem prosequuntur: *nullus moriens in peccato
  mortali potest liberari…*`) at `omne peccatum initium sumit a superbia¹`, and
  n. 2 (`Epist. I. Tim. 1, 17. Ibid. 2, 5: Unus et mediator Dei et hominum, homo
  Christus Iesus.`) at `omnis honor et gloria in saecula saeculorum. Amen²`.
  nn. 3–10 anchor in PARS QUARTA Cap. I.
- **Footer-block division: after n. 5.** The left block runs nn. 1–5 and closes
  complete (n. 5 `…quae etiam inferius post *repararet* addunt *reparanda*.`)
  followed by the printer's signature `S. Bonav. — Tom. V.`; the right block opens
  **numbered** ⁶ — so the p. 241 gutter runover is **NEGATIVE**, tested from the
  band and not inferred.
- **Column division: after n. 7.** The left column carries the end of Cap. XI, the
  full-width `PARS QUARTA / De incarnatione Verbi` display heading, and Cap. I
  down to `…accipiat *formam servi*⁷?`; anchor ⁸ onward is in the right column
  (`…non recuperaret statum excellentiae¹⁰` is visibly right-column).

So the left block **under-runs the column division by two notes**, and the pars
boundary falls **inside the left block**, between nn. 2 and 3 — three independent
structures, none coinciding. The running head on p. 241 reads `PARS IV. C. I.`
though the top of the page is still Pars III's body; the boundary was set from the
`PARS QUARTA` / `Cap. 1.` headings in the raw, never from the head.

**What I certify about the seam:**

1. `p3-c11`'s tail is the last body of Pars III and is contiguous with the
   `PARS QUARTA` display heading in the raw (L45033 → L45036), with nothing
   between but blank lines.
2. p. 241's register totals **10**, matching `KNOWN_TOTALS`, and divides
   **2 (`p3-c11`) / 8 (`p4-c1`)** by anchor.
3. n. 10 **closes complete on p. 241** (`…E brevius concludit *Deus factus est
   similis homini* etc.`), followed by the signature `31`. **Nothing is forwarded
   from p. 241 into p. 242**, and p. 242's register (total 6) opens its own n. 1.
4. All ten p. 241 entries were compared word-for-word against the two blocks;
   `p4-c1`'s `[^p241-3]` … `[^p241-10]` and `p3-c11`'s `[^p241-1]`–`[^p241-2]`
   reproduce the plate, including n. 9's `c. 55. n. 110`.
5. The `KNOWN_TOTALS` note for p. 241 describing this as "split by PARS, not by
   block" is **confirmed on the band**, and was re-derived rather than quoted
   (CLAUDE.md: a structural generalisation is the least reliable line in any
   `## Notes`).

---

## Observations (no defect, no repair, nothing edited)

1. **`<!-- page N -->` markers round to paragraph boundaries in BOTH directions,
   so an anchor's page label need not match its enclosing marker region.** This is
   the frozen corpus convention ("page breaks … at the right paragraph
   boundaries"), it is applied **uniformly across all eleven Pars III chunks**, and
   it is not drift. Recorded because it is easy to misread as a mis-assignment at
   a seam. Clearest instances: `p3-c5` places `<!-- page 235 -->` before the
   paragraph `Postremo, quia *carentia* huius iustitiae…`, whose **first two lines
   in fact stand at the foot of p. 234's right column** (band-confirmed, with the
   marginal gloss `Poena parvulorum` beside them); and, in the other direction,
   `p3-c9` places `[^p238-1]` and `p3-c10` places `[^p239-1]`–`[^p239-3]` **above**
   their respective page markers, because the paragraphs carrying them begin on the
   previous leaf. The **labels** are right in every case, which is what
   `check-vol5-apparatus.py` verifies, and the ownership table above is derived
   from the labels and the bands, not from the markers.
2. **`[?]` flags in scope: zero.** All eleven chunks' `## Notes` record
   `No [?] flags`, and a grep for live inline `[?]` markers in `vol5/bon-brev-p3-*`
   returns none (the eleven hits are the "No `[?]` flags" sentences themselves).
3. **Two mid-column `Cap. N.` headings destroyed a majority of the gutter windows**
   (pp. 234 and 238, eight and nine windows lost). CLAUDE.md's gutter-rule 2
   footnote — added from p. 263 in Pars V — is if anything understated for Pars III:
   on these leaves the *default* 45–92 % window is among the survivors, but on
   p. 240 it is the one that fails outright. There is no window that is safe by
   position; only the run width decides.
4. **Raw-quality grade, given per page and per region as required.** p. 234: body
   **clean above** the `C.\p. V.` heading (Cap. IV's closing paragraphs run as
   continuous lines, L43916–43927) and **degraded below it** (from L43938 the raw
   interleaves marginalia and blank lines into the body — `De coipa / origLnali.`,
   `T>emenii7iam quadrupliccm poenam`). p. 237: the mirror — body **degraded above**
   the `Cap. LX.` heading (L44452–44458 splice `Coroi- / larium` into the text) and
   **clean below it** (L44492–44493). Footers on both pages are, as always in Vol V,
   numeral-less and were read only from the bands. p. 231 reproduces its documented
   shape: body clean, footer wrong in at least two digits.

## A wording discrepancy I would raise, but did not touch

**`[?] tools/check-vol5-apparatus.py`, the `KNOWN_TOTALS` comment for p. 239.**
The comment calls p. 239 "a one-note **OVERRUN**", and CLAUDE.md's list of pages
where "the left block … can **overrun** the column division" also names p. 239
alongside pp. 220, 221, 226, 233. On the band the p. 239 relation is the
**opposite direction** to p. 233's: the left block holds nn. 1–4 while the left
**column** carries anchors nn. 1–6 (anchor ⁶ at `malum autem *poenae* est affectio
involuntaria⁶` is plainly in the left column), so the block break falls **two
notes above** the column division — the same shape as pp. 234 and 237, which
CLAUDE.md classes as **under**-runs. The comment's own per-note data ("nn. 1–6 ALL
anchor in the LEFT column, so nn. 5–6 anchor left and print right") is **correct
and agrees with my read**; it is only the one-word label beside it that points the
wrong way — precisely the "summary contradicts its own data one paragraph away"
failure CLAUDE.md froze a rule about on 2026-07-30. **No corpus text is affected
and no chunk is wrong**; nothing was edited. Suggested repair for whoever owns the
file: relabel p. 239's gloss as a **two-note under-run** and drop p. 239 from
CLAUDE.md's over-run list, leaving pp. 220, 221, 226, 233 there.

---

## Disposition

**PASS 3 CLEAN for Pars III. Zero defects, zero repairs, no chunk edited,
`KNOWN_TOTALS` unchanged, no git write command run.**

- The **incoming** seam `p2-c12 → p3-c1` is certified clean **from the Pars III
  side, independently derived**: p. 230's register is exhausted by `p2-c12`
  (n. 7 complete on the page), and `p3-c1` correctly opens its own p. 231 register
  at n. 1 beneath the `PARS TERTIA` display heading.
- The **outgoing** seam `p3-c11 → p4-c1` is certified clean: p. 241 divides 2/8 by
  anchor across the pars boundary, its register totals 10 as recorded, n. 10 closes
  complete on the page, and nothing is forwarded into p. 242.
- One `[?]`-grade flag is raised, and it is **documentation only** (the p. 239
  "overrun" label in `check-vol5-apparatus.py`'s comment and in CLAUDE.md's page
  list). It affects no chunk and blocks nothing.
