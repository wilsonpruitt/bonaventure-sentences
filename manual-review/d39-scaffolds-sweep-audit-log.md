# d.39 scaffolds sweep audit log

**Date**: 2026-05-08
**Scope**: re-audit `vol1/bon-sent-I-d39-{divisio, littera, dubia}.md` after the 2026-05-07 [?]-pass polish-audit (d.39 a1-q2 Sch II had a wholesale fabrication caught + fixed during polish; the three scaffold-class chunks are now re-checked for silent paraphrase / cross-chunk reuse / fabricated apparatus the [?]-pass might not have surfaced).

Per the dispatcher brief: every chunk gets bounds-vs-raw verification, semantic-marker count diff, full Latin-body diff against raw OCR pt2, and apparatus-vs-OCR-footer diff.

## Anchor / def pairing (programmatic)

| Chunk | Apparatus defs | Body anchors (Latin) | Body anchors (English) | Status |
|---|---|---|---|---|
| d39-divisio | 2 | 1×{1..2} | 1×{1..2} | clean |
| d39-littera | 8 | 1×{1..8} | 1×{1..8} | clean |
| d39-dubia   | 16 | 1×{1..16} | 1×{1..16} | clean |

All anchors paired correctly across Latin/English; no orphan defs; no orphan anchors.

## Per-chunk verdicts

### d39-divisio — VERDICT: PASS-AS-IS

- **Bounds**: frontmatter `line_start: 26536, line_end: 26584` verified against raw OCR pt2. Line 26536 opens `COMMENTARIUS IN DI8TINCTI0NEM XXXIX.`; line 26584 closes the `TRACTATIO QUAESTIONUM` listing immediately before `ARTICULUS I.` at line 26585. Boundaries semantic, not arbitrary.
- **Header count vs raw**: chunk has `## Commentarius in Distinctionem XXXIX.` (1), `### Divisio textus.` (1), `### Tractatio quaestionum.` (1) — all three appear in raw OCR at lines 26536, 26544, 26562 respectively. No silent dropouts.
- **Body diff**: line-by-line walk of raw lines 26536–26584 vs the chunk's `## Latin` block — content present in full. The "tres partes / In prima / In secunda / In tertia" tripartite division and the "duo principaliter / quaeruntur tria" question listing reproduced exactly. No paraphrase, no compression.
- **Apparatus**: 2/2 entries match the page-684 footer band at raw lines 26595–26597:
  - footer 1 "Cfr. supra pag. 312, nota 8." → chunk [^1] ✓
  - footer 2 "Supple cum Vat. ibi: Simul itaque." → chunk [^2] ✓
- **transcription_status**: extended with 2026-05-08 audit note (see edit below).
- **No edits to body or apparatus made.**

### d39-littera — VERDICT: PASS-AS-IS

- **Bounds**: frontmatter `line_start: 26377, line_end: 26535` verified against raw OCR. Line 26377 opens `DISTINCTIO XXXIX.` (Lombard text head); line 26535 closes Cap. IV at "praescit quoque omnia futura, tam bona quam mala." with line 26536 opening Bonaventure's `COMMENTARIUS`. Clean semantic boundary. Frontmatter status string already documents this in detail.
- **Header count vs raw**: chunk has `### DISTINCTIO XXXIX.` and 4 `#### Cap. {I,II,III,IV}.` — all 5 markers appear in raw OCR at lines 26377, 26380, 26447, 26467, 26483 respectively. No silent dropouts.
- **Body diff**: line-by-line walk of raw lines 26377–26535 (≈1.5 printed pages, two-column body band only) vs chunk `## Latin` — content present in full across all four chapters. Augustine *De Trinitate* XV cap. 13/14 long quotation reproduced verbatim. Hieronymus *Comm. in Habacuc* quotation in Cap. IV likewise verbatim. Apostle citation (1 Cor 9:9 / Sap 12:13) present. Page-break placement (`<!-- page 683 -->` after "Et licet possit scire vel prae-") lands exactly at the OCR column-foot break.
- **Apparatus**: 8/8 entries match raw OCR footer bands across pp. 682–683:
  - p. 682 footer (raw lines ~26456–26462), 2 entries: "Vat. cum edd. 2, 3 sub" → [^1]; "Cap. 13. n. 22. Sequens locus est c. 14. — In ultimo textu solummodo Vat. et edd. 1, 5, 6, 8, 9 post inamissibilis addunt et invariabilis…" → [^2] (combined Augustine note: chapter cite + Vat. variant + cod. D/E variants — preserved as one entry per OCR) ✓
  - p. 683 footer (raw lines ~26519–26527), 6 entries: "Cod. addit vel mutari" → [^3]; "Ad c. 1, 14." → [^4]; "I. Cor. 9, 9; alius locus est Sap. 12, 13." → [^5]; "Intellige: respectu quorum dedit septem praecepta posteriora decalogi…" → [^6]; "Respicitur Matth. 5, 45: Qui solem suum oriri facit…" → [^7]; "Solummodo Vat. et edd. 4, 5, 6, 8, 9 semel." → [^8] ✓
  - 2 + 6 = 8 entries; chunk has 8. No fabrication, no silent dropouts.
