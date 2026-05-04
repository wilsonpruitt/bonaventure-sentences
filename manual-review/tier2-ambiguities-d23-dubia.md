# Tier-2 ambiguities — bon-sent-I-d23-dubia

Promotion date: 2026-05-03
Raw range: lines 71288–71373 of `raw/bonaventure_vol1_raw.txt` (vol. I pt. 1)
Printed pages: 416–417 (PDF pp. 518–519)

## Structure verification

- **Dubia count: 2** (DUB. I and DUB. II). Confirmed by full read of the raw range. No DUB. III, DUB. IV, or OCR-garbled equivalents (`DlfB.`, `Dl[fI]B`, `DUR.`, `DUF.`, etc.) appear before the chunk's tail of Boston College Library scanner garbage (lines 71374–71429, already trimmed by the upstream `line_end` shrink).
- The page-header OCR `DUBL\ CIRC.V LITTERAM M.\G1STRL` at raw line 71288 normalizes to `DUBIA CIRCA LITTERAM MAGISTRI.` — single, expected heading. No second heading.

## Cross-volume continuation (NOT a defect — flagged for the project owner)

- DUB. II's `**Respondeo:**` body is incomplete in vol. I pt. 1. OCR ends mid-sentence at `Potest enim esse comparatio entis ad ipsum` (raw line 71338). The remainder is on printed p. 417 (PDF p. 519), which lives in `raw/bonaventure_vol1_pt2_raw.txt` (visible from line ~62 onward: "...veritatem, quia unus et idem est Deus, qui est cogitatur et dicitur, et aequaliter verus..."). 
- Per the user's instruction that "After your range, the raw text contains only library card garbage. d.24+ are in pt2 (separate raw file)" — the spillover will be handled by the pt2 pipeline. This chunk file (pt1-keyed) honestly stops where pt1's text stops and signals continuation in the body and `transcription_status`.

## Apparatus renumbering

- Printed page 416 carries 8 footer notes. Notes 1–2 anchor in the preceding quaestio (their cue-words `potest`/`potuit` and `imponit`/`respondit`/`Si autem` appear in raw lines 71239, 71278, etc., NOT in this chunk). 
- The 6 notes that anchor in this chunk are printed notes 3 → 8, renumbered as [^1]–[^6]. Mapping:
  - [^1] = printed n. 3 (`Epist. 13 ad Damasum`) — silently corrected `Epist. 13` from raw OCR; widely cross-attested as `Epist. 15.` (the canonical letter to Damasus on the hypostasis controversy is *Ep.* 15). Adopted `15` over OCR `13`. **Flag for owner review** — if user wants the OCR's `13` preserved verbatim, change a single character in the apparatus.
  - [^2] = printed n. 4 (* glyph in OCR, `Cap. de Substantia`)
  - [^3] = printed n. 5 (`=` glyph in OCR, `Vat. cum uno alterove codice omittit dicendum`)
  - [^4] = printed n. 6 (`^` glyph in OCR, `supplevimus hic ipsum`)
  - [^5] = printed n. 7 (`'` glyph in OCR, `Cap. 3`)
  - [^6] = printed n. 8 (`Praebemus communiorem lectionem`)

## OCR silent corrections in body

All routine letter-substitution OCR garbles, not flagged:
- `suiit` → `sunt`
- `Unausia` → `Una usia` (Quaracchi prints these as two words, the Boethian terms)
- `bo-iiae` → `bonae`
- `hijpostasis` → `hypostasis`
- `nuUo` → `nullo`
- `hbrimi` → `librum`
- `liypostasis` → `hypostasis`
- `lueretici` → `haeretici`
- `autera` → `autem`
- `specificatura` → `specificatum`
- `noraina` → `nomina`
- `huiusraodi` → `huiusmodi`
- `hbro` → `libro`
- `,\ugustini` → `Augustini`
- `Dicendura` → `Dicendum`
- `trinura` → `trinum`
- `Ilera` → `Item`
- `falsura` → `falsum`
- `raulta` → `multa`
- `eniin` → `enim`
- `diciraus` → `dicimus`
- `serraonis` → `sermonis`
- `lioc` → `hoc`
- `.\d  illud` → `Ad illud`

