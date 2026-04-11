# Opera Omnia Translation Plan

Roadmap for rendering St. Bonaventure's *Opera Omnia* (Quaracchi, Vols I–X) in
English using the unified-format pipeline established in this repo.

Last updated: 2026-04-11 (after commits `86ecefe` + `9df9f53`).

---

## Scope

| Vol | Work | Raw text | Legacy chunks | Unified-format rebuild |
|---|---|---|---|---|
| I | *Comm. in I Sent.* (d. 1–23) | ✅ `raw/bonaventure_vol1_raw.txt` | ✅ ~135 files (cleaned by `clean_latin.py`) | **6 of 135** |
| II | *Comm. in II Sent.* | ✅ `raw/bonaventure_vol2_raw.txt` | ❌ not chunked | — |
| III | *Comm. in III Sent.* | ✅ `raw/bonaventure_vol3_raw.txt` | ❌ not chunked | — |
| IV | *Comm. in IV Sent.* | ✅ `raw/bonaventure_vol4_raw.txt` | ❌ not chunked | — |
| V | *Opuscula I* (incl. *Breviloquium*, *Itinerarium*) | ❌ not downloaded | — | — |
| VI | *Opuscula II* | ❌ | — | — |
| VII | *Opuscula III* (incl. *Coll. in Hexaemeron*) | ❌ | — | — |
| VIII | *Opuscula IV* | ❌ | — | — |
| IX | *Sermones* | ❌ | — | — |
| X | *Indexes, dubia, fragments* | ❌ | — | — |

**Total remaining Vol I chunks to rebuild: 129.**

---

## Velocity baseline

Measured from the 2026-04-11 session:

- **~1 full unified-format chunk per session** at high quality
  (Latin vision OCR → Latin→English translation → apparatus translation +
  scholion + notes). Examples: `d1-a1-q3` (16 apparatus), `d1-a3-q1` (17
  apparatus), `d4-a1-q2` (17 apparatus).
- **~1 OCR-only chunk per session** at lower quality, flagged for vision
  verification. Example: `d3-p2-a2-q3` (6 apparatus).
- **A productive session** can do 3–4 chunks plus infrastructure work; the
  2026-04-11 session delivered 4 chunks + the entire reader-page upgrade +
  two commits. This is a *ceiling*, not a sustainable pace.

At ~1 chunk/session, 129 remaining Vol I chunks = 129 sessions. **Linear
work is not viable for the full Opera Omnia.** Pipeline automation is
required.

## The bottleneck

**Latin → English body translation is the only step that cannot be
automated without sacrificing quality.** All other steps can be scripted,
batched, or tool-assisted:

- Latin vision OCR: batch PDF read → page-by-page text dumps
- Apparatus translation: `tools/apparatus-translate.py` already at ~60%
  publication-ready; v2 will push to ~80%
- Chunk assembly: scaffolding script can pre-populate every section
  except `## English`
- Content pipeline: `site/scripts/build-content.mjs` handles backwards
  compatibility, so legacy and rebuilt chunks coexist indefinitely

---

## Phases

### Phase A — Finish Dist. 1 as a completeness showcase (next 1–2 sessions)

**Goal**: one complete distinction in the new unified format, top-to-bottom,
production-reviewable by partners.

Currently in unified format:
- ✅ `bon-sent-I-d1-littera.md`
- ✅ `bon-sent-I-d1-a1-q1.md`
- ✅ `bon-sent-I-d1-a1-q3.md`
- ✅ `bon-sent-I-d1-a3-q1.md`

Still to rebuild for Dist. 1:
- ⬜ `bon-sent-I-d1-a1-q2.md` — *Utrum contingat uti malis*
- ⬜ `bon-sent-I-d1-a2-q1.md` — *De utibili* (sole question of Art. 2)
- ⬜ `bon-sent-I-d1-a3-q2.md` — *Utrum frui sit actus voluntatis an aliarum virium* (or similar; to verify from title)
- ⬜ `bon-sent-I-d1-dubia.md` — Part I dubia

**Exit criterion**: all of Dist. 1 shows a green translated-dot on
`/browse/1` and reads cleanly in the reader.

### Phase B — Pipeline automation (interleaved with Phase A, 1–2 sessions)

