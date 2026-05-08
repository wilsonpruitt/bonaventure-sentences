# d.38 scaffolds sweep audit log

**Date**: 2026-05-08
**Scope**: re-audit `vol1/bon-sent-I-d38-{littera, divisio, dubia}.md` after the 2026-05-07 [?]-pass polish-audit and same-day d.38-dubia rebuild (commit `b96626c`).

Per the dispatcher brief: dubia is verify-only (do not re-rebuild); littera + divisio get full body + apparatus diff against raw OCR pt2.

## Anchor / def pairing (programmatic)

| Chunk | Apparatus defs | Body anchors (Latin) | Body anchors (English) | Status |
|---|---|---|---|---|
| d38-littera | 8 | 1×{1..8} | 1×{1..8} | clean |
| d38-divisio | 3 | 1×{1..3} | 1×{1..3} | clean |
| d38-dubia | 13 | 1×{1..13} | 1×{1..13} | clean |

All anchors paired correctly across Latin/English; no orphan defs; no orphan anchors.

## Per-chunk verdicts

### d38-littera — VERDICT: CORRECTED

- **Body diff vs raw OCR pt2 lines 24851–25069**: line-by-line walk shows no silent dropouts. Cap. I and Cap. II both transcribed in full. Page-break placement (`<!-- page 668 -->`) lands at the right semantic boundary (after "non decedit aliquid vel succedit scientiae Dei").
- **Header count**: chunk has `### DISTINCTIO XXXVIII.`, `#### Cap. I.`, `#### Cap. II.` — all three appear in raw OCR (lines 24851, 24859, 25023). ✓
- **Apparatus**: all 8 entries verbatim from OCR footer bands at lines 24898–24910 (p.667 footer) and 25024–25037 (p.668 footer). ✓
- **Marker placement audit**:
  - `[^1]` Supra → matches OCR ` ' ` after *Supra* ✓
  - `[^2]` praeteritis → **was misplaced after *futuris*; fixed to after *praeteritis*** in both Latin and English. The OCR superscript (`%`-glyph) sits directly after `praeteritis`, and the apparatus's `non bene futuris` variant is anchored on the disputed word `praeteritis` (some codd. wrongly read `futuris` for `praeteritis` here).
  - `[^3]` de Trinitate → matches OCR `'` after *Trinitate* ✓
  - `[^4]` Ecclesiastico → matches OCR `*` after *Ecclesiastico* ✓
  - `[^5]` sexto libro → matches OCR `''` after *libro* ✓
  - `[^6]` penderet → OCR shows `'` after *praescientia*, not after *penderet*. Retained current pegging (after *penderet*) on logical grounds — apparatus 6 governs the *dependeret/penderet* variant. Flagged in `tier2-ambiguities-d38-littera.md` for a future eyes-on PDF check.
  - `[^7]` ad Romanos → matches OCR `"` after *Romanos* ✓
  - `[^8]` fieret → matches OCR `^` after *fieret* ✓
- **Backup**: `vol1/_backup-d38-littera-pre-rebuild-20260508/bon-sent-I-d38-littera.md` (pre-fix snapshot from HEAD).
- **transcription_status**: extended with 2026-05-08 audit note.
- **Existing [?] flags retained**: trailing `sine qua non` punctuation; stray `^` glyph at `non esset praescitum` Cap. II tail. Both deferred to decade-polish PDF pass.

### d38-divisio — VERDICT: PASS-AS-IS (annotation update only)

- **Body diff vs raw OCR pt2 lines 25070–25146**: line-by-line walk shows no silent dropouts. The `Commentarius in Distinctionem XXXVIII / DIVISIO TEXTUS / TRACTATIO QUAESTIONUM` structure is reproduced exactly.
- **Header count**: 4/4 (commentarius header, sub-title `*De divinae praescientiae causalitate, infallibilitate et necessitate.*`, `### Divisio textus.`, `### Tractatio quaestionum.`) all match raw OCR. ✓
- **Apparatus**: 3/3 entries match the `NOTAE AD COMMENTARIUM` footer block at raw lines ~25144–25146. Entry [^3] (`Supple cum Vat. infra distinct. 39:`) is genuinely truncated in the source — its continuation is a cross-reference into d.39's apparatus. Trailing colon retained verbatim per OCR.
- **No edits to body or apparatus made.**
- **transcription_status**: extended with 2026-05-08 audit note.
- **Existing [?] flags retained**: footnote 2 variant truncation; [^2] body position at *In prima*. Both deferred to decade-polish PDF pass.

### d38-dubia — VERDICT: VERIFY-ONLY PASS

Per dispatch instructions, do NOT re-rebuild this chunk (rebuilt today, prior session). Verification only:

- **Parses cleanly**: 13 apparatus defs, 13 unique body anchors in Latin, 13 unique body anchors in English, all paired 1:1.
- **Header structure**: 4 `#### DUB.` sections in both Latin and English (DUB. I–IV / DOUBT I–IV), bracketed by `### DUBIA CIRCA LITTERAM MAGISTRI.` / `### DOUBTS CONCERNING THE TEXT OF THE MASTER.`. Symmetric. ✓
- **Note**: dispatch brief mentioned "32 apparatus entries" and "DUB V tail + DUB VIII insinuatur→innuitur" fixes. The chunk on disk has 13 entries and 4 DUB sections, which matches the d.38-dubia raw OCR span (lines 26274–26376) — the d.38 dubia in Quaracchi has only 4 DUB. The "32" / "DUB V" / "DUB VIII" references in the brief appear to belong to a different chunk's rebuild (e.g. d.2-dubia, which was the actual subject of commit `b96626c` per `git log`). No action.
- **No edits made.**

## Smoke-test build

Run at end of audit. See bottom of log.

## Totals

- Chunks audited: 3 (littera, divisio, dubia)
- Substantive body fixes: 1 (littera `[^2]` marker repositioning, both Latin + English)
- Apparatus rebuilds: 0
- New [?] flags raised: 0 (one new logged-but-not-acted observation in tier2-ambiguities-d38-littera.md re: `[^6]` OCR position vs logical position)
- Pre-existing [?] flags resolved: 0 (all deferred to decade-polish)
- Backups created: 1 (`_backup-d38-littera-pre-rebuild-20260508/`)
- Anomalies: dispatch brief's "32 apparatus / DUB V / DUB VIII" references appear to describe a different chunk; d.38-dubia has 13 entries / 4 DUB. Verified clean as-is.

## Smoke-test

`cd site && node scripts/build-content.mjs` →
```
Built content.json: 1 book(s), 422 questions, 350 translated
```
Clean build. No parse errors raised by the d.38 chunks.