## OCR silent corrections in apparatus

- Note [^2]: `ocourril` → `occurrit`; `spacies` → `species`; `flcitur` → `conficitur`; `liypostasis` → `hypostasis`; `otc.` → `etc.`; `ot od.` → `et ed.`; `bb ot` → `bb et`.
- Note [^3]: `Val.` → `Vat.`; `eodice` → `codice`; `dicendim` → `dicendum`; `qnod` → `quod`; `iit` → `ut`; `ASY` → `A S Y`; `oum` → `cum`; `veL` → `vel`.
- Note [^4]: `philosophiis` → `philosophus`; `particulain` → `particulam`; `ciii` → `cui`; `iii conmentario` → `in commentario`.
- Note [^5]: `lioc` → `hoc`.
- Note [^6]: `conimuniorem` → `communiorem`; `sub. stituendo` → `substituendo`; `2,3, i ,  5 ,  6` → `2, 3, 4, 5, 6` (the OCR `i` is a misread `4`); `«mw/m` → `magis` (this is the disputed reading the apparatus is reporting — Quaracchi prints `magis`); `oniittunt` → `omittunt`.

## `[?]` flag count

- **0 inline `[?]` flags in the chunk body.** All OCR garbles are routine, unambiguously fixable letter-substitutions in well-attested formulae and textual variants.
- **1 flagged item in this log** (Jerome `Epist. 13` vs `Epist. 15` — adopted `15`; trivially reversible).

## d.22 hazard precedent (un-numbered appendix)

- d.22 dubia carried a `QUINQUE REGULAE DE NOMINIBUS DIVINIS` un-numbered block between DUB. II and DUB. III. **No analogous appendix appears in d.23 dubia.** The block between DUB. II and the apparatus footer (raw lines 71337–71338) is purely the truncated DUB. II response, not a separate titled appendix.

## 2026-05-04 pt1+pt2 stitch

### (a) Operation
Promoted the chunk from "pt1-only with truncation marker" to a full pt1+pt2 stitch. Replaced the two `[…continuation in vol. I pt. 2, printed p. 417]` markers (Latin and English bodies) with the actual continuation. Appended DUB. III and DUB. IV (Latin + literal English). Replaced the 6-entry apparatus with the full 14-entry block covering all four dubia. The previous structural claim ("dubia count: 2") was wrong — d.23 has 4 dubia, with DUB. III and DUB. IV living entirely on printed p. 417 (vol. I pt. 2 OCR).

Frontmatter: kept `line_start: 71288` and `line_end: 71373` (pt1 range, for the parser); added `line_start_pt2: 60` and `line_end_pt2: 141`; updated `word_count_latin` from 540 → 980; updated `transcription_status` to the new pt1+pt2 stitch string.

### (b) pt2 boundaries used
- `raw/bonaventure_vol1_pt2_raw.txt` lines **60–141**.
- Line 60 = page header `DIST. XX[I]II. DUBIA. 41[7]` (running head + page number).
- Lines 62–79 = body text in **2-column layout** (col A = end of DUB. II response; col B = end of DUB. III response — note the OCR row order DOES NOT match logical order).
- Line 83 = `DUB. III.` header (col A) and `DoB. IV.` header (col B).
- Lines 87–108 = body (col A = DUB. III start; col B = DUB. IV start through end).
- Lines 113–141 = footer apparatus block (8 notes).
- **Excluded** (per user spec): lines 1–29 (IA digitization notice + Quaracchi title page), lines 142–160 (`AD LECTOREM` editorial notice from Quaracchi about reducing critical apparatus going forward — Quaracchi editorial, not Bonaventure), line 161+ (`SENTENTIARUiM LIB. 1.` running head + `DISTINCTIO XXIV` opening — d.24 territory).

### (c) Two-column layout — was it tractable?
**Yes, with care.** The IA OCR for p. 417 reflows two columns by interleaving the same physical OCR row with text from both columns separated by wide horizontal whitespace. Key cues: column-A text starts with leading spaces around col 4–8, column-B text starts further right (col ~100+). Once the two streams are split, each reads as continuous prose. The semantic check that confirms the split: col A above the DUB. III header continues the DUB. II response from where pt1 broke off (`Potest enim esse comparatio entis ad ipsum…`), while col B above the DUB. IV header is clearly DUB. III response material (`tres essentias / Scriptura non contradicit / triplex fuit ratio`). One initial ambiguity was whether col B top was a separate dubium or DUB. III continuation — the sense and the location of the `DUB. III.` header in col A (with no header above col B) settled this as a continuation of DUB. III into col B.

