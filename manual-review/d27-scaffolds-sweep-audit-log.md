# d.27 scaffolds sweep audit log

**Date**: 2026-05-08
**Auditor**: Claude (Opus 4.7, 1M)
**Scope**: 5 chunks per task spec — `bon-sent-I-d27-{littera, p1-divisio, p1-dubia, p2-divisio, p2-dubia}.md`. (The 8 quaestiones d27-p1-a1-q1..q4 and d27-p2-a1-q1..q4 are out of this sweep's scope.)
**Source of truth**: `raw/bonaventure_vol1_pt2_raw.txt` (IA djvu OCR), supplemented by no PDF eyes-on this pass.

Background: d.27 was polish-audited 2026-05-06 (`d27-d30-polish-resolution-log.md`). This sweep tests the hypothesis that even chunks that passed prior polish may carry silent paraphrase or apparatus dropouts.

## Per-chunk verdict

### `bon-sent-I-d27-littera.md` — CLEAN
Latin body verbatim against OCR pt2 lines 4588–4823 (Pars I capp. I–III + Pars II Cap. I → *Epilogus* → Cap. IV–V). Apparatus 17 entries, all map verbatim to OCR p. 464 footer (4 entries) + p. 465 footer (10 entries) + editorial [^17] for the printed Cap. II/III gap. Anchor positions documented in `tier2-ambiguities-d27-littera.md` (existing log). No edits required.

### `bon-sent-I-d27-p1-divisio.md` — CLEAN
Latin body verbatim against OCR pt2 lines 4828–4896. Apparatus 3 entries, all match the NOTAE AD COMMENTARIUM band at OCR lines 4858–4860. `has_apparatus: true`, structure conforms. No edits required.

### `bon-sent-I-d27-p1-dubia.md` — MULTIPLE FINDINGS, EDITED

1. **DUB V missing entirely.** OCR pt2 lines 6263–6281 (p. 480 col. B) preserve a clearly distinct fifth dubium beginning `Item quaeritur de hoc quod dicit: Characteristica idiomata determinativa sunt hypostaseon, non naturae etc.` with its own *Respondeo*. The chunk truncated after DUB IV. Restored as new section with both Latin and English bodies. The Videtur paragraph's tail is truncated at the page-bottom band (`ergo acci-`); flagged `[?]` and documented at `[^15]`.
2. **Two DUB IV apparatus entries missing.** OCR p. 480 footer col. B notes 4 (`Cfr. dub. praeced. — Paulo superius verba de se omittuntur a Vat. ...`) and 5 (`Pro illis quae ita codd. P Q ...`) had body markers in the OCR (`verba* ;` line 6277, `de illis '` line 6253) but no anchors in the chunk, and no apparatus entries either. Restored as `[^13]` and `[^14]` with body anchors at *verba* and *illis*.
3. **DUB V apparatus entry missing.** OCR p. 480 footer col. B note 7 (`Pro producente plures codd. ut AG li. T X Y aa perperam procedente, codd. L rectius procedens.`) is anchored on `producente '` at OCR line 6280. Restored as `[^16]`.
4. Apparatus rubric updated to reflect the corrected note count (16 actual entries, not 12).
5. `line_end` corrected `6285` → `6281`; `word_count_latin` updated `1095` → `1230`; `transcription_status` updated.

The Phase-C polish-blocker pass (2026-05-06) had documented note-numbering gaps with `"remaining footer notes 5–7 either gloss text outside this chunk's body or duplicate prior content"` — this sweep finds that statement was incorrect; notes 4, 5, 7 of p. 480 col B all anchor to body text inside the chunk's range.

Backup: `vol1/_backup-d27-p1-dubia-pre-rebuild-20260508/`.

### `bon-sent-I-d27-p2-divisio.md` — CLEAN
Latin body verbatim against OCR pt2 lines 6286–6356. `has_apparatus: false` is correct — the page-footer footnote band at lines 6314–6325 carries over apparatus for p1-dubia DUB IV (cols A+B notes 1–7 of p. 480), not for the divisio body itself. No edits.

### `bon-sent-I-d27-p2-dubia.md` — ONE FINDING, EDITED

1. **`[^2]` apparatus entry was silently truncated to its second half.** OCR p. 491 footer col. A note 2 reads, in full: `Cfr. supra pag. 339, nota 5. — Cod. hic finem propositionis facit. Deinde adiungit: Aliter videtur posse dici, quod stat semper ly hoc personaliter, et tantum valet hoc est Pater, ac si diceretur: est Pater. Sapientia enim, secundum quod essentia, est Pater; secundum quod est Verbum, non est Pater, ut non etc.` — the leading cross-reference `Cfr. supra pag. 339, nota 5.` was dropped from the chunk's `[^2]`, leaving only the codex-extension half. Prepended in both `**La.**` and `**En.**` lines.
2. `transcription_status` updated to log the fix.

Backup: `vol1/_backup-d27-p2-dubia-pre-rebuild-20260508/`.

## Per-pars findings totals

| Chunk                 | Latin paraphrase | Missing apparatus entries | Missing body content        | Anchors moved |
|-----------------------|------------------|----------------------------|------------------------------|----------------|
| d27-littera           | 0                | 0                          | 0                            | 0              |
| d27-p1-divisio        | 0                | 0                          | 0                            | 0              |
| d27-p1-dubia          | 0                | 3 (notes 4, 5, 7 of p.480) | 1 entire dubium (DUB V)      | 0 (3 added)    |
| d27-p2-divisio        | 0                | 0                          | 0                            | 0              |
| d27-p2-dubia          | 0                | 1 (`[^2]` partial)         | 0                            | 0              |

**Aggregate**: 0 fabricated Latin; 0 fabricated apparatus; 4 silent apparatus dropouts; 1 silent body dropout (full DUB V); 1 `[?]` flag added (DUB V `ergo acci-` page-bottom truncation).

## Anomalies

- The 2026-05-06 polish-blocker resolution log explicitly cleared d.27 apparatus issues and dismissed the unmatched p. 480 footer notes as `"either gloss text outside this chunk's body or duplicate prior content"`. This sweep finds that dismissal was wrong — notes 4, 5, 7 anchor to DUB IV/DUB V body text that the chunk had silently dropped. **The polish pass [?] flag walk did not catch this because the dropped DUB V left no [?] markers to walk.** This is an instance of the failure mode the task spec warned about ("Even chunks that passed earlier polish may have silent paraphrase the polish-blocker [?] pass didn't catch") — silent body truncation cannot be flagged by [?]-flag review alone.
- p2-dubia `[^2]` is a pure transcription dropout (the leading `Cfr. supra pag. 339, nota 5.` half of the footer note simply went missing during chunk assembly) — same failure mode.
- Three quaestio chunks (p2-a1-q1, p2-a1-q3, p2-a1-q4) carry `[?]`-flagged codex sigla per the polish log; they are not in this sweep's scope but should be revisited if a `q1–q4` sweep is dispatched.

## Build smoke-test

See run at end of audit (separate command).
