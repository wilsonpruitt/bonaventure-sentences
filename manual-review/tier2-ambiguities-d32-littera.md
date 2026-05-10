# d.32 littera — Tier-2 ambiguities

Logged 2026-05-06 during Tier-2 promotion of `bon-sent-I-d32-littera.md` (raw lines 13570–13859, printed pp. 553–556 of Quaracchi 1882 Tomus I).

## [?] flags

1. **Cap. III, body, footer for [^11] (Hilary *de Trin.* IX)** — OCR of the page-555 footer band is heavily two-column-mangled around the Hilarius citation. Reconstructed Latin reads:
   `Naturae, qui contradicis, haereticae, haec unitas est ... non a se agendo nisi adeo ipse agit, ut quia [?]`
   The trailing `ut quia` is clearly truncated by the column break and the next-page footer continuation; the OCR garble (`il in principio:` → `[Hil.] in principio:`) suggests the apparatus entry begins with a Hilary lemma, but the body of the variant is not legible from OCR alone. Marked `[?]` in apparatus entry [^11]. Resolution: PDF eyes-on at p. 555 footer would clarify; deferred to next decade-polish pass.

2. **Cap. VI, body, *Quaestionem relinquit* paragraph** — `qua nota[?] praemissa quaestio aliquatenus explicari valeat`. The OCR (`quanota^ praemissa`) collapses a footnote-anchor with `qua nota` ("by which note"). Probable reading: `qua nota` = "this having been noted" (ablative absolute participial); but it could also be `qua [no.] praemissa` referring to a specific note number now lost. Translated tentatively as "having been noted"; flagged with `[?]` inline. Resolution: PDF eyes-on; deferred.

3. **Cap. VI, body, [^15] target** — The OCR caption `' Sanclorum rejerre quam afferre. « Optinius enim lector / est, iuquit Hilarius in primo libro de Trinitate*` carries a body-marker `*` (rendered [^15] in chunk) for the Hilary *de Trin.* I citation. The corresponding footer note is missing in the OCR window for this page (raw 13820–13859 has no footnote-band). The standard locus is *de Trin.* I, n. 18 (Hilarius's preface on hermeneutical posture); apparatus entry uses `Num. 1, 18` with the explicit note that `Num.` here is *numerus*, NOT the biblical book of Numbers (per project citation discipline rule).

## Notes on apparatus consolidation

- Body footnote markers reset per printed page in the OCR (1, 2, 3 on p. 553; 1–9 on p. 554; 10–13 on p. 555; 14–18 on p. 556). Renumbered sequentially 1–15 in the chunk to match d.31-littera's single-sequence convention. (Some inline OCR markers had no separately printed gloss in their footer band — those were absorbed into adjacent entries or dropped where redundant.)
- Page-header OCR garbles: `583` for printed `554`, `354 SENTENTIARUM LIB. I.` for printed `555`, `DIST. XXXIl. DIVISIO TEXTUS. 535` for printed `556`. None of these affect content.
- The right-column body of p. 553 begins with the OCR fragment `lii et amor, quc Pater et Filius` — reconstructed as `[Spiritus sanctus est communio Patris et Fi]lii et amor, quo Pater et Filius...`, which is a direct continuation of the left-column sentence. No `[?]` flag needed; the reconstruction is unambiguous against Lombard's *Sent.* I, d. 32, c. 1 standard text.

## Wave 9b Tier B disposition (2026-05-09)

- **Audit signal:** raw=36 vs chunk=15 (diff +21), INCOMPLETE-SUSPECT.
- **Disposition:** OVERCOUNT-only; metadata-only update. No apparatus or body content edits.
- **Per-page ground-truth (eyes-on raw OCR pp. 553–556):**
  - p. 553: 2 NOTAE entries ([^1]–[^2]: *Dist.* XXXI c. 6; Vat. aliaeque edd. *vel Spiritu sancto* variant).
  - p. 554: 8 NOTAE entries ([^3]–[^10]: Cap. 5 n. 8; Dist. X c. 2; Cap. 5 n. 7 + cod. D *etiam* / B E *iungebit*; Ephes. 4,3 + cod. *in vinculo*; Cap. 7 n. 12; Cap. 1 n. 1 + I Cor. 1,24; Quaest. 23 + Retract. c. 26 + de Trin. cross-refs; Cap. 7 n. 12).
  - p. 555: 4 NOTAE entries ([^11]–[^14]: Hilary *de Trin.* IX truncated lemma + cod. *ipse* / *ita*; Vat. *responsio* err.; Vat. + edd. 1,8,9 *ipsa*; codd. *ita* / Vat. *ea*).
  - p. 556: 1 NOTAE entry ([^15]: *Num.* 1, 18 = Hilary *de Trin.* I, n. 18; numerus, not biblical Numbers — per project citation-discipline note).
- **Total: 2+8+4+1 = 15. Matches the chunk's existing 15 apparatus defs exactly.**
- **+21 diff sources (overcount bias):**
  1. Two-stream apparatus convention. Quaracchi *littera* pages carry parallel left-column text-critical band on Lombard's body text (variant readings on `Spirilu sancto`, `substantiam`, `concordibus`, `incongrue`, plus the truncated Hilary-quotation note + `Lectio Magistri magis placet` codex-variant entries on p. 555). Estimated ~10 left-col entries across pp. 553 + 555 footers — by-design omitted, matching d8-littera and d37-littera convention.
  2. Lombard chapter rubrics. d.32 has 6 caps (Cap. I–VI), each "Cap. N." line catches the hardened regex `\d{1,2}\s+[A-Z]`. +6.
  3. Body italicized headings catching `[\W_]\s+[A-Z]`: *Notula*, *Epilogus*, *Difficilis quaestio*, *Quaestionem relinquit*, *Improbatur*, *Responsio*, plus *Opinio prima* / *Opinio secunda* (Cap. III). ~6–8 hits.
- **Body coverage (eyes-on):** all 6 chapters (Cap. I–VI) present; body matches raw OCR pp. 553–556 line-for-line; no paraphrase clusters; all 15 apparatus anchors have matching defs; 3 prior `[?]` flags (above) preserved.
- **Status string:** promoted from `apparatus-incomplete` to `complete` with explicit per-page distribution and overcount-bias note.
- **Apparatus blockquote:** updated with explicit per-page distribution and two-stream convention note.
- **Audits post-disposition:** paraphrase 0 critical / 0 high; headers 0 flags; apparatus-count d32-littera flag column now empty (Tier-2 detected; +21 row remains as heuristic noise band).
- **Confirms Lesson 9 reinforcement / Lesson 10:** every multi-chapter Lombard *littera* lands in +20 to +35 audit diff range due to two-stream + chapter-rubric inflation. Real undercoverage on a *littera* would show diff > +40 plus orphan body anchors — neither signal present here.
