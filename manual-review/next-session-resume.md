# Next-Session Resume Prompt

Drafted 2026-05-09 at end of session that shipped Task 9 waves 1–4. Paste the block below verbatim into the next session.

---

```
Resume Bonaventure Vol I cleanup — Task 9 wave 5. Last session shipped
4 waves (commits f035c16, 0e3992d, 4b25bc7, 1f8dd5c). HEAD is currently
1f8dd5c. Working tree should be clean.

Confirm starting state:
1. git log -1 → 1f8dd5c
2. python3.11 tools/audit-paraphrase.py → 0 critical / 1 high
   (d11-divisio, pre-existing, not your problem)
3. python3.11 tools/audit-formatting.py 2>&1 | grep -c "missing required keys"
   → 0 (was 17 before wave 1)
4. python3.11 tools/audit-apparatus-count.py --min-d 1 --max-d 4
   → 3 flagged (d3-p1-dubia +22, d3-p2-a1-q3 +22, d3-p2-dubia +10)
5. df -h ~ → free space

Read FIRST:
- manual-review/d1-d4-tier2-promotion-log.md — full disposition history
  including 2 new lessons (Lesson 7: format-drift before translation;
  Lesson 8: fabrication-via-omission via scholar's cross-refs masking
  missing Quaracchi apparatus). Lesson 8 applies directly to this wave.
- manual-review/d1-d11-pdf-supplement-resolution-log.md — 6 prior
  lessons (page-split footer numbering, Notes-as-fabrication-suspect,
  reconstructed-boundary-sentence, smell-word collision, loc.cit.
  back-references, status-string ambiguity classification).
- CLAUDE.md "Tier-2 verification workflow" + "Apparatus conventions"
  sections.

Wave 5 scope: ~60 real Quaracchi textual-variant apparatus entries
across 3 chunks. Raw-OCR ranges already located:
- d3-p1-dubia: raw lines 20563–21005 (22 entries; chunk currently
  has 0; status string honestly says "apparatus pending"; printed
  pp. 77–80)
- d3-p2-a1-q3: raw lines 21664–22244 (22 entries; chunk currently
  has 6 scholar's cross-refs that are NOT verbatim Quaracchi —
  Lesson 8 reframe already applied wave 4; status is "Phase C
  partial —"; printed pp. 85–88)
- d3-p2-dubia: raw lines 23056–23296 (10 entries; chunk currently
  has 1 legitimate Psalm 72:20 anchored citation [^1]; 3 prior
  scholar's cross-refs were moved to ## Notes wave 3; status is
  "Phase C partial —"; printed pp. 93–94)

Per-entry recipe (CLAUDE.md Tier-2 workflow):
1. Locate raw OCR footer text (footer notes appear at the bottom of
   each printed page in the OCR — usually marked with a leading
   number followed by 2+ spaces, sometimes garbled as `*`).
2. Clean OCR garbles silently (e.g. `mrdus` → `nudus`, `essmtia` →
   `essentia`); flag genuinely ambiguous spots with `[?]` and log in
   `manual-review/tier2-ambiguities-d3-*.md`.
3. Translate literally — codex sigla preserved (Vat., cod. cc, ed.
   1, etc.); textual-variant phrases like `Vat. pro X habet Y` →
   `Vat. has Y in place of X`.
4. Place body `[^N]` anchors at the OCR-confirmed printed superscript
   positions in BOTH Latin and English bodies.
5. Format: `[^N]: **La.** <Latin>\n    **En.** <English>` with 4 or 5
   space indent on **En.** (corpus convention since d.10 is 5 spaces;
   parser tolerates 4).
6. Body anchor positions matter — Lesson 1 (page-split footer
   numbering) and Lesson 5 (loc.cit./ibid. preserved verbatim) apply.

Wave-dispatch strategy:
- 3 subagents in parallel (one per chunk), each handling its full
  chunk's apparatus (10–22 entries each).
- Use the Acta agent prompt template (feedback_acta-agent-prompt.md):
  permission test + 30-chunk floor for high-quality output.
- Background subagents need PROJECT-SCOPE .claude/settings.json
  (feedback_acta-subagent-permissions.md).
- 6-agent hard cap (feedback_acta-usage.md); 3 is well under.

After each subagent completes:
- Triple-audit (paraphrase + headers + apparatus-count for d.1–d.4)
- Confirm body anchors in both Latin and English bodies match
- Update transcription_status from "Phase C partial —" to
  "Phase C Tier 2 complete — Latin re-set verbatim from IA djvu OCR
  (raw lines NNNN–NNNN), fresh literal English translation, full
  apparatus from raw OCR (N entries), [optional [?] flags] (YYYY-MM-DD)"
  (Lesson 4: status-string smell-word collision — point at log file
  rather than restating prior reconstruction history inline)
- For d3-p1-dubia, also remove the `[Apparatus footnotes pending — see
  Quaracchi…]` stub block when the real apparatus lands

Important — don't re-rebuild what wave 3/4 already preserved:
- d3-p2-dubia [^1] (Psalm 72:20) is legitimate — keep the existing
  anchored entry; renumber surrounding new entries around it
- d3-p2-dubia ## Notes section (3 scholar's cross-refs moved there
  wave 3) is intentional — preserve as-is; do not move back into
  apparatus
- d3-p2-a1-q3's 6 existing entries are scholar's cross-refs — Wave 5
  decision needed: (a) replace them with real Quaracchi entries and
  delete the cross-refs (cleaner Tier-2), (b) move cross-refs to a
  ## Notes section like d3-p2-dubia (preserve), or (c) keep both,
  with the real apparatus added under new numbers and the
  cross-refs renumbered to high values. Ask the user before
  starting if the call is non-obvious.

Pace: 1 chunk per agent in parallel = ~60 min wall-clock for all 3
chunks if subagents run concurrently. If running serial-by-self,
expect 30–60 min per chunk; one or two chunks per session is fine.

After Task 9 closes (all 3 chunks Tier-2):
- Task 10 (d.5–d.11 apparatus rebuild, ~25 quaestiones, similar
  pattern but spotcheck for Lesson 8 first — those chunks may also
  be carrying scholar's-cross-refs masquerading as Quaracchi)
- Task 11 (final triple-audit + commit; declare d.41 chunking
  unblocked)

Don't chase d.41 chunking until #11 closes — guard-rail discipline
(feedback_bonaventure-guard-rail-discipline.md) is non-negotiable.

Optional bonus before advancing to Task 10: sample-Tier-2 verification
on one randomly-picked already-"Tier-2-claimed" d.4 chunk per Task 6
protocol (600 dpi PDF diff vs chunk; look for fabrication, both
wholesale-paraphrase d9-a1-q4 style and scholar's-cross-refs Lesson-8
style). If d.3 has 2 of 12 chunks with Lesson-8 fabrication, base
rate of corrupted "Tier-2" claims may be 10–20% — worth a probe.
```

