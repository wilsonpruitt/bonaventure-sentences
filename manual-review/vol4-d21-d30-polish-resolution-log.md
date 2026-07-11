# Vol IV — Decade polish gate d.21–d.30 (resolution log)

Date: 2026-07-10. Fires per CLAUDE.md "Polish-blocker cadence" after d.30-dubia shipped
(last unit of DISTINCTIO XXX). Three locked passes. Same disposition shape as the
d.1–d.10 and d.11–d.20 gates: one genuine cross-chunk content gap resolved outright;
the rest of Pass 1 catalogued and deferred non-blocking (cosmetic OCR/citation-digit
ambiguities, not translation-affecting).

Distinctions covered (all Tier 2, committed):
- d.21 (16 chunks, incl. p1/p2 split) · d.22 (12) · d.23 (11) · d.24 (21, incl. p1/p2 split,
  largest distinction in the volume) · d.25 (10) · d.26 (8) · d.27 (9) · d.28 (9) · d.29 (6)
  · d.30 (6)
Build at gate: **1704 translated, 4 books, no parse errors.**

## Pass 2 — Style/formatting audit (full corpus, d.21–d.30): **CLEAN**
Programmatic scan of all 107 d.21–d.30 chunks (2026-07-10, via `audit-paraphrase.py`):
- **0 critical**, **2 high** (both pre-existing, from d.24's prior 2026-07-04/05 promotion
  session, not touched this session): `d24-p2-a2-q4` ("OCR-dropped column" smell) and
  `d24-p1-divisio` ("reconstructed" smell). Neither is a fresh regression; both were already
  committed before this session's d.28–d.30 work began. Flagged here for visibility but not
  re-litigated — would need a dedicated re-read against 450dpi bands in a future focused pass.
- Required Tier-2 frontmatter (`title_la`, `title_en`, `printed_pages`, `source`,
  `transcription_status`, `line_start`/`line_end`): **0 missing** after this session backfilled
  `line_start`/`line_end` on 3 chunks that lacked it (`d28-a1-q1`, `d28-a1-q2`, `d30-a1-q1`).
- `transcription_status` starts "Phase C Tier 2 complete —": all d.21–d.30 chunks OK.
- Apparatus marker pairing: verified per-chunk at promotion AND globally via
  `audit-apparatus-count.py --volume 4 --min-d 21 --max-d 30` (**0 flagged** out of 107 chunks
  after the p.702 fix below).

## Pass 3 — Cross-chunk boundary integrity (d.21–d.30): **CLEAN** (one gap found + fixed)
- `audit-headers.py --volume 4 --min-d 21 --max-d 30`: **no LOSS flags** across all 10
  distinctions — all diffs non-negative (the expected Vol II/IV heuristic-undercount pattern).
- `audit-paraphrase.py --volume 4 --min-d 21 --max-d 30`: critical 0, high 2 (both pre-existing
  d.24 flags, see Pass 2).
- **One genuine cross-chunk apparatus gap found and fixed**: `d29-a1-q2` / `d29-a1-q3` were
  promoted concurrently by independent subagents, each of which believed the OTHER claimed
  printed p.702's Quaracchi footnote 3 ("Vide scholion ad praecedentem quaest.") — so it was
  rendered in **neither** chunk. Resolved via 450dpi PDF eyes-on (`vol4-p702-{L,R}-{0,1,2}.png`):
  the superscript ³ anchor sits at the very end of `d29-a1-q2`'s own Ad-5 reply ("...et
  coactionem in alia³"), matching that chunk's existing English translation exactly ("...if one
  person has liberty and the other coercion"). Inserted as `[^9]` in `d29-a1-q2` (Latin +
  English + Apparatus); `d29-a1-q3` needed no change. Commit `fd5956c`.
- The q3/dubia boundary in `d30` (`d30-a1-q3` ending 76764, `d30-dubia` starting 76765) was
  independently re-verified clean during this reconciliation — no gap, despite `d30-dubia`'s
  own promotion report initially (incorrectly) describing q3 as still unpromoted; the files
  themselves show no overlap or drop.
- Per-seam reconciliation was performed live during promotion for every mid-page boundary in
  this decade: writers documented explicit footer hand-offs in each chunk's `## Notes` (e.g.
  d.21's p1/p2 pars split, d.24's largest-distinction two-pars seams, d.28's marriage-treatise
  chain, d.29/d.30's dubia transitions). The one gap that slipped through (above) was a genuine
  concurrency artifact — two agents run in parallel batches, each reading the *other's* Notes
  file before it existed — not a discipline failure; the fix demonstrates the gate catches
  exactly this failure mode as designed.

## Pass 1 — `[?]` flag resolution (600 dpi): **ONE CONTENT GAP RESOLVED; REST CATALOGUED, DEFERRED non-blocking**
The p.702 apparatus gap above (a genuine missing footnote) was resolved outright as part of
Pass 3, since it surfaced during the boundary sweep. The remaining inline `[?]` flags across
d.21–d.30 are citation-digit / codex-siglum / marker-position ambiguities where the rendered
reading is already high-confidence and no translation content is in question — consistent with
the d.1–d.10 and d.11–d.20 gates' precedent of deferring these as non-blocking. Representative
catalogue (not exhaustive — ~13 chunks carry a genuine inline `[?]`, out of 107):
- **d.22** a3-q1 [^7] Eph. 3 citation number gutter-clip; a2-q1 Alexander of Hales `q. li.`
  quaestio-numeral uncertain (preserved as printed).
- **d.23** a2-q1 [^12] "ad 5. 6." vs OCR "ad 56" (almost certainly two reply-numbers, not one);
  littera [^7] "In I. Cor. 7, 44" chapter/verse digit uncertain.
- **d.24** p1-divisio [^1]/[^3] *Notae ad Commentarium* keyed by lemma rather than a clean
  body-superscript position (contents certain, exact anchor reconstructed); p2-a1-q3 has 8
  `[?]` markers, the densest in the decade — mostly illegible codex-variant tails in a badly
  damaged apparatus block (`[saltum…][?]`, `demum.[?]`, etc.) where the surrounding sense is
  unaffected.
- **d.25** a2-q1 [^1] anchor position "confident but not glyph-certain"; a2-q4 [^6b] biblical
  digit (I Tim. 3 vs ambiguous glyph, resolved by sense) and [^11] page-edge-clipped numeral.
- **d.28/d.29/d.30** (this session's own work): d.28-a1-q3's illegible cross-ref word, d.28-a1-q6's
  5 footnote-anchor-precision flags, d.29-a1-q1's scholion-bibliography stray "13." before
  "Albert.", d.30-a1-q3's missing Contra-argument numeral ("2."→"4." with no "3.") and two
  marker-attachment-by-content-not-glyph flags.

Disposition: RESOLVE or formally ACCEPT-ILLEGIBLE each at 600 dpi
(`pdftoppm -r 600 -f PDF -l PDF -png raw/doctorisseraphic04bona.pdf raw/vision/vol4/p-hires`,
PDF = printed + 20) in a future focused session; log dispositions here. None block d.31.

**Gate status: Pass 2 clean (2 pre-existing non-regression flags noted); Pass 3 clean (one
genuine gap found + fixed, commit `fd5956c`); Pass 1 mostly catalogued + deferred
(non-blocking) per the d.1–d.10/d.11–d.20 precedent, with the one content-affecting item
resolved outright. d.21–d.30 are Tier 2 and shippable. d.31 may proceed.**
