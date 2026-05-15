# Next session — Vol II d.1 Tier-2 continuation (session 6)

Updated 2026-05-15 at close of session 5 (d.1 p2-divisio done + p1-dubia page-38 apparatus backfill).

Head commit: `eee7f5f` — Vol II d.1 Tier-2 session 5 (p2-divisio + p1-dubia entries 16–21).

## Status

- Vol I COMPLETE (411/411 Tier-2).
- Vol II auto-chunked: 464 skeletons across d.1–d.44.
- Vol II d.1 pars 1 **COMPLETE** (9/9 chunks Tier-2):
  - `d1-littera` (session 1)
  - `d1-p1-divisio` (session 1)
  - `d1-p1-a1-q1` *causal principle* (session 2)
  - `d1-p1-a1-q2` *world-eternity* (session 3)
  - `d1-p1-a2-q1` *Manichaean dualism* (session 4)
  - `d1-p1-a2-q2` *immediate vs. mediated creation* (session 4)
  - `d1-p1-a3-q1` *creation as mutation* (session 4)
  - `d1-p1-a3-q2` *creation as medium* (session 4) — incl. Erigena/Council-of-Sens history
  - `d1-p1-dubia` *DUB I–V* (session 4; **page-38 apparatus backfilled session 5**, entries 16–21)
- Vol II d.1 pars 2 **IN PROGRESS** (1/8 chunks Tier-2):
  - `d1-p2-divisio` *Divisio textus + Tractatio quaestionum* (session 5)
- Site build: 2 books, 873 chunks, **421 translated**.
- No deploy. Wilson's policy: hold until Vol II has meaningful Tier-2 work to show.

## Open [?] flags parked for d.10 polish-blocker

- `d1-p1-a3-q1` [^21] (*vel inceptio* anchor on p. 33) — footer entry was not separately resolvable in OCR before the SCHOLION block; mapped by content match. Resolution: 600 dpi PDF extract of p. 33 and eyes-on. See `manual-review/tier2-ambiguities-II-d1-p1-a3-q1.md`.
- `d1-p1-a3-q2` — page-mapping in the apparatus crosswalk is approximate where two-column OCR linearization is ambiguous; per-footer content match is faithful, but per-page sequence numbers may be off by one in places.
- `d1-p2-divisio` [^1] — the page-38 footer note-7 anchor: OCR shows an isolated `*` at *In prima*, possibly a divisio-diagram brace rather than a footnote marker. Also the page-38 note-6/7/8 boundary (where the footer splits between p1-dubia and the divisio) rests on two-column content match. See `manual-review/tier2-ambiguities-II-d1-p2-divisio.md`.
- `d1-p1-dubia` *in octavo* — stray `\` OCR glyph after *motorem primum, in octavo* (raw 3308); no distinct page-38 note, treated as covered by note 3's *Subaudi: libro Physicorum* ([^19]). Confirm at 600 dpi (printed p. 38 = PDF p. 60).

## Next chunk: d1-p2-a1-q1

Chunk: `vol2/bon-sent-II-d1-p2-a1-q1.md`
Raw lines: **~3381–~3550** (ARTICULUS I, QUAESTIO I begins at raw 3382; *QUAESTIO I.* header line 3382, title line 3383).
Title (from raw 3383): *Utrum a primo efficiente debuerit, vel potuerit esse rerum multitudo* — "Whether from the first efficient [cause] there ought, or could, have been a multitude of things."
Printed pages: 39 (q1 starts mid-page 39) through ~40–41.
PDF pages: ~61–63 (offset +22).

Verify the `line_end` against the next semantic header (`QUAESTIO II.`) before translating — auto-chunker boundaries leak. The q1 arguments visible at raw 3385–3414 (Philosophus *idem uniformiter*; *quanto substantia spiritualior*; *quanto simplicior potentior*; *bonum diffusivum sui* Dionysius; Plato *Timaeus*) anchor the page-39 footer block at raw ~3415–3429 (running head `40 SENTENTIARUM LIB. II.` at line 3430 marks page 40).

### Apparatus note (carry forward — IMPORTANT)

Session 5 found that the **page-38 footer split across two chunks**: notes 1–6 belonged to `d1-p1-dubia` (which had only captured pp. 36–37 and left page-38 footer unworked despite holding page-38 body) and were backfilled there; notes 7–8 went to `d1-p2-divisio`. Before promoting q1, **check the page-39 footer is fully captured here and that no page-39 note actually anchors back into `d1-p2-divisio`'s page-39 tail** (divisio textus + tractatio occupy the top of page 39 before q1 starts). The recurring failure mode: a chunk that physically contains a footer block but whose body for that page is short, vs. a chunk whose body is on that page but whose promotion stopped at the prior page's footer.

### Workflow per CLAUDE.md (locked-in)

1. Find OCR line range; verify boundaries against raw.
2. Latin verbatim from raw OCR, NOT from PDF.
3. `[^N]` anchors at OCR positions, not end-of-clause.
4. English literal, paragraph-for-paragraph.
5. Apparatus walked page-by-page from raw OCR footers.
6. Log `[?]` flags inline; resolve at decade polish-blocker (d.10).
7. `node scripts/build-content.mjs` smoke-test before commit.

### Lessons confirmed by sessions 2–4 (carry forward)

- **Trim marginal glosses aggressively** (`Ad oppositum`, `Fundamenta`, `Conclusio`, `Solutio`, `Distinctio`, `Notandum`, `Triplex productio`, `Determinatio trium productionum`, `Epilogus`, `Dupliciter relatio`, `Aliter`, `Eliditur error 1/2/3`, etc.). Don't render them as headings or text.
- **Apparatus marker renumbering is fine** — chunk-internal sequence 1–N is more readable than Quaracchi's per-page restart. Document the page-by-page crosswalk in `## Notes`.
- **Page-break markers** go in the chunk at the printed-page running-head or page-number boundary; if OCR ate a running head, mark `<!-- page N -->` position as `[?]` rather than guessing.
- **Don't try to resolve subtle OCR ambiguities eyes-on-OCR alone** — the d.10 polish pass + 600dpi PDF clears them in seconds.
- **Watch for column-linearization page-spillover** — session 4 caught a "missing" page-30 footer at the top of the next chunk's OCR window. Always glance at the next chunk's first ~20 lines if a footer reference seems short.
- **Cross-chunk footer split is now a confirmed recurring pattern (session 5, page 38).** When a printed page's footer block sits at a chunk boundary, its notes split by *body anchor*, not by which chunk physically contains the footer text. Session 5: page-38 footer notes 1–6 anchored in `d1-p1-dubia`'s page-38 body (DUB III tail/IV/V) but that chunk had only captured pp. 36–37 footer; notes 7–8 anchored in `d1-p2-divisio`. **Before promoting any chunk, verify the prior chunk's last printed page footer was fully captured for the body it holds on that page.** Same convention as `d1-p1-divisio` (notes 1–4 in next chunk's footer). Backfilling a committed Tier-2 chunk is acceptable and expected when this is found — renumber its sequence continuously and document in its Notes + `transcription_status`.
- **Vol II audit scripts not yet implemented**: `audit-paraphrase.py`, `audit-headers.py`, `audit-apparatus-count.py` still vol1-only. Manual confidence required for vol2 chunk quality until those scripts are extended. Smoke build (`build-content.mjs`) is the only mechanical check.

