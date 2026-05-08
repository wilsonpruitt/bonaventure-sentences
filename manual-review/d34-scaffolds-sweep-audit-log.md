# d.34 scaffolds sweep audit log — 2026-05-08

Scope: `vol1/bon-sent-I-d34-{littera, divisio, a1-q1, a1-q2, a1-q3, a1-q4, dubia}.md` (7 chunks). Goal: verify chunk bounds, diff Latin against pt2 raw OCR, diff/build apparatus, fix paraphrase, never invent Latin or fabricate apparatus.

Source: `raw/bonaventure_vol1_pt2_raw.txt`. Pt2 PDF offset = printed − 410 (so printed pp. 582–597 = pdf pp. 172–187).

Context: d.34 was promoted to Tier-2 on 2026-05-07 (all seven chunks built fresh from OCR with bilingual `**La.**`/`**En.**` apparatus and literal English). Pre-rebuild skeletons preserved at `vol1/_backup-d34-pre-rebuild-20260507/`. The d.31–d.40 polish-blocker `[?]`-resolution pass (Pass A) ran 2026-05-07 and cleared multiple d.34 flags spanning all seven chunks (full disposition logged in `d31-d40-polish-resolution-log.md`, lines 162–188). This sweep audits the post-polish state for silent paraphrase, fabricated apparatus, body omissions, and bound integrity. The user's prompt named "divisio, littera, dubia" but the actual d.34 chunkset is seven files; all seven were swept.

## Boundary tile-out

d.34 is a single-pars distinction (no `p1`/`p2` chunks) with ARTICULUS UNICUS containing four questions. Raw range: 16585–18017 (`DISTINCTIO XXXIV.` at 16585; `DISTINCTIO XXXV.` at 18018).

| Chunk | line_start | line_end | OCR landmark above | OCR landmark at end |
|---|---|---|---|---|
| littera | 16585 | 16888 | `DISTINCTIO XXXIV.` at 16585 | divisio's `COMMENTARIUS IN DISTINCTIONEM XXXIV.` follows |
| divisio | 16889 | 16969 | `COMMENTARIUS IN DISTINCTIONEM XXXIV.` (also `TRACTATIO QUAESTIONUM` at 16940; `ARTICULUS UNICUS` at 16970) | a1-q1 begins at 16970 |
| a1-q1 | 16970 | 17308 | `ARTICULUS UNICUS.` at 16970 | running head `DIST. XXXIV. ART. UNICUS QUAEST. II.` at 17277 marks page-flow into next chunk; bare `QUAESTIO H.` at 17309 |
| a1-q2 | 17309 | 17542 | `QUAESTIO H.` (OCR-garbled `II.`) at 17309 | `QUAESTIO III.` at 17543 |
| a1-q3 | 17543 | 17680 | `QUAESTIO III.` at 17543 | `QUAESTIO IV.` at 17681 |
| a1-q4 | 17681 | 17796 | `QUAESTIO IV.` at 17681 | `DUBIA CIRCA LITTERAM MAGISTRL` (OCR garble for `MAGISTRI`) at 17797 |
| dubia | 17797 | 18017 | `DUBIA CIRCA LITTERAM MAGISTRI` at 17797 | `DISTINCTIO XXXV.` at 18018 |

Bounds tile cleanly across the d.34 raw range with no overlap and no gap. All `line_start`/`line_end` frontmatter values match these landmarks exactly.

## Per-chunk verdicts

### bon-sent-I-d34-littera.md — PASS WITH MINOR STATUS DRIFT

- **Bounds**: 16585–16888 verified.
- **Latin body**: 5 capitula (Capp. I–V) over printed pp. 582–584. Verbatim against OCR; reflowed Lombard text with embedded Hilary/Augustine block-quotations from the column-bleed footer band. No silent dropouts.
- **Apparatus**: 21 bilingual `**La.**`/`**En.**` entries `[^1]–[^21]`, all with content (no fabrication). The 2026-05-07 polish pass corrected `vi` → `ut` (twice) in `[^10]` and stripped a speculative bracketed gloss + trailing `[?]` from `[^18]`; both corrections sustained. All 21 markers present in both Latin and English bodies (pairing verified via marker-set diff).
- **transcription_status**: dated 2026-05-07; states "16 entries" — actual count is 21. **Frontmatter inaccuracy** (descriptive only; the parser does not consume this string). Pre-existing skeleton backup confirms the rebuild added all 21 from raw OCR; the frontmatter count is bookkeeping drift from the rebuild draft.
- **Verdict**: clean content. Recommend a one-line frontmatter polish (`16 entries` → `21 entries`); not applied here per "Commit nothing" instruction.

### bon-sent-I-d34-divisio.md — PASS

