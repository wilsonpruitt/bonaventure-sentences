# Next session — Vol II d.1 Tier-2 continuation (session 4)

Updated 2026-05-13 at close of session 3 (q2 promoted).

Head commit: `5191478` — Vol II d.1 Tier-2 session 3 (p1-a1-q2 world-eternity).

## Status

- Vol I COMPLETE (411/411 Tier-2).
- Vol II auto-chunked: 464 skeletons across d.1–d.44.
- Vol II d.1 promotions to date:
  - `d1-littera` (session 1, 2026-05-12)
  - `d1-p1-divisio` (session 1, 2026-05-12)
  - `d1-p1-a1-q1` (session 2, 2026-05-13) — *Utrum res habeant principium causale*. 6 fundamenta + 6 contra + conclusio + respondeo (4 historical positions: Eleatics/Xenophanes, Anaxagoras, Platonists, Peripatetics) + 6 solutiones + SCHOLION I–IV. 34 apparatus entries spanning pp.13–19. Ambiguities log: `manual-review/tier2-ambiguities-II-d1-p1-a1-q1.md`.
  - `d1-p1-a1-q2` (session 3, 2026-05-13) — *Utrum mundus productus sit ab aeterno, an ex tempore*. The world-eternity quaestio. 6 rationes Philosophi (2 a motu, 2 a tempore, 2 a parte causae producentis) + 6 fundamenta per se nota (infinity-addition, ordering, traversing, finite-virtus comprehending infinity, infinita simul, esse-post-non-esse) + conclusio + respondeo + 6 ad-arguments + Scholion I–IV. 51 apparatus entries spanning pp.19–24, chunk-internal renumbering with page crosswalk. Ambiguities log: `manual-review/tier2-ambiguities-II-d1-p1-a1-q2.md`.
- Site build: 2 books, 873 chunks, **415 translated**.
- No deploy. Wilson's policy: hold until Vol II has meaningful Tier-2 work to show.

## Open [?] flags from session 3 (parked for d.10 polish-blocker)

- `d1-p1-a1-q2`: codex-letter list at [^3] (raw `ni B E F H Iv V`, provisionally read as `B E F H K V` with `ni` left flagged); *potum / lutum* variant at [^49] (Vat. reads *lutum* "clay" where body has *potum* — possible Du Cange "vasculum vel poculum"). Resolution path: 600dpi extract of pp.19, 24 and eyes-on confirm. See `manual-review/tier2-ambiguities-II-d1-p1-a1-q2.md` for full disposition log.

## Next chunk: d1-p1-a2-q1

Chunk: `vol2/bon-sent-II-d1-p1-a2-q1.md`
Raw lines: 2420–2605 (~186 lines — about half the size of q1/q2)
Printed pp.: probably 24–27 (continues from where q2 ends mid-p.24; new ARTICULUS II opens with running head `DIST. 1. P. I. ART. II. QUAEST. I.` visible at raw line 2402).
PDF pp.: ~46–49 (offset +22).

This opens ART. II of P. I (still d.1). The thematic shift: from the *whether/when* of creation (ART. I: causal principle + temporal principle) to the *how/by whom*. ART. II quaestiones typically circle the agent-cause (Trinity as creator, Father-only vs. Father-Son-Spirit, the question whether creation is appropriable). Verify the actual quaestio title from raw OCR before drafting.

### Workflow per CLAUDE.md (locked-in)

1. Find OCR line range; verify boundaries against raw (`python3.11 tools/auto-chunk-volume.py 2 --dry-run`).
2. Latin verbatim from raw OCR, NOT from PDF.
3. `[^N]` anchors at OCR positions, not end-of-clause.
4. English literal, paragraph-for-paragraph.
5. Apparatus walked page-by-page from raw OCR footers; Quaracchi restarts numbering per page → chunk uses single sequence 1–N with crosswalk in Notes.
6. Log `[?]` flags inline; resolve at decade polish-blocker (d.10).
7. `node scripts/build-content.mjs` smoke-test before commit.

### Lessons confirmed by sessions 2–3 (apply forward)

- **Trim marginal glosses aggressively** (`Ad oppositum`, `Fundamenta`, `Conclusio`, `Solutio`, `Distinctio`, `Notandum`, `Alii aliter intelligunt Aristotelem`, etc.). Don't render them as headings; the structural divisions are surfaced via bold numbering and `### Conclusio` / `### Scholion` section headings only.
- **Apparatus marker renumbering is fine** — chunk-internal sequence 1–N is more readable than Quaracchi's per-page restart. Always document the page-by-page crosswalk in `## Notes`.
- **Page-break markers** go in the chunk at the printed-page running-head or page-number boundary; if OCR ate a running head, mark the `<!-- page N -->` position as `[?]` rather than guessing.
- **Don't try to resolve subtle OCR ambiguities eyes-on-OCR alone** — the d.10 polish pass + 600dpi PDF clears them in seconds.
- **Vol II audit scripts not yet implemented**: `audit-paraphrase.py`, `audit-headers.py`, `audit-apparatus-count.py` still vol1-only. `audit-formatting.py` audits 411 vol1 chunks but ignores `vol2/`. Manual confidence required for vol2 chunk quality until those scripts are extended. Smoke build (`build-content.mjs`) is the only mechanical check.

### Pace

- q1 (~350 lines, 6 fundamenta + 6 contra + scholion): one focused session.
- q2 (~392 lines, the world-eternity heavyweight, 6+6+Scholion I-IV): one focused session.
- q3 candidate is `d1-p1-a2-q1` at ~186 lines — comfortably one session, possibly with d1-p1-a2-q2 (~171 lines) bundled if energy allows.

### Remaining d.1 chunks after q3 (in order)

| Chunk | Lines | Notes |
|---|---|---|
| d1-p1-a2-q1 | 2420–2605 | **next** — opens ART. II of P. I |
| d1-p1-a2-q2 | 2606–2776 | |
| d1-p1-a3-q1 | 2785–2974 | |
| d1-p1-a3-q2 | 2975–3182 | |
| d1-p1-dubia | 3183–3329 | DUB. I–V |
| d1-p2-divisio | 3330–3378 | p2 commentary intro |
| d1-p2-a1-q1 … d1-p2-a3-q2 | 3382–4188 | 6 quaestiones |
| d1-p2-dubia | 4189–4263 | |

11 quaestiones + 2 dubia + 1 divisio remaining in d.1 ⇒ ~11 more sessions to finish d.1 alone.

## Polish-blocker (after d.10 ships)

1. `[?]` flag resolution — last 10 distinctions only (Vol II d.1–d.10 since this is Vol II's first decade).
2. Style/formatting audit — full corpus (Vol I + Vol II).
3. Resolution log at `manual-review/II-d1-d10-polish-resolution-log.md` (note `II-` prefix to distinguish from Vol I's d.1–d.10 log).

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
