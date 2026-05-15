# Tier-2 ambiguities — Vol II, d.1, p.2, divisio

*Commentarius in Distinctionem I. Pars II — Divisio textus et Tractatio quaestionum.* (pp. 38–39)

Promotion date: 2026-05-15.

## Cross-chunk apparatus correction (resolved this session)

The printed-page-38 footer carries 8 Quaracchi notes. The body that page 38 footnotes splits across two chunks:

- **Notes 1–6 → `bon-sent-II-d1-p1-dubia`** (DUB III tail / DUB IV / DUB V). The original p1-dubia promotion (2026-05-13) captured pp. 36–37 footer only and left the page-38 footer unworked, though the page-38 *body* was present and anchor-free. Backfilled this session as p1-dubia entries 16–21 by content match:
  - note 1 → *in Physicis* ([^16]) — the long privatio / *facto esse* vs *fieri* editorial note
  - note 4 → *privatio non differt a forma* ([^17]) — Albert/Aquinas three-principles *Notandum*
  - note 2 → *materia et specie* ([^18]) — Greek μορφή; Cod. L / cc variants
  - note 3 → *determinat in primo* ([^19]) — *Subaudi: libro Physicorum*
  - note 5 → *in secundo die* ([^20]) — Gen. 1, 6-8
  - note 6 → *malum culpae* ([^21]) — *Cfr. infra d. 2. p. I. a. 2. q. 1.*
- **Notes 7–8 → this chunk** (rendered renumbered 1–2): note 7 (*Vide infra d. 36. a. 3. q. 1.*) at *In prima*; note 8 (*In Vat. … quare rationalis creatura facta sit*) at the Master's lemma *quare sit creatus homo*.

This is the same cross-chunk-footer pattern already documented for `bon-sent-II-d1-p1-divisio` (its notes 1–4 physically sit in the next chunk's footer).

## Open flags (carried to d.10 polish-blocker)

- **Note-7 anchor (the `*` at *In prima*).** In the OCR the marker is an isolated `*`; in Quaracchi divisio diagrams `*` is sometimes a brace/diagram reference rather than a footnote marker. Note 7 (*Vide infra d. 36. a. 3. q. 1.*) is mapped here by position; the anchor identity is provisional. Inline `[?]` placed in the chunk at [^1]. Resolution path: `python3.11 tools/extract-pages.py --volume vol2 --pages 38 --dpi 600` (printed p. 38 = PDF p. 60) and eyes-on the footer/diagram region.
- **Note-6/7/8 boundary.** The split of the 8 page-38 notes into the 1–6 / 7–8 groups rests on content match through two-column OCR linearization; notes 6 (*Cfr. infra d. 2…*) and 7 (*Vide infra d. 36…*) are short forward cross-refs whose exact body anchors are the least certain in the block. Confirm at the same 600 dpi pass.
- **`in octavo` (in p1-dubia).** Stray `\` glyph after *motorem primum, in octavo* (raw line 3308) with no distinct page-38 footer note; treated as covered by note 3's *Subaudi: libro Physicorum* ellipsis ([^19] there). Confirm at 600 dpi.

## Resolved

- Page-38 footer cross-chunk split (see above) — applied this session; the residual uncertainties are the position flags listed under Open flags.
