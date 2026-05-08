# d.40 scaffolds sweep audit log

Date: 2026-05-08
Scope: structural / scaffold chunks only — `divisio`, `littera`, `dubia` for d.40 (final distinction of Vol I, in pt2).
Out-of-scope (already polish-cleared per `manual-review/d31-d40-polish-resolution-log.md`): the eight a{1..4}-q{1,2} quaestio chunks.

## Files audited
- `vol1/bon-sent-I-d40-divisio.md` (125 lines, 1 chunk pages 701–702 / pdf 291–292, raw lines 28213–28266)
- `vol1/bon-sent-I-d40-littera.md` (166 lines, pages 699–701 / pdf 289–291, raw lines 28028–28209)
- `vol1/bon-sent-I-d40-dubia.md` (271 lines, pages 722–724 / pdf 312–314, raw lines 30130–30397)

## Per-chunk verdict

### divisio — VERIFIED CLEAN. No edits.
- Bounds correct against raw OCR. Body opens at line 28213 with `COMMENTARIUS IN DI[S]TINCTIONEM XL.` heading and closes at 28266 with `Secundo, quid sit praedestinatio secundum *rem*.`
- The previously-flagged `secundum [?]` (resolved 2026-05-07 from PDF p. 702 → `rem`) is in place. `transcription_status` already updated 2026-05-08.
- Structure: `## Latin` / `## English` / `## Apparatus` / `## Notes` all present; 4 page comments (2 per language); `has_apparatus: false` honestly declared (apparatus block notes that the p. 702 footer apparatus belongs to the sibling a1-q1 chunk).
- Latin body diff against raw: paragraph-for-paragraph match; *Tractatio Quaestionum* listing matches the printed enumeration.
- English: literal, parallel; no paraphrase smuggling; `secundum rem` rendered "according to the thing (*rem*)" (preserves Latin term — appropriate per CLAUDE.md key-terminology convention).
- 0 anchors / 0 apparatus defs (none expected). 0 inline `[?]` flags.

### littera — VERIFIED CLEAN. No edits.
- Bounds correct. Lombard d.40 littera proper begins after the centered `DISTINCTIO XL.` heading on the bottom of p. 699 (raw 28028) and runs through p. 700 + the first three lines of p. 701 (raw 28209), ending with `altitudo divitiarum sapientiae et scientiae Dei` (raw line 181 of the slice — verified). Frontmatter footnote in `source` already documents the prior scaffolding error (printed_pages `[696,697,698]` → `[699,700,701]`; line_start `27967` → `28028`) corrected on 2026-05-07.
- Cap. I and Cap. II structural headers preserved verbatim from raw, italic subtitles intact.
- 16 apparatus entries, 16 unique anchors, every `[^N]` appears exactly 3× (Latin body + English body + apparatus def). No orphaned defs, no orphaned anchors.
- Apparatus spot-checks against raw OCR pp. 699–701 footer (raw lines 28063–28209): `[^1]` (`In codd. CDE et ed. 1...`), `[^2]` (`Cap. 10. n. 19; sed ultima verba ex Glossa ad Rom. 8, 29.`), `[^5]` (`In codd. et ed. 1 (5 in margine) *in aliis faceret*...`), `[^8]` (`Vat. et aliae edd. contra codd. et ed. 1 addunt *istorum*.`), `[^9]` (`Libr. I. ad Monimum, c. 25...`), `[^16]` (`Libr. I. *quaest.* 2. n. 19...`) — all match raw OCR verbatim. No silent invention; no Vat-variant inversion.
- Page comments: 6 (3 per language: 699, 700, 701).
- 0 inline `[?]` flags (the four trailing-`[?]` hedges on `[^5]/[^9]/[^15]/[^16]` were removed in the d.39+d.40 polish pass per the resolution log; spot-checks confirm clean).

