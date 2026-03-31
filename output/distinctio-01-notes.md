# Distinctio 1 — Translation Notes and Future Directions

## What This Is

This is a complete English translation of **Distinctio 1** from St. Bonaventure's *Commentary on the Sentences of Peter Lombard*, Book I (*In Primum Librum Sententiarum*), translated from the Quaracchi critical edition (1882).

**Source:** *Doctoris Seraphici S. Bonaventurae Opera Omnia*, Tomus I. Ad Claras Aquas (Quaracchi): Ex Typographia Collegii S. Bonaventurae, MDCCCLXXXII.

**Internet Archive:** https://archive.org/details/doctorisseraphic11bona

No complete English translation of Bonaventure's Sentences commentary has ever been published. The Franciscan Institute Publications has published partial translations (selected questions), but a full open-access translation would be the first.

---

## Translation Decisions

### Model and Method
- **Bulk translation** was done by Claude Sonnet with a carefully tuned prompt, then reviewed by Claude Opus for accuracy and glossary consistency.
- The Latin was OCR'd from Internet Archive scans of the 1882 Quaracchi printing, chunked by *quaestio* using a Python script, and translated chunk by chunk.
- Chunks sometimes split mid-sentence at page boundaries. These joins were verified against the PDF and stitched together in the final output.

### Scholastic Formulae
Standard formulae are translated consistently throughout:
- *Videtur quod...* → "It seems that..."
- *Sed contra* / *Contra* → "On the contrary"
- *Respondeo dicendum quod...* → "I respond: It must be said that..."
- *Ad primum/secundum/tertium...* → "To the first/second/third [objection]..."
- *Item* → "Likewise"
- *Ergo* → "Therefore"
- *Dicendum quod...* → "It must be said that..."

### Key Terminology
These terms are rendered consistently across the translation:

| Latin | English | Notes |
|-------|---------|-------|
| *uti* | to use | Central concept of Dist. 1 |
| *frui* | to enjoy / enjoyment | The counterpart to *uti* |
| *abuti* | to misuse | |
| *ratio* | account / ground / formal character | Context-dependent; never "reason" in the modern sense |
| *potentia* | potency / power | "potency" when opposed to *actus*; "power" for faculties |
| *actus* | act / actuality | |
| *voluntas* | will | |
| *caritas* | charity | Not "love" (which is *amor*) |
| *facultas* | faculty | Bonaventure glosses this as *dominium* (mastery/dominion) |
| *suppositum* | supposit | Not "person" — more general |
| *honestum* | the honorable | Ciceronian term via Augustine; opposed to *utile* |
| *bonum honestum* | honest good | Intrinsically valuable good |
| *actus quietativus* | quietative act | Bonaventure's technical term for *frui* as resting in an end |
| *complacentia* | complacency | Not the modern pejorative sense; means resting delight |

### What Is Omitted
- **Critical apparatus** — The Quaracchi footnotes documenting manuscript variants (e.g., "Vat. cum cod. cc contra mss. et ed. 1") are omitted. These are essential for textual criticism but would overwhelm a readable translation.
- **Scholia** — The Quaracchi editors' own theological commentary (marked SCHOLION) is omitted. These are valuable secondary scholarship but are not Bonaventure's text.
- **Marginal glosses** — The printed edition has marginal notes (e.g., "Fundamenta", "Ad oppositum", "Conclusio 2") that the OCR sometimes garbled into the body text. These have been silently omitted where they intruded.

---

## What Is Not Yet Included

### Peter Lombard's Text (*Littera Magistri*)
Each distinction in the Sentences commentary begins with the Master's own text — the passage from Peter Lombard that Bonaventure is commenting on. For Distinction 1, this includes three chapters:
- **Cap. I** — *Omnis doctrina est de rebus vel de signis* ("All doctrine is about things or signs")
- **Cap. II** — *De rebus quibus fruendum est, vel utendum* ("On things to be enjoyed or used")
- **Cap. III** — *Quid sit frui et uti* ("What enjoyment and use are")

This text is in the PDF (pp. 26–28 of the printed edition) and should be translated and placed before Bonaventure's commentary to give readers the base text he's responding to.

### Divisio Textus
Bonaventure provides a structural outline (*Divisio Textus*) of how the Lombard organizes each distinction before launching into his own questions. For Dist. 1 this is on printed p. 29. It could be included as a brief structural introduction.

### Praenotiatio Quaestionum
The outline of all six questions (three on *uti*, three on *frui*) that appears at the top of p. 30, before Art. I. This is included in the current translation.

---

## Possible Future Formats

### Latin-English Parallel Text
The current output is English-only for readability. A parallel edition would place the Latin and English side by side, either:
- **Two-column layout** — Latin on the left, English on the right (traditional for critical editions)
- **Alternating paragraphs** — Latin paragraph followed by English paragraph (easier for digital formats)
- **Interlinear** — Latin with English underneath each sentence (useful for students)

The Latin source text for each chunk is preserved in `vol1/bon-sent-I-d1-*.md`. A parallel edition could be generated by merging the Latin from those files with the English translations.

### Apparatus and Annotations
Several layers of annotation could be added in future editions:
1. **Scripture references** — Bonaventure cites the Vulgate extensively. A modern edition could add standardized references (e.g., Prov. 16:4, 2 Cor. 5:7).
2. **Patristic source identification** — Augustine citations could be linked to modern critical editions (CCSL/CSEL numbers, PL columns).
3. **Cross-references within the commentary** — Bonaventure frequently references other distinctions ("as was said above," "as will be shown below"). These could be hyperlinked.
4. **Quaracchi critical apparatus** — The variant readings could be restored as footnotes for scholars who need them.
5. **Scholion summaries** — Brief notes on the Quaracchi editors' theological commentary, for context without the full Latin.

### Margin Notes
The Quaracchi edition uses marginal labels to mark the structure of each *quaestio*:
- *Fundamenta* — foundational arguments for the affirmative
- *Ad oppositum* — arguments for the negative
- *Conclusio* — the thesis statement
- *Solutio oppositorum* — resolution of the contrary arguments

These could be restored as inline labels or sidebar annotations in a digital edition.

---

## Volume Coverage

This translation covers **Distinctio 1** from the first half of Volume I (Dist. I–XXIII, from Internet Archive item `doctorisseraphic11bona`). The full Book I commentary covers 48 distinctions across two physical books:

| Part | Distinctions | IA Identifier | Status |
|------|-------------|---------------|--------|
| Vol I, dist. 1 | I–XXIII | `doctorisseraphic11bona` | OCR downloaded, 131 chunks created |
| Vol I, dist. 2 | XXIV–XLVIII | `doctorisseraphic12bona` | Not yet downloaded |

The complete Sentences commentary spans four volumes (Books I–IV), totaling approximately 2,500–3,000 pages of Latin text.
