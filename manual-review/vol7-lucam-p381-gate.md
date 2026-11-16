# Vol VII — *Commentarius in Evangelium S. Lucae*, p. 381 GATE (printed pp. 288–381; Cap. XI v. 14 – Cap. XIV complete; the *pietas* review) — CLOSED

**STATUS: CLOSED 2026-11-16.** Docket ruled by Wilson in one sitting ("Approve all", 2026-11-16: every ⭐ recommendation of the evidence sheet — D-1, D-3, D-4, D-7 applied; D-2 no edit; D-5 kept as built with the adjective clause written into ruling 32's *excessus* row; D-6 as tool item J-12; the "Found by the sheet" fixes F1–F7 and F13, **the five pre-interval lines included**; the records F8–F12; the *pietas* review closed; all batches ratified) → Vol VII rulings 77–92 in `manual-review/vol7-pilot-setup.md` § *LUCAM* p. 381 GATE. **42 English lines changed: 37 in 13 interval chunks + 5 in 4 pre-interval chunks (three of the 42 are new `tr-lumen` definitions, one is a `title_en`), plus Notes records in 19 chunks; no line in any `## Latin` body or `**La.**` half changed; no manifest cell changed.** Ruling 32's *excessus* row gains one clause (the adjective); the setup table's Cap. XIV cell is corrected 68 → 69. No CLAUDE.md change. J-12 joins ruling 76's tool job, which stays queued. The live `[?]` (p. 122 n. 11) stays open. **No push, no deploy.**

Ruling 14 placed this gate at p. 381 (close of c. 14; the *pietas* review). This close makes no recommendation about the deploy.

**Procedure (the p. 288 gate's):** a read-only agent compiled the evidence sheet, `manual-review/vol7-lucam-p381-gate-evidence-sheet.md` (censuses over the rendered region of all 82 chunks, the decisive sentence, alternatives with costs, a ⭐ per item, and thirteen "found by the sheet" items F1–F13); a second read-only agent ran Passes 1–3 into `manual-review/vol7-lucam-p381-gate-passes-draft.md` (both committed at `0165212`); manifest stage 5 (`21637e0`, Cap. XV–XVIII, 19 rows) was drawn alongside. Both documents are kept as the evidence record and are summarised here, not repeated. Wilson ruled in one sitting; the edits, the re-run and Pass 4 then closed the gate.

**Scope: the 19 chunks of pp. 288–381** (`bon-luc-c11-v14-26` → `bon-luc-c14-v25-35`; XI 4 · XII 5 · XIII 5 · XIV 5), **1,229 numbered apparatus entries, 13 `tr-` notes** before the close; censuses over all 82 *Lucam* chunks (pp. 3–381, 4,429 entries, 62 `tr-` notes), and over Vols V–VI where a corpus precedent decided (Ps. 4:7, *excessivus*, Titus 2:12). **p. 381 nn. 12–13 belong to the next interval** (`bon-luc-c15-v1-7`, unbuilt; checker `PENDING n.12,13`).

---

## PASS 1 — live flags: **AS EXPECTED**

`check-live-flags.py vol7` → 82 chunks, **2 occurrences = one flag, La + En: `bon-luc-c5-v12-16` p. 122 n. 11** (*A C G E [?]*). Same after the edits. Stays open (ruling 90). Exit 0. Zero `[?]` in the 19 interval chunks.

## PASS 2 — mechanical suite: **CLEAN** (figures below, § CLOSE)

## PASS 3 — read-through / consistency: **NO NEW DEFECT beyond the sheet's; D-1..D-7 CONFIRMED**

La/En parity in every ¶ of all 82 chunks (anchors 4,429 = 4,429; page markers; ¶ numbers; `####`; guillemets ¶ by ¶; verse tags); 13 interval `tr-` notes all paired; no page gap or overlap pp. 288–381 (18 shared pages, one abutment at 361 / 362); hand-offs agree on all 18 shared pages and on p. 381's PENDING. No false Notes self-claim in the interval. The passes draft's four new findings are the sheet's: **N-1 = F3, N-2 = F4, N-3 = F5, N-4 = F10**, all applied or ruled. Its observations: O-4 = F6 (applied), O-5 = item 15 (ratified); **O-1, O-2, O-3 were not on the docket and are not ruled** (below, ruling 91). Records point: the setup table's Cap. XIV cell still read 68 → corrected (ruling 89).

## PASS 4 — plate cleanup: **NOTHING TO DELETE**

This close read no plate and made no crop. The `raw/vision/vol7/` plates are left as they are; p. 381 serves the next interval's first chunk. Whether to delete the pp. 288–380 plates now that their interval is closed is Wilson's call; not done here.

---

## THE DOCKET — RULED 2026-11-16, "Approve all"

| # | item(s) | ruling | lines applied | recorded |
|---|---|---|---|---|
| D-1 | `c13-v1-9` ¶ 6 "credulity" | → "belief" (ruling 55); Notes amended, struck wording kept | 1 | 77 |
| D-4 | `c11-v14-26` ¶ 36 "candle" | → "lamp" (forward reference follows its lemma) | 1 | 77 |
| D-2 + F8 | `c12-v49-59` ¶ 84 Ps. 4:7 "light" | **No edit**: exempt under the corpus test | 0 + Notes | 78 |
| D-3 + F9 | *lumen* in Fathers' notes | Applied at p. 316 n. 2 and p. 373 n. 12, + `tr-lumen` each; p. 339 n. 5 exempt | 4 | 79 |
| F4 (= N-2) | `c12-v1-7` prose *lumen* "light" | Applied, lemma Luke 12:3 included, + `tr-lumen` | 3 | 80 |
| D-5 + F10 (= N-4) | *excessivus* (4 sites) | Kept as built; adjective clause into ruling 32's *excessus* row | 0 + Notes | 81 |
| D-7 + F2 | *eruditio* "teaching"; *erudire* "teach / instruct" | "erudition"; "school" (ruling 32's row), incl. `title_en` and 2 pre-interval | 1 + 5 + 2 | 82 |
| F1 | "Holy Ghost" | "Holy Spirit" (ruling 17), 12 interval + 2 pre-interval lines | 12 + 2 | 83 |
| F3 (= N-1), F5 (= N-3), F6, F7 | *benignitas*; *redarguere*; Prov. 23:21; *mirabilis* | "kindness"; "convicts"; "club together"; "marvellous" | 3 + 2 + 1 + 1 | 84 |
| F13 | *accidia* "sloth" / "accidie" | "acedia" work-wide, incl. 1 pre-interval | 3 + 1 | 85 |
| 11 | **the *pietas* review** | **The rule HOLDS for cc. 15–16**; `tr-pietas` names Cap. XV ¶ 1's divisio; Titus 2:12 split recorded | 0 | 86 |
| 10 + F12(b)(c) | *anima* "soul"; the other splits | Ratified; Luke 14:26 cross-chunk split recorded | 0 + Notes | 87 |
| 12–18 | *lumen* rest, *lucerna*, *excessus* rest, *intellectus…*, *vacare / quies*, house words, new words | Ratified; `c13-v22-30` ¶ 58 and [121] recorded | 0 + Notes | 88 |
| A, B, C + F12(a) | boundaries, Corrigenda, ruling-20 batch | Ratified; setup table XIV 68 → 69 | 0 | 89 |
| E, F, G, H | slips; `[so printed]` / *quinque ova* / the live `[?]`; readings; collection change | Ratified; no mark at *quinque ova*; `[?]` stays open; H banked | 0 | 90 |
| F8–F12; passes O-1..O-3 | records; observations not on the docket | Recorded; **O-1..O-3 not ruled, carried open** | 0 | 91 |
| T + D-6 + F11 | T-a..T-g; p. 295 n. 15 | Folded into ruling 76's job; **J-12 added**; QUEUED, NOT RUN | 0 text | 92 |

### Lines changed (git diff)

| file | English / En. lines | Notes lines | Latin / La. lines |
|---|---|---|---|
| `vol7/bon-luc-c12-v8-12.md` | 9 (F1: ¶ 12, ¶ 15, ¶ 16 ×2 lines, ¶ 20 ×2 lines, p. 315 n. 12 **En.** — 11 occurrences on 7 lines; D-3: p. 316 n. 2 **En.** "the lumen"; + the new `tr-lumen`) | headline amended in place ("Holy Ghost" ×2); register line amended, struck wording kept; 1 gate paragraph | **0** |
| `vol7/bon-luc-c14-v12-15.md` | 4 (D-7 ¶ 26 "spiritual erudition"; F2 ¶ 26, ¶ 27 "the exhortation schooling"; F6 ¶ 28 "that club together") | register line + item (156) amended, struck wording kept; 1 gate paragraph | **0** |
| `vol7/bon-luc-c14-v25-35.md` | 4 (F2 `title_en`, `####`, ¶ 51 ×3 in one line; F3 ¶ 52 "kindness") | Title and Register lines amended, struck wording kept; 1 gate paragraph | **0** |
| `vol7/bon-luc-c12-v1-7.md` | 3 (F4 ¶ 2 "lumen"; ¶ 6 lemma + gloss "lumen" in one line; + the new `tr-lumen`) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c14-v16-24.md` | 3 (D-3 p. 373 n. 12 **En.** "no lumen of wit"; F3 ¶ 37 "kindness"; + the new `tr-lumen`) | 1 gate paragraph (item (168) answered) | **0** |
| `vol7/bon-luc-c13-v1-9.md` | 2 (D-1 ¶ 6 "belief"; F3 ¶ 12 Rom. 2:4 "kindness") | register line amended, struck wording kept; 1 gate paragraph (items (85), (87); O-1, O-2 recorded) | **0** |
| `vol7/bon-luc-c11-v14-26.md` | 2 (D-4 ¶ 36 "lamp"; F13 ¶ 56 "acedia") | "Kept on the Douay" line amended, struck wording kept; 1 gate paragraph | **0** |
| `vol7/bon-luc-c11-v42-54.md` | 2 (F5 ¶ 87; p. 305 n. 6 **En.** "He convicts arrogance") | 1 gate paragraph | **0** |
| `vol7/bon-luc-c12-v13-34.md` | 3 (F1 ¶ 28, ¶ 43; F13 p. 318 n. 4 **En.** "acedia") | register line amended, struck wording kept; 1 gate paragraph (F12(a)(c)) | **0** |
| `vol7/bon-luc-c13-v18-21.md` | 2 (F1 ¶ 42, ¶ 45) | 1 gate paragraph (D-5) | **0** |
| `vol7/bon-luc-c13-v31-35.md` | 1 (F1 ¶ 73, Acts 7:51) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c14-v7-11.md` | 1 (F7 p. 365 n. 15 **En.** "marvellous") | 1 gate paragraph | **0** |
| `vol7/bon-luc-c14-v1-6.md` | 1 (F13 ¶ 11 "acedia") | register line amended, struck wording kept; 1 gate paragraph (item (140)) | **0** |
| `vol7/bon-luc-c10-v17-24.md` (pre-interval) | 2 (F1 ¶ 36 ×3, ¶ 39 ×1) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c9-v10-17.md` (pre-interval) | 1 (F2 ¶ 16 "school the Lord") | 1 gate paragraph | **0** |
| `vol7/bon-luc-c9-v32-36.md` (pre-interval) | 1 (F2 ¶ 64 "are schooled") | 1 gate paragraph (D-5 record) | **0** |
| `vol7/bon-luc-c6-v1-11.md` (pre-interval) | 1 (F13 ¶ 21 "of acedia") | 1 gate paragraph | **0** |
| `vol7/bon-luc-c12-v49-59.md` | 0 | 1 gate paragraph (D-2, D-5 (b), F12(b)) | **0** |
| `vol7/bon-luc-c13-v22-30.md` | 0 | 1 gate paragraph (item 15 ¶ 58; [121]) | **0** |

**42 English lines: 37 in 13 interval chunks + 5 in 4 pre-interval chunks — exactly the sheet's figure** (D-1 1, D-3 4, D-4 1, D-7 1, F1 12, F2 5, F3 3, F4 3, F5 2, F6 1, F7 1, F13 3; pre-interval F1 2, F2 2, F13 1). Of the 42, 39 are modified lines (in `git diff --stat` each counts once as `-` and once as `+`) and 3 are inserted `[^tr-lumen]` definitions; each insertion also brings one blank separator line (3 blank lines), and each of the 19 appended gate paragraphs one blank line before it. Classified from `git diff -U0`: every `+` line stands in `## English`, an apparatus **En.** half, a `[^tr-lumen]` definition, the one `title_en`, or `## Notes`; **0 lines carry `**La.**`; no line in a `## Latin` body changed.** No unlisted line was added. Each site was read with its Latin before the edit; the edits were exact-match replacements, each asserted unique on its line (F1's "Holy Ghost" replaced file-wide only in files whose every occurrence was a listed rendered line, and in `c12-v8-12` together with the two headline occurrences the sheet named for in-place amendment). After the edit `grep 'Holy Ghost'` finds the phrase only in `## Notes` (five older chunks, and `c12-v8-12`'s gate paragraph quoting the old wording).

**Also changed (doc):** `manual-review/vol7-pilot-setup.md` (ruling 32's *excessus* row: the adjective clause; the setup table's Cap. XIV cell 68 → 69; rulings 77–92). No CLAUDE.md line touched.

### Records the sheet found (no text effect)

- **F8:** the docket's Ps. 4:7 "defect" is not one under the test; the CLAUDE.md line is the test applied to the two Vol V attestations (ruling 78).
- **F9:** D-3 is two defects, not three; p. 339 n. 5 (Isa. 9:2 inside the Gloss) is exempt (ruling 79).
- **F10:** *excessivus* stands at four Lucam sites, not one (ruling 81).
- **F11:** D-6's cause is `scan_page()` in `tools/build-citations.py` (the `supra|infra … pag. N, nota M` pattern never compares direction with the citing page); a direction screen over the whole ledger finds 4 such records (ruling 92).
- **F12:** (a) Luke 12:20 "soul" is the Douay's own; (b) Luke 14:26 "life" / "soul" is a cross-chunk ruling-28 split; (c) John 12:25 "soul" at all three Lucam sites, each leaning; (d) T-e's *notam 11* is not captured (J-4's class).
- **F13 overturns the p. 288 sheet's item 24 claim** ("acedia at every Bonaventure / Du Cange site"), which `c6-v1-11` had already belied.
- **Outside the gate's reach (recorded, not edited):** Ps. 4:7 "light" at Vol V `bon-hex-c3` ¶ 25 (where the body leans) and `bon-itin-c5` p. 308 n. 3, pre-dating the Vol V *lux / lumen* ruling, belong with the three Vol V *excessus* sites on a later Vol V errata list. "Holy Ghost" survives in five older Lucam chunks' `## Notes` only.
- **Not on the docket, not ruled (passes draft; carried open):** O-1 `c13-v1-9` ¶ 17 *arguitur* "convicted"; O-2 `c13-v1-9` ¶ 12 *quare vacatis?* "why are you idle?"; O-3 `c14-v25-35` ¶ 66 and p. 379 n. 9 **En.** Ps. 18:6 "rejoiced". Each is a one-word register question for a later docket.

### Manifest stage 5

**Drawn at `21637e0`** (Cap. XV – XVIII, pp. 381–472, **19 rows**). Its first row is `bon-luc-c15-v1-7` (Cap. XV vv. 1–7, ¶¶ 1–14, pp. 381–387, `low`), opening at `CAPITULUM XV.` mid-page on p. 381; **p. 381 nn. 12–13 and the t4 *Impietas Iudaeorum…* are its.** Its `low` rows are settled at build time by ruling 39's procedure.

### Tool job (rulings 76, 92): recorded, NOT run

J-1..J-11 (ruling 76) + **J-12** (the `CROSSREF_SLIPS` row for p. 295 n. 15 + a report-only `supra` / `infra` direction screen), with the interval's T-a..T-f sites folded into J-1, J-2, J-4 / J-5, J-6, J-9, J-11. One bounded job; `tools/build-citations.py` only, then `build-citations.py` → `build-index-json.py`; no chunk file. Baseline below (QA 213, anaphora unresolved 391).

### Deploy

Nothing deployed, nothing pushed by this close. **The live site predates the p. 288 gate edits, all nineteen interval chunks and these 42 lines.** Push and deploy are each Wilson's own OK.

---

## CLOSE — suite re-run after the edits (2026-11-16), against the baseline

| check | after the edits | baseline (passes draft) | difference |
|---|---|---|---|
| live flags | **vol7 82 chunks, 2 occurrences = 1 flag** (`c5-v12-16` p. 122 n. 11) | same | none |
| `check-vol5-apparatus.py --volume=vol7` | **82 chunks, 4,429 entries, all checks passed** (p. 381 `1-11 ok PENDING n.12,13`) | same | none (the three `tr-lumen` are not numbered entries) |
| `check-vol5-census.py --volume=vol7` | **vol7 82/82 on disk and in ledger; 221 runovers (192 gutter / 29 page; 79 positive, 3 negative)**; "Rosters agree" | same | none |
| `polish-style-scan.py --volume 7` | **CLEAN (vol7, 82 files)** | same | none |
| `build-citations.py` (`--out` / `--qa` to the scratchpad) | **2,400 chunks; 44,808 records; QA 213**; anaphora 2,346 + 86, **unresolved 391**; coordinate ibid. 485 (382 / 103); printed slips 23, 0 stale; both outputs **byte-identical** to `index/citations.tsv` and `manual-review/citation-qa-report.md` (`cmp`) | same | none, as predicted: the ledger is built from the Latin halves, and the edits are English / Notes only |
| `build-content.mjs` → `build-index-json.py` → `build-content.mjs` | **19 books, 2,399 / 2,399 translated** (both runs); **crossref 1,879 cited / 11,331 backlinks**; goto 2,399 / 5,366; authorities 89 / 436 / 18,490 | same | none |
| `validate-chunk.py` (all 82) | **82 × "1 checked, 0 failed"** | 82 OK | none |
| `tr-` notes, vol7 | **65** (62 + the three new `tr-lumen`, each anchored once) | 62 | +3, the D-3 / F4 notes |
| `tools/build-authorities.py` | regenerated `index/authorities.tsv` with **+499 rows, all in the 19 interval chunks** (none from these edits; `c11-v27-32`, `c12-v35-48`, untouched here, are among them); **restored with `git checkout`, not committed** | not run by the passes draft; the p. 288 close found the file unchanged and committed nothing | **pre-existing drift**: the tracked `index/authorities.tsv` (and so the site's 18,490 authority citations) does not yet carry the interval's records; a regeneration and its commit are owed, Wilson's call, outside this close |

Only `site/src/data/*` (gitignored) was rewritten by the build steps; `git status` after the suite shows only the files this close edited. `vercel build` was not run; nothing was deployed.

**Front: `bon-luc-c15-v1-7`** (manifest stage-5 row 1, `low`; Cap. XV ¶¶ 1–14, pp. 381–387; p. 381 nn. 12–13 and the t4 *Impietas Iudaeorum…* are its; ruling 86: its first divine `tr-pietas` names the *impietas / pietas divina / pietas humana* divisio). **The interval pp. 381–472 needs Wilson's go and a burn OK before any builder is dispatched.** No push, no deploy.
