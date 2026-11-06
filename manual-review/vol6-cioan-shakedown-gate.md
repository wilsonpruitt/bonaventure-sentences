# Vol VI — *Collationes in Evangelium S. Ioannis*, SHAKEDOWN GATE at p. 559 (printed pp. 535–559) — CLOSED

**STATUS: CLOSED 2026-11-06.** Docket ruled by Wilson in one sitting ("Approve all", 2026-11-06) → Vol VI rulings 124–135 in `manual-review/vol6-pilot-setup.md`. No defect in the transcription; the gate conformed c2–c4 to ruling 98's word order (the one large item, N1), applied the *lumen* verse test in c1, and corrected five `## Notes` records that misstated a ruling or a precedent. **No `**La.**` half changed; one `## Latin` line changed** (c1's Horace line takes the `> ` verse form, ruling 132 — a layout prefix, the words untouched).

Ruling 123 placed this gate at p. 559, the close of Capitulum IV. ⛔ **It carries NO deploy** (one default deploy for the work, at p. 634). Push stays separate and is Wilson's per action.

**Procedure (the *Ioannem* p. 268 precedent):** a read-only agent compiled the evidence sheet, `manual-review/vol6-cioan-shakedown-gate-evidence-sheet.md` (one section per item, exact edit lists, Appendix A = the N1 site list), and ran Passes 1–3 into `manual-review/vol6-cioan-shakedown-gate-passes.md` (all CLEAN; the baseline below). Both are kept as the evidence record and are not repeated here. Wilson ruled in one sitting; the edits, the suite re-run and Pass 4 then closed the gate.

**Scope: FOUR chunks, pp. 535–559 with no gap, 202 numbered apparatus entries, 6 `tr-` notes before the gate → 7 after.**

| chunk | division | pages | entries | Collationes | Annotationes |
|---|---|---|---|---|---|
| `bon-cioan-c1` | 1 | 535–545 | 80 | I–VII | 1–3 |
| `bon-cioan-c2` | 2 | 545–550 | 45 | VIII–X | 4–6 |
| `bon-cioan-c3` | 3 | 550–554 | 36 | XI–XIII | 7–11 |
| `bon-cioan-c4` | 4 | 554–559 | 41 | XIV–XIX | 12–17 |
| **total** | | **25 pp.** | **202** | | |

Every census is over the BUILT files and the RENDERED regions (`## Latin`, `## English`, `## Apparatus`), never over `raw/` or `## Notes`.

---

## PASS 1 — live flags: **CLEAN** (the two hits are the editors' printed `[?]`, now allowlisted)

Baseline: `check-live-flags.py vol6` → 181 chunks, **2 occurrences** (`bon-cioan-c2` p. 545 n. 6, La + En), both the editors' own printed `[?]` (S5, confirmed on the plate). After ruling 131's allowlist: **181 chunks, LIVE FLAGS none; "printed by the editors, not ours: 2"** on its own line.

## PASS 2 — mechanical suite: **CLEAN**

Detail in the passes file § PASS 2 (apparatus 181 / 5,813 · census vol6 181/181, 295 runovers · style 11 / 6 / 2,300, zero ours · `validate-chunk.py` 4/4 · citations 33,254, QA 211, ours 0 · La/En digit multisets 3 mismatches of 202, all ruling-89 brackets · parity La = En in all four).

## PASS 3 — boundary sweep: **CLEAN**

Every page 535–559 owned exactly once with a contiguous 1..N register (202); four seams read on the 450 dpi plates (pp. 545, 550, 554, 559/560); 13 unnumbered block heads = the 13 runover-ledger rows. Seam table: passes file § PASS 3.

## PASS 4 — plate cleanup: **DONE 2026-11-06**

