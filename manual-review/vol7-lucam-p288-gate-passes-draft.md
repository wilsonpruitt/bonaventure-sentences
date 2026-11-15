# Vol VII *Lucam* p. 288 gate: passes 1-3 DRAFT (read-only agent, 2026-11-15)

Uncommitted. No chunk, tool, manifest, ruling file, resume note or plate was edited, committed or deleted. Nothing was pushed or deployed, and `site/.vercel/output` was left alone. Register questions to Wilson belong to the evidence sheet, not this one. Model: `vol7-lucam-p188-gate-passes-draft.md`. Pass 3 is the read-through and consistency pass as briefed: file-side parity, register census incl. rulings 41-62, `tr-` inventory, frontmatter continuity, hand-offs. No plate was read in this run.

**Scope:** 63 chunks, pp. 3-288, **3,200 numbered apparatus entries** + **49** `tr-` notes. The new ground is the 22 chunks `bon-luc-c8-v1-10` → `bon-luc-c11-v5-13`, pp. 188-288. They hold **1,185 entries** (2,015 + 1,185 = 3,200) + **15** `tr-` notes (34 + 15 = 49).

Entries per chunk: c8-v1-10 54 · c8-v11-21 56 · c8-v22-25 41 · c8-v26-33 42 · c8-v34-39 39 · c8-v40-48 53 · c8-v49-56 39 · c9-v1-9 49 · c9-v10-17 49 · c9-v18-27 65 · c9-v28-31 59 · c9-v32-36 54 · c9-v37-45 49 · c9-v46-56 61 · c9-v57-62 39 · c10-v1-3 29 · c10-v4-16 71 · c10-v17-24 62 · c10-v25-37 70 · c10-v38-42 65 · c11-v1-4 68 · c11-v5-13 71.

p. 288 nn. 4-11 belong to the next interval, which is unbuilt (checker: `PENDING n.4,5,6,7,8,9,10,11`).

## PASS 1: live flags. AS EXPECTED (one `[?]`, recorded)
`check-live-flags.py vol7` scanned 63 chunks. **LIVE [?] FLAGS: 2 occurrences, which is one flag counted in La and En:** `bon-luc-c5-v12-16` l. 279 (`[^p122-11]` **La.** … *A C G E [?]*) and l. 281 (**En.**). This is exactly the resume's one live `[?]` (ruling 59: stays open).

No `[?]` stands in any body or apparatus of the 22 new chunks. The file-side hits elsewhere are all Notes prose ("zero `[?]`").

**Divergence from the p. 188 draft (tool behaviour, not corpus):** the p. 188 draft records the tool exiting 1 while a flag is live. This run it **exited 0** with the same flag listed. The output is otherwise identical in form. Recorded only.

## PASS 2: mechanical suite. CLEAN: every resume START-HERE verification figure reproduced, no corpus divergence
| tool | result | resume "Verification at `bon-luc-c11-v5-13`" |
|---|---|---|
| `check-vol5-apparatus.py --volume=vol7` | **63 chunks, 3,200 entries**, La = En in every chunk; every page 1..N through p. 287; p. 288 `1-3 ok PENDING n.4,5,6,7,8,9,10,11`; **All checks passed** (exit 0) | 63 / 3,200 ✓ |
| `check-vol5-census.py` | vol7 **63 on disk / 63 in ledger**; **178 runovers (153 gutter / 25 page)**; **62 positive, 1 negative**; rosters agree. The one negative is `bon-luc-c10-v38-42` (ledger row `-`); its Notes say "No runover" page by page. Interval page-crossings: p. 206 n. 13 · 218 n. 12 · 233 n. 13 · 256 n. 10 · 285 n. 13 (5 of the 25). The interval added 59 runovers (54 gutter / 5 page) | ✓ |
| `polish-style-scan.py --volume 7` | **CLEAN (vol7, 63 files)**. Unscoped run: 11 issues / 6 chunks / **2,381 scanned**, all in Vols III-V as at p. 188, zero in vol7 | ✓ |
| `build-citations.py` (`--out`/`--qa` to the scratchpad) | 2,381 chunks; **42,717 ledger records**; **QA 213**; anaphora 2,321 within-chunk + 86 cross-chunk, **unresolved 379**; coordinate ibid. 477 (374 honoured / 103 unresolvable); printed slips 23 annotated, 0 stale. **Both outputs byte-identical to the tracked `index/citations.tsv` and `manual-review/citation-qa-report.md`** (`cmp`) | 42,717 / QA 213 / 379 ✓ |
| `site/scripts/build-content.mjs` → `build-index-json.py` → `build-content.mjs` (resume order) | **19 books, 2,380 questions, 2,380 translated** (both runs); **crossref index 1,862 chunks cited, 11,238 backlinks**; scripture 74 books / 28,354; goto 2,380 chunks | 2,380/2,380; 1,862 / 11,238 ✓ |
| `validate-chunk.py` (each of the 63) | 63 × "1 checked, 0 failed" | OK ✓ |