---

## Why these specific pointers

- **Audit baselines** — confirm nothing regressed between sessions; the
  3 apparatus-count flags are *expected* (deferred from wave 4) and are
  exactly the wave-5 work.
- **Promotion-log pointer first, PDF-supplement-log second** — Lessons
  7 and 8 are session-specific and apply directly; the older 6 lessons
  are ambient discipline.
- **Don't re-rebuild what was preserved** — wave 3 moved 3 scholar's
  cross-refs to ## Notes intentionally; wave 4 left d3-p2-a1-q3's 6
  cross-refs in place pending a wave-5 decision. A fresh subagent
  without context could destroy this work.
- **Decision deferred to user** — d3-p2-a1-q3's existing 6 entries
  represent a real choice (delete / move-to-Notes / keep-both); the
  next session should ask before proceeding rather than guessing.
- **Pace + sample-verification probe** — surfaces the Lesson 8 base
  rate question, which affects how Task 10 should be scoped.

## Files of interest for the resume

- `manual-review/d1-d4-tier2-promotion-log.md` — wave 1–4 full
  dispositions and lessons 7–8
- `manual-review/d1-d11-pdf-supplement-resolution-log.md` — Task 6
  lessons 1–6
- `tools/backfill-line-bounds-d3-d4.py` — wave 1 backfill script
  (kept for audit log; not invoked again unless new chunks need it)
- `vol1/_backup-*/` — historical pre-rebuild snapshots (none from
  waves 1–4; backups created before any actual content rebuild)

## Mid-session refresh

If this session goes long enough that context starts compressing,
re-read this file to refresh the plan rather than re-deriving it from
scratch.
