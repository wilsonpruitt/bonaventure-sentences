# d.32 scaffolds sweep audit log — 2026-05-08

Scope: `vol1/bon-sent-I-d32-{divisio, littera, a1-q1, a1-q2, a2-q1, a2-q2, dubia}.md` (7 chunks). Goal: verify chunk bounds, diff Latin against pt2 raw OCR, diff/build apparatus, fix paraphrase, never invent Latin or fabricate apparatus.

Source: `raw/bonaventure_vol1_pt2_raw.txt`. Pt2 PDF offset = printed − 410.

Context: d.32 was promoted to Tier-2 on 2026-05-06 (all seven chunks built fresh from OCR with bilingual `**La.**`/`**En.**` apparatus and literal English). The d.31–d.40 polish-blocker `[?]`-resolution pass (Pass A) ran 2026-05-07 and cleared 16 d.32 flags (resolved) plus 1 accepted-as-documented; full disposition logged in `d31-d40-polish-resolution-log.md`. This sweep audits the post-polish state for silent paraphrase, fabricated apparatus, body omissions, and bound integrity.

## Boundary tile-out

| Chunk | line_start | line_end | OCR landmark above | OCR landmark at end |
|---|---|---|---|---|
| littera | 13570 | 13859 | `DISTINCTIO XXXII.` at 13570 | divisio `COMMENTARIUS IN DISTINCTIONEM XXXII.` at 13860 |
| divisio | 13860 | 13946 | `COMMENTARIUS IN DISTINCTIONEM XXXII.` at 13860 | a1-q1 `ARTICULUS I.` boundary |
| a1-q1 | 13947 | 14246 | `ARTICULUS I. QUAESTIO I.` | running head `DIST. XXXII. ART. l. QUAEST. II.` at 14191 (next chunk start ~14247) |
| a1-q2 | 14247 | 14434 | `QUAEST. II.` | a2 `ART. II. QUAEST. I.` running head at 14379 (chunk tail 14434) |
| a2-q1 | 14435 | 14644 | `ARTICULUS II. QUAESTIO I.` | next quaestio start ~14645 |
| a2-q2 | 14645 | 14825 | `QUAESTIO II.` | dubia start ~14826 |
| dubia | 14826 | 15061 | `DUBIA CIRCA LITTERAM MAGISTRI.` | `DISTINCTIO XXXIII.` at 15062 |

Bounds tile cleanly across the d.32 raw range (13570–15061) with no overlap and no gap. The dubia note in transcription_status flags a 2026-05-06 column-bleed correction (originally clipped at 15017; extended to 15061 to capture DUB. VI–VII, with 7 new apparatus entries `[^16]–[^22]`); that fix is intact in the chunk.

## Per-chunk verdicts

### bon-sent-I-d32-littera.md — PASS (no changes)

- **Bounds**: 13570–13859 verified. `DISTINCTIO XXXII.` at 13570; `COMMENTARIUS IN DISTINCTIONEM XXXII.` (next chunk's head) at 13860.
- **Latin body**: 6 capitula (I–VI) verbatim against OCR pp. 553–556. Quaracchi italics preserved (`*Notula*`, `*Epilogus*`, `*Difficilis quaestio*`, `*Quaestionem relinquit*`); long Augustine/Hilary block-quotes reflowed cleanly from the two-column footer band. Page breaks (`<!-- page 553 -->` … `<!-- page 556 -->`) at correct paragraph boundaries.
- **Apparatus**: 15 bilingual `**La.**`/`**En.**` entries. Entry `[^11]` (Hilary *de Trin.* IX) carries the documented `[Quaracchi quotation truncated mid-clause; remainder not transcribed in this chunk.]` annotation, in lieu of a fabricated continuation; this disposition was logged in the polish pass and remains correct (the printed Quaracchi text genuinely ends mid-clause). Entry `[^15]` carries the explicit `(n. = numerus, paragraph number; not biblical Numbers.)` discipline-note.
- **English**: literal, paragraph-for-paragraph parallel; scholastic-formula vocabulary consistent with project glossary (`Praeterea` → "Furthermore"; `Difficilem esse mihi fateor` → "I confess … to be especially difficult to me").
- **transcription_status**: dated 2026-05-06; mentions "12 entries" — actual count is 15. **Frontmatter inaccuracy** (descriptive only; not a parse blocker).
- **Verdict**: clean. No edits.

### bon-sent-I-d32-divisio.md — PASS (no changes)

- **Bounds**: 13860–13946 verified. `COMMENTARIUS IN DISTINCTIONEM XXXII.` at 13860; first `Articulus I.` body opens 13947.
- **Latin body**: verbatim against OCR. The polish pass's `*se* [?] *ipso*` → `*se ipso*` join is correctly applied. `TRACTATIO QUAESTIONUM` block (Lombard's chapter list) is included in the divisio per chunk-build convention. Page breaks `<!-- page 555 -->` and `<!-- page 556 -->` at correct positions.
- **Apparatus**: 6 bilingual entries. Per-entry attachments to body words (`tres`/`scilicet`/`sapiens`/`affirmativam`/`sapientia`/`Difficillimam mihi hanc fateor quaestionem`) match OCR. The `manual-review/tier2-ambiguities-d32-divisio.md` log notes that several Vat./codex variants in `[^4]` and `[^5]` are likely Lombard-littera variants now captured in the d.32-littera chunk (which was promoted on the same day) — that observation remains an open re-attribution candidate but does not constitute fabrication; the apparatus entries verbatim transcribe the printed Quaracchi notes from the p. 555/556 footer band.
- **English**: literal, with quotation marks `«…»` → `"…"`. Locutions in italics preserved.
- **Notes**: ends with the documented "NOTAE AD COMMENTARIUM" provenance comment in `## Notes`.
- **transcription_status**: 2026-05-06; matches structure.
- **Verdict**: clean. No edits.

