# Tier-2 ambiguities — bon-sent-I-d25-dubia

Promotion date: 2026-05-03
Raw range: lines 2773–2999 of `raw/bonaventure_vol1_pt2_raw.txt` (vol. I pt. 2; PDF offset −410)
Printed pages: 445–447 (PDF pp. 35–37 of `doctorisseraphic12bona.pdf`)

## Structure verification

- **Dubia count: 4** (DUB. I, DUB. II, DUB. III, DUB. IV). Confirmed by full read of the raw range.
- DUB. III in OCR is rendered `DuB.   m.` (line 2850) — the `m.` is a misread of Roman numeral `III.`. Silently corrected.
- DUB. IV in OCR is rendered `DuB.   IV.` (line 2863) cleanly.
- No additional un-numbered appendix block (e.g. d.22-style `QUINQUE REGULAE`) appears between any two dubia.
- DUB. IV's response ends at "ordinem in cognoscendo" in col B of printed p. 447; immediately after, col B begins `DISTINCTIO XXVI. Cap. I.` (handled in `bon-sent-I-d26-littera.md`). The transition is clean.

## Two-column layout reflow

All three printed pages (445, 446, 447) are set in 2 columns. The IA OCR interleaves the two columns line-by-line by horizontal whitespace position, so each row contains a fragment of col A (left) and a fragment of col B (right). Reflow protocol used: read all col-A rows top-to-bottom for prose continuity, then col-B rows top-to-bottom, then stitch col-A → col-B for each page (since the Quaracchi columns flow A→B→next-page-A→next-page-B).

- **p. 445**: col A = DUB. I header + entire DUB. I body up to "...cui sub-"; col B begins with the wrap-completion "sistentia est; et sic plurificatur. Ratio autem huius est communis usus..." then DUB. II header and DUB. II opening.
- **p. 446**: col A = DUB. II continuation ("praepositiones sunt transitivae..." through end of DUB. II response and DUB. III header + DUB. III body); col B = DUB. III response ("Respondeo: Dicendum, quod unaquaeque res...") through end of DUB. III, then DUB. IV header and DUB. IV body opening ("Item quaeritur de hoc verbo Hieronymi: Non est prorsus aliquis in Trinitate gradus...").
- **p. 447**: col A = DUB. IV body continuation ("ad superius: ergo ibi est sub et super..." through "Unitas est substantia non habens positionem; ideo est in"); col B = DUB. IV response continuation ("spiritualibus. Sic gradus dicit superpositionem...") through final words "ordinem in cognoscendo". After that, col B begins d.26 territory.
- One inversion noted at the very top of p. 445 col B: OCR rows 2773–2776 have the wrap-fragment "autem huius est com- / [blank] / est; et sic plurificatur. Ratio / munis usus..." in a slightly scrambled top-of-column order. The natural prose reconstruction is "...cui subsistentia est; et sic plurificatur. Ratio autem huius est communis usus." Adopted.

## Apparatus reflow and renumbering

The footer apparatus blocks on pp. 445 and 446 are also 2-column; reflowed col-A-then-col-B. Footnote glyphs in the OCR vary (`'`, `^`, `3`, `•`, `8`, `"`, `1°`, `12`, etc.) — counted in printed-page order to assign markers [^1]–[^20]:

