# d.36 scaffolds sweep audit log — 2026-05-08

Scope: `vol1/bon-sent-I-d36-{littera, divisio, a1-q1, a1-q2, a2-q1, a2-q2, a3-q1, a3-q2, dubia}.md` (9 chunks). Goal: verify chunk bounds, diff Latin against pt2 raw OCR, diff/build apparatus, fix paraphrase, never invent Latin or fabricate apparatus.

Source: `raw/bonaventure_vol1_pt2_raw.txt`. Pt2 PDF offset = printed − 410.

Context: d.36 was promoted to Tier-2 on 2026-05-07 (all nine chunks built fresh from OCR with bilingual `**La.**`/`**En.**` apparatus and literal English). The d.31–d.40 polish-blocker `[?]`-resolution pass (Pass A, session 3) ran 2026-05-07 and cleared 26 d.35/d.36 flag-pairs (with 1 accepted-illegible Greek excerpt and 4 documented structural anomalies); full disposition logged in `d31-d40-polish-resolution-log.md`, with d.36-specific items carried forward to `d31-d40-residual-backlog.md`. This sweep audits the post-polish state for silent paraphrase, fabricated apparatus, body omissions, cross-chunk reuse, and Vat-variant inversion.

The user prompt referenced "divisio, littera, dubia" as example chunks. Actual d.36 chunk inventory contains 9 files (all 6 articulus-quaestio chunks plus those 3); audit covers all 9.

## Boundary tile-out

| Chunk | line_start | line_end | OCR landmark above | OCR landmark at end |
|---|---|---|---|---|
| littera | 19951 | 20156 | `DISTINCTIO XXXVI.` at 19951 | `DIST. XXXVl. DIVISIO TEXTUS.` page-running-head at 20158, then `COMMENTARIUS IN DISTINCTIONEM XXXVI.` at 20165 |
| divisio | 20165 (+ 20507–20520) | 20520 | `COMMENTARIUS IN DISTINCTIONEM XXXVI.` at 20165 | a2 `ARTICULUS 11.` (OCR) at 20507; ART II preamble (lines 20507–20520) is rolled into the divisio per chunk-build convention for multi-articulus distinctions |
| a1-q1 | 20242 | 20414 | `ARTICULUS I.` at 20242 | `QUAESTIO II.` (a1-q2 start) at 20415 |
| a1-q2 | 20415 | 20505 | `QUAESTIO II.` at 20415 | `ARTICULUS 11.` at 20507 (preamble pulled into divisio; q2 body proper ends at 20505) |
| a2-q1 | 20546 | 20752 | `QUAESTIO I.` (under ART II preamble) at 20546 | `QUAESTIO II.` (a2-q2 start) at 20753 |
| a2-q2 | 20753 | 20868 | `QUAESTIO II.` at 20753 | `ARTICULUS III.` at 20869 |
| a3-q1 | 20869 | 21105 | `ARTICULUS III.` at 20869 | `QUAESTIO 11.` (a3-q2 start) at 21106 |
| a3-q2 | 21106 | 21262 | `QUAESTIO 11.` at 21106 | dubia opener "In parte ista sunt dubitationes circa litteram" at 21263 |
| dubia | 21263 | 21451 | dubia opener at 21263 | `DISTINCTIO XXXVII.` at 21452 |

Bounds tile cleanly across the d.36 raw range (19951–21451) with no overlap and no gap. The divisio's split-range (20165–20231 + 20507–20520) is documented in the chunk's `transcription_status` and is the standard treatment for the Bonaventure two-stage divisio (DIVISIO TEXTUS + TRACTATIO QUAESTIONUM at front of the distinction, then ART. II preamble after q1 body); both ranges are covered in the chunk file.

The littera frontmatter `printed_pages` was corrected during the 2026-05-07 build from `[615, 616, 617]` to `[617, 618]` after eyes-on PDF check; that correction is sustained.

## Apparatus-count parity