- **Bounds**: 16889–16969 verified. `COMMENTARIUS IN DISTINCTIONEM XXXIV.` at 16889; `DIVISIO TEXTUS`; `TRACTATIO QUAESTIONUM` at 16940 (correctly housed in the divisio per chunking convention); `ARTICULUS UNICUS.` (start of a1-q1) at 16970.
- **Latin body**: verbatim against OCR. Includes the four-question `TRACTATIO QUAESTIONUM` listing.
- **Apparatus**: 4 bilingual entries `[^1]–[^4]`. The 2026-05-07 polish pass stripped the speculative bracketed gloss `[in place of, apparently, *quae posset*]. [?]` from `[^3]`, leaving just `Vat. *quaestionem*.` per PDF 600dpi. Sustained. All 4 markers paired in both bodies.
- **transcription_status**: 2026-05-07; "4 entries" — matches.
- **Verdict**: clean. No edits.

### bon-sent-I-d34-a1-q1.md — PASS

- **Bounds**: 16970–17308 verified.
- **Latin body**: pp. 585–588 verbatim. The 2026-05-07 polish pass resolved `distinctione nona[?]` (line 17209 OCR confirms `supra, distinctione nona`), removed `praeterea[?]`/`termini[?]` flag-pairs in q1 ad-6 (variants documented in `[^16]`), and removed translator-confidence `[?]` hedges on `[^11]` and `[^13]`. All sustained.
- **Apparatus**: 16 bilingual entries `[^1]–[^16]`. Entry `[^16]` (the omnibus variants entry) intentionally absorbs the printed Quaracchi footnote-7 (`Pro praeterea plures codd. cum Vat. personae`) and footnote-8 (`Ex cod. I (T in marg.) et ed. I restituimus termini…`) — i.e., the chunk's apparatus indices do not 1:1 mirror the printed footnote indices on this question. This is documented in `d31-d40-polish-resolution-log.md` line 217 (deferred, since renumbering would touch all subsequent indices). Not a fabrication — content is OCR-grounded.
- **Scholion**: present, with three sections (I, II, III) and the standard commentator list (Alex. Hal., Scotus, S. Thom., Albert., Petr. a Tar., Richard. a Med., Ægid. R., Henr. Gand., Durand., Dionys. Carth.) — verbatim against OCR.
- **transcription_status**: 2026-05-07; "16 entries" — matches.
- **Verdict**: clean. No edits. (The `[^7]`/`[^8]` index-vs-printed-footnote misalignment is a known structural deferral, not an audit finding.)

### bon-sent-I-d34-a1-q2.md — PASS

- **Bounds**: 17309–17542 verified.
- **Latin body**: pp. 588, 590–591 verbatim. The 2026-05-07 polish pass resolved scholion-I citation `S. I. q. 13. a. 2. i. 12.` → `q. 13, a. 2, 4, 12` (PDF 600dpi confirmed `i.` was OCR garble for `4.`); sustained.
- **Apparatus**: 24 bilingual entries `[^1]–[^24]`. All 24 markers paired in both bodies. No fabrication detected on spot-check.
- **Scholion**: present (I, II), commentator list intact.
- **transcription_status**: 2026-05-07; "24 entries" — matches.
- **Verdict**: clean. No edits.

### bon-sent-I-d34-a1-q3.md — PASS

- **Bounds**: 17543–17680 verified.
- **Latin body**: pp. 591–592 verbatim. The 2026-05-07 polish pass corrected `[^1]`'s reference string from `q. 1, sic[?] dub. 3` to `q. 4, ac dub. 3` (PDF 600dpi confirmed); sustained in both Latin and English.
- **Apparatus**: 10 bilingual entries `[^1]–[^10]`, all with content. All 10 markers paired in both bodies. Apparatus reflows from the OCR footer band on 17640–17680 plus carry-over to next page-top.
- **Scholion**: present (I, II), commentator list intact.
- **transcription_status**: 2026-05-07; "10 entries" — matches. Has `ambiguities_logged: "manual-review/tier2-ambiguities-d34-a1-q3.md"`.
- **Verdict**: clean. No edits.

### bon-sent-I-d34-a1-q4.md — PASS

- **Bounds**: 17681–17796 verified.
- **Latin body**: pp. 593–594 verbatim. The 2026-05-07 polish pass removed translator-confidence `[?]` on `Petr. a Tar.` in scholion II (standard corpus abbreviation); sustained.
- **Apparatus**: 11 bilingual entries `[^1]–[^11]`, all with content. All 11 markers paired in both bodies.
- **Scholion**: present (I, II), commentator list intact.
- **transcription_status**: 2026-05-07; "11 entries" — matches.
- **Verdict**: clean. No edits.

### bon-sent-I-d34-dubia.md — PASS (with one substantive verification)

