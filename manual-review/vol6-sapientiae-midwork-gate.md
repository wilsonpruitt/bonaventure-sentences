# Vol VI — *Commentarius in librum Sapientiae*, MID-WORK GATE at the Cap. XII/XIII seam (printed pp. 125–191) — CLOSED

**STATUS: CLOSED 2026-10-16.** Docket ruled by Wilson in one sitting ("all as recommended") → Vol VI **rulings 44–58** in
`manual-review/vol6-pilot-setup.md`. Repairs: A1 *punitio* → "punishing" at **34 body sites + 2 `title_en`** (English only);
B1 three `tr-doctrina` notes (c6, c7, c8); B2 five c8 "zeal" → "study" + `tr-studium`; B3 one scouting-doc line; B4 c6's Notes
count. **No Latin line changed.** Passes 1–3 had been run 2026-10-16 by a read-only agent on Wilson's go (evidence sheet
`manual-review/vol6-sapientiae-midwork-evidence.md`, commit `7fefe3d`). ⛔ **Per ruling 34 this gate carries NO deploy** (one
deploy for the work, at p. 235). Push stays separate and is Wilson's per action.

Ruling 34 placed this gate "at p. 192"; **the seam is p. 191** (`Capitulum XIII.` stands on p. 191 ~0.58; p. 192 carries its
`(Vers. 1.)` — item 20). `bon-sap-c13` is not built and is out of scope; c12 forwards p. 191 n. 8 to it.

**Procedure (the `perfectione` / `serm` / p. 125 precedent):** evidence sheet first, Wilson rules in one sitting, then the edits,
a suite re-run, and pass 4.

**Scope: TEN chunks, pp. 125–191 with no gap, 736 numbered apparatus entries, 9 `tr-` notes.**

| chunk | division / section | type | pages | entries |
|---|---|---|---|---|
| `bon-sap-c3` | 3 / 1 | pericope `"1-19"` | 125–131 | 67 |
| `bon-sap-c4` | 4 / 1 | pericope `"1-20"` | 131–137 | 58 |
| `bon-sap-c5` | 5 / 1 | pericope `"1-24"` | 137–144 | 82 |
| `bon-sap-c6` | 6 / 1 | pericope `"1-27"` | 144–151 | 74 |
| `bon-sap-c7` | 7 / 1 | pericope `"1-30"` | 151–159 | 105 |
| `bon-sap-c8` | 8 / 1 | pericope `"1-21"` | 159–166 | 75 |
| `bon-sap-c9` | 9 / 1 | pericope `"1-19"` | 166–171 | 55 |
| `bon-sap-c10` | 10 / 1 | pericope `"1-21"` | 171–177 | 71 |
| `bon-sap-c11` | 11 / 1 | pericope `"1-26"` | 177–184 | 72 |
| `bon-sap-c12` | 12 / 1 | pericope `"1-26"` | 184–191 | 77 |
| **total** | | | **67 pp.** | **736** |

Every census is over the BUILT files and the RENDERED regions (`## Latin`, `## English`, `## Apparatus`), never over `raw/`.

---

## PASS 1 — live flags: **CLEAN**

`python3.11 tools/check-live-flags.py vol6` → **59 vol6 chunks scanned, no live `[?]`.**

## PASS 2 — style scan + mechanical suite: **CLEAN; two convention defects found by census (docket B1, B2)**

