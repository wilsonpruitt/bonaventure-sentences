# d.37 scaffolds sweep audit (littera, p1-divisio, p1-dubia, p2-divisio, p2-dubia)

Date: 2026-05-08. Auditor: Claude (sweep follow-up to 2026-05-07 [?]-pass polish on d.37).

Scope: the five non-quaestio scaffold chunks of d.37 (multi-pars distinction, Pars I & Pars II):

- `vol1/bon-sent-I-d37-littera.md`
- `vol1/bon-sent-I-d37-p1-divisio.md`
- `vol1/bon-sent-I-d37-p1-dubia.md`
- `vol1/bon-sent-I-d37-p2-divisio.md`
- `vol1/bon-sent-I-d37-p2-dubia.md`

All five are stamped `Phase C Tier 2 complete (2026-05-07)`. Sweep verifies bounds, semantic-marker counts raw-vs-chunk, apparatus correspondence, anchor pairing, and absence of silent paraphrase or fabricated apparatus. **No substantive Latin or apparatus edits were made.** No backups created (no rebuild required).

Source of truth: `raw/bonaventure_vol1_pt2_raw.txt` (the printed Quaracchi pp. 633–666 fall in pt. 2). Frontmatter offset rule: PDF page = printed − 410 in this region (chunk frontmatter is consistent with this).

---

## Per-chunk verdict

### bon-sent-I-d37-littera.md — PASS (with two pre-flagged minor anomalies, acknowledged in chunk)

