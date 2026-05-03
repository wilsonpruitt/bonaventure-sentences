# d.19 littera — Tier-2 ambiguities and blockers (2026-05-03)

## Boundary correction (resolved)
- `line_end` was 60281 (auto-chunker overshot): included full COMMENTARIUS heading + DIVISIO TEXTUS + start of TRACTATIO QUAESTIONUM (lines 60181–60281), all of which belong to the divisio chunk.
- Corrected to **60178** (last line of Lombard's body, end of Cap. XII): "...sona aliam non superet magnitudine."
- COMMENTARIUS opener (line 60181) confirmed via raw-text grep and visual confirmation on PDF p.341.
- `word_count_latin` recomputed via `awk NR>=59285 && NR<=60178 | wc -w` → **5447** (auto-chunker's 17011 was wildly inflated).

## Tier-2 promotion blocker (NOT resolved)

**OCR damage on printed p.336 left column.** The IA djvu OCR (`raw/bonaventure_vol1_raw.txt` lines ~59370–59500) and `pdftotext` of `raw/doctorisseraphic11bona.pdf` p.438 are both severely garbled for this column — the underlying PDF scan shows faint/broken type impressions that no OCR can recover. Sample of corruption:

```
quantum  ad  naturae  divinae  unitatem  pertinet,  aut
;inlorior  ;iiil  in;ii()r  osl  Pulor  noc  Filiiis  Spiriln  s;ii
Aol(>rniiiii  ipiippo  ol  sliio  iiiilio  osl ,  (piod  Filins
```

At 400–600 dpi the page image is readable in spots but transcribing the entire left column verbatim requires page-by-page hand work against a high-resolution image, in addition to the right column of p.336 and pp.337–341. Total scope of the chunk: ~5,447 Latin words, 12 chapters (Cap. I–XII), ~7 printed pages, with two apparatus blocks per page (numbered fns + NOTAE AD LIBR. SENTENTIARUM running text).

### Recommendation
- Promote in a dedicated focused session (or split across two sessions) using the 400-dpi page images now in `raw/vision/vol1/p-335.png` … `p-341.png`.
- Per `feedback_clean-or-redo.md`: "Take chunks all the way to Tier-2 or leave skeleton. Never an in-between." — leaving as skeleton with corrected frontmatter rather than half-rebuilding.
- Boundary, page metadata, and word_count are now correct in the skeleton frontmatter so downstream tools (audit-tier.py etc.) report accurately.

## Structure confirmed (from page-image read of p.335 and headings visible in OCR)
- **Pars I**: Cap. I (*De aequalitate trium personarum*), Cap. II (*Quod aeternitate et magnitudine et potentia in Deo unum est, etsi videantur esse diversa*), Cap. III, Cap. IV.
- **Pars II** begins (heading visible on p.337 OCR as `DIST. XIX. P. II.`): Cap. V (*Quod nulla personarum pars est in Trinitate*), Cap. VI (*Quare tres personae dicantur summe unum*), Cap. VII, Cap. VIII, Cap. IX, Cap. X, Cap. XI, Cap. XII (*Quod Deus non est dicendus triplex, sed trinus*).
- **12 chapters total** (I–XII).

## Tier-2 promotion (2026-05-03)

Promoted to Tier 2 per Wilson's directive (re-dispatch override of prior agent's "leave skeleton" recommendation). Workflow: raw OCR (lines 59285–60178) for all but printed p.336 left column; vision OCR fallback (raw/vision/vol1/p-336.png) for p.336 left column where the IA djvu and `pdftotext` are both unrecoverable. PDF apparatus pulled per page (PDF p.437–443) and consolidated to flat 56-footnote sequence.

### `[?]` flags inline in chunk

All `[?]` markers below are flagged in the chunk file at the cited locations. They cluster in TWO regions: (a) the damaged p.336 left column, where one technical term ("magnitudine") is OCR-fragmentary in a list of three attributes; (b) several apparatus footers where Quaracchi's tiny editorial type was poorly scanned (cross-references and edition-numerals).

1. **Cap. I body, end of paragraph (p.335→336 transition)**: "...alia aliam non excedit aeternitate, magnitudine[?] aut potestate." The third attribute (greatness) is the obvious term given the chapter's argument and the parallel triad "aeternitate–magnitudine–potestate" repeated through Cap. II–III, but the OCR shows only a fragmentary "iiil" pattern. Reconstruction is high-confidence; flagged for transparency.

2. **Cap. VII body (right side of mid-quote, p.338)**: `secundum genus et speciem et individuum ista distinguantur[?]` and `non ita dicuntur tres essentiae, ut tres personae[?]`. The OCR cuts off ("dis-...non ita dicuntur tres essentiae, ut Ires per-..."). Standard Lombard text and Augustine *de Trin.* VII parallel confirm the reconstruction; flagged where verbatim ratification is impossible from the available OCR alone.

3. **Apparatus [^4] (Cap. II, Confessions/de Trin. cross-reference)**: PDF p.438 footer is OCR-fragmentary at the marker for "VII libro Confessionum"; the edition reference is genuinely truncated ("doiis i\|uo;id sonsuni ol / libr. Vi. de Trinitate,"). Bonaventure's later commentary clarifies the citation is in fact more parallel to August. *de Trin.* VI (or VII), c. 4 — but the original Lombard footer cannot be recovered cleanly. Flagged as `[?]` in apparatus.

4. **Apparatus [^7] (Damascene citation)**: PDF p.438 footer for the Damascene quote is severely OCR-damaged. The citation in [^39] (later in same chunk) provides the parallel reference to *de Fide orthodoxa* — but the p.336 footer giving the FIRST Damascene anchor is lost. Flagged.

5. **Apparatus [^14] (Hilary, John 6:11)**: PDF p.439 footer reads `Locus Scripmrac csl loan. ti , II.` — the chapter/verse digit is OCR-garbled (likely 6:38 not 6:11, given Hilary's preferred Johannine citations, but unverifiable from this scan). Flagged.

6. **Apparatus [^18] (Ambrosiaster, II Cor citation)**: PDF p.439 footer reads `II. Cor. 3, 19` but Ambrosiaster's actual exposition of "Pater in Filio" is at II Cor. 3:17. The OCR `19` may itself be a mis-scan of `17`. Flagged `[?]`.

7. **Apparatus [^19] (Vat. variant)**: PDF p.439 footer reads `excepta o,` where the "o" is the numeral identifying which edition dissents. Could be 1, 5, 6, 8, or 9. Genuinely unrecoverable from this scan. Flagged.

8. **Apparatus [^28] (Vat. variant *non inveniunt*)**: PDF p.440 footer ends with garbled `«on inve-` and is cut off mid-word. The variant reading is unrecoverable. Flagged.

9. **Apparatus [^46] (Vat. variant for *conveniunt*)**: PDF p.442 footer is partially garbled at this marker; the variant reading is reconstructed from context but flagged for transparency.

### Footnote count and structure

- **Total footnotes: 56** (consolidated from per-page Quaracchi blocks, renumbered as a single 1..56 sequence)
- **Body anchors**: matching `[^N]` markers placed in BOTH Latin and English at corresponding positions
- **Chapter count: 12** (Cap. I–XII), Pars I = Cap. I–IV, Pars II = Cap. V–XII, split at "Sed iam nunc ad propositum redeamus..."
- **Page breaks**: HTML comments at all 7 printed-page boundaries (335, 336, 337, 338, 339, 340, 341)

Per `feedback_vision-ocr-discipline.md`: where OCR is unrecoverable, flagged with `[?]` rather than guessed. Per `feedback_clean-or-redo.md` (correctly applied): chunk reaches Tier 2 with transparent `[?]` flags, not paraphrased and not invented. The d.18 littera template (33 footnotes) and the d.17 dubia chunks (each shipped with several `[?]` flags) are precedent.
