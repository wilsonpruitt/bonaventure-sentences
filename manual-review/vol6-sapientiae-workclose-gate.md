# Vol VI — *Commentarius in librum Sapientiae*, WORK-CLOSE GATE at p. 235 (printed pp. 107–235) — CLOSED

**STATUS: CLOSED 2026-10-16.** Docket ruled by Wilson in one sitting, verbatim **"all as recommended"**, off the evidence sheet
`manual-review/vol6-sapientiae-workclose-evidence.md` (commit `e36a25f`) → Vol VI **rulings 59–68** in
`manual-review/vol6-pilot-setup.md`. Repairs English/apparatus only — **no Latin line changed.** Passes 1–3 had been run
2026-10-16 by a read-only agent on Wilson's go. The third of ruling 34's three gates (shakedown p. 125 CLOSED, mid-work p. 191
CLOSED). ⛔ **Ruling 57's C1 job + its before/after `index/citations.tsv` diff is still OWED before the p. 235 deploy** —
`tools/build-citations.py` is unchanged since `dfb5adb`; that job is separate from this gate and is its own STOP, as are push
and deploy.

**Procedure (the `perfectione` / `serm` / p. 125 / p. 191 precedent):** evidence sheet first, Wilson rules in one sitting, then the
edits, a suite re-run, and pass 4.

**Scope: all 23 units, pp. 107–235 with no gap, 1,361 numbered apparatus entries, 29 `tr-` notes** (derived from the built files).

| chunk | division / section | type | pages | entries |
|---|---|---|---|---|
| `bon-sap-prooem` | 0 / 1 | prooemium | 107–109 | 22 |
| `bon-sap-prol` | 0 / 2 | expositio | 109–110 | 4 |
| `bon-sap-c1` … `c12` | 1–12 | pericope | 110–191 | 83 · 64 · 67 · 58 · 82 · 74 · 105 · 75 · 55 · 71 · 72 · 77 |
| `bon-sap-c13` | 13 | pericope `"1-19"` | 191–196 | 51 |
| `bon-sap-c14` | 14 | pericope `"1-31"` | 196–203 | 89 |
| `bon-sap-c15` | 15 | pericope `"1-19"` | 204–209 | 59 |
| `bon-sap-c16` | 16 | pericope `"1-29"` | 209–217 | 83 |
| `bon-sap-c17` | 17 | pericope `"1-19"` | 217–221 | 51 |
| `bon-sap-c18` | 18 | pericope `"1-25"` | 221–228 | 62 |
| `bon-sap-c19` | 19 | pericope `"1-20"` | 228–233 | 57 |
| `bon-sap-scholion` | 20 | scholion | 233 | 0 |
| `bon-sap-schemata` | 21 | schemata | 234–235 | 0 |
| **total** | | | **129 pp.** | **1,361** |

Every census is over the BUILT files and the LIVE region (`## Latin`, `## English`, `## Apparatus`), never `raw/`.

---

## PASS 1 — live flags: **CLEAN**

`python3.11 tools/check-live-flags.py vol6` → **68 vol6 chunks scanned, no live `[?]`.**

## PASS 2 — style scan + mechanical suite: **CLEAN; two convention defects found by census (docket B1, B2)**

- `polish-style-scan.py`: **2,187 chunks, vol1–vol6** → 11 issues / 6 chunks (the standing Vol III/IV/V baseline). **ZERO in vol6.**
- `check-vol5-apparatus.py --volume=vol6`: **68 chunks, 2,208 entries — all checks passed**; all 23 Sapientiae units La = En; no PENDING.
- `check-vol5-census.py`: vol5 167/167 · **vol6 68/68**, 107 runovers (104 gutter, 3 page); Sapientiae **59 (57 gutter, 2 page)**.
- `build-citations.py` into the scratchpad: **2,187 chunks → 28,709 records**, ledger **byte-identical**; QA **208**, **ZERO lines ours**;
  ours **3,136** (scripture A 1,472 · B 594 · C 879; crossref 148 chunk · 37 page-multi · 4 distinctio · 2 work).
- `build-content` → `build-index-json` → `build-content`: **2,186 / 2,186 translated**; index **1,732 cited / 10,560 backlinks**.
  Outputs gitignored; `git status` clean afterwards.
- Anchors, page markers, def sets: identical La/En in all 23; `tr-` anchors English-only (or in an apparatus `**En.**`, ruling 13).
- Register censuses (evidence sheet): ⚠ ***supplicium* 25 sites**, three rendered "torment", seven meeting *poena* (A1) · ⚠ **ruling 44 not
  applied in `prooem`/`c1`** (B1) · ⚠ **`tr-studium` missing in the Schemata** (B2) · bare "intellect" 0 · English `**Contra:**` 0 ·
  *impius* 109 → impious 109 · `tr-lumen` / `tr-doctrina` / `tr-vacare` in every unit carrying the word.

## PASS 3 — boundary sweep: **CLEAN**

