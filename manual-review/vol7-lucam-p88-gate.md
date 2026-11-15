# Vol VII — *Commentarius in Evangelium S. Lucae*, p. 88 GATE (printed pp. 3–88; Pars I closes, Cap. I–III complete) — CLOSED

**STATUS: CLOSED 2026-11-14.** Docket ruled by Wilson in one sitting ("approve all", 2026-11-14) → Vol VII rulings 27–40 in `manual-review/vol7-pilot-setup.md` § *LUCAM* p. 88 GATE. **2 English lines changed across two chunks (`c1-v18-25` ¶ 38, `c3-v23-38` ¶ 63), plus Notes; 1 manifest line (doc); no line in any `## Latin` body or `**La.**` half changed.** Ruling 18 amended (ruling 29, struck wording kept visible); ruling 12 gains the *praeconium* and `tr-pietas` sentences (rulings 30, 31). One tool job queued (ruling 37). Deploy preconditions recorded (ruling 38); **no deploy run, nothing pushed.**

Ruling 14 placed this gate at p. 88. **The p. 88 deploy (Luke 1–3 live for Advent) is asked of Wilson separately by the coordinator, as its own OK.** This close makes no recommendation for or against it.

**Procedure (the p. 27 gate's):** a read-only agent compiled the evidence sheet, `manual-review/vol7-lucam-p88-gate-evidence-sheet.md` (censuses over the rendered region, the decisive sentence, alternatives with costs, a ⭐ recommendation per item); a second read-only agent ran Passes 1–3 into `manual-review/vol7-lucam-p88-gate-passes-draft.md`; manifest stage 2 (`caae173`) was drawn alongside. Both documents are kept as the evidence record and are summarised here, not repeated. Wilson ruled in one sitting; the edits, the re-run and Pass 4 then closed the gate.

**Scope: 22 chunks, pp. 3–88 with no gap, 868 numbered apparatus entries, 17 `tr-` notes.** 2 front matter (`bon-luc-prooem`, `bon-luc-prol`) + `c1` ×8 + `c2` ×7 + `c3` ×5. The p. 27 gate (rulings 17–26) had already ruled on the first six; the new ground is the 16 chunks from `bon-luc-c1-v39-45` on. Per-chunk entry counts: passes draft, Scope line. **p. 88 nn. 10–12 belong to Cap. IV** (`bon-luc-c4-v1-13`, unbuilt; checker `PENDING n.10,11,12`).

---

## PASS 1 — live flags: **CLEAN**

`check-live-flags.py vol7` → **22 vol7 chunks scanned, no live `[?]`** (denominator 22 = all of vol7). Same after the edits.

## PASS 2 — mechanical suite: **CLEAN**

- `check-vol5-apparatus.py --volume=vol7`: **22 chunks, 868 entries, La = En in every chunk, all checks passed**; 86 known page totals (pp. 3–88); p. 88 `PENDING n.10,11,12`.
- `check-vol5-census.py`: **vol7 22/22, rosters agree; 56 runovers (49 gutter / 7 page)**.
- `polish-style-scan.py`: **11 issues / 6 chunks / 2,340 scanned, all in Vols III–V; ZERO ours.**
- `build-citations.py`: **37,675 records, QA 213** (211 at the p. 27 gate). vol7's share: **2,053 records; 2 of the 213 QA flags** — p. 54 n. 10 *d. 8. p. II. dub. 2.* (dangling; a Quaracchi slip, plate-verified, T8) and `c1-v46-56` ¶ 97/98 "Esther. 98" (a parser artefact, T1). ⚠ **The second is not recorded in `c1-v46-56`'s Notes** (ledger-vs-Notes discrepancy only, no text defect; recorded here and in the tool job).
- Page markers identical La/En in all 22; anchor sequences identical, unique, ascending, anchor set = def set (868 = 868); `tr-` anchors English-only, as designed.
- La/En digit multiset per entry: **7 mismatches of 868, all false positives** (passes draft lists them).

## PASS 3 — boundary sweep: **CLEAN**

Every page 3–88 owned exactly once with a contiguous 1..N register (checker + an independent per-page count over the `[^pN-n]` defs; `KNOWN_TOTALS_VOL7` matches). 17 seams read on the 300 dpi plates (pp. 27, 30, 34, 38, 43, 48, 51, 54, 58, 62, 65, 69, 75, 78, 81, 85, 88): no splice, drop or duplication; every note assigned by anchor. Footer spot-checks on one or more full pages of each of the 16 new chunks found no difference in any digit, locus or siglum. Seam table: passes draft § PASS 3.

## PASS 4 — plate cleanup: **DONE 2026-11-14**

**Deleted from `raw/vision/vol7/`:** `p-027.png` … `p-087.png` (61 plates, 227 MB: every leaf of the p. 88 interval except p. 88 itself, including the stage-1 boundary plates the p. 27 gate kept for this interval's builders). **Deleted from `/tmp/colcrop/`:** the 394 vol7 column bands for pp. 27–87 (`vol7-p027-*` … `vol7-p087-*`; pages present were 27–65 and 69–87), 415 MB.
**Kept in `raw/vision/vol7/` (110 plates):** `p-088.png` and **every plate of pp. 88–188** (101 plates: p. 88 is shared with Cap. IV, nn. 10–12; manifest stage 2 extracted pp. 89–188 for the Cap. IV–VII builders; `p-112` and `p-128`, kept as scouting plates by the p. 27 gate, fall inside this range) · `p-252` (scouting plate, kept by the p. 27 gate) · `p-604 … 607, 652, 655, 657` (work close and Appendix scouting) · `p-858` (the Corrigenda leaf). **Kept in `/tmp/colcrop/`:** the 8 `vol7-p088-*` bands; the 36 vol6 bands (pp. 220, 252, 447, 501, 551, 573: the ruling-9 job's, left for Wilson, as at the p. 27 gate); and 18 loose files not in the band naming pattern (`g63*.png`, `z-78-*`, `z-79-*`, `z-81-*`, `z65_0.png`), whose maker is not known, so they were left alone. Nothing in `raw/` other than extracted plates was touched.

---

## THE DOCKET — RULED 2026-11-14, "approve all"

| # | item | ruling | lines applied | recorded |
|---|---|---|---|---|
| 1 | the conspicuous ruling-20 Douay departures (Luke 2:32 "A lumen", 2:25 "God-fearing", Isa. 52:7, the *complacere* triad, Prov. 31:28) | **Ratified as built; no canticle exception** | 0 | ruling 27 |
| 2 | consistency pairs (2:19 / 2:51; *puerum* / *pueri*; Col. 1:13) | **All three splits kept; `c3-v23-38` ¶ 63 drops the Douay's "his"** (Quaracchi prints no *suae*) | 1 English + Notes | ruling 28 |
| 3 | ruling-18 scope: *evangelizare* in the OT; *annuntiare* verses | **Ruling 18's clause AMENDED** to "where the Douay itself says 'bring / preach good tidings' (Luke 1:19, 2:10; Ps. 67:12, Isa. 40:9, Nah. 1:15)"; Isa. 40:9 as built; Isa. 52:7 / 61:1 "announce" ratified | 0 + ruling sentence | ruling 29 |
| 4 | *praeconium* → "proclamation" | **Ratified; written into ruling 12:** "proclaim / proclamation" belongs to *praeconium* alone; *praeco* "herald" | 0 + ruling sentence | ruling 30 |
| 5 | `tr-pietas` outside cc. 15–16 | **Work-wide at the first God's-*pietas* site of any chunk**; p. 381 still reviews the rule | 0 + ruling sentence | ruling 31 |
| 6 | new house renderings, batch | **Ratified as one table** (Latin → English, in ruling 32); **`c1-v18-25` ¶ 38 "we are taught" → "we are schooled"** | 1 English + Notes | ruling 32 |
| 7 | `title_la`: sentence titles and ruling-22 applications | **All ratified; the sentence title is the precedent for heading-less spans; the `c2-v21-24` manifest cell corrected to the 54R t4** | 0 + 1 manifest line | ruling 33 |
| 8 | the two `confidence` cell edits (G50) | **Ratified as ruling 26 carried out; standing rule: a builder edits only its own row's `confidence` cell, and only when a ruling names it** | 0 | ruling 34 |
| 9 | genealogy names (G40) | **The work's names policy:** English in the Douay's spelling, Latin as printed, a name cited as a word stays Latin italic | 0 | ruling 35 |
| 10 | records, misprints, banked evidence (G38–G39, G41–G49) | **Ratified as recorded** | 0 | ruling 36 |
| 11 | tool fix job (T1–T13 + inbound forms) | **One bounded job, QUEUED, NOT RUN** (scope below) | 0 | ruling 37 |
| 12 | p. 88 deploy preconditions | **Recorded (below); no recommendation; asked separately** | — | ruling 38 |
| 13 | the `low` rows of manifest stage 2 (docket: "five"; the TSV holds six rows, four decisions) | **Accepted as drawn, alternatives recorded; each builder promotes its own row on the plate or STOPS** | 0 | ruling 39 |
| 14 | `bon-luc-c6-v1-11`'s `title_la` | **A sentence title (the `c2-v25-35` precedent), not "Capitulum VI."** (the manifest cell already has it) | 0 | ruling 40 |

### Lines changed (git diff)

| file | English lines | Notes / doc lines | Latin lines |
|---|---|---|---|
| `vol7/bon-luc-c3-v23-38.md` | 1 (¶ 63, Col. 1:13 "the Son of his love" → "the Son of love") | 2 amended in place (the ruling-20 list and the FOR WILSON item 3) + 1 gate paragraph | **0** |
| `vol7/bon-luc-c1-v18-25.md` | 1 (¶ 38, *erudimur* "we are taught" → "we are schooled") | 1 gate paragraph | **0** |
| `manual-review/lucam-chunk-manifest.tsv` | — | 1 (`c2-v21-24` `title_la` → *Qualiter factus sit sub lege sacramentali.*, `title_la_source` → `rubric-t4 p.54R`) | — |

Each site was read with its Latin before the edit, and each was as the sheet described: ¶ 63's Latin reads *transtulit nos in regnum filii dilectionis* (no *suae*); ¶ 38's reads *Sed* spiritualiter *erudimur*, and "taught" stood nowhere else in that chunk. Verified after the edits: every changed chunk line is in `## English` or `## Notes`. **The sheet listed no other Notes correction**; nothing found not as described.

### Tool job (ruling 37): recorded, NOT run — the next queued job

One bounded job (Sonnet-shaped), report → fix → report with a before/after table per site, touching `tools/build-citations.py` only (plus a site table), then `build-citations.py` → `build-index-json.py`. No chunk file, no `tools/authorities.json`. Baseline QA 213.

| # | site(s) | fix |
|---|---|---|
| T1 | `c1-v46-56` ¶ 97/98 "Esth. 98" | extend the ~L362 guard past the point-verse case (QA −1) |
| T3, T8 | p. 38 n. 7 *supra pag. 1, nota 5* (`forward` forever); p. 54 n. 10 *d. 8. p. II. dub. 2.* (`dangling`) | file under the r.57 "printed slips" class (QA −1) |
| T4 | p. 44 n. 7 *tom. VI. pag. 91, nota 3* → `bon-eccl-c11-v1-10` (wrong) | unresolvable-with-reason |
| T6 | 11 page+note self-citations on a shared page filed `page-multi` (p. 50 nn. 2, 3; p. 52 n. 10; p. 58 n. 1; p. 64 n. 5; p. 69 n. 4; p. 71 n. 6; p. 79 n. 3; p. 82 n. 12; p. 83 n. 3; p. 84 n. 6) | ruling 24's break-by-note fix for every `pag. N, nota M` |
| T7 | Bonaventure's own *Comment. in Eccle./Ioan.* inbound to Vol VI (p. 50 n. 2; p. 64 n. 10; p. 68 n. 6; p. 72 n. 4; p. 82 n. 5); *S. Bonav., IV. Sent.* (p. 82 n. 5, p. 83 n. 9) | let `S. Bonav.` through the author guard for the work's own author |
| T9 | p. 55 n. 8 *Breviloq. … (pag. 203, in nota 8.)* → `tom7:p203` | resolve in Vol V → `bon-brev-prol-s2` |
| T10 | cross-note *ibid.* / *loc. cit.* (p. 64 n. 6; p. 69 nn. 4, 9; p. 73 n. 9; p. 74 n. 1; p. 77 n. 10; p. 79 n. 3) | stop the anaphor pass at a note boundary |
| T11 | *Ecclesiastae N* body ordinals (`c2-v40-52` ¶¶ 107, 109; `c3-v1-9` ¶ 11; `c3-v10-14` ¶ 29); ¶ 93 *Deuteronomii, duodecimo*; p. 65 n. 12 *Ver. 14.* | add the book and the comma form to the body-ordinal scanner |
| T13 | roman distinctio (p. 69 n. 4 *III. Sent. d. XIII*; p. 85 n. 9 *II. Sent. lit. Magistri, d. XXIV. c. 7. seqq.*) | accept roman `d.` |
| T12 + IV-d21 | the two own-commentary *Exposit.* inbounds | **explicit two-row site table, NOT a wider `LUC_RE`** (15 Ambrose/Bede *Exposit. in Luc.* sites would otherwise be exposed) |

The site table:

| source | note | printed form | target | resolution |
|---|---|---|---|---|
| `bon-sent-IV-d21-p1-a1-q2` | n. 8 | *S. Bonav. Exposit. in Luc. 18, 13.* | `lucam:18:13` | `forward` (unbuilt) |
| `bon-ioan-c3-v13-16` | p. 283 n. 2 | *interpres noster Exposit. in cap. 3, 21. S. Lucae* (Bonelli) | `bon-luc-c3-v21-22` | `chunk`; lands on the Vat. addition Quaracchi moved to the apparatus (p. 83 n. 3), not on the body; the reciprocal p. 83 n. 3 → p. 283 n. 2 resolves under T6 |

**Not in the job:** T5 (in-work *c. N. n. M* / *supra n. N* / *infra* + ordinal; ~25 sites) stays deferred with the *Ioannem*'s class (ruling 24 / 82(a)); the job only counts it. **T2 closes** (never recurred across 15 chunks).

### Deploy preconditions (ruling 38): recorded; the coordinator asks Wilson separately

| # | precondition | state at this close |
|---|---|---|
| D1 | index tools in order before any site build: `build-citations.py` → **`build-authorities.py`** → `build-index-json.py` → `build-content.mjs` (and `build-index-json.py` + `build-content.mjs` again before the vercel build) | ⛔ **NOT MET:** `index/authorities.tsv` holds **zero** `bon-luc-*` records (last built 2026-11-07); `build-authorities.py` was not run at this close (the suite did not need it) |
| D2 | the citation → site path is current | met: `build-index-json.py` re-run at this close (1,852 cited / 11,367 backlinks); re-run it after the tool job if that lands first |
| D3 | `TOMES[7]`, `WORKS.lucam`, `VOL_DIRS` | met in code (ruling 25) |
| D4 | breadcrumb `Cap. N, Vers. a-b`; 22 chunks `hasTranslation` | met in data |
| D5 | the reader renders `/lucam`, `/tome/7`, unit pages | ⛔ **NOT YET SEEN:** no site build since vol7 began (`site/out` dated 2026-11-07, no `out/lucam`) |
| D6 | "Cite this" / tome label | met in data; `npm run build` refreshes the stale progress counts |
| D7 | ruling 23's owed look: `bon-luc-c1-v5-17` p. 16 n. 8, click "tr." | **owed** |
| D8 | p. 88 shows nine notes (nn. 10–12 are Cap. IV's, pending) | by design, not a defect |
| D9 | what the deploy carries | every unpushed commit (`git log --oneline origin/master..HEAD`), incl. `b804dec` (the Vol VI corrigenda, live Vol VI text) and the lucam citation class: **a "Luke deploy" is not Luke-only.** Push and deploy each Wilson's own OK; one deploy per OK, checked with `npx vercel ls` / `inspect`, never re-run |

**The short list, if Wilson says go:** (1) `build-authorities.py`, then `build-index-json.py`; (2) local `npm run build` and preview (`/tome/7`, `/lucam`, one pericope, p. 16 n. 8 "tr."); (3) push and deploy, each with its own OK.

---

## DEFECTS FOUND

**No text defect in the mechanical sense.** Zero live flags, zero count mismatches, zero seam defects, zero style hits ours. The two English edits are ruled conformances (ruling 28: Quaracchi's wording; ruling 32: the *erudire* family). One documentation error corrected (the `c2-v21-24` manifest cell). One ledger-vs-Notes gap recorded (the unrecorded "Esther. 98" QA artefact in `c1-v46-56`; T1).

---

## CLOSE — suite re-run after the edits (2026-11-14), against the baseline

| check | result after the edits | baseline (passes draft) | difference |
|---|---|---|---|
| live flags | **vol7 22 chunks, none** | same | none |
| `check-vol5-apparatus.py --volume=vol7` | **22 chunks, 868 entries, all passed** (p. 88 PENDING n.10–12) | same | none |
| `check-vol5-census.py` | **vol7 22/22 on disk and in ledger, rosters agree; 56 runovers (49 gutter / 7 page)** | same | none |
| `polish-style-scan.py` | **11 issues / 6 chunks / 2,340 scanned, ZERO ours** | same | none |
| `validate-chunk.py` (2 touched chunks) | **2 checked, 0 failed** | — | — |
| `build-citations.py` | **2,340 chunks → 37,675 records; QA 213**; anaphora unresolved 338; `index/citations.tsv` and the QA report **byte-identical** (`git status` clean under `index/`) | same | none, as predicted: the ledger is built from the Latin halves and the edits are English / Notes only |
| `cd site && node scripts/build-content.mjs` | **2,339/2,339 translated, 19 books** | 2,339 | none |
| `build-index-json.py` | **1,852 cited / 11,367 backlinks**; authorities 89 authors / 17,302 citations (from the existing ledger) | 1,852 / 11,367 | none |

**Front advances to `bon-luc-c4-v1-13`** (the first manifest stage-2 row: Cap. IV, Vers. 1–13, ¶¶ 1–25, pp. 88–95; p. 88 nn. 10–12 are its, n. 12 a page runover onto p. 89). The loop runs to the **p. 188 gate** (close of c. 7). **No push, no deploy.**

---

## ARCHIVE — the p. 88 gate-items and tool-items lists as they stood at the gate (moved here from `next-session-resume.md`)

The full wording of each item stands in the superseded START HERE blocks of `next-session-resume.md` (bracketed numbers) and in each chunk's `## Notes`. Every item below was ruled by rulings 27–40.

**A. `title_la` under ruling 22.** (G1) opening stack read as ONE, lowest heading taken: `c2-v1-7`; `c3-v1-9`; `c3-v10-14`; `c3-v21-22`. (G2) `c2-v21-24`: the 54R t4, departing from the manifest's t3 cell → **cell corrected, ruling 33**. (G3) sentence titles: `c2-v25-35`, `c2-v36-39`. (G4) single-heading openings: `c2-v40-52`, `c3-v15-20`, `c3-v23-38`.
**B. *evangelizare* and *annuntiare*.** (G5) Isai. 40:9 "bringest good tidings" + `tr-evangelizare` (`c1-v39-45`). (G6) Bede's *evangelizante* (`c2-v8-14` p. 50 n. 12). (G7) Luke 3:18 "preach the gospel"; ¶ 44 *bona annuntiabat*; Isai. 52:7 "him that announceth" (`c3-v15-20`). (G8) Isai. 61:1 "to announce" (`c3-v1-9`); *denuntiare* "declare" / *annuntiare* "announce" (`c2-v8-14`). → rulings 27, 29.
**C. The *praedicare* family.** (G9) *praeconium* "proclamation" (`c1-v57-66`, `c1-v67-80`, `c2-v21-24`, `c2-v25-35`). (G10) *praedicare* + predicate adjective: Prov. 31:28, Cant. 6:8, `c2-v25-35`. → rulings 27, 30.
**D. *lumen* / *lux*.** (G11) `tr-lumen` in Bonaventure's prose (`c2-v8-14`, `c2-v21-24` ¶ 55, `c2-v25-35` Luke 2:32). (G12) Tob. 10:4 kept "light" (`c2-v40-52`). → rulings 27, 32.
**E. *pietas*.** (G13) `tr-pietas` outside cc. 15–16 (`c1-v46-56` ¶ 93, `c2-v25-35` ¶ 69). (G14) human *pietas* "piety", no note. → ruling 31.
**F. *vacare* / *quies* / *requies*.** (G15) "free for" + `tr-vacare` (`c1-v67-80`, `c2-v36-39`, `c2-v40-52`). (G16) *quies* "rest" (`c2-v21-24`, `c2-v40-52`, `c3-v23-38` ¶ 63 ×3). (G17) quotations / variants (Heb. 4:11; `c2-v1-7` variant; Isai. 1:16 *Quiescite* "Cease"). → ruling 32.
**G. *intellectus* / *intelligentia* / *eruditio* / *documentum*.** (G18) "intelligence by sight" (`c2-v15-20` ¶ 43). (G19) "in the intellect … in the affection" (`c2-v40-52` ¶ 110). (G20) *intellectus* "understanding" (`c3-v23-38` ¶ 57). (G21) *erudiuntur* "are schooled", *eruditor* "schoolmaster", Lam. 1:13 "chastised". (G22) *documentum* / *instructiones*. → ruling 32 (+ the ¶ 38 fix).
**H. House word-pairs.** (G23) *benedictus* / *beatus*. (G24) *admirabilis* / *mirabilis* / *mirari*. (G25) *cohortatio* / *exhortatio*; *comminatio* / *increpatio* / *admonitio*. (G26) *praeceptum* / *consilium* / *mandatum*. (G27) *corripere* / *arguere*. (G28) *purgatio* / *purificatio*. (G29) *ortus* / *partus* / *nativitas*. (G30) *claritas*; *clarificatio*. (G31) *cultus*. (G32) singles (*exsultare*, Eccli. 18:12 *miseratio*, *largitas*, *divulgare*, *profiteri*, *egenus*, *virtus Spiritus septiformis*, *timoratus*, *comprehendere*, *dominatrix*, *poenitentia*, *eventus*, *baptismus fluminis …*, *vir occasionatus*, *status* / *situs*). → ruling 32.
**I. Ruling-20 Douay adjustments.** (G33) lemma verses per chunk. (G34) adduced verses per chunk. (G35) the *complacere* triad. (G36) one verse, two renderings (Col. 1:13; 2:19 / 2:51; *puerum* / *pueri*). (G37) kept as the Douay inside a quotation. → rulings 27, 28.
**J. Names, canticles, register.** (G38) canticles as names. (G39) Trinitarian register. (G40) the genealogy's names. → rulings 35, 36.
**K. Quaracchi readings and misprints.** (G41) slips transcribed as printed. (G42) misprints bracketed. (G43) type faults recorded. (G44) lemma readings as printed. → ruling 36.
**L. Collection change (banked).** (G45) three *expositio* italic exceptions, all inside Bernard. (G46) sub-sites. → ruling 36 (no ruling asked).
**M. Records and citations.** (G47) `CAPITULUM III.` at ~0.47 of p. 69. (G48) p. 85 holds only p. 84 n. 14's runover. (G49) the first resolved inbound; one inbound lost (T12). (G50) the two `low` rows promoted. → rulings 34, 36, 37.

**Tool items (T1–T13), as they stood:** (T1) QA +1 "Esth. 98" at `c1-v46-56`. (T2) Bede "Comment. in Luc." false positive p. 36 n. 6; never recurred → **closed**. (T3) p. 38 n. 7 `forward` forever. (T4) p. 44 n. 7 wrong target. (T5) in-work forms produce no record → **deferred** (ruling 24 / 82(a)). (T6) 11 shared-page self-citations `page-multi`. (T7) own *Comment. in Eccle./Ioan.* inbounds and *S. Bonav., IV. Sent.* lost. (T8) p. 54 n. 10 dangling. (T9) p. 55 n. 8 Vol V page filed as Vol VII. (T10) cross-note anaphora. (T11) *Ecclesiastae N* body ordinals. (T12) *Exposit. in cap. N, M. S. Lucae* inbound lost. (T13) roman distinctio. → ruling 37 (the job above).