- `polish-style-scan.py`: **2,178 chunks, vol1–vol6** → 11 issues / 6 chunks, all outside Vol VI. **ZERO in vol6.**
- `check-vol5-apparatus.py --volume=vol6`: **59 chunks, 1,756 entries — all checks passed**; in scope La = En in all ten
  (67 · 58 · 82 · 74 · 105 · 75 · 55 · 71 · 72 · 77); p. 191 `PENDING n.8` (c13's).
- `check-vol5-census.py`: vol5 167/167 · **vol6 59/59**, 86 runovers (84 gutter, 2 page); in scope **29 runovers — 28 gutter, 1
  page-crossing (p. 168 n. 11, inside c9)**, each ledgered once by its owner.
- `build-citations.py` into the scratchpad (ledger **byte-identical** to the tracked one): **2,178 chunks → 27,744 records; ours
  1,787** (scripture A 864 · B 304 · C 519; crossref 77 chunk · 19 page-multi · 2 distinctio · 2 work); **corpus QA 208; ZERO QA
  lines ours**; zero dangling/unresolvable/ambiguous. ⚠ Resolver artefacts (ruling 40) in docket C — the largest is C1, an
  `ibid. C, V` coordinate drop measured at **251 records corpus-wide**.
- **La/En digit multiset over all 736 entries: 4 mismatches, all dispositioned** — two ruling-37 brackets (c3 p. 126 n. 1, c5 p. 140
  n. 3), one wrong-sort bracket (c5 p. 144 n. 1), one number word (c11 p. 182 n. 8).
- **Page markers and anchor sequences identical La/En in all ten**; anchor set = definition set; `tr-` anchors English-only.
- **Register censuses** (evidence sheet table): bare "intellect" **0** · English `**Contra:**` **0** · *impius* 61+10 → impious 61+10 ·
  `tr-lumen` in every chunk carrying *lumen* · ⚠ **`tr-doctrina` missing in c6, c7, c8** (B1) · ⚠ **`tr-studium` missing in c8**,
  where *studium* → "zeal" ×5 (B2) · *punitio*/*poena* both → "punishment" at all sites (A1).
- Site build not run by the read-only agent; run it at the gate's close.

## PASS 3 — boundary sweep: **CLEAN**

Every page 125–191 owned exactly once, each register contiguous 1..N, `KNOWN_TOTALS_VOL6` matching on all 67. Seams:
**125** c2 1–3 / c3 4–11 · **131** c3 1–8 / c4 9–11 · **137** c4 0 / c5 1–9 · **144** c5 1–5 / c6 6–9 · **151** c6 1 / c7 2–9 ·
**159** c7 1–11 / c8 0 · **166** c8 1–8 / c9 9–12 · **171** c9 1–4 / c10 5–9 · **177** c10 1–6 / c11 7–9 · **184** c11 1–5 / c12 6–10 ·
**191** c12 1–7 / c13 8 (PENDING). Both sides of every seam state the same split in their apparatus headers; every runover matches
the ledger; every outgoing tail is a complete sentence and every incoming body opens on `### Capitulum N.` and its printed heading.
**No plate was needed for any seam or docket item.**

Found in passing (docket B3): the index page tracks **the page of `(Vers. 1.)`**, not the heading — 11 of 11 openings; Cap. VIII
(159/160) and XIII (191/192) discriminate.

## PASS 4 — plate cleanup: **DONE 2026-10-16**

**Done:** 66 plates deleted from `raw/vision/vol6` (`p-125` … `p-190`; 148 MB → 4.2 MB), **`p-191.png` and `p-192.png` kept for
`bon-sap-c13`**; `/tmp/colcrop/` was already empty (0 files). **~144 MB reclaimed.** All gitignored and regenerable. The
builders' session-scratchpad crops listed below were outside this session and outside the repo and were not touched.

Draft table (pre-rulings):

| set | files | size |
|---|---|---|
| `raw/vision/vol6/p-125.png` … `p-190.png` | 66 | ~144 MB |
| ⚠ **`p-191.png`, `p-192.png` — KEEP** (c13 opens on p. 191 below the heading and reads p. 192 next) | 2 | 4.2 MB |
| `/tmp/colcrop/*` | 0 | 0 (already empty) |
| session scratchpad crops (builders' c10/c12 dirs, `*-small.png`; not in the repo) | 249 | ~103 MB |
| **to delete** | **315** | **~247 MB** |

All gitignored or outside the repo, and regenerable (`tools/extract-pages.py --volume vol6`, `tools/colcrop.py vol6`).

---

## THE DOCKET — RULED 2026-10-16 ("all as recommended")

| # | item | recommendation | lines | ruling |
|---|---|---|---|---|
| A1 | *punitio*/*poena* (item 18) | *punitio* → "punishing" from now, conform c3–c12 | ~43 En | **44 — applied: 34 body sites + 2 `title_en`** |
| A2 | misprint class (items 1, 6, 12, 22 + 5 sites) | ratify as built | 0 | **45 — ratified** |
| A3 | verse test at Job 37:3, Col. 1:12, Isa. 50:11 (item 3) | ratify | 0 | **46 — ratified** |
| A4 | fused headings taken whole (items 11, 16) | ratify as ruling 36's corollary | 0 | **47 — ratified** |
| A5 | ruling 37 in the body (item 17) | ratify | 0 | **48 — ratified** |
| A6 | c7 *actum* (item 2) | leave, no bracket | 0 | **49 — left** |
| A7 | c11 Vers. 27 under `"1-26"` (item 15) | keep the index label | 0 | **50 — kept** |
| A8 | marginal-quaestio counting (items 4, 8) | keep; 25 in scope | 0 | **51 — kept** |
| A9 | c6 *disciplinam* → "instruction" (1 of 46) | decline (ruling 42) | 0/1 | **52 — declined** |
| B1 | ⚠ `tr-doctrina` owed in c6, c7, c8 (item 13) | write 3 notes; ratify "instruction" as the quotation branch | 3 notes | **53 — 3 notes written** |
| B2 | ⚠ `tr-studium` owed in c8; "zeal" vs the work's "study" | write the note; conform to "study" (or keep "zeal") | 1 note (+5) | **54 — conformed (5) + note** |
| B3 | scouting table `Cap. X … 174` → `171`; index = Vers. 1 page (items 9, 20) | correct; adopt as the c13–c19 end rule | 1 doc | **55 — corrected; rule adopted** |
| B4 | carry-list drift (items 2, 8, 20; c6 Notes) | correct in the next resume block | doc | **56 — resume block + c6 Notes** |
| C1 | ⭐ `ibid. C, V` never keeps its coordinates (items 5, 7, 14, 19, 21) — 30 here, 251 corpus-wide | scoped `build-citations.py` job before the p. 235 deploy | tool | **57 — OWED before p. 235 (not done here)** |
| C2–C5 | printed slips in the ledger; dropped continuations; unparsed named units; owner-blind page-multi | park (C2 inside C1's job) | 0 | **58 — parked** |

**If all recommendations are taken: ~43 English lines (A1), +5 if B2 conforms, 4 translator's notes, 1 doc line. No Latin line changes.**

## DEFECTS FOUND

1. **`tr-doctrina` missing** in `bon-sap-c6` (2 sites), `bon-sap-c7` (1, apparatus p. 154 n. 3 — not on the running list) and
   `bon-sap-c8` (4) — ruling 11 requires one per chunk carrying the word.
2. **`tr-studium` missing** in `bon-sap-c8` (7 body + 1 apparatus sites, rendered "zeal" ×5 / "study" ×1).
3. Documentation only: the scouting table's X line; the carry-list's items 2, 8, 20; c6's Notes count of *doctrina*.

## CLOSE — edits, suite re-run, pass 4 (2026-10-16)

**A1 site count — NOT the sheet's 40+1, and why.** Derived from the rendered Latin, the NOUN *punitio* (every case) stands at
**34 body sites, 0 apparatus**: c3 3 · c6 1 · c10 3 · c11 17 · c12 10 — plus the two chunks' `title_la` (→ `title_en`). The
sheet's census (c10 5, c11 20+1, c12 11) also counted the *punire* participles *puniti / punitis / punitum* ("the punished"),
which are not *punitio* and were left alone, and c11's/c12's title lines. Every one of the 34 was paired to its English by reading
the sentence; all took "punishing" with at most an added article ("on the *punishing of them in themselves*", c3; "from the
punishing and torment", c6). One rendering moved off a third word: c11 p. 183 *poenas seu punitiones* had read "punishments or
chastisements" → **"punishments or punishings"** (*castigatio* is live in c3, so "chastisements" was a collision).

**Lines changed, by chunk** (`git diff --numstat`; English + Notes only):

| chunk | change | En lines | Notes lines |
|---|---|---|---|
| `bon-sap-c3` | A1 ×3 (p. 128) | 1 | 1 |
| `bon-sap-c6` | A1 ×1 (p. 146) · B1 `tr-doctrina` anchor (p. 150) + def · B4 *doctrina* count one → two | 2 + def | 2 |
| `bon-sap-c7` | B1 `tr-doctrina`, apparatus-anchored in p. 154 n. 3's `**En.**` + def | 1 + def | 1 |
| `bon-sap-c8` | B2 "zeal" → "study" ×5 (pp. 159, 160, 165 ×2, 166) + `tr-studium` · B1 `tr-doctrina` anchor (p. 160) · 2 defs | 5 + 2 defs | 2 |
| `bon-sap-c10` | A1 ×3 | 2 | 1 |
| `bon-sap-c11` | A1 ×17 + `title_en` | 13 + title | 1 |
| `bon-sap-c12` | A1 ×10 + `title_en` | 10 + title | 1 |
| `sapientiae-pilot-scouting.md` | B3 `Cap. X … 174` → `171` + dated note | doc | — |

**Suite (denominators read):** live flags **59 vol6 chunks, none** · `check-vol5-apparatus.py --volume=vol6` **59 chunks, 1,756
entries — all passed** (p. 191 `PENDING n.8`, c13's; the four new `tr-` notes are outside the counts, English-only, c7's anchored in
the apparatus) · census **vol6 59/59, rosters agree**, 86 runovers (84 gutter, 2 page) · style scan **11 issues / 6 chunks / 2,178
scanned, ZERO in vol6** (unchanged) · `build-citations.py` **2,178 chunks → 27,744 records, QA 208, `index/citations.tsv`
byte-identical** (edits are English-only; `tr-` notes are never indexed, ruling 24) · `build-content` → `build-index-json` (1,725
cited, 10,505 backlinks) → `build-content`: **2,177/2,177 translated.** Page markers and numbered-anchor sequences re-checked La = En
in all seven touched chunks (67 · 74 · 105 · 75 · 71 · 72 · 77); no `tr-` anchor in any Latin.

**Pass 4:** above — ~144 MB, `p-191`/`p-192` kept.

Front advances to `bon-sap-c13`. No push, no deploy (ruling 34: one deploy, at p. 235). **Owed before that deploy: ruling 57's
scoped resolver job, with a before/after ledger diff for Wilson.**
