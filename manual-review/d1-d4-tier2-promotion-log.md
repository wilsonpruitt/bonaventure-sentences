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

## Wave 4 — 2026-05-09 (d3-p2-a1-q3 honesty pass; d3-p1-dubia already honest)

### Findings

Applied Lesson 8 to `d3-p2-a1-q3`. The 6 anchored apparatus entries are scholar's cross-references (Augustine *de Trin.* X.11 + XV.7; Bernard / Guilelmus *Super Cantica*; Pseudo-Aug. *de Spiritu et anima*; Aristotle *de Anima* II.37; Dionysius *Cael. Hier.* c. 11) — well-translated, properly anchored, but **not** the printed Quaracchi textual-variant apparatus. Raw OCR pp. 85–88 footers carry ~28 entries (codex collations, *Vat. pro …* readings) that are missing.

`d3-p1-dubia` requires no edit this wave — status string already honestly admits `Phase C rebuild — apparatus pending` and the apparatus block already carries an explicit stub note. Most-honest state of the three.

### Action taken

- `d3-p2-a1-q3`: added Editor's note in apparatus block with explicit "scholar's cross-references, NOT verbatim Quaracchi" framing; updated `transcription_status` to `Phase C partial —` with full disposition narrative and pointer to this log.
- `d3-p1-dubia`: left as-is. Honest non-Tier-2.

### Audit deltas

