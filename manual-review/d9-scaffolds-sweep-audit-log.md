# d.9 Scaffolds Sweep Audit Log — 2026-05-08

Audit of `bon-sent-I-d9-{divisio,littera,dubia}.md` per the d.1/d.2/d.3 sweep methodology. `bon-sent-I-d9-dubia-v2.md` is a vestigial auto-chunked skeleton (line range 37807–38245, no `## Latin` block, no English, no apparatus); per scope it was inspected only enough to confirm vestigial status — left untouched.

## Per-chunk verdict

### bon-sent-I-d9-divisio  (lines 36017–36138)
**Verdict: PASS (no rebuild needed).**

- `## Latin` body diffs cleanly against OCR lines 36017–36058 (Commentarius + Divisio textus) plus 36115–36132 (Tractatio quaestionum). Punctuation, italics, and citations match Quaracchi.
- 5-footnote apparatus verified against the two on-page apparatus blocks:
  - [^1] "Ed. 1 *particulas*" = OCR p.180 NOTAE AD COMMENTARIUM fn 1 (line 36098). Match.
  - [^2] *imperscrutabile* substitution + Vat. *Similiter* gloss = OCR fn 2 (lines 36100–36103). Match.
  - [^3] "Unus alterve cod. ut I cum ed. 1 hic *verbum*" = OCR fn 3 (lines 36105–36106). Match.
  - [^4] "Fide plurimorum mss. et ed. 4 hic adiecimus *sit*" = OCR fn 4 (lines 36108–36109). Match.
  - [^5] "Codd. et plurimae edd. omittunt *sit*" — anchor at "utrum generatio in divinis sit[^5] personarum distinctiva"; the OCR Tractatio body line 36127 shows a footnote marker on `sit`. Apparatus body text plausible (short standard variant note); could not eyes-on confirm but no fabrication risk identified.
- English translation tracks Latin paragraph-for-paragraph. Literal, not paraphrased.
- No `[?]` flags raised.

### bon-sent-I-d9-littera  (lines 35561–36016)
**Verdict: NEEDS APPARATUS PATCH (body intact).**

- `## Latin` body Cap. I–V diffs cleanly against OCR lines 35561–36015. Punctuation/italics match.
- `## English` body literal and parallel.
- 35-footnote apparatus: [^1]–[^33] verified against OCR p.177 NOTAE (fn 1–7), p.178 footnotes (fn 1–13), with anchor placements largely correct. **[^31] [^32] [^33] anchor placement slightly imprecise but apparatus content correct** — left as-is per "minor anchor drift not fabrication" rule.
- **[^34] and [^35] FABRICATED + DUPLICATED**: both entries currently read "In hoc textu Vat. et edd. omnes contra codd. nostros et originale *professionis* loco *professio*." This text does not appear anywhere in OCR p.178 or p.179 apparatus. Page 179 actually has four real footnotes (NOTAE block at lines 36081–36093):
  - fn 1: "Codd. et plurimae edd. contra originale et Vat. omittunt *nec ratio*; et deinde ante *in generatione* Vat. cum paucis edd. omittit *et*."
  - fn 2: "In codd. et Hilario deest *ea*. — Paulo post, ante *ex eo natum* Vat. cum paucis edd. *est*."
  - fn 3: "Apud Hilar. (ed. Maurin.) *natus est*, ubi in calce dicitur, plures codd. lectionem *natum* exhibere, quam mss. nostri et edd. habent. — Mox codd. C D E post *iam non* addunt *tantum*."
  - fn 4: "Totum hoc cap. excerptum est ex Hilario loc. cit. n. 22-26, sed plurimis [text truncated in OCR — likely 'mutatis']."
- The chunk's existing `## Notes` already flagged [^34]/[^35] as suspect duplicates; this audit confirms both are spurious and that page 179 footnotes were never transcribed.
- **Disposition**: extend apparatus to [^34]–[^37] using OCR p.179 NOTAE, and re-anchor in body. fn 4's truncation noted as `[?]` in `manual-review/tier2-ambiguities-d9-littera.md`.

