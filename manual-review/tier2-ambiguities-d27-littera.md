# d.27 littera — Tier-2 ambiguities

Source: `vol1/bon-sent-I-d27-littera.md`. PDF/OCR pages 464–466 (raw_pt2 lines 4588–4823).

## Pars II chapter numeration / titles

The Quaracchi printed text of Distinction XXVII Pars II numbers its chapters discontinuously in the OCR/print: after the implicit opening chapter (`Hic non est praetermittendum...`), the next clearly printed heading is `Cap. IV. De generali regula...`, followed by `Cap. V. An secundum substantiam...`. There are no `Cap. II.` or `Cap. III.` headings legible on printed p.465 right column or p.466 in the OCR or in 600-dpi crops of the printed page (`/tmp/d27ultra_p-055.png`, `/tmp/d27hi5_p-056.png`).

The `tractatus`-spec for this chunk (handed to the assembler) presupposed Pars II capp. I — V, with II and III "partly illegible". Visual inspection at 600 dpi shows that:

1. The text after the close of Cap. I (`...nihil autem horum pater dicitur») flows directly into the *Aperte ostensum est...* paragraph, which the editor marks in the margin **Epilogus** — i.e., as the epilogue of the preceding material, not as a new lemma with its own title.
2. No `Cap. II.` or `Cap. III.` printed heading is found between the close of Cap. I and `Cap. IV. De generali regula...`.

In the rendered file, to keep the published chapter numerals consistent with the printed Quaracchi page, the assembler:

- Set the *Aperte ostensum est...* paragraph as `Cap. II. *[?]*` (titled `[?]` because no printed title is legible; the *Epilogus* margin note suggests the editor treats it as Cap. I's epilogue rather than a new lemma).
- Inserted a placeholder `Cap. III. *[?]*` block at the foot of p.465 / head of p.466 noting that **no Latin body is missing**: the question is purely whether the chapter numerals jump (from the implicit opening chapter of Pars II to *Cap. IV*) or whether II–III are absorbed into the opening chapter of Pars II.
- Kept `Cap. IV. *De generali regula...*` and `Cap. V. *An secundum substantiam...*` with their printed titles intact.

**Resolution (recommended):** at the next eyes-on PDF pass, decide between:

- (a) Drop the `Cap. III. [?]` placeholder, fold *Aperte ostensum est...* under `Cap. I` as its *Epilogus*, then renumber `Cap. IV → Cap. II`, `Cap. V → Cap. III` (clean three-chapter Pars II), **or**
- (b) Confirm there really are intervening Cap. II/III headings (very small font, rule-broken in the OCR) and supply the titles from the IA print or another Quaracchi pressing.

Either resolution preserves all body text — only the chapter-numeral display changes.

## Apparatus anchor positions (approximate)

The OCR for the body of pp.464–465 shows footnote markers as inconsistent glyphs (`^`, `^^`, `*`, stray `2`/`3` digits). Anchors `[^4]`, `[^5]`, `[^9]`, `[^14]` were placed at the closest unambiguous body positions; refinement to the exact word-of-attachment would require eyes-on PDF.

- `[^4]` (`Vat. et omnes aliae edd. id est contra codd.`) was attached after *scilicet* near the foot of p.464 right column; the exact phrase to which the variant pertains may be elsewhere within the surrounding sentence.
- `[^5]` (`Vat. et aliae edd., excepta 1, dicimus contra codd.`) was attached at *significamus* (top of p.465 left column) — context implies this is the *significamus* / *dicimus* variant, but verify.
- `[^9]` (`Dist. XXVI. c. 2, et hic c. I.`) was placed at *quae supra diversis significatae sunt modis* (close of Pars I Cap. III) — fits sense.
- `[^14]` (`Cap. 13. n. 14...`) was placed at *Idem in quinto* opening the final Augustine quotation of Pars II Cap. I — fits sense.

## OCR fixes silently applied (sample)

`paler`→`pater`, `Paler`→`Pater`, `Patrera`/`Patreni`→`Patrem`, `proprielates`→`proprietates`, `dislinguunlur`→`distinguuntur`, `qidbits`→`quibus`, `Naturaergo`→`Natura ergo`, `Spirilus`→`Spiritus`, `liaec`→`haec`, `fdiatio`→`filiatio`, `genilus`→`genitus`, `bypostasim`→`hypostasim`, `subsistenliam`→`subsistentiam`, `lautum`/`tautum`/`tanlum`→`tantum`, `vocabida`→`vocabula`, `relaliones`→`relationes`, `signiflcamus`/`signiflcant`/`signiflcalur`/`signiflcarentur`→`significamus` etc., `pateryiali`→`paternali`, `Triuitas`→`Trinitas`, `COMMENTAEIUS`→`COMMENTARIUS`, `Dcus`→`Deus`, `terniinant`→`terminant`, `slases`→`stases`, `hyposlasi`→`hypostasi`, `proprielas`→`proprietas`, `seniper`→`semper`, `etproprium`→`et proprium`, `Filiiun`→`Filium`, `gi-gnere`→`gignere`, `proprielates singulae`→`proprietates singulae`, `paler`→`pater` (lowercase), `flliali`→`filiali`, `slases`→`stases`, `ai*:`→`ait:`, `eaderaque`→`eademque`, `eadera`→`eadem`, `iraago`→`imago`, `verbura`→`verbum`, `paterni`→`paterni`, `lulerque`→`uterque`, `iUae`→`illae`, `iUud`→`illud`, `noinina`→`nomina`, `nomlne`→`nomine`, `inlerdum`→`interdum`, `Trinilatis`→`Trinitatis`, `Augu-stinus`→`Augustinus`, `slinus`→`stinus` (joined), `racteristica`→`characteristica` (line-break recovery from `cha-` + `racteristica`), `idiomata`→`idiomata`, `Item '`→`Item:`, `intemporaliter`→`intemporaliter`, `aeternaliter`→`aeternaliter`, `homoousion`→`homoousion`, `differenliam`→`differentiam`, `hypostaseou`→`hypostaseon`, `flliris`→`filius` (in *Aperte ostensum est, quod swaifiliris vel genitus* the OCR reads `swaifiliris` — corrected to `sicut filius`), `notiones ipsas tan-tum signiflcamus`→`notiones ipsas tantum significamus`, `essentianv`→`essentiam`, `dixerit`/`(versio in)`/`(aTivi tlai...)`→Greek apparatus restored from page footer.

## Greek-glyph apparatus

The Greek in `[^6]` and `[^8]` was reconstructed from the garbled Roman/Greek mixture in raw lines 4741–4750 against the standard text of John Damascene, *De fide orthodoxa* III. cc. 5–7. The reconstruction is conservative and matches the printed Quaracchi.
