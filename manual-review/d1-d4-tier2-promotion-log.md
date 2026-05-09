# d.1-d.4 Tier-2 Promotion Log (Task 9)

Tracking the multi-wave Tier-2 promotion of d.1-d.4 chunks. Cross-references resolution patterns from `d1-d11-pdf-supplement-resolution-log.md` (Task 6).

## Wave 1 — 2026-05-09 (mechanical bookkeeping + cross-reference fix)

### What shipped

1. **17 d.3-d.4 line-bounds backfilled.** All chunks the formatting audit flagged with `missing required keys: ['line_end', 'line_start']` now carry the fields. Ranges located by grepping `raw/bonaventure_vol1_raw.txt` for canonical structural headers (`DIVISIO TEXTUS`, `TRACTATIO QUAESTIONUM`, `ARTICULUS`, `QUAESTIO`, `DUB.`, `DUBIA`) and bracketing each chunk between adjacent markers. Tool: `tools/backfill-line-bounds-d3-d4.py` (one-shot script with hardcoded mappings; co-resident with `tools/backfill-line-bounds.py` for audit log). Spot-verified: `d4-a1-q1` `title_la` matches `raw[23584]` ("Utrum haec locutio: Deus genuit Deum…"). Formatting audit `missing required keys` count: 17 → 0.

2. **`d2-a1-q3` `[^6]` bilingual marker resolved.** The chunk is a deliberate cross-reference: printed Quaracchi anchors footer note 5 at two body positions in the same paragraph (after *omnes* and after *sed*), and the chunk rendered these as `[^5]` and `[^6]` with a single apparatus body under `[^5]`. The audit flagged `[^6]` as missing `**En.**`. Resolution: added a matching `**En.**` cross-reference line so both languages have explicit entries pointing at `[^5]`. Convention applied: parser-friendly bilingual structure preserved; the cross-reference semantics retained. Audit flag: cleared.

### Dispositions deferred to Wave 2 (NOT FIXED THIS WAVE)

The wave-1 mechanical pass surfaced apparatus-quality issues that need raw-OCR comparison + literal apparatus rebuild — apply the per-chunk Tier-2 recipe (CLAUDE.md), with the Task 6 lessons in mind (especially Lesson 1: page-split + per-page footer numbering; Lesson 5: `loc. cit.` / `ibid.` back-references preserved verbatim).

