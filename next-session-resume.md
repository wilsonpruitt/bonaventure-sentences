# Next session — Vol II d.1 Tier-2 continuation (session 3)

Updated 2026-05-13 at close of session 2 (q1 promoted).

Head commit: not yet committed — session 2 work (q1 promotion) is uncommitted on disk. **First action next session: decide whether to commit session 2 + session 1 together, or run audits first, then commit.**

## Status

- Vol I COMPLETE (411/411 Tier-2).
- Vol II auto-chunked: 464 skeletons across d.1–d.44.
- Vol II d.1 promotions to date:
  - `d1-littera` (session 1, 2026-05-12)
  - `d1-p1-divisio` (session 1, 2026-05-12)
  - `d1-p1-a1-q1` (session 2, 2026-05-13) — *Utrum res habeant principium causale*. 6 fundamenta + 6 contra + conclusio + respondeo (4 historical positions: Eleatics/Xenophanes, Anaxagoras, Platonists, Peripatetics) + 6 solutiones + SCHOLION I–IV. 34 apparatus entries spanning pp.13–19. Ambiguities log: `manual-review/tier2-ambiguities-II-d1-p1-a1-q1.md`.
- Site build: 2 books, 873 chunks, **414 translated**.
- No deploy. Wilson's policy: hold until Vol II has meaningful Tier-2 work to show.

## Open [?] flags from session 2 (parked for d.10 polish-blocker)

- `d1-p1-a1-q1`: 2 page-break positions (p.15, p.17 — OCR ate right-page running heads); Aristotle text-number 28 in [^12]; Plato Stephanus page 465 in [^13]; 3 Scholion-IV bibliographic entries (S. Thom. *de Potent.*, Durand., Dionys. Carth.). Resolution path: extract `vol2/p-hires-r600-pp.14-19` and eyes-on the column-break positions and footer text. See `manual-review/tier2-ambiguities-II-d1-p1-a1-q1.md` for the full disposition log.

## Next chunk: d1-p1-a1-q2

Chunk: `vol2/bon-sent-II-d1-p1-a1-q2.md`
Raw lines: 2019–2410 (~392 raw lines — the largest remaining chunk in d.1 p1)
Title: *Utrum res habeant principium initiale* — whether things have an initial principle (i.e., a temporal beginning vs. eternity of the world).
Printed pp.: probably 19–24 (continues from where q1 ends mid-p.19).
PDF pp.: ~41–46 (offset +22).

This is the *world-eternity* question — Bonaventure's most famous defense that the world cannot have been eternal. Expect 4–6 *ad oppositum a parte motus* arguments at the head, the classic Bonaventure infinity arguments in the respondeo (an actual infinity of revolutions is impossible; an infinite series cannot be traversed; etc.), and a substantial Scholion drawing parallels to *I Sent.* d. 1, *Itinerarium*, and the Thomistic *de Aeternitate mundi* tradition.

### Workflow per CLAUDE.md (locked-in)

1. Find OCR line range; verify boundaries against raw (look for footer-bleed; chunker emits warnings via `python3.11 tools/auto-chunk-volume.py 2 --dry-run`).
2. Latin verbatim from raw OCR, NOT from PDF.
3. `[^N]` anchors at OCR positions, not end-of-clause.
4. English literal, paragraph-for-paragraph.
5. Apparatus walked page-by-page from raw OCR footers; Quaracchi restarts numbering per page.
6. Log `[?]` flags inline; resolve at decade polish-blocker (d.10).
7. `node scripts/build-content.mjs` smoke-test before commit.

### Lesson from session 2 (don't repeat)

- **Trim marginal glosses aggressively**. q1 had ~10 bleeding marginalia (`Adoppositum.`, `Notandum.`, `Eo primus./Secundus./Tertius./Quartus.`, `Solutio I/II.`, `Ex nihilo intelligitur tripliciter.`, `De opinione Platonis.`, `conclusio est non solum etc.`). CLAUDE.md says trim them; don't render them as headings.
- **Apparatus marker renumbering is fine**. Chunk-internal sequence 1–N is more readable than Quaracchi's per-page restart. Document the crosswalk in Notes so the polish pass can verify.
- **When OCR eats a page running head**, mark the `<!-- page N -->` position as `[?]` rather than guessing precisely. The d.10 polish pass will resolve via 600dpi PDF.
- **OCR's `text. 28[?]` vs `text. 281` ambiguity** in [^12] is the kind of thing that the polish pass + PDF verification clears in seconds — don't try to resolve eyes-on-OCR alone.

### Pace

q1 took ~one focused session, end-to-end (one big Write of the whole chunk). q2 is comparable in size (~390 raw lines vs q1's ~350); plan ~one session. Wilson's policy: go slowly through d.10 manually before launching parallel agents.

### Remaining d.1 chunks after q2 (in order)

| Chunk | Lines | Notes |
|---|---|---|
| d1-p1-a1-q2 | 2019–2410 | *Utrum habeant principium initiale* (world-eternity) — **next** |
| d1-p1-a2-q1 | 2420–2605 | |
| d1-p1-a2-q2 | 2606–2776 | |
| d1-p1-a3-q1 | 2785–2974 | |
| d1-p1-a3-q2 | 2975–3182 | |
| d1-p1-dubia | 3183–3329 | DUB. I–V |
| d1-p2-divisio | 3330–3378 | p2 commentary intro |
| d1-p2-a1-q1 … d1-p2-a3-q2 | 3382–4188 | 6 quaestiones |
| d1-p2-dubia | 4189–4263 | |

12 quaestiones + 2 dubia + 1 divisio remaining in d.1 ⇒ ~13 more sessions to finish d.1 alone.

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