- **Marker-position spot-checks**:
  - [^1] on `mutari` (Cap. I opening, "divina scientia possit augeri vel mutari") — apparatus governs the Vat./edd. 2,3 *sub* variant. ✓
  - [^2] on `de Trinitate` (Cap. I, Augustine quotation introducer) — long combined Augustine apparatus note. ✓
  - [^3] on `non potest` (Cap. III, "scientia augeri potest"; Cod. R *vel mutari* variant). ✓
  - [^4] on `Habacuc` (Cap. IV introducer "in expositione Habacuc"). ✓
  - [^5] on `Apostolus` (Cap. IV, "ut ait Apostolus"). ✓
  - [^6] on `quibus` (Cap. IV, "rationabilibus, de quibus praecepta tradidit"). ✓
  - [^7] on `dat` (Cap. IV, "qui omnibus solem suum oriri facit et pluviam dat"). ✓
  - [^8] on `semper` (Cap. IV, "immo simul et semper omnia"). ✓
- **transcription_status**: extended with 2026-05-08 audit note (see edit below).
- **No edits to body or apparatus made.**

### d39-dubia — VERDICT: PASS-AS-IS (with one pre-existing flagged ambiguity carried forward)

- **Bounds**: frontmatter `line_start: 27875, line_end: 28023` verified. Line 27875 opens `DUBIA CIRC.\ LITTER\M MAGISTRl.` (OCR garbles `CIRCA LITTERAM`); line 28023 closes DUB VI at "ut divitum." with line 28024 (`DISTINCTIO XL.`) starting d.40. Clean semantic boundary.
- **Header count vs raw**: chunk has `### DUBIA CIRCA LITTERAM MAGISTRI.` (1) + 6 `#### DUB. {I,II,III,IV,V,VI}.` headers. All 6 DUB markers appear in raw OCR at lines 27880, 27924, 27946, 27977, 27996, 28009 respectively (some printed as `DUB.` and some OCR-garbled to `DuB.` / `Dru.` / `DoB.`; corpus-correct). No silent dropouts. **Note**: the *cross-chunk-reuse* failure mode the brief warned about (cf. d.27 entire DUB V missing) is NOT present here — the 2026-05-07 extension already absorbed DUB V + DUB VI per the chunk's `transcription_status` and the matching tier2-ambiguities log.
- **Body diff**: walk of raw lines 27875–28023 (≈2 printed-page columns, splits across pp. 698–699) vs chunk `## Latin` — content present in full across all six DUB. Augustine quotation in DUB I, distinction-36-cross-reference in DUB II, *De Civitate Dei* XI cite in DUB III, two-mode *scire* analysis in DUB IV, Magister-quotation analysis in DUB V (longest), and Sap. 6 / *aequaliter* analysis in DUB VI all verbatim. No paraphrase. Page-break placement (`<!-- page 699 -->` between DUB IV and DUB V) lands at the OCR column boundary.
- **Apparatus**: 16 entries vs 9 (p. 698 footer) + 6 (p. 699 footer) = 15 raw-OCR entries. **One-entry overshoot**, but this is a *known pre-existing flag*, not a fresh fabrication:
  - p. 698 footer (raw lines ~27950–27974), 9 entries: [^1] *Ed. 1 addit vel quid essentiale*; [^2] *Dist. 32. a. 1. q. 1. ad 2…*; [^3] *Cfr. Libr. VIII. Grammat. c. 9. et 13. — Pro Gerundia…*; [^4] *Cap. 1, et ibid. in Comment. dub. 1.*; [^5] *Vide Alex. Hal., S. p. 1. q. 23…*; [^6] *Cap. 10. n. 3.*; [^7] *Huius dubii solutio invenitur etiam apud Petr. a Tar.*; [^8] *Cfr. supra pag. 690, nota 2.*; [^9] *Vat. cum pluribus codd. sic. Paulo ante pro primo cod. X proprie. — Plura de hoc dubio…* ✓
  - p. 699 footer (raw lines ~28049–28067), 6 entries: [^10] *Vat., post velle posita virgula, pro hoc substituit hic…*; [^11] *Vat. fuit. — Praecedens et intellige: ergo etiam.*; [^12] *Cod. Z hic et paulo ante ordinationem. Paulo inferius pro exemplum ed. 1 dictum…*; [^14] *Multi codd. cum Vat. post non quia alterum subiiciunt non…*; [^15] *Vers. 8, ubi Vulgata Aequaliter pro Aequalis…*; [^16] *Sive accipitur. Cfr. supra d. 1. q. 1. Scholion. — Mox pro tamen Vat. tam.* ✓
  - **Chunk's [^13] (`Vat. fuit.`) has no clear correspondent in the raw-OCR p. 699 footer band.** Body anchor sits at "et quod semel est[^13] ordinatum semper fuit ordinatum." This is a documented `[?]` flag in `manual-review/tier2-ambiguities-d39-dubia.md` line 21 (added 2026-05-07): *"Two adjacent apparatus notes in the OCR both read `Vat. fuit`. Provisionally split between [^11] and [^13]; the second may belong to a different lemma not yet identified. → Resolve against 600dpi PDF p. 699."*
  - **No new fabrication introduced by this audit.** The flag is pre-existing and scheduled for resolution in the d.31–d.40 polish-pass eyes-on PDF check after d.40 ships. Carrying forward as-is.
