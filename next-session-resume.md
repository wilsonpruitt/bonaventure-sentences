# Next session — Vol II d.1 Tier-2 continuation (session 5)

Updated 2026-05-14 at close of session 4 (d.1 pars 1 COMPLETE).

Head commit: `42969f0` — Vol II d.1 Tier-2 session 4 (p1-a2-q1, p1-a2-q2, p1-a3-q1, p1-a3-q2, p1-dubia).

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
  - `d1-p1-dubia` *DUB I–V* (session 4)
- Site build: 2 books, 873 chunks, **420 translated**.
- No deploy. Wilson's policy: hold until Vol II has meaningful Tier-2 work to show.

## Open [?] flags parked for d.10 polish-blocker

- `d1-p1-a3-q1` [^21] (*vel inceptio* anchor on p. 33) — footer entry was not separately resolvable in OCR before the SCHOLION block; mapped by content match. Resolution: 600 dpi PDF extract of p. 33 and eyes-on. See `manual-review/tier2-ambiguities-II-d1-p1-a3-q1.md`.
- `d1-p1-a3-q2` — page-mapping in the apparatus crosswalk is approximate where two-column OCR linearization is ambiguous; per-footer content match is faithful, but per-page sequence numbers may be off by one in places.

## Next chunk: d1-p2-divisio

Chunk: `vol2/bon-sent-II-d1-p2-divisio.md`
Raw lines: **3330–3378** (~49 lines — very short, the divisio textus + Tractatio quaestionum opener for art. I of pars II).
Printed pages: probably 38 (the tail end, after DUB V of pars 1 closes) into early 39.
PDF pages: ~60–61 (offset +22).

Pars II of d.1 is *De multitudine, fine et distinctione creaturarum* — opens the topic of why there are many creatures, the end / ordering of creatures, and how they differ.

This divisio chunk has TWO sub-elements:
1. **DIVISIO TEXTUS** (raw lines 3330–3349 approx): exegetical breakdown of the Master's pars II text into three parts (*distinctio rerum*, *ordo*, *epilogus*) with sub-subdivisions tracking specific phrases the Master uses (*Ideoque, si quaeratur, quare sit creatus homo*; *Et sicut factus est homo propter Deum*; *De homine quoque in Scriptura*; *Ex praemissis apparet*).
2. **TRACTATIO QUAESTIONUM** (raw lines 3349–3378): the question-listing for art. I, with three principal questions (rerum distinctione / ordine / differentia Angeli et animae) and two sub-questions under the first (multiplicatione rerum quantum ad principium / quantum ad differentias).

Both elements together fit comfortably in one short session. After this, art. I q1 (`d1-p2-a1-q1`) begins at raw line 3381.

### Apparatus expected

Page 38 footer block (visible in OCR around lines 3354–3378) contains 8 footers — most pertain to the divisio textus body. Heavy editorial Schol-like note on Aristotle's three principles + Albert's / Aquinas's reading of it (footer 4), with cross-refs to several other doctors. Footers 5–7 are quick scripture / cross-references.

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
- **Watch for column-linearization page-spillover** — session 4 caught a "missing" page-30 footer that turned out to sit at the top of the next chunk's OCR window. Always glance at the next chunk's first ~20 lines if a footer reference seems short.
- **Vol II audit scripts not yet implemented**: `audit-paraphrase.py`, `audit-headers.py`, `audit-apparatus-count.py` still vol1-only. Manual confidence required for vol2 chunk quality until those scripts are extended. Smoke build (`build-content.mjs`) is the only mechanical check.

### Pace

- a2-q1, a2-q2, a3-q1, a3-q2, dubia all in session 4 (one extended session): demonstrated 5-chunk-per-session bundle is feasible when chunks are short-to-medium and apparatus is OCR-clean.
- `d1-p2-divisio` is small enough to bundle with `d1-p2-a1-q1` in session 5 if energy allows. (`d1-p2-a1-q1` raw lines 3381–~3550, ~170 lines — comfortably one focused session on its own.)

### Remaining d.1 pars 2 chunks (in order)

| Chunk | Lines | Notes |
|---|---|---|
| d1-p2-divisio | 3330–3378 | **next** — DIVISIO TEXTUS + TRACTATIO QUAESTIONUM for pars II |
| d1-p2-a1-q1 | 3381–~3550 | *Utrum a primo efficiente debuerit, vel potuerit esse rerum multitudo* |
| d1-p2-a1-q2 | ~3551–~3720 | |
| d1-p2-a2-q1 | ~3721–~3890 | |
| d1-p2-a2-q2 | ~3891–~4030 | |
| d1-p2-a3-q1 | ~4031–~4140 | |
| d1-p2-a3-q2 | ~4141–~4188 | |
| d1-p2-dubia | 4189–4263 | closes d.1 |

6 quaestiones + 1 divisio + 1 dubia remaining in d.1 pars 2 ⇒ ~7–8 more focused sessions to finish d.1 entirely (or fewer with bundling).

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
