# Vol VI *Ioannem* shakedown gate (p. 268): passes 1–3 DRAFT (read-only agent, 2026-10-20)

This draft is uncommitted. No file under `vol*/` was edited, nothing was committed, pushed or stashed, and no plates were deleted. The register questions are covered by the separate evidence sheet and are not repeated here.

**Scope:** 13 chunks, pp. 239–269, **331 numbered apparatus entries** plus **12** `tr-` notes (corrected at the gate close from "11"; verified by `cat vol6/bon-ioan-*.md | grep -cE '^\[\^tr-[^]]*\]:'`). The per-chunk counts are prooem 52 · prol 9 · c1-v1-2 22 · v3-5 22 · v6-8 18 · v9-14 29 · v15-18 25 · v19-23 23 · v24-28 23 · v29-30 7 · v31-34 17 · v35-42 38 · v43-51 46. The scope total equals the sum of `KNOWN_TOTALS_VOL6` for pp. 239–268 plus p. 269 n. 1.

---

## PASS 1: live flags. **CLEAN**

`python3.11 tools/check-live-flags.py vol6` → **scanned 81 chunks in vol6; LIVE [?] FLAGS: none.** The denominator is 81, which is all of vol6 and includes the 13 in scope.

## PASS 2: mechanical suite. **CLEAN on every baseline; one documentation DEFECT**

| tool | denominator / result | baseline | verdict |
|---|---|---|---|
| `check-vol5-apparatus.py --volume=vol6` | header `volume: vol6 (81 chunks, 256 known page totals)`; it scans vol6 and not vol5, and p. 239–269 rows are printed. **81 chunks, 2,539 entries, all passed**; p. 269 `PENDING n.2–13` | same | CLEAN |
| `check-vol5-census.py` | **vol6 81/81, 124 runovers (120 gutter / 4 page)**; rosters agree | same | CLEAN |
| `polish-style-scan.py` | **11 issues / 6 chunks / 2,200 scanned**: `bon-hex-c23` plus five Vol III–IV PAIR chunks, none of them ours | same | CLEAN |
| `build-citations.py` (`--out`/`--qa` into the scratchpad) | **29,110 records, QA 209**; the ledger is **byte-identical** to `index/citations.tsv` and the QA report matches the tracked one | same | CLEAN |
| ↳ in scope | 374 records from the 13 chunks. **1 QA flag**: `c1-v15-18` p. 256 n. 3 `III. d. 14. a. 1. q. 3.`, the already-docketed resolver mis-read. Five unresolved-anaphora lines (`ibid.` in p246-5, p248-8, p250-10, p255-6, p256-5) are outside the 209 count | | NOTE (already docketed) |
| `build-index-json.py` | 1,739 cited / 10,643 backlinks | same | CLEAN |
| `build-content.mjs` | **2,199/2,199 translated**; `git status` clean afterwards | same | CLEAN |

**Page markers:** in all 13 chunks the `<!-- page N -->` lists are identical in Latin and English. **Anchor sequences** are also identical in both languages for all 13 (counts 52/9/22/22/18/29/25/23/23/7/17/38/46).

**La/En digit multiset per entry:** four mismatches out of 331, all false positives.
- p. 246 n. 1 and p. 250 n. 3: `83 Qq.` → "*Eighty-three Questions*" (a spelled-out number, a known false positive).
- p. 261 n. 10: the English repeats the quoted Latin `[n. 60, 65 and 67]` and then glosses it, so the digits are doubled. Checked on the plate: it prints `[n. 60. 65.` / `et 67.]`.
- p. 259 n. 15: the Latin prints **`d. XXV.`** (confirmed on the plate) and the English gives `d. 25`. → **NOTE:** the corpus is mixed here. About 86 Vol V–VI English halves keep the roman numerals, against about 114 Latin roman sites, so this is a house-style inconsistency and not a defect.

### DEFECT 1 (documentation only, no text change): `bon-ioan-c1-v43-51` says "forty-five entries" when it has 46
- **File / location:** `vol6/bon-ioan-c1-v43-51.md`, in the frontmatter `transcription_status` ("Forty-five entries + tr-studium (p. 265 nn. 3-8, p. 266 nn. 1-12, p. 267 nn. 1-12, p. 268 nn. 1-15, p. 269 n. 1…") and in the `## Notes` heading (line ~390, "**⭐ APPARATUS: FORTY-FIVE ENTRIES + `tr-studium`.**"). The same figure is carried into the START HERE block of `next-session-resume.md` ("45 entries + `tr-studium`") and probably into the commit message of `581b626`.
- **Evidence:** the chunk's own page-split map gives 6 + 12 + 12 + 15 + 1 = **46**. The file has 46 numbered defs (`p265` ×6, `p266` ×12, `p267` ×12, `p268` ×15, `p269` ×1) plus `tr-studium`, and `check-vol5-apparatus.py` reports 46 La / 46 En. The plate agrees: the KNOWN_TOTALS give p. 265 nn. 3–8 and pp. 266–268 at 12/12/15, and the footer heads read numbered.
- **Proposed fix:** "Forty-five" → "Forty-six" in `transcription_status` and in the Notes heading. Correct the START HERE line in the resume at the gate close. Do not amend the commit. This is the CLAUDE.md "summary vs per-note data" rule: the per-note data wins.

## PASS 3: boundary sweep. **CLEAN**

Every page from 239 to 269 is owned exactly once with a contiguous 1..N register (checker), and `KNOWN_TOTALS_VOL6` matches the plate count on each leaf whose register head and foot were read. The seams were read on the 450 dpi plates (2067×2985 px, pHYs 450) as region crops of 0.5–1.0×. No full page was read at 450 dpi.

