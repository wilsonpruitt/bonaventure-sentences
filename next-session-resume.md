# Next session — d.45 + d.46 Tier-2 promotion

Updated 2026-05-13 at close of d.43+d.44 session.

## Where we are

- d.1 through d.44 are Tier-2 (411 questions / 379 translated as of 2026-05-13 build).
- Today (session 2, 2026-05-13): promoted 15 d.43+d.44 chunks (7 + 8) in 6 parallel-agent waves under the d.41/d.42 cadence. Mechanical pre-flight cleared two vestigial p2-dubia chunks (d.43 + d.44) and created one gap-fill scaffold (`d44-a2-q1`, ART. II QUAEST. UNIC. the auto-chunker had dropped). Final audits: 0 critical, 0 high, 0 apparatus flags.
- Polish blocker for d.41-d.50 still pending at d.50 (per CLAUDE.md cadence — runs after d.50 ships, not before).

## What's next — d.45 + d.46

Same cadence and dispatch pattern. Reference logs:
- `manual-review/d41-d50-polish-resolution-log.md` (session 1 d.41+d.42 + session 2 d.43+d.44; ~395 lines).
- d43-divisio + d44-divisio for non-pars distinction frontmatter pattern (no `pars:` field).

### Pre-flight grep (do this first before dispatching agents)

```
awk 'NR>=37122 && NR<=GUESS_END && /DISTINCTIO|DIST\.|ARTICULUS|ART\.|QUAESTIO|QUAEST\.|DUB|DIVISIO|PARS|SCHOLION|COMMENTARIUS/ {print NR": "$0}' raw/bonaventure_vol1_pt2_raw.txt
```

DISTINCTIO XLV begins at raw line **37122**. Use that as `line_start` for d.45-littera. End bound: search for `DISTINCTIO XLVI.` (run grep with broader range).

### Expected patterns (same five as before)

1. Spurious `p1`/`p2` rename targets (only if neither distinction has a real *Pars Prima/Secunda*, which is the case for d.41–d.44; verify d.45/d.46 with grep for "PARS").
2. Vestigial chunks (typically `p2-dubia` at running-head boundary).
3. line_end truncations cutting off closing scholia or final dubia.
4. Possible gap-fill chunks the auto-chunker missed entirely (look for ARTICULUS / QUAESTIO / DUBIA headers that don't have a corresponding file).
5. line_end overshoots into next distinction.

### Dispatch cadence

1. Solo dry-run on one divisio chunk first to validate any new patterns.
2. Parallel sub-waves of 2-3 agents at the 8 GB RAM cap.
3. Agent prompts MUST include:
   - "**KEEP EMITTING PROGRESS OUTPUT**" + cap of 60 seconds per garbled-word investigation (avoids the 600s watchdog stalls that killed two wave-4 agents this session before redispatch).
   - 400 dpi PNGs for header verification, not 600 (faster).
   - Raw OCR is the canonical Latin source; PNGs are for header confirmation + flag resolution only.
   - Don't bleed into neighbor chunks; report scope findings rather than acting.

## d.41-d.50 polish-blocker (deferred until d.50 ships)

Per CLAUDE.md "Polish-blocker cadence (every 10 distinctions)": runs after d.50 ships, not before. Carry list (so far):

- 23 `[?]` flags across d.43+d.44 chunks (most in d44-a1-q3 = 6, d43-littera = 5, d43-a1-q1 = 5, d44-a1-q2 = 3). All catalogued per-chunk in `manual-review/d41-d50-polish-resolution-log.md`. PDF eyes-on at 600+ dpi will resolve most.
- `d43-divisio` `[^1]` may be mis-anchored on `reperitur` (true anchor likely on `multa` in d43-littera body, line 34122) — re-investigate.
- `d44-a1-q1` apparatus undercount: raw=27, chunk=12 (most p.783 footers correctly excluded as belonging to q2; verify a few p.782 footers aren't missing).
- `d44-a1-q2` 3 `[?]` flags on p.785 — Q.II + Q.III footers folded in raw OCR; needs 600 dpi eyes-on.

## Pre-existing carry-over (from session 1 close 2026-05-12)

- ~140 `[?]` flags in d.41+d.42 chunks were resolved this session via the pre-existing log entries. Polish pass at d.50 will sweep the remaining ~23 d.43+d.44 flags listed above.
- `d41-d50-polish-resolution-log.md` is the canonical per-chunk record; ~395 lines after today's append.

## Build state at handoff

- `cd site && node scripts/build-content.mjs` → `Built content.json: 1 book(s), 411 questions, 379 translated`.
- No commits this session. All 15 d.43+d.44 chunks ready to commit as one unit; pre-existing skeletons in d.45+ untouched.
- Keep around per project convention: `_backup-d43-p2-dubia-vestigial-20260513/`, `_backup-d44-p2-dubia-vestigial-20260513/`, plus the per-chunk pre-promote backups the agents wrote.

## Tools cheat sheet

```bash
# Pre-flight structural grep
awk 'NR>=START && NR<=END && /DISTINCTIO|DIST\.|ARTICULUS|ART\.|QUAESTIO|QUAEST\.|DUB|DIVISIO|PARS|SCHOLION|COMMENTARIUS/ {print NR": "$0}' raw/bonaventure_vol1_pt2_raw.txt

# 400dpi PNG header verification
pdftoppm -r 400 -f PDF_START -l PDF_END -png raw/doctorisseraphic12bona.pdf raw/vision/vol1/d45XX-r400

# Audit gates (after edits)
python3.11 tools/audit-paraphrase.py --min-d 45 --max-d 46
python3.11 tools/audit-headers.py --min-d 45 --max-d 46
python3.11 tools/audit-apparatus-count.py --min-d 45 --max-d 46

# Build smoke
cd site && node scripts/build-content.mjs
```

**pt2 offset**: `pdf_page = printed - 410` (confirmed throughout d.41–d.44).

---

## (Archived) Prior next-session note — d.1-d.10 polish PDF eyes-on

The previous content of this file (created 2026-05-10 at close of the d.1-d.10 rechunk pipeline) has been overwritten. d.1-d.10 polish-blocker pass was completed 2026-05-12 (Bonaventure session 1 wrap-up); see `manual-review/d1-d10-polish-resolution-log.md` for the per-flag resolution record. The 250-flag PDF-eyes-on backlog described in the prior note is now resolved or dispositioned.
