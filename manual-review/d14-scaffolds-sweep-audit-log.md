# d.14 Scaffolds Sweep Audit Log — 2026-05-08

Audit of `bon-sent-I-d14-{divisio,littera,dubia}.md` per the d.4–d.9 sweep methodology. All three chunks were already promoted to Tier 2 on 2026-05-02 with apparatus drawn from OCR; this audit re-verifies bounds, body fidelity, and apparatus content against `raw/bonaventure_vol1_raw.txt`. Only the `dubia` chunk required substantive edits — to resolve four prior `[?]`-flagged apparatus entries.

## Per-chunk verdict

### bon-sent-I-d14-littera  (lines 45344–45634)
**Verdict: PASS (no rebuild needed).**

- Bounds verified. `DISTINCTIO XIV.` at OCR line 45344; running-head break to printed page 243 at line 45491; chunk's `<!-- page 243 -->` placed at the OCR-confirmed paragraph boundary (between the second Ambrose-quotation block and `«Quid autem dubitem dicere…»`). Body terminates correctly before `SENTENTIARUM LIB. I.` running head and the `COMMENTARIUS IN DISTINCTIONEM XIV.` opener at line 45635.
- `## Latin` body diffs cleanly against OCR lines 45344–45489 (page 242) and 45491–45633 (page 243). Punctuation, italics, Quaracchi quotation marks (« »), Augustine/Bede/Ambrose citations all match. Marginal labels (`De temporali processione in specie.`, `Quod ipse Spiritus sanctus, non solum dona, datur hominibus`) correctly absorbed/excluded.
- 27-footnote apparatus verified against OCR page-242 NOTAE (lines 45415–45485) and page-243 NOTAE (lines 45517–45634 footer). Spot-checked entries [^1], [^2], [^5], [^7], [^10], [^14], [^16], [^20], [^27] — all match OCR verbatim, including the long n-46 transposition note in [^7] and the Vat./edd. variant catalog in [^9] [^15] [^18] [^19] [^20].
- English translation literal and parallel paragraph-for-paragraph; renders Quaracchi's `« »` quotation marks as English `"…"` and preserves italic emphasis on Latin formulae.
- No `[?]` flags raised.

### bon-sent-I-d14-divisio  (lines 45641–45750)
**Verdict: PASS (no rebuild needed).**

- Bounds verified. `COMMENTARIUS IN DISTINCTIONEM XIV.` at OCR line 45635; `DIVISIO TEXTUS.` at line 45641; `TRACTATIO QUAESTIONUM.` at line 45705. Body extends to roughly line 45744 (closing `Secundo, utrum processio temporalis ponat in numerum cum aeterna.`); chunk `line_end: 45750` is generous-but-correct (covers the trailing whitespace before the page-244 NOTAE footer).
- `## Latin` body diffs cleanly against OCR. Five-paragraph DIVISIO TEXTUS plus the TRACTATIO QUAESTIONUM listing of two principal questions are present and ordered correctly. Footnote anchors `[^1]`–`[^8]` are placed at the OCR superscript positions (e.g. `per ¹`, `Hic quaeritur, utrum semel tantum missus sit ²`, `ostendit ³`, `quaerit ⁴`, `tria capitula ⁵`, `Hic quaeritur, utrum et sancti viri dent vel possint dare ⁶`, `ab eius ministerio ⁷`, `Primo quaeritur ⁸`).
- 8-footnote apparatus verified against the page-243-bottom NOTAE block (the divisio footer continues onto the next page; OCR footers spanning lines ~45517–45634 cover both littera-ending and divisio-opening footnotes — Quaracchi's per-page footer numbering is preserved). Spot-checked [^1] (Vat. *secundum*), [^2] (Vat. falso *Nunc de Spiritu sancto videndum est*), [^5] (Vat. *tres partes* vs *tria capitula*), [^6] (Vat.'s long alternate-presentation note), [^8] (supplied *Primo quaeritur*). All match OCR verbatim.
- English translation literal; explicit interpolations bracketed (`[the Spirit proceeds]`, `[as the opening, namely]`, `[reads]`, etc.) per Tier-2 convention.
- No `[?]` flags raised.

### bon-sent-I-d14-dubia  (lines 47036–47318 body, footers extending to 47396)
**Verdict: EDITED — four prior `[?]`-flagged apparatus entries resolved against OCR.**