- **`d1-a3-q1` apparatus `[^13]`-`[^18]`** — 6 entries flagged missing both `**La.**` and `**En.**`. Inspection needed: are these stub `[^N]:` defs with no content, or body anchors with no def? Either way, rebuild from raw OCR (line range visible in chunk's existing `transcription_status`).

- **`d3-p1-dubia` apparatus** — audit-apparatus-count diff `+22` (raw=22, chunk=0). Status string honestly says "apparatus pending"; chunk needs full apparatus build from raw lines 20563-21005.

- **`d3-p2-a1-q3` apparatus** — diff `+22` (raw=28, chunk=6). Significant gap; rebuild from raw lines 21664-22244.

- **`d3-p2-dubia` apparatus** — diff `+7` (raw=11, chunk=4). Plus formatting WARN: "apparatus def with no marker: ['2', '3', '4']" — three orphaned apparatus defs without body anchors. Investigate orphans before rebuild.

- **`d3-p1-dubia` and `d3-p2-divisio` status strings** — both currently `"Phase C rebuild — …"` rather than `"Phase C Tier 2 complete — …"`. **Do not silently flip the prefix.** The current strings are honest admissions of incompleteness ("apparatus pending"); flipping would falsify per Lesson 2 (`## Notes` disclaimers = fabrication suspect, not soft TODO — same logic applies to status-string disclaimers). When the apparatus rebuild lands, update prefix as part of that change.

### Audit state at wave-1 close

| Audit | Pre | Post |
|---|---|---|
| `audit-formatting.py` missing-required-keys (d.1-d.4 scope) | 17 | 0 |
| `audit-formatting.py` apparatus-bilingual (d.1-d.4 scope) | `d2-a1-q3 [^6]`, `d1-a3-q1 [^13]–[^18]` | only `d1-a3-q1 [^13]–[^18]` (deferred to wave 2) |
| `audit-paraphrase.py` (full corpus) | 0 critical / 1 high | 0 critical / 1 high |
| `audit-headers.py --min-d 1 --max-d 4` | 0 flags | 0 flags |
| `audit-apparatus-count.py --min-d 1 --max-d 4` | 3 flagged | 3 flagged (deferred to wave 2) |

The 1 high in paraphrase is `d11-divisio` (pre-existing, not part of this arc).

### Lessons added (none new this wave)

Wave 1 was mechanical; the Task 6 lesson catalog covered every disposition encountered. New lessons (if any) will land in subsequent waves.

## Wave 2 — 2026-05-09 (apparatus format conversion on d1-a3-q1)

### What shipped

**`d1-a3-q1` apparatus format converted to parser-canonical bilingual.** All 18 entries used the legacy Tier-1 format `[^N]: **La** — <Latin><br>\n      **En** — <English>` (em-dash, no period after `La`/`En`, trailing `<br>`). The audit flagged all 18 as missing both `**La.**` and `**En.**`. The translations were already present and complete; the issue was purely formatting drift from the d.10+ corpus convention.

Conversion (three replace-all Edits):
1. `**La** — ` → `**La.** ` (period, drop em-dash)
2. `**En** — ` → `**En.** ` (same)
3. `<br>\n` → `\n` (drop legacy line-break tags)

Audit flag: 36 → 0 for `d1-a3-q1`. No translation work needed because the Tier-1 author had already done literal renderings — they just used a non-canonical wrapper.

**Lesson 7 (parser format drift, this session):** when the audit flags `apparatus [^N] missing **La.**` and `**En.**` on a chunk whose `transcription_status` claims `Phase C Tier 2 complete`, do not assume the translations are missing — first check the raw entry format. Tier-1-era format `**La** — ... <br>` parses as neither La nor En because the parser regex requires `**La.**` / `**En.**` (period). A purely mechanical replace-all clears it without touching content. Apply this lesson before opening a translation tool.

## Wave 3 — 2026-05-09 (d3-p2-dubia honesty pass)

### Finding

`d3-p2-dubia`'s 4 apparatus defs were a fabrication-via-omission pattern (same class as d9-a1-q4, Task 6 lesson 2):
- `[^1]` = Psalm 72:20 scripture citation properly anchored to body (legitimate).
- `[^2]`–`[^4]` = scholar's cross-references (Psalm 48:13 source for *homo cum in honore esset*; Augustine *de Trin.* X.10 on *essentia/vita/mens*; Priscian/Alan-of-Lille on the threefold genitive). Useful as scholar's commentary, but **not** from the printed Quaracchi apparatus.
- The 11 actual Quaracchi textual-variant footnotes on printed pp. 93–94 (visible in raw OCR lines 23056–23296: codex collations, *Vat. pro …* readings) were entirely missing from the chunk despite the status string claiming "Phase C Tier 2 — 4-footnote apparatus".

### Action taken

- Kept `[^1]` (legitimate scripture citation, anchored body marker).
- Moved `[^2]`–`[^4]` content to a new `## Notes` section as preserved scholar's commentary, with explicit "NOT part of the printed Quaracchi critical apparatus" framing — preserves the useful pointers without misrepresenting them.
- Inserted an Editor's note in the apparatus block flagging that the 11-entry Quaracchi rebuild is pending.
- Updated `transcription_status` from `Phase C Tier 2 —` to `Phase C partial —` (honest non-Tier-2 marker; auditor will warn about the unrecognized prefix, which is the correct signal).

### Audit deltas

- `audit-formatting`: removed 3 orphan-def WARN; added 1 unrecognized-prefix WARN (honest).
- `audit-apparatus-count`: chunk count 4 → 1; diff `+7` → `+10` (diff *grew* because the 3 orphan defs no longer mask the gap — this is the desired honest signal).
- Paraphrase audit and build both clean.

### Lesson 8 (fabrication-via-omission)

When `audit-apparatus-count` flags a chunk with chunk-count > 0 but a `+N` diff, do not assume the existing entries are correct. Spot-check whether they correspond to the printed Quaracchi footer markers in the raw OCR range. If the chunk's entries are scholar's cross-references (Augustine cites, Aristotle cites, scripture parallels) while the raw OCR footers are textual-variant notes (codex sigla, *Vat. pro …*, *Cod. X legit …*), the chunk is masking a missing apparatus with fabricated commentary — same pattern as d9-a1-q4. Disposition recipe: keep legitimate-anchored entries, move fabricated cross-refs to a `## Notes` section with explicit non-apparatus framing, downgrade status string to honest `Phase C partial —`, and queue the real apparatus rebuild.

## Wave 4+ — pending

Remaining d.1-d.4 audit findings (post-wave-3):

1. `d3-p2-a1-q3` apparatus-count diff `+22` (raw=28, chunk=6) — full apparatus rebuild from raw 21664-22244. Weight: large. Apply Lesson 8 first: spot-check whether the 6 existing entries are real Quaracchi or fabricated cross-refs.
2. `d3-p1-dubia` apparatus-count diff `+22` (raw=22, chunk=0); status string honestly says "apparatus pending" — full build from raw 20563-21005. Weight: large.
3. `d3-p2-dubia` apparatus-count diff `+10` (raw=11, chunk=1) — 10 entries pending from raw 23056-23296. Status string already honest as `Phase C partial`. Weight: medium.
4. `d3-p1-dubia` and `d3-p2-divisio` status strings still `"Phase C rebuild — …"` (honest non-Tier-2). Update the prefix only when the apparatus actually lands.
5. Optional: sample-Tier-2 verification on one already-Tier-2-claimed d.3/d.4 chunk per Task 6 protocol (600 dpi PDF diff vs chunk; look for fabrication).

After wave 4+ closes, re-baseline the audits and confirm formatting + apparatus-count both clean for d.1-d.4 before proceeding to Task 10 (d.5-d.11).
