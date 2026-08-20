---
id: "bon-sent-III-littera"
volume: 3
book: 3
distinctio: 0
type: littera
title_la: "LIBER TERTIUS SENTENTIARUM. De incarnatione Verbi et humani generis reparatione"
title_en: "Book Three of the Sentences — on the incarnation of the Word and the repair of the human race"
printed_pages: [3]
pdf_pages: [25]
source: "S. Bonaventurae, Opera Omnia, Tomus III (Quaracchi, 1887), p. 3"
has_scholion: false
has_apparatus: true
transcription_status: "Phase C Tier 2 complete — Latin re-set column-by-column from 450 dpi PDF bands of printed p.3 (PDF 25) with IA djvu OCR cross-check (raw lines 832–886), fresh literal English translation, apparatus nn.1–2 from the p.3 footer (nn.3–8 on the same page belong to bon-sent-III-capitula), no [?] flags (2026-08-19)"
format_version: 1
---

# bon-sent-III-littera

## *Book Three of the Sentences — the Master's prologue*

---

## Latin
<!-- page 3 -->

# LIBER TERTIUS SENTENTIARUM.

### DE INCARNATIONE VERBI ET HUMANI GENERIS REPARATIONE.

Iam nunc his intelligendis atque pertractandis, quae ad Verbi incarnationem pertinent, integra mentis consideratione intendamus, ut de ineffabilibus vel modicum aliquid fari, Deo revelante, valeamus[^p3-1]. Sic enim rationis ordo postulat, ut, qui in primo libro de inexplicabili mysterio summae Trinitatis irrefragabili Sanctorum attestatione aliquid diximus, ac deinde in secundo libro conditionis rerum ordinem hominisque lapsum sub certis[^p3-2] auctoritatis regulis insinuavimus, de eius reparatione, per gratiam Mediatoris Dei et hominum praestita, atque humanae redemptionis Sacramentis, quibus contritiones hominis alligantur ac vulnera peccatorum curantur, consequenter in tertio et quarto libro disseramus, ut Samaritanus ad vulneratum, medicus ad infirmum, gratia ad miserum accedat.

---

## English
<!-- page 3 -->

# BOOK THREE OF THE SENTENCES.

### ON THE INCARNATION OF THE WORD AND THE REPAIR OF THE HUMAN RACE.

Now let us bend the mind's whole consideration to the understanding and the treating of those things which pertain to the incarnation of the Word, so that we may be able — God revealing it — to utter at least some little about things unutterable[^p3-1]. For the order of reason demands this: that we who in the first book said something concerning the inexplicable mystery of the highest Trinity, on the irrefragable attestation of the Saints, and who then in the second book set forth the order of the founding of things and the fall of man under sure rules[^p3-2] of authority, should consequently in the third and fourth books discourse concerning his repair — bestowed through the grace of the Mediator of God and men — and concerning the Sacraments of human redemption, by which the bruises of man are bound up and the wounds of his sins are healed: so that the Samaritan may come to the wounded man, the physician to the sick, grace to the wretched.

---

## Apparatus

> The numbered footnotes below correspond to markers in both the Latin body above and the English translation. Quaracchi restarts footnote numbering on each printed page, so the markers are page-qualified (`p3-`).

[^p3-1]: **La.** Repetimus hanc propositionem iam in fine ultimae distinctionis II. libri Sententiarum positam.
    **En.** We repeat here the statement already set at the end of the last distinction of the second book of the Sentences.

[^p3-2]: **La.** Ed. 1 *subiectis*, deinde pro *auctoritatis* cod. A *auctoritatum*.
    **En.** Edition 1 reads *subiectis*; then, for *auctoritatis*, codex A reads *auctoritatum*.

---

## Notes

**Provenance.** Latin re-set column-by-column from 450 dpi PDF bands of printed p.3 (PDF 25, offset `pdf = printed + 22`), cross-checked against the IA djvu OCR (`bonaventure_vol3_raw.txt` raw lines 832–886). The plate was needed: the OCR gives `intelligentlis` for **intelligendis**, `auctoritalis` for **auctoritatis**, `bumanae`, `euranlur`, `mcdicus`, and `ordiuem`.

**Type.** `littera` — the Master's own text, the prologue opening Lombard's Book III. `distinctio: 0`: it prints before Distinction I, which begins *Cum venit igitur plenitudo temporis* on p.6. Bonaventure's own proemium (`bon-sent-III-proem`, pp.1–2) ends by quoting that incipit.

**★★ THIS PAGE HOLDS TWO UNITS AND ITS FOOTER SPLITS 2/6 WHILE ITS BLOCKS SPLIT 4/4.** Printed p.3 carries the Master's prologue at the head, then the full-width display heading `INCIPIUNT CAPITULA TERTII LIBRI.` — **which crosses the gutter** (the OCR shatters it as `I.NCIPIU.NT CAPITULA` in the left column and `TERTII LIIIRI.` in the right) — and then the Capitula begin **on this same leaf**, running Distinctio I through Distinctio VI. So:
- **Footer BLOCKS divide 4/4** — nn.1–4 in the left block, nn.5–8 in the right.
- **Footer ANCHORS divide 2/6** — only **nn.1–2** answer to this chunk (both in the prologue's single paragraph). **nn.3–8 all anchor in capitula entries** (`potuerit³ incarnari`, `intelligendum sit⁴`, `qualis ante⁵ fuerit`, `dicit⁶ Christum`, `assumserit⁷ hominem`, `ponit⁸`) and belong to `bon-sent-III-capitula`.

A reader dividing this register by block would hand two of the Capitula's notes to the prologue. The standing rule — *read anchors, only anchors* — is what decides it.

**★ THE PAGE-LEVEL GUTTER MEASUREMENT IS WRONG HERE, AND ITS RUN WIDTH SAYS SO.** `colcrop.py vol3 3 auto` returns `split_x=1570` on a **126 px** run. That is far above the sound 58–64 px band, which is as much a failure signal as far below it — the profile is straddling two regions set to different measures (the prologue's two columns, and the Capitula's narrower indented entries below the display heading). Profiled over the prologue's own rows (1500–2000 of 5049) the band is **1487–1526, width 40 → split 1506**, and that is the value this chunk was cut at. Same species as the Itinerarium p.313 case in CLAUDE.md: *a gutter is a property of a region, not of a page.*

**Apparatus count.** 2 entries owned (p.3 nn.1–2 of 8 on the page).

**Hand-off forwarded.** `bon-sent-III-capitula` takes p.3 nn.**3–8** together with the `INCIPIUNT CAPITULA TERTII LIBRI.` display heading, and runs pp.3–6 to `EXPLICIUNT CAPITULA TERTII LIBRI.` ⚠ **It shares printed p.6 with `bon-sent-III-d1-littera`** (which already claims pp.6–7), so p.6's footer must be divided by anchor between them and the existing chunk checked for what it already holds.

**[?] flags.** None — p.3 fully legible at 450 dpi.
