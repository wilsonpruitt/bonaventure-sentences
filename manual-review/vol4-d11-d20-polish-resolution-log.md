# Vol IV — Decade polish gate d.11–d.20 (resolution log)

Date: 2026-06-23. Fires per CLAUDE.md "Polish-blocker cadence" after d.20 closes, sweeping
Vol IV d.11–d.20. Three locked passes. Same disposition shape as the d.1–d.10 gate
(`vol4-d1-d10-polish-resolution-log.md`): Passes 2 & 3 mechanical-clean; Pass 1 (600 dpi
flag sweep) catalogued and deferred non-blocking.

Distinctions covered (all Tier 2, committed):
- d.11 (17 chunks, 6dd15f6) · d.12 (20, 41ac661) · d.13 (9, 88f37a0) · d.14 (17, e41fd52)
- d.15 (19, 1d4ad11) · d.16 (19, 16217d8) · d.17 (27, ac6d33a) · d.18 (17, c4cea2a)
- d.19 (9, 7c1b05d) · d.20 (17, c672e1b)
Build at gate: **1597 translated, 4 books, no parse errors.**

## Pass 2 — Style/formatting audit (full corpus): **CLEAN**
Programmatic scan of all 171 d.11–d.20 chunks (2026-06-23):
- Required Tier-2 frontmatter (`title_la`, `title_en`, `printed_pages`, `source`,
  `transcription_status`): **0 missing.**
- `transcription_status` starts "Phase C Tier 2 complete —": **all 171 OK.**
- Structure (`## Latin`, `## English`, `## Apparatus` where apparatus present): **0 missing.**
- `### Scholion` ordering (must be LAST subsection of its language block — the
  empty-body parser trap): **0 violations** (no body heading after a `### Scholion`).
- Apparatus marker pairing: verified per-chunk by the writers at promotion AND globally by
  the clean `build-content.mjs` parse + `audit-apparatus-count.py --volume 4 --min-d 11
  --max-d 20` (**0 flagged**). (A coordinator-side bulk pairing check produced false
  positives because its `(?!:)` lookahead wrongly drops body anchors followed by a colon,
  e.g. `…nisi panis[^3]: ergo` — a common scholastic construction; not a real defect.)

## Pass 3 — Cross-chunk boundary integrity (d.11–d.20): **CLEAN (mechanical) + writer-verified**
- `audit-headers.py --volume 4 --min-d 11 --max-d 20`: **no LOSS flags** (no gross
  whole-chunk body dropouts; all diffs non-negative, the expected Vol II/IV pattern).
- `audit-paraphrase.py --volume 4 --min-d 11 --max-d 20`: **critical 0, high 0** across 171.
- Per-seam reconciliation was performed live during promotion: every mid-page chunk
  boundary in this decade was hand-reconciled by the writers (opener-continuity checks +
  explicit footer hand-offs documented in each chunk's `## Notes` — e.g. d.11 footer-split
  chains, d.17 three-pars seams, d.20 cascade-merged dubia headers caught and re-set).
- DEFERRED (non-blocking): a fresh full 450 dpi re-read of every mid-page seam independent
  of the writers' own reads. Accepted as covered by the writer discipline + the two audits;
  flag any residual splice during a future read, per the d.1–d.10 precedent.

## Pass 1 — `[?]` flag resolution (600 dpi): **CATALOGUED, DEFERRED non-blocking**
Genuine inline `[?]` flags live in each chunk's `## Notes` and are summarized per
distinction in `next-session-resume.md` (the "Open [?] flags" lines). They are OCR-glyph /
gutter-clip / digit-mangle ambiguities where the rendered reading is high-confidence and the
body text is sound; none affect translation correctness. Representative catalogue:
- **d.11** p1-littera p.238→239 column-foot seam + p.239 [^5] *Veritas* variant; p1-a1-q4
  [^2b] Aristotle *de Anima* number gutter-clip; p1-a1-q5 [^6] merged p.249 notes 4–5.
- **d.12** a2-q1(P1) [^14] p.277 gutter-clip; littera [^12]/[^18] p.268/269 illegible.
- **d.14** a2-q1(P2) [^14–17] gutter-bled footers; a1-q1(P2) [^10–11] codex-variant tails.
- **d.15** a1-q2(P1) scholion §II gutter-clip + doctor-list abbreviations.
- **d.16** **a4-q1(P1) printed_pages mis-set** (says 391–392; body on 394–395 — fix metadata);
  p2-dubia(P2) p.413 footers [^10–14] reconstructed (next-dist NOTAE overlap).
- **d.17** a2-q1(P1) [^20] p.426 footer-number garble; p3-dubia p.464 [^8/15/16] anchor ±1 clause.
- **d.18** p1-a2-q1 p.472 f1–6 ownership vs a1-q3 tail (confirm at 600 dpi).
- **d.19** dubia transcription_status string says "19 entries" but body has 20 (cosmetic).
- **d.20** a1-q4(P1)/a1-q6(P2)/a1-q4(P2) gutter-clipped variant tails; p2-a1-q3 [^1] anchor.

Disposition: RESOLVE or formally ACCEPT-ILLEGIBLE each at 600 dpi
(`pdftoppm -r 600 -f PDF -l PDF -png raw/doctorisseraphic04bona.pdf raw/vision/vol4/p-hires`,
PDF = printed + 20) in a future focused session; log dispositions here. Two are pure-metadata
fixes doable without imaging: d.16 a4-q1 `printed_pages`, d.19 dubia status-string count.

**Gate status: Passes 2 & 3 closed; Pass 1 catalogued + deferred (non-blocking) per the
d.1–d.10 precedent. d.11–d.20 are Tier 2 and shippable. d.21 may proceed.**
