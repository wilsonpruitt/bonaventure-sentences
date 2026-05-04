# Tier-2 ambiguities — bon-sent-I-d24-a3-q1

Source: `raw/bonaventure_vol1_pt2_raw.txt` lines 1165–1285. Printed pages 428–429 (pdf 18, 19).

## Body

- **opener "tertia differentia"** (raw line 1171): OCR reads `de tertia differentia ^`. The `^` glyph is the footnote anchor for fn 1 (Vat. textual variant). Placement in body kept after *differentia*. No textual question, marker only.
- **fundamentum 2, "hoc non est ratione pluralitatis"** (raw line 1206): OCR `hoc    '    non est ratione pluralilatis` — anchor `'` placed after *hoc*; corrected `pluralilatis` → `pluralitatis` silently (OCR `l↔t`).
- **contra 2, "distinctum et indistinctum"** (raw line 1231): OCR `indistinctum ^`. The fn it triggers (fn 7 in our numbering) gives a Vat. textual variant `ergo hoc nomen Trinitatis si recipiatur in divinis...`; the variant string lives in the apparatus, not the body. **[?] flagged**: the apparatus-side phrasing also includes `reputatur pro recipitur`, but raw OCR shows `repmtur` — silently restored to *reputatur* as the obvious Quaracchi variant on *recipitur*. Confidence high; flagged for cross-check against PDF.
- **contra 3 hymn lines** (raw lines 1240–1243): OCR runs `Qui supra caeli residens cacumen / Tolius mundi macliinam gubernat, / Trinus et unus`. Silently corrected `Tolius → Totius`, `macliinam → machinam` (OCR `cl↔ch`, `t↔t`). Marker `'` after *unus* → fn 9 (Breviarium gothicum reference). High confidence.
- **respondeo "speciali modo"** (raw line 1213): OCR has `speciali modo*`. Marker `*` placed after *modo* anchoring fn 10 (Vat. omits *modo*). High confidence.
- **respondeo "huiusmodi nomina important pluralitatem et unitatem"** (raw line 1217): OCR `unitatem^`. Marker s belongs to fn ("Cod. Y addit simul"). **[?] dropped from final**: the variant only adds *simul* once and is captured implicitly in the apparatus chain; not promoted to a separate footnote anchor — merged into context. **Logged here**: if a later editor wants every variant marker preserved, add fn between fn 10 and fn 11 with `Cod. Y addit simul.`
- **ad 2 "nullum nomen simul importat"** (raw line 1230): OCR `importat"`. Marker `"` → fn 11 (cod. T `qui` variant). Placement after *importat*. High confidence.
- **ad 3 "intelligendum in relativis"** (raw line 1242): OCR `intelligendum in "`. The trailing `"` glyph anchors a fn (`Vat. cum solo cod. cc de.`). **[?] flagged**: this final variant note (`de` for `in`) is too sparse to render as a meaningful standalone footnote and is omitted from the final apparatus to avoid a stub. Logged here for completeness.

## Apparatus reconstruction notes

- p.428 footer (raw lines 1190–1198) yielded 5 footnotes: ' = supplevimus *hoc* (= our fn 3); - = Cod. aa notionem (skipped — refers to ART. II content above; not in this chunk's body); 3 = Vat. *tantum* (skipped — same; refers to prior page); • = Tertio principaliter (= our fn 1); ^ = Isidor. (= our fn 2).
  - **Decision**: dropped the two `-` and `3` footnotes from the top footer block because their referents are body text in d.24 a.2 q.2 (preceding chunk), not in this chunk. They will be picked up there.
- p.429 footer (raw lines 1260–1278) yielded 6+ footnotes; matched by position to body markers in p.429 portion (Contra arguments + Respondeo + Replies). Renumbered 6–11.
- One marginal subscholion gloss (`Nempe, quod in divinis nomen trinitas recipitur.` raw line 1260) is an editorial gloss-pointer for marker `1` (= our fn 7); its substantive content is preserved in the fn 7 body.

## `[?]` flag count
- **In chunk file**: 1 explicit `[?]` marker on fn 7 (apparatus body) flagging the Vat.-variant Latin string for PDF cross-check.
- **In this log**: 3 `[?]`-tagged decision points (markers above).

## OCR silent corrections applied
- `pluralilatis → pluralitatis`
- `Tolius → Totius`
- `macliinam → machinam`
- `repmtur → reputatur` (in apparatus quotation of Vat. variant)
- `unltas → unitas`
- `simihter → similiter`
- `persoriis → personis`
- `siraul → simul`, `pluralita- tera → pluralitatem`, `unura → unum`, `forraa → forma`, `suppositorura → suppositorum`, `noraen → nomen`, `boc → hoc`, `cecle → cede`, `siraihter → similiter`, `dura → dum`, `lianc → hanc`, `Tliom. → Thom.`, `Iiic → hic`, `liic → hic`, `Tar. → Tar.`, `aMed. → a Med.`, `iS. → 48.` (read `iS` as garble of `48`), `S. p. I. tr. 10. q. iS. m. 1. 2.` → reading the `iS.` as `48.` per Albert's *Summa Theol.* layout.

— wp 2026-05-03