- Bounds verified. `DUBIA CIRCV LITTEKAM iVl.\GlSTRI.` (OCR garble of `DUBIA CIRCA LITTERAM MAGISTRI.`) at line 47036; `DUB. I` at 47039; `DUB. II` at 47064; `DUB. III` at 47095; `DUB. IV` at 47168; `DUB. V` at 47195; `DUB. VI` at 47216. Body of Dub VI continues at OCR line 47296 (after the OCR's spurious `DISTINCTIO XV.` running-head insertion at 47290 — this is a column-OCR layout artifact, NOT a semantic boundary; the actual d.15 begins at line 47798 with the next `DIVISIO TEXTUS.`). Body of Dub VI correctly closes at line 47318 with `caritas habet originem indeficientem, sicut fluvius`. The chunk's `<!-- page 234 -->` and `<!-- page 235 -->` markers are placed at correct paragraph boundaries (mid-Dub-III for p.234, mid-Dub-VI for p.235).
- `## Latin` body diffs cleanly across all six dubia. Punctuation, italics, ellipses match OCR. Footnote anchor positions verified against OCR superscripts (`Magister ¹`, `declarationem ²`, `trium ³`, `Magister ⁴`, `exibat ⁵`, `primo ⁶`, `Spiritus sancti ⁷`, `facta sunt ⁸`, `ad ⁹`, `in quantum ¹⁰`, `dicetur ¹¹`, `decimo ¹²`, `vigesimo ¹³`, `secundo ¹⁴`, `Rabanus ¹⁵`, `item ¹⁶`, `controversia ¹⁷`, `quinto ¹⁸`, `nono ¹⁹`, `restringit ²⁰`, `Gregorius ²¹`, `animae ²²`, `verbo ²³`, `intra ²⁴`, `Gregorius ²⁵`, `septimo ²⁶`, `deficiente ²⁷`, `fluvius ²⁸`).
- **EDIT — [^24], [^25], [^27], [^28] resolved against OCR Dub VI footnote block at lines 47388–47396** (OCR's `1 Nonnulli codd. ut T V W X intiis. / ' Homil. 30. in Evang. n. 2. ' Vers. 38. / * Praeferimus leclionem codd. L 0 deficiente loco deficiendi, quia et in se verior est et cum subnexis conformior. / 5 Egregie de hoc loquitur S. Doctor in Commcnt. in loan. c. 8, 39 (Supplem. Bonelli, tom. I. col. 735.).`). Prior versions of these four entries were placeholder text reading "OCR truncated", "exact locus unrecovered from OCR", or "exact OCR text not recovered" — with `[?]` markers. The OCR is intact: the prior chunk author missed that the Dub VI footers fall *after* the spurious `DISTINCTIO XV.` running-head garble at line 47290, not before it. Replaced placeholders with verbatim Latin and literal English bilingual entries. No content fabrication; all four entries trace directly to OCR lines 47388, 47390, 47392–47393, 47395–47396 respectively.
- Other apparatus entries [^1]–[^23] verified against OCR page-244 NOTAE (lines 47104–47133) and page-244-bottom-right NOTAE (lines 47222–47287). All match OCR verbatim. The Rabanus/Glossa-ordinaria long quotation in [^15] preserves the full OCR text including the Lyrani-1488-attribution note.
- English translation literal; *Respondeo* / *Ad hoc* / *Item quaeritur* formulae rendered consistently.
- All four prior `[?]` flags now cleared. No new `[?]` flags raised.

## Totals

| Chunk | Bounds | Latin body | English | Apparatus entries | Fabricated entries | `[?]` raised | `[?]` cleared |
|---|---|---|---|---|---|---|---|
| littera | 45344–45634 (verified) | clean | clean | 27 | 0 | 0 | — |
| divisio | 45641–45750 (verified) | clean | clean | 8 | 0 | 0 | — |
| dubia | 47036–47318 body / footers to 47396 (verified) | clean | clean | 28 | 0 | 0 | 4 |
| **TOTAL** | | | | **63** | **0** | **0** | **4** |

## Anomalies

1. **Dubia OCR layout artifact**: at raw lines 47290 and 47320 the OCR inserts spurious `DISTINCTIO XV.` running heads inside the body of Dub VI. These come from column-OCR layout glitches (the page-bottom running head is duplicated above and below the column gutter). The actual `DISTINCTIO XV.` semantic boundary is at line 47798 (`DIVISIO TEXTUS.`). A prior chunk author appears to have stopped reading OCR at line 47290 on first pass, missing the Dub VI footnote block at 47388–47396 — this is the root cause of the four `[?]` flags now resolved. **Lesson for future audits**: when a chunk's `[?]` flags cluster at the *end* of its OCR range, look beyond the next OCR running-head garble before concluding the footers are unrecoverable.

2. **`printed_pages` frontmatter potentially off-by-one or off-by-two across all three chunks** (divisio claims [242, 243], littera claims [242, 243], dubia claims [233, 234, 235]). Cross-checking OCR page-number markers: littera spans printed pages 242–243 (verified by `242` running-head garble at OCR line 45338 and `243` at line 45491), correct as labeled; divisio falls between page-243 marker (line 45491) and the next visible page-246 marker (line 45888) with the page-244-and-245 markers eaten by OCR — divisio likely on pp. 244–245, NOT 242–243; dubia falls between line 47036 (well past page 246) and runs to ~line 47396, so the `[233, 234, 235]` claim is inconsistent — actual printed pages are likely 254–255. This is a **metadata** issue, not a body/apparatus issue, and does not affect rendered output; flagging here for a future frontmatter-cleanup pass. Not addressed in this sweep per scope (sweep targets body + apparatus damage, not frontmatter pagination).

3. **No fabrication, no body omissions, no bound leakage, no misplaced page breaks** across the three chunks. d.14 falls in the same "post-d.9-lessons-applied" cohort as d.10–d.13: chunks were built directly from OCR with the bilingual `**La.**`/`**En.**` apparatus convention from the start, and the only audit findings are: (a) four self-flagged unresolved-from-OCR placeholders in dubia, all now resolved; (b) the cosmetic `printed_pages` frontmatter inconsistency.

## Backups

- `vol1/_backup-d14-dubia-pre-rebuild-20260508/bon-sent-I-d14-dubia.md` — pre-edit copy with the four `[?]` placeholders intact, recoverable for diff.

No backups for divisio or littera — no edits made.

## Build smoke-test

`cd site && node scripts/build-content.mjs` — see post-audit run.