### Pace

- Session 4: 5 short-to-medium chunks in one extended session when apparatus is OCR-clean.
- Session 5: 1 divisio chunk + a cross-chunk apparatus backfill (page-38 footer found mis-split). Cross-chunk corrections cost ~1 chunk-equivalent of effort — budget for them when a chunk boundary falls inside a printed page.
- `d1-p2-a1-q1` (raw ~3381–~3550, ~170 lines) is comfortably one focused session; the remaining 6 quaestiones are similar size and can bundle 2–3/session when footers are clean.

### Remaining d.1 pars 2 chunks (in order)

| Chunk | Lines | Notes |
|---|---|---|
| ~~d1-p2-divisio~~ | 3321–3378 | ✅ done session 5 (Tier-2) |
| d1-p2-a1-q1 | ~3381–~3550 | **next** — *Utrum a primo efficiente debuerit, vel potuerit esse rerum multitudo* |
| d1-p2-a1-q2 | ~3551–~3720 | verify boundary at next `QUAESTIO` header |
| d1-p2-a2-q1 | ~3721–~3890 | |
| d1-p2-a2-q2 | ~3891–~4030 | |
| d1-p2-a3-q1 | ~4031–~4140 | |
| d1-p2-a3-q2 | ~4141–~4188 | |
| d1-p2-dubia | 4189–4263 | closes d.1 |

6 quaestiones + 1 dubia remaining in d.1 pars 2 ⇒ ~3–5 more focused sessions to finish d.1 entirely (with 2–3/session bundling when footers are clean).

## Polish-blocker (after d.10 ships)

1. `[?]` flag resolution — Vol II d.1–d.10 only.
2. Style/formatting audit — full corpus (Vol I + Vol II).
3. Resolution log at `manual-review/II-d1-d10-polish-resolution-log.md`.

## Tools cheat sheet

```bash
# Inspect raw chunk range
awk 'NR>={start} && NR<={end}' raw/bonaventure_vol2_raw.txt

# Vol II offset: pdf_page = printed + 22
python3.11 tools/extract-pages.py --volume vol2 --pages {printed_pages}

# Chunker warnings
python3.11 tools/auto-chunk-volume.py 2 --dry-run 2>&1 | awk '/WARNINGS/,/Chunk list/'

# Smoke build
cd site && node scripts/build-content.mjs
```

Vol II offsets: see CLAUDE.md table (`pdf = printed + 22`). No deploy until meaningful Vol II Tier-2 work to show.
