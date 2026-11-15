# Vol VII *Lucam* p. 188 gate: passes 1-3 DRAFT (read-only agent, 2026-11-15)

Uncommitted. No chunk, tool, manifest, ruling file, resume note or plate was edited, committed or deleted; nothing pushed or deployed. Register questions to Wilson are the evidence sheet's, not this sheet's. Model: `vol7-lucam-p88-gate-passes-draft.md`. Pass 3 here is the read-through / consistency pass as briefed (file-side parity, register census, `tr-` inventory, frontmatter continuity, hand-offs); no plate was read in this run.

**Scope:** 41 chunks, pp. 3-188, **2,015 numbered apparatus entries** + **34** `tr-` notes. New ground: the 19 chunks `bon-luc-c4-v1-13` → `bon-luc-c7-v36-50`, pp. 88-188, **1,147 entries** (868 + 1,147 = 2,015) + **17** `tr-` notes. Per chunk (entries): c4-v1-13 76 · c4-v14-22 49 · c4-v22-30 50 · c4-v31-37 39 · c4-v38-44 54 · c5-v1-11 71 · c5-v12-16 45 · c5-v17-26 61 · c5-v27-39 68 · c6-v1-11 70 · c6-v12-19 80 · c6-v20-26 61 · c6-v27-31 39 · c6-v32-38 48 · c6-v39-49 60 · c7-v1-16 90 · c7-v17-23 56 · c7-v24-35 58 · c7-v36-50 72. p. 188 nn. 6-8 belong to Cap. VIII, unbuilt (checker: `PENDING n.6,7,8`).

## PASS 1: live flags. AS EXPECTED (one `[?]`, recorded)
`check-live-flags.py vol7` → scanned 41 chunks in vol7; **LIVE [?] FLAGS: 2 occurrences = one flag, La + En**: `bon-luc-c5-v12-16` l. 279 (`[^p122-11]` **La.** … *A C G E [?]*) and l. 281 (**En.**). Exactly the resume's live `[?]` (docket F 56). No other `[?]` anywhere in vol7 (file-side count: `[?]` occurs only in `c5-v12-16`, twice). The tool exits 1 because a flag is live; that is its design, not a failure.

## PASS 2: mechanical suite. CLEAN — every resume line-17 figure reproduced, no divergence
| tool | result | resume line 17 |
|---|---|---|
| `check-vol5-apparatus.py --volume=vol7` | 41 chunks, 186 known page totals (pp. 3-188); **2,015 entries**, La = En in every chunk; every page 1..N; p. 188 `1-5 ok PENDING n.6,7,8`; **All checks passed** | 41 / 2,015 ✓ |
| `check-vol5-census.py` | vol7 **41/41** on disk and in ledger; **119 runovers (99 gutter / 20 page)**; 41 positive, 0 negative; rosters agree. Page-crossing: p. 9 n. 7 · 13 n. 10 · 21 n. 10 · 38 n. 12 · 72 n. 12 · 83 n. 10 · 84 n. 14 · 88 n. 12 · 91 n. 12 · 99 n. 12 · 101 n. 12 · 103 n. 12 · 105 n. 13 · 115 n. 12 · 122 n. 11 · 126 n. 11 · 133 n. 10 · 143 n. 10 · 151 n. 12 · 153 n. 13 (13 of the 20 in the interval) | ✓ |
| `polish-style-scan.py` | **11 issues / 6 chunks / 2,359 scanned**, scope vol1-7; all in Vols III-V (`bon-hex-c23`, `III-d31-a3-q3`, `III-d32-a1-q2`, `III-d5-a2-q4`, `IV-d14-p2-a2-q1`, `IV-d16-p2-a2-q2`); **zero in vol7** | ✓ |
| `build-citations.py` | 2,359 chunks; **40,415 ledger records**; **QA 212**; anaphora 2,308 within-chunk + 86 cross-chunk, **unresolved 370**; coordinate ibid. 473 (370 honoured / 103 unresolvable); printed slips 23 annotated, 0 stale | 40,415 / QA 212 / 370 ✓ |
| `build-index-json.py` | **crossref index 1,837 chunks cited, 11,111 backlinks**; scripture 74 books / 26,205; goto 2,358 chunks | 1,837 / 11,111 ✓ |
| `validate-chunk.py` (each of the 41) | 41 × "1 checked, 0 failed" | OK ✓ |
| `site/scripts/build-content.mjs` | **19 books, 2,358 questions, 2,358 translated** | 2,358/2,358 ✓ |

