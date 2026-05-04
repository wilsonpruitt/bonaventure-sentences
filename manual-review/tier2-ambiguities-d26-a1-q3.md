# d.26 a1 q3 — Tier-2 ambiguities

Created 2026-05-04 alongside the split of d.26 a1-q2 → a1-q2 + a1-q3 (after discovering Quaracchi's `QDAESTIO III.` header at raw line 3831 was missed in earlier auto-chunking due to the OCR garble `QU` → `QD`).

## Apparatus marker alignment (inherited from merged source)

The pre-split d.26 a1-q2 chunk (which combined Q.II + Q.III content) had a known apparatus-vs-body marker mis-alignment in roughly the [^15]/[^16] transition: apparatus content lags body anchors by ~1 in the merged apparatus list. After the split, this mis-alignment is preserved in both halves:

- **Q3 [^1]** body anchor at *actus huiusmodi*, but apparatus [^1] content is about `tamen pro etiam cum` (which is Q.II body content, no longer in this chunk). The proper apparatus content for "actus" is at Q3 [^2] ("In multis codd. ... desideratur *actus*").
- **Q3 [^2]** body anchor at *Boethium de Trinitate*; apparatus [^2] is "desideratur actus" (matches Q3 body [^1]). The proper Boethius cap. 6 cite is at Q3 apparatus [^3].
- The shift continues through several entries before fading; by the end of the chunk, apparatus content matches body anchors again (Q3 [^23] / "iam non habet" matches the long *habet/habetur* variants entry).

**Resolution requires** eyes-on-PDF read of pp. 456–459 footers (pdf pp. 46–49) to confirm Quaracchi's exact note numbering and marker positions, then either (a) shift body markers up by one to align, or (b) shift apparatus entries down with a deletion. Currently flagged but content is preserved — readers can follow markers across by reading entries 1+1.

## Body OCR

No `[?]` flags inserted inline. All OCR garbles silently corrected per the rules in the in-repo `CLAUDE.md`. Notable corrections inherited from the merged a1-q2 chunk: `Riehardus`→`Richardus`, `simihter`→`similiter`, `omniiio`→`omnino`, `entitale`→`entitate`, `Sidicas`→`Si dicas`, `qiiod`→`quod`, `Itera`→`Item`, `liypostasi`→`hypostasi`, `chstinguit`→`distinguit`, `solura`→`solum`, `vernm`→`verum`, `prins`→`prius`, `eonstituantur`→`constituantur`, `relationera`→`relationem`, `clistinguere`→`distinguere`, `liabitudinem`→`habitudinem`, `noraine`→`nomine`, `inteliexisse`→`intellexisse`.
