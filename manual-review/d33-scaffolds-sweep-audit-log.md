# d.33 scaffolds sweep audit log (2026-05-08)

Sweeps three "scaffold" (non-quaestio) chunks promoted/polish-cleared 2026-05-07:

- `vol1/bon-sent-I-d33-divisio.md` — pp. 569–570, raw lines 15352–15450, 6 apparatus entries
- `vol1/bon-sent-I-d33-littera.md` — pp. 567–569, raw lines 15062–15351, 19 apparatus entries
- `vol1/bon-sent-I-d33-dubia.md` — pp. 580–581, raw lines 16435–16584, 11 apparatus entries

Audit reference: raw OCR `raw/bonaventure_vol1_pt2_raw.txt`. PDF NOT consulted in this pass (audit-only; eyes-on PDF reserved for the d.31–d.40 polish-blocker pass).

## Method

- Verified frontmatter `line_start`/`line_end` by inspecting raw at the boundaries.
- Counted semantic markers (DISTINCTIO, Cap I/II, COMMENTARIUS, DIVISIO, TRACTATIO, ARTICULUS, DUB. I–IV) raw vs chunk.
- Diffed `## Latin` body against raw OCR for silent paraphrase or dropouts.
- Diffed every apparatus entry against the page-footer Notae blocks.
- Verified `[^N]` anchor positions match raw footnote markers.
- Counted inline `[?]` flags (none found in body; only in `transcription_status` description text).

## Per-chunk verdicts

### d33-divisio — VERDICT: CLEAN with two minor silent-insertion concerns

**Bounds**: raw 15352 = `COMMENTARIUS IN DISTINCTIONEM XXXIII.` ✓; raw 15448–15450 = `TRACTATIO QUAESTIONUM` listing of 4 quaestiones, immediately preceded by `ARTIGULUS UNICUS.` running-head which the chunk correctly excludes (belongs to a1 chunks). ✓

**Markers** (raw vs chunk):
- COMMENTARIUS heading: 1 / 1 ✓
- DIVISIO TEXTUS: 1 / 1 ✓
- TRACTATIO QUAESTIONUM: 1 / 1 ✓
- 4 enumerated quaestiones in tractatio (Primo/Secundo/Tertio/Quarto): 4 / 4 ✓

**Body**: Latin matches raw verbatim (modulo silent OCR cleanup: `delerminantur → determinantur`, `proprietatibus iii comparatione → in comparatione`, etc., all justified). English is literal, paragraph-parallel.

**Apparatus**: 6 entries claimed, 6 entries present. Spot-checks:
- [^1] `Codd. aa bb addunt *quae dicuntur*` — raw fn 1 ✓
- [^2] `Hi duo textus inveniuntur apud Aristot., I. *Elench.* c. **2**. (c. 1.).` — raw OCR shows `apud Aristot., I. Elench. c.` followed by column-flow breakage and later `(c. 1.).`. **The "2." is silently inserted** by the prior translator. The ambiguity log (`tier2-ambiguities-d33-divisio.md`) explicitly flags this and says "Resolve via 600 dpi PDF read." The current chunk renders the inferred reading as if verbatim. **Not fabrication of apparatus content (the entry exists); but a silent editorial fill of an OCR gap that should bear a `[?]`.**
- [^3] `Codd. I X aa bb cum ed. 1 *particulas*. Aliquanto inferius pro *distincta* **codd. aa bb *distinctiva***.` — raw OCR truncates at `pro distinc.ta codd.`; everything after is inferred. Same `[?]` flagging concern as [^2]. Ambig log explicitly says "the list of codices reading the variant for *distincta* is dropped" and marked `[?]` — but the chunk presents the reading as resolved.
- [^4]–[^6] match raw fn 4–6 verbatim ✓

**Recommendation**: defer correction to d.31–d.40 polish-pass (PDF eyes-on resolution). The two silent-insertion items are pre-existing, already logged, and within scope of the polish blocker.

### d33-littera — VERDICT: CLEAN; one editorial-gloss-in-La concern

**Bounds**: raw 15062 = `DISTINCTIO XXXIII.` opening of Cap. I ✓; raw 15351 ends mid-page-569 immediately before the COMMENTARIUS heading (line 15352). ✓

**Markers** (raw vs chunk):
- DISTINCTIO XXXIII: 1 / 1 ✓
- Cap. I (printed page 567 left column, OCR-garbled but recoverable): 1 / 1 ✓
- Cap. II (printed page 569 left column, garbled `Quomodo proprietates possint esse in natura Dei, nec eam determinent.` at raw line 15264): 1 / 1 ✓

**Body**: Latin tracks raw closely. Quoted Hilary, Jerome, Augustine passages preserved verbatim. Spot-check of the long Augustine-on-Psalm-68 passage (raw ~15300–15330 → chunk Cap. II second half): faithful.

**Apparatus**: 19 entries claimed, 19 entries present, anchor count matches. Page 568 footer = fns 1–11 (chunk [^1]–[^11]); page 569 footer = fns 12–19 (chunk [^12]–[^19]). Spot-checks:
- [^1] `Cfr. d. XXVI. c. 2, et d. XXVII. c. 1.` ✓
- [^4] `*Num.* 21. (n. = numerus, paragraph number; not biblical Numbers.)` — raw fn 4 = `Num. 21.` only. **The parenthetical gloss is editorial commentary embedded inside `**La.**`.** Per CLAUDE.md "verbatim Latin," translator gloss belongs in the `**En.**` field, not Latin. The English already carries the gloss. **Recommendation: strip the parenthetical from `**La.**`** to leave `*Num.* 21.` Restored gloss is preserved in `**En.**`.
- [^5] `*Num.* 40. Sequens locus VII. n. 22.` ✓
- [^14] `August. *Enarratio in Psalm.* 68, 3, sermo 1. n. 5.` ✓ (raw `n. S.` is OCR garble of `n. 5.`)
- [^15] page-569 fn 1 — raw text ends `et in cd. I congrue adiungitur` matches chunk verbatim ✓