| seam | receiving opening, read on the plate | footer split | verdict |
|---|---|---|---|
| **244** prooem / prol | R col: `…peditare debent cum agnis.` → `PROLOGUS S. HIERONYMI IN EVANGELIUM SECUNDUM IOANNEM⁹.` → *Hic est Ioannes evangelista* | 8 / 1; n. 9 = `In ed deest Prologus, non ipsius expositio.` anchored on the heading | CLEAN |
| **245/246** leaf edge | p. 245 R: `…ut aliis fructum laboris relinquat⁸.`, rest blank; p. 246 opens on the COMMENTARIUS display stack | 8 / 0; p. 246 L block opens with a numbered `¹ Cap. 1, 6.` | CLEAN |
| **248** v1-2 / v3-5 | L foot: `…talibus argumentis est consequens⁵.`; R head: *Secundo, de Verbo in comparatione ad ea quae per ipsum dicuntur.* / `9. (Vers. 3.)` | 5 / 4; R block opens with a numbered `⁴ Ed. addit` (n. 4 prints R, anchor L, as recorded) | CLEAN |
| **250** v3-5 / v6-8 | R head: `…nec fide nec amore adhaeserunt.` → `PARS. II. DE VERBO, QUATENUS EST CARNI UNITUM, PONUNTUR TRIA.` (point after *Pars* as printed) → 17. | 7 / 6; the R block opens with n. 7's tail (ledgered gutter) | CLEAN |
| **251** v6-8 / v9-14 | R: `…verbo et exemplo¹².` → `De adventu Christi.` → 24.; forwards in the body only | 12 / 0 | CLEAN |
| **254** v9-14 / v15-18 | L: `…sibilem: ideo³ etc.` → *Secundo, de ipsa incarnatione quoad eius manifestationem dupliciter.* (italic, as built) → 35. | 3 / 7; R block opens with a numbered `⁶` | CLEAN |
| **256** v15-18 / v19-23 | L: `…statim amittebat.` → `Secundo, de manifestatione Verbi incarnati in speciali dupliciter.` (roman, as built) → 44.; the plate confirms `sen-|tinnt` as printed | 3 / 8; R block opens with a numbered `⁴ Vers. 43.` | CLEAN |
| **258** v19-23 / v24-28 | L: `…cum ad praeceptum vita praeparatur ».` → `53. Et qui missi fuerant.` (no heading) | 3 / 8; the R block opens with n. 5's tail (ledgered by v24-28) | CLEAN |
| **259** v24-28 / v29-30 | R: `…qui in eum non credebant¹⁵.` → `61. Altera die vidit Ioannes` | 15 / 2; R block opens with a numbered `⁹` | CLEAN |
| **260** v29-30 / v31-34 | R: `…tangitur in littera⁵.` → `65. Et ego nesciebam.` | 5 / 5; R block opens with a numbered `⁷` | CLEAN |
| **261** v31-34 / v35-42 | R: `…potuit dubitare.` → `72. Altera die iterum stabat` …`conversio;` (no anchor on p. 261), → p. 262 `tertio` | 12 / 0; the R block opens with n. 7's tail (ledgered) | CLEAN |
| **265** v35-42 / v43-51 | L: `…Romana Ecclesia in summo Pontifice.` → `De manifestatione Verbi per se ipsum.` → 89. | 2 / 6; the L block opens with p. 264 n. 12's tail (ledgered `page`), and the R block with n. 2's tail (ledgered) | CLEAN |
| **269** v43-51 / Cap. II | four run-on lines `culi, vel alicuius famosi consanguinei … filium hominis se appellat¹.` → `CAPITULUM II.`; n. 1 = `Cfr. Breviloq. p. IV. c. 3.` = def | 1 / 12 pending; n. 2 `Vulgata Et die tertia. — De 1. membro vide superius n. 89. seqq.` | CLEAN (hand-off as recorded) |

No seam shows a cascade-merge splice. Every outgoing tail is a complete sentence and every incoming text opens on its printed paragraph number or heading.

**Register heads and ledger negatives, re-derived:** the LEFT and RIGHT register heads were read on every leaf from 239 to 269 (with p. 245 taken from the structural view). **The only unnumbered LEFT-block head is p. 265**, which is p. 264 n. 12, ledgered as `page`. So there is no unledgered page-crossing runover anywhere in scope. Every unnumbered RIGHT-block head corresponds to a ledgered gutter runover (pp. 239, 240, 241, 243, 245, 246, 249, 250, 251, 253, 258, 261, 263, 264, 265, 266). The three `-` lines are **CONFIRMED**:
- `c1-v15-18`: heads of 255, 256 and 257 are numbered, and its RIGHT heads on pp. 254–256 are numbered.
- `c1-v19-23`: heads of 257, 258 and 259 are numbered; its RIGHT heads on 256 and 257 are numbered, and 258's unnumbered R head is v24-28's n. 5.
- `c1-v29-30`: heads of 260 and 261 are numbered; the RIGHT heads on 259 and 260 are numbered.

## Summary for the gate log
- Pass 1 CLEAN · Pass 2 CLEAN (the suite matches the baselines exactly) · Pass 3 CLEAN.
- **One documentation DEFECT** (c1-v43-51 "45 entries" → 46), no text defect.
- NOTEs: the `d. XXV.` roman→arabic house-style inconsistency (corpus-mixed), and one in-scope dangling QA line already on the resolver docket.