Per-chunk apparatus-definition count (`grep -cE "^\[\^[0-9]+\]:"`) versus the count declared in `transcription_status`:

| Chunk | declared | actual | parity |
|---|---|---|---|
| littera | 21 | 21 | ✓ |
| divisio | 4 | 4 | ✓ |
| a1-q1 | 14 | 14 | ✓ |
| a1-q2 | **13** | **9** | ✗ count drift in status string |
| a2-q1 | 17 | 17 | ✓ |
| a2-q2 | 8 | 8 | ✓ (but see anchor-reuse note below) |
| a3-q1 | 13 | 13 | ✓ |
| a3-q2 | 11 | 11 | ✓ |
| dubia | 16 | 16 | ✓ |

Anchor-occurrence parity (each apparatus marker should appear 3 times: once in Latin body, once in English body, once as `[^N]:` definition):

- All 9 chunks pass the `3×` parity check **except `a2-q2`**, where `[^1]` appears 5 times (1 La body in obj. 1 + 1 En body in obj. 1 + 1 La body in respondeo "Augustinus de Trinitate" + 1 En body in respondeo "Augustine *On the Trinity*" + 1 def). All other anchors `[^2]–[^8]` appear cleanly 3×.

This `a2-q2` anchor-reuse is the same defect formally documented as item B in `d31-d40-residual-backlog.md`:

> **d.36 a2-q2 missing body anchors for fns 4, 6, 7** — printed p. 624 anchors on body words; chunk's `[^4]/[^6]/[^7]` defs hold different content, mis-mapped.

In effect, the printed Quaracchi p. 624 has its own footnote sequence (1, 2, 3 …) starting fresh from page 623 (1–8); the chunk-builder collapsed both pages into a single 1–8 sequence and reused `[^1]` in the second-page body. The result is that the def block holds the page-623 1–8 notes; the page-624 fresh `1` (cited at "de Trinitate") is *not* present in the apparatus block as a distinct entry, and the body-anchor for it is misrouted to `[^1]`. Resolving this requires either (a) renumbering the d.36-a2-q2 apparatus to reflect both pages' note streams (which would knock-on body anchors), or (b) inserting the page-624 entries (Vat./codex variants on `de Trinitate`, `quod sunt sed`, `voluntate`, `comparatione`, etc., not transcribed in the present chunk apparatus) and re-anchoring the body. Either is a focused single-chunk rebuild, not a sweep-scope edit. Carried forward; not addressed here per "Commit nothing".

## Per-chunk verdicts

### bon-sent-I-d36-littera.md — PASS (no changes)

