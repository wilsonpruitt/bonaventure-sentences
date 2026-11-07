# Vol VI *Collationes in Evangelium S. Ioannis* WORK-CLOSE GATE (p. 634, ruling 123): passes 1–3 (read-only agent, 2026-11-07)

Run on Wilson's go ("Run the gate", 2026-11-07). **First half only:** no chunk, tool, ledger, registry, `build-progress.mjs` or resume
note was edited; nothing pushed, deployed or stashed; no plate deleted. `build-citations.py` and `build-authorities.py` were first
pointed at scratch paths (`--out`/`--qa`/`--residue`) and compared with the committed ledgers (**byte-identical**), so the default-path
`build-index-json.py` / `build-content.mjs` runs that followed could not move anything; `git status --short` afterwards shows only the
pre-existing untracked `.claude/settings.local.json`. A W-auth prototype was run on a **scratch copy** of `tools/authorities.json` and
of the builder (scratch output only). Register and form questions are in the parallel `…-evidence-sheet.md` and are not repeated here.

**Scope: the whole work, 22 chunks, `bon-cioan-c1` … `bon-cioan-app`, pp. 535–634 with no gap, 889 numbered apparatus entries, + 22
`tr-` notes.** 889 = the sum of `KNOWN_TOTALS_VOL6` for pp. 535–634 (100 pages, every one carrying notes), re-derived independently of
the checker by parsing every `[^pP-N]` def in all 199 vol6 chunks: **every page 535–634 carries exactly its run 1..N, each entry owned
once, 0 mismatches on 100 pages.** Claimed entry counts in `transcription_status`: 22/22 match the file.

| chunk | div | pages | entries | Collationes | Annotationes | `tr-` notes |
|---|---|---|---|---|---|---|
| `c1` | 1 | 535–545 | 80 | I–VII | 1–3 | lumen, doctrina |
| `c2` | 2 | 545–550 | 45 | VIII–X | 4–6 | lumen |
| `c3` | 3 | 550–554 | 36 | XI–XIII | 7–11 | lumen, doctrina |
| `c4` | 4 | 554–559 | 41 | XIV–XIX | 12–17 | lumen, vacare |
| `c5` | 5 | 560–565 | 41 | XX–XXV | 18–21 | lumen, doctrina |
| `c6` | 6 | 565–569 | 40 | XXVI–XXIX | 22–27 | doctrina |
| `c7` | 7 | 570–573 | 30 | XXX–XXXII | 28–32 | doctrina |
| `c8` | 8 | 573–578 | 45 | XXXIII–XXXVI | 33–36 | doctrina |
| `c9` | 9 | 578–581 | 21 | XXXVII–XXXVIII | — | lumen |
| `c10` | 10 | 581–585 | 49 | XXXIX–XL | — | doctrina, lumen |
| `c11` | 11 | 585–593 | 71 | XLI–XLIV | 37–44 | lumen |
| `c12` | 12 | 593–597 | 34 | XLV–XLVII | 45–51 | — |
| `c13` | 13 | 597–601 | 45 | XLVIII–LI | 52–56 | — |
| `c14` | 14 | 601–604 | 24 | LII–LIV | 57 | — |
| `c15` | 15 | 604–605 | 15 | — | 58–65 | — |
| `c16` | 16 | 605–609 | 33 | LV–LX | 66 | doctrina |
| `c17` | 17 | 609–611 | 27 | LXI–LXII | 67 | — |
| `c18` | 18 | 611–615 | 30 | LXIII–LXVI | 68 | doctrina |
| `c18-19` | 19 | 615–619 | 39 | LXVII–LXXI | 69 | — |
| `c20` | 20 | 619–622 | 29 | LXXII–LXXIV | 70–72 | doctrina |
| `c21` | 21 | 622–632 | 92 | LXXV–LXXIX | 73–79 | vacare |
| `app` | 22 | 632–634 | 22 | App. I–II | App. 1–2 | lumen, doctrina |
| **total** | | **100 pp.** | **889** | **I–LXXIX contiguous** | **1–79 contiguous** | **22** |

---

## BASELINE (the denominators the second half re-runs against)

