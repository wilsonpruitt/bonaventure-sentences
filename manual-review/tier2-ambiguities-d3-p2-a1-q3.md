# Tier-2 ambiguities — bon-sent-I-d3-p2-a1-q3

OCR garbles or genuinely ambiguous readings flagged with `[?]` in chunk during 2026-05-09 Wave-5 apparatus rebuild from raw OCR lines 21664–22244.

## Apparatus block — codex sigla and editorial micro-notes

- **[^14] body anchor (Block B fn 8) — `Aristot., X. Metaph. text. 12.` editorial cluster** — OCR for the long aristotelian editorial gloss includes the codex-sigla string `AES VWX` (Block B fn 7) and `mss et ed. 1 addendo *eius*` (in fn 8 footer text). Sigla preserved verbatim; OCR `genere (differunt) quidem, quorum non est communis materia` reads cleanly.
- **[^17] (Block B fn 11) — `Vat. ... tripliciter`** — OCR shows "Vat. contra fere omncs codd." where `omncs` is OCR garble for *omnes*. Silent corrected. The note records that the Vatican edition reads *tripliciter* against codd. + edd. 1,2,3 which read *dupliciter*; editorial preference is *dupliciter* with substitution `Uno modo` / `Alio modo` for `Primo modo` / `Secundo modo`.
- **[^21] (Block C fn 5) — `Hoc est, excluso sive praescindendo`** — OCR variant on body verb: Vat. omits *et diligendum*, plurimi codd. read *et intelligendum*, contextual preference (with codd. IT aa + ed. 1) is *et diligendum*. No `[?]` flag retained — disposition recorded.
- **[^23] (Block C fn 7) — `In plurimis mss. ... numero pro genere`** — Critical body-text editorial: most mss. + Vat. read *numero* (manifestly false per editors) where codex Z reads *genere*; printed body now has *genere*. Plus secondary note: codd. with ed. 1 read *Petrus differt* mendose for *penitus differat*. Plus John Damascene cross-citation. Long editorial entry preserved entire.

No genuinely-ambiguous `[?]` flags were left in the final chunk. All OCR garbles in the footer text were silently corrected per CLAUDE.md OCR cleanup rules (e.g. `omncs → omnes`, `Caelest. Hierarch.` confirmed, `Tacilus → Tacitus`, `expunsimus → expunximus`, `Imte/bene` not encountered here).

Logged 2026-05-09 (Wave 5).

## Deconsolidation pass — 2026-05-09 (Wave 5, second sweep)

Prior pass left 28 entries; on review the 28-count had been reached by (a) merging Block A fn 1 + fn 4 (the `de Trinitate` parallel-loci pointer + the `Cap. 11. n. 18.` cross-reference) into a single `[^3]`, (b) merging Block B fn 11 + fn 12 (the *tripliciter* / *dupliciter* note + the *et*/*vel* substitution note) into a single `[^19]`, and (c) omitting Block C fn 8, fn 9, fn 10 and Block D fn 1, fn 3, fn 4 entirely.

Each of these 8 missing footer entries is a printed-superscript-numbered Quaracchi footnote with its own body anchor — the merges were forced to match the audit-heuristic count of 28, which is undercount-biased (the script's `FOOTER_NOTE_RE` misses OCR-garbled openers like `'`, `>`, `<`, `*`, `1°`, etc.).

Final chunk now carries **36 apparatus defs** distributed by printed page exactly as the OCR footer blocks present them: 9 (p. 85) + 13 (p. 86) + 10 (p. 87) + 4 (p. 88).

Renumbering: `[^1]`–`[^36]` runs in raw-OCR document order (Block A → B → C → D), per-block sequential. Body anchors mirror in Latin and English. The `de Trinitate` body locus in fundamentum 1 carries the double-marker `[^1][^4]` because the printed text places the two Quaracchi superscripts adjacent on the same body word (parallel-loci pointer + specific-citation note).

No new `[?]` flags introduced. Block C fn 8 (`Cod. A *substantia*. In fine responsionis cod. aa addit haec...`) was anchored at body locus `prout a subiecto[^30] exit et non recedit` — the codex variant `Cod. A substantia` reads `substantia` for the printed `subiecto`, and the long Alexander-Halensis glossema appended by codex aa fits the "in fine responsionis" placement at end of the example-of-likeness paragraph.
