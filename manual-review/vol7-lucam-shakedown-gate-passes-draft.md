# Vol VII *Lucam* shakedown gate (p. 27): passes 1-3 DRAFT (read-only agent, 2026-11-14)

Uncommitted. No chunk, tool or plate was edited, committed or deleted. Register questions are on the separate evidence sheet.

**Scope:** 6 chunks, pp. 3-27, **220 numbered apparatus entries** + **7** `tr-` notes. Per chunk: prooem 35 (+1 tr) · prol 34 (+1) · c1-v1-4 11 (+0) · c1-v5-17 50 (+2) · c1-v18-25 21 (+1) · c1-v26-38 69 (+2). p. 27 nn. 7-11 belong to the next, unbuilt chunk.

## PASS 1: live flags. CLEAN
`check-live-flags.py vol7` -> scanned 6 chunks in vol7; LIVE [?] FLAGS: none. Corpus baseline (per volume, scanned chunks): vol1 150 (421) · vol2 9 (468) · vol3 2 (415) · vol4 66 (649) · vol5 12 (167) · vol6 none (199) · vol7 none (6). None in vol7.

## PASS 2: mechanical suite. CLEAN
| tool | result |
|---|---|
| `check-vol5-apparatus.py --volume=vol7` | 6 chunks, 25 known page totals (pp. 3-27); 220 entries, La = En in every chunk; p. 27 `PENDING n.7-11`; All checks passed |
| `check-vol5-census.py` | vol7 6/6 chunks, 18 runovers (15 gutter / 3 page: p. 9 n. 7, p. 13 n. 10, p. 21 n. 10); rosters agree |
| `polish-style-scan.py` | 11 issues / 6 chunks / 2,324 scanned, all in Vol III-V (`bon-hex-c23`, five PAIR chunks); none ours; scope covers vol1-7 |
| `build-citations.py` | 36,077 records, **QA 211** (209 at the Vol VI gate; +2 not in vol7). `git status` / `git diff --stat` empty afterwards: `index/citations.tsv` and the QA report are byte-identical to HEAD, no restore needed |
| in scope | 474 ledger records from the 6 vol7 chunks (prooem 63, prol 32, v1-4 21, v5-17 123, v18-25 64, v26-38 171); **0 QA flags** attributable to vol7 (no `bon-luc` in the QA report) |

**Page markers:** identical La/En in all 6 chunks (3-7; 7-11; 11-12; 12-17; 17-20; 20-27). **Anchors:** numeric anchor sequences identical La/En in all 6, unique and ascending (35/34/11/50/21/69); the `tr-` anchors exist only in English (as designed).

**`tr-` notes (7):** prooem `tr-annuntiare`; prol `tr-corrigenda`; v5-17 `tr-annuntiare`, `tr-corrigenda`; v18-25 `tr-evangelizare`; v26-38 `tr-corrigenda`, `tr-corrigenda-2`.

**`[so printed]` marks in the rendered text:** p. 5 n. 4 (`I John 1:1 and Isa. 52:1 [so printed; the verse is Isa. 52:7]`); p. 5 n. 6 (`V. 37 [so printed; the verse is John 20:31]`); p. 7 n. 3 (`corsummationem [so printed: for consummationem]`). Others (v18-25 `impotestas`, v26-38 `exluditur`) occur only in `## Notes`/body discussion as recorded.

**La/En digit multiset per entry:** 2 mismatches of 220, both false positives.
- prooem p. 5 n. 4: En adds the editorial gloss `[... the verse is Isa. 52:7]` (extra digit 7).
- prooem p. 5 n. 6: En adds `[... John 20:31]` (extra digits 2,0,3,1). Both glosses sit inside `[so printed; ...]` brackets; the print reads `Isai. 52, 1` and `Vers. 37` (plate p. 5 notes are the Latin side; the Latin digits match the file).

