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

# RULING 15 — THE UNINDEXED `(Vers. 17.)` UNIT (Wilson, 2026-09-30, at `bon-eccl-c4-v13-16`)

15. **ECCLE. 4:17 FOLDS INTO THE FIRST CAPITULUM V CHUNK, `bon-eccl-c5-v1-8`, whose `verses` stays `"1-8"`;
    the Cap. IV verse is recorded in its Notes and `transcription_status`, not in the label.** The chunk opens
    seven lines down p. 42's LEFT column at the in-column italic *Partis secundae membrum II. De remedio triplici
    contra triplicem vanitatem culpae…*, carries the *Custodi pedem tuum* Divisio, `Aʀᴛ. 1.` *De remedio contra
    vanitatem malitiae, ex qua oritur triplex inordinatio.*, *Primo datur remedium contra inobedientiam.* and the
    `(Vers. 17.)` exposition, then the full-measure `Cᴀᴘɪᴛᴜʟᴜᴍ V.` heading and Cap. V's verses. `division: 5`.
    **Why:** ruling 1's index pericope has no line for Vers. 17, and the text's own structure decides it —
    Art. 1's subdivisio names its three remedies at 4:17 (*contra inobedientiam*), 5:1 (*ibi: Ne temere quid
    loquaris*) and 5:7 (*ibi: Si videris calumnias egenorum*), so Art. 1 = 4:17 → 5:7, the head of the index's
    Cap. V `Vers. 1-8`. A stand-alone `c4-v17` would split Art. 1 across two chunks; extending `c4-v13-16` would
    put a new membrum's opening inside the previous article's chunk. Both refused.
    ▶ **General rule for Vols VI–X: when a verse falls outside every index pericope, it goes with the unit whose
    printed divisio claims it, not with the chapter number it happens to carry.** ⚠ The breadcrumb will read
    `Cap. 5, Vers. 1-8` although the chunk opens on Eccle. 4:17 — accepted cost; the `verses` field keeps the
    index's label so the build needs no new title shape.

# RULING 16 — CAP. VII VERS. 1 AND THE QUAESTIONES AFTER IT (Wilson, 2026-10-04, at `bon-eccl-c6-v8-11`)

16. **`bon-eccl-c7-v1` takes Eccle. 7:1 AND all the Quaestiones printed after it, including Q. I on 6:9;
    `bon-eccl-c6-v8-11` is unchanged and closes above the full-width `CAPITULUM VII` heading (p. 53, ~41 %).**
    Art. 3 announces three steps — 6:8–9, 6:10–11, *non inquirat sublimia* — and the third is expounded only
    after the heading, at 7:1; the index files the Quaestiones under Cap. VII Vers. 1. **Why (a):** the printed
    capitulum heading and the index agree, nothing already built changes, and Art. 3's steps still read in order
    across the seam. ▶ **Distinguishes ruling 15:** there a verse had NO index line, so the divisio decided; here
    both units have index lines and a printed heading stands between them, so the heading + index decide. Record
    in `c7-v1`'s Notes that its first exposition completes Art. 3 of Cap. VI and that Q. I concerns 6:9.

# RULING 17 — THE HEADING-LESS PERICOPE OPENING (Wilson, 2026-10-11, at `bon-eccl-c10-v4-7`)

17. **`bon-eccl-c10-v4-7` opens with NO `####` heading, and its `title_la` is the divisio's first sentence after the
    lemma: *Praemissa est supra sapientis despectio et econtra ipsius iusta commendatio; subiungitur hic tertio
    stultorum promotio* (option (a)).** The pericope opens ~41 % down p. 80's RIGHT column on an ordinary indented
    paragraph standing directly below `c10-v1-3`'s Quaestio reply 1 (*…et ideo totum meretur amittere.*) — no blank
    line, no class-2 `Art.`, no class-3 or small-bold heading — whose italic lemma (*Si spiritus potestatem
    habentis.*) is the next index verse and whose divisio says *tertio* (marginale `De 3. parte.`). The first such
    opening in the work: every earlier pericope opened on a printed heading, so the `####` opener and the
    heading-text `title_la` precedent had nothing to take. Option (b) (the same, with the marginale as a guide only)
    was not needed. **Why:** a heading invented for the reader would be our text set where Quaracchi set none (ruling 9
    — transcribe as printed); the divisio's first sentence after the lemma is the unit's own statement of what it is,
    exactly as the first sentence served at `c7-v1` and `c9-v1-3` where no heading stood below a capitulum heading.
    ▶ **General rule for Vols VI–X: a pericope that opens with no printed heading takes no opener heading, and its
    `title_la` is the first sentence of its divisio after the lemma** (italics dropped in the title fields). Extends
    the `c7-v1` / `c9-v1-3` "first sentence" precedent from an exposition below a capitulum heading to a divisio with
    no heading at all.

# RULING 18 — THE FORM OF THE SCHEMATA (Wilson, 2026-10-11, at `bon-eccl-scholion`)

