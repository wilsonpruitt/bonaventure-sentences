# Vol VI — *Commentarius in librum Sapientiae*, WORK-CLOSE GATE at p. 235 (printed pp. 107–235) — OPEN

**STATUS: OPEN.** Passes 1–3 run 2026-10-16 by a read-only agent on Wilson's go ("Run the gate"). **Docket awaiting Wilson's
rulings** — evidence sheet `manual-review/vol6-sapientiae-workclose-evidence.md`. No chunk edited; no push, deploy or stash.
Repairs, a suite re-run and pass 4 follow the rulings (a later agent). The third of ruling 34's three gates (shakedown p. 125
CLOSED, mid-work p. 191 CLOSED). ⛔ **Ruling 57's C1 job + its before/after `index/citations.tsv` diff is still OWED before the
p. 235 deploy** — `tools/build-citations.py` is unchanged since `dfb5adb`; that job is separate from this gate and is its own STOP,
as are push and deploy.

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

## PASS 4 — plate cleanup: **NOT RUN (awaits the rulings and Wilson's OK)**

Plates on disk: `raw/vision/vol6/p-191.png` … `p-237.png` (47 files, gitignored, regenerable). Disk ~7.9 GiB free — **nothing
deleted.** No plate is needed by any docket item.

---

## THE DOCKET — AWAITING WILSON

| # | item | recommendation | lines | ruling |
|---|---|---|---|---|
| A1 | ⭐ *supplicium* — 25 sites; "punishment of punishment" ×5; c1 p. 117 silent *poena* → "penalty" | ***supplicium* → "penalty"** (24 sites; Matt. 25:46 in c3's Gloss keeps "punishment"); c1's *poena* → "punishment" | ~22 En | — |
| A2 | c11 p. 182 "punishments or punishings" | keep | 0 | — |
| A3 | Job 24:13 c14 "light" / c17 "lumen" | ratify (ruling 46, by passage) | 0 | — |
| A4 | c17 p. 218 *dati* bracket | keep (ruling 45) | 0 | — |
| A5 | Schemata *de merito culpae* "desert" vs c13/c16 "merit of fault" | conform the Schemata to "merit of fault" | 1 En | — |
| A6 | c19 `Opponitur` + c16 `Obiectio` (ruling 51) | keep the rule — 61 in the work | 0 | — |
| A7 | *tormentum* → "punishment" at c11 p. 180 / c5 p. 142 n. 8 (Douay) | conform to "torment(s)" | 2 En | — |
| B1 | ruling 44 not applied in `prooem` p. 108–109, `c1` p. 115 | "punishing" ×2 | 2 En | — |
| B2 | `tr-studium` missing in the Schemata | write the note | 1 note | — |
| B3 | doc: p. 183 → p. 182; *supplicatio* in c18 | next resume block | doc | — |
| — | ruling 57's C1 job + diff | **OWED before the deploy; not this gate's** | tool | — |

**If all recommendations are taken: ~27 English lines + 1 translator's note + doc. No Latin line changes.**
