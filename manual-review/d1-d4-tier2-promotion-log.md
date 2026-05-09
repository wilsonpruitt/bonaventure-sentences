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

## Wave 2+ — pending

Targets in priority order (by audit signal strength):

1. `d3-p2-a1-q3` (diff +22, ARTICULUS I QUAESTIO III content) — full apparatus rebuild from raw 21664-22244.
2. `d3-p1-dubia` (diff +22, all 4 dubia of pars 1) — full apparatus from raw 20563-21005.
3. `d1-a3-q1` (6 missing entries) — rebuild `[^13]`-`[^18]` from raw OCR for d.1 a.3 q.1.
4. `d3-p2-dubia` (diff +7, plus 3 orphaned def markers) — investigate orphans, rebuild from raw 23056-23296.
5. Optionally a sample-Tier-2 verification on a d.3 or d.4 already-Tier-2-claimed chunk (per Task 6 protocol): pick one at random, 600 dpi PDF diff against the chunk, look for fabrication. d9-a1-q4 caught wholesale fabrication this way.

After wave 2 closes, re-baseline the audits and confirm formatting + apparatus-count both clean for d.1-d.4 before proceeding to Task 10 (d.5-d.11).