**Generated files.**
- `git status --short` was the same before and after the whole suite: ` M index/authorities.tsv`, ` M site/vercel.json`, `?? .claude/settings.local.json`. All three were **pre-existing**, already present before this agent ran anything (presumably from the site build and deploy). This agent did not touch them, and `git diff --stat` was unchanged (1,188 + 15 lines).
- `build-index-json.py` *reads* the modified `index/authorities.tsv`. Its authorities output (89 authors / 436 works / 18,490 citations) is therefore built from the working copy. No resume figure depends on it.
- `build-citations.py` was pointed at the scratchpad, so no tracked file was rewritten even transiently. The `site/src/data/*.json` outputs are gitignored.
- No step was skipped.

## PASS 3: read-through / consistency. One NEW defect, one KNOWN defect confirmed (D-1); otherwise clean

### 3a. Per-chunk La/En parity (all 63, computed from the files, then checked against each chunk's own Notes claim)
- **Anchors:** in all 63 chunks the `[^pN-n]` sequence is identical La/En, unique, in page/note order, and the anchor set equals the def set (3,200 = 3,200). Interval: 1,185 = 1,185. Every def's page lies in the chunk's `printed_pages`.
- **Page markers:** identical La/En in all 63, and equal to `printed_pages` in 62. The exception is old-ground `c3-v21-22` (markers 81-84, `printed_pages` 81-85; the p. 84 n. 14 page runover), as at the p. 88 and p. 188 gates. **Non-defect.**
- **¶ numbers:** La = En in all 63, and each chunk's ¶s run exactly over its frontmatter `paragraphs` range with no gap.
- **Guillemets, paragraph by paragraph:** the « and » counts agree La/En in every ¶ of every chunk. One interval chunk is unbalanced: **`c8-v49-56` 57 « / 56 »**, the same in both languages. Its Notes give the counts and the cause: ¶ 91 Gal. 4:19 *« « Filioli mei*, a doubled opening guillemet as printed, with `[so printed]` in the English (resume item 27). **Non-defect (recorded).** Every other interval chunk balances, and each stated count matches the file.
- **Verse tags:** the La and En sequences agree in every ¶, reading English `(V. N.)` as `(Vers. N.)`. Interval La counts: 10 · 11 · 4 · 8 · 6 · 9 · 8 · 9 · 8 · 9 · 4 · 5 · 9 · 11 · 6 · 3 · 13 · 8 · 12 · 5 · 4 · 8 (= 170). Every tag's number falls inside the chunk's `verses`. Multi-verse tags as printed, both languages: `c9-v1-9` *(Vers. 7. 8.)*, `c9-v10-17` *(Vers. 14. 15.)*, `c9-v18-27` *(Vers. 21. 22.)*, `c9-v28-31` *(Vers. 30. 31.)*, `c10-v25-37` *(Vers. 36. 37.)*, `c11-v5-13` *(Vers. 11. et 12.)*. Old-ground `c4-v38-44` *(Vers. 40)* without its period, as recorded at p. 188.
- **English verse-tag form, D-1 (KNOWN, CONFIRMED):** **`c8-v49-56` writes `(V. 49.)` … `(V. 56.)` at all 8 of its English body tags** (¶¶ 88, 89, 90, 92, 93, 94, 95, 98). Every other one of the 63 chunks writes `(Vers. N.)` in the English body. The chunk's own Notes claim "`(Vers.` 8 = 8 in each language", which is **false for the English** (0 `(Vers.` there) and stale. The fix is mechanical: 8 lines, plus that one Notes clause. This is the resume's D-1 [51]; no other `(V. N.)` body tag exists in vol7. (The apparatus **En.** lines use "V. N" for *Vers. N* in all 63 chunks. That is uniform house practice and not in scope.)
- **Notes self-claims:** in every interval chunk, the stated apparatus-entry total (the "N APPARATUS ENTRIES" headline, word or digit) equals the file's def count. So do the stated "anchors N = N", "Guillemets N « / M »" and, where stated, "page markers N = N". **The only false claim is the `c8-v49-56` "(Vers.` 8 = 8 in each language"** above.