18. **The Schemata (pp. 100–103, `Schema I.`–`IV.`) render as NESTED INDENTED OUTLINES, in Latin and in English,
    each branch keeping its verse range** (e.g. *titulus* 1,1 · *tractatus* 1,3–12,8 · *epilogus* 12,9–14). Chosen
    over tables and over plate images. **Why:** an outline is searchable, reads on a phone, and is consistent with the
    rest of the site, where every other unit is text; a table cannot carry a bracket-tree's depth without merged cells,
    and an image is neither searchable nor translatable. This is the form ruling 3 left open (*a schema's form is
    decided when reached*); ruling 3 still governs that the Schemata are their own chunk(s), rendered in full. ▶ The
    Scholion's own section II says what the schemata are for — *multitudinem divisionum et principalium sententiarum,
    quae sunt in expositione litterali … in uno conspectu* — so each branch carries its divisio member WITH its
    governing sentence, and the outline's job is the single view. ⛔ Nothing printed is dropped: the rotated part-title,
    every bracket member, every verse range, p. 100's one footnote, and p. 103's closing line *(Post tertiam partem
    sequitur conclusio…)* are all transcribed as printed (ruling 9). ▶ **General rule for Vols VI–X:** a printed
    bracket-tree schema is rendered as a nested indented outline in both languages, its addresses kept verbatim.

# RULING 19 — THE CHUNKING OF THE SCHEMATA (Wilson, 2026-10-11, at `bon-eccl-schemata`)

19. **The four Schemata are ONE chunk, `bon-eccl-schemata`, `division: 14`, with `Schema I.`–`IV.` as four sections
    on one page** (option (a), chosen over four chunks `bon-eccl-schema-1`…`-4`). **Why:** the editors' own p. 100
    footnote ties them together — *Harum trium partium divisiones exhibentur in schematibus II. III. IV.* — so Schema I
    is the trunk and II–IV are its three branches drawn out; split into four pages, the note on Schema I would point
    across chunks at the very trees it introduces. The index's single line (`Schemata » 100`) and the Scholion's *his
    quatuor schematibus … in uno conspectu* agree. Ruling 3 (their own chunk, rendered in full) and ruling 18 (nested
    indented outlines, each branch keeping its verse range) are unchanged; this settles only what ruling 3's plural
    left open. Division 14 is the next after the Scholion's 13. ▶ **General rule for Vols VI–X: a set of editorial
    schemata that cross-refer to one another is one chunk with one section per schema.**

# ECCLESIASTES WORK-CLOSE GATE — RULINGS 20–26 (Wilson, 2026-10-11)

Full evidence and edit list: `manual-review/vol6-ecclesiastes-workclose-gate.md`. All taken as recommended.

- **20.** *poenalitas* → "penalty" · *poena* → "punishment" · *supplicium* → "punishment" (shared with *poena*, as the body already had it). `c7-v24-30` and the Schemata conformed (10 edits); `c7-v2-7`'s legal "liable to penalty" stands.
- **21.** *mutabilitas* → "mutability" everywhere; the Prooemium/Scholion "changeableness" conformed (4 edits). *intransmutabilitas* ("unchangeableness") and *volubilitas* ("changeableness") are other words and stand.
- **22.** *commotio* "shaking" / *tremor* "trembling" · *resolutio* "resolution" / *dissolutio* "dissolution" — kept apart; `c12-v1-14` conformed to the Schemata (3 edits).
- **23.** *iucunditas*: no fixed term (the `bon-serm` ruling-6 release — nothing contrasts it).
- **24.** Translator's (`tr-`) notes are never indexed: `build-citations.py` skips them (−11 ledger records).
- **25.** p. 11's italic Scripture reproduced as printed; question CLOSED. Exact count pp. 10/12/13 = 0/11/23.
- **26.** Heading depth stays flat; CLOSED.
- **Housekeeping:** Schemata wording differences recorded as printed; Schemata verse ranges not indexed; trailing-`---` bug fixed in `build-content.mjs`; `tr-studium` confirmed.

# SAPIENTIAE MINI-PILOT — RULINGS 27–35 (Wilson, 2026-10-15; "all as recommended")

Evidence sheet: `manual-review/sapientiae-pilot-scouting.md` (index read on the plate, idx-678 both halves; structure,
register census, mechanics). Taken before any chunk existed.

- **27. Chunk unit = the CAPITULUM: nineteen chunks `bon-sap-c{1..19}`**, `division: N`, `verses: "1-N"` (the index label
  verbatim), `type: pericope`. The index gives each chapter ONE line and lists NO Quaestiones; Quaracchi's self-citations
  are chapter+verse. Ruling 1's principle (the index unit) applied to an index whose unit is the chapter.
- **28. Prooemium = TWO chunks, division 0:** `bon-sap-prooem` (section 1, `type: prooemium`, pp. 107–109, Introductio
  generalis + De quadruplici causa, ¶¶1–9) and `bon-sap-prol` (section 2, `type: expositio`, pp. 109–110, Prologus
  S. Hieronymi + Expositio prologi). **The p. 110 `COMMENTARIUS / IN LIBRUM SAPIENTIAE.` stack, `DIVISIO GENERALIS.`, the
  `PARS I.` heading and its three subdivisiones go to `bon-sap-c1`.**
- **29. `PARS I.` (p. 110) and `PARS II.` (p. 144) are transcribed as headings inside `c1` and `c6`; NO `pars:` field;
  breadcrumb stays `Cap. N, Vers. 1-N`.** Recorded in those chunks' Notes and the registry comments.
- **30. `bon-sap-scholion` (p. 233, division 20, `type: scholion`) and `bon-sap-schemata` (pp. 234–235, division 21,
  `type: schemata`, ONE chunk, two sections)** — rulings 3, 18, 19 as written.
