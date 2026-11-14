# Vol VII — *Commentarius in Evangelium S. Lucae*, SHAKEDOWN GATE at p. 27 (printed pp. 3–27) — CLOSED

**STATUS: CLOSED 2026-11-14.** Docket ruled by Wilson in one sitting ("Approve all", 2026-11-14) → Vol VII rulings 17–26 in `manual-review/vol7-pilot-setup.md` § *LUCAM* SHAKEDOWN GATE. **8 English lines changed across four chunks (prooem 3 · c1-v5-17 1 · c1-v18-25 3 · c1-v26-38 1), plus Notes; no line in any `## Latin` body or `**La.**` half changed.** One code line (`TOMES[7]`), two doc restatements (ruling 12's *evangelizare* sentence; the `title_la` gloss), one tool job queued.

Ruling 14 placed this gate at p. 27. ⛔ **Per ruling 14 this gate carries NO deploy** (one deploy by default, at p. 604; every gate is a legitimate deploy boundary Wilson may call, per action; **p. 88 is the recommended Advent boundary, and that deploy is asked for on its own when the p. 88 gate closes**). Push stays separate and is Wilson's, per action. Nothing was pushed or deployed at this close.

**Procedure (the *Ioannem* p. 268 precedent):** a read-only agent compiled the evidence sheet, `manual-review/vol7-lucam-shakedown-gate-evidence-sheet.md` (censuses over the rendered region, the decisive sentence, alternatives with costs, a ⭐ recommendation per item), and a second read-only agent ran Passes 1–3 into `manual-review/vol7-lucam-shakedown-gate-passes-draft.md`. Both are kept as the evidence record and are summarised here, not repeated. Wilson ruled in one sitting; the edits, the re-run and Pass 4 then closed the gate.

**Scope: SIX chunks, pp. 3–27 with no gap, 220 numbered apparatus entries, 7 `tr-` notes.**

| chunk | division / section | type | pages | entries |
|---|---|---|---|---|
| `bon-luc-prooem` | 0 / 1 | prooemium | 3–7 | 35 |
| `bon-luc-prol` | 0 / 2 | expositio | 7–11 | 34 |
| `bon-luc-c1-v1-4` | 1 / 1 | pericope `"1-4"` | 11–12 | 11 |
| `bon-luc-c1-v5-17` | 1 / 2 | pericope `"5-17"` | 12–17 | 50 |
| `bon-luc-c1-v18-25` | 1 / 3 | pericope `"18-25"` | 17–20 | 21 |
| `bon-luc-c1-v26-38` | 1 / 4 | pericope `"26-38"` | 20–27 | 69 |
| **total** | | | **25 pp.** | **220** |

p. 27 nn. 7–11 belong to the next, unbuilt chunk (`bon-luc-c1-v39-45`). `tr-` notes: prooem `tr-annuntiare`; prol `tr-corrigenda`; c1-v5-17 `tr-annuntiare`, `tr-corrigenda`; c1-v18-25 `tr-evangelizare`; c1-v26-38 `tr-corrigenda`, `tr-corrigenda-2`.

---

## PASS 1 — live flags: **CLEAN**

`python3.11 tools/check-live-flags.py vol7` → **6 vol7 chunks scanned, no live `[?]`** (denominator: 6 = all of vol7). Same after the edits.

## PASS 2 — mechanical suite: **CLEAN**

- `check-vol5-apparatus.py --volume=vol7`: **6 chunks, 220 entries, La = En in every chunk, all checks passed**; 25 known page totals (pp. 3–27); p. 27 `PENDING n.7–11`.
- `check-vol5-census.py`: **vol7 6/6, rosters agree; 18 runovers (15 gutter / 3 page: p. 9 n. 7, p. 13 n. 10, p. 21 n. 10)**.
- `polish-style-scan.py`: **11 issues / 6 chunks / 2,324 scanned, all in Vols III–V (10 PAIR, 1 V5LABEL `bon-hex-c23`); ZERO ours.**
- `build-citations.py`: **2,324 chunks → 36,077 records; QA 211** (209 at the Vol VI gate; +2 not in vol7). Ours: **474 ledger records, 0 QA flags.**
- Page markers identical La/En in all six; numeric anchor sequences identical La/En, unique and ascending (35/34/11/50/21/69); `tr-` anchors English-only, as designed.
- La/En digit multiset per entry: **2 mismatches of 220, both false positives** (the `[so printed; the verse is …]` glosses at p. 5 nn. 4 and 6).

## PASS 3 — boundary sweep: **CLEAN**

Every page 3–27 owned exactly once with a contiguous 1..N register; `KNOWN_TOTALS_VOL7` matches the plate on every leaf read. Six seams read on the 300 dpi plates (pp. 7, 11, 12, 17, 20, 27): no splice, drop or duplication; every outgoing tail is a complete sentence or the printed hyphen (pp. 12/13, 17/18); every note assigned by anchor. Footer spot-checks against 1.7× bands on pp. 4, 7, 8, 11, 12, 14, 17, 18, 20, 23, 27 found no difference in any digit, locus or siglum. Seam table: passes draft § PASS 3.

## PASS 4 — plate cleanup: **DONE 2026-11-14**

**Deleted from `raw/vision/vol7/`:** `p-001.png` … `p-026.png` (26 plates, 91 MB: the two leaves before the work and every leaf of the shakedown interval except p. 27). **Deleted from `/tmp/colcrop/`:** the 138 vol7 column bands for pp. 3–26 (`vol7-p003-*` … `vol7-p026-*`; pages present were 3–20, 22, 26), 332 MB.
**Kept in `raw/vision/vol7/`:** `p-027.png` (the next chunk opens on it, nn. 7–11 are its) · the manifest-stage-1 boundary plates `p-030, 034, 038, 043, 044, 048, 051, 054, 056, 058, 061, 062, 064, 065, 069, 075, 078, 081, 085, 087, 088` (p. 62 is ruling 26's read) · `p-112, 128, 252` (scouting/structure plates for later chunks) · `p-604 … 607, 652, 655, 657` (work close and Appendix scouting) · `p-858` (the Corrigenda leaf). **Kept in `/tmp/colcrop/`:** the vol7 bands for pp. 27 and later (manifest work) and 36 vol6 bands (pp. 220, 252, 447, 501, 551, 573: the ruling-9 Vol VI corrigenda job's, not this gate's; left for Wilson). Nothing in `raw/` other than extracted plates was touched.

---

## THE DOCKET — RULED 2026-11-14, "Approve all"

| # | item | ruling | lines applied | recorded |
|---|---|---|---|---|
| 1 | ruling 12 register, sites in view | **Ruling 12 ratified at every site; carried-rule departures fixed:** *eruditio* → "erudition" (`prooem` ¶ 17, `c1-v5-17` ¶ 7); Acts 10:38 "Holy Ghost" → "Holy Spirit" (`prooem` ¶ 18); *generalis intelligentia* → "general intelligence" (`prooem` ¶ 24). *documentum* ratified by number. `c1-v18-25` Notes' III Kings 1:42 Douay claim corrected | 4 English + Notes | ruling 17 |
| 2 | *evangelizare* | **`c1-v18-25` ratified as built; ruling 12 amended to its reason** ("preach the gospel", never bare "preach"; Douay "bring good tidings" stands at 1:19, 2:10 with `tr-evangelizare`). Prooem Notes' "the Douay's wording" (4:43) corrected | 0 English + Notes + ruling sentence | ruling 18 |
| 3 | *verecundia* | **"shamefastness" / "shamefast" for the work; *pudicitia* → "purity":** `c1-v18-25` ¶ 35, ¶ 38, p. 20 n. 3 | 3 English + Notes | ruling 19 |
| 4 | Ps. 118:173 "Let thy hand be done" | **Ratified** (silent Douay adjustment + Notes is the practice) | 0 | ruling 20 |
| 5 | *praedicabilis*, Cant. 6:8 | **"worthy to be preached" kept; Cant. 6:8 → "preached her most blessed"** (`c1-v26-38` ¶ 49) | 1 English + Notes | ruling 21 |
| 6 | `title_la` scope | **Lowest heading of the opening stack, whole** (*Ioannem* 79(b)); gloss restated in `vol7-pilot-setup.md` and `lucam-chunk-manifest-notes.md`; no title changes | 0 + 2 doc | ruling 22 |
| 7 | corrigenda addendum inside a note | **Shape kept**; one browser look at the next preview owed | 0 | ruling 23 |
| 8 | ruling 13 citation class | **INBOUND "Comment. in Luc." class, chapter + verse; no in-work `supra n.` class yet.** **TOOL JOB, QUEUED, NOT RUN** (below) | 0 | ruling 24 |
| 9 | `TOMES[7]` | **`7: { title: "Book VII: Commentarius in Evangelium S. Lucae", initial: "7" }`** added to `site/scripts/build-content.mjs`, with the title-page wording quoted in a comment | 1 code | ruling 25 |
| 10 | `low` rows at ¶ 81 | **¶ 81 cut kept**; rows stay `low` until their builder reads pp. 58–65 | 0 | ruling 26 |

### Lines changed (git diff, `vol7/`)

| chunk | English lines | Notes lines | Latin lines |
|---|---|---|---|
| `bon-luc-prooem` | 3 (¶¶ 17, 18, 24) | 3 amended + 1 gate paragraph | **0** |
| `bon-luc-c1-v5-17` | 1 (¶ 7) | 1 amended + 1 gate paragraph | **0** |
| `bon-luc-c1-v18-25` | 3 (¶ 35, ¶ 38, p. 20 n. 3 En) | 3 amended + 1 gate paragraph | **0** |
| `bon-luc-c1-v26-38` | 1 (¶ 49) | 1 amended + 1 gate paragraph | **0** |

Each site was read with its decisive Latin before the edit; every site was as the sheet described. Verified after the edits by mapping each diff hunk to its section: every changed line is in `## English`, an `**En.**` half or `## Notes`. Each touched chunk carries a closing "⭐ p. 27 SHAKEDOWN GATE — RULED" paragraph in its `## Notes`.

### Tool follow-up (item 8): recorded, NOT run — the next queued job

One tool job, after the gate and separately (the *Ioannem* ruling 82(a) pattern): write the inbound Luke-commentary class in `tools/build-citations.py`, keyed **chapter + verse** (`Comment.? in Luc(am)?` + `c.`/roman/bare chapter + verse, `ad` allowed), resolving to the chunk whose `verses:` holds the verse and reading `forward` until it is built; the one `c. 6. n. 20` site (`bon-sent-III-d36-a1-q1`) by `paragraphs:`; other authors' "in Luc." excluded by `governed_by_author`; and fix the page+note branch so `pag. 7, nota 5` resolves to `bon-luc-prol` instead of `page-multi`. ~22 sites in 19 Vols I–VI chunks re-class from scripture to crossref; ledger/QA re-run, then `build-index-json.py`. No in-work `supra n. N` class. It is not a precondition for `bon-luc-c1-v39-45`.

---

## DEFECTS FOUND

**No text defect in the mechanical sense.** Zero live flags, zero count mismatches, zero seam defects, zero style hits ours. The register corrections above are ruled conformances to carried rules. Three documentation errors in Notes were corrected (prooem 4:43 "the Douay's wording"; c1-v18-25 III Kings 1:42 "the Douay's"; prooem *intelligentia* justification).

---

## CLOSE — suite re-run after the edits (2026-11-14), against the baseline

| check | result after the edits | baseline (passes draft) | difference |
|---|---|---|---|
| live flags | **vol7 6 chunks, none** | same | none |
| `check-vol5-apparatus.py --volume=vol7` | **6 chunks, 220 entries, all passed** (p. 27 PENDING n.7–11) | same | none |
| `check-vol5-census.py` | **vol7 6/6, rosters agree; 18 runovers (15 gutter / 3 page)** | same | none |
| `polish-style-scan.py` | **11 issues / 6 chunks / 2,324 scanned, ZERO ours** | same | none |
| `validate-chunk.py` (4 touched chunks) | **4 checked, 0 failed** | — | — |
| `build-citations.py` | **36,077 records, QA 211**; `index/citations.tsv` and the QA report **byte-identical** (`git status` clean under `index/`) | same | none, as predicted: the ledger is built from the Latin halves and the edits are English/Notes only |
| `cd site && node scripts/build-content.mjs` | **2,323/2,323 translated, 19 books**; Luke now carries `tomeTitle` "Book VII: Commentarius in Evangelium S. Lucae" | 2,323 | `TOMES[7]` only |
| `build-index-json.py` | **1,842 cited / 11,306 backlinks** | — | — |

**Front advances to `bon-luc-c1-v39-45`** (pp. 27–30, ¶¶ 71–85; opens at 27R top under the t3 cascade *Secundo, de gratiarum actione pro utraque conceptione.* / ¶ 71 / *De prima gratiarum actione dicuntur tria.* / *Primo praemittitur testimonium prophetiae.*; p. 27 nn. 7–11 are its). **No push, no deploy.**
