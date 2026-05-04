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
