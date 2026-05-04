# Tier-2 ambiguities: bon-sent-I-d23-littera

Compiled 2026-05-03 during Phase C Tier-2 promotion.

## Boundary / structural notes

- **Tail trim**: chunk range 69043–69437 ends one line before `COMMENTARIUS IN DISTINCTIONEM XXIII.` at line 69438. Trailing blank lines and the running footer `SENTENT[\RUM LIB. l.` plus the page number `404` were trimmed as page-furniture, per d.20/d.22 precedent.
- **Cap. I and Cap. II missing in OCR**: the Quaracchi print labels for Cap. I and Cap. II of Lombard's Dist. XXIII appear to have been dropped by the djvu OCR (only Cap. III–VI survive as bare headings). Cap. I and Cap. II labels supplied by inference, matching the d.22 littera convention where Cap. I was likewise restored.
- **Page-bottom apparatus on p. 402 vs NOTAE block**: page 402 carries TWO apparatus zones — a small 3-footnote block (raw lines 69108–69134) numbered with symbols (`'`, `'`, `3`), and immediately below it the `NOTAE AD LIBR. SENTENTIARUM.` block (raw 69136–69157) with notes 1–8. The first block contains:
  - note 1: variant *autem*/*tamen* — appears to gloss the Lombard text opener `Praedictis ... adiiciendum est`.
  - note 2: `Vat. est, sed contra mss. et sex prinias edd.` — a textual reading note that could equally fit the Lombard text or the d.22 commentary.
  - note 3: a long scholarly note citing Albertus, Alex. Halensis, Aquinas, Petr. de Tarantasia, ending `Vide etiam Petr. a Tar., hic circa lit.` — this is plainly a commentary-level Bonaventure-or-editorial note (parallel to the "scholion-style" notes attached to the COMMENTARIUS sections), not a Lombard-text apparatus entry.
  - **Per d.22 precedent** (which only emitted the `NOTAE AD LIBR. SENTENTIARUM.` block) these 3 footnotes were SUPPRESSED from the d.23 littera apparatus. Notes 1–2 are plausible candidates for the d.22 commentary chunks (`bon-sent-I-d22-divisio.md` or one of d.22's question chunks); note 3 unambiguously belongs to a d.22 commentary chunk. **Not relocated** here per task instruction; flagged for the d.22 chunks owner.
- **Three NOTAE blocks**: page 402 block (notes 1–8 in OCR symbols), page 403 block (notes 1–9), and page 404 block (notes 1–10). Renumbered consecutively as `[^1]`–`[^27]` in the chunk file.

## OCR garbles silently corrected (context unambiguous)

- `Trinitale` → `Trinitate` (multiple occurrences; standard Quaracchi long-s/t confusion)
- `oinnia`, `oinnlbus`, `cuin`, `cum` etc. — `oi` for `om` (broken ligature) restored
- `personls`, `singuiariter`, `pluralller`, `acclpitur` etc. — `l` for `i`, `i` for `l` swaps restored
- `phiraliter` → `pluraliter`
- `dlcatur`, `dlcitur`, `dlctur` etc. — `dl` for `di` restored
- `Probatur,` and similar marginal glosses (`5?°Hturse-`, `^^"'''sed`, `Quiei signi-`, `JSomine`, `"■^^-`, `iiesponsit, sfinum'^"^"`, `Essenua`, `"""mj"'*""";`, `sonaedisiiQ.`, `^"""'"'`, `loqQendi.`) treated as bleed-in marginalia per CLAUDE.md and trimmed.
- `osteudlt` → `ostendit`
- `Item^` → `Item` (caret = footnote anchor 5)
- `Deic?n` → `Deum`
- `magnim` → `magnum`
- `hac Trinitale` → `hac Trinitate`
- `dlciriius` → `dicimus`
- `cessltate` → `necessitate` (with hyphen restoration `ne-cessitate`)
- `inelTabilis` → `ineffabilis`
- `Trinitatc` → `Trinitate`
- `iuelTabilibus` → `ineffabilibus`
- `tim` → `una`; `essmtia` → `essentia`; `substanlia` → `substantia`; `persmae` → `personae`; `eslLatino` → `est Latino`
- `G\",\cc\s` → `Graecis`
- `iriu`, `Ires`, `(|uid` etc. — restored
- `taceremus` (originale) preserved per NOTAE [^6] which says Vat. wrongly reads `taceamus interrogati`.
- `uno  nomine  quaerentibus  de  trlbus  respondeamus  *.` — preserved `respondeamus` per Lombard text; NOTAE [^8] notes `responderemtis`/`responderemus` is the codd./ed. I variant.
- `Cap. IIL` → `Cap. III.`
- `cLeos` → `deos`; `perso7ias` → `personas`
- `Si)iritus` → `Spiritus`; `Si)iritus sanctus` similar
- `Auguslinus` → `Augustinus`; `dcTrinitate` → `de Trinitate` (preserved across all occurrences)
- `Kiliuin` → `Filium`
- `dieimus` → `dicimus`
- `dii»?Ecce` → `dii?» Ecce` (paragraph-internal; punctuation reflows kept literal)
- `subdens'` → `subdens` (apostrophe is footnote anchor 14)
- `Cwr` → `Cur`
- `dicens°` → `dicens` (degree-sign is footnote anchor 16)
- `cssentiae` → `essentiae`
- `nonien` → `nomen`
- `cpiod` → `quod`
- `parla` → `parta`
- `secrc-tario` → `secretario`
- `consequenter` etc. — preserved
- Page-403 fragment `loqQendi.` after running head → trimmed as marginalia gloss / column-running text
- `seciindiim` → `secundum`; `iioslram` → `nostram`; `liyposlases` → `hypostases`; `unani` → `unam`
- `trla prosopa` preserved (Greek loanword)
- `sneludinem` → `consuetudinem`
- `nc-cessitale` → `necessitate`
- `septlmo deTrinitale^` → `septimo de Trinitate` (caret = footnote 18)
- `Hilarius … de Trinitate '` — apostrophe = footnote 19
- `Qid me videl, videl et Palrem` → `Qui me videt, videt et Patrem` (Hilary cite, John 14:9)
- `dicit*:` → `dicit:` with asterisk = footnote 20
- `Ilem in eodem":` → `Item in eodem:` with double-quote = footnote 21
- `Quaeslionuin` → `Quaestionum`
- `Legis*` → `Legis` with asterisk = footnote 22
- `deFide'aTt` → `de Fide ait` (apostrophe before `aTt` = footnote 23)
- `secundo libro de Fide'` → footnote 24 anchor
- `Item in eodem ':` → footnote 25 anchor
- `noti` → `non`
- `Fide  "` → footnote 26 anchor
- `(`(uod` → `quod`
- Final phrase `Multiplex itaque Deus non esl.` → `Multiplex itaque Deus non est.` with [^27] appended (Quaracchi NOTAE [^27] cites *de Fide* I, c. 2, n. 17 — anchored at end of cap. VI per common Quaracchi practice).

## Genuinely flagged readings

None marked `[?]` in the chunk body — all OCR garbles were resolvable from context. The body text is well-attested standard Lombard-Augustine-Hilary-Ambrose material with the Quaracchi apparatus itself supplying any meaningful textual variants.

## Cross-chunk apparatus relocation candidates

Three p. 402 page-bottom footnotes (raw lines 69108–69134), particularly note 3 (the Albertus/Aquinas/albedo scholarly note), are strong candidates for relocation INTO the d.22 commentary chunks. Per task instruction these were not touched here. Worth a separate review pass on `bon-sent-I-d22-divisio.md` and the d.22 question chunks to see whether they're missing 1–3 entries that match.