**Goal**: make each subsequent distinction 3–5× faster to rebuild.

Concrete deliverables:

1. **Batch vision OCR script** (`tools/vision-ocr-batch.py`)
   - Input: PDF path + page range
   - Output: `raw/vision/vol1/p-NNN.txt` one file per printed page
   - Reads N pages per invocation, idempotent, skips already-captured pages
   - Runs in a single session to cover Vol I pp. 27–632 (printed) = ~600 pages

2. **Apparatus translator v2** (`tools/apparatus-translate.py` update)
   - Fix `De + [work]` title pattern (currently renders *De praedicamentis*
     → "Concerning praedicamentis")
   - Italicized-span protection (currently quoted variant readings leak)
   - Latin idiom handlers (*videri non debet* etc.)
   - Ablative-absolute pattern (currently renders *(with X) omitted*)
   - Target: 80% publication-ready, 15% good-with-issues, 5% manual

3. **Vol I sigla registry** (`tools/apparatus-sigla.json`)
   - Populate from Quaracchi Vol I prolegomena (codices A–cc, edd. 1–9, etc.)
   - Enables `<abbr>` tooltips in the reader
   - One focused session of data entry

4. **Chunk-scaffolding script** (`tools/build-chunk.py`)
   - Input: legacy chunk id (e.g. `bon-sent-I-d1-a1-q2`)
   - Reads the cleaned legacy Latin body + the vision-OCR'd PDF pages for
     that chunk's `printed_pages`
   - Produces a unified-format `.md` skeleton with:
     - Frontmatter populated from legacy metadata + page inference
     - `## Latin` with vision body + page-break comments + `[^N]` markers
       at apparatus positions
     - `## English` containing `[Translation pending]`
     - `## Apparatus` pre-populated via `apparatus-translate.py`
     - `## Notes` with a standard "transcription_status" note
   - **Reduces each rebuild to one step**: the Latin→English translation

### Phase C — Vol I completion (22 sessions, one distinction per session)

**Goal**: all of Vol I in unified format.

Cadence: one distinction per session. With the Phase B tooling, each
session's work is:

1. Run `build-chunk.py` across all chunks of distinction D (produces
   skeletons with translation-pending English)
2. Translate each chunk's `## English` section (the expensive step)
3. Review the auto-generated apparatus English, fix the ~20% that needs it
4. Verify scholion extraction
5. Commit the distinction as a single atomic unit

**Priority order within Vol I** (roughly by doctrinal density first, ease
second):

1. Dist. 2 (Trinity of persons) — the first "hard" distinction
2. Dist. 3 (image of God) — completes the d3-p2-a2 conflation cleanup too
3. Dist. 4 (supposition theory) — the `d4-a1-q1` chunk that today's
   `d4-a1-q2` scholion depends on
4. Dist. 5–7 (generation)
5. Dist. 8 (divine essence and simplicity)
6. Dist. 9–13 (procession of the Son)
7. Dist. 14–18 (procession of the Holy Spirit, gifts)
8. Dist. 19–23 (Trinity properties, appropriations, missions)

**Exit criterion**: 135/135 Vol I chunks in unified format, all rendering
with the new reader chrome. Vol I Book page fully green-dotted.

### Phase D — Vol II–IV (Sentences continuation)

**Goal**: the rest of Peter Lombard's *Sentences* commentary.

Prerequisite: Phase C must ship first so partner feedback has shaped the
translation quality bar.

Each Vol is roughly another ~135 chunks. At improved post-pipeline velocity
(estimate: 2× faster, so 1 distinction per 2 sessions on average, including
the initial chunking work), each Vol is ~45 sessions. **Vol II–IV together
= ~135 sessions** spread across months.

Open question: **should the pipeline be refactored to handle II–IV
chunking automatically**, or is one-time hand-chunking acceptable? The raw
text files exist but aren't split into distinction/article/question units.
Decision deferred to end of Phase C.

### Phase E — Opuscula & Collationes (Vols V–VIII), targeted by demand

**Goal**: famous standalone works translated on demand, not linearly.

Prerequisite: download Vol V–VIII PDFs from Internet Archive.

Priority order (based on demand, not page count):

