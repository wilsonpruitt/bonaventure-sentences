# Tier-2 ambiguities — d.22 divisio

**bon-sent-I-d22-divisio, chunk boundary (raw lines 67255–67262, COMMENTARIUS opener)**: Raw OCR contains a `COMMENTARIUS IN DISTINCTIONEM XXII.` rubric block with subtitle `De fide Trinitatis, quatenus credita et intellecta per catholicos sermones exprimitur, et quidem de nominibus divinis in generali.` and opener `Post praedicta disserendum nobis videtur de nominum diversitate.` between the d.22 littera (ended ~67253) and `DIVISIO TEXTUS.` heading at 67263. Per the d.20 chunking convention (where the d.20 littera ended at 64133 and divisio began at 64135 with no commentarius rubric preserved), this rubric+opener block is dropped from the divisio chunk. `line_start` left at 67263. **Flag for project owner**: if a future policy change wants to preserve commentarius openers, all of d.20–d.22 divisio chunks should be revisited together. → Resolved per d.20 convention.

**bon-sent-I-d22-divisio, apparatus block sourcing (raw lines 67323–67326)**: OCR shows two footnote entries (`'  Ex eodem loc. cit. c. 10. n. II.` and `2  Cap. H. n. 12.`) sitting BEFORE the `NOTAE AT COMMENTARIUM` heading at 67328. These are Lombard-text apparatus from the bottom of p.389 belonging to the d.22 littera (already extracted by the d.22 littera agent — confirmed in `tier2-ambiguities-d22-littera.md` notes 7, 8). Only the seven entries under `NOTAE AT COMMENTARIUM` (lines 67328–67348) belong to the divisio. → Resolved.

**bon-sent-I-d22-divisio, NOTAE heading OCR (line 67328)**: OCR rendered `NOTAE AT COMMENTARIUM` (typo: `AT` for `AD`). Standard Quaracchi heading is `NOTAE AD COMMENTARIUM`. → Silently corrected in the apparatus blockquote intro.

**bon-sent-I-d22-divisio, fn 1 OCR cod. siglum (line 67330)**: OCR rendered `eod.  Z  et  ed.  I  Magistei:` — `eod.` likely abbreviation of `cod.` (codex), and `Magistei:` is OCR garble for `Magister.`. → Resolved as `cod. Z et ed. 1 Magister.`.

**bon-sent-I-d22-divisio, fn 2 OCR (lines 67331–67336)**: OCR has `nDivisio` (for `«Divisio`), `lerminos` (for `terminos`), `elc.` (for `etc.`), `crgo` (for `ergo`), `gemina secaretur` preserved as-is, `diffe-rentiis` line-broken. → Silently corrected.

**bon-sent-I-d22-divisio, fn 7 OCR (lines 67347–67348)**: OCR rendered `post  ntnm  addit  bene  emnia` — clearly `post unum addit bene omnia` (n/u and e/o substitutions). → Silently corrected.

**bon-sent-I-d22-divisio, body OCR garbles silently corrected**: `secundimi → secundum` (67268), `credilur → creditur` (67267), `hahet → habet` (67271, 67295), `dislinctione → distinctione` (67273), `iliud → illud` (67280), `Boelhii → Boethii` (67280), `reducilii-lis → reducibilis` (67281, 67284 line-break), `Sciend.um → Sciendum` (67284), `estigitur → est igitur` (67284), `ahas → alias` (67290), `raembra → membra` (67295), `Dcus → Deus` (67299), `TRACT.^TIO → TRACTATIO` (67303), `dkantur → dicantur` (67319). All standard OCR letter substitutions per CLAUDE.md cleanup rules.