- **31. Marginal `Quaestio.` paragraphs (~5 sites) are ordinary paragraphs, transcribed as printed; the marginale goes to
  Notes.** Not lifted into `### Quaestiones`. Ruling 4 otherwise ports whole.
- **32. Register:** *Sapientia* capitalised in the print → "Wisdom", lower-case → "wisdom" (follow the print, never decide
  it); *Sapiens* as the book's author → "the Wise Man", generic → "the wise man"; *iustus/iniustus* → just/unjust;
  *impius* → **impious** (Douay "wicked" adjusted — one Latin word, one root); *iniquus* → wicked, *iniquitas* → iniquity;
  *idolum* → idol, *idololatria* → idolatry, *idololatra* → idolater, *simulacrum* → image. **Purity triple APPLIED**
  (*pudicitia* purity · *puritas* pureness · *munditia* cleanness — *pudicitia* is live here, so the *serm* release does
  not apply). Carried unchanged: ruling 2 (`tr-lumen` per chunk; Sap 6:23 *Diligite lumen sapientiae* keeps "lumen"),
  rulings 5, 10, 11, 20, 21, the *vacare* dikaisune rule, `tr-studium`, *intellectus*/*intelligentia*. Work title
  "Commentarius in librum Sapientiae" / **"Commentary on the Book of Wisdom"**.
- **33. Registry:** slug `sapientiam`, id prefix `bon-sap-`, book 16, tome 6, initial "S", `divisionLabel: "Capitula"`,
  divisions 0 Prooemium · 1–19 Capitulum N · 20 Scholion · 21 Schemata; `sapientiam` joins the `ecclesiasten` branch of
  `buildWorkChunkTitle`. Entry goes in with `prooem` (division 0 only); each capitulum adds its line after reading its
  heading in place.
- **34. Cadence: THREE gates — shakedown at p. 125 (after Cap. II), mid-work at p. 192 (Cap. XII/XIII seam), work-close at
  p. 235. ONE deploy, at p. 235.** Each gate on Wilson's go only.
- **35. One Opus agent per chunk, incremental-append discipline from the start; a two-pass build only for a chunk that
  dies once or measures over ~10 pp.** ~50–70 apparatus entries per capitulum is a planning figure, never a gate.

# SAPIENTIAE SHAKEDOWN GATE (p. 125) — RULINGS 36–43 (Wilson, 2026-10-16; "all as recommended")

Evidence sheet: `manual-review/vol6-sapientiae-shakedown-evidence.md`; gate log
`manual-review/vol6-sapientiae-shakedown-gate.md`. Scope `bon-sap-prooem` · `prol` · `c1` · `c2`, pp. 107–125.

- **36. `title_la` procedure RATIFIED:** take the first heading printed below `Capitulum N.`; if that heading
  governs a run of capitula, descend to the next; if nothing stands below, take the subdivisio heading above that
  covers exactly the chapter (c1/c2 as built). Expect XIII, XVI, XVIII to need it. 0 lines.
- **37. A Quaracchi verse slip is transcribed as printed in the Latin and bracketed in the English** —
  `[so printed; the verse is Job 6:25]` at c1 p. 115 n. 6 (the `bon-qpe-q4-a1` form). No `[?]`; the ledger's
  Job 6:2 record goes to the resolver docket. 1 line.
- **38. The same treatment for a locus slip:** c2 p. 121 n. 3 `I. de Doctr. christ. c. 3. n. 4` →
  English `[so printed; the passage is I, c. 4, n. 4]`. 1 line.
- **39. Ruling 31 KEPT at the measured density** — c1 **9**, c2 **4** `Quaestio` marginalia (c1's Notes and the
  resume note had said "seven"; corrected). **From `bon-sap-c3` on, each chunk's Notes carries a
  `### Marginal quaestiones` table** (page, column, marginale, incipit) so the p. 192 / p. 235 gates can derive
  the count. Notes only; nothing rendered. 0 text lines.
- **40. Resolver docket (ruling 14) gains:** "2c" — c2 p. 121 n. 2's stray `ibid. 37, 20` binds to a false
  crossref (p. 118) and loses Gen. 37:20; plus c1 p. 116 n. 2 `d. 38. q. 5. et 6.` (q. 6 never emitted),
  prooem p. 108 n. 7 `[I: Cor.` → `Cor*`, prol p. 109 n. 8 `Supra n. 5. 6.` unparsed. No text edit.
- **41. DEFECT REPAIRED:** c2 English `**Contra:**` at pp. 123 and 125 → "**On the contrary:**" (c1's form and
  the formula table's). The Latin keeps `**Contra:**`. 2 lines.
- **42. Optional conformings DECLINED:** *malorum* → "wicked men" (c2 p. 122) and Sap. 5:6 "hath not shone"
  stand. One site each; no ruling earned.
- **43. OUT OF SCOPE, PARKED as its own scoped job:** untranslated `Contra:` / `Sed contra:` labels in DEPLOYED
  English (Ecclesiastes 14 + 2; scattered in Vols III–V — ~34 English sites corpus-wide against ~1,170
  "On the contrary:"). Mechanical conform to "On the contrary:"; needs a deploy, so after the Vercel freeze.

# SAPIENTIAE MID-WORK GATE (p. 191) — RULINGS 44–58 (Wilson, 2026-10-16; "all as recommended")

Evidence sheet: `manual-review/vol6-sapientiae-midwork-evidence.md` (commit `7fefe3d`); gate log
`manual-review/vol6-sapientiae-midwork-gate.md`. Scope `bon-sap-c3` … `bon-sap-c12`, pp. 125–191. Ruling 34 placed the gate
"at p. 192"; the seam is p. 191.

- **44. (A1) *punitio* → "punishing"; *poena* → "punishment".** Per-site, English only; *supplicium* untouched here (its
  sharing with *poena* under ruling 20 is c16's question). **Binding on `bon-sap-c13` onward.** Reason: the divisio of
  cc. XI–XIX is built on the act/penalty pair (*punitionem per poenas leviores / graviores*), and one English word for both
  hid the hinge of Part II's third ratio at a site count that is large and growing. Applied: 34 body sites + 2 `title_en`.
- **45. (A2) The misprint class RATIFIED as built:** an identifiable wrong sort or slip → as printed + English bracket
  (`[so printed: X for Y]` for a letter fault, `[so printed; the verse/passage is …]` for a locus slip); an unnameable sort →
  read plain and disclosed (the `necessarium` rule); a compositor's blank → reproduced + `[*sic*]`. Reason: one rule for the
  whole class, consistent at all ten sites; ruling 9 forbids silent emendation. 0 lines.
- **46. (A3) The verse test RATIFIED at Job 37:3, Col. 1:12 and Isa. 50:11** — received "light" kept; each is quoted only as
  a verse and nothing in the prose turns on *lumen*. 0 lines.
- **47. (A4) A fused heading is taken WHOLE for `title_la`, never split — a corollary of ruling 36** (c10 run + member; c11
  member + sub-member). Reason: cutting invents a title Quaracchi did not print. 0 lines.
- **48. (A5) Ruling 37's bracket applies in the BODY as in the apparatus** (c11 p. 180, *Proverbiorum decimo sexto* for
  Prov. 24:16). Reason: the bracket marks a certain printed slip wherever it stands. 0 lines.
- **49. (A6) c7 p. 156 *Amans bonum, actum* LEFT as printed, no bracket.** Reason: it construes as a gloss, and a bracket
  would assert a slip nobody has shown; one site. 0 lines.
- **50. (A7) The `verses` field keeps the index label VERBATIM even when the last address exceeds it** (c11 reaches
  `(Vers. 27.)` under `"1-26"`; ruling 27, the c1 Vers. 16 precedent). 0 lines.
- **51. (A8) Marginal quaestiones are counted by the PRINTED marginale** (a numbered `Quaestio 1./2.` pair = two); an
  unlabelled pair (c7 p. 159 L) is recorded in Notes, not counted. 25 in pp. 125–191. 0 lines.
- **52. (A9) The c6 Sap. 6:27 *accipite disciplinam* → "instruction" conform is DECLINED** (ruling 42: one site of 46, no
  ruling earned). 0 lines.
- **53. (B1) `tr-doctrina` — one note per chunk carrying the word, apparatus-only included (ruling 11); "instruction"
  RATIFIED as the quotation branch** (Douay kept inside a quotation nothing leans on: c8 Ecclus. 6:18, c10 Prov. 1:7).
  Written in c6, c7 (apparatus-anchored, p. 154 n. 3, ruling 13) and c8. 3 notes, 0 text lines.
- **54. (B2) c8 *studium* → "study" (the work's one root, with the prooem/c1/c6 notes); `tr-studium` written in c8.**
  Reason: c8's heading *ex studio quaerendi sapientiam* is a proof inside the exhortation *ad studium et amorem
  sapientiae*. Five "zeal" sites conformed; Prov. 20:11 *Ex studiis suis* keeps Douay. 5 lines + 1 note.
- **55. (B3) The index page = the page of `(Vers. 1.)`; the `Capitulum N.` heading may stand on the leaf before — the
  end-prediction rule for c13–c19** (11 of 11 openings; VIII 159/160 and XIII 191/192 discriminate). The scouting table's
  `Cap. X … 174` corrected to `171`. 1 doc line.
- **56. (B4) Carry-list drift corrected in the next resume block** (item 8 "first numbered quaestiones" false — c1 p. 112/116,
  c6 p. 146 came first; item 2 "3×" = one site read at 3×; item 20 "indistinguishable until here" — VIII had decided it), and
  c6's Notes *doctrina* count "one" → two, corrected at the gate because c6 was being edited for ruling 53. Doc only.
- **57. (C1) The `ibid. C, V` / `ibid. v. N` coordinate drop in `build-citations.py` is a SCOPED JOB BEFORE THE p. 235
  DEPLOY** — capture the coordinates after `ibid.`, take the antecedent's BOOK and the ibid.'s own C:V, look back past a
  non-scripture antecedent — with a before/after ledger diff reviewed by Wilson. NOT done at this gate. Measured: 30 records
  in scope, 251 corpus-wide, 1 honoured.
- **58. (C2–C5) PARKED** (ruling 40: logged, chunks never edited): C2 printed slips in the ledger (fold into C1's job as a
  small override table) · C3 dropped chain continuations · C4 unparsed named units · C5 owner-blind `page-multi` (1,178
  corpus-wide; a design improvement, not a defect).

# SAPIENTIAE WORK-CLOSE GATE (p. 235) — RULINGS 59–68 (Wilson, 2026-10-16; "all as recommended")

Evidence sheet: `manual-review/vol6-sapientiae-workclose-evidence.md` (commit `e36a25f`); gate log
`manual-review/vol6-sapientiae-workclose-gate.md`. Scope: the whole work, all 23 units `bon-sap-prooem` … `bon-sap-schemata`,
pp. 107–235. The third of ruling 34's three gates. Wilson's ruling, verbatim: **"all as recommended"**.

- **59. (A1) *supplicium* → "penalty" throughout the work; *poena* stays "punishment" (ruling 20), *punitio* "punishing"
  (ruling 44).** Per-site, English only, 24 sites in 11 units (c1 5 · c2 1 + 1 apparatus · c3 1 · c5 4 · c6 2 · c10 1 · c13 1 ·
  c16 3 · c17 1 · Schemata 4), the three former "torment" sites (c5 ×2, c6) included. **Matt. 25:46 inside c3's Gloss
  (p. 129, *impii ibunt in supplicium aeternum*) keeps Douay "eternal punishment"** — the quotation branch (rulings 46/53).
  c1 p. 117 *aequitatem supplicii seu poenae inflictae* → "the equity of the penalty or of the punishment inflicted", the
  earlier undisclosed *poena* → "penalty" reverted to ruling 20. Reason: one Latin word with one sense; ruling 20's sharing
  produced "the punishment of punishment" ×5, including the run heading of cc. XVI–XIX (*de supplicio poenae*), the hinge
  of ratio 3's second member — the ruling-44 argument at n = 25. "Torment" refused by census (it is *tormentum* /
  *cruciatus*'s, and meets *supplicium* on pp. 138 and 146). "Penalty" is otherwise used only for *poenalitas* (c2 p. 118,
  ruling 20), in a different paragraph — **no sentence holds both.** ⚠ Ecclesiastes' four body *supplicium* sites stay
  "punishment" under ruling 20 — a cross-work divergence, recorded, not extended.
- **60. (A2) c11 p. 182 *poenas seu punitiones* → "punishments or punishings" KEPT** (ruling 44 exactly; the *seu* pair is the
  Latin's). 0 lines.
- **61. (A3) Job 24:13 RATIFIED as built:** c14 p. 201 "the light" (quoted only as a verse) and c17 p. 218 "lumen" (the body's
  *merito defuit eis lumen* leans on it). Ruling 46 decides by passage, not by verse. 0 lines.
- **62. (A4) c17 p. 218 *id est dati radii* keeps its bracket "[so printed: *dati* for *clari*]"** (ruling 45): *dati* does not
  gloss *limpidae*, unlike c7's *actum* (ruling 49), which construes. 0 lines.
- **63. (A5) Schemata p. 235 *de merito culpae* → "on the merit of fault"**, conformed to c13 p. 191 and c16 p. 209, whose
  sentences the Schemata summarise; the Latin and c13's printed heading *demerito* ("demerit") untouched. 1 line.
- **64. (A6) Ruling 51 KEPT: 61 marginal quaestiones in the work.** c19 p. 229 `[O]pponitur.` and its sibling c16 p. 214
  `Obiectio.` / `Solutio.` are labelled non-`Quaestio` objections, recorded, not counted (63 if the class were counted). 0 lines.
- **65. (A7) *tormentum* → "torment(s)" at the two Douay sites:** c11 p. 180 lemma Sap. 11:14 *per sua tormenta* → "by their
  torments"; c5 p. 142 n. 8 *in tormentum* → "(unto torment)", so Sap. 16:24 reads one way with c16 p. 216. Douay adjusted to
  Quaracchi's Latin (ruling 5, the *impius* precedent of ruling 32); after ruling 59 "punishment" is *poena*'s alone (save c3's Douay Matt. 25:46). 2 lines.
- **66. (B1) Ruling 44 applied to the two pre-c3 sites the mid-work gate's scope missed:** `bon-sap-prooem` p. 108–109
  *in punitione rebellium* → "in the punishing of the rebellious"; `bon-sap-c1` p. 115 *id est punitionem* → "that is, the
  punishing". *punire* forms untouched. 2 lines. The work's 69 *punitio* noun sites now all read "punishing".
- **67. (B2) `tr-studium` written in `bon-sap-schemata`** at *ex studio eam inveniendi* → "the study of finding her" (p. 235),
  English-only anchor, shaped as c8's note (ruling 54); ruling 11's one-note-per-chunk logic, as the Schemata already
  followed for `tr-vacare` and `tr-doctrina`. 1 note, 0 text lines.
- **68. (B3) Documentation:** *poenas seu punitiones* is on **p. 182**, not p. 183 — corrected in the mid-work gate log and
  c11's Notes; the running list's "c18 … *supplicium* ZERO" is true of *supplicium* only — c18's two `supplic-` hits (p. 222)
  are *supplicatio* / *supplicationis* ("supplication"), stated in the next resume block. Doc only.

# IOANNEM MINI-PILOT (pp. 237–532) — RULINGS 69–77 (Wilson, 2026-10-18; "all as recommended")

Evidence sheet: `manual-review/ioannem-pilot-scouting.md` (commit `70c0d01`), whose PROPOSED RULINGS section carries the
full argument and the refused alternatives for each item. Wilson's ruling, verbatim: **"All as recommended."** The
*Commentarius in Evangelium S. Ioannis* is the volume's third work: half-title 237, blank 238, body 239–532, Scholion +
Schema I on 530, Schemata II–III 531–532, the Collationes half-title on 533. Index shape = Ecclesiastes (verse-pericopes
with Quaestiones), not Sapientiae (capitula).

- **69. Chunk unit = the index verse-pericope WITH its Quaestiones (ruling 1 unchanged): 105 chunks `bon-ioan-c{N}-v{a}-{b}`,
  `division: N`, `verses: "a-b"`, `type: pericope`, ~2.7 pp each (max ~6).** The two pericopes without Quaestiones (XV 18-27,
  XVIII 39-40) and the two with a singular `Quaestio` (I 29-30, XXI 24-25) are the same unit. The capitulum (21 chunks, mean
  14 pp) refused, as for Ecclesiastes.
- **70. Prooemium = TWO chunks, division 0:** `bon-ioan-prooem` (section 1, `type: prooemium`, pp. 239–244, the Prooemium
  ¶¶ + its Quaestiones, shaped like `bon-eccl-prooem`) and `bon-ioan-prol` (section 2, `type: expositio`, pp. 244–246,
  *Prologus S. Hieronymi* + whatever stands with it — measure). The p. 246 `COMMENTARIUS` stack, ¶ 1's *Divisio generalis*
  and the `PARS I` heading go to `bon-ioan-c1-v1-2` (short-opener rule, Sap ruling 28). ⭐ **p. 239 n. 1 — the anchored
  heading's note carrying the whole reportatio *Sermo … quando incepit Ioannem* — is transcribed IN FULL as entry n. 1,
  both languages** (the `bon-hex-c23` precedent: an anchored entry carrying a text). Lifting the Sermo out as a `p239-nota`
  refused: the note is anchored, so the closing-note rule does not apply.
- **71. The printed `PARS I.` (p. 246) and `PARS II.` (p. 250, ¶ 17) are headings inside `c1-v1-2` and `c1-v6-8`,**
  recorded in Notes and registry comments; NO `pars:` field; breadcrumb `Cap. N, Vers. a-b` — ruling 29 as written.
- **72. Scholion (p. 530, one line) = own chunk `bon-ioan-scholion`, division 22; Schemata I–III (pp. 530–532) = ONE chunk
  `bon-ioan-schemata`, division 23, three sections** — rulings 3/18/19/30 as written. Folding the Scholion into the
  Schemata refused (ruling 3; the Sap pilot refused the same trade at six lines).
- **73. Quaestiones rendered `### Quaestiones` (ruling 4); the printed singular `QUAESTIO.` → `### Quaestio`; `Quaest. N.`
  and the per-chapter paragraph numbers kept verbatim in both languages — and ⭐ each pericope chunk records its paragraph
  range in frontmatter, `paragraphs: "17-24"`,** because Quaracchi cites this work by `c. N, n. M` (177 raw `supra/infra
  n. N` sites) and the chunk is coarser than the paragraph. One line per chunk at build; it is what a later resolver job
  needs to land `n. M` on a chunk. (The build does not read the field yet; the chunk records it.)
- **74. Register — the working register; the shakedown gate reviews it with sites in view:**
  - ⭐⭐ ***lux* → light / *lumen* → "lumen": RULING 2 UNCHANGED**, `tr-lumen` at the first site of each chunk, the verse
    test at every scriptural site — knowing that **the test fails at John 1:7–8 by its own terms** (the expositio leans on
    *lumine*), so the Prologue reads *"to give testimony of the lumen … He was not the light, but was to give testimony of
    the lumen"* against *"the true light"* at 1:9. Reasons: six gates have ratified the rule with the cost stated; Eccl and
    Sap in this volume carry it; the quaestio here turns on *lux per essentiam / per participationem*. **Alt (b) — release
    ruling 2 for this work alone — REFUSED** (a cross-work divergence inside Vol VI and a precedent that the rule yields
    where the text is famous; the Sermones gate refused the same carve-out for the Tractatus). **Alt (c) — exempt the
    Vulgate lemma only — REFUSED** (it splits the gloss from its lemma, the very thing the *mysterio* test prevents).
  - *Verbum* (capital) → **"the Word"**; *verbum* → word — follow the print, never decide it (ruling 9).
  - *signum* → **sign** (Douay "miracle" adjusted at 2:11, 2:23, 3:2, 4:54, 6:2, 6:14 …); *miraculum* → miracle (135 sites).
  - *caritas* → charity · ***dilectio* → "dilection"** (the corpus's 927 sites) · *amor* → love; the verbs *diligere* /
    *amare* both → "love", and **at 21:15–17, where *diligis* and *amas* are set against each other, one `tr-dilectio`
    note** says the Latin distinguishes what the Douay's "lovest" does not.
  - *testimonium* → testimony, *testis* → witness, *testimonium perhibere* → "give testimony" (Douay).
  - ***magister* → "teacher"** (Sermones ruling 2), **inside the Douay quotations too** (1:38, 3:2, 11:28, 13:13–14,
    20:16); **Lombard → "the Master"** in the apparatus (Eccl ruling 10). *doctor* → doctor; *discipulus* → disciple.
  - *Glossa* → "the Gloss" · *Evangelista* → "the Evangelist" · *Iudaei* → "the Jews" · *Paraclitus* → "the Paraclete" ·
    *Rabbi* kept.
  - **Carried unchanged:** *doctrina* dikaisune + `tr-doctrina` (ruling 11); *intellectus*/*intelligentia*; *pietas* →
    piety; the *vacare* dikaisune rule + `tr-vacare`, never "rest"; ruling 5 (*fundam.* in the apparatus; census the BUILT
    text); the purity triple **if** *pudicitia* is live (census at the shakedown; release per Sermones ruling 6 if zero);
    rulings 10, `tr-studium`, 21; the lemma = Douay adjusted to Quaracchi's Vulgate (ruling 5).
  - ***supplicium* → "penalty"** — Sap ruling 59 governs (the later ruling), not Eccl ruling 20.
  - **Title:** registry `title: "Commentarius in Evangelium S. Ioannis"` (half-title form; index *in Evangelium Ioannis*
    and running head *in Ioannem* recorded), English **"Commentary on the Gospel of John"**.
