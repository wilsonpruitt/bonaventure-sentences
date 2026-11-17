# Vol VII *Lucam* p. 472 gate: passes 1-3 DRAFT (read-only agent, 2026-11-16)

Uncommitted. No chunk, tool, manifest, ruling file, resume note or plate was edited, committed or deleted. Nothing was pushed or deployed, and `site/.vercel/output` was left alone. Scratch scripts and the two `build-citations.py` outputs live in the agent's scratchpad, not the repo. Register questions to Wilson belong to the evidence sheet, not this one. Model: `vol7-lucam-p381-gate-passes-draft.md` (and the p. 288 one before it). Pass 3 is the read-through and consistency pass as briefed: file-side parity, register census over the house words at issue this interval, `tr-` inventory, frontmatter continuity, hand-offs. No plate was read in this run.

**Scope:** 101 chunks, pp. 3-472, **5,624 numbered apparatus entries** + **79** `tr-` notes. The new ground is the 19 chunks `bon-luc-c15-v1-7` → `bon-luc-c18-v28-43`, pp. 381-472 (manifest stage 5, `lucam-chunk-manifest.tsv` rows 84-102). They hold **1,195 entries** (4,429 + 1,195 = 5,624) + **14** `tr-` notes (65 + 14 = 79; the p. 381 sheet's 62 became 65 when the p. 381 gate's rulings added `tr-lumen` to `c12-v1-7`, `c12-v8-12` and `c14-v16-24`, commit `45627c9`).

Entries per chunk: c15-v1-7 69 · c15-v8-10 35 · c15-v11-20 69 · c15-v20-24 55 · c15-v25-32 51 · c16-v1-8 62 · c16-v9-18 103 · c16-v19-22 50 · c16-v22-31 85 · c17-v1-4 48 · c17-v5-10 48 · c17-v11-19 56 · c17-v20-30 83 · c17-v31-37 56 · c18-v1-8 50 · c18-v9-14 74 · c18-v15-17 41 · c18-v18-27 68 · c18-v28-43 92.

p. 472 nn. 8-12 belong to the next interval (Cap. XIX ¶ 1), which is unbuilt (checker: `p.472: 1-7 (7 notes) ok PENDING n.8,9,10,11,12`; `KNOWN_TOTALS_VOL7[472] = 12`). The p. 381 PENDING of the last gate (nn. 12-13) is now closed by `c15-v1-7`.

## PASS 1: live flags. AS EXPECTED (one `[?]`, recorded)
`check-live-flags.py vol7` scanned 101 chunks. **LIVE [?] FLAGS: 2 occurrences, which is one flag counted in La and En:** `bon-luc-c5-v12-16` l. 279 (`[^p122-11]` **La.** … *A C G E [?]*) and l. 281 (**En.**). This is exactly the resume's one live `[?]` (rulings 59, 73, 90: stays open). Tool exit 0, as at p. 381.

