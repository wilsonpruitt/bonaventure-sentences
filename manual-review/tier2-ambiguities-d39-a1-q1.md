# Tier-2 ambiguities — bon-sent-I-d39-a1-q1

OCR re-set against `raw/bonaventure_vol1_pt2_raw.txt` lines 26585–26927 (Quaracchi 1882, pp. 684–687). Date: 2026-05-07.

## Inline `[?]` flags placed in chunk

1. **Scholion I, Alex. Hal. quotation**: OCR reads "*Scientia Dei, quae est ad res, non est po-* res; unde cum ipse sit causa immutabilis...*". The token `po-` at end of OCR line followed by orphan `res` is unresolved. Left as `[?]` after `po`. Likely intended *posterior a rebus* or *post res*, but the line break and "po'" with apostrophe in OCR is ambiguous. Retain as `po[?]res` until 600 dpi PDF check (decade-polish pass at d.40).

## Frontmatter corrections

- `printed_pages` was `[662, 663, 664, 665]` (off by ~22; that range is mid-d.36). Corrected to `[684, 685, 686, 687]` from running heads at OCR line 26613 ("...QUAEST. I. 685") and corroborated by surrounding distinctio-headers and column count. d.38 chunk pages 669–671 use the same offset family; d.39 follows at 684–687.
- `pdf_pages` corrected to `[274, 275, 276, 277]` (offset = printed − 410).
- Added `has_apparatus: true`, `has_scholion: true`.

## Other notes

- Auctores list at end of Scholion III follows the OCR token-order; minor OCR digit garbles (e.g. "3S" for "35", "iO" for "40") were silently normalized per CLAUDE.md unambiguous-correction rule.
- Greek words τάττεσθαι / τάττειν in apparatus [^3] reconstructed from context; OCR garbles them as `(IraTiTTEsSai)` and `(iTciTaTTEiv)`.
- Apparatus footnotes [^1] (Psalm 93:9) and [^2] (Eccli. 23:29) draw from the bottom-of-p.684 footnote block (OCR lines 26605–26607), which mixes Lombard-text footnotes (1, 2 = Verba scilicet / Cum paucis codd.) with Bonaventure-text footnotes (3 = Psalm. 93, 4 = Vers. 29). Only the latter belong to this question.
