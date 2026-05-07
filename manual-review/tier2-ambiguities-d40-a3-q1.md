# Tier-2 ambiguities — bon-sent-I-d40-a3-q1

OCR raw: `raw/bonaventure_vol1_pt2_raw.txt` lines 29361–29589.
PDF: `raw/doctorisseraphic12bona.pdf`, pp. 304–305 (printed 714–715).

## Inline `[?]` flags

- **apparatus [^1] (article cross-ref note)**: OCR fragment "Cum art. I. divisus sit in duos" trails into footnote-block junk before the next note picks up. Currently rendered as a literal-fragment placeholder. → Resolve from PDF p. 304 footnote 1.
- **apparatus [^15] ("Facta enim c. 16[?] n. 32")**: OCR shows `c. 6` or `c. 16` ambiguously next to a stray `1` glyph; both Augustine, *de Praedest. Sanctor.* loci are plausible (the section-numbering of the work uses both). Currently rendered as `c. 16[?] n. 32`. → Resolve from PDF p. 305 apparatus block, last footnote, against Migne PL 44 col. 985 ff.
- **apparatus [^15] (Vat. *effectu* variant)**: OCR shows `Multi codd. sunt dubiae lectionis`; the immediately preceding clause "nec discerni potest, utrum *effectum* exhibeant, an *effectu*" — the codices listed (H R I aa) are read with low confidence; siglum `aa` is OCR-derived. → Verify codex sigla against the d.39–40 apparatus key in PDF.

## OCR-only structural notes (silently corrected)

- Title `Utrmn electio sil in Deo ah aetenio, an ex tempore` → restored to `Utrum electio sit in Deo ab aeterno, an ex tempore` (matches frontmatter `title_la`).
- `Ekgit` → `Elegit` (Eph. 1:4, fundamentum 1).
- `temporaliter , qui` and similar Quaracchi-style spaces around punctuation normalized.
- `praeopiatio` (sol. ad 5) → `praeoptatio`.
- `praeoixlinatio-nis` line-break → `praeordinationis`.
- `lemporalis` → `temporalis` (one obvious `l/t` confusion in sol. ad 6).
- `oQines` → `omnes` (sol. ad 2).
- `eUgitur` → `eligitur`; `melior a niinus bono` → `melior a minus bono` (sol. ad 3).
- `inquisitiove` and `delibera-tione` line-break joined.
- `qua vult cum praescientia` (sol. ad 2) supplied from collated reading where OCR splits "qua vult cum lecuo." (`lecuo` is OCR garble for `praescientia`); confirmed against parallel passage at d.46.
- Damascene and Aristotle Greek (κυρίως, προαίρεσις, περὶ προαιρέσεως) restored from OCR transliterations (`xupiws`, `jtpoaipEois`, `npoai-pE(3i?l`).

## Frontmatter corrections

- `printed_pages`: changed from `[712, 713, 714]` → `[714, 715]`. Verified against running heads:
  - line 29357 OCR: "SENTENTIARUM LIB. I." (verso head — top of even page; here = p. 714).
  - line 29471 OCR: "DIST. XL. ART. III. QUAEST. I.   715" (recto head, p. 715).
  - line 29586 OCR: "SENTENTIARIIM LIB. I." (next verso head — p. 716, beyond chunk).
- `pdf_pages`: corrected to `[304, 305]` (printed − 410 for vol1 pt2 offset).
- `source` updated to `pp. 714–715`.
- `has_scholion: true`, `has_apparatus: true` added.
