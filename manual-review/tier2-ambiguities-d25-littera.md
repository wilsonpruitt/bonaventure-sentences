# Tier-2 ambiguities — bon-sent-I-d25-littera

Promotion to Tier 2 on 2026-05-03. Source: `raw/bonaventure_vol1_pt2_raw.txt` lines 1430–1722, printed pp. 432–434.

## Boundary / structural

- **Page-432 top-of-page footer block (raw lines 1456–1485)** contains apparatus that semantically belongs to the *d.24 commentarius* (references "responsionis", "praesupponit", "quantum", and the "Notandum quod pro quia" pattern from a d.24 dubium). These five spillover entries are SUPPRESSED in this chunk's apparatus per d.23-littera precedent. The page-432 littera apparatus proper begins at the second NOTAE block (raw lines 1487–1495 + 1577–1601, two-column re-flow).
- **Tail trim**: chunk ends at raw line 1722 ("etiam nominum proprietates, id est personas, vel, ut" → continues across column to "Graeci exprimunt..."). The OCR places the COMMENTARIUS IN DISTINCTIONEM XXV rubric at raw line 1723 (between the two columns of Lombard text on p. 434). Both columns of p. 434 Lombard text ARE in the line range 1430–1722; the COMMENTARIUS opener and DIVISIO TEXTUS that follow are correctly excluded.
- **Page-434 littera apparatus** is split off from the COMMENTARIUS apparatus block. Notes 1 (Hieronymus *ad Damasum* codd. variants) and 2 (John Damascene *de Fide orthodoxa* III.5) sit at raw lines 1796–1810, immediately preceding the "NOTAE AD COMMENTARIUM" marker at line 1810. The free-standing "*Nota bene*: Codices huic distinctioni addunt IV. caput…" editorial aside (also in that block) is not anchored to a body marker and is **omitted** from the apparatus.

## OCR garbles silently corrected

- "perspiia" / "persoiia" / "pcrsouae" → *persona* / *personae* (consistent throughout)
- "considerandum est, cum hoc nonien per-sona" → *…hoc nomen persona* (n misread as ni)
- "praedlctum est" → *praedictum est*
- "ait Augustlnus, ad se dicitur" → *ait Augustinus, ad se dicitur*
- "essenlia" → *essentia*; "iutelligentia" → *intelligentia*
- "Wter" (line 1505) → *Pater*
- "Spiii-tus" → *Spiritus*
- "manifestum flt" → *manifestum fit*
- "polest" → *potest* (multiple)
- "respondetur" / "respondebunt" / "respondemus" — variants normalized
- "tyerum" / "verumtamen" → *Verumtamen*
- "loquendi" / "loquuntur" — preserved as-is
- Greek transliterations (*hypostasis*, *hypostases*) normalized from OCR garbles like "hjfpostasim", "hyposlasis", "liypostases".
- "Iibro" / "hbro" → *libro*
- "Damasuni" → *Damasum* (apparatus n. 23 confirms title)
- "couiecturis" → *coniecturis*

## Translation choices flagged

- *ad se dicitur* — rendered "is said *to itself*" with Latin formula preserved on first occurrence per CLAUDE.md convention. Lombard's grammar treats *persona* as said *to itself* (i.e., absolutely / non-relatively).
- *quid tres, vel quid tria* — kept as "*what three* or *what three things*" throughout to preserve Augustine's distinction (masc. vs. neut.) which Lombard repeatedly leverages.
- *subsistentia / subsistentes / subsistentiae* — rendered consistently "subsistence" / "subsisting [things]" / "subsistences"; left Greek *hypostasis*/*hypostases* in italic Latinized form (no transliteration to Greek script).
- *processibilis proprietas* — rendered "processional property" (technical term for the Spirit's distinguishing property of *processio*).
- Augustine quote at apparatus [^17] (1 John 5:7) — Lombard's *perhibent* preserved against the Vulgate's *dant*; apparatus note records the variant.

## No `[?]` flags inline

This chunk required no inline `[?]` placeholders; all OCR garbles were unambiguously resolvable from context, and the Quaracchi apparatus on pp. 432–434 confirmed all wording variants flagged in the OCR.
