# Wave 9b Tier B — resume document

> **CLOSED 2026-05-09 in commit `8ca85a3`.** All 14 chunks dispositioned
> (8 rebuilt, 6 overcount-accepted). See `wave9b-tier-c-resume.md` for
> the next initiative. This file preserved for reference.

Created 2026-05-09 after Wave 9b Tier A landed. This is the queue for the **next session** to pick up.

## Context (skim before starting)

Wave 5 (`6fa6b43`) closed the d.1–d.4 apparatus-count flags by rebuilding three chunks from raw OCR. While there, the audit-apparatus-count.py regex was hardened (it had been undercounting by ~50% due to OCR-garbled footer openers). The hardened audit then surfaced ~23 already-"Tier-2 complete" chunks corpus-wide where the apparatus undercovers raw OCR by significant amounts (Lesson 9 / inverse-Lesson-8). Status strings on all 23 were demoted from `Phase C Tier 2 complete —` to `Phase C Tier 2 apparatus-incomplete —` with an audit-flag tail.

**Tier A** (9 chunks at diff ≥ +30) was rebuilt in the same session. **Tier B** (14 chunks at diff +20 to +29) is queued here.

Read these before working:
- `CLAUDE.md` Tier-2 verification workflow (item 5 has the Lesson-9 update)
- `manual-review/d1-d4-tier2-promotion-log.md` Lessons 7, 8, 9 — direct precedents
- `tools/audit-apparatus-count.py` — hardened regex docs in the comment block

## Tier B chunk queue

Each entry: `chunk` | `distinctio` | `line range` | `printed pages` | `current chunk-app count` | `hardened-heuristic raw count` | `diff`. The `expected ~N` is calculated as printed-page-count × ~10 (Quaracchi page-restart convention).

| Chunk | d | Lines | Pages | App | Raw | Diff | Expected |
|---|---|---|---|---|---|---|---|
| `bon-sent-I-d39-a1-q1` | 39 | (look up) | (look up) | 13 | 40 | +27 | ~40 |
| `bon-sent-I-d8-littera` | 8 | (look up) | (look up) | 14 | 42 | +28 | ~40 |
| `bon-sent-I-d37-p2-a1-q1` | 37 | (look up) | (look up) | 13 | 38 | +25 | ~40 |
| `bon-sent-I-d7-a1-q2` | 7 | (look up) | (look up) | 7 | 31 | +24 | ~30 |
| `bon-sent-I-d27-littera` | 27 | 4588–4823 | (look up) | 17 | 40 | +23 | ~40 |
| `bon-sent-I-d8-p1-a1-q2` | 8 | 32054–32575 | (look up) | 11 | 34 | +23 | ~30 |
| `bon-sent-I-d8-p2-a1-q2` | 8 | 34190–34634 | (look up) | 8 | 31 | +23 | ~30 |
| `bon-sent-I-d31-littera` | 31 | 11190–11540 | (look up) | 21 | 43 | +22 | ~40 |
| `bon-sent-I-d33-littera` | 33 | 15062–15351 | (look up) | 19 | 41 | +22 | ~40 |
| `bon-sent-I-d28-littera` | 28 | 7590–7777 | (look up) | 15 | 36 | +21 | ~30 |
| `bon-sent-I-d32-littera` | 32 | 13570–13859 | (look up) | 15 | 36 | +21 | ~30 |
| `bon-sent-I-d8-p1-a1-q1` | 8 | 31620–32053 | (look up) | 10 | 31 | +21 | ~30 |
| `bon-sent-I-d38-a1-q1` | 38 | 25147–25411 | (look up) | 11 | 31 | +20 | ~30 |
| `bon-sent-I-d38-a2-q1` | 38 | 25639–25983 | (look up) | 10 | 30 | +20 | ~30 |

To regenerate this table with current frontmatter values:

```bash
cd ~/bonaventure-sentences
python3.11 tools/audit-apparatus-count.py 2>&1 | grep -E "d(8|7|27|28|31|32|33|37|38|39)-" | sort
```

## Suggested approach

1. **Per chunk: 1 subagent**, page-by-page enumeration recipe (see Wave 5 prompts in this session's transcript or apply the Lesson 9 disposition recipe directly). Do NOT quote the heuristic count to the agent as a target; tell it "Quaracchi restarts numbering each printed page; render every numbered footer entry; expected ~10 per page."
2. **Wave dispatch 3 in parallel** per round (8GB RAM machine; 6-cap from Acta feedback memory but 3 is comfortable). Watch out: most of these are `littera` chunks with their own structure — the `vol1/bon-sent-I-d8-littera.md` template is the reference.
3. **Status string update** on success: replace `Phase C Tier 2 apparatus-incomplete —` (current downgrade) with `Phase C Tier 2 complete — ` plus the new full disposition narrative.
4. **Triple-audit** before each commit (paraphrase + headers + apparatus-count with hardened regex).
5. **Note on littera chunks:** Lombard's text has its own footer apparatus that's different in character from Bonaventure's commentary apparatus. Both are valid Quaracchi footnotes; the rebuild should capture both.

## Possible scope reduction

If post-Tier-A the Tier B chunks turn out to be smaller than Tier A on average, consider doing all 14 in 5 rounds of 3 across ~2 sessions. Otherwise expect 4-5 sessions.

## After Tier B

Tier C is still open (37 chunks at diff +5 to +19). That's a separate planning conversation — some may be heuristic noise rather than real undercoverage and need eyes-on triage rather than rebuild.

After all three tiers close, the next-session-resume.md baseline of "all d.1–d.40 Tier-2 chunks audit-clean" finally holds — and d.41+ chunking can advance under the polish-blocker discipline.