**Deleted:** `raw/vision/vol6/p-533.png` … `p-559.png` (**27 plates, 54.8 MB**: the half-title leaves 533–534 and the whole scope 535–559) · **all 96 files in `/tmp/colcrop/`** (**177.7 MB**). **123 files, 232.5 MB freed** (decimal MB; 221.8 MiB). All gitignored, regenerable from `raw/doctorisseraphic06bona.pdf`.
**Kept:** `p-560.png` (Capitulum V opens at its head — the next chunk's first leaf, the *Ioannem* `p-269.png` precedent) and `p-604.png`, `p-615.png`, `p-632.png`, `p-634.png` (later leaves pulled at the pilot). `raw/vision/vol6/` is now 5 files, 9.6 MB.

---

## THE DOCKET — RULED 2026-11-06, "Approve all"

| # | item | ruling | lines applied | recorded |
|---|---|---|---|---|
| N1 | ordinal word order | **Ruling 98 fixes the order: "Book, the Nth chapter"**, never "the Nth chapter of Book"; "the Nth Psalm" kept | **251 sites on 80 English lines** (c2 78 / 30 · c3 82 / 22 · c4 91 / 28): 247 mechanical (scripted, Python), 4 by hand (c2 L211, c3 L139, c4 L215, L255). ⚠ **One more than Appendix A's 250:** c3 L199 *ad Colossenses primo* ("the first chapter to the Colossians") was missing from the list; conformed with the class. Notes: the four "Ordinals (ruling 98)" lines (c1's misdescribed its own correct body) | ruling 124 |
| S8 | *lumen* in quotations | **Verse test applied in c1:** Eph. 5:13 (¶ 2) and Tob. 5:12 (¶ 7) → Douay "light"; Isa. 60:1 and Ps. 4:7 keep "lumen" (the prose leans on them); c1's `tr-lumen` marker moved ¶ 5 → ¶ 2 (ruling 74, first site) and the note rewritten to name both exceptions; **c2 `tr-lumen` added** (p. 549 n. 1, Bede); c4's note's last sentence no longer overclaims | c1 2 English lines + the marker line (shared with ruling 134) + 1 note rewrite · c2 1 `**En.**` half + 1 new note · c4 1 note sentence · Notes c1 (2 lines), c2 (1) | ruling 125 |
| S1/S9 | Quaracchi slips | **PRINTED_SLIPS rows owed for p. 537 n. 6 (`Ps 75:2` → `Ps 75:3`) and p. 556 n. 1 (`Luc 16:10` → `Luc 16:19`), queued with ruling 113's docket, NOT run.** Horace "[so printed; the line is v. 343]" ratified. c4's bracket put into ruling 89's form: "[so printed; the passage is Luke 16:19 ff.]" | 1 `**En.**` half (c4) + c4 Notes | ruling 126 |
| S7 | Silius for Ovid (p. 551 n. 5) | **Recorded in c3's Notes only; no bracket** — an editorial attribution, not a misprint | 0 text · 1 Notes line | ruling 127 |
| S2 | resolver gap | **Queued as D7, not run:** `Hexa[eë]m\w*\.\s*(\(tom\. V\.\)\s*)?collat\.\s*N` (83 sites to add, 1 to refine) + the `hexaemeron` `chunk_pattern` `bon-hex-coll{coll}` → `bon-hex-c{coll}` in the same diff + the ruling-116 guard widened to `Hexa[eë]m` | 0 | ruling 128 |
| S3 | breadcrumb | **`Cap. 1` (Arabic) kept** | 0 | ruling 129 |
| S4 | *culpa* / *reatus* / *manere* | **Ratified as built;** c1's Notes corrected (*culpa* = Sap ruling 63, *reatus* = practice, not "ruling 20"; Luke 24:29 "Remain with us" disclosed) | 0 text · 1 Notes line | ruling 130 |
| S5 | editors' printed `[?]` | **Kept as printed;** `PRINTED_QUERIES` allowlist **implemented** in `tools/check-live-flags.py` (keyed chunk + apparatus label + context; exempt hits printed on their own line). Verified: vol6 2 → 0 live with `bon-cioan-c2` p. 545 n. 6 listed exempt ×2; whole corpus 241 → 239 + 2 exempt | 0 text · ~25 tool lines | ruling 131 |
| S6 | verse in a note / body | ` / ` in the apparatus ratified (ruling 91); **c1's Horace line set `> `** in both languages, as c3's Ovid and Sap c11's Boethius | 2 (1 `## Latin`, 1 `## English`) | ruling 132 |
| S10–S12 | Coll. XVI address; *vacare*; guillemets | Coll. XVI `(Cap. VI, 27.)` no convention (`bon-cioan-c6` to record the Annot. 22 pairing); `tr-vacare` ratified; absent `»` record-only | 0 text · c4 Notes line | ruling 133 |
| N0 | bare ordinal | c1 ¶ 5 "and the sixtieth" → "and the sixtieth chapter" | 1 (shared with ruling 125's marker move) | ruling 134 |
| — | close | gate CLOSED after the suite re-run; Pass 4 as above | — | ruling 135 |

**Totals (diff against the pre-gate files):** **English body lines changed 84** (c1 4 · c2 30 · c3 22 · c4 28) · **`**En.**` halves 2** (c2 p. 549 n. 1, c4 p. 556 n. 1) + **2 `tr-` notes rewritten** (c1, c4) + **1 `tr-` note added** (c2) + **1 `tr-` marker moved** (c1 ¶ 5 → ¶ 2) · **`**La.**` halves 0** · **`## Latin` lines 1** (c1 Horace `> `, ruling 132) · frontmatter 0 · `## Notes`: 9 lines corrected + one dated GATE line appended per chunk. `tr-` notes in scope **6 → 7** (`tr-lumen` now c1, c2, c3, c4: every chunk with a live *lumen*).

---

## DEFECTS FOUND

**No transcription defect.** Five documentation records were wrong and are corrected (c1 Notes: the *lumen* "as applied in *Ioannem*" claim, refuted; the ruling-20 citation for *culpa* / *reatus*; the undisclosed Luke 24:29; the Ordinals line misdescribing its own body · c2 Notes: "no `tr-lumen`", contrary to ruling 92). c4's `tr-lumen` overclaim and c2–c4's ordinal order are conformances to rulings, not transcription errors.

**NOTE:** the gate's own site list (Appendix A) missed one N1 site (c3 L199, the second locus of a coordinated pair whose first was already in ruling 98's order). Found by the post-run grep, which is why the grep is the verification and not the list.

