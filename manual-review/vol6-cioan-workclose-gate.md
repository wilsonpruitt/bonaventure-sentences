# Vol VI — *Collationes in Evangelium S. Ioannis*, WORK-CLOSE GATE at p. 634 (printed pp. 535–634) — CLOSED

**STATUS: CLOSED 2026-11-07.** Wilson ruled the docket (2026-11-07): **all proposed rulings 137–152 approved as recommended**, with the
four close calls answered explicitly (137 "Appendix"; 141 c5 Coll. XXI ¶ 2 only; 144 this work only, a corpus pass queued; 147 D7 D2 W23
W41 W37 now, D1 D4 D5 D6 queued; 148 the scoped edit without the genitive sigla). Binding summary: `manual-review/vol6-pilot-setup.md`
§ COLLATIONES WORK-CLOSE GATE. **No transcription defect.** Three conformance classes found by census were conformed (W21's residue,
"Holy Ghost" ×2, ruling 101's spellings), one breadcrumb was decided, five resolver jobs were run, 14 PRINTED_SLIPS rows were added, and
`tools/authorities.json` was edited once. **No `**La.**` half and no `## Latin` line changed.**

Ruling 123 placed this gate at p. 634, the close of the work. ⛔ **The ONE deploy for the work follows it as its own hard stop**
(Wilson's per-action OK), and the push is a separate ask. **Neither has been done.**

**Procedure:** a read-only agent ran the first half (`03acea3`): baseline, passes 1–3 (`manual-review/vol6-cioan-workclose-gate-passes.md`,
all CLEAN) and the evidence sheet (`…-evidence-sheet.md`, proposed rulings 137–152 with exact sites). Both are kept as the evidence
record and are not repeated here. Wilson ruled; the second half applied the edits in the resume note's housekeeping order, re-ran the
suite against the baseline and ran Pass 4.

**Scope: 22 chunks, pp. 535–634 with no gap, 889 numbered apparatus entries, 22 `tr-` notes.**

## BASELINE (passes file § BASELINE)

citations 35,240 records / QA 211 / anaphora unresolved 286 / printed slips 6, 0 stale (ledger + QA report byte-identical) ·
authorities 17,118 (98.0 % to a work, byte-identical) · index 78 books / 21,412; crossref 1,836 / 11,211 · content 2,317 / 2,317 ·
live flags vol6 199, none live, 2 exempt · apparatus 199 / 6,500, all passed · census vol5 167/167, vol6 199/199, 317 runovers (292 /
25); in scope 35 (32 / 3) · style 11 / 6 / 2,318, zero ours · `validate-chunk.py` 22 / 22.

## PASSES 1–3: CLEAN

Pass 1 none live · Pass 2 every tool clean, parity 22/22, registry 22/22; the census found three conformance classes (W21's five "sick",
"Holy Ghost" ×2, the ruling-101 spellings) · Pass 3 100 pages / 889 entries owned once, 21 seams as built, 35 runovers = ledger;
p. 632 n. 3's anchor read on the plate.

## RULINGS (Wilson, 2026-11-07) AND EDITS APPLIED

| # | ruling | applied | lines |
|---|---|---|---|
| 137 | type-first `appendix` → "Appendix" (W57) | `buildWorkChunkTitle` + 2 comments (`site/scripts/build-content.mjs`). The built titles of the 22 `bon-cioan-` chunks were diffed: **one** changed, `Cap. 22` → `Appendix` | 3 code lines |
| 138 | W18 / W58 ratified | none | 0 |
| 139 | W21's residue conformed | c11 L215 (John 4:46 *infirmabatur*), L220 (*infirmus*), L226 ×2 (*infirmi … infirmatur*, the lemma John 11:3), L230 (Ecclus. 7:39 *infirmum*) → "infirm". *languens* ("such a sick man") and IV Kings 1:2 *aegrotavit* are other words and stand | **4** |
| 140 | ruling-93 families ratified | none | 0 |
| 141 | W1 by passage | c5 L181 (Coll. XXI ¶ 2) → "Heal thou the contritions thereof"; L157 (Coll. XX) keeps "breaches" | **1** |
| 142 | W12 / W13 ratified | none | 0 |
| 143 | "Holy Ghost" → "Holy Spirit" | c21 L333 (John 3:5), L370 (Acts 7:55) | **2** |
| 144 | judgement / recognize, this work only | **40 "judgment(s)" on 18 lines** (c1 L292, L297, **L301** · c7 L132, L134, L136, L138, L142, L147, L149, L151, L153, L155, L157, L203, L249 `**En.**` · c12 L239 · c13 L135) + **4 "recognise" on 3 lines** (c3 L147 ×2, c8 L252, c18-19 L132). ⚠ c1 L301, the capitalised `> ` verse line *Judgement, parity, precedence…*, was outside the sheet's 39 / 17 (its census was lower-case only). It is within the ruling's intent, so it was applied. A corpus-wide pass is QUEUED, not done | **21** |
| 145 | 14 PRINTED_SLIPS rows | `tools/build-citations.py`. Each row was checked to match exactly one record, before the resolver jobs and again after them (QA: 20 annotated, 0 stale) | ~45 tool lines |
| 146 | index slips recorded, no row | the list is in ruling 146 | 0 |
| 147 | D7 D2 W23 W41 W37 now; D1 (4) D4 D5 D6/W51 queued | `tools/build-citations.py` + `tools/scripture-books.json` (`chunk_pattern`); ledger diffs below | tool |
| 148 | the scoped `authorities.json` edit | 6 entries (4 works added, 1 abbreviation added, 2 new authors). The genitive sigla were NOT added (a queued yes/no) | table |
| 149 | W53 ratified | none | 0 |
| 150 | record-only block ratified | none | 0 |
| 151 | housekeeping | `complete: true` (`site/scripts/build-progress.mjs` L190); Pass 4 below | 1 |
| 152 | close | suite below | — |

Each edited chunk carries one dated `**GATE (p. 634 work-close …)**` line at the end of its `## Notes` (11 chunks: c1 c3 c5 c7 c8 c11 c12
c13 c18-19 c21 app). c11's GATE line notes that its "80 Latin tokens" W21 line is now true of the English too.

**Diff verification (against `03acea3`):** `git diff --numstat vol6` = **50 insertions / 28 deletions**. That is the 28 English lines above
(27 body, 1 `**En.**` half) plus 11 GATE lines, each with its blank line. A script checked that every changed line lies between
`## English` and `## Notes` and that none starts `**La.**`: **0 `**La.**` halves, 0 `## Latin` lines, 0 frontmatter lines changed.** The
citation and authority scanners read only the Latin, so the English edits moved no ledger record. Every ledger delta below comes from a
tool job.

## RESOLVER JOBS (ruling 147): before/after ledger diffs

Rows were compared on chunk · section · anchor · class · subclass · raw · target · confidence · resolution. Each job was run on its own,
cumulatively, to a scratch ledger and diffed against the previous step. The default-path build was run once, at the end.

| step | job | records | what moved |
|---|---|---|---|
| — | baseline | 35,240 | — |
| 1 | **D7**: `HEX_COLLAT_RE` `Hexa[eë]m\w*\.\s*(\(tom\. V\.\)\s*)?collat\.\s*N` in `scan_work`, superseding the cap-less `Hexaem.` record at the same position; `hexaemeron` `chunk_pattern` `bon-hex-coll{coll}` → **`bon-hex-c{coll}`** in the same diff | **35,323 (+83)** | **+83 crossrefs → `bon-hex-cN`**, plus **1 refined** `work:hexaemeron` → chunk (`bon-serm-s3` p. 555 n. 9). By work: Vol V 73 (`bon-serm` 43 · `bon-don` 23 · `bon-praec` 7); Vol VI 11 (`bon-ioan` 7 · `bon-sap` 3 · `bon-cioan-c1` 1), the refine included. Crossref `work` 217 → 216; **`forward` stays 3**. ⚠ **Two cross-chunk anaphora moved onto the new records**: `bon-cioan-c1` p. 541 n. 6 `ibid.` (Aristotle's *De partibus*; was `Ps 73:12` A, now `bon-hex-c1`) and `bon-serm-s4` p. 568 n. 5 `ibid. c. 12, 36` (was `bon-sent-III-d35-a1-q3`, now `bon-hex-c9`). Both were **wrong before and are wrong after**. They are the D1 class and are left for the queued session; the first accounts for scripture −1 / crossref +1. The ruling-116 guard needed no change: it has read `Hexa[eë]m` over the whole clause since the W4 fix |
| 2 | **W23**: `coll\.` (lower case only) admitted by `CIOAN_COLL_RE` | **35,324 (+1)** | `bon-cioan-c11` p. 589 n. 4 `coll. XVIII.` → `bon-cioan-c4` (chunk). Nothing else in the corpus matches |
| 3 | **W41**: `POINT_VERSE_RE`. A chapter-level `Book C` followed by `. V` reads V as the verse, provided it is on the same line and not followed by `Sent`, `q`, `d`, `a`, `n`, `c`, `p`, `pag`, `tom`, `text`, `lib`, `cap`, `art`, `dist` or `nota` | **35,325 (+1)** | **38 records refined chapter → verse, C → A**, plus **4 anaphora that follow them**. **+1 added**: `bon-sent-II-d8-p1-dubia` n. 4 `Num. 12. 8`, which `require_verse` had dropped. The sheet estimated 29; every site was read, and all are genuine verses (`Ps. 10. 7. et Apoc.`, `Col. 3. 1. seq.`, `Num. 12. 8, ubi Vulgata …`). ⚠ **One false positive was caught and excluded.** `bon-eccl-c8-v9-13` already has a false body record: *…de Esau et Iacob.* followed by the reply numerals `1. 2.` (`Iac 1`, C). This job would have hardened it to `Iac 1:2` A. The point-verse is never read across a line break, so that record is unchanged; it remains a known false record, noted in that chunk's Notes |
| 4 | **W37**: `IBID_Q_RE`. `ibid. [a. N.] q. N` takes its own article and question, but only when the antecedent is the locus immediately before it in the same chain (≤ 60 chars, no parenthesis or dash between, the antecedent naming a question) | **35,326 (+1)** | **15 records retargeted to the question printed.** 1 record that de-duplication had collapsed now stands on its own (`bon-sent-IV-d18-p2-dubia` n. 1 `ibid. q. 1`). 6 authority-class records now carry their `q. N` in the raw (targets unchanged, still excluded). Every retarget was read against its note (list below). A first, unrestricted version moved 48 records, put 8 into `dangling` and raised QA 211 → 216, because it reached far-off antecedents (the D1 class). It was narrowed before the run that counts |
| 5 | **D2**: `primae / secundae / tertiae` immediately before the body form `Ioannis` → `1Ioan` / `2Ioan` / `3Ioan` | **35,333 (+7)** | **110 body records retargeted `Ioan` → `1Ioan`** (all *primae*; no *secundae / tertiae Ioannis* occurs), plus **4 anaphora that follow them**. **7 records** that had been collapsed into a same-anchor Gospel record now stand on their own. By work: `bon-ioan` 40 · **`bon-cioan` 25** · `bon-sap` 18 · Sentences 23 · `bon-eccl` 7 · `bon-serm` 5 · `bon-qmt` 2 · `bon-hex` 1. The sheet's nine named sites in this work were checked (p543-1 → `1Ioan 4:16` B … p613-5 → `1Ioan 2:23` B). QA unchanged |

**W37: every changed record (after):**
`bon-cioan-c17` apparatus:p610-1 `ibid. q. 2` → `bon-sent-II-d27-a2-q2` · `bon-hex-c9` apparatus:p376-3 `ibid. a. 2. q. 2` → `bon-sent-II-d1-p1-a2-q2` · `bon-qmt-q2-a2` apparatus:p67-4 `ibid. q. 1` → `bon-sent-I-d8-p2-a1-q1` · `bon-sent-I-d27-p2-a1-q2` scholion `ibid. q. 6` → `bon-sent-I-d18-a1-q6` · `bon-sent-I-d29-a2-q1` scholion `ibid. q. 1` → (authority, excluded) · `bon-sent-I-d38-a2-q1` scholion `ibid. a. 2. q. 1` → `bon-sent-I-d40-a2-q1` · `bon-sent-I-d7-a1-q4` scholion `ibid. a. 3. q. 1` → `bon-sent-I-d1-a3-q1` · `bon-sent-I-proem-q1` scholion `ibid. q. 4` → `bon-sent-III-d23-a1-q4` · `bon-sent-II-d12-dubia` apparatus:8 `ibid. a. 2. q. 1` → `bon-sent-II-d2-p1-a2-q1` · `bon-sent-II-d26-a1-q5` apparatus:15 `ibid. a. 1. q. 2` → `bon-sent-II-d17-a1-q2` · `bon-sent-II-d28-a1-q1` scholion `ibid. q. 2` → (authority, excluded) · `bon-sent-II-d3-p1-a1-q2` apparatus:14 `ibid. a. 2. q. 3` → `bon-sent-II-d2-p1-a2-q3` · `bon-sent-II-d35-a2-q2` apparatus:5 `ibid. q. 2` → `bon-sent-I-d3-p1-a1-q2` · `bon-sent-II-d7-p1-a2-q1` scholion `ibid. q. 5` → (authority, excluded) · `bon-sent-II-d8-p2-a1-q6` scholion `ibid. q. 2` → (authority, excluded) · `bon-sent-III-d14-a2-q1` scholion `ibid. q. 2` → (authority, excluded) · `bon-sent-III-d15-a1-q1` scholion `ibid. q. 4` → (authority, excluded) · `bon-sent-III-d26-a1-q5` apparatus:15 `ibid. a. 2. q. 2` → `bon-sent-III-d23-a2-q2` · `bon-sent-IV-d14-p2-dubia` apparatus:43 `ibid. a. 1. q. 1` → `bon-sent-II-d34-a1-q1` · `bon-sent-IV-d18-p2-dubia` apparatus:1 `ibid. q. 1` → `bon-sent-II-d25-p2-a1-q1` (formerly collapsed) · `bon-sent-IV-d29-a1-q1` apparatus:16 `ibid. q. 3` → `bon-sent-IV-d4-p1-a2-q3` · `bon-sent-IV-d6-p2-a2-q1` apparatus:5p153 `ibid. q. 1` → `bon-sent-IV-d4-p1-a2-q1`

**W41: every changed record (after):**
`bon-cioan-app` p632-4 `I. Petr. 4. 7` → `1Petr 4:7` · `bon-cioan-c18` p613-1 `Ps. 10. 7` → `Ps 10:7` · `bon-cioan-c4` p559-4 `Eccli. 26. 15` → `Eccli 26:15` · `bon-don-c9` p499-5 `Col. 3. 1` → `Col 3:1` · `bon-eccl-c5-v9-11` p47-7 `I. Tim. 4. 7` → `1Tim 4:7` · `bon-hex-scholion` latin_body `II. Cor. 4. 4` → `2Cor 4:4` · `bon-ioan-c18-v1-3` p478-10 `Luc. 22. 39` → `Luc 22:39` · `bon-ioan-c6-v22-33` p325-15 `Exod 13. 9` → `Exod 13:9` · `bon-ioan-c6-v60-72` p337-7 `Ioan. 11. 27` → `Ioan 11:27` · `bon-qpe-q2-a1` p132-4 `II. Cor. 4. 8` → `2Cor 4:8` · `bon-sap-c1` p111-9 `Eccli. 30. 24` → `Eccli 30:24` · `bon-sap-c15` p207-9 `Ier. 4. 22` → `Ierem 4:22`, `Sap. 13. 10` → `Sap 13:10` · `bon-sap-c4` p135-2 `II. Cor. 11. 3` → `2Cor 11:3` · `bon-sent-I-d41-littera` 9 `I. Cor. 12. 6` → `1Cor 12:6` · `bon-sent-II-d17-a1-q1` 6 `Tim. 6. 16` → `Tim* 6:16` · `bon-sent-II-d18-a1-q3` scholion `Cor. 13. 9` → `Cor* 13:9` · `bon-sent-II-d22-a2-q3` 22 `Gen. 19. 33` → `Gen 19:33` · `bon-sent-II-d26-a1-q2` scholion `II. Petr. 1. 2` → `2Petr 1:2` · `bon-sent-II-d26-littera` 13 `Cor. 4. 7` → `Cor* 4:7` (+ n. 15 `ibid.`) · `bon-sent-II-d30-a3-q1` 20 `I. Cor. 3. 7` → `1Cor 3:7` · `bon-sent-II-d42-littera` 12 `Deut. 23. 23` → `Deut 23:23` · `bon-sent-II-d44-a2-q1` 17 `Exod. 22. 18` → `Exod 22:18` · `bon-sent-II-d8-p1-dubia` 4 `Num. 12. 8` → `Num 12:8` (added) · `bon-sent-III-d1-a2-q2` 4 `Psalm. 68. 3` → `Ps 68:3` (+ n. 5 `loc. cit.`) · `bon-sent-III-d1-a2-q4` 4 `Luc. 5. 31` → `Luc 5:31` · `bon-sent-III-d11-a1-q2` 11 `I. Petr. 2. 21` → `1Petr 2:21` · `bon-sent-III-d14-a3-q2` p322-3 `Hebr. 5. 8` → `Hebr 5:8` · `bon-sent-III-d20-a1-q5` p427-4 `Ps. 21. 7` → `Ps 21:7` (+ `loc. cit.`) · `bon-sent-III-d21-a2-q2` p444-4 `Ps. 15. 10` → `Ps 15:10` · `bon-sent-III-d25-littera` p533-2 `Cor. 13. 8` → `Cor* 13:8` · `bon-sent-III-d28-a1-q5` 17 `Sap. 6. 21` → `Sap 6:21` · `bon-sent-III-d9-a1-q5` 4 `II. Cor. 6. 16` → `2Cor 6:16` · `bon-sent-IV-d14-p2-a1-q1` 1 `II. Reg. 12. 13` → `2Reg 12:13` · `bon-sent-IV-d15-p2-a2-q2` 6 `Matth. 5. 44` → `Matth 5:44` · `bon-sent-IV-d4-p2-a1-q2` 1b `I. Cor. 13. 3` → `1Cor 13:3` · `bon-sent-IV-d4-p2-a2-q3` 8 `Rom. 9. 13` → `Rom 9:13` · `bon-sent-IV-d6-p1-a1-q4` 8 `Deut. 20. 8` → `Deut 20:8` · `bon-sent-IV-d9-a1-q1` 3 `Cor. 11. 29` → `Cor* 11:29` (+ n. 5 `ibid.`)

**Queued, NOT run (ruling 147):** D1 + (4) (cross-note anaphora at A or to a wrong chunk; *Ioannem* 33 + 12, plus the two that D7 moved),
D4 (roman book numeral not emitted; 144 in this work), D5 (body ordinals with no record) and D6 / W51 (bare `Vers. N; ibid. v. M`, 28
corpus-wide; p. 622 n. 7 is ours). These are for one resolver session after the deploy.

## AUTHORITIES (ruling 148): the one table edit

`tools/authorities.json`:
- Bernard: `sermo-in-assumptione` ("Serm. in Assumt. B. Mariae", "Serm. in Assumpt. B. Mariae") and `meditationes-piissimae` (pseudo; it
  lands only with the genitive siglum).
- Augustine: `manuale` (pseudo).
- Jerome: `in-ieremiam` + "Comment. in Ier." (never bare "in Ier.", which false-matches *in Ierusalem*).
- NEW author `juvenal` (sigla `Iuvenal.`, `Iuvenalis`; work `satirae`, "Satyra", "Sat.").
- NEW author `vitae-patrum` (sigla `de Vitis Patrum`, `Vitae Patrum`, `Vitis Patrum`; `default_work`).

**17,118 → 17,127 (+9, 0 removed); to a work 16,776 → 16,785.** All nine added records were read (this is the fresh sample):
- app p. 633 n. 7 (Jerome)
- c12 p. 596 n. 4 (Juvenal)
- c17 p. 609 n. 4 (Bernard, inter opera)
- c17 p. 610 n. 8 (*Vitae Patrum*)
- `bon-ioan-c17-v24-26` p. 477 n. 1 (*Manuale*)
- `bon-sap-c5` p. 143 n. 2 (Jerome)
- `bon-sent-II-d38-a1-q4` n. 4 (Juvenal)
- `bon-sent-IV-d20-p1-a1-q5` n. 8 (*Vitae Patrum*)
- **`bon-sent-III-d9-a1-q6` n. 11** (*Vitae Patrum*): the one beyond the sheet's +8, `Libr. V. de Vitis Patrum, libell. 15. n. 70`, genuine.

**Queued yes/no for Wilson:** the genitive sigla `Dionysii`, `Augustini`, `Bernardi` (+196 / −4 corpus-wide). This needs a full
before/after sample.

## CLOSE: suite re-run against the baseline

Run 2026-11-07 on default paths, in the build order citations → authorities → index-json → content → index-json → content. The second
index pass is the one cited.

| check | after | baseline | delta, explained |
|---|---|---|---|
| `build-citations.py` | **35,333 records** (scripture 21,441 · crossref 12,726 · authority 1,166); A 13,092 / B 4,864 / C 3,475; crossref chunk 9,313 · page-multi 1,436 · distinctio 779 · unresolvable 297 · articulus 284 · dangling 226 · work 216 · ambiguous 172 · forward 3; anaphora unresolved 286; **QA 211**; printed slips **20 annotated, 0 stale** | 35,240; scripture 21,434 · crossref 12,640; A 13,050 / C 3,510; chunk 9,226 · work 217; QA 211; slips 6 / 0 | **+93** = D7 +83, W23 +1, W41 +1, W37 +1, D2 +7. **Scripture +7** = D2 +7, W41 +1, and D7's moved anaphor −1. **Crossref +86** = D7 +84 (83 + that anaphor), W23 +1, W37 +1. **A +42 / C −35 / B 0** = W41's 42 refinements C → A (38 + 4 anaphora) and its one new A record (A +43, C −42), D2's 7 new records (all C, +7), and D7's moved anaphor (A −1). **chunk +87** = D7 +85 (83 + the refine + the anaphor), W23 +1, W37 +1; **work −1** = D7's refine. **QA unchanged**: no job created a dangling or out-of-range record. The QA report gains the 14 slip annotation lines, one existing QA row's raw now reads `ibid. q. 2`, and the header count changes. **Slips +14** = ruling 145 |
| `build-authorities.py` | **17,127; to a work 16,785 (98.0 %)** | 17,118; 16,776 | +9, ruling 148 |
| `build-index-json.py` (2nd pass) | scripture **78 books / 21,419**; goto 2,317 / 4,987; authorities **89 authors / 427 works / 17,127**; crossref **1,836 cited / 11,278 backlinks** | 21,412; 87 / 423 / 17,118; 1,836 / 11,211 | Scripture +7 (D2's formerly collapsed records). Authors +2 (juvenal, vitae-patrum). Works +4 (sermo-in-assumptione, manuale, satirae, vitae-patrum; meditationes-piissimae has no record yet). Backlinks +67: D7's 84 into `bon-hex-c*`, W23 and W37, net of de-duplication per citing–cited pair. Cited chunks unchanged, because every `bon-hex-cN` target was already cited by something |
| `build-content.mjs` (both passes) | **18 books, 2,317 / 2,317** | same | none, except `bon-cioan-app`'s title is now `Appendix` (ruling 137) |
| `check-live-flags.py vol6` | 199 chunks; LIVE none; 2 exempt (c2 p. 545 n. 6) | same | none |
| `check-vol5-apparatus.py --volume=vol6` | 199 chunks, 6,500 entries, all passed | same | none |
| `check-vol5-census.py` | vol5 167/167 · vol6 199/199, rosters agree; vol6 317 runovers (292 / 25) | same | none |
| `polish-style-scan.py` | 11 / 6 / 2,318, **0 `bon-cioan`** | same | none |
| `validate-chunk.py vol6/bon-cioan-*.md` | 22 checked, 0 failed | same | none |
| `build-progress.mjs` | Tome VI 624 / 634 pp.; `collationes-ioannem` complete | `complete: false` | ruling 151 |

## PASS 4 — plate cleanup: DONE 2026-11-07

**Deleted:** all 75 plates `raw/vision/vol6/p-560.png` … `p-634.png`: **160.3 MB** decimal (152.9 MiB) of file data. `du` reported 170 MB
including blocks, which is the sheet's "168 MB". `raw/vision/vol6/` is now empty. `/tmp/colcrop/` was already empty, and there were no
other scratch crops on disk (session scratch is outside the repo). All of these files are gitignored and can be regenerated from
`raw/doctorisseraphic06bona.pdf`. **Nothing was kept, because Vol VI has no next chunk**: after p. 634 the next leaf is the volume index
(PDF 677), which is not chunked.

## QUEUED (not done; each needs its own decision)

- One resolver session: D1 + (4), D4, D5 and D6 / W51, plus the two anaphora that D7 moved (above).
- The genitive-sigla authorities extension (ruling 148(b)), with a full before/after sample.
- A corpus-wide spelling decision (judgement / judgment, recognize / recognise) across Vols I–V (ruling 144).
- `VOLUME_COMPLETE[6]` in `tools/build-citations.py` still reads `False`. Now that Vol VI's body is complete it is a candidate to flip.
  No record would move today, since the corpus's three `forward`s point into tomes IX and XI. Not ruled, and not changed.

**Front after the gate:** ⛔ the ONE deploy (ruling 123), which needs Wilson's per-action OK; then the push, a separate ask; then the
Vol VII mini-pilot (*Commentarius in Evangelium S. Lucae*, p. 1), a Fable-shaped STOP.
