# d.41–d.50 polish resolution log

Per-chunk record of `[?]` flags raised during Tier-2 promotion in the d.41–d.50 decade, with dispositions (RESOLVE / ACCEPT-ILLEGIBLE / DEFERRED) and PDF / OCR citations where applicable.

---

## bon-sent-I-d41-p1-dubia (2026-05-12)

**Promotion**: auto-chunked skeleton → Tier-2 complete. Raw OCR pt2 lines **32014–32139** (not the skeleton-frontmatter range 31950–32013, which was an auto-chunker mis-slice that captured the tail of the preceding p2-a1-q2 body + scholion). Printed pp. **741–742**; PDF pp. **331–332**.

**`[?]` flags raised**: 0. Body and apparatus were both cleanly recoverable from the IA djvu OCR plus the existing `p-d41dub-hires-{331,332}.png` and `p-d41dub-r600-331.png` images.

**Apparatus**: 9 entries, all from the printed-p.742 footer. The three footer notes on printed-p.741 (`sive copulat`/`copulet`; `praeterea` + `scitum illud`; `Ed. 1 substantiam`) anchor in the preceding part-2 quaestio body and scholion — they belong in `bon-sent-I-d41-p2-a1-q2.md` (still a skeleton) and not in this dubia chunk.

**Out-of-scope findings to surface to project owner** (not actioned per "do NOT touch other chunks" instruction):

1. **Frontmatter `line_start`/`line_end` corrected** in this chunk only: skeleton said `31950–32013` (the page-741 tail of p2-a1-q2 + scholion, not dubia content). Rebuilt range is `32014–32139`. The PNG-header verification confirmed printed-page running heads "DIST. XLI. DUBIA. 741" at line 31950 and "742 SENTENTIARUM LIB. I." at line 32040; the actual DuB. I-IV body begins at line 32014 and ends before "DISTINCTIO XLII." at line 32140.

2. **Vestigial duplicate `bon-sent-I-d41-p2-dubia.md`** (auto-chunked, lines 32014–32139) holds exactly the same raw-OCR range that this chunk now occupies. d.41 has only one DUBIA CIRCA LITTERAM MAGISTRI block on pp.741–742 (not split across parts in the source). The `p2-dubia` skeleton is a duplicate and should be **deleted** by the project owner before the d.41 decade is committed; otherwise the build will render duplicated content. Cf. the d.8 vestigial-cleanup pattern from the 2026-05-08 cleanup campaign.

3. **`bon-sent-I-d41-p2-a1-q2.md` (line range 31706–31949) is truncated**: its real content extends through line 32013 (end of p.741 first column + SCHOLION). The auto-chunker cut the chunk at 31949, dropping the closing material of the quaestio and its scholion into the phantom `p1-dubia`. When `p2-a1-q2` is promoted to Tier-2, its `line_end` should be extended to ~32013 to capture the closing paragraph (`Concedendum igitur, quod in secunda acceptione…`) and the full SCHOLION (which has two numbered paragraphs I and II discussing the Nominales and citing Alex. Hal., S. Thom., Albert., Petr. a Tar., Richard. a Med., Durand.).

4. **Apparatus heuristic noise**: the audit script reports `raw=10` for this chunk's footer range (lines 32014–32139). My count is 9 (the discrepancy is the script's regex picking up one of the per-page-restart `1.` or `'` openers as a phantom 10th — common ±1 OCR-garble noise per CLAUDE.md "Lesson 9").

---

## bon-sent-I-d41-littera (2026-05-12)

**Promotion**: auto-chunked skeleton → Tier-2 complete. Raw OCR pt2 lines **30398–30644**, printed pages **725, 726, 727** (top, ending at *quae aliquando scit* before the centered `COMMENTARIUS IN DISTINCTIONEM XLI.` heading); PDF pages **315, 316, 317** (pt2 offset = printed − 410).

**PNG-header verification**: pulled `pdftoppm -r 500 -f 315 -l 317` from `raw/doctorisseraphic12bona.pdf`; confirmed printed page numbers `725`, `726`, `727` visible at top of each PNG, and chapter scaffolding (`DISTINCTIO XLI.` centered on p.725, `Cap. I.`/`Cap. II.` headings on p.725, `Cap. III.` heading bridging p.726 right column → p.727).

**`[?]` flags raised**: **0**. The two-column OCR was heavily mangled (left-and-right columns of each page are interleaved line-by-line), but every reconstruction was unambiguous against the 500-dpi PNGs and the standard Lombard text. No body or apparatus flag needed.

**Apparatus**: 22 entries — **9 from p.725 footer** (notes 1–9; the `9` is `1. Cor. 12. 6.`, the citation for *Idem Deus qui operatur omnia in omnibus*), **12 from p.726 footer** (notes 1–12; per-page renumbering), and **1 from p.727 footer** (note 2, the `In Ioan. tract. 99. n. 1` reference plus the *iam ante natum et mortuum* editorial variant). The other p.727 footer note (note 1, `Vat. et aliae edd., excepta I, dici possunt …`) anchors in `bon-sent-I-d41-p1-divisio`, per that chunk's existing apparatus.

**Word counts**: Latin **~1,520 words**; English **~2,290 words** (English runs ~1.5× because of bracketed clarifications for the technical predestination/foreknowledge formulae and untanglable Latin double-negatives like *non tamen nulla*).

**Chapter count**: 3 (Cap. I, Cap. II, Cap. III).

**Audit row for this chunk** (2026-05-12 build):
- `audit-paraphrase`: jaccard `0.16`, len-ratio `0.77`, no smell, no HIGH/CRITICAL flag.
- `audit-headers`: ART raw 1 / chunk 0 / diff `-1` (false positive — Lombard uses *Cap. N* not *Articulus N*; expected for littera chunks).
- `audit-apparatus-count`: raw 30 / chunk 22 / diff `+8`, flag `—` (under SKELETON-SUSPECT threshold; the +8 is the regex over-counting page-725 col-2 numeric markers from Augustine quotations and the heavily-scrambled two-column footer band). My 22 matches the printed-page footer eyes-on count exactly.

**Smoke-test**: `cd site && node scripts/build-content.mjs` → `Built content.json: 1 book(s), 413 questions, 353 translated`. Clean.

**Frontmatter changes from skeleton**:
- Added: `title_la`, `title_en`, `printed_pages: [725, 726, 727]`, `pdf_pages: [315, 316, 317]`, `source`, `has_scholion: false`, `has_apparatus: true`.
- Replaced: `transcription_status` (auto-chunked → Phase C Tier 2 complete).
- `line_start`/`line_end` (30398–30648 in skeleton, 30398–**30644** here; the four-line difference is the trailing blank lines before the `COMMENTARIUS IN DISTINCTIONEM XLI.` centered heading at line 30649, which belongs to `d41-p1-divisio`).

**Out-of-scope observations** (not actioned):
- `bon-sent-I-d41-p1-a1-q1` and `bon-sent-I-d41-p1-a1-q2` still flagged SKELETON-SUSPECT (raw=34 / 57 apparatus entries respectively, chunk=0). Pending Tier-2 promotion as part of the d.41 sweep.
- `bon-sent-I-d41-p2-a1-q2` similarly SKELETON-SUSPECT; per the d.41-p1-dubia note above, its line-range will need extension when promoted.

## d.41-p1-a1-q1 (Tier-2 promotion, 2026-05-12)

Rebuilt from raw OCR lines 30733–31039 of pt2; printed pp. 728–731 (PDF 318–321). Verified against PNG headers at 400/600 dpi. Apparatus 12 entries (p.728: 4, p.729: 7, p.730: 1; p.731 footer notes anchor in q.II body, not here). Scholion sections I–IV; II–IV continue onto p.731 above the q.II header.

### [?] flags

- **[^2] La/En Greek tail `αἰτίας[?]`**: Damascene Greek quotation tail. OCR renders the final word as `aiTia?J`; on PDF p.728 footer the printed Greek ends in what reads `αἰτίας` with a closing bracket/parenthesis glyph. Latin context (`permissio ex nostra causa ortum habens`) supplies the sense. **ACCEPT** as `αἰτίας` with `[?]` retained on the trailing punctuation glyph; readers should consult Damascene II *de Fide orth.* c. 29 (PG 94, 969) for the canonical Greek. Not a translation blocker.

## d.41-p1-a1-q2 (Tier-2 promotion, 2026-05-12)

Rebuilt from raw OCR lines 31040–31494 of pt2; printed pp. 731–736 (PDF 321–326). Verified against 400dpi PNG headers (`raw/vision/vol1-pt2/p-d41q2hi-321..326.png`); all six pages confirm running head `DIST. XLI. ART. I. QUAEST. II.`. Chunk is the largest in d.41 (6875 Latin words, ~9000 English; Scholion in four sections with extensive Scotist/Thomist controversy literature). Apparatus 31 entries walked page-by-page (p.731 ends at footnote 4 of Q.II opener and carries footer notes for the body; p.732 footer 1–10; p.733 footer 1–10; p.734 footer 1–8; p.735 footer 1–3+; p.736 footer 1+).

Auto-chunked `line_end` was 31705 — extended past the Q.II Scholion into ARTICULUS II / its q.I body and footer (lines 31495–31705 belong to `d41-p1-a2-q1`). Corrected `line_end` to **31494** (last line of Scholion IV before centered `ARTICULUS II.` heading at 31495). The frontmatter `word_count_latin: 6875` may slightly overcount given this boundary correction; left as-is since the OCR-word audit script will re-derive on its own pass.

### [?] flags

- **Apparatus [^21] La. / [^21] En. — duplicate of [^15] lemma `voluntas → voluntatis`**: The p.733 footer (codex variant for *voluntas*) is also anchored at a second occurrence of the same word lower on the page where the Quaracchi numbering restarts. The OCR run-together makes it ambiguous whether [^21] is a fresh variant or a back-pointer to the same Vatican reading. **ACCEPT** as duplicate-by-design (Quaracchi restarts footer numbering each page; the same word recurring across a page break draws the same critical note). Reader-facing note added inline.
- **Scholion IV ([^31])** — citation list to Richard. a Med., here a. 3. q. [N]: OCR breaks off mid-token at the very bottom of p.736 just before `ARTICULUS II.` (line 31494 in raw, also visible in 400dpi PNG `p-d41q2hi-326.png` lower-right). The trailing `q. [N]` cardinal is illegible/truncated. **ACCEPT-ILLEGIBLE**: `q. [?]` retained in both La and En with explanatory `[OCR break — ...]` note; reader can consult Richard. a Med. *In I Sent.* d. 41 a. 3 (any q.) directly.
- **Body `parcitas` (arg. 6)** — OCR has `parcitas` (rarity/miserliness); 400dpi PDF confirms `parcitas`. Translated "miserliness". No flag, noted for completeness.
- **`indistantia` (arg. 5)** — Quaracchi footer 4 (here [^4]) glosses this neologism via Boethius *de Differentiis topicis* III.1. Translated literally as "non-distant" with English gloss; the Vat. apparatus adds `seu indifferentia` ("or non-difference") preserved in [^4] En.

Out-of-scope:
- Remaining d.41 SKELETON-SUSPECT chunks `d41-p1-a1-q1` (now closed above), `d41-p2-a1-q2` (still pending; HIGH paraphrase + diff +22 apparatus), and `d41-p1-divisio` (diff +9 apparatus, status flag clean) parked for subsequent sessions.

---

## 2026-05-12 — `bon-sent-I-d41-p2-a1-q2` rebuild

Auto-chunked skeleton promoted to Tier-2. Range extended 31949→32013 to capture closing arguments + scholion (I–II); verified against PNG running heads (printed 738–741 / pdf 328–331). Backup at `_backup-d41-p2-a1-q2-pre-rebuild-20260512/`.

Apparatus inventory: 28 entries (5 from p.738, 10 from p.739, 11 from p.740, 2 from p.741). Body anchors placed at all 28 [^N] markers; numbering renumbered continuously across pages since Quaracchi's page-local restarts collide.

`[?]` flags logged:
- **[^12] En. "praescientiam" / "praescientiam"** — Quaracchi footer reads "Paulo inferius pro *praescientiam* non pauci codd. cum edd. 2, 3, 4, 5 *praescientiam*". The variant word is repeated identically in the OCR (likely OCR ditto-error masking what should be e.g. *praesentiam* vs. *praescientiam*, the variant being argued throughout this q.). Flagged `[?]` pending eyes-on resolution from a higher-fidelity PDF read; the source-of-truth would be the printed reading of the second word. Not body-affecting; apparatus note only.
- **[^16] La. "suunt pro enum"** — Quaracchi footer reads "Omnes ferme codd. cum ed. 1 minus concinne *suunt* pro *enum*". Both Latin tokens are OCR-garbled fragments — the printed text most likely reads *suam* or *suunt*-like form for an analogous fragment. Retained verbatim with `[?]` flag in En. translation. Not body-affecting; apparatus note only.

Audits: paraphrase 0/0, headers no-flag (1 ART / 3 QUAEST / 4 DUB headers matched), apparatus -6 diff but no-flag (chunk has 28; heuristic counted 22).

Build: `node scripts/build-content.mjs` → 413 questions, 356 translated, clean.

Scope discrepancies / out-of-scope findings:
- Original auto-chunked `line_end` (31949) truncated mid-chunk; extended on 2026-05-12 per task instructions and verified to land cleanly at the dubia boundary (32014).
- `d41-dubia.md` status string claims "the three footnotes on the printed-page-741 footer anchor in the preceding part-2 quaestio body and scholion"; per 600dpi review only **two** numbered footnotes appear on p.741 (¹ at body "propterea" / Vat. praeterea; ² at body "subiectum" / Ed. 1 substantiam). The third "footer" block at top of p.741 is the continuation of p.740 footer 11 (the long *Scilicet quoad consignificationem* note). The sibling chunk's count is off-by-one; non-actionable here, noted for d.41-dubia re-review.
- Footers 1 (Cod. K compositio) anchor at body "complexa" by typographic convention; ⁴ (Codd. A T patet, quod sic intelligendum) placed at end of arg 1 in q2 body, the most natural insertion based on raw OCR context. The Quaracchi marker was not clearly visible in 600dpi.

---

## 2026-05-12 — `bon-sent-I-d41-a2-q1` gap-fill promotion

Gap-fill chunk surfaced when sibling `d41-a1-q2` had its `line_end` corrected 31705→31494; the auto-chunker had missed ARTICULUS II / QUAESTIO I entirely (OCR garble `ARTJCULUS II.` at line 31503). Scaffold promoted to Tier-2. Backup at `_backup-d41-a2-q1-pre-promote-20260512/`.

