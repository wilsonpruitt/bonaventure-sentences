# Vol VII *Lucam* p. 540 gate: passes 1-4 DRAFT (read-only agent, 2026-11-20)

Phase 1 only. No chunk, tool, manifest row, ruling, resume note or plate was edited or deleted. Nothing was pushed or deployed; no `git stash`. Scratch scripts and the two `build-citations.py` outputs live in the agent's scratchpad (`g540/`), not the repo. Register questions to Wilson belong to the evidence sheet (`vol7-lucam-p540-gate-evidence-sheet.md`); the findings here are cross-referenced to its item numbers (105–130). Model: `vol7-lucam-p472-gate-passes-draft.md`.

**Scope:** 119 chunks, pp. 3-540, **6,522 numbered apparatus entries** + **92** `tr-` notes. The new ground is the 18 chunks `bon-luc-c19-v1-10` → `bon-luc-c21-v28-38`, pp. 472-540 (manifest stage 6, `lucam-chunk-manifest.tsv` rows 103-120; XIX 7 · XX 5 · XXI 6). They hold **898 entries** (5,624 + 898 = 6,522) + **13** `tr-` notes (79 + 13 = 92).

Entries per chunk: c19-v1-10 65 · c19-v11-14 40 · c19-v15-19 43 · c19-v20-28 51 · c19-v29-35 57 · c19-v36-40 48 · c19-v41-48 75 · c20-v1-9 45 · c20-v10-18 66 · c20-v19-26 39 · c20-v27-40 57 · c20-v41-47 48 · c21-v1-4 41 · c21-v5-11 49 · c21-v12-19 45 · c21-v20-24 35 · c21-v25-27 38 · c21-v28-38 56.

p. 540 nn. 2-10 belong to the next interval (Cap. XXII), which is unbuilt and whose manifest stage 7 is not drawn (checker: `p.540: 1-1 (1 notes) ok PENDING n.2,3,4,5,6,7,8,9,10`; `KNOWN_TOTALS_VOL7[540] = 10`). The p. 472 PENDING of the last gate (nn. 8-12) is closed by `c19-v1-10`.

**One plate was looked at in this run**, as one downscaled overview crop: p. 518 rows 0.25-0.65, to settle which of two builders' position figures for the 518L t4 is right (sheet item 122). Nothing else needed a plate.

## PASS 1: live flags. AS EXPECTED (one `[?]`, recorded)

`check-live-flags.py vol7` scanned 119 chunks. **LIVE [?] FLAGS: 2 occurrences, which is one flag counted in La and En:** `bon-luc-c5-v12-16` l. 279 (`[^p122-11]` **La.** … *A C G E [?]*) and l. 281 (**En.**). This is the one live `[?]` of rulings 59, 73, 90, 102 (stays open). Tool exit 0.

No `[?]` stands in any body or apparatus of the 18 new chunks. (The string `[?]` occurs once in each of the 18 at l. 17, inside the frontmatter `transcription_status` sentence "zero [?]"; the checker rightly does not count it.)

**Every `[so printed]` in the 18 chunks (rendered region; 3, as the resume says):**
- `c19-v41-48` l. 104 (¶ 65 **En**): `[so printed: *novissorum* for *novissimorum*]` (Ecclus. 38:21).
- `c20-v1-9` l. 110 (¶ 10 **En**): `[so printed: *commitiendo* for *committendo*]`.
- `c20-v10-18` l. 355 (p. 508 n. 13 **En.**): `[so printed: *itam* for *ita*]`.

