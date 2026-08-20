---
id: "bon-sent-II-littera"
volume: 2
book: 2
distinctio: 0
type: littera
title_la: "LIBER SECUNDUS SENTENTIARUM. De rerum creatione et formatione corporalium et spiritualium et aliis pluribus eo pertinentibus"
title_en: "Book Two of the Sentences — on the creation and formation of things corporeal and spiritual, and on many other matters pertaining thereto"
printed_pages: [7]
pdf_pages: [29]
source: "S. Bonaventurae, Opera Omnia, Tomus II (Quaracchi, 1885), p. 7"
has_scholion: false
has_apparatus: false
transcription_status: "Phase C Tier 2 complete — Latin re-set from the 450 dpi full-measure band of printed p.7 (PDF 29) with IA djvu OCR cross-check (raw lines ~1094–1098), fresh literal English translation, no apparatus (p.7's two footer notes both belong to bon-sent-II-capitula — verified on the band, both concern entries in the chapter list), no [?] flags (2026-08-20)"
format_version: 1
---

# bon-sent-II-littera

## *Book Two of the Sentences — on the creation and formation of things corporeal and spiritual*

---

## Latin
<!-- page 7 -->

### LIBER SECUNDUS SENTENTIARUM.
#### DE RERUM CREATIONE ET FORMATIONE CORPORALIUM ET SPIRITUALIUM
#### ET ALIIS PLURIBUS EO PERTINENTIBUS.

Quae ad mysterium divinae Unitatis atque Trinitatis, licet ex parte, cognoscendum pertinere noscuntur, quantum valuimus, diligenter exsecuti sumus; nunc ad considerationem creaturarum transeamus.

---

## English

### BOOK TWO OF THE SENTENCES.
#### ON THE CREATION AND FORMATION OF THINGS CORPOREAL AND SPIRITUAL
#### AND ON MANY OTHER MATTERS PERTAINING THERETO.

Those things which are known to pertain to the knowing of the mystery of the divine Unity and Trinity, though in part, we have diligently carried through, so far as we were able; now let us pass over to the consideration of creatures.

---

## Notes

**Provenance.** Printed p. 7 (PDF 29), raw `bonaventure_vol2_raw.txt` L~1094–1098. The whole unit is
**full-measure display matter plus one sentence**, so it was read off a full-width 450 dpi band at
1.6–1.7× rather than through `colcrop`; the OCR served only as a cross-check.

**What this chunk is.** Lombard's own opening of Book II: the book title, its two-line subtitle, and
the single transition sentence that hands the reader from the Trinity of Book I to the creatures of
Book II. It sits between `bon-sent-II-proem` (which closes on p. 6) and `bon-sent-II-capitula` (which
opens with `INCIPIUNT CAPITULA SECUNDI LIBRI.` further down p. 7).

**★ THE EDITORS SAY WHY THIS UNIT IS HERE AT ALL.** `bon-sent-II-proem`'s p. 6 n. 6 records that the
codices run straight on from the proemium into the *divisio textus,* and that Quaracchi, following
the Vatican edition, **interjected the Master's text** at this point. So this chunk's existence, and
its boundaries, are the edition's own decision, stated in the edition's own apparatus — not an
inference of ours.

**★★ NO APPARATUS, AND THAT WAS VERIFIED RATHER THAN ASSUMED.** p. 7's footer register carries
exactly **two** entries, and **both belong to the capitula table**: n. 1 (*Codd. D F et ed. 1 hic
inserunt* ad ipsos vel, *quae lectio est satis conformis ipsi capitulo*) and n. 2 (*Pro* Quod *non
pauci codd.* Qui, *edd. 1, 3, 4, 5, 9* An possunt). Each answers to an entry in the chapter list; the
title, the subtitle and the transition sentence carry **no anchor of any kind**, read at
magnification on the band. The chunk therefore declares `has_apparatus: false`. **This is the
Sentences' first zero-apparatus chunk**; Vol V's `bon-itin-scholion` is the precedent, and the
tooling was checked against it there — a zero entry count is not a failed read.
★ Note the contrast with **Book III**, whose littera on its p. 3 *did* own two entries. **The shape
does not port between books; read the anchors.**

**★ AND THE SAME READING SETTLES THE NEXT CHUNK.** Because those two notes sit **on the chapter list
itself** and record its transmission, the frozen test (*a capitula table is transmitted text when it
carries apparatus ON the table*) is **already satisfied for `bon-sent-II-capitula`** — it is chunked
and translated, exactly as Book III's was. Do not re-decide it.

**Gutter: not applicable.** This unit is full-measure; the two-column measure on p. 7 belongs to the
capitula table below it. ⚠ p. 7 is a **stacked-region leaf** — display matter, then a two-column
table, then the register — and the whole-body profile confirms it: `gutter-profile.py 7 0.10 0.80`
returns a 117 px "band" with a 110 px ink island, which is the window straddling regions, and
`colcrop vol2 7 auto` returns a **606 px** run. Profiled over the table's own rows (0.30–0.85) the
answer is **1715**, which is what `bon-sent-II-capitula` should use.

**⛔ THE THREE GUARD-RAIL AUDITS CANNOT SEE THIS CHUNK** (they select on `bon-sent-II-d(\d+)-`) and
will print CLEAN on 0 chunks audited. Verified instead by: eyes-on 450 dpi bands for the display
matter and the footer register, `build-content.mjs`, `build-citations.py`, `polish-style-scan.py`.

**`[?]` flags: none.**
