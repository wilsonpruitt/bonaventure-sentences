# d.35 scaffolds sweep audit (divisio, littera, dubia)

Date: 2026-05-08. Auditor: Claude (sweep follow-up to 2026-05-07 [?]-pass polish on d.35 a1-q1…q6).

Scope: the three non-quaestio chunks of d.35:

- `vol1/bon-sent-I-d35-divisio.md`
- `vol1/bon-sent-I-d35-littera.md`
- `vol1/bon-sent-I-d35-dubia.md`

All three were transcribed as "Phase C Tier 2 complete" on 2026-05-07. Sweep verifies bounds, semantic-marker counts raw-vs-chunk, apparatus correspondence, anchor pairing, and absence of silent paraphrase. **No substantive Latin or apparatus edits were made.** No backups created (no rebuild needed).

---

## Per-chunk verdict

### bon-sent-I-d35-divisio.md — PASS

- **Bounds**: frontmatter `line_start: 18227`, `line_end: 18308` of `bonaventure_vol1_pt2_raw.txt`.
  - Line 18227 = `COMMENTARIUS IN DISTINCTIONEM XXXV.` ✓
  - Line 18308 = end of footnote 4 (`Cod. V autem`-spillover from next chunk's a1-q1 belongs at 18309+, not in this chunk). ✓
  - Raw spans printed p. 600 (PDF p. 190); frontmatter `printed_pages: [600]`, `pdf_pages: [190]`. ✓
- **Semantic markers raw-vs-chunk**: COMMENTARIUS, DIVISIO TEXTUS, TRACTATIO QUAESTIONUM all present in raw and chunk; six `Primo…Sexto` enumerations in TRACTATIO match. No silent body dropouts.
- **Apparatus**: 4 entries (`[^1]` Cod. I, `[^2]` Vat. addit *partes*, `[^3]` Vat. ante *connotata*, `[^4]` *omnes res* / *omnia*). Raw p. 600 footer carries 4 footnotes plus a stray `Cod. V autem` that is footnote 1 of a1-q1 from PDF p. 190 footer (verified by reading line 18309+). ✓
- **Anchor pairing**: defs `[1,2,3,4]`; Latin anchors `[1,2,3,4]`; English anchors `[1,2,3,4]`. ✓
- **Inline `[?]` flags**: **0**. But `transcription_status` claims `"[?] flags on ambiguous spots"`. **MINOR ANOMALY** — status string overstates remaining work; no flags actually inline, no per-chunk ambiguities file (`tier2-ambiguities-d35-divisio.md`) exists. Recommendation: trim the "`[?]` flags on ambiguous spots" phrase from `transcription_status` (the Latin and English are clean; nothing to flag).
- **Cross-chunk reuse**: not detected (independent body content).
- **Vat-variant inversion**: spot-check on `[^2]` (Vat. addit *partes*), `[^3]` (Vat. repetit *nomina*) reads correctly in the direction the apparatus describes.
- **Fabricated apparatus**: none — all four entries trace to raw-line footer text.
- **Style note**: chunk uses `## Commentarius in Distinctionem XXXV.` and `## Commentary on Distinction XXXV.` as content H2s inside `## Latin` / `## English`. The build parser tolerates this (sentinel-only termination per `build-content.mjs`), and the smoke-test below builds cleanly. Same pattern is used elsewhere in the corpus and is not a Tier-2 violation. Mentioned only for awareness.

### bon-sent-I-d35-littera.md — PASS

- **Bounds**: `line_start: 18018`, `line_end: 18226`.
  - Line 18018 = `DISTINCTIO XXXV.` (page-top header for printed p. 597). ✓
  - Line 18226 = last apparatus row of p. 598 footer (`a Magistro omissis vel mutatis`). ✓
  - `printed_pages: [597, 598]` / `pdf_pages: [187, 188]`. Per-chunk ambiguities file documents the frontmatter scope-correction from initial `[598, 599, 600]` performed during 2026-05-07 promotion.
- **Semantic markers**: chunk presents Capp. I–IX (9 chapters). Raw OCR explicitly shows `Cap. III`, `Cap. IV`, `Cap. V`, `Cap. VI`, plus `CAP. VIII.` block; remaining caps are body-anchored by their distinctive openers (*Et est praescientia…*, *Dispositio vero…*, *Praedestinatio de hominibus…*, *Providentia autem est…*, *Sapientia vero vel scientia…*, *Hic considerari oportet…*, *Scientia vero vel sapientia…*, *Propterea omnia dicuntur…*) — all recoverable in the raw column-fragmented text. No silent dropouts.
- **Apparatus**: 15 entries. Raw p. 597 footer = 5 (Dist. VIII… ; Vat. omittunt *praevidentia* …; Ita melius codd. A B D… ; Ita codd. A B D E… ; Rom. 8, 29). Raw p. 598 footer = 10 (Vat. *Deum* … ; Cod. D addit *Deus* … ; Ita recte codd. C D… ; In Ep. ad Colos. 2, 3… ; Codd. A C E *Praeterea*… ; Libr. V c. 18 n. 36… ; Ioan. 1, 3, 4… ; Rom. 4, 17… ; Id est V. *de Fide ad Gratian.*… ; Psalm. 19, 11; August. in hunc Psalm. n. 18). Sum = 15. ✓ Renumbering 1–15 correct.
- **Anchor pairing**: `[1..15]` in defs, Latin, and English. Includes documented dual `[^3]` anchor (Cap. I body and Cap. II heading) — apparatus note explicitly addresses both positions, so dual anchor is correct.
- **Inline `[?]` flags**: **0** in body. The single `[?]`-token hit comes from the `transcription_status` line's literal mention of an ambiguity. Per-chunk ambiguities file (`tier2-ambiguities-d35-littera.md`) is present and resolves the Psalm 19/49 question to "kept Quaracchi reference verbatim, decade-polish concordance check still owed".
- **Cross-chunk reuse**: not detected.
- **Vat-variant inversion**: spot-check on `[^9]` (*terrenae* restored against *aeternae*) and `[^6]` (Vat. *Deum* against codd. + ed. I *Deo*) — both correctly oriented in body.
- **Fabricated apparatus**: none — every entry traces to raw OCR footer text.

### bon-sent-I-d35-dubia.md — PASS

- **Bounds**: `line_start: 19688`, `line_end: 19945`.
  - Line 19688 = `DUBIA CIRCA LITTERAM MAGISTRI`. ✓
  - Line 19945 ends in mid-apparatus on p. 616 footer; appropriate boundary for end of d.35 dubia (next content is d.36 ART. UNICUS). ✓
  - `printed_pages: [613, 614, 615, 616]` / `pdf_pages: [203, 204, 205, 206]`. Frontmatter scope-correction from earlier `[614…]` is documented in the per-chunk ambiguities file. (Pt2 PDF offset = printed − 410.)
- **Semantic markers**: chunk presents DUB. I–VI (6 dubia). Raw OCR shows DUB. I (line 19692), DUB. II (line 19734), DUB. III (line 19721 cross-column), DUB. V (`DuB. V.` line 19831), DUB. VI (`DuB. VI.` line 19916). DUB. IV's header was OCR-cropped but body opener (*Item quaeritur de hoc quod dicit, quod creator ita dicitur relative…*) is present at raw line ~19808 and matches the chunk verbatim. All 6 dubia accounted for.
- **Apparatus**: 21 entries (chunk's frontmatter says 18 — **MINOR ANOMALY** in metadata: actual `[^N]:` defs go 1–21). Spot distribution across the four printed pages (613, 614, 615, 616) is consistent with raw multi-column footers. Recommendation: update `transcription_status` from `(18 entries)` to `(21 entries)`.
- **Anchor pairing**: `[1..21]` in defs, Latin, and English. ✓
- **Inline `[?]` flags**: **0** in body. Per-chunk ambiguities file (`tier2-ambiguities-d35-dubia.md`) lists 5 documented items, all marked ACCEPT or ACCEPT-pending-PDF, with no body-level `[?]` left over.
- **Cross-chunk reuse**: not detected.
- **Vat-variant inversion**: spot-check on `[^19]` (Vat. *praesentium* inserted) and `[^20]` (Vat. textual expansion) — both correctly oriented (apparatus describes Vat. additions; chunk body retains the codex/non-Vat reading).
- **Fabricated apparatus**: none — every entry, including the long `[^11]` Boethius gloss and `[^20]` Scotus / Aquinas note, traces to raw OCR footer text on pp. 614–616.

---

## Totals

| Chunk    | Status | Markers raw=chunk | Apparatus entries | Anchors paired | Inline `[?]` | Notes |
|----------|--------|-------------------|-------------------|----------------|--------------|-------|
| divisio  | PASS   | yes (3 markers)   | 4 / 4             | yes            | 0            | minor: status string overstates `[?]` work; no per-chunk log |
| littera  | PASS   | yes (Cap. I–IX)   | 15 / 15           | yes            | 0            | clean; per-chunk log present |
| dubia    | PASS   | yes (DUB I–VI)    | 21 / 21           | yes            | 0            | minor: status string says "(18 entries)" — actual is 21 |

**Verdict**: all three scaffolds verify clean against raw OCR pt2. **No silent body dropouts, no missing apparatus entries, no cross-chunk reuse, no Vat-variant inversion, no fabricated apparatus detected.** Two metadata-only inaccuracies surfaced; both are inline edit candidates and do not affect the build or the user-facing site.

## Recommended (metadata-only, non-blocking) edits

1. `bon-sent-I-d35-divisio.md` — strip `"[?] flags on ambiguous spots"` from `transcription_status` (chunk has 0 inline flags; no per-chunk ambiguities file warranted).
2. `bon-sent-I-d35-dubia.md` — change `(18 entries)` to `(21 entries)` in `transcription_status`.

Neither edit is being performed in this audit (per "commit nothing"); they are noted here for the next maintainer pass.

## Build smoke-test

`cd site && node scripts/build-content.mjs` →
`Built content.json: 1 book(s), 422 questions, 350 translated`

Build clean, no parser errors.
