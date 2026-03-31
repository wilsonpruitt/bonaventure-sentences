# Bonaventure Sentences — Translation Prompt for Sonnet

Use this prompt for bulk translation. Paste the Latin text from a chunk's `### Latin` section where indicated.

---

```
You are translating St. Bonaventure's Commentary on the Sentences of Peter Lombard (Quaracchi critical edition, 1882) from Latin to English. This is a scholastic theological text from the 13th century.

## Critical Instructions

- Translate ALL Latin text provided, even if it begins mid-sentence or mid-argument. Do not skip, summarize, or reorganize any content. The chunks may start or end mid-quaestio — translate exactly what is given.
- Produce paragraph-for-paragraph parallel translation. Each Latin paragraph should have a corresponding English paragraph in the same order.
- Do NOT add editorial markup (bold headers, section labels, inline source citations) that does not appear in the Latin. Preserve only the structural markers that appear in the source (e.g., DIST., ART., QUAEST., CONCLUSIO, numbers like 1., 2., 3.).
- Do NOT identify or cite sources beyond what the Latin text itself states. If the Latin says "Augustinus in Soliloquiis," translate that reference as-is. Do not add "[De Trinitate IX.4.5]" or similar editorial additions.
- The critical apparatus (footnotes at the bottom referencing manuscript variants like "Vat. cum cod. cc") should be noted as "[Critical apparatus omitted]" — do not translate it line by line.
- The scholion sections (marked SCHOLION or SCHOLIOK in OCR) should be noted as "[Scholion omitted]" — these are Quaracchi editorial commentary, not Bonaventure's text.

## Translation Style

- Formal academic English suitable for theological scholarship
- Translate standard scholastic formulae consistently:
  - *Videtur quod...* → "It seems that..."
  - *Sed contra* / *Contra* → "On the contrary"
  - *Respondeo dicendum quod...* → "I respond: It must be said that..."
  - *Ad primum/secundum/tertium...* → "To the first/second/third [objection]..."
  - *Praeterea* / *Item* → "Likewise"
  - *Ergo* → "Therefore"
  - *Dicendum quod...* → "It must be said that..."

## Key Terminology (translate consistently)

- *esse* → being / existence (context-dependent)
- *essentia* → essence
- *substantia* → substance
- *forma* → form
- *materia* → matter
- *potentia* → potency / power (context-dependent)
- *actus* → act / actuality
- *ratio* → account / ground / formal character (context-dependent)
- *intellectus* → intellect / understanding
- *voluntas* → will
- *caritas* → charity
- *gratia* → grace
- *exemplar* → exemplar
- *illuminatio* → illumination
- *vestigium* → vestige / trace
- *imago* → image
- *similitudo* → likeness
- *processio* → procession
- *suppositum* → supposit

## OCR Notes

The Latin comes from OCR of 1882 typography. Common artifacts:
- Broken words across lines (e.g., *ehci-tus* = *elicitus*)
- Garbled marginal glosses inline (e.g., *Fundameata.invicem* = marginal note bleeding into text)
- Letter substitutions (*ahquid* = *aliquid*, *ahud* = *aliud*)
- Inline footnote numbers

Silently correct obvious OCR errors. Only note genuinely ambiguous readings.

## Output Format

Produce exactly two sections:

### English

[Full paragraph-for-paragraph translation of ALL provided Latin text]

### Notes

[Brief notes: genuinely ambiguous passages, key translation decisions, important theological context. 5-10 bullet points maximum.]

---

## Latin Text

[PASTE LATIN HERE]
```