Build order as the resume prescribes (citations → authorities → index-json → content → index-json → content), second index pass cited.

| tool | result | verdict |
|---|---|---|
| `build-citations.py` (scratch `--out`/`--qa`, then `cmp`) | **2,318 chunks → 35,240 records** (scripture 21,434 · crossref 12,640 · authority-excluded 1,166); confidence A 13,050 / B 4,864 / C 3,510; crossref chunk 9,226 · page-multi 1,436 · distinctio 779 · unresolvable 297 · articulus 284 · dangling 226 · work 217 · ambiguous 172 · **forward 3** (none ours); anaphora 2,320 + 86 cross-chunk, **unresolved 286**; **QA flags 211**; coordinate ibid. 463 (honoured 355 / unresolvable 108); **printed slips 6 annotated, 0 stale**. Ledger and QA report **byte-identical** to `index/citations.tsv` / `manual-review/citation-qa-report.md` | CLEAN |
| `build-authorities.py` (scratch, `cmp`) | **41,793 apparatus entries → 17,118 authority records; to a work 16,776 (98.0 %)**; same-passage-no-commentary 167; author-only 175 (167 distinct residue strings); `index/authorities.tsv` **byte-identical** | CLEAN |
| `build-index-json.py` (2nd pass) | scripture **78 books / 21,412**; goto 2,317 chunks / 4,987 pages; authorities 87 authors / 423 works / 17,118; **crossref 1,836 chunks cited / 11,211 backlinks** | CLEAN |
| `build-content.mjs` (both passes) | **content.json: 18 books, 2,317 questions, 2,317 translated** | CLEAN |
| `check-live-flags.py vol6` | **199 chunks; LIVE [?] FLAGS none; printed-by-editors exempt 2** (`bon-cioan-c2` p. 545 n. 6, La/En; ruling 131) | CLEAN |
| `check-vol5-apparatus.py --volume=vol6` | **199 chunks, 6,500 entries, all checks passed**; pp. 535–634 every page `ok` | CLEAN |
| `check-vol5-census.py` | **vol5 167/167; vol6 199/199, "Rosters agree"; vol6 317 runovers (292 gutter / 25 page), 154 positive / 45 negative** | CLEAN |
| ↳ in scope | **35 runovers (32 gutter / 3 page: p. 549 n. 10, p. 565 n. 8, p. 610 n. 11) in 14 positive chunks; 8 negative** (`c7`, `c9`, `c13`, `c14`, `c15`, `c16`, `c18`, `c20`) | see Pass 3 |
| `polish-style-scan.py` | **11 issues / 6 chunks / 2,318 scanned** (PAIR 10 / 5, V5LABEL 1 / 1), all pre-existing outside Vol VI; **0 in `bon-cioan-*`** | CLEAN |
| `validate-chunk.py vol6/bon-cioan-*.md` | **22 checked, 0 failed** | CLEAN |
| `git status --short` afterwards | only `?? .claude/settings.local.json` | CLEAN |