- **Bounds**: 17797–18017 verified.
- **Latin body**: pp. 595–597 verbatim, **seven dubia (DUB. I–VII) all present**.
  - **Critical verification**: the IA djvu OCR raw text contains explicit `DUB.` headings only for I, II, III, IV, V, and VI — **DUB. VII has no heading in the OCR raw**. Initial sweep flagged this as a possible silent fabrication (cf. d.27-DUB-V dropout pattern). **Resolved against PDF p. 186 (pdf-page 186 of `doctorisseraphic12bona.pdf`, extracted at 300dpi to `/tmp/d34dub-p-186.png`)**: the printed Quaracchi page-186 shows DUB. VI at top of col-a and DUB. VII near top of col-b, with the DUB. VII body running `Item quaeritur de hoc quod dicit, quod Scriptura appropriat Patri potentiam, ne videatur minus potens. Videtur hoc plus debere dici de Filio…` — exactly matching the chunk. The raw OCR column-bleeds DUB. VI's body and DUB. VII's body together (raw lines ~17960–17985 contain DUB. VII text — `…dicit polentiam ultimam et summum de potentia… maluit ei appropriare virtutem… Filio virtutem… trigesima secunda distinctione` — without the heading). The chunk correctly extracted and re-headed DUB. VII; **NOT a fabrication**.
  - The 2026-05-07 polish pass repaired DUB. VII Respondeo word-order garble (`scandalum, Graecis et[?] — ideo in stultitiam[^16]` → `scandalum, et Graecis in stultitiam[^16]`) per PDF p. 596 col-b; sustained.
- **Apparatus**: 18 bilingual entries `[^1]–[^18]`, all with content. All 18 markers paired in both bodies.
- **Scholion**: none (correct: `has_scholion: false`).
- **transcription_status**: 2026-05-07; "18 entries" + "seven dubia (DUB I–VII)" — matches.
- **Verdict**: clean. No edits.

## Totals

| Chunk | Verdict | Apparatus entries | Body `[?]` flags | Notes |
|---|---|---|---|---|
| littera | PASS w/ minor status drift | 21 | 0 | status says "16 entries" — descriptive inaccuracy |
| divisio | PASS | 4 | 0 | clean |
| a1-q1 | PASS | 16 | 0 | `[^7]/[^8]` printed-footnote-vs-chunk-index misalignment is a known structural deferral (logged in d31-d40-polish-resolution-log.md line 217), not an audit finding |
| a1-q2 | PASS | 24 | 0 | clean |
| a1-q3 | PASS | 10 | 0 | clean |
| a1-q4 | PASS | 11 | 0 | clean |
| dubia | PASS | 18 | 0 | DUB. VII OCR-headerless but PDF-confirmed; correctly captured |
| **TOTAL** | **7 PASS / 0 FAIL** | **104** | **0** | |

`[?]`-flag count is across `## Latin` and `## English` bodies only (each chunk's `transcription_status` frontmatter string contains the literal substring `[?]` as part of the descriptive boilerplate `[?] flags on ambiguous spots`; that is metadata, not a body flag).

## Anomalies

1. **Frontmatter `transcription_status` apparatus-count inaccuracy (1 of 7 chunks)**:
   - `bon-sent-I-d34-littera.md` — declares "16 entries", actual 21. Likely a draft-time count from before the rebuild added all OCR-Notae entries; carried forward into the final commit. Descriptive only; parser does not consume this string. Suggest a one-line frontmatter polish (`16 entries` → `21 entries`). **Not applied here per "Commit nothing" instruction.**

2. **DUB. VII heading absent from IA djvu OCR but present and verbatim in chunk** (dubia chunk):
   - Triggered initial silent-fabrication suspicion. Resolved by extracting `doctorisseraphic12bona.pdf` p. 186 at 300dpi and confirming the printed page has DUB. VI / DUB. VII as labeled section heads. The OCR's column-bleed dropped only the heading glyph, not the body. Chunk correctly recovers heading + body. **Not a finding.**

3. **a1-q1 `[^7]/[^8]` index-vs-printed-footnote misalignment** is a known structural deferral, already logged in `d31-d40-polish-resolution-log.md` line 217 — chunk apparatus indices `[^7]/[^8]` are NOT the same as printed-Quaracchi footnotes 7/8 on p. 588 (those variants are folded into chunk `[^16]`). Renumbering would touch all subsequent indices in both bodies; deferred as out-of-scope for the polish-blocker pass. **Not a finding** — content is OCR-grounded; only the index-mapping is non-1:1.

4. **No paraphrase, no fabricated apparatus, no body omissions, no Vat-variant inversions, no marker-pairing mismatches detected.**

## Build smoke-test

`cd site && node scripts/build-content.mjs`:

```
Built content.json: 1 book(s), 422 questions, 350 translated
```

Clean.

## Disposition

- **All 7 d.34 chunks PASS the sweep.** No file edits required.
- One non-blocking descriptive-frontmatter inaccuracy catalogued for future polish (littera apparatus-count).
- DUB. VII heading-absence-in-OCR resolved via PDF p. 186 inspection; chunk is correct.
- a1-q1 footnote-index misalignment carried forward as an existing deferral (already documented in d31-d40-polish-resolution-log.md).
- No backups created (no substantive edits made).
- Nothing committed.
