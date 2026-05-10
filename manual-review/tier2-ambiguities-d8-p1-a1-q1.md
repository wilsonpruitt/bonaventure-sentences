# d8-p1-a1-q1 Tier-2 ambiguities (2026-05-09)

Wave 9b Tier B disposition: REBUILD. Apparatus expanded 10 → 22 entries.

## Per-page footer distribution (eyes-on PDF pp. 150–152 at 300 dpi)

- **p. 150:** 13 printed-page footer entries. Fns 1–4 reference content at the **top of p. 150**, which is the *Tractatio quaestionum* listing belonging to the d8-p1-divisio chunk (printed_pages: [149, 150]). Fns 5–13 belong to this q.1 chunk → consolidated as `[^1]–[^9]`.
- **p. 151:** 10 printed-page footer entries → consolidated as `[^10]–[^19]`.
- **p. 152:** 3 printed-page footer entries (the rest of the page is taken up by Scholion sections I–IV) → consolidated as `[^20]–[^22]`.
- **Total:** 9 + 10 + 3 = 22 entries.

## Audit-overcount source

Hardened audit-apparatus-count.py raw=31 vs ground-truth=22 (residual diff +9). Sources of the +9 OCR overcount:

1. The four divisio-page footers (p. 150 fns 1–4) sit within the chunk's raw line range (31620–32053) because the d8-p1-divisio chunk's `line_end` (31619) leaves the p. 150 footer band on the d8-p1-a1-q1 side of the boundary. Audit counts them; chunk correctly does not consolidate them.
2. Scholion italicized work-citations on p. 152 (e.g. `S. Thom., I. Sent. d. 19. q. 5`, `de Verit. q. 1. a. 1`, `Hexaem. Serm. 5`, `Alex. Hal., S. p. I. q. 15. m. 5`, `Petr. a Tar.`, `Richard. a Med.`, etc.) match the hardened opener regex but are bibliographic citations within the Scholion body, not footer entries.
3. Numbered argument openers `1.`, `2.` … `7.` in the body match the hardened opener regex `\d{1,2}(?![.0-9])\s+[A-Z]` when followed by a capitalized word.

This is Lesson-10 noise (Scholion-heavy chunks) plus a chunk-boundary edge case (the divisio's footer band sits in this chunk's raw-line range). The +9 residual is acceptable — eyes-on confirms 22 ground-truth.

## Body anchors

- Latin body: 22 `[^N]` markers placed at OCR-confirmed superscript positions (where preserved) or at the most natural printed-page anchor points where the OCR garbled the superscript.
- English body: 22 `[^N]` markers mirror the Latin positions.
- Apparatus: 22 `[^N]:` definitions.

## [?] flags

None placed in this rebuild — all 22 footer entries were transcribed verbatim from the IA djvu OCR with cross-check against the PDF at 300 dpi. The OCR text for these footers was clean enough that no item required a `[?]` flag.

## Body-paraphrase guard (Lesson 11)

Body coverage check: spot-checked the chunk's `## Latin` body against `awk 'NR>=31620 && NR<=32053' raw/bonaventure_vol1_raw.txt`. All seven affirmative arguments, four contra arguments, conclusio, respondeo, three solution sections (Ad 1-2-5-6 / Ad 3 / Ad 4 et 7), three contra-solution sections (Ad 1–3 / Ad 4 / Quaestio incidens), and the closing notandum paragraph are present in both raw and chunk. **Body is sound** — disposition uses status string `Phase C Tier 2 complete —` (not `apparatus-rebuilt-body-paraphrased —`).

## Notes for future maintainers

- The d8-p1-divisio chunk should carry the four p. 150 top-of-page footers (Lombard-text variants for the *Tractatio quaestionum* listing). When that chunk is next dispositioned, the four entries should be added there. (Out of scope for this single-chunk rebuild.)
- Entry [^7] on the prior version of the chunk was an editor-supplied note ("*Veritas incomplexa* convertitur cum ente ut passio entis...") — a paraphrase, not a Quaracchi footer. It has been replaced by the Aristotelian text-citation (V Metaph text. 34) which is what p. 150 fn 11 actually contains. The `convertitur cum ente` body marker now anchors `[^9]` (= p. 150 fn 13, Aristot. II Metaph.), per the OCR superscript on `cum ente":`.