- **Marker-position spot-checks** (DUB I–IV, the cleaner block):
  - [^1] on `essentialis` (DUB I obj., "personalis est ratio rei essentialis"). ✓
  - [^2] on `est` (DUB I respondeo, "in praecedentibus habitum est"). ✓
  - [^3] on `Priscianus` (DUB I respondeo, "sicut dicit Priscianus"). ✓
  - [^4] on `sexta` (DUB II obj., "distinctione trigesima sexta"). ✓
  - [^5] on `essentia` (DUB II respondeo tail). ✓
  - [^6] on `Dei` (DUB III obj., "Augustinus undecimo de Civitate Dei"). ✓
  - [^7] on `obiectio` (DUB III respondeo tail). ✓
  - [^8] on `verum` (DUB IV obj., "nihil scitur nisi verum"). ✓
  - [^9] on `sic` (DUB IV respondeo, "et sic incipit Deus scire") — italicised lemma per Quaracchi. ✓
- **DUB V/VI marker positions** carry the pre-existing flags noted in tier2-ambiguities-d39-dubia.md (DUB V `[^10]` *hic/hoc* substitution direction; DUB V `[^10]` tail truncation; DUB V `[^12]` placement on *ordinationem* vs earlier *velle hoc*; DUB V `[^13]` orphan). No new flags introduced.
- **transcription_status**: extended with 2026-05-08 audit note (see edit below).
- **No edits to body or apparatus made.**

## Smoke-test build

`cd site && node scripts/build-content.mjs` →

```
Built content.json: 1 book(s), 422 questions, 350 translated
```

Clean build. No parse errors raised by the d.39 chunks.

## Totals

- Chunks audited: 3 (divisio, littera, dubia)
- Substantive body fixes: 0
- Apparatus rebuilds: 0
- New `[?]` flags raised: 0
- Pre-existing `[?]` flags resolved: 0 (all deferred to d.31–d.40 polish-pass eyes-on PDF)
- Pre-existing `[?]` flags carried forward unchanged: 4 (all in dubia DUB V; tracked in `tier2-ambiguities-d39-dubia.md` lines 19–22)
- Backups created: 0 (no substantive edits warranted backup)
- Anomalies: dubia chunk has 16 apparatus entries vs 15 raw-OCR footer entries; the 16th ([^13] = `Vat. fuit.`) is a pre-existing, documented `[?]` flag — *not* introduced by this audit, *not* a fresh fabrication. Carrying forward for the polish-pass PDF resolution.

## Cross-corpus observations

- The brief flagged the d.39 a1-q2 Sch II wholesale fabrication caught during the 2026-05-07 polish. The three *scaffold-class* chunks (divisio / littera / dubia) audited here show no comparable fabrication. The polish-pass appears to have correctly bounded the fabrication problem to the quaestio-Sch chunk; scaffold chunks are clean.
- Cross-chunk reuse / Vat-variant inversion / silent body dropouts: not detected.
- Recommend the d.31–d.40 decade polish-pass take the dubia [^13] anomaly as a priority eyes-on item; it is the only outstanding apparatus-vs-OCR mismatch in d.39's three scaffold chunks.