### 3b. Register-term census, pp. 188-288 (22 chunks, ¶-aligned La vs En, rendered bodies only, anchors stripped)
| Latin | English | La / En | ¶s where La > En, resolved |
|---|---|---|---|
| *benignitas* / *benignus* (r. 45) | kindness / kind | 11 / 17 | 0 (the surplus is "kind of") |
| *clementia* | clemency | 9 / 9 | 0 |
| *praeconium* (r. 30) | proclamation | 1 / 2 | 0. **But see the defect below:** the second "proclaim" is a *praedicare* |
| *praedicare* family (r. 12/30) | preach- | 120 / 131 | **1: `c9-v32-36` ¶ 69, Ambrose *praedica post consummationem* → "proclaim after consummation". DEFECT (below)** |
| *evangelizare* | "preach the gospel" etc. | 12 / 36 | 0 |
| *magisterium* | teaching office | 3 / 3 | 0 |
| *paupertas* | poverty | 13 / 14 | 0 |
| *misericordia* | mercy | 39 / 54 | 0 |
| *miseratio* | commiseration | 2 / 0 | 2, both Douay inside quotations: Ecclus. 36:1 "the light of thy mercies" (`c9-v37-45` ¶ 73); Heb. 10:28 "without any mercy" (`c10-v25-37` ¶ 63; the same verse as the p. 188 `c6-v1-11` ¶ 5 site). Ruling 12's Douay-in-quotation clause; non-defect |
| *credulitas* / *incredulitas* (r. 55) | belief / unbelief | 5 / 5 · 2 / 3 | 0 (the extra "unbelief": see the *infidelitas* observation) |
| *redarguere* (r. 56) | convict | 4 / 4 | 0 |
| *suasio* / *persuasio* (r. 44) | persuading / persuasion | 5 / 13 | 0 |
| *curare* / *curatio* (r. 53) | cure | 45 / 46 | 2 false hits: *curant de* "care for" (`c8-v1-10` ¶ 10); *curabilis* "curable" (`c8-v40-48` ¶ 79) |
| *sanare* / *sanatio* (r. 53) | heal / healing | 25 / 36 | 0 (Luke 9:11, 9:42 as item 8) |
| *caritas* (r. 52) | charity | 51 / 51 | 0 |
| *dilectio* (r. 52) | dilection | 13 / 12 | 1: `c9-v10-17` ¶ 19 *perfectio dilectionis* "the perfection of love", introducing I John 3:18 "Let us not love". Ruling 52 conforms only where the paragraph leans on *dilectio* against the Douay; recorded, not a defect |
| *otium* (r. 57) | leisure | 7 / 9 | 0. The 2 extra are *otiosa* "at leisure" (`c10-v38-42` ¶ 69, disclosed [176]); "leisure" never on *vacatio* |
| *pietas* (r. 31 / 51) | piety | 10 / 10 | 0 |
| *poenitentia* | penance | 11 / 10 | 0 real (*poenitens* "penitent") |
| *auctoritas* (r. 47) | authority | 25 / 28 | 0 |
| *admirabilis* / *mirabilis* | wonderful / marvellous | 10 / 12 · 20 / 17 | hits are *admirari* / *mirabiliter* forms; not pursued |
| *Praeceptor* (r. 12 / 49) | Master | 5 / 24 | 0 |