### bon-sent-I-d32-a1-q1.md — PASS (no changes)

- **Bounds**: 13947–14246 verified. `ARTICULUS I.` at start; `QUAEST. II.` (next chunk) running-head emerges at line 14191 (within the page-557 scholion footer column-flow), and `Quaestio II` proper starts at the OCR boundary that the next chunk picks up.
- **Latin body**: pp. 555–557 verbatim. Spot-check at OCR line 14163: chunk's `obliquus[^2] construitur reciproce` matches `obliquus^ construitur reciproce` (the polish pass had repositioned this anchor and removed `[?]`). Six fundamenta + six contra arguments + Conclusio + Respondeo + Ad-arg block + 3-section Scholion — all present, none paraphrased.
- **Apparatus**: 13 bilingual entries `[^1]–[^13]`. Entry `[^13]` is the long Priscian-citation grammatical note on reciprocal/retransitive construction — verbatim against OCR p. 557 col-b.
- **Scholion**: three sections (I, II, III) with full commentator-list (Alex. Hal., Scotus, S. Thom., Albert., etc.) — present and parallel-translated, NOT condensed.
- **English**: literal. Long Hugh-of-St-Victor `«»` quotation in fundamentum 4 preserved with internal punctuation.
- **transcription_status**: 2026-05-06; states "13 entries" — matches actual count.
- **Verdict**: clean. No edits.

### bon-sent-I-d32-a1-q2.md — PASS (no changes)

- **Bounds**: 14247–14434 verified.
- **Latin body**: pp. 559–561 verbatim. Five fundamenta + five contra arguments + Conclusio + Respondeo + Ad-arg block — none paraphrased. Polish-pass clean-ups (`Magistri Simonis Tornacensis`, `Unde Hugo:`, `Filio non appropriatur` etc.) all sustained without `[?]` residue.
- **Apparatus**: 8 bilingual entries `[^1]–[^8]`. Entry `[^8]` carries the long Richard-of-St-Victor `Quomodo Spiritus sanctus est amor Patris et Filii` block-quotation, reflowed verbatim from the OCR footer band (printed p. 561 col-b). No fabrication.
- **English**: literal; "love" / "lover" / "by-which" terminology consistent.
- **Scholion**: none (matches `has_scholion: false`).
- **transcription_status**: 2026-05-06; "8 entries" — matches.
- **Verdict**: clean. No edits.

### bon-sent-I-d32-a2-q1.md — PASS WITH MINOR STATUS CORRECTION