Every page 107–235 owned, each register contiguous 1..N, `KNOWN_TOTALS_VOL6` matching throughout. Twenty shared leaves + one leaf
edge (203/204), all re-derived from the defs and stated identically from both sides:
**109** prooem 1–5 / prol 6–8 · **110** prol 1 / c1 2–7 · **118** c1 1–3 / c2 4–8 · **125** c2 1–3 / c3 4–11 · **131** c3 1–8 / c4 9–11 ·
**137** c4 0 / c5 1–9 · **144** c5 1–5 / c6 6–9 · **151** c6 1 / c7 2–9 · **159** c7 1–11 / c8 0 · **166** c8 1–8 / c9 9–12 · **171** c9 1–4 /
c10 5–9 · **177** c10 1–6 / c11 7–9 · **184** c11 1–5 / c12 6–10 · **191** c12 1–7 / c13 8 · **196** c13 1–4 / c14 5–11 · **203|204** leaf edge ·
**209** c15 1–5 / c16 6–7 · **217** c16 1–4 / c17 5–8 · **221** c17 1–12 / c18 0 · **228** c18 1 / c19 2–8 · **233** c19 1–6 / Scholion 0.
Every outgoing tail is a complete sentence; every incoming body opens on its printed heading; all 59 runover-ledger entries are owned by
their ledgering chunk and stated in its Notes; the p. 216 n. 9 page-crossing is ledgered once (c16). **No plate was opened.**

### Misprint-bracket inventory (running-list item 6; rendered English, 21)

c1 p. 115 n. 6 Job 6:2 → 6:25 · c2 p. 121 n. 3 *Doctr. christ.* I c. 3 → c. 4 · c3 p. 126 n. 1 Job 24:19 → 5:19 · c5 p. 137 *coa tam* `[*sic*]` ·
c5 p. 140 n. 3 Vers. 30 → I Cor. 12:31 · c5 p. 144 n. 1 `9.` for *q.* · c6 p. 146 *sequalis* · c6 p. 147 *sapientium* · c6 p. 148 *merilo* ·
c8 p. 165 *defcctione* · c10 p. 171 *illam* · c10 p. 173 *Sapientium* · c11 p. 180 Prov. 16 → 24:16 · c16 p. 213 Ecclus. → Eccles. 11:3 ·
c16 p. 212 n. 8 `Eccli. 21 4` `[*sic*]` · c16 p. 214 n. 12 *potebat* · c17 p. 218 *dati* (A4) · c17 p. 218 n. 1 *iucuerunt* ·
c18 p. 226 *parte a* · c18 p. 226 Ezech. 20 → 22:30 · Schemata p. 234 *iudicum*.

## PASS 4 — plate cleanup: **DONE 2026-10-16**