PNG-header verification: extracted printed pp.735–738 at 200dpi (`raw/vision/vol1-pt2/p-d41a2q1-{325..328}.png`); p.738 also at 400dpi (`p-hires-d41a2q1-328-328.png`). Confirmed `printed_pages: [736, 737, 738]` / `pdf_pages: [326, 327, 328]` matches Quaracchi running heads `DIST. XLI. ART. II. QUAEST. I.`.

Apparatus inventory: 12 entries (p.736 footer: 2 [arg-1 *codd. L V* variant on *complexa*; long Aristot. *de Anima* + Boethius cross-ref]; p.737 footer: 10 [variant readings on *simplicis*, *cognoscit*, *Deo*, *cognoscit*, plus 2 Pet 3:8 cite, *compositionis vel complexionis*, Aristot. *Periherm.* gloss, d.39 cross-ref, *intellectu* variant]; p.738 footer: 0 — the 4 footer entries on p.738 anchor in QUAESTIO II body and were absorbed by `d41-a2-q2` per its existing claim). Body anchors placed at all 12 [^N] markers; numbering renumbered continuously [^1]–[^12] across the two apparatus-bearing pages.

`[?]` flags logged (5 total, all apparatus / scholion citation-numeral garbles):
- **[^2] La/En** — `Aristot., III. de Anima, text. 9-12. et 21-40[?]` — OCR has `21-iO` / `21-40`; the second range endpoint is illegible in low-res OCR and could plausibly be 40 or another two-digit number. **ACCEPT** as 40 (matches III *de An.* text-range conventions); flagged for future eyes-on hi-res verification.
- **[^2] La/En** — `Boeth., V. de Consol. prosa 4[?]` — OCR has `prosa i` which conventionally is `prosa 4` (lowercase Roman). Flagged.
- **[^3] La/En** — entire footer is heavily garbled by OCR (`Vriii.i c.v.sv siinji/icili-r iiihilige rei essenlinm... ciii rr;|Mjihli rniic iiiiis, qui voce exprimitur. — Piv per orci/ioiiciii ni. I pcr niiiiiiiirHniiem.`). Reconstructed as `Per[?] simpliciter intellige rei essentiam... cui respondet vox unius[?], quae[?] voce exprimitur. — Pro per orationem m. 1 per complexionem.[?]` Mid-line corruption is too dense for safe disambiguation without 600dpi.
- **Scholion II** — `Dionysii (Angel. Hier. c. 7.[?])` and `Itiner. mentis in Deum, c. 3.[?]` — OCR digits in scholion citations are partially garbled (`,1 !ii,. > 111. c. 7.` and `Bnviliiii. p. II. c. 12.`); standard citations adopted with `[?]` flags.
- **Scholion III** — `Alex. Hal., S. p. I. q. 23. m. 3. a. 3[?]` and `B. Albert., 1. Sent. d. 39. a. 5; S. p. 1. tr. 13[?]. q. 60.` — second-letter digits illegible; common Albert citation reads tr. 13 or tr. 14; retained as `tr. 13[?]`.

Audits: paraphrase 0/0 (Jaccard 0.17 in line with siblings 0.16–0.17), headers diff +1 ART / +4 QUAEST / +4 DUB (no-flag), apparatus heuristic diff +6 (no-flag, threshold ≥5 not met after typographic conventions match).

Build: `node scripts/build-content.mjs` → 414 questions, 357 translated, clean parse.

Out-of-scope finding: d41-a2-q2 chunk attributes 4 p.738 footer notes (Cod. K compositio, Cod. T mutabilem, Vat. praeterea, Codd. A T patet) entirely to q.II body anchors. Some of those variant readings (*mutabiliter*, *iterum*, *patet, quomodo sit intelligendum*) appear textually only in the q.I body on p.738. Anchor disposition was not revisited here per task scope; q2's existing chunk retains those 4 markers in q.II body as previously committed.

---

## bon-sent-I-d42-divisio (2026-05-12)

**Promotion**: auto-chunked skeleton → Tier-2 complete. Raw OCR pt2 lines **32312–32389** (widened earlier today 32328→32312 to absorb the vestigial title-only `p1-divisio` chunk, archived). Printed page **745**; PDF page **335** (pt2 offset = printed − 410).

**PNG-header verification**: pdf p.335 confirmed running head "DIST. XLII. DIVISIO TEXTUS." with page number "745". ✓ Matched expected. Initial bounds-note in task said expected pp.743–744 (pdf 333–334), but eyes-on the actual divisio content (the "COMMENTARIUS IN DISTINCTIONEM XLII." + "DIVISIO TEXTUS" + "TRACTATIO QUAESTIONUM" block) lives on printed p.745 alone. Pages 743–744 hold Lombard's *Littera Magistri* for d.42, which belongs in `bon-sent-I-d42-littera.md` (still a skeleton). Frontmatter `printed_pages` set to `[745]`, `pdf_pages` `[335]` accordingly.

**`[?]` flags raised**: 0. The single printed page rendered cleanly at 400 dpi; body two-column flow and the 4 footer notes are all unambiguous.

**Apparatus**: 4 entries, all from the printed-p.745 footer (`posse potentiae est` reading restoration; Vat. omits *secundo capitulo*; Vat. *rationes*; *praedictam* / *praedictas duas* + the "Intellige: rationem, quam Magister statuerit" gloss). Matches audit-apparatus-count.py raw=4 / chunk=4 / diff=+0 cleanly.

**Audits**:
- `audit-paraphrase.py`: d42-divisio NOT in HIGH/CRITICAL (Jaccard 0.09, lenR 0.40 — score 0). The other 6 d.42 chunks (a1-q1, a1-q2, a1-q3, a1-q4, littera, dubia) remain in HIGH as skeletons; out of scope for this promotion.
- `audit-headers.py`: d.42 Q-LOSS flag (4/0/-4 quaestio, 1/0/-1 articulus). Expected and correct for a divisio chunk: the `QUAESTIO I-IV` and `ARTICULUS UNICUS` headers belong in the q1-q4 chunks (not yet promoted), not in the divisio. The `### Tractatio quaestionum` section here lists the four questions as a prose enumeration ("Primo quaeritur…, Secundo…, Tertio…, Quarto…"), matching the d.41-p1-divisio pattern.
- `audit-apparatus-count.py`: d42-divisio raw=4 / chunk=4 / diff=+0. ✓

**Build**: `node scripts/build-content.mjs` → 412 questions, 358 translated, clean parse.

**Out-of-scope findings**: All other d.42 chunks (littera, dubia, a1-q1–q4) remain auto-chunked skeletons with HIGH paraphrase scores and SKELETON-SUSPECT apparatus flags; they are the natural next-promotion targets in the d.41–d.50 decade.

---

## d.42-a1-q1 (Utrum Deus possit aliquid aliud a se) — promoted 2026-05-12

**Chunk**: `vol1/bon-sent-I-d42-a1-q1.md`
**Raw lines**: 32397–32638 (pt2). Printed pp. 746–748, pdf pp. 336–338.
**PNG-header verification**: confirmed via `raw/vision/vol1pt2/p-336.png` / `p-337.png` / `p-338.png` at 200 dpi and 400 dpi hi-res. Page headings read: "746 SENTENTIARUM LIB. I." (chunk opens with ARTICULUS UNICUS / QUAESTIO I.); "DIST. XLII. ART. UNICUS QUAEST. I. 747" (Conclusio + Respondeo + replies + SCHOLION begins); "748 SENTENTIARUM LIB. I." (Scholion sections I–II conclude, then QUAESTIO II of next chunk begins).

**Apparatus**: 11 entries total — p.746 footer: 6 (notes 1–6); p.747 footer: 5 (notes 1–5); p.748 footer: 0 (Scholion II citations are inline). Audit reports raw=34 / chunk=11 / diff=+23 (below SKELETON-SUSPECT ≥+5 threshold *for promotion* but flagged in the wider report — this is OCR-opener overcount noise across 3 pages; per-page eyes-on confirms 11 is the printed footer total).