1. **Vol V — *Itinerarium mentis in Deum*** (short, famous, constant demand)
2. **Vol V — *Breviloquium*** (systematic theology, moderate length)
3. **Vol VII — *Collationes in Hexaemeron*** (his last course, mature thought)
4. **Vol V — *Reductio artium ad theologiam*** (very short, influential)
5. Everything else as partners request

Each Opusculum is effectively a standalone sub-project. Short ones
(*Itinerarium*, *Reductio*) = 2–3 sessions; longer ones (*Breviloquium*,
*Hexaemeron*) = 5–10 sessions each.

### Phase F — Sermones & fragments (Vols IX–X)

**Goal**: lowest priority; touched only on direct partner request. Each
sermon is a self-contained unit and can be translated in isolation without
dependencies on earlier volumes.

---

## Quality tiers

To make the full Opera Omnia tractable, not every chunk needs to meet the
today-quality bar. Establish three tiers:

### Tier 1 — "Production" (today's rebuilt chunks)
- Full vision OCR of Latin
- Full English translation with bracketed supplements where needed
- All apparatus translated (manual polish on top of translator tool)
- Scholion translated
- Notes section explaining translation choices and flagged caveats
- `transcription_status`: "first-pass vision re-OCR, pending final verification"

### Tier 2 — "Reviewable" (for Phase C bulk rebuild)
- Vision OCR of Latin where available; raw OCR fallback acceptable
- Full English translation (this is always full quality)
- Apparatus translated via `apparatus-translate.py` with **no manual polish**
  of auto-translations flagged as confidence ≥ "good"; manual polish only
  for "needs-work" entries
- Scholion translated
- Notes section brief: chunk scope + "transcription_status: reviewable,
  automation-assisted apparatus"
- Partners can request a Tier 1 rebuild for specific chunks

### Tier 3 — "Draft" (for Phase D/E if velocity demands it)
- Raw OCR Latin, no vision pass
- English translation with explicit [verify] markers on uncertain passages
- Apparatus via tool only, no manual review
- Scholion optional
- `transcription_status: "draft, vision and review pending"`
- Flagged in reader with a visible "draft" indicator (TBD)

---

## Decisions deferred

1. **Tier 2/3 reader UI indicator** — should the reader show a small
   "draft" or "reviewable" badge next to chunk titles? Deferred until after
   partner feedback on Tier 1 chunks.

2. **Automated chunking for Vol II–IV** — one-time hand-chunking or build
   a chunker script? Depends on how well the legacy chunker performed vs.
   the effort to automate. Decision: end of Phase C.

3. **Vol V–X raw text extraction strategy** — `pdftotext`, OCR, or vision?
   Depends on PDF quality. Decision: at start of Phase E for the specific
   volume being targeted.

4. **Sub-agent parallelism for translation** — can a batch of 5–10
   translation agents fan out per distinction to parallelize the expensive
   step? Blocked on token-budget concerns (see `feedback_agent-token-accounting`
   in memory); probably viable post-Phase B once the scaffolding step makes
   each parallel task self-contained.

---

## Next session concrete plan

**Session goal**: finish Phase A — all of Dist. 1 in unified format.

Target chunks (4):
1. `bon-sent-I-d1-a1-q2` — *Utrum contingat uti malis*
2. `bon-sent-I-d1-a2-q1` — *De utibili* (or verify title from PDF)
3. `bon-sent-I-d1-a3-q2` — verify title from PDF
4. `bon-sent-I-d1-dubia` — Part I dubia

Workflow per chunk (established today):
1. Read cleaned legacy chunk for Latin body reference
2. PDF vision read for apparatus + scholion + page marker positioning
3. Translate Latin body → English (Tier 1 quality)
4. Translate apparatus → English (manual, since apparatus translator v2
   isn't built yet)
5. Translate scholion → English
6. Write unified-format file; verify with `node scripts/build-content.mjs`
7. Commit at end of session as "Complete Dist. 1 rebuild in unified format"

**Expected session output**: 4 new files in `vol1/`, 1 commit, Dist. 1
shows as fully green on `/browse/1`, all cards have English titles.

After Phase A ships, **Session N+2 is Phase B pipeline work** — not
another distinction rebuild. Critical to resist the temptation to keep
rebuilding manually; the automation unlocks everything that comes after.
