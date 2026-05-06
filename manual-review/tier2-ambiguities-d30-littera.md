# Tier-2 Ambiguities: bon-sent-I-d30-littera

OCR source: raw/bonaventure_vol1_pt2_raw.txt, lines 10164–10316. Date: 2026-05-06.

## Ambiguity log

**bon-sent-I-d30-littera, apparatus [^9]**: OCR right-column footnote band reads `Psalm. 17, 2, et passim; alius locus s; Seripturae est loan. 12.` — The semicolon after `s` is likely garbled; probably `s. Scripturae` = *sacrae Scripturae*. The `loan. 12` is likely *Ioan.* 12 (John 12), but the specific verse is unclear (perhaps 12:28 or 12:32). Currently rendered: `*Psalm.* 17:2, et passim; alius locus s. Scripturae est *Ioan.* 12.` → Resolve with PDF eyes-on of p. 519 footnote band to confirm exact Ioan. citation and whether `s` = *sacrae* or a numeral.

**RESOLVED 2026-05-06 (PDF p. 519, 600dpi)**: Reading is *Ioan. 1, 12* (John 1:12), not John 12. The OCR dropped "1," after `Ioan.`. Fixed in chunk: `[^9]` Latin and English now read `Ioan. 1, 12` / `John 1:12`. The `s. Scripturae` = *sacrae Scripturae* is correct.

**bon-sent-I-d30-littera, page 520 OCR, left column**: The lower half of page 520 (OCR lines ~10279–10316) is severely degraded — two-column text interleaved with garble patterns like `gt'1'Ciniis`, `nmtalio`, `Snlisliinlia`, `iinlla siiac coiunuilalionc`, `Dcus incipil`, `tcmporalilci-` etc. The Latin text of this section was reconstructed from the partially legible right column and the general sense of the Augustine quotation (*de Trinitate* V, 16, 17). The reconstruction is consistent with known Lombard text at this locus (Dist. XXX, second half of the Augustine passage on *pater noster esse incipit*). Needs PDF eyes-on at p. 520 to verify: (a) exact wording of the transition sentence "Ex his aperte ostenditur..." and (b) the final clause about "Appellatio vero illa, qua Creator relative dicitur..." → Resolve with `tools/extract-pages.py --volume vol1 --pages 520 --dpi 400`.

**bon-sent-I-d30-littera, apparatus [^10]**: OCR right column of footnote band near end of range reads `Codd. DE donalur` — corrected to `donatur` (standard OCR l→t substitution). Low confidence on the codex letters; `D` and `E` are legible but the period after is faint. → Resolve with PDF eyes-on.
