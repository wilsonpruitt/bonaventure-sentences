# Vol VII — *Commentarius in Evangelium S. Lucae*, p. 188 GATE (printed pp. 88–188; Cap. IV–VII complete) — CLOSED

**STATUS: CLOSED 2026-11-15.** Docket ruled by Wilson in one sitting ("aprove all", 2026-11-15: every ⭐ recommendation of the evidence sheet, its recommendations against the builders and its "Found by the sheet" fixes included) → Vol VII rulings 41–62 in `manual-review/vol7-pilot-setup.md` § *LUCAM* p. 188 GATE. **18 English lines changed across 9 chunks (F1–F9), plus Notes in 10 chunks; 1 manifest cell (doc); no line in any `## Latin` body or `**La.**` half changed.** Ruling 32's table gains six rows; ruling 35 gains a clarifying sentence (ruling 54). One tool job queued (ruling 62, T-1..T-9). The live `[?]` (item 56) stays open. **No push, no deploy:** the p. 88 Advent deploy (ruling 38's preconditions) and the push remain Wilson's separate OKs.

Ruling 14 placed this gate at p. 188 (close of c. 7). This close makes no recommendation about the deploy.

**Procedure (the p. 88 gate's):** a read-only agent compiled the evidence sheet, `manual-review/vol7-lucam-p188-gate-evidence-sheet.md` (censuses over the rendered region, the decisive sentence, alternatives with costs, a ⭐ per item, and twelve "found by the sheet" items F1–F12); a second read-only agent ran Passes 1–3 into `manual-review/vol7-lucam-p188-gate-passes-draft.md`; manifest stage 3 (`f03a544`) was drawn alongside. Both documents are kept as the evidence record and are summarised here, not repeated. Wilson ruled in one sitting; the edits, the re-run and Pass 4 then closed the gate.

**Scope: the 19 chunks of pp. 88–188** (`bon-luc-c4-v1-13` → `bon-luc-c7-v36-50`; IV 5 · V 4 · VI 6 · VII 4), **1,147 numbered apparatus entries, 17 `tr-` notes**; censuses over all 41 *Lucam* chunks (pp. 3–188, 2,015 entries, 34 `tr-` notes) where a register question needed them. **p. 188 nn. 6–8 belong to Cap. VIII** (`bon-luc-c8-v1-10`, unbuilt; checker `PENDING n.6,7,8`).

---

## PASS 1 — live flags: **AS EXPECTED**

`check-live-flags.py vol7` → 41 chunks, **2 occurrences = one flag, La + En: `bon-luc-c5-v12-16` p. 122 n. 11** (*A C G E [?]*, docket item 56). Same after the edits. Stays open (ruling 59).

## PASS 2 — mechanical suite: **CLEAN** (figures below, § CLOSE)

## PASS 3 — read-through / consistency: **CLEAN**

La/En parity in every ¶ of all 41 chunks (anchors 2,015 = 2,015; page markers; ¶ numbers; guillemets ¶ by ¶; `(Vers.` tags); 17 interval `tr-` notes all paired; no page gap or overlap pp. 88–188; hand-offs agree on all 20 shared pages. Two observations, both non-defects and both recorded: (i) ***impius*** in Bonaventure's prose follows the nearest Douay word ("ungodly" `c6-v27-31` ¶ 73, "wicked" `c6-v39-49` ¶ 96; *impietas* "impiety"). The sheet's item 32 makes the call: the *pietas* rule binds the positive word only; recorded under ruling 51, no edit. (ii) **`c3-v21-22`** (old ground) carries page markers 81–84 against `printed_pages` 81–85, because p. 84 n. 14 runs onto p. 85 (a census page-crossing); as at the p. 88 gate.

## PASS 4 — plate cleanup: **NOTHING TO DELETE**

This close read no plate and made no crop: no file was written to `/tmp/colcrop/` or `raw/vision/` by it. The raw/vision plates (pp. 88–188, kept by the p. 88 gate for this interval, and the stage-3 extractions) are left as they are, per the brief. Whether to delete the pp. 89–187 plates now that their interval is closed (p. 188 is shared with Cap. VIII) is Wilson's call; not done here.

---

## THE DOCKET — RULED 2026-11-15, "aprove all"

| # | item(s) | ruling | lines applied | recorded |
|---|---|---|---|---|
| A | 1–5 boundaries, manifest, structure | Ratified; `c4-v1-13` manifest `headings` cell corrected (the 89L t3) | 1 manifest cell | 41 |
| B | 6–8 Corrigenda | Ratified as applied | 0 | 42 |
| C | 9–24 ruling-20 adjustments | Ratified as built | 0 | 43 |
| 25 + F1 | *suasio* / *persuasio*; *authenticatio* / *auctorizatio* | The work's pairs; `c4-v1-13` ¶¶ 15, 16 "persuading" | 2 | 44 |
| 26 | Prov. 1:20; Ps. 64:12 | Ratified; *benignitas* "kindness" into the table, into quotations | 0 | 45 |
| 27 + F10 | Amos 5:10, Prov. 9:8, John 8:46 | Ratified (ruling 32's preface); Amos 5:10 split recorded | 0 + Notes | 46 |
| 28 | *potentia* / *virtus* / *potestas* | "power" confirmed; two tie-breaks written | 0 | 47 |
| 29 | *solitudo* | Split ratified; Osee 2:14 recorded as a second split | 0 | 48 |
| 30, 38 | `tr-praeceptor`; *magister*; Wis. 8:16 | Ratified; forward sentence for the first *Praeceptor* + *magister* paragraph | 0 | 49 |
| 31 + F11 | `tr-lumen` reach | Ratified; scope sentence; Isa. 60:1 split recorded | 0 + Notes | 50 |
| 32 + F4–F6 | human *pietas* in quotations | Conformed to "piety" / "pious"; *impius* recorded | 3 | 51 |
| 33 + F2, F3 | Douay kept against a house word | Four ratified; `c6-v27-31` ¶ 65 and `c7-v36-50` ¶ 76 Cant. 8:6 → "dilection"; *caritas* into the table | 2 | 52 |
| 34 + F7 | *curare* / *sanare* | Work-level split; ruling sentence; `c7-v1-16` *curatio* → "cure" | 6 | 53 |
| 39 | *puer*; Gen. 15:6 *Abraham* | Ratified; ruling 35 clarified | 0 + ruling sentence | 54 |
| 42 + F9 | *credulitas* | "belief" work-wide; `c1-v26-38` conformed | 3 | 55 |
| F8 | *redarguere* | "convict" into the table; `c7-v24-35` conformed | 2 | 56 |
| 35, 36, 37, 40, 41 | Jude of James; `tr-vacare` at a vice, *exsultatio*; lending vocabulary; passive *evangelizantur*; "delightful", "piped" | Ratified as built; *otium* "leisure" into the table | 0 | 57 |
| E | 43–51 citation slips | Ratified as transcribed (r.57 class) | 0 | 58 |
| F | 52–55 `[so printed]`; 56 the live `[?]` | 52–55 ratified; **56 stays open** | 0 | 59 |
| G, H | 57–61 readings as printed; 62–64 collection change | Ratified; banked | 0 | 60 |
| F10–F12 | records and docket errors | Recorded (below) | 0 | 61 |
| T | T-1..T-9 | One tool job, QUEUED, NOT RUN | 0 | 62 |

### Lines changed (git diff)

| file | English / En. lines | Notes lines | Latin / La. lines |
|---|---|---|---|
| `vol7/bon-luc-c4-v1-13.md` | 2 (¶ 15, ¶ 16: *suasio* "persuasion" → "persuading") | 1 gate paragraph | **0** |
| `vol7/bon-luc-c4-v38-44.md` | 1 (p. 110 n. 8 **En.**: *pios* "the godly" → "the pious") | 1 gate paragraph | **0** |
| `vol7/bon-luc-c5-v17-26.md` | 1 (¶ 44, Ecclus. 44:10 "whose godly deeds" → "whose pieties") | 1 amended in place (Ruling-20 list, struck wording kept) + 1 gate paragraph | **0** |
| `vol7/bon-luc-c6-v12-19.md` | 1 (¶ 40, II Tim. 3:5 "godliness" → "piety") | 1 amended in place + 1 gate paragraph (F11 recorded) | **0** |
| `vol7/bon-luc-c6-v27-31.md` | 1 (¶ 65: Eph. 5:2 "Walk in dilection", Rom. 12:9 "dilection without dissimulation") | 1 amended in place + 1 gate paragraph | **0** |
| `vol7/bon-luc-c7-v1-16.md` | 6 (¶¶ 1, 9, 16, 17, 18, 20: *curatio* "healing" → "cure" ×8, *curatus* "healed" → "cured" ×1) | 1 amended in place + 1 gate paragraph | **0** |
| `vol7/bon-luc-c7-v24-35.md` | 2 (¶ 47, ¶ 57: *redarguere* "reprove" → "convict", 3 sites) | 1 gate paragraph (F12d corrected there) | **0** |
| `vol7/bon-luc-c7-v36-50.md` | 1 (¶ 76, Cant. 8:6 "Love" → "Dilection is strong as death") | 1 gate paragraph | **0** |
| `vol7/bon-luc-c1-v26-38.md` | 3 (¶ 67 ×2, ¶ 69: *credulitas* "credulity" → "belief") | 1 amended in place + 1 gate paragraph | **0** |
| `vol7/bon-luc-c4-v22-30.md` | 0 | 1 gate paragraph (F10 recorded) | **0** |
| `manual-review/lucam-chunk-manifest.tsv` | — | 1 (`c4-v1-13` `headings` → `capitulum@88;t1@88L;t2@88R (italic);t3@89L;t4@89L`) | — |

**18 English lines across 9 chunks** (the sheet estimated 17). Each site was read with its Latin before the edit, and the edits were made by exact-match replacement, one asserted occurrence per line. Verified after the edits: every changed chunk line is in `## English`, an apparatus **En.** half, or `## Notes`.

**Where the files differed from the sheet (no ruling affected):**
- **F7:** the sheet counts *curatio* ×9 + *curatus* ×1 = 10 sites; the rendered region of `c7-v1-16` holds **8 *curatio* + 1 *curatus* = 9**, all changed, on the six lines the sheet named. The *sanatio* / *sanare* sites keep "healing" / "heal" (¶ 1 ×2, ¶ 16 Matt. 8:13, the 7:7 lemma).
- **F9:** the sheet said 2 lines; ¶ 67 stands on two lines of the file, so the three sites take **3 lines**.

### Docket errors the sheet found (F12; no text effect)

(a) Item 4's sentence-title list omitted three (`c4-v38-44` ¶ 79, `c5-v12-16` ¶ 24, `c5-v17-26` ¶ 40); the true count is nine. (b) Item 36's *exsultatio* is ¶ 60 (Isa. 65:14), not ¶ 61. (c) The resume's START block called the wrong *ibid.* "tool item T-11"; the list numbers it **T-4** (fixed in the new resume block). (d) `c7-v24-35`'s Notes licensed Ecclus. 3:1's "love" by ruling 12's quotation clause, which governs *miseratio* only; the licence is ruling 32's preface (corrected in that chunk's Notes). Also stale in the resume and corrected there: **the ruling-37 tool job has already run** (`187bc15`, "ruling 37 tool fixes T1-T13"), and **manifest stage 3 is drawn** (`f03a544`). Also recorded from the sheet: the house `DRC.json` reads Luke 7:15 "he **gave** him" (drbo.org: "delivered"), so docket item 20's "7:15" is either an adjustment or none; the built "he gave him" is right either way. `DRC.json` is not a perfect Challoner (4:1 "was led the by the spirit").

### Manifest stage 3

**Drawn at `f03a544`** (Cap. VIII–XI v. 13, pp. 188–288, 22 rows; VIII 7 · IX 8 · X 5 · XI 2). **Its 8 `low` rows (four decisions: `c8-v26-33` / `c8-v34-39`; `c8-v40-48` / `c8-v49-56`; `c9-v46-56` / `c9-v57-62`; `c10-v1-3` / `c10-v4-16`) are settled at build time by ruling 39's procedure:** each builder reads its boundary plates and promotes its own row's `confidence` cell, or STOPS and reports. The p. 288 gate falls at ¶ 35 / ¶ 36 on 288L.

### Tool job (ruling 62): recorded, NOT run

T-1..T-9 as one bounded job after the gate, order and scope in the sheet § T and ruling 62 (T-4 first: the Bernard *ibid.* at `c7-v36-50` p. 183 n. 6 bound to a parenthetical crossref). `tools/build-citations.py` only, then `build-citations.py` → `build-index-json.py`; no chunk file. Baseline below (QA 212, anaphora unresolved 370).

### Deploy

Nothing deployed, nothing pushed. Ruling 38's preconditions for the p. 88 deploy are unchanged (D1 `build-authorities.py` still not run for vol7; D5/D7 the local build and the p. 16 n. 8 "tr." look still owed). A deploy now would carry this gate's edits and every unpushed commit. Push and deploy are each Wilson's own OK.

---

## CLOSE — suite re-run after the edits (2026-11-15), against the baseline

| check | after the edits | baseline (passes draft) | difference |
|---|---|---|---|
| live flags | **vol7 41 chunks, 2 occurrences = 1 flag** (`c5-v12-16` p. 122 n. 11) | same | none |
| `check-vol5-apparatus.py --volume=vol7` | **41 chunks, 2,015 entries, all checks passed** (p. 188 PENDING n.6–8) | same | none |
| `check-vol5-census.py` | **vol7 41/41 on disk and in ledger; 119 runovers (99 gutter / 20 page)** | same | none |
| `polish-style-scan.py` | **11 issues / 6 chunks / 2,359 scanned, ZERO in vol7** | same | none |
| `validate-chunk.py` (the 10 touched chunks) | **10 × "1 checked, 0 failed"** | 41 OK | — |
| `build-citations.py` | **40,415 records; QA 212**; anaphora 2,308 + 86, **unresolved 370**; coordinate ibid. 473 (370 / 103); printed slips 23, 0 stale; `index/citations.tsv` and the QA report **byte-identical** (`git status` clean under `index/`) | same | none, as predicted: the ledger is built from the Latin halves, and the edits are English / Notes only |
| `build-index-json.py` | **crossref 1,837 cited / 11,111 backlinks**; goto 2,358; authorities 89 / 17,302 (existing ledger) | same | none |
| `cd site && node scripts/build-content.mjs` | **19 books, 2,358 / 2,358 translated** | same | none |

**Front: `bon-luc-c8-v1-10`** (manifest stage-3 row 1, the Cap. VIII opening; p. 188 nn. 6–8 are its). **The interval pp. 188–288 needs Wilson's go and a burn OK before any builder is dispatched.** No push, no deploy.