No `[?]` stands in any body or apparatus of the 19 new chunks (the resume's "zero new `[?]` in 19 chunks", item 25, confirmed).

**Every `[so printed]` in the 19 chunks (rendered region only; 3 of the work's 25):**
- `c15-v11-20` l. 123 (¶ 32 **En**): `[so printed: *pedem* for *pedum*]` (Isa. 60:14).
- `c17-v1-4` l. 193 (p. 427 n. 4 **En.**): `[so printed: *eundum* for *eundem*]`.
- `c18-v9-14` l. 84 (¶ 13 **En**): `[so printed: *iuducere* for *inducere*]`. `title_la` keeps *iuducere*; `title_en` translates *inducere* unbracketed (item 20).

All three stand in the English only; each Latin is transcribed as printed with no mark. These are exactly the resume's three (item 23 [37, 125, 219]).

## PASS 2: mechanical suite. CLEAN: every resume START-HERE verification figure reproduced, no corpus divergence
| tool | result | resume "Verification at `bon-luc-c18-v28-43`" |
|---|---|---|
| `check-vol5-apparatus.py --volume=vol7` | **101 chunks, 5,624 entries**, every page 1..N through p. 471; p. 472 `1-7 (7 notes) ok PENDING n.8,9,10,11,12`; **All checks passed** (exit 0) | 101 / 5,624 ✓ |
| `check-vol5-census.py --volume=vol7` | vol7 **101 on disk / 101 in ledger**; **253 runovers (220 gutter / 33 page)**; **95 positive, 6 negative**; "Rosters agree". The six negatives are the old `c10-v38-42`, `c12-v49-59`, `c13-v10-17` and the interval's **`c15-v8-10`**, **`c18-v15-17`**, **`c18-v18-27`** (ledger rows `-`). The interval added **32 runovers (28 gutter / 4 page)**. Its page-crossings are p. 400 n. 12 · 429 n. 12 · 454 n. 14 · 456 n. 16 | 101/101, 253 (220/33), 95/6 ✓ |
| `polish-style-scan.py --volume 7` | **CLEAN (vol7, 101 files)**. Unscoped run: 11 issues / 6 chunks / **2,419 scanned** (`bon-hex-c23` and the same five Vol III/IV Sentences chunks as at p. 381), zero in vol7; exit 1 from those | ✓ |
| `build-citations.py --out/--qa` to the scratchpad | 2,419 chunks; **46,767 ledger records**; **QA 213**; anaphora 2,361 within-chunk + 86 cross-chunk, **unresolved 427**; coordinate ibid. 487 (384 honoured / 103 unresolvable); printed slips (r.57 C2) 23 annotated, 0 stale. **Both outputs byte-identical (`cmp`) to the tracked `index/citations.tsv` and `manual-review/citation-qa-report.md`** | 46,767 / QA 213 / 427 ✓ |
| `site/scripts/build-content.mjs` → `build-index-json.py` → `build-content.mjs` (resume order) | **19 books, 2,418 questions, 2,418 translated** (both runs); **crossref index 1,901 chunks cited, 11,445 backlinks**; scripture 74 books / 32,111; goto 2,418 chunks / 5,457 printed pages; authorities 89 / 437 / 18,989 | 2,418/2,418; 1,901 / 11,445 ✓ |
| `validate-chunk.py` (each of the 19, and each of all 101) | 101 × "1 checked, 0 failed" | OK ✓ |

**One figure in the brief does not match: "build 2,417/2,417".** That is the `c18-v18-27` verification figure (resume l. 90). The current START HERE block says **2,418/2,418** (resume l. 17), and that is what the build gives. This is a briefing slip, not a corpus divergence.

The interval's growth over the p. 381 figures:
- entries +1,195;
- runovers +32 (221 → 253);
- citations +1,959 (44,808 → 46,767);
- anaphora unresolved +36 (391 → 427; the resume's T-a, item "391 → 427 across the interval");
- QA flat at 213;
- crossref +22 chunks cited / +114 backlinks;
- build +19 (2,399 → 2,418);
- goto +91 printed pages (5,366 → 5,457, i.e. pp. 382-472).

**Generated files.**
- `git status --short` before and after the whole suite: `?? .claude/settings.local.json` only.
- `build-citations.py` was pointed at the scratchpad, so no tracked file was rewritten even transiently.
- `build-index-json.py` and `build-content.mjs` write only gitignored files: `site/src/data/*` and `site/public/goto.json`, each listed in `site/.gitignore`, as at p. 381. Nothing tracked changed, so **no `git checkout` restore was needed or made.**
- `index/authorities.tsv` was not regenerated. Per the resume, that is owed before the next deploy, and it is Wilson's call.
- No step was skipped.

## PASS 3: read-through / consistency. No parity defect. All seven KNOWN defects (D-1..D-7) confirmed. THREE NEW undisclosed register findings (N-1..N-3) and one records slip (R-1) for the evidence sheet

Old ground (pp. 3-381, 82 chunks) is byte-unchanged since the p. 381 gate resume commit `dcb721d`: `git diff --stat dcb721d HEAD -- vol7/` lists only the 19 interval files, all pure additions (8,067 insertions, 0 deletions).

### 3a. Per-chunk La/En parity (all 101, computed from the files, then checked against each interval chunk's own Notes claim)
- **Anchors:** in all 101 chunks the `[^pN-n]` sequence is identical La/En, unique, in page/note order, and the anchor set equals the def set (5,624 = 5,624). Interval: 1,195 = 1,195. Every def's page lies in the chunk's `printed_pages`. `pdf_pages` = printed + 26 and contiguous in all 101.
- **Page markers:** identical La/En in all 101, and equal to `printed_pages` in 100. The exception is old-ground `c3-v21-22` (markers 81-84, `printed_pages` 81-85; the p. 84 n. 14 page runover), as at every earlier gate. **Non-defect.**
- **¶ numbers:** La = En in all 101, and each chunk's ¶s run exactly over its frontmatter `paragraphs` range with no gap.
- **`####` headings:** La = En in every interval chunk (4 · 1 · 1 · 0 · 0 · 3 · 1 · 1 · 0 · 2 · 1 · 1 · 4 · 0 · 1 · 0 · 0 · 2 · 0 = 22).
- **Guillemets, paragraph by paragraph:** the « and » counts agree La/En in every ¶ of every chunk. Interval ¶s unbalanced in both languages alike, each disclosed and on the resume (item 26):
  - `c16-v9-18` ¶ 14 10 « / 9 » and ¶ 21 12 / 14 (chunk 153 / 154) [92];
  - `c17-v11-19` ¶ 34 12 / 11 (chunk 75 / 74) [155];
  - `c18-v1-8` ¶ 3 19 / 20 and ¶ 4 5 / 6 (chunk 70 / 72; James 5:15, Job 21:15) [210].

  **Non-defects (recorded).** The other 16 interval chunks balance, chunk by chunk. Old-ground imbalances are unchanged since the earlier gates.
- **Verse tags:** the La and En `(Vers.` sequences agree in every ¶ of all 101. **No English `(V. N.)` body tag stands anywhere in vol7.** Interval La counts: 7 · 3 · 10 · 4 · 8 · 8 · 10 · 4 · 9 · 4 · 5 · 9 · 11 · 7 · 8 · 6 · 3 · 10 · 16 (= 142). Every tag's number falls inside the chunk's `verses`.
  - Multi-verse tags as printed, both languages: `c17-v5-10` *(Vers. 9. 10.)*, `c17-v20-30` *(Vers. 20. 21.)*, `c18-v28-43` *(Vers. 40. 41.)*.
  - Unpointed tags, each disclosed: `c16-v22-31` ¶ 49 *(Vers. 24).* (its Notes, readings (b)) and `c15-v25-32` ¶ 50 *(Vers. 30.)* without the following point (item 24 [63]).
- **Notes self-claims:** in every interval chunk the stated headline (word form), "anchors N = N", the guillemet totals, "`(Vers.` N = N", "page markers N = N" and "`####` N = N" (where stated) all equal the file. **No false self-claim in the interval.**
  - One recorded convention split: `c16-v19-22`'s headline reads "FIFTY-ONE APPARATUS ENTRIES (50 numbered + `tr-lumen`)", counting its translator's note.
  - `c18-v9-14` (74 + two `tr-`) and `c18-v28-43` (92 + `tr-lumen`) count numbered entries only.
  - Self-explained, so not false; for the records only.

### 3b. Register-term census, pp. 381-472 (19 chunks; RENDERED region only: `## Latin`, `## English`, and the **La.** / **En.** apparatus halves; Notes, frontmatter and `tr-` definitions excluded; anchors stripped; ¶-aligned and entry-aligned La vs En)
| Latin | English | La / En (bodies; apparatus) | units where La > En, resolved |
|---|---|---|---|
| *pietas* (rr. 12, 31, 86) | piety | 81 / 78 (74/74; 7/4) | 3, all apparatus variant readings quoted in Latin italic, which the En half keeps (p. 389 n. 10, p. 423 n. 8, p. 425 n. 11). Non-defect |
| *pius* / *pie* | pious / piously | 11 / 12 (11/12; 0/0) | 0. II Pet. 2:9 *Novit Dominus pios* "the pious" (`c17-v20-30` ¶ 48) |
| *impietas* / *impius* (r. 86) | impiety / impious | 72 / 41 (63/38; 9/3) | 31 units. Almost all are Douay "the wicked" / "the ungodly" / "wickedness" inside verses (Prov., Job, Ezech., Wis., Ecclus., II Mach., II Pet.: r. 86's "nearest Douay word in verses"), plus Latin variant readings kept in the En half (pp. 403 n. 6, 407 n. 9, 421 n. 6). The exceptions: **`c18-v18-27` ¶ 44 — NEW finding N-3 below**; and `c16-v19-22` p. 417 n. 6 (observation O-3) |
| *poena* (house rule `CLAUDE.md:3502`; D-4) | punishment | 30 / 53 "punish-" (22/45; 8/8) | **2: `c16-v1-8` p. 405 n. 3 "penalties" — NEW finding N-1; `c16-v19-22` p. 417 n. 12 "pains" — NEW finding N-2.** Every other *poena* site is "punishment", incl. `c17-v20-30`'s conformed triads (D-4, `e810ccc`) |
| *supplicium* (r. 87, item 14) | punishment / torment | 19 / 77 (18/66; 1/11) | 0. "punishment" at every site except `c18-v28-43` ¶¶ 52, 55 *acerbitas supplicii* "the bitterness of the torment" (the Passion; item 14 [272], disclosed). En surplus = *tormenta* / *cruciatus* "torment(s)" |
| **"penalty" in the rendered English** | — | **1** | **`c16-v1-8` l. 252 only (N-1). The interval's English otherwise holds zero "penalt-".** For scale only, outside scope: old ground holds ≥ 19 "penalt-" in 10 chunks (`c1-v18-25`, `c1-v57-66`, `c4-v1-13`, `c4-v38-44`, `c6-v20-26`, `c6-v27-31`, `c6-v32-38`, `c7-v24-35`, `c9-v32-36`, `c12-v49-59`). They are not classified here; that is for item 14's ruling, if Wilson wants it to reach back |
| *lux* | light | 24 / 38 (20/32; 4/6) | 0 |
| *lumen* (rr. 27, 50, 78-80) | lumen | 14 / 10 "lumen" (12/8; 2/2) | 3, all known: Ps. 35:10 "light" at `c17-v31-37` ¶ 62 (**D-2**); Rom. 2:19 *lumen eorum* "light" at `c18-v9-14` ¶ 14 (exempt, item 13 [221]); John 8:12 *lumen vitae* "the light of life" at `c18-v28-43` ¶ 66 (exempt, item 13 [271]) |
| **Ps. 35:10** *in lumine tuo videbimus lumen* | — | 2 sites | `c16-v19-22` ¶ 39 (En l. 95) "in thy lumen we shall see lumen", with the chunk's `tr-lumen`; `c17-v31-37` ¶ 62 (En l. 93) "in thy light we shall see light". That is **D-2** exactly; no third site in the interval |
| *puer* (r. 54, item 12) | boy | 66 / 56 "boy(s)" (54/45; 12/11) | 4 units: `c18-v15-17` ¶ 31 (24 / 17: the three "servant" verses Job 29:5, Ps. 104:42, Matt. 12:18, Luke 1:54 "his child", and *puer* named in Latin italic ×3, all item 12 [239]); p. 459 n. 14 Luke 1:73 *puerum suum* kept in Latin; `c17-v20-30` ¶ 49 Gen. 19:4 *a puero usque ad senem*, Douay; **`c18-v1-8` ¶ 8 Luke 11:7 *pueri mei* "my children" — observation O-1** |
| *intellectus* (noun) | understanding | 13 / 19 (12/19; 1/0) | 3: `c15-v1-7` ¶ 7 *intellectuum divinorum* "the divine understandings" (plural; counted once by the En regex); `c15-v11-20` ¶ 28 Isa. 28:19 Douay; p. 384 n. 3 Latin variant. Bare "intellect": 1, `c18-v9-14` ¶ 26 *in intellectu … in affectu* (r. 32's formula, item 16 [229]) |
| *affectus* (noun) | affection | 19 / 22 (16/20; 3/2) | 1: p. 387 n. 4 Latin variant. **D-3** (`c17-v1-4` ¶ 11 / `c17-v5-10` ¶ 14 "the understanding … the affection") confirmed in place |
| *pudicitia* (r. 19, item 17) | purity | 4 / — | All at `c15-v20-24` ¶ 38 "purity", beside ¶ 37's *interior puritas* "interior purity" (one English root, item 17 [46]). No other *pudicitia* in the interval |
| *puritas* | purity | 11 / 14 (11/14) | 0 |
| *praeco* (r. 30, item 19) | herald | 2 / — | Chrysostom's *praecone* "herald" (`c17-v20-30` ¶ 42); II Pet. 2:5 *praeconem* "the preacher of justice" (¶ 48, Douay; item 19 [167]). No third *praeco* |
| *praeconium* (r. 30) | proclamation | 5 / 5 | 0. **Zero "proclaim" in the interval's rendered English** |
| *lucerna* (r. 32 / 88) | lamp | 11 / 12 (9/10; 2/2) | 0. **No "candle" or "lantern"**; the one "candlestick" is Apoc. 2:5 *candelabrum* (`c16-v1-8` ¶ 7) |
| *excessivus* (r. 81) | transporting | 2 / 2 | 0. `c17-v31-37` ¶ 62 and p. 447 n. 13 *motum amoris excessivum* "transporting motion of love" (item 19 [185]) |
| *excessus* (r. 67 / 81) | transport / excess | 2 / — | p. 407 n. 8 Aristotle's *excessus … defectus* "the excess … the defect" (the measure sense; correct); p. 471 n. 1 Vat. *excessum* for *excedentiam*, glossed "excess" (observation O-2) |
| *excedere* / *excedentia* | exceed / transport | 10 / 24 | 0 short. `c18-v28-43` ¶ 63 *supra nos excedimus* "are transported above ourselves" and p. 471 n. 1 *excedentiam* "exceedingness" (item 19 [276]); II Cor. 5:13 "transported in mind" (`c15-v25-32` ¶ 52) |
| *credulitas* / *incredulitas* (r. 55) | belief / unbelief | 2 / 2 | 0. `c18-v1-8` ¶ 12 *fides credulitatis* "the faith of belief"; `c16-v22-31` ¶ 60 *incredulitatem* "unbelief". **No "credulity"** |
| *eruditio* (r. 82) | erudition | 1 / 1 | 0. Prov. 1:3 *eruditionem doctrinae* "the erudition of doctrine" (`c15-v1-7` ¶ 7). *erudire* 1 / 3 "school" |
| *Spiritus Sanctus* (r. 83) | Holy Spirit | 12 / 13 | 0. **Zero "Holy Ghost" in the interval's rendered region** |

**`tr-pietas` placement (r. 86: at the first divine site of each chunk), file-side.** Nine chunks carry one:
- the five Cap. XV chunks: ¶¶ 1, 15, 21, 33, 42;
- `c16-v1-8` ¶ 1, the look-back "divine piety" (item 15 [81]);
- `c17-v11-19` ¶ 29, *mira Dei pietas* (item 15 [150]);
- `c18-v1-8` ¶ 9, *Deum pium et iustum*, a divine ADJECTIVE (item 15 [201]);
- `c18-v9-14` ¶ 23, *nomen summae pietatis* (item 15 [220]).

In each, no rendered "piety" / "pious" stands before the anchor. Divine *pietas* with no note occurs at one site only: **D-5** (but see R-1 on its paragraph number). The other ten chunks have human *pietas* only, or none:
- `c16-v19-22` and `c16-v22-31`: the divisio look-backs and ¶ 56;
- `c17-v1-4` and `c17-v5-10`: *pietas spiritualis*;
- `c17-v20-30`: ¶ 35;
- `c18-v18-27`: ¶ 38, Ambrose, item (260);
- `c16-v9-18` (bar D-5), `c17-v31-37`, `c18-v15-17` and `c18-v28-43`.

**NEW FINDINGS (not on the resume's D-list or its items 1-31; each undisclosed in its chunk's Notes). Register calls for Wilson; reported here with exact file:line, not decided.**

- **N-1. *poena* rendered "penalties", against the house rule (`CLAUDE.md:3502`, *poena* "punishment") and the brief's zero-"penalty" test.**
  - `vol7/bon-luc-c16-v1-8.md` l. 252 (p. 405 n. 3 **En.**; La l. 250): the *Interlinear* Gloss, *ut poenas evitem* → "that I may avoid the **penalties**".
  - This is the only "penalt-" in the 19 chunks' rendered English. It is the exact word item 14 / D-4 conformed away at `c17-v20-30`.
  - The chunk's Notes are silent. The fix would be one word ("punishments").
- **N-2. *poena* rendered "pains".**
  - `vol7/bon-luc-c16-v19-22.md` l. 242 (p. 417 n. 12 **En.**; La l. 240): Chrysostom, *ut magnitudo poenarum faceret magnitudinem misericordiae* → "that the greatness of the **pains** might make the greatness of the mercy".
  - The sense is Lazarus's bodily sores, so "pains" is a sense rendering. But the house row admits no sense split for *poena* (ruling 87's "by sense" licence was given to *supplicium*).
  - Undisclosed (the chunk's Notes list this note's loci only). Keep as a disclosed exception, or "punishments".
- **N-3. *impie* rendered "wicked one" in a Father's prose, against ruling 86** ("*impietas / impius* 'impiety / impious' in prose, the nearest Douay word in verses").
  - `vol7/bon-luc-c18-v18-27.md` l. 118 (¶ 44 **En**; La l. 67): Bernard, *Non sic, impie, non sic ingredieris* → "Not so, **wicked one**, not so shalt thou go in".
  - It is Bernard's prose, not a verse, so nothing licenses the Douay word.
  - Undisclosed. One word ("impious one").

**RECORDS SLIP (no text effect):**
- **R-1. D-5's paragraph number.** Several places put `c16-v9-18`'s *invitando ad pietatem divinam* at ¶ 22: the chunk's own Notes item (88), the resume's item 15 and D-5, and the consolidated docket. In the file it stands in ¶ 21's block. La l. 59, En l. 136 ("dissuading worldly cupidity and inviting to divine piety") sit between the `21.` numeral at La l. 57 / En l. 134 and `22.` at La l. 61 / En l. 138. The text is not in question, only the citation. If the docket is right and the file's `22.` numeral is misplaced, only the plate (p. 410) can say so (see "Plate-only" below).

**OBSERVATIONS (disclosed or doubtful; recorded, not counted as defects):**
- **O-1. Luke 11:7 *pueri mei* is rendered both ways inside the interval.** "my children" stands at `vol7/bon-luc-c18-v1-8.md` ¶ 8 (En l. 106, Douay; nothing leans; not named in its Notes). "my boys" stands at `vol7/bon-luc-c18-v15-17.md` ¶ 31 (En l. 67; adjusted, ¶ 31 leans). `c18-v15-17`'s disclosure names only `c11-v5-13`'s "my children" as the split. The interval holds a second, closer one. That is one more site for item 11 / item 12, not a separate question.
- **O-2.** `c18-v28-43` p. 471 n. 1 **En.** (l. 448): Vat. *excessum* (for *excedentiam*) is glossed "excess". Ruling 81's sense test would read the noun from the body's *excedentia desiderii*. For item 19 [276], which already asks for the *excedere* forms.
- **O-3.** `c16-v19-22` p. 417 n. 6 **En.** (l. 218): the Vatican addition *qui ab Evangelista ostenditur misericordia dignus, et dives ille per consequens immisericors et impius* is quoted in Latin italic with no English gloss. Elsewhere in the interval a quoted variant is usually glossed in parentheses (e.g. p. 465 n. 10). Recorded only.

**The seven KNOWN defects, all confirmed in place, none edited:**
- D-1: the four manifest cells (item 4). The file side agrees with the builders:
  - `c16-v1-8` `title_la` = *Exemplum parabolicum pietatis providae*, against the manifest's *Primo, de pietate humana quoad opera corporalia tripliciter.* (3d).
  - The three `headings` omissions are manifest-only; the chunks carry the headings (`c15-v1-7` four `####`, `c16-v1-8` three, `c17-v20-30` four).
- D-2: Ps. 35:10, `c16-v19-22` l. 95 "lumen" / `c17-v31-37` l. 93 "light".
- D-3: `c17-v1-4` ¶ 11 (l. 117) and `c17-v5-10` ¶ 14 (l. 78) "the understanding … the affection".
- D-4: `c17-v20-30` *poena* "punishment" at every site (the `e810ccc` conformation is in the tree; zero "penalt-" in that chunk).
- D-5: `c16-v9-18` l. 136 "divine piety", no `tr-pietas` (¶ 21 by the file: R-1).
- D-6: `c17-v31-37` l. 129 (p. 444 n. 8 **La.**) *Ducange*, against 55 "Du Cange" in the work.
- D-7: Luke 17:19 "made thee safe" at `c17-v11-19` l. 117 (¶ 34) and Luke 18:42 "made thee whole" at `c18-v28-43` l. 150 (¶ 65).

**Mechanically:**
- **Ruling 83:** zero "Holy Ghost".
- **Ruling 82:** *eruditio* "erudition" 1 / 1.
- **Ruling 81:** *excessivus* "transporting" 2 / 2.
- **Ruling 30:** zero "proclaim"; the one *praeco* "preacher" is item 19 [167].
- **Ruling 55:** zero "credulity".
- **Lucerna:** zero "candle".
- **Ruling 86:** one prose *impius* off-rule (N-3).
- **House *poena* row:** two off-rule (N-1, N-2).

### 3c. `tr-` note inventory, pp. 381-472: 14 notes, every def anchored exactly once, every anchor defined, NO new id
- `c15-v1-7` pietas (¶ 1, at the divisio's "works of piety", r. 86)
- `c15-v8-10` pietas (¶ 15)
- `c15-v11-20` pietas (¶ 21)
- `c15-v20-24` pietas (¶ 33)
- `c15-v25-32` pietas (¶ 42)
- `c16-v1-8` pietas (¶ 1)
- `c16-v19-22` lumen (¶ 39, Ps. 35:10; D-2)
- `c17-v11-19` praeceptor (¶ 25, Luke 17:13 *Iesu praeceptor*, r. 69), pietas (¶ 29)
- `c17-v31-37` evangelizare (¶ 54, Isa. 40:9; item 18 [188])
- `c18-v1-8` pietas (¶ 9, the divine adjective; item 15 [201])
- `c18-v9-14` pietas (¶ 23); lumen (**inside p. 457 n. 10 En.**, Bernard's apparatus-only *lumen*; item 13 [221])
- `c18-v28-43` lumen (¶ 57)

That makes 9 `tr-pietas`, 3 `tr-lumen`, 1 `tr-praeceptor` and 1 `tr-evangelizare`.
- There is no `tr-` anchor in any Latin body.
- Thirteen of the fourteen are anchored in an English body. One, `c18-v9-14`'s `tr-lumen`, is anchored in the **En.** half of an apparatus entry, the shape of the old-ground Corrigenda notes.
- **New ids: none.** All four ids were already in use on old ground (`tr-pietas` in 10 chunks, `tr-lumen` 16, `tr-praeceptor` 5, `tr-evangelizare` 7).
- The interval has no `tr-corrigenda` (item 7: no Corrigenda in pp. 381-472), and no `tr-vacare`, `tr-excessus` or `tr-annuntiare`.
- Vol VII total: 65 + 14 = **79** (tr-pietas 19 · tr-lumen 19 · tr-corrigenda 14 + tr-corrigenda-2 1 · tr-vacare 9 · tr-evangelizare 8 · tr-praeceptor 6 · tr-annuntiare 2 · tr-excessus 1).

### 3d. Frontmatter / `printed_pages` continuity, pp. 381-472: no gap, no overlap, no abutment
- `pdf_pages` = printed + 26 and contiguous in all 101.
- **Every one of the 19 seams shares exactly its seam page; no abutment:** pp. 381 (from `c14-v25-35`), 387, 389, 394, 398, 402, 407, 415, 419, 425, 429, 433, 437, 444, 448, 452, 457, 460, 465. p. 472 is the interval's last page and is shared with the unbuilt Cap. XIX ¶ 1.
- **`division` / `section`:** `division` steps 15 → 16 → 17 → 18 once each. `section` runs XV 1-5 · XVI 1-4 · XVII 1-5 · XVIII 1-5. The manifest has no `section` cell (empty column), so this was checked from the files.
- **`paragraphs` / `verses`:** `paragraphs` restart at 1 at each capitulum and are contiguous within it. `verses` are contiguous: each chunk opens on the previous one's last verse or the next. Exactly two verses are shared across a seam, as the manifest draws them: 15:20 (`c15-v11-20` / `c15-v20-24`) and 16:22 (`c16-v19-22` / `c16-v22-31`). No other overlap.
- **Each capitulum closes on Luke's last verse:** XV 32 · XVI 31 · XVII 37 · XVIII 43. **Last ¶ per capitulum: XV 52 · XVI 61 · XVII 62 · XVIII 66**, as item 3 and the setup table have them.
- Every chunk's `division`, `verses`, `paragraphs`, `first_page` and `last_page` equal its manifest row.
- **`title_la`:** in 18 of 19 chunks it equals the manifest's cell (the final point dropped, the house form). In every chunk it occurs verbatim in the Latin body, heading or divisio sentence, where its Notes say it was read on the plate.
- **The one divergence is `c16-v1-8`: `title_la` *Exemplum parabolicum pietatis providae*, the lower 402R t4, against the manifest's *Primo, de pietate humana quoad opera corporalia tripliciter.*** That is **D-1 / item 4(c)**, built so under ruling 22 and disclosed in the chunk's Notes (gate item (72)).
- The sentence titles:
  - `c15-v20-24`, `c15-v25-32`, `c16-v22-31`, `c17-v31-37`, `c18-v9-14`, `c18-v15-17`, `c18-v28-43` = lemma + dividing words, `(Vers.` omitted as at every sentence title.
  - `c18-v9-14` keeps *iuducere* (item 20).

### 3e. Hand-offs at every shared page, pp. 381-472 (file ownership derived from the defs; each split checked against BOTH chunks' Notes)
| page | A nn. / B nn. | page | A nn. / B nn. |
|---|---|---|---|
| 381 | c14-v25-35 1-11 / c15-v1-7 12-13 | 429 | c17-v1-4 1-9 / c17-v5-10 10-12 |
| 387 | c15-v1-7 1 / c15-v8-10 2-13 | 433 | c17-v5-10 1-8 / c17-v11-19 9-14 |
| 389 | c15-v8-10 1-9 / c15-v11-20 10-12 | 437 | c17-v11-19 1-4 / c17-v20-30 5-10 |
| 394 | c15-v11-20 1-11 / c15-v20-24 12-14 | 444 | c17-v20-30 none / c17-v31-37 1-15 |
| 398 | c15-v20-24 1-11 / c15-v25-32 12-14 | 448 | c17-v31-37 1-2 / c18-v1-8 3-11 |
| 402 | c15-v25-32 1-7 / c16-v1-8 8-10 | 452 | c18-v1-8 1-6 / c18-v9-14 7-13 |
| 407 | c16-v1-8 1-9 / c16-v9-18 10-12 | 457 | c18-v9-14 1-10 / c18-v15-17 11-12 |
| 415 | c16-v9-18 1-6 / c16-v19-22 7-8 | 460 | c18-v15-17 1-9 / c18-v18-27 10-13 |
| 419 | c16-v19-22 1-6 / c16-v22-31 7-13 | 465 | c18-v18-27 1-9 / c18-v28-43 10-15 |
| 425 | c16-v22-31 1-10 / c17-v1-4 11-12 | 472 | c18-v28-43 1-7 / next interval 8-12 PENDING |

On every page the two halves make one contiguous 1..N register, and the apparatus checker confirms N against `KNOWN_TOTALS_VOL7`.
- **Where the outgoing chunk holds notes on the page (18 pages),** its Notes state the "nn. a-b" range literally, with "PENDING nn. …" for the next chunk. The incoming chunk's Notes state the same range as "the hand-off received". Every PENDING of the interval is closed by its successor.
- **Where the outgoing chunk holds none (p. 444),** `c17-v20-30`'s Notes say so in terms: "p. 444 is SHARED, but forwards NOTHING to us and receives nothing from us … p. 444's notes are yours (n. 1 at ¶ 53's *die* …)". Its text on the leaf is ¶ 52's unanchored close.
- **The p. 381 PENDING of the last gate (nn. 12-13) is closed as handed off:** `c15-v1-7` owns them, and its Notes read "ours nn. 12–13".
- **p. 429 n. 12** is a page-crossing runover onto p. 430. It is owned by `c17-v5-10`, ledgered there (`p.429 n.12:page`), and recorded in both chunks.
- p. 472 nn. 8-12 are named in the resume START HERE block (n. 8 at *secundo*, n. 9 at *ibi*, n. 10 at *caelum*, n. 11 at *ibi*, n. 12 at *descit*). They are the next interval's.

### Plate-only questions (no plate read in this run)
- **R-1:** whether the `22.` numeral of `c16-v9-18` stands where the file has it (La l. 61, *Secundo quantum ad assertionem reprobationis*) or one sentence earlier, which would put *invitando ad pietatem divinam* in ¶ 22 as the docket says (p. 410). File-side the La and En agree on ¶ 21, so this matters only if the docket's number is to be kept.
- Nothing else in this pass needs a plate. N-1 to N-3 and O-1 to O-3 are English-side calls on Latin that is not in doubt.

## Summary
- **Pass 1:** as expected. One live `[?]`, `c5-v12-16` p. 122 n. 11, La + En (rulings 59 / 73 / 90). Exit 0. There is no `[?]` in the 19 interval chunks.
  - Three `[so printed]`, all English-side: `c15-v11-20` l. 123 *pedem*, `c17-v1-4` l. 193 *eundum*, `c18-v9-14` l. 84 *iuducere*.
- **Pass 2:** clean. Every resume figure was reproduced exactly:
  - apparatus: 101 chunks / 5,624 entries; p. 472 nn. 8-12 PENDING;
  - census: 101/101, 253 runovers (220 / 33), 95 positive and 6 negative;
  - style scan: CLEAN (101 files);
  - citations: 46,767 records, QA 213, both byte-identical to the tracked files;
  - anaphora: 427 unresolved;
  - crossref: 1,901 chunks cited / 11,445 backlinks;
  - build: **2,418 / 2,418**. The brief's "2,417" is the previous chunk's figure, and the current resume line says 2,418;
  - `validate-chunk.py`: OK × 101.

  No tracked file changed, so no restore was needed.
- **Pass 3:** La/En parity holds in every ¶ of all 101 chunks: anchors, page markers, ¶ numbers, `####`, guillemets and verse tags. The `c3-v21-22` page-marker exception is the known one. No interval Notes self-claim is false. The 14 interval `tr-` notes are all paired, and no id is new. Old ground is byte-unchanged since `dcb721d`. There is no page gap, overlap or abutment (19 shared seams). The hand-offs agree on all of them and on p. 472's PENDING. Last ¶ per capitulum is XV 52 · XVI 61 · XVII 62 · XVIII 66.
- **Known defects D-1 to D-7:** all confirmed in place (3b). None was touched.
- **NEW findings (register, undisclosed; for the evidence sheet):**
  - **N-1:** *poenas* "penalties" at `c16-v1-8` l. 252 (p. 405 n. 3 **En.**). This is the interval's only "penalt-", against the house *poena* row.
  - **N-2:** *poenarum* "pains" at `c16-v19-22` l. 242 (p. 417 n. 12 **En.**).
  - **N-3:** Bernard's *impie* "wicked one" at `c18-v18-27` l. 118 (¶ 44), against ruling 86.
- **Records slip R-1:** D-5's site is ¶ 21 in the file, not ¶ 22 as the chunk's Notes, the resume and the docket say.
- **Observations:**
  - O-1: Luke 11:7 "my children" (`c18-v1-8` l. 106) / "my boys" (`c18-v15-17` l. 67) inside the interval.
  - O-2: p. 471 n. 1 Vat. *excessum* "excess".
  - O-3: p. 417 n. 6's unglossed Latin variant.
