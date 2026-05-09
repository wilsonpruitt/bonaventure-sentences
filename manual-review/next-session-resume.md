# Next-Session Resume Prompt

Drafted 2026-05-09 at end of session that shipped Tasks 6, 7, 8 of the
pre-d.41 cleanup arc. Paste the block below verbatim into the next
session.

---

```
Resume Bonaventure Vol I cleanup. Tasks 6, 7, 8 shipped this past
session (commits a31d61e, cf457d3, d10f8d7). HEAD is currently d10f8d7.
Working tree should be clean.

Confirm starting state:
1. git log -1 → d10f8d7
2. python3.11 tools/audit-paraphrase.py → 0 critical / 1 high
   (the 1 high is d11-divisio, pre-existing pre-this-arc; not your problem)
3. python3.11 tools/audit-headers.py → 0 flags
4. python3.11 tools/audit-formatting.py 2>&1 | grep -c "missing required keys"
   → 17 (the 17 d.3-d.4 chunks Task 8 deferred)
5. df -h ~ → free space; pt2 PDF crops can chew through it

Background context: this is a multi-session arc to clean ALL audit flags
AND zero out the d.1-d.11 paraphrase backlog before d.41 chunking is
unblocked. Last session knocked out:
- Task 6 (PDF-supplement diff-check across 7 already-Tier-2 chunks;
  caught 1 wholesale-fabrication chunk d9-a1-q4 + 1 paraphrase-scholion
  chunk d18-a1-q5 + 5 smaller). 6 lessons logged in
  manual-review/d1-d11-pdf-supplement-resolution-log.md — READ FIRST,
  the "## Lesson" sections at the end of each disposition section have
  audit patterns to apply during Tasks 9 and 10.
- Task 7 (d2-littera frontmatter + full d3-p1-a1-q3 rebuild — 14
  apparatus entries + restored missing scholion).
- Task 8 (backfilled line_start/line_end for 9 d.1-d.3 chunks).

Tasks 9, 10, 11 are remaining (ID order in TaskList).

Resume on Task 9: d.1-d.4 Tier-2 promotion. ~22 chunks, ~173 apparatus
entries to rebuild bilingual La/En. Includes the 17 d.3-d.4 chunks
Task 8 deferred (need per-chunk OCR header-grep to locate line ranges
since their status strings don't carry explicit lines NNN-NNN).

Read CLAUDE.md "Tier-2 verification workflow" before any chunk edits —
the per-chunk Tier-2 recipe + guard-rail discipline are non-negotiable.
Read MEMORY.md (Bonaventure-related entries) for project state.
Read manual-review/d1-d11-pdf-supplement-resolution-log.md — six audit
patterns logged there apply to this task:
  1. OCR linearization artifact (page-split + per-page footer numbering)
  2. ## Notes disclaimers = fabrication suspect, not soft TODO
  3. Status-string "reconstructed" flags mask boundary-sentence defects
  4. Audit smell-word collision — point at log file, don't restate
  5. Quaracchi loc-cit / ibid back-references — preserve verbatim
  6. Status-string ambiguities classify as fix / reframe / document

Wave-dispatch strategy per project guidance:
- 3-6 parallel subagents per wave (6-agent hard cap, see
  feedback_acta-usage.md)
- Use the agent-prompt-template pattern (feedback_acta-agent-prompt.md):
  permission test + 30-chunk floor for high-quality output
- Background subagents need PROJECT-SCOPE .claude/settings.json, not
  user-scope (feedback_acta-subagent-permissions.md)

Pace: realistic 1-2 chunks/session at first, 2-4 once patterns are
familiar. With wave-dispatch and 22 chunks total, plan 4-6 waves of
3-5 chunks each.

After Task 9, Task 10 (d.5-d.11 apparatus rebuild, ~25 quaestiones,
similar wave-dispatch).

After Task 10, Task 11: final triple-audit + commit; d.41 chunking
declared unblocked.

Don't chase d.41 chunking until #11 closes — guard-rail discipline
(feedback_bonaventure-guard-rail-discipline.md) is non-negotiable.

The TaskList from this session may persist or may have been cleared —
check first; if cleared, recreate Tasks 9, 10, 11 with the descriptions
above.
```

---

## Why these specific pointers

- **Audit baselines** (0 critical / 1 high, 17 missing-keys) — so the
  next session can verify nothing regressed between sessions
- **Resolution-log pointer** — the 6 lessons there are directly
  applicable to Task 9's apparatus work; read them before any agent
  dispatch
- **Memory pointers** to the relevant feedback files (Acta usage, agent
  prompt template, subagent permissions, guard-rail discipline) so
  agent dispatch is set up correctly from the start
- **Pace expectations** explicit — Task 9 = 22 chunks; even with
  wave-dispatch this is 4-6 waves, not one big push
- **The deferred-17-chunks note** so Task 9 picks them up (rather than
  thinking Task 8 covered everything)

## Files of interest for the resume

- `manual-review/d1-d11-pdf-supplement-resolution-log.md` — 7 chunk
  dispositions + 6 lessons
- `tools/backfill-line-bounds.py` — extended to handle d.1-d.3; for
  the 17 deferred d.3-d.4 chunks, will need a sibling tool that
  greps for `QU.ESTIO N.` / `ARTICULUS N.` / `DUB. N.` headers to
  locate ranges
- `manual-review/d1-d40-paraphrase-audit.md` — current audit state
- `vol1/_backup-*/` — historical pre-rebuild snapshots

## Mid-session refresh

If this session goes long enough that context starts compressing,
re-read this file to refresh the plan rather than re-deriving it from
scratch.