- **75. Registry and ids:** slug **`ioannem`**, id prefix **`bon-ioan-`**, **book 17**, tome 6, initial "I",
  `divisionLabel: "Capitula"`, divisions `0: Prooemium`, `1..21: Capitulum N`, `22: Scholion`, `23: Schemata`;
  `buildWorkChunkTitle`: add `ioannem` to the `ecclesiasten`/`sapientiam` branch (`Cap. N, Vers. a-b`). Goes in with
  `prooem` (division 0 only); each capitulum adds its own line after reading the heading in place.
- **76. Cadence = FOUR gates, ONE default deploy:** **shakedown at p. 268** (close of Cap. I, 13 chunks, ~30 pp — the whole
  Prologue register falls inside it) · **mid-work gate at p. 371** (close of Cap. VIII, ~103 pp) · **mid-work gate at
  p. 466** (close of Cap. XVI, ~95 pp) · **work-close gate at p. 532**. **ONE deploy, at p. 532, by default** (the Eccl
  amendment); **the two mid-work gates are legitimate deploy boundaries Wilson may call, per action.** Three gates
  (dropping p. 466) refused: cc. IX–XXI, 161 pp, reviewed only at the close.
- **77. Build cadence:** one Opus agent per chunk, incremental-append discipline from the start; the two-pass build only
  for a chunk that dies once or that the plate measures over ~10 pp (none predicted). Planning figure **~20–35 apparatus
  entries per pericope chunk** — a prompt to recount, never a gate. The session loop (repo CLAUDE.md § VOL VI — SESSION
  WORKFLOW) runs unchanged: one chunk, two commits, next chunk; STOP at each gate.