- **Bounds**: 19951–20156 verified. `DISTINCTIO XXXVI.` opens at 19951; the divisio running head + `COMMENTARIUS` headers begin at 20158/20165.
- **Latin body**: pp. 617–618. Five Lombard chapters (Capp. I–V) verbatim against OCR. Block-quotes from Augustine (sermo 26, *de Praedest. Sanctorum*, *de Natura Boni* 27 & 28, *de Trin.*), Cassiodorus, Ambrose (*de Spir. Sancto* III) all reflowed cleanly from the two-column footer/body band; OCR column-mixing was disambiguated against the 300-dpi pt2 PDF (printed pp. 617–618 = PDF pp. 207–208) per the chunk's `transcription_status` note. Page break `<!-- page 618 -->` placed at the OCR boundary (`Si ad scientiam | referas`).
- **Apparatus**: 21 bilingual entries. Status declares "21 entries (10 from p. 617 footer + 11 from p. 618 footer, renumbered consecutively)" — count matches. Entry [^10] carries the documented `[?]` flag on the Augustine-*ad Helvidium*/*Evodium* discussion; that flag is the polish-pass accepted-as-documented item, sustained.
- **English**: literal, paragraph-for-paragraph. Quaracchi `«…»` rendered as `«…»` in Latin and `« … »` in English. Vulgate citations (Eph. 1:4; Rom. 11:36; Pss. 137, 16, 74; Matt. 7:23; Luke 13:27; Acts 17:28) rendered with chapter:verse.
- **Verdict**: clean. No edits.

### bon-sent-I-d36-divisio.md — PASS (no changes)

- **Bounds**: 20165–20231 + 20507–20520 verified. `COMMENTARIUS IN DISTINCTIONEM XXXVI.` at 20165; `ARTICULUS 11.` at 20507; ART II preamble (Consequenter…secundo articulo…duo) lines 20507–20520 are the standard rolled-in slice.
- **Latin body**: verbatim against OCR. The leading `*Solet hic quaeri*` epigraph is preserved as the question-marker. `TRACTATIO QUAESTIONUM` block is included per chunk-build convention. Italics on internal references (`Proinde, si diligenter inspiciamus`; `Praeterea sciendum est`; `Illud etiam hic animadvertendum est`; `Ex praemissis apertum est`; `ex ipso`/`per ipsum`) preserved.
- **Apparatus**: 4 bilingual entries, each verbatim against the p. 619 footer band visible at OCR lines 20226–20231:
  - `[^1]`: *Pro In secunda plurimi codd. Secundo.*
  - `[^2]`: *Pro dicto codd. PQV est; in non paucis codd. neque dicitur neque est.*
  - `[^3]`: *Cod. T attendendum.*
  - `[^4]`: *Cod. V universalitatem. Paulo post pro cognoscit Vat. cod. cc praecognoscit.*
- **English**: literal.
- **Verdict**: clean. No edits.

### bon-sent-I-d36-a1-q1.md — PASS (no changes)

- **Bounds**: 20242–20414 verified. `ARTICULUS I.` at start; q2 (`QUAESTIO II.`) starts at 20415.
- **Latin body**: pp. 620–621 verbatim. Three pro-fundamenta + four contra arguments + Conclusio + Respondeo + 4 ad-replies + 3-section Scholion. Anchor positions match OCR-marker positions (e.g. `quam penes se habet[^1]`, `produclum a re[^2]`, `sed alicuius[^3]`, `agentis[^4]`, `nec ibi[^5]`, `essentia rei esset in Deo[^6]`, `vel[^7] potentiale`, `impossibile[^8]`, `in sua causa[^9]`, `primum modum existendi[^10]`, `est in aliquo[^11]`, `ratione exemplaris[^12]`, `possibile[^13]`, `in Deo[^14]`).
- **Apparatus**: 14 bilingual entries. Entry `[^3]` carries the Aristotle Greek excerpt `καὶ γὰρ τὸ χωριστὸν…` with one accepted-illegible `[?]` glyph after `οὐσίᾳ`; this is the documented polish-pass item (matches `d31-d40-residual-backlog.md` item A: `d.36 a1-q1 [^3] Aristotle Greek excerpt — same disposition as d.31 p2-a1-q2 [^8]`).
- **Scholion**: three sections (I, II, III), commentator-list (Alex. Hal., Scotus, S. Thom., B. Albert., Petr. a Tar., Richard. a Med., Ægid. R., Durand., Dionys. Carth., Biel) preserved in full, parallel-translated.
- **English**: literal.
- **Verdict**: clean. No edits.

### bon-sent-I-d36-a1-q2.md — PASS WITH MINOR STATUS CORRECTION

- **Bounds**: 20415–20505 verified. `QUAESTIO II.` at start; `ARTICULUS 11.` at 20507 (preamble lifted into divisio).
- **Latin body**: p. 622 verbatim. Three pro-fundamenta + three contra arguments + Conclusio + Respondeo + ad-replies. Polish-pass clean-ups: `tribus, patet etc.` (the residual-backlog `tribus[?]...` truncation flagged in audit candidate C is sustained as cleaned text — confirmed at chunk line 39).
- **Apparatus**: **9** bilingual entries `[^1]–[^9]`, all 3×-anchor-balanced. **`transcription_status` declares "13 entries"** — descriptive frontmatter inaccuracy. The actual 9 entries appear content-complete and OCR-grounded (spot-checked `[^4]`, `[^7]`, `[^9]` against OCR p. 622 footer band).
- **English**: literal.
- **Verdict**: clean content. **One descriptive frontmatter fix recommended: `(13 entries)` → `(9 entries)` in `transcription_status`.** Not a parse blocker; not applied per "Commit nothing".

### bon-sent-I-d36-a2-q1.md — PASS (no changes)

- **Bounds**: 20546–20752 verified. `QUAESTIO I.` (under the 20507 `ARTICULUS II.` preamble) at 20546.
- **Latin body**: pp. 622–623 verbatim. Fundamenta/contra block, Conclusio, Respondeo, replies, plus three-section Scholion.
- **Apparatus**: 17 bilingual entries `[^1]–[^17]`, anchors balanced 3× across La/En/def. Status "17 entries" matches.
- **English**: literal.
- **Verdict**: clean. No edits.

### bon-sent-I-d36-a2-q2.md — PASS WITH STRUCTURAL FLAG (deferred per residual backlog)

- **Bounds**: 20753–20868 verified. `QUAESTIO II.` at 20753; `ARTICULUS III.` at 20869.
- **Latin body**: pp. 623–624 verbatim. Four pro-fundamenta + three contra + Conclusio + Respondeo (across page break) + three replies + two-section Scholion. Body content is OCR-grounded; spot-check at OCR lines 20800–20810 (the `Adhuc similitudines rerum in intellectu creato verius et nobilius habent esse quam res in universo, ut dicit Augustinus de Trinitate¹` clause) confirms verbatim transcription.
- **Apparatus**: 8 bilingual entries `[^1]–[^8]`. **Anchor `[^1]` is reused 2× in body** (once in obj. 1 for Augustine *Genes. ad lit.* V c. 13 n. 33; once in respondeo for Augustine *de Trin.*). The `[^1]` def block holds only the *Genes. ad lit.* citation. The page-624 fresh-numbered footnotes — Quaracchi prints a new 1, 2, 3, … sequence starting from p. 624 col-a for the second-page anchors — are **not** present in the chunk's apparatus. This is the polish-pass / residual-backlog item B "d.36 a2-q2 missing body anchors for fns 4, 6, 7"; the precise diagnosis is now visible to be **page-stream collapse + reuse of `[^1]`**. The OCR-visible page-624 footer band is fragmentary and would need 600-dpi PDF eyes-on to resolve cleanly.
- **English**: literal, parallel.
- **Scholion**: two sections (I, II), commentator-list intact.
- **Verdict**: content is OCR-grounded; structural anchor mis-mapping is **deferred per the documented residual-backlog item**, not addressed here. Mark: PASS (content) / DEFERRED (structure).

### bon-sent-I-d36-a3-q1.md — PASS (no changes)

- **Bounds**: 20869–21105 verified. `ARTICULUS III.` at start.
- **Latin body**: pp. 625–627 verbatim. Polish-pass clean-up `per positionem; sed malum` (the residual-backlog item C column-wrap split) is sustained inside `[^12]` (chunk line 198): the long codex-O variant reads `…cognosci per se et per positionem; sed malum per se nec causam nec voluntatem…` continuously, no asterisk-bracket residue.
- **Apparatus**: 13 bilingual entries, anchors balanced 3×. Status "13 entries" matches.
- **English**: literal.
- **Verdict**: clean. No edits.

### bon-sent-I-d36-a3-q2.md — PASS (no changes)

- **Bounds**: 21106–21262 verified. `QUAESTIO 11.` at 21106; dubia preamble at 21263.
- **Latin body**: pp. 628–630 verbatim. Fundamenta + contra + Conclusio + Respondeo + replies + Scholion sections, all present.
- **Apparatus**: 11 bilingual entries, anchors balanced 3×. Status "11 entries" matches.
- **English**: literal, parallel.
- **Verdict**: clean. No edits.

### bon-sent-I-d36-dubia.md — PASS (no changes)

- **Bounds**: 21263–21451 verified. `In parte ista sunt dubitationes circa litteram` opener at 21263; `DISTINCTIO XXXVII.` (next chunk) at 21452. Three or more dubia (DUB. I, II, III evident at OCR markers around 21321 and 21377) all present in chunk body.
- **Latin body**: pp. 630–632 verbatim against OCR.
- **Apparatus**: 16 bilingual entries, anchors balanced 3×. Status "16 entries" matches.
- **English**: literal.
- **Scholion**: per `has_scholion: false`, none expected.
- **Verdict**: clean. No edits.

## Totals

| Chunk | Verdict | Apparatus entries | Body `[?]` flags | Notes |
|---|---|---|---|---|
| littera | PASS | 21 | 1 (in [^10], doc'd) | clean |
| divisio | PASS | 4 | 0 | clean |
| a1-q1 | PASS | 14 | 1 (Greek in [^3], doc'd accept-illegible) | clean |
| a1-q2 | PASS w/ status fix | 9 | 0 | status "13 entries" → actually 9 (descriptive) |
| a2-q1 | PASS | 17 | 0 | clean |
| a2-q2 | PASS content / DEFER struct | 8 | 0 | `[^1]` reused 2× in body; p. 624 notes absent — residual-backlog item B |
| a3-q1 | PASS | 13 | 0 | column-wrap fix sustained |
| a3-q2 | PASS | 11 | 0 | clean |
| dubia | PASS | 16 | 0 | clean |
| **TOTAL** | **9 PASS / 0 FAIL** | **113** | **2 (both doc'd)** | |

## Anomalies

1. **Frontmatter `transcription_status` apparatus-count drift in `a1-q2`**: declares "13 entries", actual 9. Descriptive string only (parser does not act on it). The 9 entries are content-complete and OCR-grounded. Suggested one-line frontmatter polish in a future cleanup. **Not applied here per "Commit nothing".**

2. **`a2-q2` anchor reuse (`[^1]` × 5 occurrences) — page-stream collapse**: as logged in `d31-d40-residual-backlog.md` item B and refined here, the chunk merges the two printed pages' (p. 623 and p. 624) independent footnote-numbering streams into a single 1–8 sequence and reuses `[^1]` for the page-624 first anchor (Augustine *de Trin.* in respondeo "Adhuc similitudines"). The page-624 footnote definitions (Vat./codex variants for the second page) are absent from the apparatus block. Resolution requires either renumbering or inserting fresh entries; both are single-chunk rebuilds out of sweep-audit scope. **Deferred to the formal residual-backlog item.**

3. **No silent paraphrase, no fabricated apparatus, no body omissions, no Vat-variant inversions, and no cross-chunk reuse** detected across the 9 chunks. Latin bodies are verbatim against `raw/bonaventure_vol1_pt2_raw.txt` lines 19951–21451 (with the divisio's documented split range 20165–20231 + 20507–20520). The two `[?]` flags remaining (littera `[^10]` Augustine *Helvidium/Evodium*; a1-q1 `[^3]` Greek `οὐσίᾳ` excerpt) are both formally accepted-as-documented in the polish-blocker pass.

## Build smoke-test

`cd site && node scripts/build-content.mjs`:

```
Built content.json: 1 book(s), 422 questions, 350 translated
```

Clean.

## Disposition

- **All 9 d.36 chunks PASS the sweep on content fidelity.** No file edits required.
- One descriptive-frontmatter inaccuracy catalogued (`a1-q2` "13 entries" → 9) for future polish.
- One structural anchor mis-mapping (`a2-q2`) carried forward to `d31-d40-residual-backlog.md` item B; not addressed in sweep scope.
- No backups created (no substantive edits made; the `_backup-d36-...` directory referenced in the prompt template was not pre-existing and was not generated since no rebuilds occurred).
- Nothing committed.
