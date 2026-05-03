# Tier-2 ambiguities — bon-sent-I-d21-a1-q1

Resolved 2026-05-03 during Tier-2 promotion. Three `[?]` flags remain in the apparatus, all from heavily damaged OCR in p.380 footnote block (notes 5–7, the very short single-line entries that the IA djvu broke into illegible runs).

- **Apparatus [^5] (p.379 fn 9, "In codd. *VX* additur ..."):** OCR shows `In codd. VX additui'  niox in codd. SY pro a ponitur ex.` — the word added in *VX* is illegible/missing in OCR. Provisionally rendered `[?]`. Resolution would require 400 dpi vision OCR of p.379 footer left column.
- **Apparatus [^17] (p.380 fn 7, opening sentence "De hoc loquuntur ..."):** OCR is severely degraded (`llr llilr liicillinlir \\ iiii' n|||,|';a i|. ',. i|. i. i|| SchollO, ubi cl piiiii iii\riiii-^ ilr Mi|i|ii.Niliniir prr.-^dirili i[ siiiiplici ac de`). Reconstructed conjecturally as a cross-reference to d.1 q.I Scholion on suppositio simplex; text near the end is irretrievable from OCR.
- **Apparatus [^17] tail (Petri Hispani term):** OCR `confmaiii iiiiiiwbitein lini siiiiptirrni ; Vn\r Polcuni Ilisp;ii,uni COnfnsiiiii fiiiifiiiii` — best guess `confusam confusam` for the Petrus Hispanus terminus oppositus, but the second word is illegible in OCR; flagged `[?]`.

All three could be cleanly resolved by extracting p.379–380 at 400 dpi via `tools/extract-pages.py --volume vol1 --pages 379-380 --dpi 400` and reading the footer block with vision OCR.
