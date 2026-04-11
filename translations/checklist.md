# Translation Checklist — Vol I, Dist. 1–23

**Format migration in progress (started 2026-04-10).** New chunks use the unified single-file format at `vol1/{chunk-id}.md` with `## Latin`, `## English`, `## Apparatus`, `## Notes` h2 sections. Legacy OCR chunks still use the old split format (Latin in `vol1/`, English in `translations/vol1/`); migrated files are preserved under `legacy/` subfolders until the rebuild replaces them. See memory and `vol1/bon-sent-I-d1-a1-q1.md` (the pilot) for the template.

**Next session priorities** (from memory; repeated here for convenience):
1. Reader page upgrade (bilingual footnotes, apparatus, scholion, pagination toggle, sigla tooltips)
2. Fill gaps: `d1-a1-q3`, `d1-a3-q1`, `d4-a1-q2`
3. Dist. III vision spot-check (printed pp. ~62–80, PDF pp. ~164–182)
4. Populate `tools/apparatus-sigla.json` for Vol I from prolegomena
5. Rebuild remaining legacy chunks in new format, distinction by distinction


## Prolegomena
- [ ] `bon-sent-I-proleg`

## Distinctio 1
- [x] `bon-sent-I-d1-littera` — Lombard Caps. I–III (pp. 26–28), translated via vision pass 2026-04-10
- [x] `bon-sent-I-d1-a1-q1` — **REBUILT in new unified format 2026-04-10** (vision re-OCR, bilingual footnotes, apparatus via `tools/apparatus-translate.py`, pagination comments, scholion header). Legacy OCR version moved to `vol1/legacy/` and `translations/vol1/legacy/`. The rebuild also **recovers the full first half of Q. I** (arguments, sed contra, conclusio) which the legacy chunk had dropped due to mis-chunking. File: `vol1/bon-sent-I-d1-a1-q1.md` (225 lines). **Build script upgraded** to parse unified-format files (`## Latin` / `## English` / `## Apparatus`) with backward compatibility for legacy split format. New file renders on the site with full content.
- [x] `bon-sent-I-d1-a1-q2`
- [ ] `bon-sent-I-d1-a1-q3` — **GAP**: Utrum solo bono creato sit utendum (printed p. 34, PDF p. 136, raw lines ~13962–14104). Confirmed via vision audit 2026-04-10.
- [x] `bon-sent-I-d1-a2-q1`
- [ ] `bon-sent-I-d1-a3-q1` — **GAP**: Utrum Deo sit fruendum (printed p. 38, PDF p. 140, raw lines ~14595–14726). Confirmed via vision audit 2026-04-10.
- [x] `bon-sent-I-d1-a3-q2`
- [x] `bon-sent-I-d1-dubia`

## Distinctio 2
- [x] `bon-sent-I-d2-a1-q2`
- [x] `bon-sent-I-d2-a1-q3`
- [x] `bon-sent-I-d2-a1-q4`
- [x] `bon-sent-I-d2-divisio`
- [x] `bon-sent-I-d2-dubia`
- [x] `bon-sent-I-d2-q1`

## Distinctio 3
- [x] `bon-sent-I-d3-a1-q4`
- [x] `bon-sent-I-d3-dubia`
- [x] `bon-sent-I-d3-p1-a1-q1`
- [x] `bon-sent-I-d3-p1-a1-q2`
- [x] `bon-sent-I-d3-p1-dubia`
- [x] `bon-sent-I-d3-p2-a1-q1`
- [x] `bon-sent-I-d3-p2-a1-q3`
- [x] `bon-sent-I-d3-p2-a2-q1`
- [x] `bon-sent-I-d3-p2-a2-q2`

## Distinctio 4
- [x] `bon-sent-I-d4-a1-q1`
- [ ] `bon-sent-I-d4-a1-q2` — **GAP**: raw lines ~23871–24169. Confirmed via OCR audit 2026-04-10 (chunker lost this question because the running header was OCR-mangled to `DIST. IV. ART. UNICUS QUAEST.` with no number).
- [x] `bon-sent-I-d4-a1-q3`
- [x] `bon-sent-I-d4-a1-q4`
- [x] `bon-sent-I-d4-dubia`

## Distinctio 5
- [x] `bon-sent-I-d5-a1-q1`
- [x] `bon-sent-I-d5-a1-q2`
- [x] `bon-sent-I-d5-a2-q1`
- [x] `bon-sent-I-d5-a2-q2`
- [x] `bon-sent-I-d5-dubia`

## Distinctio 6
- [ ] `bon-sent-I-d6-a1-q1`
- [ ] `bon-sent-I-d6-a1-q2`
- [ ] `bon-sent-I-d6-a1-q3`
- [ ] `bon-sent-I-d6-dubia`

## Distinctio 7
- [ ] `bon-sent-I-d7-a1-q1`
- [ ] `bon-sent-I-d7-a1-q2`
- [ ] `bon-sent-I-d7-a1-q3`
- [ ] `bon-sent-I-d7-a1-q4`
- [ ] `bon-sent-I-d7-dubia`

## Distinctio 8
- [ ] `bon-sent-I-d8-p1-a1-q1`
- [ ] `bon-sent-I-d8-p1-a1-q2`
- [ ] `bon-sent-I-d8-p1-a2-q1`
- [ ] `bon-sent-I-d8-p1-a2-q2`
- [ ] `bon-sent-I-d8-p1-divisio`
- [ ] `bon-sent-I-d8-p1-dubia`
- [ ] `bon-sent-I-d8-p2-a1-q1`
- [ ] `bon-sent-I-d8-p2-a1-q2`
- [ ] `bon-sent-I-d8-p2-a1-q3`
- [ ] `bon-sent-I-d8-p2-a1-q4`
- [ ] `bon-sent-I-d8-p2-dubia`