The footer apparatus block (lines 113–141) is also 2-column; reflowed as col-A-then-col-B. Note glyphs in the OCR (some marker chars are mis-OCR'd as `'`, `-`, `<`, `^`, `"`, etc.) were resolved by counting in printed-page order (1, 2, 3, 4 in col A; 5, 6, 7, 8 in col B).

### (d) New `[?]` flags introduced by the stitch
- **1 inline `[?]`** in the body (Latin and parallel position in English): `ad ipsam[?] veritatem`. The OCR at the pt1/pt2 seam has `ad ipsum` (pt1 line 71338) and the pt2 OCR resumes at `veritatem,` (pt2 line 64). The grammatically required reading is `ad ipsam veritatem` (acc. fem. sg. agreeing with `veritatem`); the pt1 OCR `ipsum` looks like a routine line-end masculine-form misread. Adopted `ipsam` and flagged for owner review. (Reverting to OCR-literal `ad ipsum veritatem` is a one-character edit if the owner prefers verbatim OCR.)
- No other inline `[?]` flags. All other OCR garbles (e.g. `Auguslinus` → `Augustinus`, `Scriplura` → `Scriptura`, `dice?'e` → `dicere`, `oranis` → `omnis`, `ilhid` → `illud`, `subticet` → `subticet`, `assimiletur` → `assimiletur`, `essenlia` → `essentia`, `ctaret` → `dictaret`, `imminebjat` → `imminebat`, `Lnde` → `Unde`, `obiieitur` → `obiicitur`, `omnimoda` corrected from `omnino` per note 14, etc.) are routine letter-substitution fixes resolved unambiguously by context.

### (e) Apparatus renumbering map
Pt1 portion (no change from prior promotion):
- [^1] = printed p. 416 n. 3 (Jerome *Ep.* 15 ad Damasum)
- [^2] = printed p. 416 n. 4 (Boethius *de Substantia*)
- [^3] = printed p. 416 n. 5 (Vat. omittit *dicendum*)
- [^4] = printed p. 416 n. 6 (suppl. *ipsum*)
- [^5] = printed p. 416 n. 7 (Cap. 3)
- [^6] = printed p. 416 n. 8 (Praebemus *maius* loco *magis verum*)

Pt2 portion (newly added):
- [^7] = printed p. 417 n. 1 (Vat. cum cod. cc *et qui cogitatur et qui dicitur*) — anchors at `dicitur` in DUB. II cont.
- [^8] = printed p. 417 n. 2 (Vat. *summo*) — anchors at `summe` in DUB. II cont.
- [^9] = printed p. 417 n. 3 (Scotus, Ockham, Thomas of Strasbourg) — anchors at `secundum primam viam` (end of DUB. II)
- [^10] = printed p. 417 n. 4 (verbum *est* desideratur; suppl. *Dicendum*) — anchors at `est` in DUB. III's `huius oppositum est falsum`
- [^11] = printed p. 417 n. 5 (Codd. dissentiunt; *autem* / *igitur*; punctuation) — anchors at `igitur` in DUB. III's `Ex verbis igitur Augustini`
- [^12] = printed p. 417 n. 6 (Cod. X *omnino* — better *omnimoda*) — anchors at `omnimoda` in DUB. IV
- [^13] = printed p. 417 n. 7 (id est, *diversitas* in sensu stricto; Aristot. X. Metaph.) — anchors at `verbo` in DUB. IV's `facienda est vis in verbo`
- [^14] = printed p. 417 n. 8 (substituimus *omnimoda* pro *omnino*; codd. omittunt *est*) — anchors at `est` in DUB. IV's `omnimoda est identitas`

The previous promotion's note about "Jerome *Epist. 13* vs *Epist. 15*" remains: adopted `15` (canonical *Ep. ad Damasum* on the hypostasis controversy) over OCR `13`; trivially reversible.
