# Tier-2 ambiguities — bon-sent-I-d24-a2-q2

Source: `raw/bonaventure_vol1_pt2_raw.txt` lines 998–1164.
PDF: `raw/doctorisseraphic12bona.pdf` (vol I pt 2). Verified offset: pdf = printed − 410. Printed pp. 426–428 → pdf pp. 16–18.
Note: The sibling chunk `bon-sent-I-d24-a1-q1.md` lists `pdf_pages: [522, 523, 524]` for printed pp. 420–422; that offset (+102) is the vol1pt1 offset and is incorrect for pt2. Confirmed by extracting pdf p.16 with `pdftoppm` — printed running head reads "426 SENTENTIARUM LIB. I." and pdf p.17 "DIST. XXIV. ART. II. QUAEST. II. 427".

## Resolved silently
- OCR `dicantur^` / `Boethius^` / `posuit^` / `idem^` etc. — superscript footnote markers; placed `[^N]` at corresponding positions in the body.
- OCR garbles fixed silently with full confidence:
  - `secundiun → secundum`
  - `dicunlur → dicuntur`
  - `dieitur → dicitur`
  - `oninino → omnino`
  - `iiumeraks → numerales` (cf. apparatus note explicitly correcting Vat.'s *numeratae* — Quaracchi's chosen reading is *numerales*)
  - `quahtatis → qualitatis`
  - `quantitafis → quantitatis`
  - `liraitatio → limitatio`
  - `Hmitatio → limitatio`
  - `subslantialiter → substantialiter`
  - `nonien → nomen`
  - `inlra → intra`
  - `iraplicat → implicat`
  - `dieuntur → dicuntur`
  - `obiicituT → obiicitur`
  - `subiicitur` (kept as in OCR — the older spelling of *subicitur*)
  - `consequenS materiam` (OCR comma-fragmentation collapsed)
  - `7-atio → ratio` (OCR garble)
  - `intelU-gendi → intelligendi`
  - `otiginem → originem`
  - `cmitra fidem → contra fidem`
  - `nuUa → nulla`
  - `notio, quae communiter → notio, quae communiter` (verified)
  - `&o\um → solum`
  - `lila → Illa`
  - `quascumque` (preserved)
  - `unitas personae,` (kept as printed)
  - `personarum *` superscript marker → `[^N]`
- Apparatus footnotes were renumbered consecutively 1–16 in body order, drawing from the q2 columns of the page-bottom NOTAE blocks on pp. 426 (2 fns), 427 (10 fns), 428 (3 fns: hoc, personales, tantum). Followup-only fns belonging to art.III on p.428 (about *trinus/trinitas*) were excluded.

## Footnote-anchor mapping caveats
- The Quaracchi apparatus on p.426 mixes notes for q1 (top of page) and q2 (bottom). Two notes were assigned to q2 here:
  1. "Auctoritate vetustiorum codd. et ed. I posuimus *dicantur*" — anchors at *dicantur* in q2's opening sentence.
  2. The Boethius/Augustine source citation "Libr. de Trin. c. 1. — August., V. de Trin. c. 1. n. 2" — anchors at *Boethius et Augustinus*.
  3. The "Vide supra d. XXII. lit. Magistri, c. 1." note — best fit is the *ad se* citation in argument 2 (anchored on p.427 due to page break mid-sentence). Placed as [^3] at "dicitur secundum substantiam" in arg.2.
- These three p.426 notes are placed as [^1], [^2], [^3] respectively. If the printed q1/q2 column-split differs from this assignment, [^3]'s placement could be re-mapped to a different position in arg.2; semantic content unaffected.

## Genuine `[?]` flags inserted
None. All garbles in the OCR for this chunk could be resolved with high confidence by cross-reference to PDF page images at 250–500 dpi.

## Notes
- The conclusio in the printed text reads only "Nomina numeralia in divinis dicuntur secundum relationem et important" — the sentence is left dangling at the line break in Quaracchi (continued by "ipsas notiones" implied from the body's matching phrase "important ipsas notiones"). Rendered as `*Nomina numeralia in divinis dicuntur secundum relationem et important [ipsas notiones].*` to match the resolution given in the body.
- Scholion on p.428 has only sections **I** and **II** for q2 (section markers in the source are "I." and "11." respectively, OCR'd "11." for "II."). No section III for this question.