**Generated files.** `git status --short` before and after the whole suite: only the pre-existing untracked `.claude/settings.local.json`; `git diff --stat` empty. `index/citations.tsv` and `manual-review/citation-qa-report.md` rebuilt byte-identical to HEAD; the `site/src/data/*.json` outputs are gitignored (`site/.gitignore`). No step would rewrite a tracked corpus file; none skipped. (Housekeeping: a scratch pickle this agent's script wrote into the repo root for a moment was moved to the scratchpad at once; the tree is as found.)

## PASS 3: read-through / consistency. CLEAN — no defect

### 3a. Per-chunk La/En parity (all 41; computed from the files, then checked against each chunk's own Notes claim)
- **Anchors:** in every chunk the `[^pN-n]` sequence is identical La/En, unique, in order, and the anchor set = the def set (2,015 = 2,015). Interval: 1,147 = 1,147.
- **Page markers:** identical La/En in all 41, and equal to `printed_pages` in 40. The one exception is the old-ground `c3-v21-22` (markers 81-84, `printed_pages` 81-85: p. 84 n. 14 runs onto p. 85, census page-crossing; as at the p. 88 gate). **Non-defect.**
- **¶ numbers:** La = En in all 41, and each runs exactly over the frontmatter `paragraphs` range with no gap.
- **Guillemets, paragraph by paragraph:** the « and » counts agree La/En in every ¶ of every chunk. Four interval chunks are unbalanced in the same way in both languages, and each one's Notes states the counts: `c6-v1-11` 114/113, `c6-v12-19` 131/132, `c6-v32-38` 74/75, `c7-v17-23` 95/94. These are docket G 57's stray/missing guillemets, kept as printed. **Non-defect (recorded).**
- **`(Vers.` tags:** the same sequence La/En in every ¶. Interval counts: 13 · 9 · 9 · 7 · 7 · 11 · 5 · 10 · 12 · 11 · 8 · 7 · 5 · 7 · 11 · 16 · 7 · 12 · 15. Every tag falls in the chunk's `verses`. `c4-v38-44` ¶ 87 `(Vers. 40).` is printed without the period; Notes record it (read at 1.8×), and both languages match. **Non-defect.**
- **Notes self-claims:** every interval chunk's stated `(Vers.` N = N, "anchors N = N" and "Guillemets N « / M »" (where stated) equals the file count. No stale claim.

### 3b. Register-term census, pp. 88-188 (19 chunks, ¶-aligned La vs En, rendered bodies only)
| Latin | English | La / En | ¶s where La > En |
|---|---|---|---|
| *benignitas* | kindness | 15 / 15 | 0 |
| *clementia* | clemency | 10 / 10 | 0 |
| *praeconium* | proclamation | 8 / 8 | 0. **All 8 "proclaim/proclamation" in the English bodies sit on a *praeconium* ¶** (c4-v1-13; c5-v12-16 ×2; c7-v17-23 ¶¶ 34-35; c7-v24-35 ×3). Ruling 30 holds |
| *praedicare* family | preach- | 69 / 84 | 0: no *praedic-* rendered "proclaim" |
| *evangelizare* | "preach the gospel" / "good tidings" | 16 / 24 | 0. No bare "preach" for it. "Good tidings" appears only in Douay verses carrying `tr-evangelizare` (c4-v14-22 ¶¶ 27, 37; c5-v1-11 ¶ 7). The c7-v17-23 passive glosses are docket D 40 |
| *magisterium* | teaching office | 5 / 5 | 0 |
| *publicanus* / *paupertas* | publican / poverty | 27/27 · 29/29 | 0 |
| *misericordia* | mercy | 34 / 52 | 0 (the surplus is *misereri*, *misericors*) |
| *pietas* | piety | — | divergent ¶s are either Douay *impius* "wicked/ungodly" in verses, or docket D 32 (c5-v17-26 ¶ 44 "godly deeds"; c6-v12-19 ¶ 40 "godliness") |
| *miseratio* | commiseration | 3 / 1 | 2, both inside quotations (Heb. 10:28 c6-v1-11 ¶ 5; Job 31:18 c7-v1-16 ¶ 23): ruling 12's Douay-in-quotation clause |
| *Praeceptor* | Master | — | only c5-v1-11 ¶ 10 (with `tr-praeceptor`). The other hits are *praeceptor* "teacher" in Isaias verses and *praeceptum* "precept" |

**Observation (no ruling covers it; not a defect):** *impius* in Bonaventure's own prose follows the nearest Douay word. It is "ungodly" at `c6-v27-31` ¶ 73 (*peccator vel impius*, after Ecclus. 12:4) and "wicked" at `c6-v39-49` ¶ 96 (*superbus et impius*, after Prov. 17:15). *impietas* is "impiety" at `c7-v17-23` ¶ 46. This could be added to the register sheet if Wilson wants one word.

### 3c. `tr-` note inventory, pp. 88-188: 17 notes, every def anchored exactly once, every anchor defined
`c4-v1-13` corrigenda (p. 95) · `c4-v14-22` evangelizare (¶ 27), vacare · `c4-v38-44` lumen (**anchored inside apparatus p. 110 n. 8**) · `c5-v1-11` evangelizare (¶ 7), praeceptor (¶ 10), corrigenda (**inside apparatus p. 114 n. 5**, ruling 23's shape) · `c5-v17-26` lumen · `c5-v27-39` lumen · `c6-v20-26` vacare (¶ 59, at a vice, docket D 36) · `c6-v32-38` lumen (**inside apparatus p. 159 n. 7**) · `c7-v1-16` pietas, corrigenda (p. 168), lumen (¶ 17) · `c7-v17-23` evangelizare, pietas · `c7-v36-50` pietas (¶ 62). No `tr-` anchor in any Latin body.

The three apparatus-anchored `tr-lumen`/`tr-corrigenda` notes are the docket's items 7 and 31, not defects. Trigger sites with no note: *lumen* at `c6-v12-19` ¶¶ 28, 47 (Notes: verses only, no prose leaning, the Vol V test) and `c6-v39-49` ¶ 93 (docket D 31). Human *pietas* with no note at `c6-v12-19`, `c6-v32-38` ¶¶ 86-87 and `c6-v39-49` ¶ 102; each chunk's Notes says it is human, so ruling 31 owes no note. Corrigenda count 3 = docket B 6-8.

### 3d. Frontmatter / `printed_pages` continuity, pp. 88-188: no gap, no overlap
- `pdf_pages` = printed + 26 and contiguous in all 41.
- Consecutive chunks share exactly their seam page, or abut. The one abutment is `c6-v20-26` (ends 152) → `c6-v27-31` (opens 153). Both Notes say ¶ 63 closes at the foot of 152R, p. 152's register closes at n. 14 with no runover, and ¶ 64 opens at the head of 153L.
- `division` 4 → 7 steps once per capitulum, and `section` runs 1..n within each (IV 1-5, V 1-4, VI 1-6, VII 1-4). `paragraphs` restart at 1 at each `CAPITULUM`, contiguous within it. Last ¶ IV 98 · V 85 · VI 111 · VII 84 (docket A 3).
- **Verse overlap, by design:** `c4-v14-22` (`verses: 14-22`) and `c4-v22-30` (`22-30`) share v. 22. The `c4-v22-30` Notes record that ¶ 46 of its predecessor is also tagged v. 22. **Non-defect.**

### 3e. Hand-offs at every shared page, pp. 88-188 (20 shared pages; file ownership derived from the defs; each page's split checked against BOTH chunks' Notes)
| page | A nn. / B nn. | page | A nn. / B nn. |
|---|---|---|---|
| 88 | c3-v23-38 1-9 / c4-v1-13 10-12 | 140 | c6-v1-11 1-7 / c6-v12-19 8-12 |
| 95 | c4-v1-13 1-10 / c4-v14-22 11-12 | 147 | c6-v12-19 1-9 / c6-v20-26 10-11 |
| 100 | c4-v14-22 1-2 / c4-v22-30 3-10 | 156 | c6-v27-31 1-2 / c6-v32-38 3-9 |
| 104 | c4-v22-30 1-9 / c4-v31-37 10-13 | 160 | c6-v32-38 1-6 / c6-v39-49 7-10 |
| 107 | c4-v31-37 1-11 / c4-v38-44 12 | 165 | c6-v39-49 1-9 / c7-v1-16 10-12 |
| 112 | c4-v38-44 1-9 / c5-v1-11 10-11 | 173 | c7-v1-16 1-2 / c7-v17-23 3-11 |
| 119 | c5-v1-11 1 / c5-v12-16 2-12 | 177 | c7-v17-23 1-7 / c7-v24-35 8-14 |
| 123 | c5-v12-16 1-6 / c5-v17-26 7-10 | 182 | c7-v24-35 1-3 / c7-v36-50 4-12 |
| 128 | c5-v17-26 1-9 / c5-v27-39 10-12 | 188 | c7-v36-50 1-5 / Cap. VIII 6-8 PENDING |
| 134 | c5-v27-39 1-7 / c6-v1-11 8-12 | | |

On every page the two halves make one contiguous 1..N register. Both chunks' Notes state the same split: A's per-page map ("p. N = k (nn. a-b of N)" or "nn. a-b are mine") and B's "hand-off measured true / re-read and right". p. 188's nn. 6-8 are named in `c7-v36-50`'s Notes and the resume as Cap. VIII's, for its first builder to re-derive. The `c5-v12-16` p. 119 n. 7 correction (docket A 5) is consistent: the census does not list p. 119 as a runover.

## Summary
- **Pass 1:** as expected. One live `[?]`, `c5-v12-16` p. 122 n. 11, La + En.
- **Pass 2:** clean. All resume line-17 figures reproduced exactly: 41 / 2,015; census 41/41, 119 runovers (99/20); style 11/6/2,359, zero ours; citations 40,415, QA 212; anaphora 370; crossref 1,837 / 11,111; validate OK; build 2,358/2,358. No tracked file changed.
- **Pass 3:** clean. La/En parity holds in every ¶ of all 41 chunks. Register rulings 12/18/30 hold mechanically over pp. 88-188. There are 17 `tr-` notes, all paired. No page gap or overlap, and the hand-offs agree on all 20 shared pages.
- **Defects found: none.** Observations: the *impius* "ungodly"/"wicked" split in prose (3b); the old-ground `c3-v21-22` page-marker vs `printed_pages` (runover, pre-existing).