### dubia — VERIFIED CLEAN. No edits.
- Bounds correct: 30130–30397 captures DUB I–VIII. d.41 `DIVISIO TEXTUS` runs starts at raw line 30612, well after this chunk's close.
- All 8 dubia present and sequential: I, II, III, IV, V, VI, VII, VIII. The user-noted DUB V + DUB VI extension (added 2026-05-07) is in place. `#### DUB.` headers count = 8 in Latin, 8 in English (16 total) — matches.
- `printed_pages` `[722, 723, 724]` consistent with the per-chunk ambiguity file's frontmatter-correction note (auto-chunker had set `[723,724,725]`).
- 27 apparatus entries, 27 unique anchors, every `[^N]` appears exactly 3×. No orphans either direction.
- Apparatus spot-checks against raw OCR p. 722–724 footers (raw lines 30179–30400 segment): `[^1]` (`Ed. 1 *debent*. — Plura de hoc dubio...`), `[^4]` (`Cfr. Alex. Hal., S. p. I. q. 28. m. 2. a. 4; B. Albert., hic a. 7;...Aegid. R., hic 1. princ. q. 2.`), `[^9]` (`Sive ut nunc dici solet: *per distinctionem in sensu composito et in sensu diviso.*`), `[^13]` (`Matth. 26, 34. — Mox post *fuit* codd. A X intericiunt *certum.*`), `[^17]` (full Aristotelian *Physics* gloss), `[^23]` (`Aristot., *de Praedicam.* c. *de Relatione*.`), `[^26]` (`Luc. 10, 20: *Gaudete autem...*`) — all match raw OCR.
- Body content: paragraph-for-paragraph match against raw; multi-column OCR interleaving (DUB I/III, DUB II/IV alternating column tops) was correctly disentangled by the prior translator — verified by content-tracing the raw-line traces of `aliquo damnando`, `Christus dixit Petrum peccaturum`, `relativa simul sint natura`, `gratiae appositio`, `nomen eius scriptum`.
- `has_apparatus: true` correctly set (was missing `has_scholion` field — minor, dubia chunks don't carry one; left as-is to match d.31–d.39 dubia convention).
- 0 inline `[?]` flags.

## Cross-cutting checks
- **Build smoke-test**: `cd site && node scripts/build-content.mjs` → `Built content.json: 1 book(s), 422 questions, 350 translated`. Clean.
- **Frontmatter fields**: all three chunks have `id`, `volume`, `book`, `distinctio`, `type`, `title_la`, `title_en`, `printed_pages`, `pdf_pages`, `source`, `transcription_status`, `format_version`. dubia is missing `has_scholion` — consistent with peer d.{31..39} dubia chunks; not a Tier-2 violation.
- **`transcription_status` strings**: divisio updated to 2026-05-08 already (residual `[?]` resolution); littera + dubia carry 2026-05-07 stamps with explicit raw-line citations and apparatus counts.
- **Scaffold-specific risks the user flagged**:
  - silent body dropouts → none detected; semantic-marker counts (DUB headers, Cap. headers, paragraph boundaries) match raw.
  - missing apparatus → none; littera 16/16, dubia 27/27, divisio 0/0 (intentional).
  - cross-chunk reuse → none; the divisio's footnote of "apparatus on p. 702 belongs to a1-q1" is the only cross-chunk reference, and it's a *disclaimer*, not a copy of foreign apparatus into the divisio chunk.
  - Vat-variant inversion → spot-checked five Vat-variant entries (littera `[^8]`, dubia `[^11]`, `[^14]`, `[^25]`, `[^26]`); each preserves the printed direction (Vat-reading vs. cod./other-edd. reading) correctly.

## Totals
- Chunks audited: 3
- Verdict: 3/3 verified clean — no substantive edits required.
- No backups created (no rebuilds performed).
- No inline `[?]` flags introduced.
- No new entries appended to `manual-review/tier2-ambiguities-d40-*.md` (no fresh ambiguities surfaced).

## Anomalies / observations
- None blocking. The d.40 scaffold trio is the cleanest decade-closing scaffold set in the corpus to date — almost certainly an artifact of the d.31–d.40 polish-blocker pass having forced these chunks through PDF eyes-on review on 2026-05-07.
- Minor cosmetic: dubia chunk's prose blockquote about footnote convention contains literal `\`**La.**\`` and `\`**En.**\`` strings inside backtick-code spans, so a naive `**La.**` count returns 28 instead of 27. This is intentional and harmless; the build parser only looks for `**La.**` at the start of an apparatus entry.

## Disposition
No commit. Audit closed.