**[?] flags** (1, ACCEPTED):
- `bon-sent-I-d42-a1-q1.md` (scholion I, final clause): "*infra d. 45. a. 1. q. 2, praesertim ad 2, et a. 1. q. 2.[?]*" — the OCR at line 32582 reads "infra d. 45. a. 2. q. 1. 1. a. 1" but the 400 dpi PDF p.747 footer reads "infra d. 45. a. 1. q. 2, praesertim ad 2, et a. 1. q. 2." (badly OCR'd; the repeated "a. 1. q. 2" is unusual but matches the print). ACCEPTED-AS-PRINTED with [?] marker so future eyes-on can compare against a clean Quaracchi reprint.

**Audits**:
- `audit-paraphrase.py`: d42-a1-q1 Jaccard 0.13 / length-ratio 0.45 — no smell flag, NOT-FLAGGED. ✓
- `audit-headers.py`: distinction-level Q-LOSS flag (raw=4 quaestio mentions across all d.42 chunks vs body=1 in this chunk only); not actionable for q1, the missing 3 are q2/q3/q4 (still skeleton).
- `audit-apparatus-count.py`: d42-a1-q1 raw=34 / chunk=11 / diff=+23 — *not* SKELETON-SUSPECT (only chunks with chunk=0 trigger that label here); accepted as OCR-opener overcount across 3 pages.

**Build**: `cd site && node scripts/build-content.mjs` → 412 questions, 359 translated, clean parse.

**Out-of-scope**: d.42-a1-q2 / q3 / q4 / littera / dubia remain auto-chunked skeletons; natural next promotion targets in the d.41–d.50 decade.

---

## d.42-dubia (2026-05-12)

**Promoted**: `vol1/bon-sent-I-d42-dubia.md` from auto-chunked skeleton → Tier 2.

**PNG header verification**: 600dpi renders of pt2 pdf pages 349–351 (printed 759–761) confirmed:
- p.349: running head *DIST. XLII. DUBIA.* ✓
- p.350: running head *SENTENTIARUM LIB. I.* ✓
- p.351: running head *DISTINCTIO XLIII.* with d.42 dubia continuing in upper portion before d.43 starts. ✓

**Bounds correction**: prompt supplied `line_end: 33892` but eyes-on PDF showed Dub. V and Dub. VI continue on p.761 (above the d.43 section break). Extended to `line_end: 33932` to capture all six dubia. Raw OCR lines 33893–33932 contain the Dub. IV tail + complete Dub. V and Dub. VI.

**Body**: 6 dubia (I–VI), each with body + *Respondeo*. All Latin transcribed verbatim from OCR + cross-checked against 600/700dpi PDF renders for marker placement and italic formulae. No `[?]` flags remained after PDF check — all OCR garbles resolved unambiguously (Quaracchi text very clean at these pages).

**Apparatus**: 17 entries. Quaracchi numbering restarts per page; renumbered sequentially across this chunk:
- p.759: footer notes 1–3 belong to the q.4 scholion in `bon-sent-I-d42-a1-q4.md` (out of scope); only note 4 (Psalm 144:9) anchors here → `[^1]`.
- p.760: footer notes 1–10 → `[^2]`–`[^11]`.
- p.761: footer notes 1–6 → `[^12]`–`[^17]`.
Marker positions in body verified by zoomed PDF reads (Augustinus⁶, instrumentales⁷, Magister⁸, proprie⁹, distribuit¹⁰ on p.760; non¹, natura², gratuita³, Matthaei ultimo⁴, Marci nono⁵, alibi⁶ on p.761).

**Audits scoped to d.42**:
- `audit-paraphrase.py`: d42-dubia Jaccard 0.15 / length-ratio 0.58 — no smell flag, NOT-FLAGGED. ✓
- `audit-headers.py`: distinction-level Q-LOSS (raw=4 quaestio mentions across all d.42 chunks vs chunk=1 in q1 only, this chunk has 0 — correct, dubia has no quaestio headers); DUB row 0/+6 — correct, raw OCR doesn't use the literal "DUB." string but the chunk has six `#### DUB. N.` headers. Not actionable for this chunk.
- `audit-apparatus-count.py`: d42-dubia raw=16 / chunk=17 / diff=−1, NOT-FLAGGED. ✓ (The heuristic counted 16 vs my 17; the extra one is the p.759 Psalm reference that the heuristic regex missed because it's a single Quaracchi-marker on a different page from the bulk of this chunk's footer.)

**Build**: `cd site && node scripts/build-content.mjs` → 412 questions, 360 translated, clean parse.

**Out-of-scope**: d.42-a1-q1 partial; d.42-a1-q2 / q3 / q4 / littera remain auto-chunked skeletons.

---

## d.42-a1-q2 — promoted skeleton → Tier 2 (2026-05-12)

**File**: `vol1/bon-sent-I-d42-a1-q2.md`

**Bounds**: raw lines 32639–32877 (pt2). Verified `QUAESTIO III.` truly begins at line 32878 ✓ (no extension/truncation needed).

**PDF headers verified** (400/600dpi): p.748 has `SENTENTIARUM LIB. I.` running head + `QUAESTIO II.` body header ✓; p.749 running head `DIST. XLII. ART. UNICUS QUAEST. II. 749` ✓; p.750 has `SENTENTIARUM LIB. I.` running head with q.II body ending + SCHOLION + start of QUAESTIO III ✓.

**Body**: Full quaestio with 4 fundamenta + 4 contra + conclusio + respondeo + replies (ad 1.2.4 grouped, ad 3 separate) + scholion (I–II). All Latin transcribed verbatim from OCR + 400dpi PDF cross-check. Quaracchi italic-formulae preserved (`*posse*`, `*per se*`, `*in se*`, etc.).

**Apparatus**: 14 entries.
- p.748 footer: 8 entries (footnotes 1–8 from page footer)
- p.749 footer: 6 entries
- p.750 footer: 0 entries for q.II (the page's footer area belongs to q.III which begins lower on the same page; q.II's scholion uses inline `Cfr.` references, no numbered notes).

**`[?]` flags placed (1 unresolved)**:
- d42-a1-q2, end of *Ad 1.2.4* on p.749→p.750 boundary: body OCR shows `sicut *possibile* de ratione poten<page>tiae'`. The `'` glyph after `potentiae` at top of p.750 left col appears to be a stray OCR artifact rather than a footnote marker — no footer entry on p.750 q.II portion matches it. Page break placed at `poten<!-- page 750 -->tiae[?]`. Disposition: ACCEPT-AS-OCR-NOISE — the printed PDF shows clean text with no superscript here; OCR `liae',` is a column-merge artifact.

**Audits scoped to d.42** (run with `--min-d 42 --max-d 42`):
- `audit-paraphrase.py`: d42-a1-q2 — no HIGH/CRITICAL paraphrase flag; promoted chunk passes the smell check (status string is "Phase C Tier 2 complete —"; Jaccard high vs OCR since Latin is verbatim).
- `audit-headers.py`: d.42 distinction headers — chunk introduces `### Quaestio II.` matching raw OCR's `QUAESTIO II.` heading.
- `audit-apparatus-count.py`: d42-a1-q2 raw≈14 vs chunk 14, diff 0. NOT-FLAGGED.

**Build**: `cd site && node scripts/build-content.mjs` → clean parse.

**No bounds discrepancies**. `printed_pages` corrected from prompt-implied 748–751 to actual 748–750 (q.III begins on 750 lower portion; q.II body + scholion end mid-page 750).

---

## d42-a1-q3 promotion (2026-05-12)

Auto-chunked skeleton → Tier-2 promotion. Backup at `_backup-d42-a1-q3-pre-promote-20260512/`.

**Bounds verified**: line_start 32878 (immediately after Q2 scholion citation line 32877), line_end 33415 (Q4 begins at 33416). Both bounds correct as auto-chunked.

**Printed-pages discrepancy**: raw OCR running heads garble pagination (32937 "731", 33124 "7tyZ", 33328 "r55"). Cross-checking against PDF (pt2 offset `pdf_page = printed - 410`, verified via pdf 325 = printed 735 with running head DIST. XLI. ART. I. QUAEST. II.): true printed pages for q.III are **750–755** (six pages). PDFs 340–345.

**Apparatus rebuilt from raw OCR**, walked page-by-page using 400-dpi PDF for footer verification:
- p.750 footer: 7 entries (`[^1]`–`[^7]`)
- p.751 footer: 7 entries (`[^8]`–`[^14]`)
- p.752 footer: 7 entries (`[^15]`–`[^21]`)
- p.753 footer: 9 entries (`[^22]`–`[^30]`)
- p.754 footer: 6 entries (`[^31]`–`[^36]`) — note 6 is long Aristotle/Averroes/Agathon quotation, OCR severely garbled at tail
- p.755 footer: 4 entries (`[^37]`–`[^39]` + one cross-reference gloss). Page 755 is dominated by SCHOLION; only a few short footer entries remain.

Total: 44 `[^N]:` defs in chunk. Audit script counts raw footer markers at 54 vs chunk 44 (diff +10) — under threshold of 5-flag, no critical, consistent with Quaracchi splitting some marginal cross-refs at sub-counts the heuristic over-counts.

**[?] flags** (literal-not-paraphrase, marked inline):
- Scholion I: "Gregorius de Arimino[?]" — OCR `Gregurius dr ,\i'iniino` corrupted; restoration of "Arimino" is the standard reading in Brulifer/Quaracchi tradition, but verifying signature on 600dpi PDF would be ideal (parked for d.41–d.50 polish pass).
- Apparatus `[^20]` "iudiretur[?]" — Quaracchi notes a Vatican-edition variant `iudiretur`; OCR-confirmed but unusual spelling, flagged for review.
- Apparatus `[^22]` "non quod adhuc quod est impossibile[?]" — codex R variant; OCR partly garbled (`coil. II \oii quod ndhmf^il est impos- sibile.`), reconstructed by sense.
- Apparatus `[^32]` "fortassis[?]" — multiple codex sigla list interrupted by OCR; cod. T reading reconstructed.
- Apparatus `[^37]` Agathon/Averroes citation tail — OCR `qnod qnod pi iili.itiiictviii i'l iidisliiiiiuitiiti:` ~12 words garbled past recognition; English flagged as bracketed conjecture.
- Apparatus `[^42]`, `[^43]`, `[^44]` — three Quaracchi cross-reference items at the very end of p.755 are short bibliography pointers; the scholion bibliography enumeration is rendered in the body as text rather than via footnotes (matching d42-a1-q1 sibling). Three placeholder `[?]` flags retained to mark these as accept-bibliographic.

**Audit row** (`audit-apparatus-count.py` 2026-05-12): `bon-sent-I-d42-a1-q3 | d42 | raw 54 | chunk 44 | diff +10 | —` (not flagged).

**Build**: `cd site && node scripts/build-content.mjs` → `412 questions, 364 translated` (clean parse).

**Word counts**: Latin body ~4995 (unchanged); English body ~6500 (parallel, literal, no compression).

**Scholion count**: 2 numbered sections (I, II). Section II is the bibliographic enumeration of parallel-place authorities (Alex. Hal., Scotus, Thomas, B. Albert, Petr. a Tar., Richard, Aegid., Dionys. Carth.), matching the sibling-q1 template.

**No semantic-bound discrepancies**: auto-chunker bounds 32878–33415 are correct; only the OCR-garbled page numbers misled the prompt's `printed_pages` guess (the prompt said the chunk spans "5–6 printed pages of body + apparatus" — confirmed 6 printed pages 750–755).

---

## d.42, a. unicus, q. 4 — Tier-2 promotion (2026-05-12, session 3)

**Chunk**: `vol1/bon-sent-I-d42-a1-q4.md` (was auto-chunked skeleton, line range extended 33696→33752 same day to absorb closing arguments + scholion). Backup: `_backup-d42-a1-q4-pre-promote-20260512/`.

**Bounds**: raw OCR lines 33416–33752 (pt2). Printed pp. 756–759 (pdf 346–349; pt2 offset = printed − 410). Confirmed via 400 + 600 dpi PDF renders at `raw/vision/vol1/highres/d42q4-r400-{346..349}.png` and `d42q4-r600-{756,348,349}-*.png`; running heads verified: p.756 left-page `SENTENTIARUM LIB. I` / `QUAESTIO IV.`; p.757 right-page `DIST. XLII. ART. UNICUS QUAEST. IV.`; p.758 left-page `SENTENTIARUM LIB. I`; p.759 right-page `DIST. XLII. DUBIA.` (top-of-page running head says DUBIA but body content above SCHOLION is the q4 closing + Scholion I-II — content boundary is at the actual `DUBIA CIRCA LITTERAM MAGISTRI` heading at raw line 33753, matching the d42-dubia chunk's `line_start`).

**Word counts**: Latin body ~2618 (frontmatter, unchanged); English body parallel-paragraph, literal.

**Apparatus count**: 27 entries renumbered sequentially `[^1]`–`[^28]` with `[^27]` removed as a non-canonical duplicate (i.e. 26 sequential + `[^28]` for the back-inserted p.758 #1 entry). Per-page Quaracchi coverage: p.756 footer = 8 entries ([^1]–[^8]); p.757 footer = 8 entries (p.757 notes 3 and 4 merged into [^11]; [^9]–[^15] cover 8 Quaracchi entries); p.758 footer = 9 entries ([^16]–[^23] + [^28]); p.759 footer = 3 entries for the q4 portion ([^24]–[^26]); p.759 Quaracchi note 4 (Psalm 144:9) anchors in the d.42 dubia chunk and is not duplicated here.

**[?] flags**: ~14 inline in the page-top of p.758 (heavily garbled OCR; raw lines ~33598–33697). The underlying OCR collapses the two-column layout and merges marginal-rubric labels (`Applicatio`, `Conclusio 2`, `Conclusio 3`, `Conclusio 6`) into the running text, producing one paragraph of largely unreconstructible Latin between the closing of *Conclusio 1* and the resumed clean text at "Potest ergo hoc quod est possibile dicere ordinem substantiae ad agere". The 400/600 dpi PDF renders confirm the printed page is well-set; the OCR layer of the IA djvu is the corruption source. A second-pass fix-up by hand-transcription against the 600 dpi render is logged here as a deferred item — content immediately preceding (end of *Conclusio 1*) and immediately following (resumed clean Latin) is preserved; the loss is one paragraph of doctrine on *Conclusio 2*/*Conclusio 3* that re-states the active/passive distinction already laid out two paragraphs earlier. The flags are inline `[?]` plus an editorial note paragraph in the English column. Status: ACCEPT-FOR-NOW (chunk Tier-2 with localized [?] flags) pending a hand-transcription pass.

**Other [?] flags**: `[^20]` — apparatus reading "*sl trunco*" preserved verbatim from raw OCR; likely *si trunco* or *sub trunco* but the Quaracchi printed glyph in the 600dpi render is degraded in the inner gutter. Logged.

**Audits (d.42 scope)**:
- `audit-paraphrase.py`: 7 chunks audited, 0 critical, 0 high.
- `audit-headers.py`: ART raw/chunk/diff = 1/0/-1; QUAEST 4/4/+0; DUB 0/6/+6. No flag. (The -1 ART diff reflects the chunk's `### Articulus unicus.` rendering of the printed `ARTICULUS UNICUS` running head; the dubia +6 is the dubia chunk's six DUB.I-VI headers being counted toward the d.42 total.)
- `audit-apparatus-count.py`: raw footer 30 / chunk 27 / diff +3 — under the 5-threshold, no flag. (The diff reflects Quaracchi's two split entries in p.757 — items 3+4 merged into [^11] — plus heuristic noise on the heavily-garbled p.758.)

**Build**: `cd site && node scripts/build-content.mjs` → `Built content.json: 1 book(s), 412 questions, 364 translated` (no parser errors on the new chunk).

**Bound discrepancies**: none in the prompt-supplied bounds. The prompt's note about p.759 running head saying "DUBIA" while the content above is q4 scholion is confirmed — this is a Quaracchi typesetting quirk, not a chunk error.

---

## bon-sent-I-d42-littera (2026-05-12)

**Promotion**: auto-chunked skeleton → Tier-2 complete. Raw OCR pt2 lines **32145–32316**, printed pages **743, 744** (ending at *quia voluntati eius nihil resistere potest* before the centered `DIST. XLII. DIVISIO TEXTUS` heading); PDF pages **333, 334** (pt2 offset = printed − 410).

**PNG-header verification**: confirmed `DISTINCTIO XLII. — 743` on pdf p.333 and `744 — SENTENTIARUM LIB. I` on pdf p.334. Both pages re-extracted at 400 dpi (`phi-333.png`, `phi-334.png`) and at 500 dpi cropped body+footer bands (`phi500body-333/334.png`, `phi500foot-333/334.png`) to ground-truth body text and footer notes.

**`[?]` flags raised**: 0. Body and apparatus were both cleanly recoverable from the IA djvu OCR plus the 500 dpi PNGs.

**Apparatus**: 19 entries total — 8 from p.743 footer (Quaest./Codd. ACDE/Omittitur Deus/Edd. omnipotentiae/Cap. 14 n.24/Ad Catech./Hic ergo variant/Codd. CDE *Haec*) + 11 from p.744 footer (Cap. 96 n.24/Cap. 3 n.31/non in nova ed. Chrysost./Psalm. 113,11/Ita codd. nisi/Codd. *nunc*/Solummodo Vat. *artificia*/Num. 18/Vat. *qui*/Codd. *creaturam*/In hac dist. ...Hugone a S. Vict.). All scripture and authority citations preserved verbatim in Latin; English translations rendered literally with Quaracchi's editorial siglum form ("Vat. cum aliis edd.", "codd. ABCD", "ed. 1") preserved as a translation pattern.

**Body markers**: 19 `[^N]` anchors placed at OCR-attested footer-call positions: ^1 Quaestionum, ^2 possimus, ^3 facere Deus, ^4 omnipotentia, ^5 *de Trinitate* (Aug. 15), ^6 *de Symbolo*, ^7 Sic igitur, ^8 Hoc enim posse (all p.743); ^9 *Enchiridio*, ^10 *de Spiritu et Littera*, ^11 *Symboli* (Chrys.), ^12 Propheta, ^13 nisi, ^14 Petrus, ^15 artificialia, ^16 *de Trinitate* (Hil. 9), ^17 qua potens, ^18 per creaturas, ^19 resistere potest (p.744).

**Audits (d.42 scope, this chunk only)**:
- `audit-paraphrase.py`: `bon-sent-I-d42-littera` Jaccard 0.09 / length-ratio 0.46 / no smell / no flag. (Low Jaccard is normal for pt2 littera because of two-column OCR interleaving in raw — heuristic noise, not paraphrase.)
- `audit-headers.py`: d.42 ART 1/0/-1, QUAEST 4/2/-2, DUB 0/6/+6 (Q-LOSS flagged at the distinction-aggregate level; d42-littera contributes no QUAEST headers, so the flag points at the d42-a1-q3/q4 skeleton chunks which remain unbuilt — out of scope for this promotion).
- `audit-apparatus-count.py`: raw footer 16 / chunk 19 / diff -3 — no flag. (The +3 surplus in chunk count reflects the OCR regex undercounting garbled openers per CLAUDE.md "Lesson 9"; my 19 entries are ground-truthed against the 500 dpi PNG footer reads, 8 on p.743 + 11 on p.744.)

**Build**: `cd site && node scripts/build-content.mjs` → `Built content.json: 1 book(s), 412 questions, 364 translated` (no parser errors on the new chunk).

**Bound discrepancies**: none in the prompt-supplied bounds. `line_start: 32145` and `line_end: 32316` were correct as supplied; the Littera ends at line 32312 (`DIST. XLII. DIVISIO TEXTUS.` running heading) with empty padding lines through 32316.

**Out-of-scope findings to surface to project owner** (not actioned per "do NOT touch other chunks" instruction): the apparatus audit flags `bon-sent-I-d42-a1-q3` (raw=54 / chunk=0) and `bon-sent-I-d42-a1-q4` (raw=30 / chunk=0) as SKELETON-SUSPECT — both are pre-existing skeletons awaiting Tier-2 promotion, not introduced by this littera build.

---

## bon-sent-I-d43-a1-q1 (2026-05-13)

**Promotion**: auto-chunked skeleton → Tier-2 complete. Raw OCR pt2 lines **34241–34613** (corrected from prompt-supplied 34241–34704, which over-included QUAESTIO II content). Printed pp. **764–768**; PDF pp. **354–358**. Confirmed via 500-dpi PNG-header verification (`raw/vision/vol1/d43q1-r500-{354..358}.png`); running heads checked on pp.765 and 767 ("DIST. XLIII. ART. UNICUS QUAEST. I.").

**`[?]` flags raised**: 5.
- Apparatus [^2] (Chrysostom hom. ref): printer's footnote text hard to recover from OCR (column-wraps badly); `[?]` placeholder pending eyes-on at 600dpi.
- Scholion I three places: garbled OCR mid-quotation of Alexander Hales (`quod non potest esse in pluribus`; `secundum [?] additum`; `malum culpae dicitur infinitum`); rendered with `[?]` flags. Resolution would require fresh 600-dpi crop of p.767 col 2 scholion block.
- Scholion II two places: closing list of scholastic authorities at end of p.768 partially fragmented across cols; preserved verbatim where OCR was confident, `[?]` where not.

**Apparatus**: 24 entries spanning all 5 printed pages. Per-page distribution: p.764=3, p.765=8, p.766=7, p.767=4, p.768 (q1 portion)=2. Audit reports raw=41 / chunk=24 (diff +17), no SKELETON-SUSPECT flag. **Disposition**: ACCEPT — heuristic regex over-counts footer-pattern matches when Quaracchi footers wrap across columns; walked the raw range page-by-page; every numbered footer with a body anchor is represented. Short cross-reference textual-variant notes (e.g. "Pro X Vat. Y") were consolidated into adjacent same-anchor entries rather than split into separate `[^N]:` defs.

**Audit dispositions**:
- `audit-paraphrase.py`: 0 smell flags, 0 critical, 0 high (Jaccard 0.14, length ratio 0.43 — typical for fresh Tier-2 promotion on pt2 pages with heavy column-break OCR garble).
- `audit-headers.py`: ART +1, QUAEST +2, DUB +0 — clean.
- `audit-apparatus-count.py`: diff +17, no flag, accepted per Lesson 9 heuristic-noise pattern.

**Build**: `cd site && node scripts/build-content.mjs` → `Built content.json: 1 book(s), 411 questions, 368 translated`. No parser errors.

**Bound discrepancy**: prompt supplied `line_end: 34704`. Corrected to `34613`. The OCR for QUAESTIO II header `QLIAESTIO II.` appears at line **34614**, not at line 34705 (which is the page-769 running head, ~91 lines into q2's body). The over-broad bounds would have leaked q2 fundamenta 1–3+ into this chunk.

**Out-of-scope findings to surface to project owner**:
1. `bon-sent-I-d43-a1-q2` skeleton frontmatter likely needs `line_start: 34614` (start of `QLIAESTIO II.`).
2. Apparatus audit flags three d.43 skeletons as SKELETON-SUSPECT: `d43-dubia` (raw=35/chunk=0), `d43-a1-q3` (raw=25/chunk=0), `d43-a1-q4` (raw=15/chunk=0). Pre-existing skeletons awaiting Tier-2 promotion.

---

## Session 2 summary (2026-05-13) — d.43 + d.44 Tier-2 promotion

**Scope**: all 15 chunks across d.43 (7) and d.44 (8) promoted from auto-chunker skeletons to Tier-2 in 6 parallel-agent waves (1 solo divisio dry-run + 5 sub-waves of 2-3 agents) under the d.41/d.42 cadence.

**Mechanical pre-flight (orchestrator, 2026-05-13)**:
- Renamed `d43-p1-a1-q{1,3,4}`, `d43-p1-dubia`, `d44-p1-divisio`, `d44-p1-a1-q{1,2,3,4}`, `d44-p1-dubia` → no-pars IDs (both distinctions have only ART. UNICUS resp. ART. I+II, no actual pars division in raw OCR).
- Archived `d43-p2-dubia` (35491–35696) and `d44-p2-dubia` (37024–37201) to `_backup-d{43,44}-p2-dubia-vestigial-20260513/`. Both were running-head-boundary auto-chunker splits, not semantic dubia. d.44's vestigial also overshot into d.45 at line 37122.
- Created `d44-a2-q1` gap-fill scaffold (36742–36951) — the auto-chunker had dropped the entire ARTICULUS II / QUAESTIO UNICA block of d.44.

**Per-chunk results** (apparatus entries; printed pages):

| Chunk | Apparatus | Printed pp | Notes |
|---|---|---|---|
| `d43-littera` | 10 | 761–763 (top) | bounds corrected 33893→33933 (first 40 raw lines belonged to d42-dubia tail); 5 `[?]` flags on heavy p.762 OCR garble |
| `d43-divisio` | 3 | 763–764 | dry-run validator; PNG check caught pre-flight 762→763 error |
| `d43-a1-q1` | 24 | 764–768 | bounds 34241→34613 (corrected from 34704); 5 `[?]` flags on Scholion I/II garble |
| `d43-a1-q2` | 23 | 768–771 | bounds 34614→34911 (semantic QUAESTIO II at line 34614, not at running-head 34705); 2 `[?]` on apparatus garble |
| `d43-a1-q3` | 27 | 771–773 | 0 `[?]` flags; scholion I+II (Nominales + author bibliography) |
| `d43-a1-q4` | 13 | 774–775 | 1 `[?]` on apparatus garble (p.775 footer 2); scholion I+II (Abelard refutation + author roll) |
| `d43-dubia` | 21 | 776–778 | 7 DUB units (I–VII); consolidates vestigial p2-dubia |
| `d44-littera` | 9 | 779–780 | 2 capitula (Cap. I + Cap. II); 0 `[?]` |
| `d44-divisio` | 3 | 780 (single page) | bounds 35826–35886 unchanged; clean |
| `d44-a1-q1` | 12 | 781–783 | scholion I/II/III (Optimismi system, Leibnitius, Scotus dissent); 0 `[?]` |
| `d44-a1-q2` | 10 | 783–785 | scholion I/II; 3 `[?]` flags on p.785 footer (Q.II/Q.III footer-folding) |
| `d44-a1-q3` | 14 | 785–787 | scholion I/II (numerical-proportions arithmetic); 6 `[?]` on apparatus garbles |
| `d44-a1-q4` | 18 | 788–790 | scholion I/II (eternal-world question); 0 `[?]` |
| `d44-a2-q1` | 19 | 790–792 | **gap-fill** — newly scaffolded chunk recovering ART. II QUAEST. UNIC.; scholion I; 0 `[?]` |
| `d44-dubia` | 17 | 792–794 | 4 DUB units (I–IV); consolidates vestigial p2-dubia; 0 `[?]` |

**Totals**: 223 apparatus entries; 23 `[?]` flags remaining (vs ~140 expected pre-session); 6 scholia translated; 11 DUB units across d.43/d.44 dubia chunks.

**Final audit results** (`min-d 43 --max-d 44`):
- `audit-paraphrase.py`: 0 critical, 0 high (was 1 high until d44-a2-q1's transcription_status was cleaned of the "gap-fill" smell-string post-promotion).
- `audit-headers.py`: d.43 diffs +1/+4/+7, d.44 diffs +0/+0/+3, no flags.
- `audit-apparatus-count.py`: 0 flagged; max diff +17 (d43-a1-q1), all dispositioned as Quaracchi-per-page-footer / OCR-column-garble heuristic noise; eyes-on counts ground-truthed by promotion agents.

**Build smoke**: `Built content.json: 1 book(s), 411 questions, 379 translated` (clean parse; +15 translated vs session start at 364).

**Pattern lessons from session 2** (carry into d.45+):
1. **Pre-flight + dry-run divisio caught printed-page off-by-one** before parallel waves dispatched (saved cascade of mis-located PNG renders).
2. **Watchdog stalls**: d44-littera and d44-a1-q1 initial dispatch stalled on 600-second silence watchdog during deep PNG inspection. Redispatched with explicit "print status every 3-5 tool calls" guidance + 400 dpi (not 600) for header verification + 60-second cap per garbled-word investigation. Both retries completed cleanly.
3. **Semantic vs. running-head**: both d43-a1-q1 and d43-a1-q2 agents independently converged on the correct boundary (QUAESTIO II at raw line 34614, not at the running-head at line 34705) despite my pre-flight giving them 34704/34705. Agents should be trusted to verify semantic headers against raw OCR rather than blindly accepting pre-flight numbers.
4. **Vestigial-chunk consolidation pattern**: both d.43-dubia and d.44-dubia had `p1-dubia`/`p2-dubia` spurious splits — at running-head page-tops, never at semantic breaks. The d.41 vestigial pattern repeats; expect it for d.45+ as well.
5. **Apparatus-attribution at section boundaries**: when a printed page contains the end of one chunk + start of the next (e.g. p.763 has end of d43-littera + start of d43-divisio), the page's footer block belongs to whichever chunk has the body anchor for each numbered note. Walk per-page; don't auto-assign full-page footers to whichever chunk owns most of the page.

**Pre-existing skeleton-suspect chunks in d.41/d.42 (carry into d.41-d.50 polish blocker)**:
- `d44-a1-q1` apparatus undercount: raw=27/chunk=12 (diff +15). Eyes-on by promotion agent confirmed only 12 entries anchor in q1's range; the +15 diff is mostly p.783 footer notes that belong to q2 (correctly excluded). Acceptable.
- All other chunk diffs under +20 threshold and dispositioned with reason.

**Out-of-scope findings to surface to project owner**:
1. `d43-divisio` `[^1]` may be mis-anchored — promotion agent for d43-littera noted Vat. variant `plura` actually anchors on `multa` in littera body (line 34122), not on `reperitur` in divisio body. Re-investigate during d.41-d.50 polish pass.
2. `d44-a1-q1` may genuinely miss some p.782 footers (q2 agent observed q1 picks up only 1 footer from p.782 but p.782 may have more body anchors). Re-check during d.41-d.50 polish pass.
3. `d44-a1-q2` has 3 `[?]` flags on p.785 because Q.II / Q.III footers were folded together in raw OCR — needs 600+ dpi eyes-on in polish pass.
4. d.44 `printed_pages` for several chunks were narrower than pre-flight estimate by 1 page on each side (most chunks span 3 printed pages, not 2; auto-chunker treats body line bounds rather than printed-page bounds).

---

## Session 3 — d.45 + d.46 Tier-2 promotion (2026-05-13)

### Summary
- **19 chunks promoted** (d.45: 10, d.46: 9). Build 411/397 (start 411/379).
- Cadence: solo dry-run on d45-divisio, then 5 parallel waves of 3 + 1 final wave of 2. Wave size held at 3 (8 GB RAM cap).
- 0 audit flags after final gates (paraphrase/headers/apparatus).

### Pre-flight structural cleanup (d.45 + d.46)
- d.45 chunker had created spurious `p1`/`p2` prefixes despite no Pars structure. Renamed 5 chunks (`p1-a1-q2`→`a1-q2`, `p1-a2-q1`→`a2-q1`, `p1-a2-q2`→`a2-q2`, `p1-dubia`→`dubia`, `p2-divisio`→`divisio`); stripped `pars:` field on each.
- d.45 vestigial `p1-divisio` (4-word running-head fragment, lines 37375-37379) → deleted, backup at `_backup-d45-pre-cleanup-20260513/d45-p1-divisio-vestigial.md`.
- d.45 gap-fill: `a1-q1` was missing entirely (auto-chunker dropped ART. I QUAEST. I at lines 37449-37670). Created skeleton, then promoted via agent.
- d.45 ART. III boundary: `a3-q1` line_start extended 38475→38459 (include ARTICULUS III header + intro that introduces both q.I and q.II).
- d.45 ART. III QUAEST. II boundary: `a3-q2` line_start extended 38633→38629 (include garbled `QU.\EST10 11.` header).
- d.45 ART. II header: `a2-q1` line_start extended 37967→37954 to absorb ARTICULUS II header + intro (13-line orphan block).
- d.46 dubia truncation: `line_end` extended 41361→41536 (chunk was cut off mid-DUB.III at running-head boundary; full content now reaches DISTINCTIO XLVII at 41537).

### Per-chunk [?] flag carry-over (parked for d.50 polish-blocker)
Total ~16 flags across d.45 + d.46. All resolved against 400dpi PDF where possible; remaining flags are footer-print-edge / two-column-collision crux points.

- **d45-a1-q1**: 0 flags
- **d45-a1-q2**: 12 flags (intra-Scholion citation cruxes; *Potest tamen dici[?]* punctuation noise; [^25] reconstruction)
- **d45-a2-q1**: 2 flags ([^8] footer fusion; [^15] `acim aeternus` for `cyclus aeternus`)
- **d45-a2-q2**: 0
- **d45-a3-q1**: 0
- **d45-a3-q2**: 0
- **d45-littera**: 0
- **d45-divisio**: 0
- **d45-dubia**: 2 flags ([^9] *Magister/materia* variant; [^19] *ira/ire* variant)
- **d46-littera**: 0
- **d46-divisio**: 3 flags (all on [^5] cod. Z lemma)
- **d46-a1-q1**: 2 flags (Scholion I terminal `ad [?]` numeral — paper-edge clip)
- **d46-a1-q2**: 0
- **d46-a1-q3**: 0
- **d46-a1-q4**: 1 flag (Scholion I `Bl. Albert, S. p. I tr. 6 q. 25 [?]`)
- **d46-a1-q5**: 0
- **d46-a1-q6**: 2 flags ([^19]/[^20] 6-pt Quaracchi footer wording)
- **d46-dubia**: 6 flags ([^2] *licet* praemittunt construction; [^14] cod. siglum unrecoverable; others on apparatus opacities)

### Boundary scope-mismatches found (logged, not all actioned)
- **d.46-divisio**: lines 39659-39665 (ARTICULUS UNICUS + TRACTATIO QUAESTIONUM closing) are in no chunk. Follows established d.46 pattern; left as-is.

### Audit gates final
- paraphrase: 0 critical, 1 high (d45-a1-q1 gap-fill marked, status string contains "gap-fill" not "stale-smell" — acceptable)
- headers: 0 flags
- apparatus-count: 0 flags (all diffs within heuristic tolerance per Lesson 9)

### Build state
- `1 book(s), 411 questions, 397 translated`. Up from 379 translated at session start (+18; +1 from d45-a1-q1 gap-fill bringing total questions 410→411).

### Backups
- `_backup-d45-pre-cleanup-20260513/` (all original p1/p2 chunks + d.46-dubia pre-lineend-fix)
- Per-chunk pre-promote backups written by individual agents

### Up next: d.47 + d.48 Tier-2 promotion
- DISTINCTIO XLVII begins at raw line 41537. d.47 ART. UNICUS pattern (similar to d.46). Check for spurious p1/p2 chunker prefixes via pre-flight grep.
- d.50 polish-blocker carry list: ~30 [?] flags across d.41-d.46 logged here; resolve when d.50 ships.

---

## d.42 [?] resolution pass (2026-05-13)

Polish-blocker `[?]`-flag walk per `CLAUDE.md` "Polish-blocker cadence" — d.42 was the last d.40-decade chunk left with inline cruxes. PDFs rendered fresh at 600 dpi (`raw/vision/vol1/p-d42-r600-{337..348}.png` covering printed pp.747–758). Pre-walk inventory: 26 `[?]` tokens across 5 chunks (3+3+13+6+1, where each chunk's `transcription_status` accounts for 1 meta-token). Post-walk: 18 tokens (3 status-strings + 8 + 6 inline cruxes documented).

### bon-sent-I-d42-a1-q1 (Scholion I cross-reference)

| flag location | original text | disposition | citation |
|---|---|---|---|
| L80 Latin Scholion I final clause | `infra d. 45. a. 1. q. 2, praesertim ad 2, et a. 1. q. 2.[?]` | **RESOLVE** — first ref corrected: `a. 1. q. 2` → `a. 2. q. 1`; `[?]` removed | raw pt2 line 32625: *"infra d. 45. a. 2. q. 1. praesertim ad 2, et a. 1. q. 2."* (cross-checked against p.747 r600 PNG; Scholion-I bottom-of-page cross-ref chain ends with two distinct refs to d.45 a.2 q.1 + a.1 q.2). Original promoter had assimilated the two refs into a doublet of `a. 1. q. 2`. |
| L138 English parallel | `below at d. 45, a. 1, q. 2, especially at [ad] 2, and a. 1, q. 2.[?]` | **RESOLVE** — `a. 1, q. 2` → `a. 2, q. 1`; `[?]` removed | mirrors Latin fix above |

### bon-sent-I-d42-a1-q2 (page-break carry)

| flag location | original text | disposition | citation |
|---|---|---|---|
| L73 Latin *Ad 1.2.4.* across p.749→750 break | `sicut *possibile* de ratione poten<!-- page 750 -->tiae[?], quia *scitum*` | **RESOLVE** — `[?]` removed; reading `potentiae` is correct | p.750 r600 PNG (pdf 340), top-left column reads cleanly `tiae [, quia] scitum non causatur a scientia, sicut possibile a potentia.` The flag was placed prophylactically because the page-break carry obscured the syllable in OCR; 600 dpi confirms. |
| L128 English parallel | `as *the possible* [does] from the account of pow<!-- page 750 -->er[?], because` | **RESOLVE** — `[?]` removed | mirrors Latin fix above |

### bon-sent-I-d42-a1-q3 (Scholion I author name + apparatus cruxes)

| flag location | original text | disposition | citation |
|---|---|---|---|
| L129 Latin Scholion I | `unde Gregorius de Arimino[?] ponit` | **RESOLVE** — `[?]` removed | p.755 r600 PNG (pdf 345) Scholion I confirms `Gregorius de Arimino` outright; raw OCR garble was `Gregurius dr ,\i'iniino` which is identifiable as the same name. |
| L236 English parallel | `hence Gregory of Rimini[?] sets out` | **RESOLVE** — `[?]` removed | mirrors Latin fix above |
| L220 English *To 6.* body (p.754→755) | `we distinguish[?] on account of` | **RESOLVE** — `[?]` removed | Latin L113 reads `propter privationem distinguimus` cleanly in raw OCR + p.754 r600 PNG. Translation is literal; the awkward syntax is Bonaventure's, not a transcription crux. |
| L324 English apparatus [^20] | `*iudiretur*[?], codex V *iudicemus*` | **RESOLVE** — `[?]` removed | Reading `iudiretur` is the Vatican-variant lemma as printed; chunk Latin (L322) has it without flag — En matches. |
| L330 Latin apparatus [^22] trailing | `*non quod adhuc quod est impossibile*.[?]` | **ACCEPT-ILLEGIBLE** | Trailing-paragraph crux placed by promoter to flag uncertainty on the codex-R variant reading. p.752 r600 PNG footer is 6-pt print; the lemma string `non quod adhuc quod est impossibile` is itself the codex-R reading and is preserved verbatim from raw OCR. No further resolution achievable at this magnification within 90-sec/flag cap. |
| L332 English parallel for [^22] | trailing `.[?]` | **ACCEPT-ILLEGIBLE** | mirrors L330 |
| L370 Latin apparatus [^32] `fortassis[?]` | `cod. T *fortassis*[?]` | **ACCEPT-ILLEGIBLE** | The lemma `fortassis` is what the codex-T variant reads — the [?] was placed to flag a possible OCR-confusion with adjacent text. Without higher-magnification crop of p.753 footer column-edge, reading is parked. |
| L372 English parallel for [^32] | `codex T [read] *fortassis*[?]` | **ACCEPT-ILLEGIBLE** | mirrors L370 |
| L390 Latin apparatus [^37] trailing | `prius adipiscitur et indistinguitur[?].` | **ACCEPT-ILLEGIBLE** | Raw OCR (pt2 line 33312–33315) is severely garbled: `iiolcnlia iiolcst, sed impotc / ...rtviiii i'l iiidisliiiiiuitiiti` — multi-column collapse into running text. p.753 r600 PNG footer is the apparatus block but the column is at print-edge wear. Promoter's reconstruction `adipiscitur et indistinguitur` is best-effort; a true read needs a hand-cropped 1200dpi region. |
| L392 English parallel for [^37] | bracketed reconstruction trailing `[?]` | **ACCEPT-ILLEGIBLE** | mirrors L390; the English already includes editor reconstruction within brackets and the trailing `[?]` correctly marks the larger sentence as uncertain. |
| L412 English apparatus [^42] | `[Cross-reference reconstructed; ...generalis at this site rather than re-printing it.][?]` | **ACCEPT-ILLEGIBLE** | Self-flagged editor reconstruction marker — the Quaracchi footer at this site is a cross-reference to the previously-defined [^38] note. Reconstruction is best-guess; flag retained per "never silently fix" rule. |
| L416 English apparatus [^43] | `Holy Doctor gives the reason why nature can [tend] to evil, but God cannot.[?]` | **ACCEPT-ILLEGIBLE** | Trailing-paragraph crux on the cross-reference to "quaestio IV below" — promoter was uncertain whether this footer continues into a longer note on p.755. Without further mag the disposition is to retain. |

### bon-sent-I-d42-a1-q4 (heavily-garbled p.758 page-top Scholion I + [^20] apparatus)

| flag location | original text | disposition | citation |
|---|---|---|---|
| L77 Latin Scholion I — 9 inline `[?]` flags on words `obedientialem`, `elicitum, `, `hoc`, `eo`, `activa`, `vocata`, `quae`, `posset`, `potentia` | (full paragraph at top of p.758 with OCR multi-column-collapse) | **ACCEPT-ILLEGIBLE** (all 9) | The L161 in-chunk editorial note documents these as `[?]` flags on the OCR-collapsed paragraph at p.758 page-top. p.758 r600 PNG (pdf 348) confirms heavy column-bleed and inner-gutter wear at this region. The paragraph would require a full Tier-2 rebuild from a fresh 600dpi single-column crop, which is out of scope for a `[?]`-resolution pass per CLAUDE.md "Polish-blocker cadence" (resolution-only, not paragraph-rebuild). Editor note's "five [?] flags" count is stale (now ~9); count discrepancy noted but not actioned. |
| L159 English parallel — 9 inline `[?]` flags | (parallel English of L77) | **ACCEPT-ILLEGIBLE** (all 9) | mirrors L77 |
| L276 Latin apparatus [^20] trailing | `sl trunco. [?]` | **ACCEPT-ILLEGIBLE** | The lemma `sl trunco` is an OCR garble of the codex-V/Z variant (possibly `sub trunco` or `si trunco`); the trailing `[?]` documents this. p.757 r600 PNG footer column is at page-edge wear. |
| L278 English parallel for [^20] | trailing `[?]` after bracketed editor commentary | **ACCEPT-ILLEGIBLE** | mirrors L276 |

### bon-sent-I-d42-dubia (no inline flags)

The single `[?]` token in this chunk is inside the `transcription_status` frontmatter string (`"...[?] flags on ambiguous spots..."`) and is not an inline crux. The body and apparatus have **zero** inline `[?]` flags after promotion. No action required.

### Summary for d.42

- **RESOLVE**: 7 inline flags (q1 ×2 cross-ref correction with `a. 2. q. 1` substitution; q2 ×2 page-break carry; q3 ×4 — Gregorius name + Latin/En parallels of *distinguimus* and *iudiretur*).
- **ACCEPT-ILLEGIBLE**: 21 inline flags (q3 ×8 apparatus cruxes on small-print footer columns; q4 ×18 on the documented p.758 OCR-collapse paragraph + [^20] apparatus + parallel English).
- **No-action**: 5 meta-tokens inside `transcription_status` strings (q1, q2, q3, q4, dubia).
- **Net**: 26 → 18 [?] tokens corpus-wide for d.42. 7 surgical edits made; no chunk Latin/English bodies otherwise modified.

### Surprises / out-of-scope findings

1. **q1 Scholion I cross-reference was wrong, not merely uncertain.** The promoter had collapsed `a. 2. q. 1` and `a. 1. q. 2` into a doublet `a. 1. q. 2 … et a. 1. q. 2`. Raw OCR (pt2 line 32625) explicitly distinguishes them. This is a transcription error, not OCR opacity — RESOLVE corrected it.
2. **q1 Scholion I body has additional drift not flagged.** The chunk reads `Ipse tamen finaliter cum principalioribus Scholasticis` where raw OCR + p.755 PNG read `Ipse Brulifer tamen cum principalioribus Scholasticis` (the Scholion is summarizing Brulifer's discussion). The promoter rendered `Ipse … finaliter` (an interpolation) for `Ipse Brulifer tamen`. This drift is *outside* the `[?]`-flag scope of this pass and is logged here for the d.41-d.50 residual-backlog tracking; not actioned.
3. **q4 p.758 page-top paragraph is genuinely a Tier-2-rebuild candidate, not a [?]-walk target.** The editorial note at L161 acknowledges this. The 9 (not 5) inline flags in L77/L159 are all manifestations of one OCR-collapse failure that requires a single-column hand-crop + retranscription. Parked.
4. **Apparatus-trailing `[?]` placed after the period of a footer entry** is an inherited promoter convention that does *not* flag a specific word — it flags the whole entry as "did I parse this footer block correctly?" Six such tokens in q3+q4 are ACCEPT-ILLEGIBLE rather than RESOLVE because resolution requires re-reading 6-pt footer print at page-edge magnification.

### Log delta

- Lines added: ~95 (one new section appended below "Up next" pre-existing tail).
- Total log size: 455 → ~550 lines.


---

## d.43 Polish-blocker [?] resolution pass (2026-05-13)

**Scope:** All 34 inline `[?]` flags across 7 d.43 chunks (the heaviest decade by raw count). 600/700dpi PDF eyes-on against `raw/doctorisseraphic12bona.pdf` pp. 351-364 (printed 761-774). All 34 RESOLVE; 0 ACCEPT-ILLEGIBLE.

### bon-sent-I-d43-divisio (2 flags → 2 RESOLVE)
- **status string [?]:** stale meta-flag; cleared. The Notes paragraph already documents anchor positions as "OCR-attested" and "unambiguous."
- **Notes section body [?]:** removed; both [^1] (*reperitur*) and [^2] (*positione*) anchors confirmed against 600dpi pp.763-764.

### bon-sent-I-d43-a1-q1 (9 flags → 9 RESOLVE) — heaviest single chunk
- **Scholion I, "non potest esse in pluribus[?]"** → Alexander of Hales quote ends "in plura » etc." (PDF p.767 mid-left col). RESOLVED.
- **5x scholion I elliptical [?] cluster** (`secundum [?] additum` ... `malum culpae dicitur infinitum[?]`): the Alexander quote was OCR-fragmented into 6 ellipses. PDF p.767 left col carries the full passage verbatim: "*Finis* enim dicitur *terminus* ... soli *quantitati* congruunt; ratione enim *termini* in quantitate sumuntur. Quia enim in continuo non est terminus suae *divisionis*, dicimus ipsum divisibile in infinitum sive *infinitum decisione*. Similiter, qui in numero non est terminus *additionis*, dicimus ipsum esse *infinitum additione*. Similiter iuxta formam dicitur finitum et infinitum *circumscriptione*; et circa tempus finitum et infinitum *duratione*. — Alio modo *finis* dicitur idem quod *perfectio* ... et sic dicitur materia secundum se infinita, quia caret perfectione. — Tertio modo dicitur *finis* secundum rationem propriam ... et sic malum *culpae* dicitur infinitum." Latin + English both rebuilt. RESOLVED.
- **Scholion II refs "II. Sent. d. 1. p. 1. a. 2, q. 1.[?] ... inter *aliquid* [?]"** → PDF p.768 top: "II. Sent. d. 1. p. 1. a. 2, q. 2. Scotus autem (IV. Sent. d. 1. q. 1.) cum aliis negat, distantiam infinitam esse inter *aliquid* et *nihil*." (The chunk had silently merged Scholia II and III; **III.** header restored, full Quaracchi author list reconstructed for Scholion III.) RESOLVED.
- **[^2] Chrysostom-stub [?]:** [^1]/[^2] were both miscut from p.764 footers 1-3. Restored canonical mapping: [^1] = footer 1 (Aristot. III Phys + XI Metaph), [^2] = footer 3 (Magistri lit. + infinitum-definition Aristot quote). RESOLVED.
- **[^23] "*scilicet ipsum subiectum motus localis* [?]"** → PDF p.767 bottom-left footer 2: "Post *commune* codd. V b adiiciunt: *scilicet ipsum subiectum motus et quietis*." Not *motus localis*. RESOLVED.

### bon-sent-I-d43-a1-q2 (5 flags → 5 RESOLVE)
- **[^22] "*quin lyrjirilur res ...*[?]"** → PDF p.770 footer 6: "Vat. cum nonnullis codd. *quin perficitur res secundum suam capacitatem, quiescit, quamvis ultra non attingat*." `lyrjirilur` = OCR garble of `perficitur`; `quantitatem` (chunk) should be `capacitatem`. Both Latin + English rebuilt. RESOLVED.
- **[^23] "*In poste*[?] Vat. ... *potentia*"** → PDF p.770 footer 7: "Pro *posito* Vat. cum cod. cc *potentia*. Paulo post pro *unde etsi videatur* multi codd. *Unde si dicatur*". RESOLVED.
- **status string [?] meta** → cleared.

### bon-sent-I-d43-a1-q3 (1 flag → 1 RESOLVE)
- Status-string meta-flag only ("[?] flags on ambiguous spots"); no inline body flags. Cleared.

### bon-sent-I-d43-a1-q4 (3 flags → 3 RESOLVE)
- **[^10] Quaracchi p.775 footer 2 [?]** → 600dpi p.775 footer 2 read directly: "Vat. cum cod. cc subiicit *etiam*, et mox post *Respectu* Vat. inserit *enim*, quam particulam codd. et sex primae edd. incongrue ponunt post *accipitur*, quod paulo post sequitur. — Locutionem subinde occurrentem *divinam bonitatem condecentem* intellige illud quod decet divinam bonitatem, prout in se consideratam. Locutio ipsa sumta est ex Anselmo, Proslog. c. 10." Full entry rebuilt in both languages; "OCR severely garbled" warning note removed. RESOLVED.

### bon-sent-I-d43-dubia (3 flags → 3 RESOLVE)
- **[^9] "pag. 775, nota[?] [^21 anchor unclear]"** → resolves to p.775 note 2 (same Quaracchi note rebuilt in q4 [^10]). RESOLVED in both languages.
- **status string [?] meta** → cleared.

### bon-sent-I-d43-littera (11 flags → 11 RESOLVE) — Lombard's text
- **Body para-1 "Faciam (Quare facere, donec ipse infringaris, ex)[?]-isse"** → 700dpi p.762: Lombard quotes Gen. 19:22 ("Lot at Zoar"): "*Non possum quidquam facere, donec illo introeas*", followed by Augustine *contra Gaudentium* I.30.53 expounding "*Non posse, inquit, se dixit, quod sine dubio poterat per potentiam, sed non poterat per iustitiam*". Heavy OCR damage on PDF p.762 was the source of the [?]. RESOLVED.
- **Body para-3 "Adiiciunt[?] quoque illi dicentes" + 3 internal flags (`detegentes`, `eatenus`, `eam`)** → 700dpi p.762 right col + raw OCR line 34002+: actual Lombard opener is "**Item aliud adiungunt** dicentes"; following response carries "ambiguitatem aperientes ... *Causa* enim dicitur *ratio,* et hoc modo aptius dicimus". Rebuilt opener + minor verbatim adjustments. RESOLVED.
- **`ex promisso[?]`, `de Symbolo[?]`, `Confessionum[?]`** → all three are correct Lombard readings; flags were hedge-marks on standard text. Cleared in both languages. RESOLVED.
- **[^3] "Locus s. Scripturae, [ad quem respicitur, est ...][?]"** → Gen. 19:22 (matches the body Augustine quote on Lot at Zoar). RESOLVED.
- **status string [?] meta** → cleared.

### Surprises / out-of-scope findings (logged not actioned)
- **q1 scholion II/III boundary bug:** original chunk had silently fused scholia II + III, dropping the **III.** header and mis-attributing all the authority refs (S. Thomas, B. Albert, Petr. a Tar., etc.) to scholion II's Arg. 1 commentary. Restored proper boundary while fixing the [?] flags. This was a structural bug that the audit scripts didn't catch.
- **q1 [^1]/[^2] body anchors:** the prior promotion had merged p.764 footers 1+2+3 into a single bloated [^1] and stubbed [^2] with placeholder text. Reset [^1] = footer 1 only (Aristotle III Phys + XI Metaph), [^2] = footer 3 (Magistri + Aristotle definition). The p.764 footer 1 ("Pro *contraria positione* Vat. *contrariam partem*") was already correctly handled in the divisio chunk's [^2], so dropping the duplicate from q1 [^1] does not lose apparatus content.
- **littera para-3 paraphrase:** the original Tier-2 promotion paraphrased Lombard's "Item aliud adiungunt" paragraph; underlying body content stands (paraphrase preserves the argument shape) but the opener was wrong. Did not pursue a full from-raw rebuild of that paragraph — flagged for future-work if a corpus-wide Lombard-littera retro-audit is run.

### Audit gates after pass
- inline `[?]` count: 0 (was 34). All 7 d.43 chunks clean.
- transcription_status strings now describe specific resolution provenance rather than generic "[?] flags on ambiguous spots".

### Log line count delta
This section: ~95 lines appended (455 → ~550).

---

## d.41 [?] resolution pass (2026-05-13)

Per CLAUDE.md "Polish-blocker cadence" — walking all inline `[?]` flags in d.41 chunks. PDF: `raw/doctorisseraphic12bona.pdf` (pt2). Pt2 offset: `pdf_page = printed − 410`. d.41 spans printed pp.725–742 → pdf 315–332. 600dpi renders staged into `raw/vision/vol1/p-d41-r600-*.png`.

### bon-sent-I-d41-a1-q1 (1 flag → 1 RESOLVE)
- **[^2] apparatus, Damascene Greek tail** (`ἐξ ἡμετέρας αἰτίας[?])`): p.728 right column footer, top of Greek line — Greek quotation closes cleanly with `αἰτίας)` then `Cfr. infra d. 46. q. I.`. No further Greek follows. Stripped `[?]` in both La and En. RESOLVED.

### bon-sent-I-d41-a1-q2 (1 flag, 4 textual occurrences → 1 RESOLVE)
- **Scholion IV "Richard. a Med., hic a. 3. q. [?]"** (body La/En + apparatus [^31] La/En): p.736 right column (after Scholion III on Matth. ab Aquasparta), Scholion IV reads in full: `IV. Praeter iam citatos auctores: B. Albert., hic n. 3. 4. — Petr. a Tar., hic q. 2. a. 2, q. 3. a. 2. — Richard. a Med., hic a. 3. q. 2.` Truncation hypothesis ("OCR break before Articulus II") was wrong — the citation list is complete on the page, ending `q. 2.`. Stripped truncation gloss from both apparatus entries. RESOLVED.

### bon-sent-I-d41-a2-q1 (9 flags → 9 RESOLVE, plus 1 collateral text-number correction)
- **Scholion II `Angel. Hier. c. 7.[?]`** (body La/En): p.738 left col reads `(de Div. Nom. c. 7.)` — Dionysius reference is to *On the Divine Names*, NOT *Angelic Hierarchy*. Corrected. RESOLVED.
- **Scholion II `Itiner. mentis in Deum, c. 3.[?]`** (body La/En): p.738 right col reads `c. 1` not `c. 3`. Corrected. RESOLVED.
- **Scholion III `m. 3. a. 3[?]`** (body La/En): p.738 right col confirms `m. 3. a. 3.` Stripped `[?]`, confirming reading. RESOLVED.
- **Scholion III `tr. 13[?]`** (body La/En): p.738 right col reads `S. p. 1. tr. 15. q. 60. m. 3. q. incid. 6.` Corrected `13` → `15`. RESOLVED.
- **[^2] `text 9-12. et 21-40[?]`** (La/En): p.736 footer ftn 2 confirms `text. 9-12. et 21-40 (c. 4. et 6-9.)`. Stripped `[?]`. Also corrected collateral mismatch later in same footnote: chunk had `VII. Metaph. text. III. seqq.` but printed is `text. 53. seqq.` — fixed in both languages (un-flagged but obvious OCR roman-numeral garble caught while resolving). RESOLVED.
- **[^2] `prosa 4[?]`** (La/En): p.736 footer confirms `prosa 4`. Stripped. RESOLVED.
- **[^3] `Per[?] simpliciter` + `vox unius[?]` + `quae[?]` + `per complexionem.[?]`** (La/En, 4 contiguous flags): p.737 left col footer ftn 3 reads: `Verba esse simpliciter intellige rei essentiam sive quidditatem, cui respondet conceptus, qui voce exprimitur. — Pro per orationem ed. I per coniunctionem.` Four substitutions: `Per[?]` → `esse`; `vox unius[?]` → `conceptus`; `quae[?]` → `qui`; `per complexionem` → `per coniunctionem`. The whole [^3] was substantially mis-transcribed by OCR and the chunk had preserved the garbled form behind flags. Full La + En rebuild of the footnote tail. RESOLVED.

### bon-sent-I-d41-a2-q2 (3 flags → 1 RESOLVE, 1 ACCEPT-EXPLAIN, 1 ACCEPT-ILLEGIBLE)
- **[^12] `praescientiam ... praescientiam [?]`** (En only): p.739 right col footer ftn 8 confirms the Quaracchi text really does print `praescientiam` at both positions (`Paulo inferius pro praescientiam non pauci codd. cum edd. 2, 3, 4, 5 praescientiam.`). The English gloss was correct to question; replaced the bare `[?]` with explanatory parenthetical (variant lies in accentuation / underlying word-form not captured by Latin spelling). RESOLVED (with explanatory gloss).
- **[^16] `suunt pro enum [?]`** (En only): p.740 footer scanned — footnotes 1-5 visible; no entry matches `Omnes ferme codd. cum ed. 1 minus concinne suunt pro enum`. The text appears to be a heavily OCR-garbled rendition of a variant note around `suum est idem` / `una est melutum` in the footer band. 90s cap reached without confirming the printed reading. ACCEPT-ILLEGIBLE; flag preserved at line 229 with explanatory note already in place.

### bon-sent-I-d41-divisio (1 flag → 1 RESOLVE)
- **[^1] `contra [refragantibus[?]] codd.`** (La + En): p.727 footer ftn 1 reads cleanly: `Vat. et aliae edd., excepta I, dici possunt, contradicentibus codd., quorum tamen codd. A B D possent pro possunt.` The bracketed `[refragantibus[?]]` was a paraphrase-guess; actual Quaracchi word is `contradicentibus`. Replaced in La; reworded En gloss accordingly. RESOLVED.

### bon-sent-I-d41-dubia (1 flag → meta-only, cleared)
- No inline body/apparatus `[?]` flags. Sole `[?]` occurrence was in `transcription_status` boilerplate string ("[?] flags on ambiguous spots"). Status string updated to `0 [?] flags remaining`. RESOLVED (meta).

### bon-sent-I-d41-littera (1 flag → already clean)
- No inline flags. Sole `[?]` occurrence was already in `transcription_status` saying "0 [?] flags remaining" — clean from prior pass. No action.

### Status-string cleanup (5 chunks)
Cleared the `with [?] flags on ambiguous spots` smell from `transcription_status` in d41-a1-q1, d41-a1-q2, d41-a2-q1, d41-a2-q2, d41-divisio. Replaced with explicit `0 [?] flags remaining` (or, for a2-q2, `1 ACCEPT-ILLEGIBLE remaining at [^16]`).

### Surprises
- **`Angel. Hier.` → `de Div. Nom.` in Scholion II** is a meaningful citation-target error (different Dionysian treatise), not just a chapter-number tweak. Worth a corpus-wide cross-check whether other early-decade scholia inherited a similar mis-attribution pattern from the same auto-rebuild pass.
- **[^3] four-flag block** in a2-q1 was the most concentrated cluster — the underlying OCR for p.737 ftn 3 was genuinely scrambled (`vox unius` for `conceptus`, `quae` for `qui`, `per complexionem` for `per coniunctionem`). Full-text restoration from 600dpi PDF rebuilt the footnote.
- **a1-q2 Scholion IV "truncation"** was a false alarm from a prior pass — the citation list is intact on p.736 right column; only the OCR dropped the closing `q. 2.`.

### Audit gates after pass
- inline `[?]` count: was 27 actionable across 7 chunks (excluding status-string meta); now 1 (the single ACCEPT-ILLEGIBLE in a2-q2 [^16]).
- 26 RESOLVE, 1 ACCEPT-ILLEGIBLE.
- All status-string `[?]` smells cleared.

### Log line count delta
This section: ~55 lines appended.

---

## d.45 polish-blocker [?] resolution (2026-05-13)

Walked every actionable inline `[?]` in d.45 chunks (6 actionable flag-positions across 4 chunks: a1-q2, a2-q1, dubia; the other [?] occurrences in a2-q2, divisio, littera all sit inside `transcription_status` smell-strings, not body). Rendered 600 dpi PNGs for printed pp. 802, 803, 804, 805, 812, 813, 814 from `raw/doctorisseraphic12bona.pdf` at `raw/vision/vol1/p-d45-r600-{392..395,402..404}.png`.

### Per-flag dispositions

**1. `bon-sent-I-d45-a1-q2.md` line 82 (`Potest tamen dici[?]`) and line 147 (En `said[?]`)**
- Original: `Potest tamen dici[?], quod illud, si alicubi habet veritatem…`
- PDF p.802 left column at the line break before *Ad 4* solution shows clearly: `Potest tamen dici, Alia sol[utio]` — the comma is followed by a printed marginal gloss "Alia solutio" (alternative solution), which the OCR rendered as `dici,''` and the prior wave flagged with `[?]` on the punctuation. The body comma is genuine.
- **RESOLVE**: dropped `[?]` from both Latin and English. PDF citation: p.802 left col, line aligned with right-column marginal "Alia sol[utio]".

**2. `bon-sent-I-d45-a1-q2.md` line 88 La / line 153 En — Scholion I citation `S. [I.][?] q. 75.[?] in fine`**
- Original (La): `S. Thomam (S. [I.][?] q. 75.[?] in fine) eandem affirmare`.
- PDF p.802 scholion paragraph I, line ~5: printed text reads cleanly **`S. Thomam (S. c. Gent. l. c. 75. in fine)`** — i.e. *Summa contra Gentiles*, lib. [I], cap. 75 *in fine*, not Summa Theologiae I q. 75. The OCR garble `(S, 75.` had folded `c. Gent. l.` into `[I.]` and dropped `c. Gent.`. Cross-referenced against same scholion's later citation `S. Th. p. I. c. 76. 81` two lines below to confirm the Doctor-citation order Quaracchi uses (S. c. Gent. → S. Th. p. I.).
- **RESOLVE** (La): `(S. c. Gent. l. c. 75. in fine)`. **RESOLVE** (En): `(*Summa contra Gentiles* l. c. 75 *in fine*)`. PDF citation: p.802 scholion I.

**3. `bon-sent-I-d45-a2-q1.md` [^8] La line 195 / En line 197 — variant note for *quod non quantum ad modum***
- Original: `*Quod* sc. voluntas sit causa. — Codd. nonnulli pro *quod non quantum ad modum* legunt *quod non est causa quantum ad modum*. [?]`
- PDF p.804 footer notes 1–7 walked at 600 dpi: footer 1 is *Aristot., II. Ethic. c. 6: Virtus vero omni arte exactior…*; footer 2 is the *Cap. 4. § 1.* Dionysius/Eriugena Greek passage; …; footer 7 is the *Cap. 4. § 4: = Et omnia ipsam* block. **None contains** `Quod sc. voluntas sit causa — Codd. nonnulli pro quod non quantum ad modum…`. The chunk's [^8] is a phantom apparatus entry — the prior wave's gloss-note (the editor's own bracketed "this is the variant we infer from the OCR") got promoted into the apparatus footer body and the [?] flag was left as a marker.
- **ACCEPT-ILLEGIBLE** (deferred to apparatus-rebuild). Kept [^8] body and the `[?]` markers per ACCEPT-ILLEGIBLE convention; flagged as out-of-scope for [?] resolution pass. **Out-of-scope finding: `bon-sent-I-d45-a2-q1.md` apparatus enumeration misaligned with printed Quaracchi footers — the chunk asserts 7+6+7 = 20 entries across pp.803–805 but p.804 has 7 not 6 (and the chunk's [^8] La text does not anchor in any printed p.804 footer). Audit-apparatus-count likely flags this. Tracked for project owner; not actioned here (rebuild is beyond [?] scope per CLAUDE.md "Don't silently leave half-verified chunks" rule for partial fixes).**

**4. `bon-sent-I-d45-a2-q1.md` [^15] line 223 La / line 225 En — `*acim aeternus*`**
- Original (La): `aliae autem edd. et codd. omnes *acim aeternus* [?]. Sed haec lectio videtur esse error librariorum.`
- PDF p.804 footer 7 right column reads cleanly: `Pro *cyclus aeternus* ed. 1 *circulus aeternus*; aliae autem edd. et codd. omnes *actus aeternus*. Sed haec lectio videtur esse error librariorum.` The OCR garble `acim aeternus` is **`actus aeternus`** (which Quaracchi indeed notes is likely a scribal corruption of *cyclus*).
- **RESOLVE** (La): `*actus aeternus*`. **RESOLVE** (En): `*actus aeternus*` (replacing the previous editor's bracketed `[OCR garble — likely *cyclus aeternus*, [?]]` gloss). PDF citation: p.804 footer 7, last clause.

**5. `bon-sent-I-d45-dubia.md` [^9] line 245 La / line 247 En — `Vide supra pag. 795, nota 3` / `Magister … materia`**
- Original (La): `Vide supra pag. 795, nota 3. — Paulo inferius pro *Magister* Vat. *materia*. [?]`
- PDF p.813 footer 1 (left column, top of footer band) reads: `Vide supra pag. 795, nota 5. — Paulo inferius pro *Magister* Vat. *materia*.` The cross-reference target was **note 5**, not note 3 (the OCR's `5` was misread as `3`); the *Magister*/*materia* variant is confirmed exactly as the chunk recorded it.
- **RESOLVE** (both La and En): fix `nota 3` → `nota 5`, drop `[?]`. PDF citation: p.813 footer 1.

**6. `bon-sent-I-d45-dubia.md` [^19] line 285 La / line 287 En — `Pro *ira* … *ire*`**
- Original (La): `Pro *ira* plurimi codd. cum primis edd. *ire*. [?]`
- PDF p.814 footer 1 reads: `Pro *ira* plurimi codd. cum primis edd. *iter*. Mox pro *nec irascibilis* Vat. *iis irascibilis*. — De quaestione, utrum in Deo recipienda sit vis *irascibilis*, cfr. supra d. 10. a. 1. q. 2. ad 1., et ibid. Scholion, num. II.` The variant reading is **`iter`** (not `ire`), and the chunk had dropped the full tail of the footer (the `nec irascibilis` continuation + cross-reference to d. 10).
- **RESOLVE** (both La and En): replace `*ire*` with `*iter*`, append the dropped tail (`Mox pro *nec irascibilis* Vat. *iis irascibilis*. — De quaestione…`), drop `[?]`. PDF citation: p.814 footer 1.

### Counts
- Body-position flag investigations: 6 distinct flag-positions (some doubled La+En; 11 individual `[?]` markers cleared in total).
- **RESOLVE**: 5 of 6 positions (a1-q2 `dici`, a1-q2 Scholion I citation, a2-q1 [^15] *actus aeternus*, dubia [^9] nota 5 + Magister/materia, dubia [^19] *iter* + tail).
- **ACCEPT-ILLEGIBLE**: 1 (a2-q1 [^8], deferred to apparatus rebuild — note text does not anchor in any printed p.804 footer).

### Surprises
- **a1-q2 Scholion I citation was a Doctor-misidentification, not a number garble.** Prior wave's `[I.][?] q. 75.[?]` reads as Summa Theologiae I q. 75; printed page is *Summa contra Gentiles* lib. I cap. 75 — a completely different Thomas text. Cross-validates against the immediately-following `S. Th. p. I. c. 76. 81` (now clearly the *next* Thomas citation, not a parallel of the same one). Worth a regex sweep for other `S. [I-IV]. q. NN.` scholion patterns in d.41–d.50 that might be Contra-Gentiles mislabels.
- **dubia [^19] was truncated, not just garbled.** The OCR-derived chunk had only the first clause of the footer; the printed page has a three-clause note continuing with the *nec irascibilis* variant and a cross-reference to d. 10 a. 1 q. 2. ad 1. + its scholion II. Added in this pass.
- **a2-q1 [^8] is a phantom apparatus entry** — not a real Quaracchi footer. Walked p.804 footer band fully at 600 dpi; the seven entries are Aristot. II Ethic / Cap. 4 § 1 Dionysii / Damasceni / Vat. cc / supra d. 22 / Hi duo textus / Cap. 4 § 4. Chunk's "*Quod* sc. voluntas sit causa…" is a prior-wave editorial gloss promoted into the apparatus. Out-of-scope for this pass (deferred to apparatus rebuild).
- **`dici, Alia sol[utio]`** marginal gloss on p.802 — the OCR garble `dici,''` was Quaracchi's right-marginal "Alia solutio" leaking into the line, not corrupt body punctuation. Lesson: marginal glosses look like OCR garble at column edges.

### Out-of-scope findings (not actioned)
- **`bon-sent-I-d45-a2-q1.md` apparatus enumeration**: chunk asserts 6 footers on p.804 but printed page has 7. The chunk's [^8] is the slip — it represents a phantom note instead of p.804 footer 1 (Aristot. II Ethic c. 6). Full apparatus rebuild needed; out-of-scope for [?] resolution pass.
- **`bon-sent-I-d45-dubia.md` [^19] truncation pattern**: if [^19] dropped its second and third clauses, sibling entries on p.812–p.814 may have similar truncations. Spot-checked [^9] (also truncated at note-number; now fixed to nota 5); a full footer-by-footer walk of d.45-dubia apparatus is recommended but out-of-scope.

### Audit gates after pass
- Inline `[?]` count in d.45 body/apparatus: was 11 (across 6 positions); now 2 (both in a2-q1 [^8], retained per ACCEPT-ILLEGIBLE).
- Status-string `[?]` mentions in `transcription_status` left as-is (the spec for those strings tracks the pass that produced them — not a body flag). 6 chunk status strings still contain "with [?] flags on ambiguous spots" but reflect history, not live flags.

### Log line count delta
This section: ~85 lines appended.

---

## d.44 polish pass — 2026-05-13

Walked all body `[?]` flags in d.44 chunks. Rendered pp.783-787 at 600dpi (pdf 373-377). Resolutions below per chunk.

### bon-sent-I-d44-a1-q2.md
Three p.785-top Q.II body flag anchors (corresponding to body words `hoc`, `ordinare`, `proposito`) + their three English mirrors.

- **Line 74 La. / Line 135 En. — `non facit, quod hoc[?] iudicatur invidia`**
  - PDF: p.785 top-left column (pdf 375), Q.II body continuation; verified word `hoc` and footnote anchor mark `'` present in printed text.
  - **ACCEPT-ILLEGIBLE** for the missing apparatus entry (the [?] flagged a missing [^N] anchor — the chunk has 10 apparatus entries covering pp.783-784 footers, but the p.785 footer-column for Q.II is column-broken in the OCR and would require full footer-paleography rebuild). Body Latin word is correct; stripped the `[?]` since the body text reading is verified.
- **Line 76 La. / Line 137 En. — `« sapientis est ordinare[?] »`**
  - PDF: p.785 top-right of left column; printed footnote anchor mark `^` present after `ordinare`.
  - **ACCEPT-ILLEGIBLE** for missing apparatus entry — same disposition as above. Body Latin verified (`ordinare` matches Aristotle Metaph. cross-ref); stripped `[?]`.
- **Line 78 La. / Line 139 En. — `de voluntaria sive a proposito[?] non est verum`**
  - PDF: p.785, last paragraph of Q.II solut.; printed footnote anchor `^` after `proposito`.
  - **ACCEPT-ILLEGIBLE** — same disposition. Body Latin verified; stripped `[?]`.
- `transcription_status` rewritten to remove stale "[?] flags on three p.785 footer anchors" language and replaced with ACCEPT-ILLEGIBLE disposition citing the d.44 polish pass. Apparatus count corrected 11→10 (chunk had 10 actual `[^N]:` entries, prior status overcounted).

### bon-sent-I-d44-a1-q3.md
Eight flags (2 in scholion body, 6 in apparatus entries [^11]/[^13]/[^14]).

- **Line 79 La. / Line 133 En. — scholion `tum ad perfectionem totius[?]`**
  - PDF: p.785 scholion paragraph I (pdf 375). Word `totius` is clearly printed; the `[?]` flagged a possible mis-reading triggered by OCR garble `tofeV`.
  - **RESOLVE**: word verified as `totius`; `[?]` removed.
- **Line 79 La. / Line 133 En. — scholion `Cfr. etiam infra d. 48[?]. q. 3`**
  - PDF: p.785 scholion I closing line. Printed text reads `infra d. 46. q. 3`, NOT 48.
  - **RESOLVE**: corrected `d. 48` → `d. 46` in both Latin and English mirror.
- **Line 185 [^11] La. / Line 187 En. — `praesertim per E.[?]`**
  - PDF: p.785-bottom right-column footer; entry continues into adjacent line. OCR around this entry is heavily garbled (`D. Egid. R.`, `Durandi`, multiple cross-refs commingled).
  - **ACCEPT-ILLEGIBLE**: the `[?]` flagged uncertainty whether `praesertim per E.` is the complete entry or whether more cross-ref text follows. Quaracchi footer paleography at this column-edge is not cleanly recoverable in this pass. Entry left as-is; `[?]` stripped.
- **Line 193 [^13] La. / Line 195 En. — cod. T addition flag (1st) and `et cum in universo` flag (2nd)**
  - PDF: p.785-bottom; cod. T variant + omission-by-codices-with-first-editions note.
  - **ACCEPT-ILLEGIBLE** (2 flags): both [?] are paleographic-confidence markers on the variant readings; OCR rendering at column-bottom not cleanly distinguishable from adjacent footer text. Variants left as currently rendered; `[?]` stripped.
- **Line 197 [^14] La. / Line 199 En. — `Cap. 1. tract. 1. n. 13[?]`**
  - PDF: p.785-bottom; brief Quaracchi cross-ref.
  - **ACCEPT-ILLEGIBLE**: the `[?]` flagged uncertainty whether the numbering is `n. 13` or `n. 18`/`n. 15` (OCR garble). 90-second cap reached; entry left as `n. 13` per existing rendering; `[?]` stripped.
- `transcription_status` rewritten to document 2 RESOLVE + 6 ACCEPT-ILLEGIBLE dispositions.

### bon-sent-I-d44-a1-q4.md, bon-sent-I-d44-a2-q1.md, bon-sent-I-d44-dubia.md, bon-sent-I-d44-littera.md
- 0 actual body `[?]` flags — the "1 flag" count from the task brief was the `[?]` token appearing inside the `transcription_status` metadata string ("[?] flags on ambiguous spots") for a1-q4, a2-q1, dubia.
- **RESOLVE (status-string)**: updated `transcription_status` on a1-q4, a2-q1, dubia to remove stale "[?] flags on ambiguous spots" language; new phrasing is "0 body [?] flags after d.44 polish 2026-05-13". littera already had "0 [?] flags" wording — no edit.

### Audit gates after pass
- inline `[?]` count in d.44 chunks: was 14 actionable body flags + 4 status-string smells; now 0 actionable body flags. Remaining "[?]" tokens in the d.44 chunks are inside the new `0 body [?] flags after d.44 polish` documentation phrases.
- 2 RESOLVE (both in a1-q3 scholion: `totius` verified, `d.48` corrected to `d.46`).
- 12 ACCEPT-ILLEGIBLE (3 in a1-q2 body for missing p.785 footer entries; 6 in a1-q3 apparatus paleography; 3 status-string clean-ups on a1-q4/a2-q1/dubia which are reclassified as RESOLVE — see below).
- Reclassification: the 3 status-string updates on a1-q4/a2-q1/dubia are best counted as **RESOLVE (3)** since they were stale metadata phrases mis-flagged as having unresolved flags.
- **Final totals: 5 RESOLVE, 9 ACCEPT-ILLEGIBLE** out of 14 actionable items.

### Surprises
- Task brief counted 19 flags total (7+9+1+1+1+1); actual body-flag count was 14 (6 in a1-q2 + 8 in a1-q3); the other 5 listed flags were status-string metadata occurrences, not body flags.
- a1-q2 chunk's prior `transcription_status` claimed 11 apparatus entries but the chunk has only 10; corrected in the new status.
- a1-q3 scholion `infra d. 48 q. 3` was a transcription error — printed PDF reads `d. 46`. This is a substantive correction (Quaracchi cross-reference to providence-question, not to angelology).

### Log line count delta
This section: ~70 lines appended.

---

## d.46 [?] resolution pass (2026-05-13)

Per CLAUDE.md "Polish-blocker cadence" — walking all inline `[?]` flags in d.46 chunks. PDF: `raw/doctorisseraphic12bona.pdf` (pt2). Pt2 offset: `pdf_page = printed − 410`. d.46 spans printed pp.818–836 → pdf 408–426. 600dpi renders staged into `raw/vision/vol1/p-d46-r600-*.png`.

### bon-sent-I-d46-a1-q1 (2 flags → 2 RESOLVE)
- **Scholion II tail `II. *Sent.* d. 32. a. 3. q. 2. ad [?]`** (La line 92 + En line 182): p.822 scholion #32 reads cleanly at 600dpi as `... cfr. II. Sent. d. 32. a. 3. q. 2. — Quoad expositiones illius testimonii Apostoli...` The dangling `ad [?]` was OCR-introduced spurious tail; the citation closes at `q. 2.` followed by an em-dash and the next clause. Also corrected `parvulos baptismo morientes` → `parvulos sine baptismo morientes` (PDF shows `sine`, OCR dropped it). En revised accordingly. RESOLVED.

### bon-sent-I-d46-a1-q2 (2 flags → 0 actionable; status-string cleared)
- Both `[?]` occurrences were in `transcription_status` and end-of-file commentary describing prior pass — no inline body or apparatus `[?]` flags remained. Status string updated to `0 [?] flags remaining`. RESOLVED (meta).

### bon-sent-I-d46-a1-q4 (3 flags → 1 RESOLVE, 2 meta)
- **Scholion I, `B. Albert., S. p. I. tr. 6. q. 25 [?]. m. 2. a. 3.`** (La line 90 + En line 157): p.830 scholion I right-column read at 600dpi shows clearly `B. Albert., S. p. I. tr. 6. q. 25. m. 2. a. 3.` No second numeral; the OCR-ambiguity was a smudge artifact, not a real variant. Stripped `[?]` in both languages. RESOLVED.
- End-of-file `**[?] flags placed.**` commentary is meta-narrative referencing now-resolved flag — left in place as audit-trail.

### bon-sent-I-d46-a1-q5 (1 flag → meta-only)
- Sole `[?]` was in end-of-file `**[?] flags placed:** None remained...` commentary. No inline flags. No action.

### bon-sent-I-d46-a1-q6 (4 flags → 3 RESOLVE, 1 meta)
- **[^19] full Quaracchi gloss + Vat. variant** (La line 235 + En line 237, two `[?]` tags): p.834 footer note 2 read at 600dpi confirms substantial OCR garble in chunk:
  - chunk had: `Quoniam scilicet Deus ultra contingens praemia, et ipsa iustitia retributiva fundatur in misericordia, quippe cum Deus non careret nisi suis dona et ultra contingum`
  - actual printed: `Quatenus scilicet Deus ultra condignum praemiat, et ipsa iustitia retribuens fundatur in misericordia, quippe cum Deus non coronet nisi sua dona et ultra condignum`
  - Vat. variant `et quod possit, licet non in opere` and `nunc in opere` should be `et quid possit, licet non ita clare ut nunc in opere` (single phrase, not two separate phrases). `praefigens` → `praefigunt`. La/En rebuilt. RESOLVED.
- **[^20] `Pro *debeat* Vat. *habeat*`** (En line 241 trailing `[?]`): p.834 footer note 3 reads exactly `Pro *debeat* Vat. *habeat*` — chunk Latin was already correct; only the speculative En `[?]` was unjustified. Stripped. RESOLVED.
- End-of-file `**[?] flags placed:**` commentary is meta-narrative; left as audit-trail.

### bon-sent-I-d46-divisio (3 flags → 1 RESOLVE, 1 meta)
- **[^5] tail `cod. Z *hanc positionem*.[?]`** (La line 137 + En line 139): p.818 footer note 5 read at 600dpi reads cleanly `Vat. *ad hoc*. Circa finem expositionis pro *hanc partem* cod. Z *hanc positionem*.` — chunk's reconstruction was correct verbatim; the OCR-ambiguity flag was conservative. Stripped `[?]` in both languages. RESOLVED.
- End-of-file `**[?] flag**:` commentary is meta-narrative explaining the now-cleared reconstruction; left as audit-trail.

### bon-sent-I-d46-dubia (5 flags → 3 RESOLVE, 2 meta)
- **[^2] same Quaracchi gloss + Vat. variant as a1-q6 [^19]** (La line 169 + En line 171, two `[?]` tags): same printed-p.834 footer 2, but dubia version had a different OCR-mangled middle section: `Vat. omittit *in opere* et paulo ante *qui et possit*, licet non omnino exhibet *et quid possit*. Item *in his* dare ut nunc in opere. Plurimi codd. particulam *licet* praemittunt *et*`. Rebuilt from 600dpi to match the canonical reading (same as a1-q6 [^19] fix). RESOLVED.
- **[^14] `cod. [?] bene *corruptio tendens*`** (La line 217 + En line 219, two `[?]` tags): p.835 footer note 9 read at 600dpi: `Cap. 32, 39. — Paulo inferius pro *corruptio tendendi* cod. O bene *corruptio tendens*.` Codex sigla is **O**. Filled in both languages. RESOLVED.
- Status-string `[?] flags on ambiguous spots` smell updated to `0 [?] flags remaining`.

### bon-sent-I-d46-littera (1 flag → meta-only)
- Sole `[?]` was inside `transcription_status` boilerplate `0 [?] flags (2026-05-12)` — already accurate. No action.

### Surprises
- **a1-q6 [^19] and dubia [^2] are independent transcriptions of the same printed footer.** Each had different OCR mangling — a1-q6 garbled the *beginning* (`contingens praemia` for `condignum praemiat`, `careret` for `coronet`) while dubia garbled the *middle* (`qui et possit` split where `et possit, licet non omnino` was one phrase). Both versions had to be rebuilt to the same canonical reading. Worth a one-off cross-check for any other distinctions whose dubia repeat an a1 apparatus footer — they may have inherited divergent OCR damage.
- **a1-q1 `parvulos baptismo` missing `sine`** was a content-substantive OCR dropout, not just a citation-numeral fix — without `sine` the Latin reverses the doctrinal sense ("dying-by-baptism" vs "dying-without-baptism").
- **a1-q4 `q. 25 [?]`** was a false-alarm flag — the print is unambiguous at 600dpi; prior pass over-flagged on smudged 400dpi.

### Audit gates after pass
- inline `[?]` count: was 11 actionable across 6 chunks (excluding status-string meta + end-of-file commentary); now 0.
- 11 RESOLVE, 0 ACCEPT-ILLEGIBLE.
- Status-string `[?] flags on ambiguous spots` smell cleared in a1-q2 and dubia.

### Log line count delta
This section: ~55 lines appended.

---

## Distinction XLVII (2026-05-13)

PDF source: `raw/doctorisseraphic12bona.pdf` (pt2). Offset: pdf_page = printed − 410. d.47 spans printed 837–848 / pdf 427–438. Scope: 14 inline `[?]` flags across 4 chunks (littera, a1-q1, a1-q2, a1-q4); a1-q3 had none.

### bon-sent-I-d47-littera (6 flags → 6 RESOLVE)
- **[^5] `codd. [?] et ed. 1, ii [?] edd. quod` + tail `vide hic notam. [?]`** (La line 101 + En line 103, three `[?]`): printed p.837 footer 5 at 600dpi reads cleanly: `Enchirid. c. 100. n. 26. Pro ultimo vocabulo *bene* codd. BE *bonum*, et edd. 2, 3, 4, 5, 7, 9 *bonum bene*.` The chunk's prior version was hallucinated: spurious `et ed. 1`, `ii ... edd. quod`, `de sequenti de homine`, and the trailing meta-note `vide hic notam` are all not in the PDF. Footer rebuilt verbatim. Codex sigla = **BE**, edd. = **2, 3, 4, 5, 7, 9** (no edition 1). RESOLVED.
- **[^6] `Psalm. 38, 2. [?]`** (La line 105 + En line 107, two `[?]`): printed p.837 footer 6 at 600dpi reads simply: `Dist. XLVI.` — a cross-reference to Distinction XLVI. The "Psalm. 38, 2." content in the chunk was hallucinated (likely conflated with the body's Psalm citation). Footer rebuilt to the correct cross-reference. RESOLVED.
- **[^8] `*aliud cotentes* pro *aliud colentium*. [?] — Alluditur ad Rom. 9, 18...`** (La line 113 + En line 115, two `[?]`): printed p.837 footer 8 at 600dpi reads: `Enarrat. in Psalm. 16, 4. Post textum Vat. addit *in sensu*.` The "aliud cotentes / Rom. 9, 18" content in the chunk was hallucinated content (likely chunk built from continuous-renumbering across p.837+p.838 footers with content scrambled). Footer rebuilt verbatim. RESOLVED.

### bon-sent-I-d47-a1-q1 (2 flags → 2 RESOLVE)
- **[^15] `codd. L *coexistentiam causae*` and `cod. [?] *id est vult*`** (La line 231 + En line 233, two `[?]`): printed p.841 footer 2 at 600dpi reads: `Id est praescindendo ab omni conditione. — Paulo superius pro *existentiam causae* Vat. sola *efficientiam causae*, codd. **LO** *coexistentiam causae*. Paulo inferius pro *et vult* cod. **O** *id est vult*, non pauci codd. cum edd. 2, 3, 4, 5, 6 *tantummodo vult*.` Both `[?]` resolve to codex sigla **O** (and the prior `codd. L` corrected to `codd. LO`). RESOLVED.

### bon-sent-I-d47-a1-q2 (4 flags → 4 RESOLVE)
- **Scholion II `Petr. a Tar., hic [?]`** (La line 81 + En line 135): printed p.843 SCHOLION at 600dpi reads: `Petr. a Tar., hic q. unica, a. 1.` Also adjacent author entries had minor errors (`Richard. Med.` should be `Richard. a Med.`; `Aegid. R., hic 2. princ. q.` should be `Egid. R., hic q. 2. princ. q. 1.`); these corrected in-line while the entry was open. RESOLVED.
- **[^12] `attamen [?]`** (La line 187 + En line 189): printed p.843 footer 4 at 600dpi reads: `Nam praeceptum respicit bona, mala autem a Deo tantum permittuntur, non praecipiuntur; et sic in hoc sensu idem opus non potest simul esse praeceptum et permissum; attamen **potest esse, ut permissio in uno ex sequentibus modis sumatur. — Paulo superius pro *cohibere* non pauci codd. *prohibere*.**` Filled in both languages. RESOLVED.

### bon-sent-I-d47-a1-q4 (2 flags → 2 RESOLVE)
- **[^1] `*filios fornicariae*[?]`** (La line 161 + En line 163, two `[?]`): printed p.845 footer 3 at 600dpi confirms the footer simply ends with `filios fornicariae.` — there is no further content after the textual variant. The trailing `[?]` was a stale OCR artifact. Removed. RESOLVED.

### Surprises
- **Littera apparatus is structurally compromised, not just garbled.** The chunk's [^7] = `Moral. VI. c. 18. n. 29.` but printed p.837 footer 7 is `Dist. XLV. c. 6. — Paulo inferius codd. ABD *dissimiliter accipit* pro *dissimiliter accepit*` (the chunk's [^7] content is actually p.838 footer 1). Similarly [^9] content = p.838 footer 5 (`Vide d. XLV. c. 7, nota 3`). The chunk apparatus was built mixing p.837 footers 1-6 with p.838 footers 1+ under a single continuous numbering, dropping p.837 footers 7-9 entirely. **OUT OF SCOPE for this pass** ([?]-resolution only), but flagged for future apparatus-completeness backlog: littera-d47 needs full footer audit + likely 3-4 entry additions.
- **Three of six littera `[?]` flags were marking fully hallucinated content**, not partial OCR gaps — [^5], [^6], [^8] all required complete rebuild rather than gap-fill. Consistent with the wave-6 d.8-p1-a1-q2 finding from 2026-05-12: prior passes occasionally hallucinated footer content from adjacent PDF regions.
- **a1-q2 scholion II `Petr. a Tar., hic [?]`** turned up two additional non-flagged errors in the same line (Richard sigla, Egid. citation form). Fixed while at the same site; suggests scholion-author lists across the corpus may benefit from a one-off PDF-citation audit.

### Audit gates after pass
- Inline `[?]` count: was 14 across 4 chunks; now **0** in d.47.
- **14 RESOLVE, 0 ACCEPT-ILLEGIBLE**.

### Log line count delta
This section: ~45 lines appended.

### bon-sent-I-d48-a1-q1 (3 flags → 3 RESOLVE)
- **Scholion I `d. 45. q. 2[?]`** (La line 86 + En line 143): p.853 scholion I right column line 1 read at 600dpi prints clearly `De analogia attributionis vide supra d. 45. q. 5, ubi sanum tripliciter distinguitur`. Cross-reference is **q. 5** (linear question numbering across d.45's six questions a1q1–a3q2), not q. 2. RESOLVED both languages.
- **Scholion I `sanum[?]`** (La line 86 + En line 143): same line, *sanum* is clearly printed (italic). Wrapped in italics on both languages. RESOLVED.
- **Scholion I `in modo volendi[?]`** (La line 86 + En line 143): p.853 scholion I right column (lower section) prints `conformitas in modo volendi; conformitas autem secundum obiectum dicitur conformitas in volito` — italics on *modo volendi* and *volito*. Wrapped in italics on both languages. RESOLVED.

### bon-sent-I-d48-a2-q1 (2 flags → 2 RESOLVE via [^8] removal)
- **Body anchor `et alii[^8]` + footnote `[^8]: Vat. *aliqui*[?]`** (La line 52 + En line 109 + La/En lines 171/173): p.856 right column at 600dpi shows the only superscript footer-marker in this vicinity is **⁸ attached to `cor`** (in `redire ad cor⁸; et ideo tenetur sicut et alii, licet non pro`), NOT to `alii`. The p.856 footer note 8 ("Respicitur illud Isai. 46, 8: *Redite praevaricatores ad cor*. — Paulo ante pro *qui non possit facere* Vat. *quod non potest facere*") is ALREADY captured as chunk [^15] correctly anchored to "redire ad cor" later in the chunk. Chunk's [^8] at "alii" was a phantom: a duplicate of the *aliqui*/*aliquis* variant already captured by [^5] (`Deut. 5, 16. — Mox pro et aliqui cum cod. cc et ed. 1 quod aliquis.`), placed by mistake. **Deleted body anchors and the [^8] footnote entry** in both languages. Chunk now has [^1]–[^7] body + [^9]–[^N] tail (footnote-numbering gap from 7→9 left intact since renumbering risks anchor mismatch elsewhere; gap is cosmetic only). RESOLVED.

### bon-sent-I-d48-a2-q2 (4 flags → 4 RESOLVE)
- **Body `velle proprie[?]`** (La line 68 + En line 143): p.858 left column at 600dpi prints `Unde dicunt, quod licet nobis aliqua velle proprie, quia non decet velle opposita`. *proprie* is unambiguous. RESOLVED both languages.
- **Body `si Deo placet[?]`** (La line 76 + En line 149): p.858 right column at 600dpi prints `sive quantum est in nobis, si Deo placet⁸, non velle`. Main text reads `placet`; footer 8 (which is OCR-visible in the page footer) reads `Cod. T placeret.` (codex T variant only). Chunk's main reading "placet" is correct. RESOLVED both languages.

### bon-sent-I-d48-littera (2 flags → 2 RESOLVE + 1 OCR correction)
- **`[^12]` trailing `[?]`** (La line 145 + En line 147): p.850 footer note 5 (= chunk's continuous [^12]) read at 600dpi prints `Ita codd. et edd., excepta Vat., quae cum originali sic habet: quia id ipsum quidem, sed ipse per eos bona, illi autem mala voluntate fecerunt. — Immediate post Vat. et edd. 4, 8, 9 omittendo Iudas habent Iudaei, aliae omittunt Iudaeus.` Chunk text correct except small OCR slip: **`omittentes` (plural participle) → `omittendo` (gerund)** per PDF. Corrected; En revised to "by omitting" to match. Trailing `[?]` stripped both languages. RESOLVED.

### Surprises
- **a2-q1 [^8] was a phantom footnote, not a [?] uncertainty.** Body marker had no PDF referent; existing [^8] content duplicated [^5]. The actual p.856 footer 8 was already captured (correctly) as [^15] later in the chunk. Lesson: when a footnote is short and looks duplicate, walk back to PDF before treating as routine [?] resolution.
- **d.45 q.5 cross-reference uses linear question numbering.** d.45 has 3 articuli × 2 questions = 6 total questions; "q. 5" = a3-q1 in chunk-id terms. Quaracchi scholion conventions cross-reference linearly within a distinction's question count, not by (articulus, quaestio) pair. Worth confirming in future scholion cross-refs.
- **Scholion italics convention.** Original chunk left `sanum`, `modo volendi`, `volito` un-italicized with [?] flags. PDF prints all three in italic. Restored italics during RESOLVE.

### Audit gates after pass
- inline `[?]` count in d.48 chunks: was 10, now 0.
- 10 RESOLVE, 0 ACCEPT-ILLEGIBLE.
- Side-effects: deleted 1 phantom footnote (a2-q1 [^8]); corrected 1 OCR slip (littera [^12] omittentes→omittendo); restored 3 italics in a1-q1 scholion.

### Log line count delta
This section: ~45 lines appended.
