# Vol VI — *Commentarius in Evangelium S. Ioannis*, SHAKEDOWN GATE at p. 268 (printed pp. 239–269) — CLOSED

**STATUS: CLOSED 2026-10-21.** Docket ruled by Wilson in one sitting ("Approve all", 2026-10-21) → Vol VI rulings 79–82 in `manual-review/vol6-pilot-setup.md`. One documentation defect repaired (2 lines); 58 lines changed in all across ten chunks (titles, register, housekeeping, Notes), **no Latin line in `## Latin` or `## Apparatus` changed**.

Ruling 76 placed this gate at p. 268, after Capitulum I. ⛔ **Per ruling 76 this gate carries NO deploy** (one default deploy for the work, at p. 532). Push stays separate and is Wilson's per action. ⚠ **The next deploy from `master` publishes *Ioannem*** (Cap. I) along with everything committed since the p. 235 *Sapientiae* deploy of 2026-10-19.

**Procedure (the `perfectione` / `serm` / Sap precedent):** a read-only agent compiled the evidence sheet FIRST, `manual-review/vol6-ioannem-gate-evidence-sheet.md` (site counts by chunk over the live region, the decisive sentence in both languages, alternatives with a one-line cost, a recommendation), and a second read-only agent ran Passes 1–3 into `manual-review/vol6-ioannem-gate-passes-draft.md`. Both are kept as the evidence record and are folded in below, not repeated. Wilson ruled in one sitting; the four passes then closed.

**Scope: THIRTEEN chunks, pp. 239–269 with no gap, 331 numbered apparatus entries, 12 `tr-` notes.**

| chunk | division / section | type | pages | entries |
|---|---|---|---|---|
| `bon-ioan-prooem` | 0 / 1 | prooemium | 239–244 | 52 |
| `bon-ioan-prol` | 0 / 2 | expositio | 244–245 | 9 |
| `bon-ioan-c1-v1-2` | 1 / 1 | pericope `"1-2"` | 246–248 | 22 |
| `bon-ioan-c1-v3-5` | 1 / 2 | pericope `"3-5"` | 248–250 | 22 |
| `bon-ioan-c1-v6-8` | 1 / 3 | pericope `"6-8"` | 250–251 | 18 |
| `bon-ioan-c1-v9-14` | 1 / 4 | pericope `"9-14"` | 251–254 | 29 |
| `bon-ioan-c1-v15-18` | 1 / 5 | pericope `"15-18"` (was `"14-18"`) | 254–256 | 25 |
| `bon-ioan-c1-v19-23` | 1 / 6 | pericope `"19-23"` | 256–258 | 23 |
| `bon-ioan-c1-v24-28` | 1 / 7 | pericope `"24-28"` | 258–259 | 23 |
| `bon-ioan-c1-v29-30` | 1 / 8 | pericope `"29-30"` | 259–260 | 7 |
| `bon-ioan-c1-v31-34` | 1 / 9 | pericope `"31-34"` | 260–261 | 17 |
| `bon-ioan-c1-v35-42` | 1 / 10 | pericope `"35-42"` | 261–265 | 38 |
| `bon-ioan-c1-v43-51` | 1 / 11 | pericope `"43-51"` | 265–269 | 46 |
| **total** | | | **31 pp.** | **331** |

(The scope total equals the sum of `KNOWN_TOTALS_VOL6` for pp. 239–268 plus p. 269 n. 1.) Every census is over the BUILT files and the RENDERED regions (`## Latin`, `## English`, `## Apparatus`), never over `raw/` or `## Notes`.

---

## PASS 1 — live flags: **CLEAN**

`python3.11 tools/check-live-flags.py vol6` → **81 vol6 chunks scanned, no live `[?]`** (denominator read: 81 is all of vol6 and includes the 13 in scope).

## PASS 2 — style scan + mechanical suite: **CLEAN; one documentation DEFECT (below)**