---

## CLOSE — suite re-run after the edits (2026-11-06), against the baseline

| check | result after the edits | baseline (passes 1–3) | difference |
|---|---|---|---|
| `check-live-flags.py vol6` | **181 chunks, LIVE FLAGS none; 2 printed-by-editors exempt** (c2 p. 545 n. 6 La/En) | 181 chunks, 2 occurrences | −2 live, by the ruling-131 allowlist; whole corpus 241 → 239 live |
| `check-vol5-apparatus.py --volume=vol6` | **181 chunks, 5,813 entries, all checks passed** | same | none |
| `check-vol5-census.py` | **vol5 167/167, vol6 181/181, rosters agree; vol6 295 runovers (272 gutter / 23 page)** | same | none |
| `polish-style-scan.py` | **11 issues / 6 chunks / 2,300 scanned, ZERO ours** | same | none |
| `validate-chunk.py` (the 4) | **4 checked, 0 failed** | same | none |
| `build-citations.py` (default paths) | **2,300 chunks → 33,254 records, QA 211**, anaphora unresolved 285, printed slips 6 / 0 stale; `index/citations.tsv` and `manual-review/citation-qa-report.md` **byte-identical** (unchanged in `git status`) | same | none, as predicted: the edits are English-only and no `**La.**` half changed |
| `build-content.mjs` → `build-index-json.py` → `build-content.mjs` | **2,299 / 2,299 translated** both times; index 77 books / 19,479 scripture citations, crossref 1,819 cited / 11,166 backlinks (generated files, gitignored: nothing to commit) | not run at passes 1–3 | — (ledger byte-identical, so nothing could move) |

**Front advances to `bon-cioan-c5`** (Capitulum V *Post haec erat dies festus*, index pp. 560–564, Coll. XX–XXV + Annot. 18–21), which inherits nothing (p. 559 is a leaf edge). **No push, no deploy.**
