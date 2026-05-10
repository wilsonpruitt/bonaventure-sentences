# Tier-2 ambiguities — d.10 littera

Created 2026-05-08 during the d.10 scaffolds sweep (rebuild from OCR after wholesale-fabrication finding).

OCR scan damage on Quaracchi p.193 footer (raw lines 38221–38239) leaves multiple footnote bodies partially or fully garbled. Six chunk apparatus entries are flagged `[?]` for PDF eyes-on resolution at the d.41–d.50 polish-blocker pass.

Resolution method per CLAUDE.md polish-blocker cadence: `pdftoppm -r 600 -f 295 -l 295 -png raw/doctorisseraphic11bona.pdf raw/vision/vol1/p-hires-PRINTED-r600` (PDF page 295 = printed p. 193 for vol I pt 1, offset +102).

| Chunk | Footnote | Body anchor | OCR fragment | Resolution needed |
|---|---|---|---|---|
| d10-littera | [^12] | Cap. II body, *diligamus²* (line 38114) | Body marker is real OCR `^`/`²` at *diligamus*; footer fn 2 reads *Vat. cum ceteris edd. contra originale; Ipse ergo Deus est dilectio.* — but that text is what we attached to [^13] (anchor at *dilectio* line 38121). It is possible [^12] and [^13] share a single OCR footer entry and the second body marker is editorial duplication; or fn 2 attaches to *diligamus* and fn 3 (currently [^14] = *Omnia... ex Augustino*) attaches to the next position. Confirm anchor sequence on PDF p.193. | Confirm whether fn 2 anchor is *diligamus* or *dilectio*. Consolidate. |
| d10-littera | [^17] tail | Cap. III, *Psalmum⁶* (line 38137) | Footer fn 6 reads *Cap. 1. et 5. n. 6. et 7; ex ultimo cap. etiam sequentes huius capituli textus excerpti sunt. In fine primi textus pro subsistit cod. D et edd. 1, 8 subsisti t* ... and then OCR garbles ("subsisti t  ,m\m\    ni,ii,'is  i.i.Hvrci  ,    si"). | Recover the *subsisti·* substitution variant tail. |
| d10-littera | [^18] | Cap. III, *de Trinitate⁷* (line 38140) — but actually OCR fn 7 = *Ephes. 4, 8* which attaches to *pacis* (line 38151) | Footer fn 7 reads "Ephes. 4, 8. — Paulo ante pro siidqu... suntque ac forte meliiis. Deinile codd. .\C inc... textum verbis: Spiriius quoqur:  pro  Spiritui:" — heavily garbled. | Recover the *suntque*/*Spiritus* codicological tail. Re-anchor [^18] to *pacis* (line 38151) not *Trinitate* (line 38140). |
| d10-littera | [^19] | Cap. III, *Deus caritas est⁸* (line 38161) | Footer fn 8 reads "1. Ioan. 4, 16. — Vat. el cd. 4 jiosl ii, omittunt :  quoniodo  Deus  dileetio  est,  si  mui <" — truncated. | Recover the full *quomodo Deus dilectio est, si non est substantia, quomodo Deus substantia est* omission scope. |
| d10-littera | [^20] tail | Cap. III, *de Trinitate⁹* (line 38176) | Footer fn 9 reads "Cap. 19. n. 37. — Cod. C brevius : Pa[trem  diligit  Filius. Mo\\  codd.  BCIi n... origin:'li  jii-''  iiii'!fiit)i'cm   lri;iinl  iiii'lpiliilili-r" — truncation worsens to "ACDE / Dio / ililiii" by line 38239. | Recover the *ineffabilem ... ineffabiliter* substitution variant. |
| d10-littera | [^21] | Cap. III, second *de Trinitate* anchor | Body shows two footnote markers in Cap. III before/after the long Augustine quotation. OCR p.193 footer has only 9 visible footnotes and ends garbled, so an additional fn (10) may exist but is lost. | Confirm whether Cap. III has 1 or 2 footer references in this position. |
| d10-littera | [^22] | Cap. III, *Apostolus¹⁰* (line 38192) | Body marker `'°` is clearly visible at line 38192, attaching to the Col. 1:13 quotation *Transtulit nos in regnum Filii caritatis suae*. No corresponding footer fn 10 is recoverable from OCR; reconstruction "Coloss. 1, 13." is near-certain by context. | Confirm scripture citation form on PDF; check for codicological-variant tail. |

## Note for next polish-blocker

The d.10 littera chunk is otherwise body-clean (verbatim from OCR pp. 192 lines 37971–38040 and p. 193 lines 38110–38198). No body-text `[?]` flags raised — only apparatus tail-truncation `[?]` flags. The chunk's Latin and English bodies render correctly; only the apparatus footer text is provisional pending PDF resolution.

When the d.41–d.50 decade polish runs, the seven `[?]` items above can be resolved together via a single PDF p. 295 read.

## 2026-05-10 from-scratch rebuild

Chunk rebuilt from raw OCR (lines 37971–38198) under the d.1–d.10 rechunk pipeline. Apparatus now totals **22 entries** (13 from p.192 footer block — 3 above-NOTAE textual variants on Master's text + 10 below-NOTAE reference notes; 9 from p.193 footer block). Eleven `[?]` flags inline on apparatus entries [^6], [^14], [^19] (×2), [^20] (×3), [^21] (×2), [^22] (×3) covering p.193 OCR scan damage at raw lines 38217–38239 (truncated tails: *subsisti·*, *suntque/Spiritus*, *quomodo Deus dilectio est si non est*, *ineffabilem/ineffabiliter*, Codex C *brevius* clause). Carryover: resolve at d.41–d.50 polish via 600dpi PDF p.295 read. All three audits clean (paraphrase 0/0, headers no flag, apparatus diff −6 with no flag).