## Distinctio 9
- [ ] `bon-sent-I-d9-a1-q1`
- [ ] `bon-sent-I-d9-a1-q2`
- [ ] `bon-sent-I-d9-a1-q4`
- [ ] `bon-sent-I-d9-divisio`
- [ ] `bon-sent-I-d9-dubia`
- [ ] `bon-sent-I-d9-dubia-v2`

## Distinctio 10
- [ ] `bon-sent-I-d10-a1-q1`
- [ ] `bon-sent-I-d10-a1-q2`
- [ ] `bon-sent-I-d10-a1-q3`
- [ ] `bon-sent-I-d10-a2-q1`
- [ ] `bon-sent-I-d10-a2-q3`
- [ ] `bon-sent-I-d10-dubia`

## Distinctio 11
- [ ] `bon-sent-I-d11-a1-q1`
- [ ] `bon-sent-I-d11-a1-q2`
- [ ] `bon-sent-I-d11-dubia`

## Distinctio 12
- [ ] `bon-sent-I-d12-a1-q2`
- [ ] `bon-sent-I-d12-a1-q4`
- [ ] `bon-sent-I-d12-dubia`

## Distinctio 13
- [ ] `bon-sent-I-d13-a1-q1`
- [ ] `bon-sent-I-d13-a1-q2`
- [ ] `bon-sent-I-d13-a1-q3`
- [ ] `bon-sent-I-d13-dubia`

## Distinctio 14
- [ ] `bon-sent-I-d14-a1-q1`
- [ ] `bon-sent-I-d14-a1-q2`
- [ ] `bon-sent-I-d14-a2-q1`
- [ ] `bon-sent-I-d14-a2-q2`

## Distinctio 15
- [ ] `bon-sent-I-d15-p0-dubia`
- [ ] `bon-sent-I-d15-p1-a1-q1`
- [ ] `bon-sent-I-d15-p1-a1-q2`
- [ ] `bon-sent-I-d15-p1-a1-q3`
- [ ] `bon-sent-I-d15-p1-a1-q4`
- [ ] `bon-sent-I-d15-p2-a1-q3`
- [ ] `bon-sent-I-d15-p2-divisio`
- [ ] `bon-sent-I-d15-p2-dubia`

## Distinctio 16
- [ ] `bon-sent-I-d16-a1-q3`
- [ ] `bon-sent-I-d16-divisio`
- [ ] `bon-sent-I-d16-dubia`

## Distinctio 17
- [ ] `bon-sent-I-d17-p0-divisio`
- [ ] `bon-sent-I-d17-p1-a1-q1`
- [ ] `bon-sent-I-d17-p1-a1-q3`
- [ ] `bon-sent-I-d17-p1-a1-q4`
- [ ] `bon-sent-I-d17-p1-dubia`
- [ ] `bon-sent-I-d17-p2-a1-q1`
- [ ] `bon-sent-I-d17-p2-a1-q2`
- [ ] `bon-sent-I-d17-p2-a1-q3`
- [ ] `bon-sent-I-d17-p2-a1-q4`

## Distinctio 18
- [ ] `bon-sent-I-d18-a1-q2`
- [ ] `bon-sent-I-d18-a1-q5`
- [ ] `bon-sent-I-d18-a1-q5-v2`

## Distinctio 19
- [ ] `bon-sent-I-d19-p0-a1-q4`
- [ ] `bon-sent-I-d19-p0-dubia`
- [ ] `bon-sent-I-d19-p0-q0`
- [ ] `bon-sent-I-d19-p1-a1-q1`
- [ ] `bon-sent-I-d19-p1-a1-q4`
- [ ] `bon-sent-I-d19-p1-divisio`
- [ ] `bon-sent-I-d19-p1-dubia`
- [ ] `bon-sent-I-d19-p2-a1-q1`
- [ ] `bon-sent-I-d19-p2-a1-q2`
- [ ] `bon-sent-I-d19-p2-a1-q3`
- [ ] `bon-sent-I-d19-p2-a1-q4`
- [ ] `bon-sent-I-d19-p2-dubia`
- [ ] `bon-sent-I-d19-p2-q2`

## Distinctio 20
- [ ] `bon-sent-I-d20-a1-q1`
- [ ] `bon-sent-I-d20-a2-q2`
- [ ] `bon-sent-I-d20-dubia`

## Distinctio 21
- [ ] `bon-sent-I-d21-a1-q1`
- [ ] `bon-sent-I-d21-a2-q1`
- [ ] `bon-sent-I-d21-dubia`
- [ ] `bon-sent-I-d21-q2`

## Distinctio 22
- [ ] `bon-sent-I-d22-a1-q2`
- [ ] `bon-sent-I-d22-a1-q3`
- [ ] `bon-sent-I-d22-a1-q4`
- [ ] `bon-sent-I-d22-divisio`
- [ ] `bon-sent-I-d22-dubia`
- [ ] `bon-sent-I-d22-q0`

## Distinctio 23
- [ ] `bon-sent-I-d23-a1-q1`
- [ ] `bon-sent-I-d23-a1-q2`
- [ ] `bon-sent-I-d23-a1-q3`
- [ ] `bon-sent-I-d23-a2-q1`
- [ ] `bon-sent-I-d23-a2-q2`
- [ ] `bon-sent-I-d23-a2-q3`