(Full detail: `vol6-ioannem-gate-passes-draft.md` § PASS 2, with the `tr-` count corrected there from 11 to **12**.)

- `polish-style-scan.py`: **2,200 chunks scanned** → 11 issues / 6 chunks, all outside Vol VI (10 PAIR Vols III–IV, 1 V5LABEL `bon-hex-c23`). **ZERO ours**, before and after the edits.
- `check-vol5-apparatus.py --volume=vol6`: **81 chunks, 2,539 entries, all checks passed**; La = En in all 13; p. 269 `PENDING n.2–13` (Capitulum II's).
- `check-vol5-census.py`: vol5 167/167 · **vol6 81/81, rosters agree**; **124 runovers (120 gutter-crossing, 4 page-crossing)**.
- `build-citations.py`: **2,200 chunks → 29,110 records; QA 209; ours 374 records from the 13 chunks and ONE QA flag** (`bon-ioan-c1-v15-18` p. 256 n. 3 `III. d. 14. a. 1. q. 3.`, already on the resolver docket); five unresolved-`ibid.` lines (p246-5, p248-8, p250-10, p255-6, p256-5) sit outside the 209. `index/citations.tsv` and the QA report **byte-identical** after the edits (the edits touch English, titles and Notes; no `**La.**` half changed).
- **La/En digit multiset per entry: 4 mismatches of 331, all false positives** (p. 246 n. 1 and p. 250 n. 3 `83 Qq.` spelled out; p. 261 n. 10 doubled `[n. 60, 65 and 67]`; p. 259 n. 15 `d. XXV.` → "25", a NOTE, see below).
- **Page markers and anchor sequences identical La/En in all 13 chunks** (counts 52/9/22/22/18/29/25/23/23/7/17/38/46).

## PASS 3 — boundary sweep: **CLEAN**

Every page 239–269 owned exactly once with a contiguous 1..N register; `KNOWN_TOTALS_VOL6` matches the plate on every leaf read. Twelve seams read on the 450 dpi plates (pp. 244, 245/246, 248, 250, 251, 254, 256, 258, 259, 260, 261, 265) plus the hand-off at p. 269 (n. 1 `c1-v43-51`'s, nn. 2–13 Capitulum II's). No seam shows a cascade-merge splice; every outgoing tail is a complete sentence and every incoming body opens on its printed paragraph number or heading. The only unnumbered LEFT-block head in scope is p. 265 (p. 264 n. 12, ledgered `page`); every unnumbered RIGHT-block head is a ledgered gutter runover; the three `-` ledger lines (`c1-v15-18`, `c1-v19-23`, `c1-v29-30`) are CONFIRMED. Seam table: `vol6-ioannem-gate-passes-draft.md` § PASS 3.

## PASS 4 — plate cleanup: **DONE 2026-10-21**

**Deleted from `raw/vision/vol6/`:** `p-237.png` … `p-268.png` (32 plates: the Prooemium/Prologus and Capitulum I leaves, plus the two leaves before the work, 237–238) · `idx-677.png` … `idx-688.png` (12 volume-index crops from the pilot) · and **all 124 files in `/tmp/colcrop/`** (~196 MB).
**Kept:** `p-269.png` (Capitulum II opens on it; the Sapientiae gate kept `p-125.png` the same way) and `p-529.png` … `p-533.png` (the pilot's scouting of the Scholion/Schemata leaves, which belong to a later chunk).

---

## THE DOCKET — RULED 2026-10-21, "Approve all"

| # | item | ruling | lines applied | recorded |
|---|---|---|---|---|
| 1 | headless-pericope titles (`c1-v24-28`, `c1-v29-30`, `c1-v31-34`, `c1-v35-42`) | **Eccl ruling 17 applied:** `title_la` = the divisio's first sentence after the lemma, with matching `title_en`; ruling 17 cited in each chunk's Notes; the lemma default is withdrawn | per chunk: `title_la`, `title_en`, `## *…*`, the `transcription_status` title clause, the Notes TITLE paragraph (5 lines × 4 = 20; sheet estimated 16 without the Notes paragraph and status clause). English titles carry item 4(i) ("gave", "gives") | ruling 79(a) |
| 2 | stacked heading at `c1-v43-51`; dropped ordinals | **Keep lowest heading, whole (Sap ruling 47), 0 lines.** **Ordinals RESTORED** at `c1-v3-5` (*Secundo,* / "Second,"), `c1-v15-18` (*Primo,* / "First,"), `c1-v19-23` (*Primo,* / "First,") | 3 chunks × (`title_la`, `title_en`, `## *…*`) = 9, plus 3 Notes lines | ruling 79(b), (c) |
| 3a | *virtus* → power/virtue | **Ratified as built** (9 "power", 11 "virtue", ¶ 71 *virtutem baptizandi* stays "virtue") | 0 | ruling 80(a) |
| 3b | "Holy Spirit" in Douay | **"Holy Spirit" everywhere:** `c1-v15-18` p. 254 n. 9 "Holy Ghost" → "Holy Spirit" | 1 | ruling 80(b) |
| 3c | *studium* one-root rule | **Released for *Ioannem*** (Sap ruling 54's reason belongs to *Sapientia*): `c1-v35-42` p. 264 n. 1 "human study" → "human effort"; `c1-v43-51` ¶ 94 "a study of profiting" → "an eagerness to profit" (anchor moved after "eagerness"); both `tr-studium` notes reworded; the two Notes bullets updated | 2 text + 2 notes + 2 Notes bullets | ruling 80(c) |
| 4(i) | *testimonium perhibere* | **"give testimony" throughout:** `prol` p. 245 "are borne" → "are given"; `c1-v29-30` ¶ 61 "bore … bears" → "gave … gives", ¶ 62 "bears" → "gives", *perhibitio* "bearing" ×2 → "giving"; `c1-v31-34` ¶ 71 Quaest. IV "bore" → "gave" (second "bore", *tulit*, kept); `c1-v35-42` ¶ 72 "bore" → "gave", ¶ 83 "bore" → "gave" and "bearing" → "giving". Notes bullets of the three chunks updated | 7 sites (+ 3 *perhibitio* forms) in 7 text lines | ruling 81(a) |
| 4(ii) | *doctor* | `prooem` ¶ 4 "teacher" → "doctor" (and the `tr-doctrina` note's "of a teacher") | 2 | ruling 81(b) |
| 4(iii) | I Tim. 6:16 *habitat* | `c1-v3-5` ¶ 16 "inhabiteth" → "dwelleth in light inaccessible" (the Vulgate note keeps "inhabiteth") | 1 | ruling 81(c) |
| 4(iv) | Wis. 7:24 *munditiam* | **"purity" ratified** (*pudicitia* = 0 sites; Vol V ruling 6 reasoning) | 0 | ruling 81(d) |
| 5 | resolver docket | **NO text edits.** Classes A–G and the three new items recorded; a follow-up TOOL job, run after the gate and separately, dangerous classes first (see below) | 0 | ruling 82(a) |
| 6 | housekeeping | `c1-v15-18` `verses` `"14-18"` → `"15-18"` (frontmatter, breadcrumb, two Notes lines; 1:14b explained in Notes); `c1-v43-51` "Forty-five" → "Forty-six" (status line, Notes heading); Douay block ratified; index misses and gate-page-vs-close-page recorded | 6 | ruling 82(b)–(e) |

**Totals (git diff, 10 files in `vol6/`): 58 lines changed (58 insertions / 58 deletions), 63 individual replacements.** The sheet's estimate was 39 English/frontmatter lines + 2 note rewrites + ~5 doc lines; the difference is the Notes paragraphs and `transcription_status` clauses that described the replaced state and had to be kept true. No Latin text line changed.

### Resolver follow-up (item 5): recorded, not run

One tool job, after the gate. Classes in the order to run them: **A** a bare roman book numeral before `d.` restarts the book (`c1-v6-8` p. 250 n. 8; `c1-v15-18` p. 256 n. 3 incl. the one QA line); **B** a bare `pag. N` of a non-Bonaventure book inherits a Bonaventure volume (`prooem` p. 239 n. 1 ×2; `c1-v1-2` p. 246 n. 7); **C** *ibid.* binding across notes or to a bracketed verse, and a commentary siglum not blocking a scripture reading (`c1-v35-42` ¶ 77; `prol` p. 245 n. 2; ★ `prooem` p. 241 n. 3 `ibidem`; ★ `c1-v15-18` p. 254 n. 8 `Cfr. ibid. XXV. c. 10. n. 25`); **D** ordinal-word book numerals (*primae/secundae/tertii* …; ★ `prooem` p. 239 n. 1 `tertii Reg. 3, 12`); **E** lost self-references (a `Bonav.` siglum is self; `et N`; `q. a-b`; roman distinctio; Sentences Prooemium; named-work forms); **F** the work's own `n. N` form via the `paragraphs:` field (ruling 73); **G** scripture *ibid.* as in C. Rows H (no record by design), I (transcription, correct) and E′ (ambiguous by design) need nothing. The three ★ items were found at the gate and are in no chunk's Notes. The tool job is **next-up-optional**: it is not a precondition for Capitulum II.

---

## DEFECTS FOUND

1. **Documentation only (repaired):** `bon-ioan-c1-v43-51` claimed "forty-five entries" in its `transcription_status` and its Notes heading (and the START HERE block of `next-session-resume.md`, which this close rewrites). The chunk's own page-split map sums 6 + 12 + 12 + 15 + 1 = **46**, the file holds 46 numbered defs, and `check-vol5-apparatus.py` reports 46 La / 46 En. Repaired to "Forty-six" / "FORTY-SIX". The commit message of `581b626` is not amended. (The CLAUDE.md rule: per-note data beats the summary sentence.)

**No text defect.** Zero live flags, zero count mismatches, zero seam defects, zero style hits ours.

**NOTE (not a defect):** `c1-v24-28` p. 259 n. 15 prints `d. XXV.` and the English gives `d. 25`. The corpus is mixed here (about 86 Vol V–VI English halves keep the roman numerals against about 114 Latin roman sites), so this is a house-style inconsistency, not an error in this chunk. Recorded, no edit.

---

## CLOSE — suite re-run after the edits (2026-10-21), against the baseline

| check | result after the edits | baseline | difference |
|---|---|---|---|
| live flags | **vol6 81 chunks, none** | same | none |
| `check-vol5-apparatus.py --volume=vol6` | **81 chunks, 2,539 entries, all passed** (p. 269 PENDING n.2–13) | same | none |
| `check-vol5-census.py` | **vol5 167/167, vol6 81/81, rosters agree; 124 runovers (120 gutter / 4 page)** | same | none |
| `polish-style-scan.py` | **11 issues / 6 chunks / 2,200 scanned, ZERO ours** | same | none |
| `build-citations.py` | **29,110 records, QA 209; ours 374 records, 1 QA flag (c1-v15-18 p. 256 n. 3)**; `citations.tsv` and QA report unchanged in `git status` | same | none, as predicted: the edits are English-only |
| `build-index-json.py` | **1,739 cited / 10,643 backlinks** | same | none |
| `cd site && node scripts/build-content.mjs` | **2,199/2,199 translated** | same | none |

No difference from the baseline in any number. Title changes shift nothing numerically.

**Front advances to Capitulum II's first chunk** (opens at ~0.12 of p. 269 under `CAPITULUM II.`, no heading below; its title per ruling 79 is the divisio's first sentence after the lemma, *Postquam descripta est discipulorum vocatio, describitur hic facta per Verbum et de Verbo incarnato manifestatio* — raw, to be verified on the plate). **No push, no deploy.**