**No silent body dropouts. No fabricated apparatus. No cross-chunk apparatus reuse.**

### d33-dubia — VERDICT: CLEAN

**Bounds**: raw 16435 = `DUBIA CIRCA LITTERAM M.^GISTRl.` ✓; raw 16584 ends in the page-581 footer block (footnotes 6–8 of page 581) just before line 16585 begins blank lines leading to `DISTINCTIO XXXIV.` heading at line ~16590. ✓

**Markers** (raw vs chunk):
- DUBIA CIRCA LITTERAM MAGISTRI: 1 / 1 ✓
- DUB. I: raw 16438 / chunk ✓
- DUB. II: raw 16487 / chunk ✓
- DUB. III: raw 16544 / chunk ✓
- DUB. IV: raw 16527 (printed `DuB. IV.` lowercase-u OCR variant, present in right column near the seam between DUB. III and DUB. IV reflow) / chunk ✓ — **NOT a silent dropout**, despite the polish-pass log's older note that "DUB IV header is missing from raw"; it is in fact present at raw 16527 with `DuB.` glyph variant.

**Body**: Latin matches raw verbatim across the four dubia. The DUB IV opening "Notandum super ista solutione Magistri quam ponit hic: *Nos autem ista aliter intelligenda fore dicimus*..." matches raw 16527–16533 verbatim. The chunk's reconstruction of the two-column DUB. III/IV reflow is consistent with raw column-flow.

**Apparatus**: 11 entries claimed, 11 present. Page-580 footer (DUB I) = chunk [^1]–[^3]; page-581 footer = chunk [^4]–[^11]. Spot-checks:
- [^1] `In multis codd. deest *ita*, pro quo cod. X et ed. 1 *ideo*` — raw verbatim ✓
- [^2] `Vat. hic et inferius *distinguit*.` ✓
- [^3] `Epist. I. Cor. 13, 12. — Paulo superius voculae *haec*...` — raw verbatim, full text preserved ✓
- [^5] `Supple cum cod. *Magister*.` ✓
- [^9] `Cod. B clarius sic: *quia licet ipsi recipiant revelationem a maioribus, tamen nobis non exprimunt*. Pro *quia ipsi* ed. 1 *quantum ipsi*. Ante *exprimunt* non pauci codd. cum edd. 2, 3, 4, 5, 6 falso omittunt *non*.` — raw verbatim ✓ (raw `!ulfO` = `falso` OCR garble silently fixed)
- [^11] `Hoc dubium solvunt etiam B. Albert., hic a. 9; S. Thom. et Richard., hic circa lit.` ✓

Polish-pass note in `tier2-ambiguities-d33-dubia.md` line 18 ("page-580 footnotes 1–4 belong to QUAESTIO IV scholion") **is incorrect** — the page-580 footer fns 1–3 ("In multis... deest ita", "Vat... distinguit", "Epist. I. Cor. 13, 12...") are dubia-content footnotes (their anchors are in DUB I body). No correction needed to chunk; the note is just a stale misreading of layout.

**No silent body dropouts. No missing dubia (all 4 present). No fabricated apparatus. No cross-chunk apparatus reuse.**

## Totals

| Chunk | Verdict | Body issues | Apparatus issues | Anchors balanced | Inline `[?]` |
|---|---|---|---|---|---|
| divisio | clean (minor) | 0 | 2 silent fills (entries [^2], [^3]) — already logged | 6/6 | 0 |
| littera | clean (minor) | 0 | 1 editorial gloss embedded in `**La.**` ([^4]) | 19/19 | 0 |
| dubia | clean | 0 | 0 | 11/11 | 0 |

## Anomalies

1. **divisio [^2], [^3]**: silent OCR-gap fills lacking `[?]` flag. Pre-existing; ambiguity log already records the open question. Within scope of d.31–d.40 polish-blocker (PDF eyes-on).
2. **littera [^4]**: editorial parenthetical `(n. = numerus, paragraph number; not biblical Numbers.)` is embedded inside `**La.**` field. Per CLAUDE.md `feedback_subagent-citation-discipline`, the *content* of the note (preventing biblical-Numbers misreading) is correct user-feedback-derived; the *placement* in `**La.**` (vs. `**En.**` only) is a verbatim-rule violation. Mechanical fix: move the parenthetical out of `**La.**`. Not fixed in this audit pass (no commits per task).
3. **dubia ambiguity-log misnote** (cosmetic): line 18 of `tier2-ambiguities-d33-dubia.md` misidentifies page-580 fns 1–3 as belonging to QUAESTIO IV scholion. They are dubia footnotes. No chunk-content impact.

## Build smoke-test

```
$ cd site && node scripts/build-content.mjs
Built content.json: 1 book(s), 422 questions, 350 translated
```

Build clean.

## Recommendation

No urgent rebuilds required. d.33 scaffolds are substantively faithful — no silent body dropouts (DUB IV verified present), no fabricated apparatus, no cross-chunk reuse, no Vat-variant inversion, no dubia missing. The three minor concerns (2 silent fills + 1 mis-placed gloss) are mechanical clean-ups appropriate for the d.31–d.40 polish-pass rather than emergency rework.