- **Bounds**: `line_start: 21452`, `line_end: 21915`.
  - Line 21452 = page-top `DISTINCTIO XXXVII.` (start of Lombard's text on printed p. 633). ✓
  - Line 21915 ends just before `DIST. XXXVII. P. I. DIVISIO TEXTUS.` running head at 21916 (= start of p1-divisio). ✓
  - `printed_pages: [633, 634, 635, 636]`; `pdf_pages: [223, 224, 225, 226]`. Frontmatter notes the correction from initial `[633…637]` — verified independently: line 21916 is the Bonaventure DIVISIO TEXTUS header (printed p. 637), so Lombard's littera proper does end on p. 636. ✓
- **Semantic markers raw-vs-chunk**: chunk presents Capp. I–VIII (Pars I = Capp. I–IV, Pars II = Capp. V–VIII). Raw page-running-heads at lines 21511, 21604, 21720 (`P. II.` switch), 21805 (p. 636) align with chunk page-break comments. The Pars-II Cap.-numbering ambiguity is pre-flagged in `transcription_status`; chunk's note at line 94 (Cap. VII) and 181 (English) acknowledges that Quaracchi prints these as Cap. VIII, kept here for body-flow consistency. **Author-acknowledged anomaly retained, not introduced by sweep.**
- **Apparatus**: 32 entries assembled from four page-footer notae blocks (12+9+1+10 per status string). Spot-verified against raw notae at lines 21574–21598 (p. 633 footer block) and 21580–21596 (continuation): contents of `[^1]` Coloss. 2, 9; `[^2]` *Errat Magister citando Gregorium…*; `[^3]` Epist. 187 c. 6 n. 19; `[^4]` Num. 24; `[^5]` Cap. 7 n. 81; `[^6]` Edd. 1, 3 *qui*; `[^7]` Ibid. n. 86 + Ier. 23, 24; etc. — all match raw OCR text. No fabricated entries.
- **Anchor pairing**: defs `[1..32]`; Latin body anchors `[1..32]`; English body anchors `[1..32]`. ✓
- **Pre-existing acknowledged anomalies (NOT introduced by sweep, not fixed by sweep)**:
  - **`[^8]` / `[^9]` content duplication** — both are `Cap. 66, 1. Vulgata: Caelum sedes mea etc.` The `[^8]` entry has an inline parenthetical noting "this note in the OCR footer appears under what is in fact n. 9 of the Quaracchi list and gives the cross-reference for the Isaiah quotation in cap. II; it is here renumbered to its OCR position." Body anchor `[^8]` sits at *aperte monstratur* (per the OCR footnote-marker spacing) but apparent original Quaracchi note 8 may have been a different reference. Renumbering preserved by author; left as-is for sweep scope.
  - **`[^20]` reused twice in Latin body** (`sordibus corporis[^20]` and `omnia replet[^20] loca`) — author note in `[^20]` definition acknowledges the reuse of OCR footer marker n. 5. Markdown is valid (both anchors will resolve to the same footnote); not a parser issue.
- **Inline `[?]` flags**: 0. `transcription_status` mentions three flags (Pars-II cap-numbering, an OCR-garbled column-rule glyph in n. 22, final Augustinus citation in n. 32) — these are author-acknowledged in the apparatus prose and the structural note rather than as inline `[?]` markers. Acceptable.
- **Fabricated apparatus / silent paraphrase**: none detected.

### bon-sent-I-d37-p1-divisio.md — PASS

- **Bounds**: `line_start: 21916`, `line_end: 21986`.
  - Line 21916 = `DIST. XXXVII. P. I. DIVISIO TEXTUS.` page-top heading (printed p. 637). ✓
  - Line 21997 = `ARTICULUS 1.` start (= next chunk a1-q1). 21986 ≈ end of footnote-1 prose at column-2 of p. 637 footer. ✓
  - `printed_pages: [637]`, `pdf_pages: [227]`. ✓
- **Semantic markers raw-vs-chunk**: COMMENTARIUS / DIVISIO TEXTUS / TRACTATIO QUAESTIONUM all present in raw at 21916, 21969; chunk reflects three-fold structure (`Prima pars… In secunda… In tertia…`) and Tractatio enumeration "Primo… Secundo… Tertio…". No silent dropouts.
- **Apparatus**: 1 entry — `[^1]` `Vat. suppressit secundo, quam vocem ex antiquioribus mss. et ed. 1 revocavimus…` Verified against raw line 21985–21986 (column-broken notae at `Vat. suppressit secundo… apparet ex paulo longiore lectione cod. R: ideo primo agit, quomodo Deus sit in rebus, et secundo etc.`). Faithful Latin transcription; English literal. ✓
- **Anchor pairing**: defs `[1]`, Latin `[1]`, English `[1]`. ✓
- **Inline `[?]` flags**: 0. Status string mentions "[?] flags on ambiguous spots" — none actually present; minor status-string overstatement, same pattern as d.30/d.35 sweeps.
- **Fabricated apparatus / silent paraphrase**: none.

### bon-sent-I-d37-p1-dubia.md — PASS

- **Bounds**: `line_start: 23038`, `line_end: 23291`.
  - Line 23038 = `DIST. XXXVII. P. I. DUBIA.` running head (printed p. 649). ✓
  - Line 23292 = `COMMENTARIUS IN DISTINCTIONEM XXXVII. Pars II.` (start of next chunk p2-divisio). ✓
  - `printed_pages: [649, 650, 651]`, `pdf_pages: [239, 240, 241]`. p. 651 col-a contains DUB V–VI, col-b begins Pars II material — chunk correctly clips at the column boundary. ✓
- **Semantic markers raw-vs-chunk**: chunk presents DUB I–VI. Raw OCR (mangled by two-column layout):
  - DUB. I @ line 23133 (`DuB. I.`)
  - DUB. II @ line 23194
  - DUB. III @ line 23158 (`DuB. Ili.`)
  - DUB. IV @ line 23183
  - DUB. V @ line 23224 (`Dhb. V.`)
  - DUB. VI @ line 23282 (`DuR. VI.`)
  - All six accounted for; chunk has all six DUBs with bodies and Respondeos. **No DUB silently missing** (this was the d.27-class concern — clean here.)
- **Apparatus**: 16 entries, all traceable to raw page-footer notae at lines 23231–23257 (p. 650 footer block: 9 notes) + lines 23330–23339 (p. 651 col-b footer carryover for p1-dubia material — 7 notes). Spot-checked: `[^1]` Act. 17, 28; `[^2]` Libro X. c. 27. n. 38; `[^7]` Vers. 1. Glossa Lyrano *Erat apud Deum*; `[^15]` long *id est, infectio carnis…* note; `[^16]` Cap. 4 *Verba proxime subiexa a Vat.…*. All match raw. ✓
- **Anchor pairing**: defs `[1..16]`, Latin `[1..16]`, English `[1..16]`. ✓
- **Inline `[?]` flags**: 0; status-string boilerplate as above.
- **OCR cleanup**: chunk silently corrects raw OCR garbles per project rule (e.g. raw `intelleciu non capimus` → chunk `intellectu non capimus` in DUB IV). Defensible, conservative.
- **Fabricated apparatus / silent paraphrase**: none.

### bon-sent-I-d37-p2-divisio.md — PASS

- **Bounds**: `line_start: 23292`, `line_end: 23368`.
  - Line 23292 = `COMMENTAMUS IN DISTINCTIONEM XXXVII.` (OCR `COMMENTAMUS` for `COMMENTARIUS`; chunk silently normalized — defensible). ✓
  - Line 23363 = `ARTICULUS 1.`, line 23369 = `QUAESTIO I.` (= start of next chunk p2-a1-q1). 23368 ≈ blank line before. ✓
  - `printed_pages: [651]`, `pdf_pages: [241]`. ✓
- **Semantic markers raw-vs-chunk**: COMMENTARIUS / Pars II / DIVISIO TEXTUS / TRACTATIO QUAESTIONUM at 23292/23309/23348 + the page-cite `TEXTUM MAGISTRI VIDE SUPRA PAG. 638` at 23305 — all present in chunk. Chunk also fronts `Articulus II. *De mutabilitate Angelorum per locum.*` per the Tractatio enumeration. No silent dropouts.
- **Apparatus**: 2 entries.
  - `[^1]` `Vat. locabilitas.` — matches raw line 23335.
  - `[^2]` `Vat., supra posito quatuor partes pro tres partes…` — matches raw lines 23336–23339.
  - Raw page-footer columns at 23330–23339 also contain the *carryover* notes for p1-dubia DUB V/VI (Vers. 13, *Id est, infectio carnis*, *Cap. 4. — Verba proxime subnexa a Vat.…*, *Ed. I videtur*) — chunk correctly **excludes** these (they belong to p1-dubia, which already incorporates them). No fabrication; no over-extraction.
- **Anchor pairing**: defs `[1, 2]`, Latin `[1, 2]`, English `[1, 2]`. ✓
- **Inline `[?]` flags**: 0; status-string boilerplate.
- **Fabricated apparatus / silent paraphrase**: none.

### bon-sent-I-d37-p2-dubia.md — PASS

- **Bounds**: `line_start: 24645`, `line_end: 24846`.
  - Line 24645 = `DUBIA CIRCA LITTERAM MAGISTRL` (OCR `MAGISTRL` for `MAGISTRI`). ✓
  - Line 24851 = `DISTINCTIO XXXVIII.` (= start of next distinction). ✓
  - `printed_pages: [665, 666]`, `pdf_pages: [255, 256]`. Page break in chunk between DUB IV and its long Respondeo at line 62 (`<!-- page 666 -->`) verified against raw layout. ✓
- **Semantic markers raw-vs-chunk**: chunk presents DUB I–IV. Raw markers:
  - DUB. I @ line 24649
  - DUB. II @ line 24691
  - DUB. III @ line 24729
  - DUB. IV @ line 24721
  - (No DUB V or beyond before line 24851 = next distinction.)
  - All four DUBs accounted for; chunk has all four with bodies and full Respondeos (DUB IV's long four-mode treatment intact). **No DUB silently missing.**
- **Apparatus**: 11 entries.
  - `[^1]` Vers. 18 + Glossam … apud Lyranum.
  - `[^2]` Aristot. *de Praedicam.* c. *de Motu* (six species).
  - `[^3]` Aristot. VIII *Phys.* + IV *Phys.*
  - `[^4]` Supple cum codd. P Q W *est motus* / cod. D *transit*…
  - `[^5]` Long Liber de Causis prop. 10 + Dionysius cross-reference.
  - `[^6]` Vide supra pag. 411 nota 6, Boethius *de Unitate et uno*…
  - `[^7]` *Patet* pro *videtur* + Vat. *paulatim* / *paulative* + Du Cange.
  - `[^8]` Hoc dubium solvitur a B. Alberto…
  - `[^9]` B. Albert., hic a. 27, long Aristotelian methodological note + cod. T *sed primum* + cod. L variants.
  - `[^10]` Augustine *Epist.* 487 *ad Dardan.* n. 10 + *de Civ. Dei* XXII c. 29 n. 3 + Damascene + *Elucidarium*.
  - `[^11]` Vat. *fundatur ei* + cod. Y addit *scilicet rei in causa*.
  - All eleven entries traceable to the raw page-footer notae blocks of pp. 665–666; faithful Latin, literal English. No fabrication. ✓
- **Anchor pairing**: defs `[1..11]`, Latin `[1..11]`, English `[1..11]`. ✓
- **Inline `[?]` flags**: 0; status-string boilerplate.
- **Fabricated apparatus / silent paraphrase**: none.

---

## Totals

| chunk | bounds | DUBs/Caps | apparatus | anchors La/En/def | inline [?] | rebuild? |
|---|---|---|---|---|---|---|
| littera | 21452–21915 ✓ | Capp. I–VIII (8) | 32 (12+9+1+10) | 32/32/32 ✓ | 0 | no |
| p1-divisio | 21916–21986 ✓ | divisio + Tractatio (3 art) | 1 | 1/1/1 ✓ | 0 | no |
| p1-dubia | 23038–23291 ✓ | DUB I–VI (6) | 16 | 16/16/16 ✓ | 0 | no |
| p2-divisio | 23292–23368 ✓ | divisio + Tractatio (2 art) | 2 | 2/2/2 ✓ | 0 | no |
| p2-dubia | 24645–24846 ✓ | DUB I–IV (4) | 11 | 11/11/11 ✓ | 0 | no |

- **Bound mismatches**: 0
- **Silently-missing DUBs/Caps** (the d.27-class concern): **0**
- **Fabricated apparatus entries**: **0**
- **Silent-paraphrase footprint**: **0** detected on spot-check (chunks are verbatim-from-OCR with documented OCR-cleanup corrections only)
- **Marker-pairing failures**: **0**
- **Per-chunk audit log entries written**: this file. No `tier2-ambiguities-d37-*.md` files were modified — they are pre-existing skeletons from the polish pass and require no updates from this sweep.

## Anomalies (carried over, not introduced)

1. **littera `[^8]` / `[^9]` apparatus duplication** — author-acknowledged via inline parenthetical in `[^8]`. Body anchor `[^8]` may need re-mapping to a Sap. 8, 1 reference if a future deeper pass elects to disambiguate; outside polish-blocker scope.
2. **littera `[^20]` body-anchor reuse** — author-acknowledged in apparatus def. Markdown valid; no parser impact.
3. **littera Pars-II Cap-numbering offset** — author-flagged: chunk numbers Pars II caps as V–VIII for body-flow continuity, while Quaracchi prints them as V, VII, VIII, IX. Structural rewrite deferred per chunk's own inline note. Outside polish-blocker scope.
4. **All five chunks**: `transcription_status` boilerplate ends with `"[?] flags on ambiguous spots"` although **none of the five carries inline `[?]` markers**. Minor status-string overstatement (same pattern observed in d.30 and d.35 sweeps). Recommendation: when the status string is next touched (e.g. for unrelated edits), trim that phrase from p1-divisio, p1-dubia, p2-divisio, and p2-dubia. The littera status string carries genuine substantive provenance and should be preserved.

## Build smoke-test

```
$ cd site && node scripts/build-content.mjs
Built content.json: 1 book(s), 422 questions, 350 translated
```

Clean. ✓

## Verdict

All five d.37 scaffold chunks **PASS** the sweep audit. No silent paraphrase, no fabricated apparatus, no missing DUBs/Caps, no anchor-pairing failures. The pre-flagged littera anomalies are author-acknowledged and out of polish-blocker scope. d.27-class missing-section pattern: not present in d.37.