- **Bounds**: 14435–14644 verified. `ARTICULUS II.` heading at start.
- **Latin body**: pp. 561–563 verbatim. Polish-pass clean-ups (`aut sicut subiecti`, `obliquus construitur reciproce`, etc.) sustained. Page-break inline `<!-- page 563 -->` correctly placed mid-paragraph at `praepositio *in* cum suo casuali ... <!-- page 563 -->praepositio` to match the printed Quaracchi col-b break.
- **Apparatus**: **14** bilingual entries `[^1]–[^14]`. **transcription_status declares "17 entries" — frontmatter inaccuracy.** All 14 entries are content-complete and verbatim from the OCR footer band; spot-check `[^13]` (Aristotle *de Anima* III + *Metaph.* VI cross-ref) is the long entry, present in full. No missing apparatus that I can identify against pp. 561–563 footer marker positions in OCR (markers 1–14 fully accounted for; the OCR markers `15`/`16`/`17` do not appear at marker positions inside the chunk's body line range).
- **Scholion**: three sections (I, II, III), commentator-list intact.
- **English**: literal, parallel.
- **Verdict**: clean content. **One descriptive frontmatter fix recommended: `(17 entries)` → `(14 entries)` in `transcription_status`.** Not a parse blocker; non-substantive. Per the prompt instruction "Commit nothing", I am NOT applying this edit; logging here for future polish.

### bon-sent-I-d32-a2-q2.md — PASS (no changes)

- **Bounds**: 14645–14825 verified. `Quaestio II` at start.
- **Latin body**: pp. 563–564 verbatim. Polish-pass clean-ups (`magis debeat dici`, `Idem est me potentem quod me`, `Filio non appropriatur`) sustained. Page break at `<!-- page 564 -->`.
- **Apparatus**: 10 bilingual entries `[^1]–[^10]`. Entry `[^9]` (Aristotle *de Caelo* I, with Greek excerpt `Ἡ δὲ δύναμις τῆς ὑπεροχῆς ἐστιν` and St. Thomas's lect. 25 gloss) is the substantial one — verbatim against OCR. Entry `[^10]` (Hilary on Ps. 137 + Augustine *Enarrat.* on Ps. 43 + the codd. F l aa bb additional Hugh quotation) is fully reflowed from the multi-line OCR footer.
- **English**: literal.
- **Scholion**: two sections (I, II), commentator-list intact.
- **transcription_status**: 2026-05-06; "10 entries" — matches.
- **Verdict**: clean. No edits.

### bon-sent-I-d32-dubia.md — PASS (no changes)

- **Bounds**: 14826–15061 verified. `DUBIA CIRCA LITTERAM MAGISTRI` heading at start; `DISTINCTIO XXXIII.` at 15062 (next chunk's head, outside this chunk).
- **Latin body**: pp. 565–567. Seven dubia (DUB. I–VII), all present. The 2026-05-06 column-bleed correction (DUB. VI–VII appended after originally clipping at line 15017) is sustained — both DUB. VI (Hilary on John 14 / John 8 reduction-ad-impossibile) and DUB. VII (genitive-construction analysis) are present and verbatim, with the page-break `<!-- page 567 -->` at the correct DUB. VI/VII boundary.
- **Apparatus**: 22 bilingual entries `[^1]–[^22]`. Entry `[^4]` is the long Anselm `de Fide Trinitatis et de incarnatione Verbi` block — quoted from Alex. Hal. *S.* p. I. q. 67. m. 1, verbatim. Entries `[^16]–[^22]` (the post-correction additions) are content-complete and OCR-grounded; spot-check `[^17]` (John 14:10 with Vulgate variant `autem`/`in`/`enim` notation) and `[^18]` (John 8:29 with Vulgate `mecum est et` insertion) match the printed Quaracchi footer notes.
- **English**: literal, parallel paragraph-for-paragraph.
- **Scholion**: none (correct: `has_scholion: false`).
- **transcription_status**: 2026-05-06; descriptive of the column-bleed correction.
- **Verdict**: clean. No edits.

## Totals

| Chunk | Verdict | Apparatus entries | Body `[?]` flags | Notes |
|---|---|---|---|---|
| littera | PASS | 15 | 0 | status says "12 entries" — descriptive inaccuracy |
| divisio | PASS | 6 | 0 | re-attribution candidates noted in pre-existing ambiguities log |
| a1-q1 | PASS | 13 | 0 | clean |
| a1-q2 | PASS | 8 | 0 | clean |
| a2-q1 | PASS w/ minor status fix | 14 | 0 | status says "17 entries" — descriptive inaccuracy |
| a2-q2 | PASS | 10 | 0 | clean |
| dubia | PASS | 22 | 0 | column-bleed correction sustained; DUB. VI–VII present |
| **TOTAL** | **7 PASS / 0 FAIL** | **88** | **0** | |

## Anomalies

1. **Frontmatter `transcription_status` apparatus-count inaccuracies (2 of 7 chunks)**:
   - `bon-sent-I-d32-a2-q1.md` — declares "17 entries", actual 14.
   - `bon-sent-I-d32-littera.md` — declares "12 entries", actual 15.

   These are descriptive strings only (the parser does not act on them). Both apparatus blocks are content-complete and OCR-grounded; the count mismatches are bookkeeping drift from the 2026-05-06 build (likely rough-counted or stale post-edit). Suggest a one-line frontmatter polish in a future cleanup. **Not applied here per "Commit nothing" instruction.**

2. **Pre-existing `manual-review/tier2-ambiguities-d32-divisio.md` re-attribution flags (items 4, 5)**: notes three apparatus entries (`[^3]`, `[^4]`, `[^5]`) whose Vatican/codex-variant attachments are likely to Lombard littera body-words, not to the divisio. The polish-blocker pass on 2026-05-07 confirmed the entries' Latin content is OCR-correct and resolved the trailing-`[?]` formatting hedge, but did not formally re-attach them to the d.32 littera (which was being promoted in parallel). Outcome: the apparatus is content-correct in both chunks, but the *attachment locus* of these three editorial-variant notes within the divisio is best-guess. This is a structural anomaly (not a fabrication) and is appropriately documented in the per-chunk ambiguities log; carry forward to a future cross-chunk reconciliation pass.

3. **No paraphrase, no fabricated apparatus, no body omissions, no Vat-variant inversions detected.**

## Build smoke-test

`cd site && node scripts/build-content.mjs`:

```
Built content.json: 1 book(s), 422 questions, 350 translated
```

Clean.

## Disposition

- **All 7 d.32 chunks PASS the sweep.** No file edits required.
- Two non-blocking descriptive-frontmatter inaccuracies catalogued for future polish.
- Pre-existing divisio-apparatus re-attribution candidates remain as documented in `tier2-ambiguities-d32-divisio.md`; not addressed here.
- No backups created (no substantive edits made).
- Nothing committed.