## PASS 3: boundary sweep. CLEAN
Every page 3-27 owned exactly once with a contiguous 1..N register (checker, plus an independent per-page min/max/count over the `[^pN-n]` defs); `KNOWN_TOTALS_VOL7` matches the plate on every leaf read (p. 7 = 10, p. 11 = 7, p. 12 = 9, p. 17 = 9, p. 20 = 10, p. 27 = 11, counted on the plate). Plates: 300 dpi (2476x3921, pHYs 300), read as native or 1.7x footer bands; whole-page views (0.35-0.5x) were used for structure only.

| seam | plate | split | verdict |
|---|---|---|---|
| **7** prooem / prol | L top: `...Ezechielis primo^1: Facies aquilae desuper. ...totius Libri generalis intelligentia.` (prooem, n. 1 only) then in-column `PROLOGUS SANCTI HIERONYMI^2` heading, Prologus text, `Expositio huius Prologi` ¶ 1 to `Cui ideo post baptismum etc.` (prol) | 1 / 9 (nn. 2-10; n. 2 on the heading) | CLEAN |
| **11** prol / v1-4 | prol ends `...potest exponi.` above the COMMENTARIUS / IN EVANGELIUM S. LUCAE / Capitulum I display; v1-4 opens `Prologus Evangelistae.` ¶ 1 | 3 / 4 (n. 4 anchored `Hieronymi^4`, below the stack) | CLEAN |
| **12** v1-4 / v5-17 | v1-4 ends `...ab Evangelista.`; v5-17 opens `Divisio generalis^8`, ¶ 7 `...habet qua-` / p. 13 `tuor` (hyphen join across the page, as printed; markers match La/En) | 7 / 2 (n. 8 two paragraphs, n. 9); n. 8 full text read on the plate band | CLEAN |
| **17** v5-17 / v18-25 | v5-17 ends `...viam parat »?`; v18-25 opens heading `Tertio describitur promissionis confirmatio quadrupliciter.` ¶ 29, ends p. 17 `...quidam signa quae-` | 7 / 2 (nn. 8-9) | CLEAN |
| **20** v18-25 / v26-38 | v18-25 ends `...matrem filiorum laetantem ».`; v26-38 opens heading `Tria dicuntur etiam de conceptu Salvatoris.` ¶ 40 | 6 / 4 (nn. 7-10); n. 9 runs over the gutter (`Isai.` / `66, 22.`), carried whole | CLEAN |
| **27** v26-38 / next | v26-38 ends `...misericordiam consequamur in auxilio opportuno^6 ».` (¶ 70 complete); next chunk opens `Secundo, de gratiarum actione pro utraque conceptione.` ¶ 71 | 6 / 5 pending (nn. 7-11 anchored below, ¶ 71-72); all 11 notes read | CLEAN (hand-off as recorded) |

No seam shows a splice, drop or duplication. Every outgoing tail is a complete sentence (or the printed hyphen at p. 12/13, p. 17/18). Every note is assigned by anchor. Marginalia are trimmed from the body and transcribed in `## Notes` per the chunk convention.

**Full-page apparatus spot-checks against 1.7x footer bands** (digits, loci, sigla): prooem p. 4 (all 12); prol p. 7 (nn. 2-4, 6-10) and p. 8 (nn. 6-9 tails); v1-4 p. 11 (nn. 1-7); v5-17 p. 12 (nn. 8-9) and p. 14 (nn. 1-3, rest by file); v18-25 p. 17 (nn. 8-9) and p. 18 (nn. 2-5); v26-38 p. 20 (all 10), p. 23 (nn. 1-5), p. 27 (nn. 1-6). **No difference found** from the file in any digit, locus or siglum.

## Summary
Pass 1 CLEAN · Pass 2 CLEAN (2 digit-multiset false positives) · Pass 3 CLEAN. No defects. Note for the register sheet only: p. 5 n. 6 En renders the print `Vers. 37.` as `V. 37`, consistent with the volume's apparatus house form (`V. N`) used throughout vol7 En; Vol VI's ruling 4/73/97 concerned body print addresses.
