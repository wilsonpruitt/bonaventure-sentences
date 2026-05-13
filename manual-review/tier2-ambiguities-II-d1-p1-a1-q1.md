# Vol II d.1 p.I a.1 q.1 — Tier-2 ambiguities log

Chunk: `vol2/bon-sent-II-d1-p1-a1-q1.md`
Raw OCR range: lines 1669–2018 of `raw/bonaventure_vol2_raw.txt`
Printed pp.13–19 (PDF pp.35–41, vol2 offset +22)
Promoted to Tier 2: 2026-05-13.

## [?] flags

- **Latin body, p.15 page break**: position approximate; OCR ate the p.15 right-page running head. Placed marker after fundam.3 of *ad oppositum*. Resolve at d.10 polish pass by extracting `vol2/p-hires-r600-pp.14-15` and locating the column break.
- **Latin body, p.17 page break**: same situation; placed after solutio 2 (just before solutio "3. 4."). Resolve at d.10 polish.

## Apparatus

- **[^12]** *Aristot. VII Metaph. text. 28*: OCR `'' Tcxt. 281 (VI. c. 8.)` is ambiguous — could be *text. 28*, *text. 281*, or two run-together values. Chose 28 based on the cited passage ("homo hominem generat" sits at *Metaph.* VII.8 = 1033b30ff., which corresponds to Quaracchi's standard "text. 28" numbering of the Bekker recension). Confirm against PDF p.16 column-1 footer.
- **[^13]** *Plato Gorgias pag. .i6o*: OCR Stephanus-page number is garbled to `.i6o`. Standard *Gorgias* 465a (the locus of "ars… careat ratione") falls in Serranus tom. I around p. 465; chose 465 over 460 because 465a is the canonical citation. Confirm against PDF p.17 footer.
- **Scholion IV bibliography**: three entries (S. Thom. *de Potent.* q. 3. a. 1. 2 — possibly should be "a. 1, 2, 3"; Durand. *hic q. 2*; Dionys. Carth. *hic q. 2*) are flagged because the OCR right-column rows are degraded with positional jumble. Most likely all are *q. 2* but article/question numbers may need correction. Resolve via PDF p.19 right-col SCHOLION footer at 600dpi.

## Out-of-scope findings (no action required, parked for awareness)

- The chunk's auto-generated `line_end: 2018` correctly clips just before raw line 2019's *QUAESTIO II.* heading. No boundary bug.
- Solutio numbering: Quaracchi merges replies to fundamenta 3 and 4 under a single "3. 4." heading because both objections are answered by the *agens secundum naturam / agens per intellectum* distinction. Preserved as-is.
- Apparatus marker numbering in this chunk is sequential 1–34 across the chunk; Quaracchi's per-printed-page restart is collapsed for chunk-internal coherence. Crosswalk documented in the chunk's Notes section.