- **p. 445** (5 notes): [^1] Codd. *aa bb cc* *antonomastice* (col A, glyph `'`); [^2] Ed. 1 *subiicit etiam* (col A, glyph `'`); [^3] Cod. *G* *sola analogia* (col A, glyph `3`); [^4] Boethius Cap. 3 (col A, glyph `•` — long; wraps from col A bottom into col B top of footer); [^5] Vide supra pag. 412, nota 7 (col B, glyph `^`).
- **p. 446** (11 notes): [^6] Cfr. supra d. 5; [^7] Vat. *aliquando*; [^8] Sic vetustiores codd.; [^9] Libr. XVIII *Grammat.* c. 1 (Priscian); [^10] Cap. 5. n. 5; [^11] Vat. omittit *quod recipitur*; [^12] Vat. supprimitur *unaquaeque*; [^13] Notamus, quod *rei* primo et tertio modo (long Quaracchi note on prima/secunda intentio); [^14] Verba *et sic, quia anima omnia accipit* a Vat. suppressa; [^15] Cfr. supra d. 1. dub. 7; [^16] Etsi codd. allegant Lib. 9 *Confessionum* (Pseudo-Augustine *Quaestiones* q. 122 + Tertullian *adv. Prax.* c. 2).
- **p. 447 col A only** (4 notes): [^17] Vers. 26 + Glossa apud Lyr. (*Non ascendes per gradus*); [^18] Aristot. I. *Poster.* c. 23 (*Unitas substantia est sine positione*); [^19] Cfr. supra d. 20. a. 2; [^20] Cfr. supra d. 16. dub. 4. 5. The col-B footer of p. 447 (NOTAE AD LIBR. SENTENTIARUM block) is d.26 territory and is NOT included here.

### p. 446 note 12 OCR truncation (resolved without `[?]`)

OCR line 2914 reads "Val.   cum paucis tantum n" — the note is truncated mid-word at the end of the page-446 footer block in the OCR stream. In the printed apparatus this is a textual-variant note about the *Confessions* citation. Quaracchi's full note text is recoverable as note [^16] above (the long *Etsi codd. et edd. concordes allegant Librum 9. (vel 11.) Confessionum...* note). Because the surviving OCR fragment "Val. cum paucis tantum n..." reads as the OPENING of a different short note rather than the continuation of the long [^16] note, it is most likely the abbreviated apparatus entry that anchors at the *subsistentia* marker in DUB. IV's body ("in divinis est subsistentia") — but it is unrecoverable from this OCR alone. **Adopted as `[^16]`-only mapping for the *Confessions* anchor; the DUB. IV "subsistentia" anchor is left without a numbered marker** (the note that would have anchored there is the truncated "Val. cum paucis tantum n..." fragment, which I cannot reconstruct without the printed page). Flag for owner review against the printed PDF p. 446 footer note 12.

## Anchor-position uncertainties (no inline `[?]`, but flagged)

The anchor positions for the following body markers are best-fit guesses from content rather than directly visible OCR markers, due to glyph noise in the OCR:

- **[^2]** ("Marcum Tullium") — apparatus content "Ed. 1 *subiicit etiam*" describes a nearby textual variant; the exact lemma is not specified in the note. Anchored at "Tullium" because that is the second-glyph position visible in the OCR for col A of p. 445.
- **[^3]** ("Ratio" in col B of p. 445) — apparatus "Cod. *G* *sola analogia*" suggests a nearby variant where Cod. G writes "analogia" alone. Best-fit placement is at "Ratio" (which "analogia" might gloss/replace), but could equally anchor a few words earlier or later.
- **[^7]** anchored at "quando aliquid"; **[^11]** at "unaquaeque"; **[^12]** at "componere et dividere"; **[^14]** at "rationis"; **[^15]** at "Confessionum" — all on direct-content matches with the apparatus text.

## OCR silent corrections in body

All routine letter-substitution OCR garbles, not flagged inline:

