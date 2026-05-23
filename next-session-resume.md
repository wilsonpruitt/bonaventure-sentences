# Next session — Vol II **d.11 promotion** (decade gate d.1–d.10 is now OPEN).

**d.1–d.10 COMPLETE = 130 chunks; build 541 translated.** The d.1–d.10
decade polish-blocker is fully closed as of 2026-05-22 (session 77):

- **Pass 1** — every `[?]` flag and logged low-confidence item in d.1–d.10
  resolved against 600 dpi PDF. Full disposition in
  `manual-review/vol2-d1-d10-polish-resolution-log.md`.
- **Pass 2** — both apparatus follow-ups resolved: `d1-p1-a1-q1 [^6]`
  footer-merge split (new `[^6]` = `Cod. Q ratione formae.`, new `[^7]`
  = Aristotle *Metaph.* note, all later markers shifted; chunk now carries
  35 entries) + `d3-p1-a1-q1` apparatus crosswalk corrected to
  `p.89 1–7 → [^1]–[^7]; p.90 1–9 → [^8]–[^16]; p.91 1–8 → [^17]–[^24]`.
- **Pass 3 (this session)** — cross-chunk boundary integrity sweep.
  d.10's nine mid-page boundaries were documented CLEAN at promotion
  (each d.10 chunk's `## Notes`); the d.1–d.9 sweep added ~98 more
  mid-page boundaries, **all CLEAN** — no cascade-merge splices found,
  no missing footer notes uncovered, shared-page apparatus splits already
  documented in chunk Notes from earlier polish passes. Tally per
  distinction: d.1=14, d.2=15, d.3=13, d.4=7, d.5=7, d.6=7, d.7=13,
  d.8=14, d.9=8 (counts include cross-distinction seams where the prior
  dubia/littera share a printed page with the next distinction's opening
  chunk). d9-divisio body re-verified to contain the s67-restored
  *tertia hierarchia* subdivision + Gregorius/Dionysius reconciliation.

## What to do this session

**Promote d.11.** Verify chunk layout first: `ls vol2/bon-sent-II-d11-*.md`.
Per the locked Vol II workflow (see CLAUDE.md):

1. Read CLAUDE.md "Vol II Override" + "Per-chunk recipe" before touching
   anything. The 450 dpi column-band PDF crops are authoritative for damaged
   regions (Respondeo / Solutio / footers); IA djvu OCR is base only for
   clean running prose.
2. One quaestio per session is realistic — large cascade-damaged respondeos
   are solo sessions. Article openers fold into that article's q1; the
   pars-level divisio holds DIVISIO TEXTUS + TRACTATIO QUAESTIONUM.
3. Two-commit rhythm: (1) chunk work + `content.json`, (2) update this
   resume note for the next session. Always set up the *next* session's
   pointer before stopping.
4. Document each chunk's incoming + outgoing boundary CLEAN status in its
   `## Notes` at promotion time (the d.10 convention) — this is what made
   d.10's Pass 3 a no-op and should be carried forward for d.11+ so the
   next polish-blocker is similarly cheap.
5. Before commit, run all three audits with `--volume 2`:
   `python3.11 tools/audit-paraphrase.py --volume 2 --min-d 11 --max-d 11`
   (and `audit-headers.py`, `audit-apparatus-count.py` likewise) plus
   `cd site && node scripts/build-content.mjs`.

## Open project-wide TODOs (not d.11-specific)

- **Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com as of 2026-05-23**
  (deployment `dpl_A5VrMrRvVdH96VnwNZ6k6jjtYxnw`, 876 quaestio routes,
  541 translated). Vol-II-deploy pause is LIFTED — going forward, deploy
  after each decade ships (or sooner at Wilson's discretion).
- **Next decade polish-blocker fires after d.20.** Same three-pass cadence;
  `manual-review/d11-d20-polish-resolution-log.md` will be the log.
- **Vol I site copy** still hardcodes "Volume I" in `site/src/app/page.tsx:47,57`
  — update when Vol II has enough real chunks to surface in landing copy.

## Convention reminders

- "keep going" = continue chunk-by-chunk, committing each, no check-ins
  (cf. [[feedback_bonaventure-bucket-e-autopilot]]).
- Tier-2 = literal, not paraphrase, incl. scholia/apparatus.
- Marginal labels (`*Fundamenta.*`, `*Conclusio.*`, `*Solutio.*`, etc.) are
  preserved inline per Vol II convention, NOT promoted to headings.
- Backup before any rebuild: `cp <chunk>.md _backup-<chunk>-pre-<reason>-<YYYYMMDD>/`.
- Vol II offset: `pdf = printed + 22`. Trust running-head text, never the
  OCR'd digits.

Prior session-by-session vol2 history (sessions 1–77) is trimmed per
Wilson's request 2026-05-22; the per-decade resolution logs and chunk
`## Notes` are the durable record. Backup of the pre-trim resume is at
`_backup-resume-pre-trim-20260522.md` if you need to walk back.