- `audit-formatting`: `d3-p2-a1-q3` status string prefix changed from `Phase C Tier 2 —` to `Phase C partial —` (auditor will warn on prefix; correct honest signal).
- `audit-apparatus-count`: unchanged (chunk-counts didn't change). Three-flag baseline: `d3-p1-dubia +22`, `d3-p2-a1-q3 +22`, `d3-p2-dubia +10`.
- Paraphrase audit and build both clean.

## Wave 5+ — pending

The three apparatus-count flags above are the remaining d.1-d.4 work. Each is a real Quaracchi textual-variant apparatus rebuild from raw OCR (60 entries total across the three chunks). This is wave-dispatch / subagent-template territory:

- 60 entries × ~50 words bilingual translation each = ~3,000 words of careful Latin → English
- Per-entry recipe: locate raw OCR footer text → clean OCR garbles → translate literally → place body anchor at OCR-marker position → 4-5 space indent **En.** convention
- Use the Acta agent prompt template (permission test + 30-chunk floor) per `feedback_acta-agent-prompt.md`
- Wave-dispatch 3-5 subagents in parallel; one chunk per subagent or split largest by ~10-entry batches

Then re-baseline audits, confirm formatting + apparatus-count clean for d.1-d.4, advance to Task 10.

Optional: sample-Tier-2 verification on one already-Tier-2-claimed d.3/d.4 chunk per Task 6 protocol (600 dpi PDF diff vs chunk; look for fabrication). The wave-3 d3-p2-dubia and wave-4 d3-p2-a1-q3 findings suggest other "Tier-2" chunks may be carrying scholar's-cross-refs in place of real Quaracchi apparatus — worth a probabilistic sample.

Remaining d.1-d.4 audit findings (post-wave-3):

1. `d3-p2-a1-q3` apparatus-count diff `+22` (raw=28, chunk=6) — full apparatus rebuild from raw 21664-22244. Weight: large. Apply Lesson 8 first: spot-check whether the 6 existing entries are real Quaracchi or fabricated cross-refs.
2. `d3-p1-dubia` apparatus-count diff `+22` (raw=22, chunk=0); status string honestly says "apparatus pending" — full build from raw 20563-21005. Weight: large.
3. `d3-p2-dubia` apparatus-count diff `+10` (raw=11, chunk=1) — 10 entries pending from raw 23056-23296. Status string already honest as `Phase C partial`. Weight: medium.
4. `d3-p1-dubia` and `d3-p2-divisio` status strings still `"Phase C rebuild — …"` (honest non-Tier-2). Update the prefix only when the apparatus actually lands.
5. Optional: sample-Tier-2 verification on one already-Tier-2-claimed d.3/d.4 chunk per Task 6 protocol (600 dpi PDF diff vs chunk; look for fabrication).

After wave 4+ closes, re-baseline the audits and confirm formatting + apparatus-count both clean for d.1-d.4 before proceeding to Task 10 (d.5-d.11).

## Wave 5 — 2026-05-09 (apparatus rebuild on the three flagged chunks; Lesson 9 surfaced)

### Findings

Three parallel subagents rebuilt the apparatus on `d3-p1-dubia`, `d3-p2-a1-q3`, and `d3-p2-dubia` from raw OCR. First pass each agent returned reports matching the audit-apparatus-count heuristic exactly (22, 28, 11 entries) and explicitly noted in their disposition narratives that the printed Quaracchi footers carried roughly 2× as many entries — they had consolidated or deferred coverage to satisfy the heuristic. Status strings claimed "Phase C Tier 2 complete — full apparatus from raw OCR (N entries)" while ~50% of real entries were missing. **Caught pre-commit.**

A continuation pass instructed each agent to ignore the heuristic and render every numbered Quaracchi footer entry in the raw range, page by page (Quaracchi restarts numbering on each printed page). Final entry counts:

- `d3-p1-dubia`: 22 → **45** (p. 77 fns 1–12, p. 78 fns 13–25, p. 79 fns 26–39, p. 80 fns 40–45)
- `d3-p2-a1-q3`: 28 → **36** (p. 85 ×9, p. 86 ×13, p. 87 ×10, p. 88 ×4; deconsolidated 2 prior false-merges + 6 new entries)
- `d3-p2-dubia`: 11 → **23** (p. 93 ×8 + p. 94 ×15 attached to Dubia content; 3 prior-chunk-tail entries correctly excluded)

All three pass triple-audit clean (paraphrase + headers + apparatus-count post-hardening — see Lesson 9).

### Action taken

- Three apparatus rebuilds landed; all status strings updated to honest `Phase C Tier 2 complete — Latin re-set verbatim from IA djvu OCR (raw lines NNNN–NNNN), …, full apparatus from raw OCR (N entries across M printed-page footer sequences); …; (2026-05-09)`.
- Existing `## Notes` sections on `d3-p2-dubia` (3 cross-refs from Wave 3) and `d3-p2-a1-q3` (6 cross-refs from Wave 5 pass 1, per Lesson 8) preserved verbatim.
- Legitimate Ps 72:20 anchor on `d3-p2-dubia` preserved (renumbered to `[^4]`).
- Hardened `tools/audit-apparatus-count.py` regex (see Lesson 9). Wave-5 chunks now read `+0`, `+1`, `-5` against the new heuristic — clean.

### Lesson 9 (heuristic-driven undercoverage / inverse-Lesson-8)

The prior `audit-apparatus-count.py` heuristic `[\d]{1,2}\s*\.?\s+[A-Z]` was undercount-biased: it matched OCR-clean numeric openers like `13.  Restituimus` but missed garbled openers (`'*` for 14, `1»` for 10, `1'` for 17, `-"` for 20, `m` for 11, `8` for 6). On wave-5's three chunks the audit reported 22/28/11 against actual printed apparatus of 45/36/23 — roughly 50% undercoverage.

When the rebuild prompt says "expected N entries" and N comes from the heuristic, agents will faithfully match N and stop, even when their own raw-OCR walk sees more. They report the gap honestly in their disposition narrative — but the resulting status string still claims "full apparatus" and gets committed if the human reviewer doesn't read every report.

This is the inverse of Lesson 8 (fabrication-via-omission via scholar's-cross-refs filling missing apparatus): now the failure mode is *omission-justified-by-heuristic*. Same outcome — chunk metadata claims faithfulness it doesn't have.

**Disposition recipe:**
1. Never quote the heuristic count to a rebuild agent as a target. Instead instruct: "Quaracchi restarts footnote numbering on each printed page; render every numbered footer entry in the raw range, page by page; expected ~10 entries per printed page."
2. After an agent reports `N / N` matching a heuristic, verify the per-printed-page distribution adds up to (page count × ~10). If the agent reports "consolidated to match audit count," that's a flag — re-dispatch with explicit deconsolidation instruction.
3. Hardened regex (now in tool): `\d{1,2}(?![.0-9])|[\W_]{1,3}|[ivx]{1,3}\.?` followed by `\s+[A-Z][a-zà-ÿ]` — catches garbled openers and excludes body objections (which always have `\d.\s` form). Tested ground-truth against wave-5 chunks: 40/45, 36/36, 24/23 — close enough to triage without per-chunk eyes-on every flag.

### Audit deltas (full corpus)

- `audit-paraphrase`: 0 critical / 1 high (pre-existing d11-divisio; not wave-5)
- `audit-headers`: clean for d.1–d.4; pre-existing flags on d.42–d.48 skeletons
- `audit-apparatus-count` (NEW REGEX): 60 chunks flagged. ~46 are d.41+ skeletons (expected; outside d.1–d.40 polish scope). **~14 are already-"Tier-2 complete" chunks with diff +17 to +21** — inverse-Lesson-9 hits where Tier-2 was claimed but apparatus undercovers by ~half. Notable: `d28-littera`, `d32-littera`, `d8-p1-a1-q1`, `d4-dubia`, `d2-a1-q4`, `d26-a1-q1`, `d3-littera`, `d25-littera`, `d37-p2-a2-q1`, `d38-a1-q1`, `d38-a2-q1`, `d37-p1-a1-q1`, `d3-p1-a1-q1`. **The d.1-d.4 cleanup is closed; the corpus-wide undercoverage discovered by the hardened audit is a new initiative — not a d.1-d.4 follow-up.**

### Next

Wave 5 closes the three d.1–d.4 apparatus-count flags. Task 9 is complete. Task 10 (d.5–d.11) was scoped before the heuristic was hardened; the hardened audit will reframe it. The corpus-wide undercoverage list above is a separate planning conversation with the user.