**DEFECT (NEW, not on the resume's D-list): `bon-luc-c9-v32-36` ¶ 69, English, the last sentence: Ambrose's *« Lauda post mortem, praedica post consummationem »* is rendered « Praise after death, proclaim after consummation ».**
- Ruling 30: "'Proclaim / proclamation' belongs to *praeconium* alone in this translation; … *praedicare* is never 'proclaim'."
- The chunk's Notes do not disclose it, and the census found no other *praedic-* → "proclaim" anywhere in the 22 chunks.
- Every other "proclaim/proclamation" in the interval's English bodies sits on a *praeconium* (`c10-v4-16` ¶ 15).
- `c10-v4-16`'s Notes record Jonas 3:5 adjusted to "preached" against the Douay's "proclaimed" under r. 30, so the interval's own builders read the rule this way.
- Fix: "preach after consummation". One word, one line, the chunk's closing sentence.

**Ruling 49 (forward clause), mechanically:** *Praeceptor* stands in four interval ¶s: `c8-v22-25` ¶ 38, `c8-v40-48` ¶ 82, `c9-v32-36` ¶ 60 and `c9-v46-56` ¶ 90. Each chunk carries `tr-praeceptor`. *Magister* shares the ¶ only at `c8-v40-48` ¶ 82 and `c9-v46-56` ¶ 90, and both of those notes carry the *magister* sentence. This matches resume item 16 exactly.

**Trigger sites without a note, all disclosed:**
- `c8-v49-56` ¶ 91 *non vacat a mysterio* "free from" (r. 32's *vacare a*, Notes say no `tr-vacare`).
- *lumen* at `c9-v28-31` ¶ 51 (Eccles. 11:7) and `c10-v4-16` ¶ 18 (Matt. 10:27): the Vol V exemption, item 19 [76, 142].
- Human *pietas* with no `tr-pietas` at `c9-v57-62` ¶¶ 106, 108, `c10-v4-16` ¶ 12, `c10-v25-37` ¶ 57, `c11-v1-4` ¶ 3 and `c11-v5-13` ¶ 19. Each chunk's Notes says the *pietas* is human (item 21).

**Observation (no ruling covers it; for the evidence sheet's item 99):** *infidelitas* is "faithlessness" at `c9-v37-45` ¶¶ 72, 77 (which writes it "kept off *incredulitas* 'unbelief'", r. 55), `c11-v5-13` ¶ 33 and `c8-v34-39` ¶ 62. It is **"unbelief"** at `c10-v4-16` ¶ 19 (*excusationem de infidelitate* "no excuse for unbelief"), and that Notes is silent. *infidelis* "unbeliever" follows the Douay (II Cor. 4:4) at `c10-v25-37` ¶ 55 and `c9-v57-62` ¶ 107. This is a one-site split, recorded and not counted as a defect. If item 99 is ratified it is one word.

### 3c. `tr-` note inventory, pp. 188-288: 15 notes, every def anchored exactly once, every anchor defined
- `c8-v11-21` lumen (¶ 24)
- `c8-v22-25` praeceptor (¶ 38)
- `c8-v40-48` pietas (¶ 74), praeceptor (¶ 82)
- `c9-v1-9` evangelizare (¶ 2)
- `c9-v28-31` vacare (¶ 44), **excessus (¶ 47, at "the transport of contemplation")**
- `c9-v32-36` lumen (¶ 57), praeceptor (¶ 60)
- `c9-v37-45` pietas (¶ 77)
- `c9-v46-56` praeceptor (¶ 90)
- `c10-v1-3` corrigenda (**on the p. 252 `####` rubric**, item 6/25)
- `c10-v25-37` lumen (¶ 52)
- `c10-v38-42` vacare (¶ 67)
- `c11-v1-4` vacare (¶ 11, *vacabimus* "wholly free for him")

There is no `tr-` anchor in any Latin body and none inside the interval's apparatus. Vol VII total: 34 + 15 = **49**.

The interval has one Corrigenda note, matching item 6. `tr-excessus` is D-3 / item 15. It is anchored at ¶ 47, whose English reads "transport", while the note's case is the lemma's "excess" (¶ 54, Luke 9:31). That is the split the gate must decide, so it is not a new defect.

### 3d. Frontmatter / `printed_pages` continuity, pp. 188-288: no gap, no overlap
- `pdf_pages` = printed + 26 and contiguous in all 63.
- Each consecutive pair either shares exactly its seam page (21 shared pages: 188, 193, 198, 201, 205, 208, 213, 216, 220, 230, 234, 239, 243, 248, 252, 254, 261, 266, 272, 277, 282) or abuts. The one abutment is **`c9-v10-17` (ends 224) → `c9-v18-27` (opens 225)**. Both Notes agree on it:
  - `c9-v10-17`: ¶ 28 closes at ~0.60 of 224R, "all eleven of p. 224's notes are mine", "last page 224, not 225".
  - `c9-v18-27`: the t4 *Via proficiendi* at the head of 225L, "p. 225 owes nothing backward".
- `division` steps 7 → 8 → 9 → 10 → 11 once each. `section` runs VIII 1-7 · IX 1-8 · X 1-5 · XI 1-2. `paragraphs` restart at 1 at each capitulum and are contiguous within it. Last ¶: VIII 99 · IX 111 · X 80; XI so far 35 (item 3).
- No `verses` overlap in the interval.

### 3e. Hand-offs at every shared page, pp. 188-288 (file ownership derived from the defs; each split checked against BOTH chunks' Notes)
| page | A nn. / B nn. | page | A nn. / B nn. |
|---|---|---|---|
| 188 | c7-v36-50 1-5 / c8-v1-10 6-8 | 239 | c9-v32-36 1-4 / c9-v37-45 5-12 |
| 193 | c8-v1-10 1-9 / c8-v11-21 10-13 | 243 | c9-v37-45 1-4 / c9-v46-56 5-13 |
| 198 | c8-v11-21 1-6 / c8-v22-25 7-11 | 248 | c9-v46-56 1-10 / c9-v57-62 11-12 |
| 201 | c8-v22-25 1-10 / c8-v26-33 11-12 | 252 | c9-v57-62 1-3 / c10-v1-3 4-10 |
| 205 | c8-v26-33 1-6 / c8-v34-39 7-11 | 254 | c10-v1-3 1-10 / c10-v4-16 11 |
| 208 | c8-v34-39 1-9 / c8-v40-48 10-11 | 261 | c10-v4-16 1-3 / c10-v17-24 4-12 |
| 213 | c8-v40-48 1-3 / c8-v49-56 4-11 | 266 | c10-v17-24 1-2 / c10-v25-37 3-13 |
| 216 | c8-v49-56 1-7 / c9-v1-9 8-11 | 272 | c10-v25-37 1-3 / c10-v38-42 4-10 |
| 220 | c9-v1-9 1-10 / c9-v10-17 11 | 277 | c10-v38-42 1-6 / c11-v1-4 7-13 |
| 230 | c9-v18-27 1 / c9-v28-31 2-13 | 282 | c11-v1-4 1-11 / c11-v5-13 12-14 |
| 234 | c9-v28-31 1-11 / c9-v32-36 12 | 288 | c11-v5-13 1-3 / next interval 4-11 PENDING |

On every page the two halves make one contiguous 1..N register, and the apparatus checker confirms N against `KNOWN_TOTALS_VOL7`. Both chunks' Notes state the same split on all 21 pages: A's "nn. a-b are mine" or per-page map ("p. N = k (nn. a-b of N)"), and B's "hand-off measured true / re-derived on the plate, nn. a-b are mine". p. 288 nn. 4-11 are named in `c11-v5-13`'s Notes and in the resume as the next interval's.

## Summary
- **Pass 1:** as expected. One live `[?]`, `c5-v12-16` p. 122 n. 11, La + En. Tool exit code 0 this run (the p. 188 draft records 1); tool behaviour only.
- **Pass 2:** clean. Every resume figure reproduced exactly: 63 / 3,200; census 63/63, 178 runovers (153/25; 62 positive, 1 negative = `c10-v38-42`); style CLEAN (63); citations 42,717, QA 213; anaphora 379; crossref 1,862 / 11,238; validate OK ×63; build 2,380/2,380. No tracked file changed. The pre-existing `M index/authorities.tsv`, `M site/vercel.json` and `?? .claude/settings.local.json` are not this agent's.
- **Pass 3:** La/En parity of anchors, page markers, ¶ numbers, guillemets and verse tags holds in every ¶ of all 63 chunks. The 15 interval `tr-` notes are all paired, there is no page gap or overlap, and the hand-offs agree on all 21 shared pages.
- **Defects:**
  - **(1) NEW: `c9-v32-36` ¶ 69, *praedica* "proclaim" against ruling 30.** One word, undisclosed.
  - **(2) KNOWN D-1 confirmed: `c8-v49-56` English `(V. N.)` ×8**, and its Notes claim "`(Vers.` 8 = 8 in each language" is false for the English.
- **Observations:** the *infidelitas* "faithlessness" / "unbelief" split (`c10-v4-16` ¶ 19); `c9-v10-17` ¶ 19 *dilectio* "love"; old-ground `c3-v21-22` page markers vs `printed_pages` (pre-existing runover).