### bon-sent-I-d9-dubia  (lines 37250–37970)
**Verdict: NEEDS APPARATUS PATCH (body intact, [^61] fabricated).**

- `## Latin` body Dub. I–XIII diffs cleanly against OCR lines 37250–37968. All 13 dubia present. Punctuation/italics/citations match.
- `## English` body literal and parallel; well-translated.
- 61-footnote apparatus: spot-checked [^1] [^2] [^3] [^11] [^16] [^25] [^33] [^46] [^50] [^58] all match OCR. Most apparatus content is genuine and accurate.
- **[^60] CHECK**: "Vat. contra plurimos codd. minus bene *hic* pro *ipse*." — anchor at p.192 body word `ipse`. OCR truncates p.192 footnote bodies (line 37952 has only "492" running-head garble; footnote bodies cut). Plausible reconstruction — accepted with `[?]` flag.
- **[^61] FABRICATED**: chunk text "Oportet mutationem fieri in illa natura — scilicet humana, quam assumpsit — sed non in persona divina." This is an interpretive editorial gloss, not a Quaracchi textual variant. The phrase "scilicet humana, quam assumpsit" is paraphrase. The body anchor is on Dub. XIII Respondeo word `aliam` — OCR p.192 line 37965 has a marker there but the apparatus text was truncated.
- **Disposition**: replace [^61] with `[?]`-flagged stub; surface in `manual-review/tier2-ambiguities-d9-dubia.md` for resolution at next polish-blocker decade pass (d.50, when d.41–d.50 polish runs and d.9 also gets re-examined per existing PDF eyes-on cadence). Do NOT delete — keep marker so build still parses; replace prose only.

### bon-sent-I-d9-dubia-v2
**Verdict: VESTIGIAL — left untouched per scope.**

- Frontmatter: legacy auto-chunk format (`title:` not `title_la`/`title_en`; `line_start: 37807 line_end: 38245`; `word_count_latin: 3242`; no `transcription_status`).
- Content: raw OCR slice for Dub. VIII–XIII only, with no `## Latin` heading, no English, no apparatus block — just bare OCR text after the breadcrumb.
- Confirmed: this file is a pre-Tier-2 fragment that was superseded by `bon-sent-I-d9-dubia.md` (which covers Dub. I–XIII fully). It should be moved to `vol1/legacy/` at next housekeeping pass.

## Totals

| Chunk | Latin body | English | Apparatus entries | Fabricated entries | `[?]` raised |
|---|---|---|---|---|---|
| divisio | clean | clean | 5 | 0 | 0 |
| littera | clean | clean | 35 (was 35; fixing [^34]/[^35] dupe → 4 entries [^34]–[^37]) | 2 (both same dupe) | 1 (fn 4 OCR-truncated) |
| dubia | clean | clean | 61 | 1 ([^61]) | 1 ([^61]) |
| dubia-v2 | n/a (vestigial) | n/a | n/a | n/a | n/a |

## Anomalies

1. **OCR p.192 footnote-body truncation**: the OCR jumps from page-192 body text (Dub. XIII Respondeo) directly to "DISTINCTIO X." without rendering the three footnote bodies anchored on p.192 (`ipse`, `aliam`, `alia`). Suspect: the OCR's running-head "492" at line 37952 is itself a garble of "192", and the footnote-block scan-region was misclassified by ABBYY as a different page. This is the only OCR-truncation anomaly in d.9. Resolution-via-PDF deferred to the next d.10 polish-blocker (d.41–d.50) since d.9 isn't due for another full polish-blocker pass for several decades; the `[?]` flag is sufficient until then.

2. **Littera apparatus [^34]/[^35] fabrication pattern**: matches the d.1-dubia and d.2-dubia pattern (apparatus invented when transcriber crossed a page boundary they hadn't read). Recommendation: when re-running future scaffold-sweep audits, **always check the last 2–3 apparatus entries in any chunk that crosses a Quaracchi page boundary** — that's where this failure mode reliably emerges.

3. **Dubia apparatus [^61] fabrication**: same pattern — last entry, on page-bottom OCR truncation. Confirms the recommendation above.

## Build smoke-test
`cd site && node scripts/build-content.mjs` — TODO at end of fix.
