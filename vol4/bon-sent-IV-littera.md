---
id: "bon-sent-IV-littera"
volume: 4
book: 4
distinctio: 0
type: littera
title_la: "LIBER QUARTUS SENTENTIARUM. De doctrina signorum"
title_en: "Book Four of the Sentences — on the doctrine of signs"
printed_pages: [4]
pdf_pages: [24]
source: "S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), p. 4"
has_scholion: false
has_apparatus: false
transcription_status: "Phase C Tier 2 complete — Latin re-set from the 450 dpi full-measure bands of printed p.4 (PDF 24) with the IA djvu OCR as cross-check only (raw L1161–1166), fresh literal English translation, no apparatus (p.4's footer nn.1–7 all answer to bon-sent-IV-capitula below it — every anchor read on the table), no [?] flags (2026-08-20)"
format_version: 1
---

# bon-sent-IV-littera

## *Book Four of the Sentences — the Master's text*

---

## Latin
<!-- page 4 -->

# LIBER QUARTUS SENTENTIARUM

### DE DOCTRINA SIGNORUM.

His tractatis quae ad doctrinam rerum pertinent, quibus fruendum est, et quibus utendum est, et quae fruuntur et utuntur, ad doctrinam signorum accedamus.

---

## English
<!-- page 4 -->

# BOOK FOUR OF THE SENTENCES

### ON THE DOCTRINE OF SIGNS.

These things having been treated which pertain to the doctrine of things — the things which are to be enjoyed, and the things which are to be used, and the things which enjoy and use — let us approach the doctrine of signs.

---

## Notes

**Provenance.** Printed p. 4 (PDF 24; offset `pdf = printed + 20`), raw
`bonaventure_vol4_raw.txt` L1161–1166. The unit is **full-measure display matter plus one
sentence**, so it was re-set from full-width 450 dpi bands of the head of the leaf rather than
through `colcrop`; the OCR served only as a cross-check (it gives `Iractalis` for **tractatis**,
`acl` for **ad**, `perlinent` for **pertinent**, `siguorum` for **signorum**).

**What this chunk is.** Lombard's own opening of Book IV: the book title, its one-line subtitle, and
the single transition sentence that hands the reader from the *doctrina rerum* of Books I–III to the
*doctrina signorum* — the Sacraments — of Book IV. It sits between `bon-sent-IV-proem` (which closes
about a fifth down p. 3) and `bon-sent-IV-capitula`, whose `INCIPIUNT CAPITULA QUARTI LIBRI.` opens
further down this same leaf.

**★ THE EDITORS SAY WHY THIS UNIT IS HERE AT ALL — AND IT IS THE PROEM'S OWN LAST NOTE.**
`bon-sent-IV-proem`'s p. 3 n. 5 records that in the codices the proemium's closing sentence runs
straight on into the *divisio textus,* and that Quaracchi, following the Vatican edition,
**interjected the Master's text** at this point (*Nobis autem cum Vaticana interiiciendus erat textus
Magistri*). Book II's p. 6 n. 6 says the same thing in the same words. So this chunk's existence and
its boundaries are the edition's own decision, stated in the edition's own apparatus.

**★★ NO APPARATUS, AND IT WAS VERIFIED RATHER THAN ASSUMED.** p. 4's footer register carries
**seven** entries and **all seven answer to the chapter list below the littera**, each traced to its
anchor on the table: n. 1 → dist. I cap. IV *Quo¹ differant signum et Sacramentum* · n. 2 → dist. I
cap. V *Quare instituta sint²* · n. 3 → dist. II cap. I *De Sacramentis novae legis³* · n. 4 →
dist. III cap. IV *Si in nomine Patris possit tradi baptismus⁴* · n. 5 → dist. IV cap. VI *Quid
dimittitur⁵ in baptismo iustis* · n. 6 → dist. IV cap. VII *…quem recipit iustus⁶* · n. 7 →
dist. VII cap. III *Quae⁷ sit virtus huius Sacramenti.* The title, the subtitle and the transition
sentence carry **no anchor of any kind**, read at magnification on the band. The chunk therefore
declares `has_apparatus: false`. This is the same shape as `bon-sent-II-littera` (whose p. 7 held two
footer notes, both the capitula's) — and the **opposite** of `bon-sent-III-littera`, whose p. 3 did
own two entries. **The shape does not port between books; read the anchors.**

**★ AND THE SAME READING SETTLES THE NEXT CHUNK.** Because all seven notes sit **on the chapter list
itself** and record its transmission (codices' variant chapter wordings, an omitted capitulum, cod. D's
added eighth capitulum), the frozen test — *a capitula table is transmitted text when it carries
apparatus ON the table* — is **already satisfied for `bon-sent-IV-capitula`.** It is chunked and
translated, exactly as Books II and III were. Do not re-decide it.

**★ THE HEADING PRINTS WITHOUT A FULL STOP.** `LIBER QUARTUS SENTENTIARUM` carries no period on the
plate (Books II and III both print one); `DE DOCTRINA SIGNORUM.` does. Transcribed as printed.

**Gutter: not applicable.** This unit is full-measure. p. 4 is a **stacked-region leaf** — display
heading, full-measure littera, then a two-column table, then the register — and per the frozen Vol V
rule the gutter is a property of the region, not the leaf: the two-column measure on p. 4 belongs to
`bon-sent-IV-capitula` and is that chunk's to profile.

**⛔ THE THREE GUARD-RAIL AUDITS CANNOT SEE THIS CHUNK** — they select on the filename regex
`bon-sent-IV-d(\d+)-`, which a littera at distinctio 0 never matches, and all three print a clean
verdict on **0 chunks audited**. Verified instead by: eyes-on 450 dpi bands for the display matter,
the littera and the footer register; marker pairing (none in either body, `has_apparatus: false`);
structural parity between the Latin and English bodies; `build-content.mjs`; `build-citations.py`;
`polish-style-scan.py`.

**`[?]` flags: none.**