**Attributable to this scope in the ledger: 2,652 records** (scripture: apparatus-explicit 1,238 · body-ordinal 1,307 · anaphor 40;
crossref 67: chunk 61 · page-multi 5 · unresolvable 1; confidence A 1,246 · B 590 · C 749). **QA flags ours: 0 of 211.** Unresolved
anaphora ours: 1 (p. 622 n. 7, W51). Printed-slip rows ours: 0 (the nine owed are the evidence sheet's ruling 145).

## PASS 1: live flags. **CLEAN**

199 chunks, none live; the two exempt hits are the editors' printed `[?]` at p. 545 n. 6 (ruling 131). p. 630 n. 12's printed
**`[sive ?]`** (W55) contains no bare `[?]` token, so the checker does not see it and needs no `PRINTED_QUERIES` row (a row would match
nothing).

## PASS 2: mechanical suite + parity + whole-work register census. **CLEAN on every tool; three conformance classes found by census (→ docket)**

**Per-chunk parity (22 of 22 identical):** paragraphs La = En (85/85 … 20/20) · `### ` headings La = En · `<!-- page N -->` lists
identical La/En and = `printed_pages` · `[^pN-M]` anchor sequences identical La/En · ¶ numbers identical La/En · `pdf_pages` =
printed + 42 · `printed_pages` contiguous. `collationes:` / `annotationes:` = the headings present; **Collationes I–LXXIX and
Annotationes 1–79 contiguous across the 21 capitulum chunks with no gap and no repeat**; the Appendix's own App. Coll. I–II / Annot. 1–2.

**Registry (`site/scripts/build-content.mjs`, `collationes-ioannem`, book 18): 22 of 22 division titles MATCH the in-place headings**
(1–18, 19 *Capitulum XVIII et XIX: Tunc ergo apprehendit Pilatus Iesum*, 20, 21, 22 *Appendix*). **Breadcrumbs as built:** `Cap. 1` …
`Cap. 18`, `Cap. 18–19` (ruling 136), `Cap. 20`, `Cap. 21`, **`Cap. 22` for the Appendix (W57, open)**. `build-progress.mjs` L190
`collationes-ioannem … complete: false` (to flip at the gate).

**Whole-work register census** (rendered regions only; aligned paragraph against paragraph where a count could hide a miss):

| rule | census | verdict |
|---|---|---|
| ruling 124 ordinal order | "the Nth chapter of/to Book" **0** in 22 chunks; bare ordinal **0** (two regex hits are "the second of Peter, the first chapter" and "the third of Kings, the last chapter", both conforming) | ✓ |
| ruling 99 *Item* → "Likewise" | Latin body *Item* ≤ English "Likewise" in 22/22 (c10, c18-19 one extra "Likewise" for *Similiter*); c21's six *Item* all "Likewise" | ✓ |
| *magister* → teacher | 11 → 11 | ✓ |
| *caritas* → charity | 65 → 65 | ✓ |
| *dilectio* → dilection | 25 → 30 (Douay "love" adjusted, W21/W29/W32) | ✓ |
| *intellectus* → understanding | 22 → 30; bare "intellect" **0** | ✓ |
| *poena* → punishment (109) | 89 → 103; "penalt-" 9 = *supplicium* ×7 + *poenalitas* ×2 (c3 ¶, c6 *funiculi Adam*) | ✓ |
| `tr-doctrina` (ruling 53) | **11 of 11** chunks carrying *doctrina* have the note | ✓ |
| `tr-lumen` (rulings 74/125) | **9 of 9** chunks with a live *lumen* (c1, c2, c3, c4, c5, c9, c10, c11, app) have the note; 12 body units + 2 apparatus entries, every quoted *lumen* decided by the verse test, **Tob. 5:12 "light" at all three of its sites (c1, c9, app)** | ✓ (evidence sheet ruling 138) |
| `tr-vacare` | c4 (Acts 17:21), c21 | ✓ (as ratified, ruling 133) |
| ruling-93 families (W2 … W61) | Latin family tokens vs English family word, aligned by paragraph, in the chunk that claims the family: *lutum* 65/65 · *calix* 23/24 · *tradere* c13 11/11, c18-19 31/46 · *exaltare* 60/61 · *arguere* 33/33 · *tristitia* 68/70 · *clarificare/claritas* 28/28 · *transire* 29/31 · *illudere* 50/52 · *monumentum* 8/8 · *manifestare* 4/4 · *manere* (c15) 15/15 · *conflare* 6/6 · *ascendere* 45/46 · *advocatus* 21/21 · *trahere* 51/51 · *vivificare* 23/19 by regex, the two short paragraphs (c5 ¶¶ 21–22) read by eye and conforming ("hast given me life", "he shall give life to his soul") — **no real short paragraph** | ✓ |
| ⚠ W21 *infirmitas / infirmari* (c11) | **80 Latin → 75 "infirm-"**: five sites rendered "sick" (c11 L215, L220, L226 ×2, L230), one of them the lemma John 11:3 the W-item says was adjusted | **NEW → docket ruling 139** |
| ⚠ ruling 80(b) "Holy Spirit everywhere, Douay quotations included" | **"Holy Ghost" ×2 in `c21`** (L333 John 3:5; L370 Acts 7:55) | **NEW → docket ruling 143** |
| ⚠ ruling 101 N9 spelling (judgement / honour / recognized) | honour ✓ (0 "honor"); **"judgment" ×39 on 17 lines** (c1 3 · c7 34 · c12 1 · c13 1) against "judgement" ×54; **"recognise/-es/-ed" ×4** (c3 ×2, c8, c18-19) against "recognized" ×1 | **NEW → docket ruling 144 (⚖)** |
| names | Isaias / Jeremias / Ezechiel only; 0 Isaiah / Jeremiah / Ezekiel | ✓ |

**La/En digit sweep:** not re-run entry by entry; the ruling-89 brackets added by c5–app (W8, W11, W14, W17, W20, W26, W49) each add the
true locus in the English only, as at the shakedown (3 of 202 there, all brackets).

## PASS 3: boundary sweep (from the built files; plates NOT re-read except p. 632). **CLEAN**

**Ownership:** above — 100 pages, 889 entries, each owned once, contiguous 1..N.

**Seams (21), split by anchor as built:**

| seam | page | outgoing / incoming notes | shape |
|---|---|---|---|
| c1 → c2 | 545 | 1 / 6 | shared |
| c2 → c3 | 550 | 4 / 1 | shared |
| c3 → c4 | 554 | 8 / 0 | shared, incoming body unanchored on the leaf |
| c4 → c5 | 559 / 560 | 6 / — | leaf edge |
| c5 → c6 | 565 | **0** / 8 | shared, outgoing tail unanchored (the p. 498 rule from the outgoing side) |
| c6 → c7 | 569 / 570 | 7 / — | leaf edge |
| c7 → c8 | 573 | 4 / 5 | shared |
| c8 → c9 | 578 | 5 / 2 | shared |
| c9 → c10 | 581 | 1 / 7 | shared |
| c10 → c11 | 585 | 8 / 3 | shared |
| c11 → c12 | 593 | 6 / 2 | shared |
| c12 → c13 | 597 | 2 / 8 | shared |
| c13 → c14 | 601 | 8 / 1 | shared |
| c14 → c15 | 604 | 2 / 8 | shared; Cap. XV heading anchored (n. 3) |
| c15 → c16 | 605 | 7 / 4 | shared |
| c16 → c17 | 609 | 1 / 9 | shared; Cap. XVII heading anchored (n. 2) |
| c17 → c18 | 611 | 7 / 1 | shared |
| c18 → c18-19 | 615 | 4 / 6 | shared; joint heading anchored (n. 5) |
| c18-19 → c20 | 619 | 5 / 4 | shared |
| c20 → c21 | 622 | 8 / 2 | shared |
| c21 → app | 632 | 3 / 4 | shared; `APPENDIX.⁴` anchored; **n. 3 anchors c21's last words *visio salutaris*³ (read on the plate this pass, p. 632 at 1:3)** |

Every split agrees with the builders' hand-offs and with W30 (2/8), W34 (1/9), W36 (7/1), W40 (4/6), W44 (5/4). Every incoming body
opens on its `### Capitulum …` (or `### Appendix.`) heading. **Runover ledger:** 35 rows in scope = the census; 8 negative lines are
the 8 chunks without a runover. The earlier gate read pp. 535–560 on the plate (13 heads = 13 rows); pp. 560–634 rest on each
builder's own plate reading (two-pass at c11 and c21).

---

## Plate inventory (for PASS 4; nothing deleted) — ⚠ CORRECTS THE RESUME NOTE

`raw/vision/vol6/` holds **75 plates, `p-560.png` … `p-634.png`, 168 MB**, every one 2067×2985 at 450 dpi (pHYs checked on 16) — **not**
"pp. 560, 604, 615, 622–634" as the resume block says: each builder's plates were left on disk. All gitignored and regenerable from
`raw/doctorisseraphic06bona.pdf`. `/tmp/colcrop/` is empty. Scratch (prototypes, census scripts, a p. 632 downscale) is in the session
scratchpad only. **At a work close there is no next chunk to keep a leaf for** (the next item is the deploy, then a new work's pilot),
so Pass 4 deletes all 75.