Deleted all 47 plates `raw/vision/vol6/p-191.png` … `p-237.png` (96,044 KiB; `raw/vision/vol6/` now empty — pp. 107–190 had
gone at the earlier gates' pass 4) and `/tmp/colcrop/*` (42 files, 91,104 KiB). **~183 MiB reclaimed.** All gitignored and
regenerable (`tools/extract-pages.py --volume vol6`, `tools/colcrop.py vol6`); nothing kept — the *Ioannem* mini-pilot extracts
its own. Covered by Wilson's "all as recommended" (gate pass-4 cleanup approved at the previous gate).

---

## THE DOCKET — RULED 2026-10-16 ("all as recommended")

| # | item | recommendation | lines | ruling |
|---|---|---|---|---|
| A1 | ⭐ *supplicium* — 25 sites; "punishment of punishment" ×5; c1 p. 117 silent *poena* → "penalty" | ***supplicium* → "penalty"** (24 sites; Matt. 25:46 in c3's Gloss keeps "punishment"); c1's *poena* → "punishment" | ~22 En | **59 — applied: 24 sites + c1 *poena* revert** |
| A2 | c11 p. 182 "punishments or punishings" | keep | 0 | **60 — kept** |
| A3 | Job 24:13 c14 "light" / c17 "lumen" | ratify (ruling 46, by passage) | 0 | **61 — ratified** |
| A4 | c17 p. 218 *dati* bracket | keep (ruling 45) | 0 | **62 — kept** |
| A5 | Schemata *de merito culpae* "desert" vs c13/c16 "merit of fault" | conform the Schemata to "merit of fault" | 1 En | **63 — conformed (1)** |
| A6 | c19 `Opponitur` + c16 `Obiectio` (ruling 51) | keep the rule — 61 in the work | 0 | **64 — kept (61)** |
| A7 | *tormentum* → "punishment" at c11 p. 180 / c5 p. 142 n. 8 (Douay) | conform to "torment(s)" | 2 En | **65 — conformed (2)** |
| B1 | ruling 44 not applied in `prooem` p. 108–109, `c1` p. 115 | "punishing" ×2 | 2 En | **66 — applied (2)** |
| B2 | `tr-studium` missing in the Schemata | write the note | 1 note | **67 — note written** |
| B3 | doc: p. 183 → p. 182; *supplicatio* in c18 | next resume block | doc | **68 — corrected** |
| — | ruling 57's C1 job + diff | **OWED before the deploy; not this gate's** | tool | — |

**If all recommendations are taken: ~27 English lines + 1 translator's note + doc. No Latin line changes.**

## CLOSE — edits, suite re-run, pass 4 (2026-10-16)

**A1 re-derived by script over the LIVE region before editing** (`## Latin` / `## English` / `## Apparatus`, Latin and English
paired by paragraph index): **25 *supplic-ium* sites — 24 body + 1 apparatus (c2 p. 124 n. 3)**, exactly the sheet's table;
c18's two `supplic-` hits are *supplicatio* (not this word). Converted **24** to "penalty"/"penalties" (plurals: c2 n. 3
*suppliciorum*, c5 p. 138 *suppliciorum*, c5 p. 143 *suppliciis*, c17 *supplicia*; one added article, c1 p. 113 *ad supplicium*
→ "to the penalty"); **Matt. 25:46 in c3's Gloss keeps "eternal punishment"**, as the sheet recommended. c1 p. 117
*seu poenae inflictae* back to "or of the punishment inflicted". **Collision check:** every English "penalt-" in the work listed
by sentence — 24 *supplicium* sites + c2 p. 118 *propter poenalitatem* "on account of penalty" (ruling 20), which stands in its
own paragraph; **no sentence holds both, no collision.** Afterwards: zero "punishment" for *supplicium* in the live region except
the one Douay quotation. **B1 verified the same way:** 69 *punitio* noun sites in the work, and every Latin paragraph carrying
*n* of them has ≥ *n* "punishing" in its English paragraph (zero short).

**Lines changed, by chunk** (English text lines; Notes = one dated "Work-close gate" bullet appended per touched chunk, superseding
the banked renderings; `git diff --numstat` in the commit):

| chunk | change | En lines | Notes |
|---|---|---|---|
| `bon-sap-prooem` | B1 (p. 108–109) | 1 | +1 |
| `bon-sap-c1` | A1 ×5 + *poena* revert (pp. 113, 117) · B1 (p. 115) | 4 | +1 |
| `bon-sap-c2` | A1 body (p. 119) + apparatus p. 124 n. 3 | 2 | +1 |
| `bon-sap-c3` | A1 (p. 128); Matt. 25:46 (p. 129) kept | 1 | +1 |
| `bon-sap-c5` | A1 ×4 (pp. 138, 142 ×2, 143) · A7 p. 142 n. 8 | 5 | +1 |
| `bon-sap-c6` | A1 ×2 (pp. 144, 146) | 2 | +1 |
| `bon-sap-c10` | A1 (p. 173) | 1 | +1 |
| `bon-sap-c11` | A7 lemma (p. 180) | 1 | +1, B3 p. 183 → 182 |
| `bon-sap-c13` | A1 (p. 191) | 1 | +1 |
| `bon-sap-c16` | A1 ×3 (run heading, divisio, Vers. 4) | 3 | +1 |
| `bon-sap-c17` | A1 (p. 219) | 1 | +1 |
| `bon-sap-schemata` | A1 ×4 (3 lines) · A5 · B2 anchor + `tr-studium` def | 5 + def | +1; status line + Notes note-count |
| `vol6-sapientiae-midwork-gate.md` | B3 p. 183 → 182 | doc | — |
| **total** | | **27 + 1 note** | |

No `title_en` quoted *supplicium* (c16's is *De poena sensus duplici*); the one English heading carrying it, c16's run heading
(`####`), is among the A1 sites.

**Suite (denominators read):** live flags **68 vol6 chunks, none** · `check-vol5-apparatus.py --volume=vol6` **68 chunks, 2,208
entries — all checks passed** (unchanged; the new `tr-studium` is outside the counts, English-only) · `check-vol5-census.py`
**vol5 167/167 · vol6 68/68, rosters agree**, vol6 107 runovers (104 gutter, 3 page) · `polish-style-scan.py` **11 issues / 6
chunks / 2,187 scanned, ZERO in vol6** (the standing baseline) · `build-citations.py` **2,187 chunks → 28,709 records, QA 208,
232 no-citation; `index/citations.tsv` BYTE-IDENTICAL** (edits English-only; `tr-` notes never indexed, ruling 24) ·
`build-content` → `build-index-json` (**1,732 cited / 10,560 backlinks**) → `build-content`: **16 books, 2,186 / 2,186
translated.**

**Pass 4:** above — ~183 MiB.

Front: **ruling 57's C1 resolver job + its before/after `index/citations.tsv` diff for Wilson (OWED before the deploy; dispatch on
Wilson's go)**, then ONE deploy at p. 235 (Wilson's OK), then the *Commentarius in Ioannem* mini-pilot. No push, no deploy here.
