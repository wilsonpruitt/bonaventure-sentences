# Tier 2 ambiguities — d.24 littera

Source: `raw/bonaventure_vol1_pt2_raw.txt` (start of pt2), lines 166–290; printed pp. 418–419; pdf pp. 520–521.

## OCR cleanup performed silently (unambiguous fixes)

- `iu` → `in` (e.g., "in Trinitate") — common OCR mis-segmentation.
- `signiflcetur` → `significetur`, `signiflcamus` → `significamus`, `signiflcari` → `significari`, etc. (the `fl` ligature → `fi` substitution is consistent throughout).
- `quanlitatem` → `quantitatem`; `quanlitatem` → `quantitatem`; `tanlum` → `tantum`; `tantnm` → `tantum`; `dislinctio`/`dislinctione` → `distinctio`/`distinctione`; `discrelio` → `discretio`; `dislinctio` → `distinctio`; `dislin-ctio` (line break) → `distinctio`.
- `iritiitaSjphires` → resolved to `trinitas, plures` (corrupted run from the heading list).
- `triniis vel Iritii-tas, phires yA plwalilas` → `trinus vel trinitas, plures vel pluralitas` (chapter heading list, fully clarified by parallel reading of the cap. body).
- `inlelligentia` → `intelligentia`; `intelligeuliam` → `intelligentiam`; `inlelligendum` → `intelligendum`.
- `auctoritalum` → `auctoritatum`; `multiludo` → `multitudo`; `Hbro` → `libro`.
- `decentes` / `dicentes` — kept as `dicentes`.
- `ditferunt` → `differunt`; `siu-gularitatem` (line break) → `singularitatem`.
- `Trinilate^` → `Trinitate` (footnote marker preserved as `[^4]`).
- `i.` (Roman) in apparatus footnote 8 (`Libr. VII. de Trin. c. i. n. 9.`) — the OCR shows `c. i.`, but the standard reference is *de Trinitate* VII.4.9. Quaracchi consistently cites the chapter as **4**; rendered as `c. 4`.
- `sinc/ukirem` → `singularem` (apparently a copy/print artifact at p.419 left col).
- `multipiicem` → `multiplicem`.
- `espressa` → `expressa` (Ambrose quote on p.419).
- `Ha eiiam` (apparatus footnote 11 OCR tail) → `Ita etiam` — the apparatus is glossing the body's `Ita etiam` reading.

## Marginalia suppressed (Quaracchi side-glosses, not Lombard's text)

Quaracchi prints rubric-style marginal headings beside the body. These are editorial reading aids and are dropped per CLAUDE.md convention:
- `Cur introducta sint haec verba`
- `Quid dicit unus Deus.`
- `Quid unus est Pater.`
- `Quid plures personae vel pluralitas.`
- `Quae tres personae.`
- `Quid duae personae.`
- `Quid distinctae sunt personae.`
- `Quid discretae personae.`
- `Explicit littera.`

## 2-column OCR caveat

P. 418 is set in 2 columns. The OCR reads left column then right column line-by-line, producing interleaving artifacts like `non | gularitatem noluit.` where the LEFT column says "in-" and the RIGHT column begins "Spiritus sanctus...". I disentangled by following the body sense and the natural sentence flow. No single sentence is left straddling the split.

## Marker positions

All 16 footnote markers ([^1]–[^16]) placed at the OCR positions of the original superscripts (digits, `^`, `*`, `°`, `"`, etc.). Note that many of the OCR's superscript glyphs are mangled (`° "` for footnote 5 and 6; `*` for footnote 4); positions inferred from sense and apparatus content.

## Unflagged ambiguities

None require `[?]` flags. The text is well preserved; all variants are documented in the apparatus.
