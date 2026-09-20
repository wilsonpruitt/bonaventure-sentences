# Vol VI — load + pilot setup (2026-09-19, Sonnet; for the Fable pilot session)

Everything below is **MEASURED** unless labelled **PREDICTION**. Nothing here is a chunking decision — those are the pilots' job.
Standing warning: *a work map's description of an unopened work is a guess wearing a table cell.*

## Loaded

- Source: Internet Archive `doctorisseraphic06bona` (identity confirmed by its own contents leaf: "IN HOC SEXTO TOMO").
  `raw/doctorisseraphic06bona.pdf` (74 MB, **688 pp**) + `raw/doctorisseraphic06bona_djvu.txt` (4.4 MB, 100,589 lines) — both gitignored.
- **`pdf = printed + 42`.** Verified on 14 running-head folios (19/78/98/138/178/218/298/318/378/418/478/538/578/598) and against the
  boundary leaves below. ⛔ The raw's *folio digits* misread in the worn-5→3 class here too (a header read "38" at PDF 100 = p. **58**;
  "238" at PDF 300 = p. **258**) — the tracker's "leaf 0678 = p. 634" is a *leaf* count (offset 44), not a PDF page.
- Pages are **2067 × 2985 px at 450 dpi** (Vol V's were 2571 wide) — two-column, marginalia, footnote register, same Quaracchi
  furniture as Vol V (checked on p. 3 at ⅓ scale).
- Tooling wired: `tools/extract-pages.py --volume vol6` (offset 42, printed 1–634); `tools/colcrop.py` now defaults `auto` gutter for
  `vol6` as for `vol5`. `vol6/` and `raw/vision/vol6/` created. **NOT yet wired:** `build-content.mjs` `VOL_DIRS`, `build-citations.py`
  `VOLUME_COMPLETE`, `check-vol5-*`/census `VOLUMES`, `build-progress.mjs` (its Vol VI denominator is already hardcoded) — do these when
  the first chunk lands, not before.
- Plates pulled at 450 dpi (regenerable, gitignored): pp. 1, 2, 3, 4, 103–107, 235–239, 531–535, 634.

## The volume: four works, not the tracker's guess

Contents leaf (raw L90–96): Eccl. p. 1 · Sap. p. 105 · Ioan. p. 237 · Coll. in Ioan. p. 533. Prolegomena run pp. I–XL+ (PDF 3–~42; not chunked, editorial, as Vol V).
Index leaf PDF 677 ("INDEX EORUM QUAE IN HOC SEXTO TOMO CONTINENTUR"), then the index proper to PDF 688.

| # | Work | Half-title | Blank | **Body** | Raw band (approx.) | Notes |
|---|---|---|---|---|---|---|
| 1 | *Commentarius in Ecclesiasten* | p. 1 (PDF 43; 0.543 %) | p. 2 (0.004 %) | **3–103** (PDF 45–145) | L≈3990 → L18259 (`EXPLICIT ECCLESIASTES` L18260) | p. 104 blank (0.005 %) |
| 2 | *Commentarius in Sapientiam* | p. 105 (0.550 %) | p. 106 (0.042 %) | **107–235** (PDF 149–277) | L18908 → L38373 | p. 236 blank (0.006 %) |
| 3 | *Commentarius in Ioannem* | p. 237 (0.637 %) | p. 238 (0.053 %) | **239–532** (PDF 281–574) | L38374 → L83854 | **ends on p. 532**, not 531 — it carries content (3.9 % dark), a `SCHEMA III` page; p. 533 is the next half-title |
| 4 | *Collationes in Ioannem* + Appendix | p. 533 (0.654 %) | p. 534 (0.009 %) | **535–634** (PDF 577–676) | L83855 → L99315 | two Appendix collationes at pp. 632–634 (`APPENDIX COLL. I` L98887, `II` L99029); index L99316 |

⚠ Blank-leaf numbers: pp. 106 and 238 read ~10× the other blanks (0.04–0.05 % vs 0.004–0.009 %). **PREDICTION: scan-edge, as p. 116 in Vol V —
read both plates before calling either work's first page.** The two half-title/blank pairs at 105/106 and 237/238 are otherwise the shape of every
Vol V work opening; **unlike Vol V's three QD, EVERY work here has its own half-title** (all four measured).

## Structure signals from the raw (counts, not decisions)

| | Eccl | Sap | Ioan | Coll |
|---|---|---|---|---|
| Lines in band | 14,918 | 19,466 | 45,481 | 15,461 |
| `Vers.` (apparatus verse notes) | 629 | 1,052 | 2,199 | 758 |
| `QUAESTIO` headings | 3 (`QuAESTio I` at L4394) | 0 | 3 | 0 |
| `SCHEMA` | 1 | 2 | 2 | 0 |
| `SCHOLION` | 1 | 0 | 1 | 0 |
| `PROOEMIUM` | yes (L4057 area; opens with `INTRODUCTIO GENERALIS`) | yes (L18920) | yes (L38383) | — |
| Running head | `COMMENT. IN ECCLESIASTEN C. N.` | `COMMENT. IN SAPIENTIAM C. N.` | `COMMENT. IN IOANNEM C. N.` | `COLLATIONES IN IOANNEM CAP. N. COLL. N.` (75 hits) |

- **Eccl.** `Capitulum I.` L4843 · II L6485 · III L7620 · IV L9047 · **VII L11446 ("VH" — garbled)** · VIII L13113 · XI L16562 · XII L17198.
  **Only eight of twelve found — V, VI, IX, X are missing from a first grep**, the same garble class as `COLLATIO`/`SUMMARIUM`; find them by content. **Not
  a finding that they are absent.** Eccl. p. 3 is `PROOEMIUM / COMMENTARII IN ECCLESIASTEN` + `INTRODUCTIO GENERALIS` with marginalia and a
  ⅓-column footnote register; notes cite `Vers. N` (the commentary is verse-keyed, so the footnote grid is **verse-anchored**, unlike Vol V's
  pure citations — expect the citation index's tier-B/C machinery to matter).
- **Collationes:** running heads name `CAP. N. COLL. N.` and some carry **two** numbers (`COLL. VI. VII.`, `COLL. XVII. XVIII.`, `COLL. XLIX. L.`) — the PDF
  running heads reach at least **LXXIX** (PDF 672–673) before the Appendix. **PREDICTION: ~79 collationes + 2 Appendix, per-John-chapter.
  Unverified until the index leaf is read — ⛔ do not carry 79 as a count.**
- All four commentaries are **schematic/scholastic *divisio textus*** commentaries (`EXPOSITIO HUIUS Prologi… Prima pars habet tres partes`), as Sap/Eccl
  are Bonaventure's earliest Scripture lectures. **PREDICTION: the `Vers. N` grid means the paragraph-numbers (`1.` `2.`) are Quaracchi's citation unit,
  as in the Itinerarium — check before deciding anything finer than the capitulum.**

## What the pilots have to decide (Fable's; one mini-pilot per genre, per the standing plan)

1. **Chunk unit for the three commentaries** — capitulum (12 / 19 / 21) is the first hypothesis; the test is the frozen one: *does the unit carry apparatus
   anchors, and what does Quaracchi's own citation practice cite?* Read every `supra`/`infra` cross-reference into this volume from Vols I–V
   (grep `Comment. in` / `in Eccl.` / `in Ioan.` in `index/citations.tsv`) before deciding.
2. **The `Proemium`/`Introductio generalis`** — chunk of its own (Breviloquium precedent: division 0) or folded into c1 (the Vol V short-opener rule);
   at Eccl. it fills pp. 3–~? (measure).
3. **`QUAESTIO`s inside a commentary** (Eccl. ×3, Ioan. ×3) — are they whole quaestio-shaped units or headings within one chunk? **Do not import the
   Sentences quaestio conventions until read.**
4. **`SCHEMA` and `SCHOLION` pages** — the Ioan. tail (p. 531–532) is `SCHEMA` display matter; how does a schema render (table? indented outline?). Never
   trim it as furniture (the Summarium rule: display matter set in the text block is rendered).
5. **Collationes** — reportatio register (Hexaemeron/donis/praeceptis shape, Summarium?) or not; the double-numbered running heads (`COLL. VI. VII.`) decide
   whether a leaf-shared collatio pair is one unit or two.
6. **Register:** Vol V's rulings carry (*intellectus*/*intelligentia*; *lux*/*lumen*; *pietas* piety; *vacare* dikaisune rule; *fundam.* in the apparatus).
   **New pressure:** Vulgate-verse quotation at commentary density (the Douay-adjusted-to-Quaracchi rule will be exercised hundreds of times per work),
   and John's *Verbum*/*lux*/*veritas* — expect *lux*/*lumen* ruling 2 to bite at Ioan. 1 **hard**; census over the BUILT text, never the raw.
7. **Cadence:** four works → four work-close gates; page counts 101 / 129 / 294 / 100. Ioan. (294 pp) exceeds the ~100-pp trigger ~3× — the shakedown/gate
   placement needs deciding; **place a gate where the register load falls, not by distance** (Vol V Sermones lesson).
8. **Order:** Wilson's call. Suggested by size and by what the register already knows: **Eccl. (101 pp) is the natural first pilot** — smallest, first in the
   volume, and its own page 3 is already read.

## Traps carried in from Vol V (do not re-derive)

- The raw has **no reliable footnote numerals** — check on the plate whether that holds here (the Sentences volumes' OCR carried them; Vol V's did not). **Measure it in
  the first pilot: it decides whether `audit-apparatus-count` works on Vol VI.** Nothing is asserted here.
- Any blank/half-title claim is a screen; the plate is the evidence. Every span end fixed positively from the next unit's heading, never from white space.
- A mirror-reversed leaf (Vol V p. 535) is possible in any archive scan: **a leaf whose OCR alone is unreadable while its neighbours are clean → look at the image.**
- `extract-pages.py` skips an existing file **whatever its dpi** — check pixel size of any page touched twice.
- ⛔ Never `git stash` in this repo.
- Disk: **6.9 GB free (97 %)**. Plates per unit, never in bulk; pass-4 deletion at each gate.

---

# ECCLESIASTES — RULINGS (Wilson, 2026-09-19; taken off the evidence sheet before any chunk existed)

Evidence (measured 2026-09-19): Quaracchi cites the work by chapter+verse (`Comment. in Eccle. 1, 4.`); the volume index (PDF 677–678, read on the plate) gives Prooemium pp. 3–9 (Introductio generalis, De quadruplici causa, Quaestio I–IV, Jerome's Prologus, Expositio prologi) → 12 capitula → ~41 verse-pericopes each followed by `Quaestiones` → Cap. XII Scholion p. 99, Schemata p. 100. The raw has no footnote numerals (bands-only apparatus). Gutter runs measure 45–49 px at 2067 px width — recalibrate; Vol V's 58–64 px band is not the floor here.

1. **Chunk unit = the index verse-pericope, with its Quaestiones** (~41 chunks; `division` = capitulum, `verses: [a, b]` in frontmatter). Capitulum-level chunking refused.
2. **Prooemium = TWO chunks, division 0:** Bonaventure's opener pp. 3–8 (`bon-eccl-prooem`) and Jerome's Prologue + Expositio pp. 8–9 (`bon-eccl-prol`).
3. **Scholion (p. 99) and Schemata (p. 100) = own chunks, rendered in full**; a schema's form is decided when reached.
4. **Small-cap divisio headings kept as `####` headings; `(Vers. N.)` addresses kept verbatim in both languages; `QUAESTIONES.` rendered `### Quaestiones`.**
5. **Register:** Vol V rulings carry. *Ecclesiastes* stays the name, *concionator* → "preacher"; *vanitas* → "vanity" throughout; the lemma is Douay adjusted to Quaracchi's Vulgate; the scripture index must not count a chunk's own lemma as a citation (first-chunk resolver job).
6. **Cadence:** shakedown gate after Cap. I (p. 19), work-close gate at p. 103. ~~Deploy at each, each a separate OK.~~ ⭐⭐ **AMENDED BY WILSON 2026-09-20: BOTH GATES STILL RUN, BUT THERE IS ONLY ONE DEPLOY AND IT IS AT THE END OF ECCLESIASTES (p. 103).** The shakedown gate is a QUALITY gate and fires as ruled; it simply no longer carries a deploy with it. ▶ **Do not surface a deploy at p. 19** — the two cadences are separate (repo CLAUDE.md § DEPLOY CADENCE: *a polish gate and a deploy boundary coincide at a work boundary and nowhere else*), and here they have been deliberately decoupled. The deploy at p. 103 is still Wilson's own per-action hard stop, and it carries the **deploy-only batch** with it — see the resume note's carry-list.
8. **Work order after Eccl.:** Sap → Ioan → Collationes (Sap a confirmation pilot; Coll a full pilot).
7. *(pilot chunk — awaiting answer)*

---

# CAPITULUM I SHAKEDOWN GATE — RULINGS 9–14 (Wilson, 2026-09-20)

**Run over pp. 3–20, seven chunks, 156 entries. Full log + evidence: `manual-review/vol6-cap1-shakedown-gate.md`
and `manual-review/vol6-cap1-shakedown-evidence.md`.** Procedure as at the `perfectione` and `serm` gates: a
read-only agent compiled the evidence sheet first; Wilson ruled all six items in one sitting without opening a
chunk. ⛔ **No deploy, per ruling 6 as amended.** ⭐ **ZERO text lines changed by the gate** — rulings 9, 10, 12
and 14 changed nothing by design, and 11 and 13 added notes beside text that was already right.

9. **THE ITALIC CONVENTION: p. 11 STANDS AS PRINTED; the exception is RECORDED, not repaired.** The inversion
   stated at p. 9 n. 4 holds in the *expositio* on every leaf but p. 11 and does not reach the Prooemium or the
   Quaestiones. Normalising was refused — Quaracchi is never silently emended, and five builders have found no
   discriminator. ⛔ The "self-quotation" hypothesis is **dead**, measured: p. 16 sets Ecclesiastes quoting
   itself roman-in-guillemets. To the p. 103 gate, with an exact expositio count for pp. 10/12/13 owed there.
10. ***magister* RATIFIED at n = 3** (two of the ruling + Lombard → "the Master", an exception fixed by its own
    object). Off the docket. ⚠ ***doctor* is NOT zero in Vol VI** — one Latin site, `prooem` p. 5 n. 6,
    untranslated in the **En.** half. The zero was true of the English only.
11. ***doctrina* CONTEXTUAL under the dikaisune rule, with `tr-doctrina` notes.** Ten Latin sites in four chunks
    taking three English words; all three renderings stand. **Four notes written, one per chunk carrying the
    word**, because notes do not reach across chunks on the site — the same argument that decided ruling 13.
12. **HEADING FLATTENING KEPT. Level tracks FUNCTION and is uncorrelated with class and size**, settled by the
    p. 10 pair (one leaf, one column, one class, one size, three lines apart, different levels). ⚠ The docket's
    premise was wrong: classes 1 and 2 each take both levels; only class 3 is uniform. Revisit depth at p. 103.
13. **THE `tr-` MECHANISM EXTENDED: an English-side anchor inside `## Apparatus` satisfies the pairing, for
    `tr-` labels only.** Applied in `polish-style-scan.py`, `check-vol5-apparatus.py` and
    `vol6/bon-eccl-c1-v12-15.md`; tested positive and negative; renderer needed no change.
14. **THE RESOLVER DOCKET RECORDED, NOT SCHEDULED.** Five artefacts confirmed live off the ledger; 2a and 2b are
    one missing rule (*an apparatus note's `ibid.` takes its antecedent from WITHIN the note*) and 2b is the only
    one filed confidence A on a wrong target. Its own scoped job with its own before/after diff, unscheduled.

⚠⚠ **A FROZEN CLAIM IN THE REPO CLAUDE.md WAS FALSE AND IS CORRECTED:** translator's notes DO enter the citation
ledger when their English prose names a scripture reference (four such records already stand in deployed Vol V).
Corpus-wide; carried to p. 103.