All three stand in the English only. None of the three forms is in the Vol VII Corrigenda table (`vol7-pilot-setup.md` ll. 147-165; the one interval entry is p. 533 col. 2 l. 11 *poterunt* → *poterant*, applied by `c21-v25-27`'s `tr-corrigenda`).

## PASS 2: mechanical suite. CLEAN: every resume START-HERE figure reproduced, no divergence

| tool | result | resume "Verification at `bon-luc-c21-v28-38`" |
|---|---|---|
| `check-vol5-apparatus.py --volume=vol7` | **119 chunks, 6,522 entries**, every page 1..N through p. 539; p. 540 `1-1 (1 notes) ok PENDING n.2..10`; **All checks passed** (exit 0) | 119 / 6,522 ✓ |
| `check-vol5-census.py --volume=vol7` | vol7 **119 on disk / 119 in ledger**; **285 runovers (247 gutter / 38 page)**; **112 positive, 7 negative**; "Rosters agree" | 119/119, 285 (247/38), 112/7 ✓ |
| `polish-style-scan.py --volume 7` | **CLEAN (vol7, 119 files)**, exit 0 | ✓ |
| `validate-chunk.py` on each of the 18 | 18 × "1 checked, 0 failed" | OK ✓ |
| `build-citations.py --out/--qa` to the scratchpad | 2,437 chunks scanned; **48,221 ledger records** (scripture 33,480 · crossref 13,574 · authority 1,167); **QA 213**; anaphora 2,372 within-chunk + 86 cross-chunk, **unresolved 442**; coordinate ibid. 492 (388 honoured / 104 unresolvable); printed slips (r.57 C2) 23 annotated, 0 stale. **Both outputs byte-identical (`cmp`) to the tracked `index/citations.tsv` and `manual-review/citation-qa-report.md`** | 48,221 / QA 213 / 442 ✓ |
| `site/scripts/build-content.mjs` → `build-index-json.py` → `build-content.mjs` | **19 books, 2,436 questions, 2,436 translated** (both runs); **crossref index 1,917 chunks cited, 11,533 backlinks**; goto 2,436 chunks / 5,525 printed pages; authorities 89 / 437 / 18,989 | 2,436/2,436; 1,917 / 11,533 ✓ |

The interval's growth over the p. 472 figures:
- entries +898 (5,624 → 6,522);
- runovers +32 (253 → 285): **27 gutter + 5 page**. The five page-crossings are **p. 478 n. 14 · 485 n. 15 · 488 n. 11 · 507 n. 15 · 513 n. 14**. (The resume's consolidated item 6 names three of them; p. 488 n. 11, `c19-v29-35`, and p. 513 n. 14, `c20-v27-40`, are ledgered and in their chunks' Notes but missing from that sentence: a docket omission, sheet item 128.) One negative ledger row in the interval: `c20-v41-47` (`-`);
- citations +1,454 (46,767 → 48,221); the interval's own 1,454 records: scripture 1,346 (999 verse / 347 chapter), crossref 108 (87 chunk · 15 unresolvable · 4 page-multi · 1 distinctio · 1 articulus);
- anaphora unresolved +15 (427 → 442); QA flat at 213;
- crossref +16 chunks cited / +88 backlinks; build +18 (2,418 → 2,436); goto +68 printed pages (pp. 473-540).

**Generated files.** `git status --short` before and after the whole suite: `?? .claude/settings.local.json` only. `build-citations.py` was pointed at the scratchpad. `build-index-json.py` and `build-content.mjs` write only gitignored files (`site/src/data/*`, `site/public/goto.json`). Nothing tracked changed, so **no `git checkout` restore was needed or made.** `index/authorities.tsv` was not regenerated (still owed before the next deploy, Wilson's call). `vercel build` not run. No step was skipped.

## PASS 3: read-through / consistency. THREE defects the builders did not record (N-1..N-3), ONE builder claim that is wrong (N-4), one records slip (R-1); all six recorded defects D-1..D-6 confirmed, three of them wider than recorded

Old ground (pp. 3-472, 101 chunks) is byte-unchanged since the p. 472 gate's apply commit `3114828`: `git diff --stat 3114828 HEAD -- vol7/` lists only the 18 interval files, all pure additions (6,356 insertions, 0 deletions).

**How pass 3 was run.** By script over the rendered region of every chunk (bodies ¶-aligned La/En; apparatus entry-aligned), not by a reader fleet: the brief allowed subagents, but a fleet over 1.4 MB of chunk text is a six-figure token job, and Wilson's standing rule asks for his own word before one. Every finding below was then read by eye at its site. What a script cannot see (a mistranslation that keeps the right words) is therefore not covered beyond the register census; that is the pass's stated limit.

### 3a. Per-chunk La/En parity (the 18, computed from the files)
- **Anchors:** in all 18 the `[^pN-n]` sequence is identical La/En, unique, in page/note order, and the anchor set equals the def set (898 = 898). Every def has both a **La.** and an **En.** half. Every def's page lies in the chunk's `printed_pages`. `pdf_pages` = printed + 26 in all 18.
- **Page markers:** identical La/En in all 18, and equal to `printed_pages`.
- **¶ numbers:** La = En in all 18, and each chunk's ¶s run exactly over its frontmatter `paragraphs` range with no gap.
- **`####` headings:** La = En in every chunk (1 · 0 · 0 · 0 · 3 · 0 · 3 · 2 · 0 · 0 · 2 · 3 · 1 · 1 · 0 · 0 · 0 · 0 = 16), and equal to the manifest's `headings` cell (t3 / t4 count) in every row.
- **Guillemets:** « = » in every chunk, La and En alike (89 · 49 · 55 · 74 · 63 · 61 · 105 · 63 · 74 · 53 · 68 · 76 · 59 · 63 · 63 · 52 · 61 · 91); counts agree La/En paragraph by paragraph.
- **Verse tags:** the La and En `(Vers.` sequences agree in every ¶. No English `(V. N.)` body tag. Counts 10 · 4 · 5 · 9 · 7 · 5 · 8 · 9 · 9 · 8 · 11 · 6 · 4 · 6 · 7 · 5 · 3 · 10 (= 126). Every tag's number falls inside the chunk's `verses`.
- **Untranslated Latin in the English:** a screen for Latin function words standing outside italics in every English ¶ and every **En.** half returns one hit in 898 entries + 18 bodies, and it is right: p. 532 n. 3 quotes the Vulgate's *Ex iniquis enim somnis filii* with only *somnis* italic, as the **La.** half prints it, and glosses it. No **En.** half repeats its **La.** half. Digit parity La/En per entry: two differences, both right (p. 513 n. 6's gloss "John 11"; p. 533 n. 10's "(c. 4)").
- **⚠ Paragraph shape — NEW finding N-3** (sheet item 121), five places in three chunks, none in any Notes:
  - `c20-v10-18` **Latin** l. 36: ¶ 16 (`16. (Vers. 11.). Secundo quantum ad …`) follows ¶ 15's last line with **no blank line** (English ll. 77-79 have it). The site splits paragraphs on blank lines (`site/src/lib/paragraphs.ts` l. 46), so on the page the Latin ¶ 16 runs on inside ¶ 15 and the chunk's Latin has one paragraph fewer than its English from there down.
  - `c19-v1-10` **English**: a stray hard line break inside ¶ 5 (ll. 102/103, "… those wishing ⏎ to come to Christ"), ¶ 7 (ll. 109/110) and ¶ 9 (ll. 118/119). `c21-v12-19` **English**: one inside ¶ 25 (ll. 86/87). The Latin has none of the four. A soft break renders as a space, so nothing shows on the page; the file shape is off (the work's rule is one paragraph, one line, as the line counts La 31 / En 34 and La 19 / En 20 show).

  `validate-chunk.py` and the style scan pass all five. For scale: the same screen finds the same stray-break shape at 102 places in 26 old-ground chunks (all mid-paragraph, none a numbered paragraph run on for want of a blank line); those passed four gates and are not this gate's ground.

### 3b. Register census, pp. 472-540 (18 chunks; rendered region only; ¶-aligned and entry-aligned)

| Latin | English | La / En | what the census found |
|---|---|---|---|
| *virtus* (r. 47) | power; the moral virtue "virtue" | 58 La | **D-1 confirmed and wider than recorded.** `c19-v29-35` renders *virtus* "virtue" at **8 sites on 5 lines**, not only ¶ 50's two: ¶ 44 Ambrose *in sublimi virtute* (l. 91), ¶ 46 *non est virtute humana, sed divina* (l. 99), ¶ 50 ×5 (ll. 111, 113), p. 490 n. 12 the Gloss's *virtus emineat* (l. 298); its Notes say "*virtus* 'virtue' throughout". ¶ 52's *doctrina virtutum* is the moral virtue and is right. And `c21-v25-27` ¶ 44 (l. 70) + p. 534 n. 11 (l. 160) render Chrysostom's / Jerome's *resistendi virtus* "strength of resisting" (undisclosed). Sheet item 105 |
| *poena* (`CLAUDE.md:3502`; r. 94) | punishment | 12 / 10 | **NEW finding N-1:** `c20-v27-40` ¶ 37 (l. 94) and p. 513 n. 8 **En.** (l. 196), *poena discalceationis* "the **penalty** of unshoeing" ×2, undisclosed; the p. 472 gate's N-1 class exactly. Sheet item 119 |
| *supplicium* (r. 94) | penalty | 1 / 1 | `c19-v41-48` p. 496 n. 4 *inferni supplicia* "the penalties of hell" ✓ |
| *simulatio* (rr. 88, 96) | dissembling | 14 La | `c20-v19-26` ¶ 26 "dissembling" 4 / 4 (its Luke 20:20 lemma keeps the Douay's "feign themselves just"); **`c20-v41-47` "feigning" at 7 prose sites on 4 lines** (ll. 96, 98, 106, 108) + the lemma ×2 (ll. 106, 300). Disclosed (426). All 119: "dissembling" 52, "feigning" only here. Sheet item 108 |
| Job 36:13 *provocant iram Dei* | Douay "prove the wrath of God" | 2 sites | **NEW finding N-2:** `c20-v19-26` ¶ 26 (l. 70) "prove", as its item (410) says; **`c20-v41-47` ¶ 56 (l. 108) "provoke"**, while that chunk's Notes list the verse under "Kept as the Douay". One verse, two renderings two chunks apart, nothing leaning, undisclosed. Sheet item 120 |
| *excidium* | — | 8 La | **D-4 confirmed, and the sites are 6 + 2, not 1 + 1:** "destruction" at `c19-v36-40` ¶ 62, `c19-v41-48` ¶¶ 63, 66, 70, `c21-v5-11` ¶ 14 and **`c21-v20-24` ¶ 31 itself**; "overthrow" only at `c21-v20-24` ¶¶ 28, 35. "Overthrow" is also the work's word for *subversio* / *eversio* (13 La sites, incl. `c19-v36-40` ¶ 62, `c19-v41-48` ¶ 67, `c21-v5-11` ¶¶ 15-16), which `c21-v20-24` alone renders "overturning" (¶ 29, p. 532 n. 7). Sheet item 107 |
| *cautela* | caution | 19 La (all 119) | **D-5 confirmed:** "caution" 18 / 19 from `c3-v1-9` on; "wariness" once, `c20-v19-26` ¶ 30 (l. 82). Sheet item 111 |
| Luke 16:8 *filii huius saeculi … filiis lucis* | — | 2 sites | **D-3 confirmed:** `c16-v1-8` ¶¶ 11-12 + p. 407 n. 5 "children" (the Douay; nothing there leans on *filius*); `c20-v27-40` ¶ 40 (l. 104) "sons" (¶ 40's chain *filii huius saeculi / filii ancillae / filii Dei / filii resurrectionis*). Work-wide the *filii X* phrases stand "sons of" 161 / "children of" 79, each following the Douay or the leaning. Sheet item 106 |
| *cultus* · *cultor* · *cultura* (r. 32 "worship") | — | 45 La (all 119) | worship of God: "worship" at every site; dress: "adornment" at `c2-v1-7` ¶ 11, `c7-v24-35` ¶ 49, `c12-v13-34` ¶ 39, `c16-v19-22` ¶ 38 and `c20-v41-47` ¶¶ 52-53; *cultor* "husbandman" (Luke 20:10, the Douay) / "worshipper" by sense; *cultura* "cultivation" / "worship" by sense. No site off its sense. Sheet item 112 |
| *arguere* (r. 32 "reprove") | reprove | 79 La (all 119) | "reprove" (or the Douay's verse word) at every moral site; the logical *argui potest* "argue" at three: `c7-v1-16` ¶ 13, `c12-v13-34` ¶ 36, `c20-v27-40` ¶ 42. Sheet item 113 |
| *denarius* | penny (the coin) / ten, tenth (the number) | 25 La (all 119) | coin: "penny" at every site (`c7-v36-50`, `c9-v10-17`, `c10-v25-37`, `c15-v8-10` ¶ 16, `c20-v19-26` ¶ 30 ×5). Sheet item 114 |
| *lumen* (rr. 27, 50, 78-80) | lumen | 10 / 16 "lumen" | 1 La site "light": `c20-v1-9` ¶ 2 Job 24:13 *rebelles lumini* (the Douay, nothing leans; disclosed (385)). Six `tr-lumen`, each at its chunk's first site. `c21-v25-27` ¶ 41 *illorum luminum* "those lumens" is the work's only prose plural (James 1:17 *Patre luminum* "Father of lights" ×2 is a verse). Sheet item 117 |
| *pietas / pius / pie* (rr. 12, 31, 86, 99) | piety / pious / piously | 24 / 31 | 0 short. Three `tr-pietas`, each at its chunk's first divine site (`c19-v1-10` ¶ 2, `c19-v29-35` divisio, `c19-v41-48` ¶ 63). The other *pietas* sites are human (`c20-v27-40` ¶¶ 35, 42; `c21-v1-4` ¶ 8; `c21-v12-19` ¶ 19 II Tim. 3:12 "piously", r. 51). Zero "godl-" |
| *vacare* (rr. 32, 68) | free for / free from / to be free | 3 / 3 | `c19-v36-40` ¶ 54 *non vacat a mysterio* "not free from mystery" (*vacare a*, the row; no note, as the row requires none); `tr-vacare` at `c20-v1-9` ¶ 12 and `c20-v27-40` ¶ 38 |
| *excessus* (rr. 67, 81) | transport / excess | 2 / 1 + 1 | `c21-v28-38` ¶ 55, both senses in one paragraph, with `tr-excessus` (the `c9-v28-31` shape) ✓ |
| *intelligentia* · *intellectus* (r. 32 / 97) | intelligence · understanding | 9 / 8 · 13 / 14 | 1 short: `c21-v12-19` ¶ 22 Job 32:8, the Douay's "understanding" (disclosed (453)). **Zero bare "intellect"** |
| *Praeceptor* (rr. 49, 69) | Master + `tr-praeceptor` | 1 | **D-2 confirmed; and NEW finding N-4:** `c21-v5-11` ¶ 12 (l. 80) Luke 21:7 "Master" with **no `tr-praeceptor`**, where all six earlier *Praeceptor* lemma sites carry the note, with or without *magister* beside them (`c5-v1-11`, `c8-v22-25`, `c8-v40-48`, `c9-v32-36`, `c9-v46-56`, `c17-v11-19`). The builder's reason ("no *magister* in ¶ 12, so ruling 69 owes no note") misreads ruling 69, which fixes one *sentence* of the note where *magister* stands; `c9-v32-36`'s and `c17-v11-19`'s notes each say in terms that no *magister* stands beside the word. Sheet item 110 |
| *infidelitas* · *incredulitas* (rr. 55, 71) | faithlessness · unbelief | — | "unbelief" 12, "faithlessness" 2 (`c19-v41-48` ¶ 69, `c20-v27-40` ¶ 34), each on its Latin. Zero "infidelity", zero "credulity" |
| *turba* | multitude; "crowd" on the Luke 19:3 lemma | 35 La | `c19-v1-10` ¶ 5 "crowd" ×12 (the Douay's word at Luke 19:3; disclosed (295)); "multitude(s)" elsewhere, the work's word (198 of 214 in all 119) |

**Mechanically, in the 18 chunks' rendered English:** zero "Holy Ghost" (r. 83) · zero "proclaim" (r. 30) · zero "credulity" (r. 55) · zero "infidelity" (r. 71) · zero "simulation" (r. 96) · zero "boy(s)" (r. 93) · zero "godl-" · zero bare "intellect" (r. 97) · "wicked one" once, II Thess. 2:8 (the Douay verse; r. 86 allows it) · "candle(s)" only for *candela* / *candelabrum* · "penalt-" 3 (one right, two N-1).

### 3c. `tr-` note inventory, pp. 472-540: 13 notes, every def anchored exactly once, every anchor defined, NO new id
- `c19-v1-10` pietas (¶ 2), lumen (¶ 11)
- `c19-v29-35` pietas (the divisio below ¶ 43), lumen (**inside p. 487 n. 13 En.**, Jerome's apparatus-only *lumen*)
- `c19-v41-48` pietas (¶ 63)
- `c20-v1-9` lumen (¶ 5, John 1:8), vacare (¶ 12)
- `c20-v19-26` lumen (¶ 30, with Ps. 4:7)
- `c20-v27-40` vacare (¶ 38)
- `c21-v25-27` lumen (¶ 41), corrigenda (¶ 41, Wis. 17:5)
- `c21-v28-38` lumen (¶ 51, Bernard), excessus (¶ 55)

That makes 3 `tr-pietas`, 6 `tr-lumen`, 2 `tr-vacare`, 1 `tr-corrigenda`, 1 `tr-excessus`. No `tr-` anchor in any Latin body. Twelve are anchored in an English body, one in an **En.** apparatus half. **New ids: none.** Vol VII total: 79 + 13 = **92** (tr-lumen 25 · tr-pietas 22 · tr-corrigenda 15 + tr-corrigenda-2 1 · tr-vacare 11 · tr-evangelizare 8 · tr-praeceptor 6 · tr-annuntiare 2 · tr-excessus 2). The interval has no `tr-praeceptor` (N-4), `tr-evangelizare` or `tr-annuntiare`.

### 3d. Frontmatter / manifest continuity, pp. 472-540: no gap, no overlap, no abutment
- **Every one of the 18 seams shares exactly its seam page:** pp. 472 (from `c18-v28-43`), 477, 480, 483, 487, 491, 495, 501, 504, 509, 512, 516, 520, 523, 527, 530, 533, 536. p. 540 is the interval's last page and is shared with the unbuilt Cap. XXII ¶ 1.
- **`division` / `section`:** `division` steps 19 → 20 → 21 once each; `section` runs XIX 1-7 · XX 1-5 · XXI 1-6.
- **`paragraphs` / `verses`:** restart at 1 at each capitulum, contiguous within it. **Last ¶ per capitulum: XIX 75 · XX 56 · XXI 60.** Each capitulum closes on Luke's last verse (48 · 47 · 38).
- **Every chunk's `verses`, `paragraphs`, first and last page equal its manifest row. `title_la` equals the manifest's cell in all 18** (final point dropped, the house form) and occurs verbatim in the chunk's Latin (heading or divisio sentence). No divergence of the `c16-v1-8` kind this interval.
- **`confidence`:** all 18 rows `high`. Nine were drawn `low` and promoted by their builders under ruling 39 (`c19-v29-35`, `c19-v36-40`, `c20-v1-9`, `c20-v10-18`, `c20-v27-40`, `c20-v41-47`, `c21-v1-4`, `c21-v5-11`, `c21-v12-19`): sheet item 109.

### 3e. Hand-offs at every shared page (file ownership derived from the defs)
| page | A nn. / B nn. | page | A nn. / B nn. |
|---|---|---|---|
| 472 | c18-v28-43 1-7 / c19-v1-10 8-12 | 512 | c20-v19-26 1-5 / c20-v27-40 6-15 |
| 477 | c19-v1-10 1-5 / c19-v11-14 6-13 | 516 | c20-v27-40 1-8 / c20-v41-47 9-12 |
| 480 | c19-v11-14 1-5 / c19-v15-19 6-13 | 520 | c20-v41-47 1-2 / c21-v1-4 3-11 |
| 483 | c19-v15-19 1-10 / c19-v20-28 11-15 | 523 | c21-v1-4 1-4 / c21-v5-11 5-12 |
| 487 | c19-v20-28 1-4 / c19-v29-35 5-13 | 527 | c21-v5-11 1 / c21-v12-19 2-12 |
| 491 | c19-v29-35 1-12 / c19-v36-40 13-15 | 530 | c21-v12-19 1-6 / c21-v20-24 7-12 |
| 495 | c19-v36-40 1-5 / c19-v41-48 6-12 | 533 | c21-v20-24 1-4 / c21-v25-27 5-12 |
| 501 | c19-v41-48 none / c20-v1-9 1-11 | 536 | c21-v25-27 1-4 / c21-v28-38 5-15 |
| 504 | c20-v1-9 1-9 / c20-v10-18 10-14 | 540 | c21-v28-38 1 / next interval 2-10 PENDING |
| 509 | c20-v10-18 1-4 / c20-v19-26 5-12 | | |

On every page the two halves make one contiguous 1..N register, and the apparatus checker confirms N against `KNOWN_TOTALS_VOL7`. p. 501 is the interval's one leaf where the outgoing chunk holds no note (Cap. XIX ¶ 75's tail in the top band carries no anchor).

### Records slip (no text effect)
- **R-1. The 518L t4's position.** `c20-v27-40`'s item (414) says the heading was "read at ~0.36 as stage 6 measured"; `c20-v41-47`'s item (424) says ~0.53. The overview crop of p. 518 puts *Informatio discipulorum ad prudentiam, de qua tria.* at **~0.53** of the leaf (¶ 51 closes on *« … consummatio autem sermonum ipse est ».* just above it; ¶ 52 *Audiente autem omni populo* just below). `c20-v41-47` is right; the stage-6 notes' `518L 518.36` (l. 980) and `c20-v27-40`'s (414) are wrong, in the position figure only. The joint, the rows and the built chunks are unaffected. Sheet item 122.

## PASS 4: plate cleanup. REPORTED, NOTHING DELETED

`raw/vision/vol7/` (gitignored) holds **462 PNG plates, 1,807 MB**, all 300 dpi (2476 × 3921), named by printed page:

| range | files | size | status |
|---|---|---|---|
| pp. 88-471 | 384 | 1,517 MB | intervals closed at the p. 188 / 288 / 381 / 472 gates; each of those gates left the deletion to Wilson and none was made |
| **pp. 472-539** | 68 | ~269 MB | **this interval's**; deletable once the gate closes (every one regenerable with `tools/extract-pages.py --volume vol7 --dpi 300`) |
| pp. 540-541 | 2 | ~8 MB | **keep:** p. 540 is shared with Cap. XXII ¶ 1 and both serve manifest stage 7, the next job |
| pp. 604-607, 652, 655, 657, 858 | 8 | 13 MB | pilot / Corrigenda leaves (p. 858 is the Corrigenda leaf the `tr-corrigenda` notes cite); keep |

No `/tmp/colcrop` directory exists (0 files). The agent's own scratch (`g540/`: scripts, two ledger copies, one 825 × 522 crop of p. 518) is in the session scratchpad and is not the repo's. **Deletable on Wilson's word: 68 files / ~269 MB for this interval, or 452 files / ~1,786 MB if the four earlier intervals' plates go with them.** Deleting files is a hard stop; nothing was deleted.

## Summary
- **Pass 1:** as expected. One live `[?]`, `c5-v12-16` p. 122 n. 11, La + En. Three `[so printed]`, all English-side, none in the Corrigenda.
- **Pass 2:** clean. Every resume figure reproduced: 119 / 6,522; census 119/119, 285 runovers (247 / 38), 112 / 7; style CLEAN (119); validate OK × 18; citations 48,221, QA 213, both byte-identical to the tracked files; anaphora unresolved 442; crossref 1,917 / 11,533; build 2,436 / 2,436. No tracked file changed.
- **Pass 3:** anchors, page markers, ¶ numbers, `####`, guillemets and verse tags agree La/En in all 18; no untranslated Latin; `title_la` = manifest in all 18; 18 shared seams, hand-offs contiguous; 13 `tr-` notes paired, no new id; old ground byte-unchanged since `3114828`.
  - **Recorded defects D-1..D-6: all confirmed in place, none touched.** D-1 (*virtus*), D-4 (*excidium*) and the page-crossing count are wider than the resume records.
  - **NEW, not recorded by any builder:** **N-1** *poena* "penalty" ×2 in `c20-v27-40` (ll. 94, 196) · **N-2** Job 36:13 "provoke" at `c20-v41-47` l. 108 against "prove" at `c20-v19-26` · **N-3** paragraph shape: `c20-v10-18` Latin ¶ 16 run on to ¶ 15 (no blank line, l. 36), and four stray English line breaks (`c19-v1-10` ×3, `c21-v12-19` ×1) · **N-4** `c21-v5-11` ¶ 12 *Praeceptor* without the work's `tr-praeceptor`, on a misreading of ruling 69.
  - **R-1:** the 518L t4 stands at ~0.53 (plate), so `c20-v41-47` is right and the stage-6 notes / `c20-v27-40` (414) are wrong.
- **Pass 4:** 462 plates / 1.8 GB on disk; 68 (pp. 472-539, ~269 MB) are this interval's and deletable after the close; nothing deleted.
