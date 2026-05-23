# Next session — Vol II d.11 in progress, **d11-dubia next**.

**d.1–d.10 COMPLETE = 130 chunks. d.11 promotion: 7/9 done**
(d11-divisio + d11-a1-q1 + d11-a1-q2 + d11-a1-q3 + d11-a2-q1 +
d11-a2-q2 + d11-a2-q3). Build: 548 translated, 878 quaestio routes.
Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com since 2026-05-23;
deploy after each decade ships.

## d.11 chunk inventory + Tier-2 progress

| chunk | lines | wc_la | status |
|---|---|---|---|
| `d11-littera`  | 19518–19627 | 1483 | skeleton |
| `d11-divisio`  | 19629–19657 |  268 | Tier 2 (2026-05-23) |
| `d11-a1-q1`    | 19658–19835 | 2333 | Tier 2 (2026-05-23) |
| `d11-a1-q2`    | 19836–19927 | 1078 | Tier 2 (2026-05-23) |
| `d11-a1-q3`    | 19928–20037 | 1430 | Tier 2 (2026-05-23) |
| `d11-a2-q1`    | 20050–20245 | 2244 | Tier 2 (2026-05-23) |
| `d11-a2-q2`    | 20246–20353 | 1354 | Tier 2 (2026-05-23) |
| `d11-a2-q3`    | 20354–20531 | 2231 | Tier 2 (2026-05-23) |
| `d11-dubia`    | 20532–20645 | 1470 | skeleton — **NEXT** |

## What to do this session

**Promote `d11-dubia`** (printed pp.289–?). Three dubia circa litteram
Magistri:
- *Dub. I.* — *Utrum unaquaeque anima ab ortu nativitatis habeat
  Angelum delegatum* (Whether each soul has an Angel deputed to it
  from the moment of birth).
- *Dub. II.* — *Utrum omnes Angelos in cognitionem divinorum
  mysteriorum secundum processum temporis profecisse* [opening
  question text: «Item quaeritur de hoc quod dicit: Constat, omnes
  Angelos in cognitionem divinorum mysteriorum secundum processum
  temporis profecisse»].
- *Dub. III.* — TBD, third dubium on a subsequent page.

Body opens at p.289 L-1 immediately after the DUBIA CIRCA LITTERAM
MAGISTRI header, "*In parte ista sunt dubitationes circa litteram, et
primo quaeritur de hoc quod dicit Hieronymus, quod unaquaeque anima
ab ortu nativitatis habeat Angelum delegatum*."

1. Extract/colcrop p.290 (and p.291 if dubia III bleeds onto it):
   `python3.11 tools/extract-pages.py --volume vol2 --pages 290,291
   --dpi 450 && for p in 290 291; do python3.11 tools/colcrop.py
   vol2 $p; done`. p.289 crops already cached at `/tmp/colcrop/vol2-p289-*`.
2. **Page 289 footers belonging to this chunk:** nn.3–5
   (*Antiquiores codd. capabilis*, *Post tamen excidisse videtur et
   minus*, *Vide Alex. Hal., S. p. II. q. 41. m. 4. a. 3; B. Albert.,
   hic a. 3; …*). d11-a2-q3 retained p.289 nn.1–2.
3. **Continuous [^N] numbering for dubia:** start at [^1] for p.289
   footer ³ (the *capabilis* variant on Dub. I).
4. Marginal labels likely present (*Notandum.*, *Solutio.*,
   *Aliter.*, *Conclusio.*, etc.) — preserve inline italic.
5. Document incoming + outgoing boundary CLEAN status in `## Notes`.
6. Three audits + smoke build, then two-commit rhythm (chunk +
   content.json; this resume note → **d11-littera** for the closing
   d.11 chunk).

After d11-dubia + d11-littera, d.11 is complete. Next d.11 milestone:
deploy + announce LIVE (deploy after each decade ships rule), then
the d.11–d.20 polish-blocker fires after d.20.

## Tooling status

- 450 dpi PDF crops cached for pp.275–289 at `/tmp/colcrop/vol2-p*`
  and `raw/vision/vol2/p-hires-*.png`.
- Manual-rescue chunks created earlier session (d.11–d.20 boundary
  sweep): d18-dubia, d19-littera, d13-a1-q2, d16-a1-q2,
  d14-p2-divisio, d14-p2-a1-q3, d14-p1-a2-q1/q2, d14-p1-a3-q1/q2.
  All are skeleton Tier-1; promote in normal Vol II cadence.
- Pre-promotion boundary sweep log:
  `manual-review/d11-d20-boundary-sweep-audit.md` — all blockers
  cleared 2026-05-23.

## Open project-wide TODOs

- **Next decade polish-blocker fires after d.20.** Three-pass cadence;
  `manual-review/d11-d20-polish-resolution-log.md` will be the log.
- **Vol I site copy** still hardcodes "Volume I" in
  `site/src/app/page.tsx:47,57` — update when Vol II has enough real
  chunks to surface in landing copy.

## Convention reminders

- "keep going" = continue chunk-by-chunk, committing each, no check-ins
  (cf. [[feedback_bonaventure-bucket-e-autopilot]]).
- Tier-2 = literal, not paraphrase, incl. scholia/apparatus.
- Marginal labels (*Ad oppositum.*, *Fundamenta.*, *Ratio …*,
  *Solutio …*, *Notandum.*, *Alia solutio.*, etc.) are preserved inline
  per Vol II convention, NOT promoted to headings.
- Backup before any rebuild: `cp <chunk>.md _backup-<chunk>-pre-<reason>-<YYYYMMDD>/`.
- Vol II offset: `pdf = printed + 22`. Trust running-head text, never
  the OCR'd digits.

Prior session-by-session vol2 history (sessions 1–77) is trimmed per
Wilson's request 2026-05-22; the per-decade resolution logs and chunk
`## Notes` are the durable record. Backup of the pre-trim resume is at
`_backup-resume-pre-trim-20260522.md` if you need to walk back.