- `Ilem` → `Item` (lines 2783, 2794, 2852, 2866)
- `perso7ias` → `personas`
- `essenlia` → `essentia` (multiple)
- `subsistenlia` → `subsistentia`
- `persooae` → `personae`
- `es^m^me` → `essentiae`
- `aUis` → `aliis`
- `aUerum` → `alterum`
- `ahquid` → `aliquid` (line 2826)
- `aocidentibus` → `accidentibus`
- `recipilur` → `recipitur` (multiple)
- `iilud` → `illud`
- `ahud`/`Aliud` distinction preserved
- `nuUo` → `nullo`
- `aho` → `alio`
- `?-es` → `res`
- `huiusrnodi` / `huiusraodi` → `huiusmodi`
- `forniam` → `formam`
- `signifieationi` → `significationi`
- `ratitudinem`/`stabihtatem` → `stabilitatem` / `ratitudinem` (preserved as in printed)
- `obiieitur` → `obiicitur`
- `inteUigendi` → `intelligendi`
- `inteUigi` → `intelligi`
- `Cnde` → `Unde`
- `corporahbus` → `corporabilibus`→ corrected to `corporalibus`
- `gradiis` → `gradus`
- `tollal` → `tollat`
- `pouitur` → `ponitur`
- `prout` / `pront` → `prout`
- `principii` / `principm` → `principii`
- `transilivae` / `transilivi` → `transitivae` / `transitivi`
- `denominaiu` → `denominans` (footer)
- `traliit` → `trahit`
- `signiflcationem` → `significationem`
- `ISon` → `Non` (line 2866 — DUB. IV opening)
- `flunt` → `fiunt` (NB: not in d.25 dubia range; in d.26 portion)
- `dicilur` → `dicitur`
- `puncliis` / `punclus` → `punctus`

DUB. III header in OCR: `DuB.   m.` → `DUB. III.` (silent fix).
DUB. IV header in OCR: `DuB.   IV.` → `DUB. IV.` (silent fix; case normalization only).

## OCR silent corrections in apparatus

- [^1]: `antonoma^stice` → `antonomastice`; `flgura` → `figura`; `quolies` → `quoties`.
- [^2]: `eiiam` → `etiam`.
- [^4]: `quod ipsum aocidentibus` → `quod ipsum accidentibus`; `accidentibus` punctuation; `restauraviraus` → `restauravimus`.
- [^5]: `Vat,` → `Vat.`; `subsisteridi` → `subsistendi`.
- [^7]: `Val.` → `Vat.`; `atiquando` → `aliquando`; `denominaiu` → `denominans`; `Posl` → `Post`.
- [^8]: `Sic vetustioi-es` → `Sic vetustiores`.
- [^9]: `Libr. XVlll. Grammat.` → `Libr. XVIII. Grammat.`; `Cfr` punctuation; `Ale.x.` → `Alex.`.
- [^10]: `Cap. S. n. S.` → `Cap. 5. n. 5.` (S = misread 5).
- [^11]: `cum.` → `cum`; `recipilur` → `recipitur`; `koc` → `hoc`; `paulo infe-/rius` → `paulo inferius`.
- [^12]: `nnaqnaeque` → `unaquaeque`.
- [^13]: `iVotamus` → `Notamus`; `terlio` → `tertio`; `elsecunda` → `et secunda`; `tt » modernis` → `a modernis`; `nun-/cupatur` → `nuncupatur`; `re-/praesentatur` → `repraesentatur`; `raliona\e` → `rationale`; `atlributis` → `attributis`; `S!(6j>cfam` → `subiectum`; `potcst` → `potest`; `complectitur` (margin glyph stripped); `concomilantur` → `concomitantur`; `Val.` → `Vat.`; `loquend'` → `loquendi`.
- [^14]: `auctoritale` → `auctoritate`; `recepimus` (no change).
- [^15]: `Confcssionum` → `Confessionum`; `inscribitur:` (no change); `verbum lamen` → `verba tamen`; `polestate` → `potestate`.

## `[?]` flag count

- **0 inline `[?]` flags** in the chunk body. All OCR garbles are routine, unambiguously fixable letter-substitutions in well-attested formulae and textual variants.
- **2 flagged uncertainties in this log**:
  1. p. 446 footer note 12 ("Val. cum paucis tantum n…") OCR-truncated; not surfaced as a numbered apparatus entry in the chunk; the body anchor that would have carried it (DUB. IV "in divinis est subsistentia") is currently unmarked. Resolvable from the printed PDF p. 446.
  2. Anchor positions for [^2] and [^3] on p. 445 (col A "Marcum Tullium" and col B "Ratio") are best-fit content matches rather than direct-glyph anchors; both are within ±1 sentence of the correct position.