- **78. Hand additions in the scanned copy stay OUT of the apparatus (Wilson, 2026-10-18):** the p. 249 n. 7 tail `C.P I. Sent. d. 5. dub. 11.` (larger, irregular, hand-lettered) is excluded, its verbatim record in `bon-ioan-c1-v3-5`'s Notes stands (no edit to that chunk), and every later hand-lettered addition is likewise excluded and recorded verbatim in its chunk's Notes — never admitted on aptness.
- **79. *Ioannem* shakedown gate at p. 268 (Wilson, 2026-10-21, "Approve all" on the six-item docket in `vol6-ioannem-gate-evidence-sheet.md`) — TITLES.** (a) **Ruling 17 governs the headless pericopes of *Ioannem*:** `c1-v24-28`, `c1-v29-30`, `c1-v31-34` and `c1-v35-42` open with no printed heading, so `title_la` is the divisio's first sentence after the lemma (with the matching `title_en`), no opener heading is added, and each chunk's Notes cites ruling 17. The lemma-title default in the dispatch brief departed from ruling 17 and is withdrawn; the first sentence of Capitulum II's first chunk (`Postquam descripta est discipulorum vocatio…`, raw, unverified on the plate) falls under the same rule. The English titles carry ruling 74 as conformed in ruling 81 (*perhibuit* → "gave"). (b) **A stacked heading takes its LOWEST heading, whole (Sap ruling 47):** `c1-v43-51` is kept as built (*Prima manifestatio, quae est facta discipulis*), though that heading also names 2:1–11. A sentence title is used only where no heading stands. (c) **Leading ordinals are RESTORED** in the titles of `c1-v3-5` (*Secundo, de Verbo …* / "Second, on the Word …"), `c1-v15-18` (*Primo, de manifestatione Verbi incarnati in generali* / "First, …") and `c1-v19-23` (*Primo, de manifestatione per Ioannem* / "First, …"), as Eccl and Sap keep them (33 of 64 titles); the build had dropped them. The printed `Pars. I.` label stays out of `c1-v1-2`'s title.
- **80. PROVISIONAL CONVENTIONS (same sitting).** (a) ***virtus* is split by sense, ratified as built:** 9 "power", 11 "virtue", and *virtutem baptizandi* (`c1-v31-34` ¶ 71) stays "virtue" so *potestas* keeps "power" in the sentence that sets them side by side. (b) **"Holy Spirit" everywhere, Douay quotations included** (Vols I–IV have no "Holy Ghost"): `c1-v15-18` p. 254 n. 9 (Luke 1:15) conformed. (c) ***studium* is RELEASED in *Ioannem* from the one-root rule (Sap ruling 54)** and renders by context under the dikaisune rule, like *doctrina* and *vacare*: Sap ruling 54's reason (c8's heading is a proof inside an exhortation *ad studium*) belongs to *Sapientia*, and here n = 3 with no competing Latin word. Applied: `c1-v35-42` p. 264 n. 1 *humano studio* → "human effort"; `c1-v43-51` ¶ 94 *studio proficiendi* → "an eagerness to profit"; ¶ 79 *studiose* stays "studiously"; both `tr-studium` notes reworded to say the English takes the side by context (this removes "a study of profiting"). Ruling 74's carried `tr-studium` is read accordingly for this work only.
- **81. RULING 74 REGISTER CONFORMANCES (same sitting).** (a) ***testimonium perhibere* → "give testimony" throughout, in Bonaventure's own prose as already in the Douay:** the seven "bear" sites (`prol` p. 245 "testimonies are given"; `c1-v29-30` ¶ 61 ×2, ¶ 62; `c1-v31-34` ¶ 71 Quaest. IV; `c1-v35-42` ¶ 72, ¶ 83) and *perhibitio* "bearing" → "giving" (×3) conformed; *ferre testimonium* (¶ 71 *tulit*) keeps "bore", since the Latin sets it beside *perhibuit*. (b) ***doctor*:** `prooem` ¶ 4 "teacher" → "doctor" (and its `tr-doctrina` note's "of a teacher"); *magister* stays "teacher". (c) **I Tim. 6:16:** `c1-v3-5` ¶ 16 *habitat* → "dwelleth in light inaccessible" (the Douay adjusted to the print, as `c1-v15-18` already reads); the Vulgate note keeps "inhabiteth". (d) **Wis. 7:24 *munditiam* → "purity" is RATIFIED** (`c1-v9-14`): *pudicitia* has zero sites in the live region, so the purity triple is released for this work exactly as Vol V ruling 6 released it; the "cleanness" of `bon-sap-c7` is a recorded cross-work divergence, not a defect.
- **82. RESOLVER DOCKET AND HOUSEKEEPING (same sitting).** (a) **No text edit for the resolver docket;** its classes (the evidence sheet's § 5: bare book numeral restarting the book in a chain; bare `pag. N` of a non-Bonaventure book; *ibid.* bound across notes or to a bracketed verse; ordinal-word numerals; lost self-references; the work's own `n. N` form) and three items found at the gate (`prooem` p. 241 n. 3 `ibidem`; `c1-v15-18` p. 254 n. 8 `Cfr. ibid. XXV. c. 10. n. 25`; `prooem` p. 239 n. 1 `tertii Reg. 3, 12`) are one follow-up TOOL job, run after the gate and separately, the dangerous classes (wrong `chunk`, wrong book at confidence A/B) first. (b) `c1-v15-18` `verses` conformed to `"15-18"` (Eccl ruling 15, Sap ruling 50); the folded-in 1:14b stays in the chunk and is explained in its Notes. (c) The Douay adjustments disclosed for the gate (1:9 "illumines", 1:14 "dwelt in us", the three "Who was made before me", 1:25 "a prophet", 1:29 "sins", 1:37 "speaking", 1:39 "stayed there", 1:42 "Joanna", 1:46, 1:50, 1:51, *Nazaraeus* "Nazarite") are ratified as a block. (d) The index misses (*Vers. 35-42 » 262*; *Capitulum II » 268*) are recorded as the *Ioannem* analogue of Sap ruling 55 (index page = page of the first `(Vers. N.)` marker); the gate is named p. 268 although Cap. I closes four lines into p. 269. (e) Documentation: `c1-v43-51` has 46 numbered entries, not 45 (status line, Notes heading, resume). The optional *certitudinaliter* conformance was not in the docket and is not applied.
- **83. *munditia* IN WASHING PASSAGES → "cleanness" (Wilson, 2026-10-21, off the session's disclosures).** Where the passage is about washing or cleansing (`c4-v1-6` ¶ 9 and after: *aquam mundam* "clean water", *mundat* "cleanses", *immunditia* "uncleanness"), *munditia* takes "cleanness" so the English keeps one root. Ruling 81(d)'s "purity" stands for Wis. 7:24 and contexts with no cleansing figure. As built; no text change.
- **84. *magister Hugo* → "Master Hugh" (same sitting).** A title of a named doctor, like Lombard's "the Master" and as in Vol V; plain *magister* stays "teacher" (81(b)). As built (`c3-v3-12`); no text change.
- **85. BORDERLINE FAILING-IMPRESSION RESTORATIONS KEPT (same sitting).** `c3-v27-36` ¶ 59 *glori[a]m* and p. 288 n. 8 *e[x]hibetur* stay restored in brackets: faint flanking letters meet the rule, the readings are certain from sense, and the brackets disclose them. A gap narrower than the lost letter does not by itself put a site on the compositor's-blank branch.
- **86. MISPRINTS IN NAMES ARE MARKED, NOT CORRECTED, IN THE ENGLISH (same sitting).** `c4-v15-27` p. 294 n. 3 `Forceilini` → English "Forceilini [*so printed*]", matching *lueem* / *Galileam*; the silent correction to "Forcellini" was conformed. Proper names get no exception.

**The front after the rulings: `bon-ioan-prooem` (pp. 239–244)** — brief in the START HERE block of `next-session-resume.md`.

**The front after the gate rulings (2026-10-21): the first chunk of Capitulum II** (title per ruling 79: *Postquam descripta est…*).
