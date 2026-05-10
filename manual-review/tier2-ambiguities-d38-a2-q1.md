# Tier-2 ambiguities — d.38 a.2 q.1

Logged 2026-05-07 during Tier-2 promotion of `bon-sent-I-d38-a2-q1.md`. OCR raw lines 25639–25983 of `raw/bonaventure_vol1_pt2_raw.txt`.

## Inline `[?]` flags

1. **Scholion I, opening sentence**: OCR reads "Utramquc opiiiiuii ([uae vel liberlatom croaluri / gul, ul cliviiiiim ijniosde ini salvet, vel praesoientiam / ul libt'1-lalom salvol , ul i iam respuendam esse, catholica fide / conslat." — heavily garbled crossover between columns. Reconstructed sense: "Both opinions — the one which [tollit/destroys] the freedom of the creature in order to safeguard divine foreknowledge, the other which [tollit/destroys] foreknowledge in order to safeguard freedom — are now to be rejected, as the catholic faith establishes." Verbs `[tollit?]` flagged twice; reading is contextually compelled but OCR is unrecoverable here. → Resolve via 600dpi PDF p.676 in next polish pass.

2. **Scholion I, "nec libertatem inflit"**: OCR has "nec libcrtalom inllil" — clearly a misread; expected verb `infringit` or `tollit` ("does not [infringe?] freedom, but rather posits it"). Flagged `[destroy?]`. → 600dpi PDF needed.

3. **Apparatus [^6]** (Augustine, *de Lib. arb.* original wording): OCR "Sicut enim tu memoria tua non cogis, facta esse quae / prae etc." — last word fragmentary; PL has "praescivisti" or "praeterierunt". Flagged `[?]` and `[scivisti?]`. → PDF needed.

4. **Apparatus [^10]**, "Aliter loquendum de futuro sub ratione divinae praecisionis": OCR "praecisionis" looks like a misread of `praescientiae` given context (the whole apparatus is about divine foreknowledge, not "precision"). Flagged `[?]`. → PDF needed.

5. **Apparatus [^III]** (Scholion III bibliography): final entry "Biel, hic" with OCR cut off. Standard formula in Quaracchi is `q. unica` or a numbered q. Flagged `[q. unica?]`. → PDF needed.

## Notes

- Page running heads: confirmed p.673 (line 25565), p.674 (line 25665, OCR'd as `SENTENTIARUM L-IB. I.`), p.675 (line 25793, OCR'd `673` — actually 675 — running head numeral misread), p.676 (line 25877, OCR `(i7(i` for `676`).
- Frontmatter `printed_pages` and `pdf_pages` corrected from prior `[635, 636, 637, 638]` / `[225, 226, 227, 228]` (which were borrowed from earlier d.36/d.37 chunks during auto-chunking) to `[673, 674, 675, 676]` / `[263, 264, 265, 266]` (offset = printed − 410, per pt2).
- `source` field updated to `pp. 673–676`.
- Two-column OCR required manual column re-pairing throughout the body. Argument numbering reconstructed: pro-args 1–5, contra-args 1–5; conclusion + respondeo + ad 1–5.

---

## Wave 9b Tier B disposition (2026-05-09): apparatus rebuild 10 → 14

Audit-apparatus-count flagged this chunk with diff +20 (raw=30 vs chunk=10) on the hardened heuristic 2026-05-09. Eyes-on per-page footer walk revealed mixed disposition: real undercoverage on page 676 (4 missing entries) + accepted consolidation on page 674 (Quaracchi printed convention).

### Per-page footer reconciliation

| Page | Printed footer entries | Anchors before | Anchors after | Disposition |
|---|---|---|---|---|
| 673 | 8 | 8 | 8 | 1:1; no change. |
| 674 | 8 (6 left-col + 2 right-col) | 2 | 2 | Consolidation **accepted** per Lesson 10 reinforcement: [^9] aggregates 6 left-col entries (Plurimi codd / Cfr. Boeth / Cfr. de his Aristot / In cod. Y / Cod. R / Secundum Boeth + Paulo superius + Mox post Dicendum / Quaest. seq.) under one body anchor at *vituperium*; [^10] aggregates 2 right-col entries (Sophistica + Cod. T particulam quia) under one anchor at *sophistica*. Both consolidations match Quaracchi's printed convention of em-dash-joined sub-clauses under a single body marker (cf. d.37-littera). |
| 675 | 0 | 0 | 0 | Scholion-only page; no footer band. |
| 676 | 4 | 0 | 4 | **Real undercoverage rebuilt.** New anchors [^11]–[^14] at OCR-confirmed body positions in *ad 4* (after *quod*) and *ad 5* (after *aliter sit*, after *ergo aliter*, after *oppositum ponenti*). |

Total: 8 + 2 + 0 + 4 = 14 chunk anchors covering ~20 printed footer entries (page 674 consolidation absorbs 6 sub-clauses under [^9] and 2 under [^10]).

### Page 676 anchor positions (all OCR-confirmed)

- **[^11]** at *dicendum, quod* in *ad 4* — OCR pt2 line 249 shows body marker `'` at *quod ' falsitas*; matches footer entry "Sicut veritas venit ex concordia... Mox post *Dico igitur* codd. H T interserunt *quod*" anchored to the *quod / Dico igitur* zone.
- **[^12]** at *aliter sit* in *ad 5* opening — OCR line 261 shows body marker at *sit'-, ponitur*; matches footer entry "Fide codd. A F H K T... substituimus *sit* pro *scit*" (the *sit/scit* variant is the entry's whole subject).
- **[^13]** at *aliter* (second occurrence, in *ergo aliter quam Deus praescit*) — OCR line 245 shows body marker `^` at *aliter^ quam Deus praescit*; matches footer entry "Vat. cum edd. 4, 5... addit *volunt*" which discusses the conclusion's *volunt*-insertion at this position.
- **[^14]** at *oppositum ponenti* — OCR line 262 shows body marker `"` at *oppositum ponenti "*; matches footer entry "Intelligo: hoc potest esse sive evenire... Vat. posito... post ponatur supple etc." — multi-clause closing footer for the *ad 5* discussion.

No new `[?]` flags issued in the rebuild; all four positions are OCR-confirmed.

### Body-paraphrase guard (Lesson 11)

Spot-checked chunk Latin body for page 676 (chunk file *ad 4* + *ad 5* paragraphs) against raw OCR pt2 lines 244–262. Body content is faithful — every clause in the chunk maps to OCR text; no missing prose clusters. Disposition is therefore `complete`, not `apparatus-rebuilt-body-paraphrased`.

### Audit-count expectation post-rebuild

Hardened-heuristic raw count = 30; chunk now has 14 `[^N]:` defs (residual diff +16). Gap is Lesson 10 noise from page 675 Scholion content (italicized work-citations *Sent.* d. 36 etc., lettered series in Sch. II *de dicto / de re*, and the Sch. III reference list of ~13 authors with em-dash-joined entries — all match the hardened regex). No further rebuild warranted.
