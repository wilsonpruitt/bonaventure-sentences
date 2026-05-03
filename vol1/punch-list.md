# Vol I Punch List — Manual Boundary & Cleanup Issues

Generated 2026-04-17. Work through top-to-bottom; each item is independent.

## Legend

- **RENAME**: file needs renaming (wrong distinction/pars label)
- **SPLIT**: chunk is oversized — contains multiple quaestiones, needs splitting with vision
- **FIND-Q**: a QUAESTIO marker is too garbled for the script to detect; find it via PDF
- **MISSING**: chunk doesn't exist yet, needs creation from PDF
- **VERIFY**: boundary looks right but content needs spot-check
- **TIER-2**: needs full vision OCR cleanup (all non-Tier-2 chunks need this eventually)

## Priority 1 — Structural Fixes (do before vision pass)

| # | Dist | Issue | File(s) | Action | Notes |
|---|------|-------|---------|--------|-------|
| 1 | d.9 | Stale duplicate | `bon-sent-I-d9-dubia-v2.md` | DELETE | Old pre-rechunk file, superseded by clean `d9-dubia.md` |
| 2 | d.10 | Stale file | `bon-sent-I-d10-a2-q3.md` (old) | VERIFY | Old file had lines 39568-39885; new boundary is 39630-39886. Check no orphan |
| 3 | d.12 | Missing q1 | No `d12-a1-q1` exists | FIND-Q | QUAESTIO I marker garbled between lines 42122-42339. Check PDF pp. ~216-217 |
| 4 | d.13 | Missing q3 | No `d13-a1-q3` exists | SPLIT | `d13-a1-q2` is 6,058w — QUAESTIO III likely garbled inside. Check PDF pp. ~230-232 |
| 5 | d.13 | Missing dubia | No `d13-dubia` exists | FIND-Q | "DUBIA CmCA LITTKKAM" at raw line 44977 — script found QUAESTIO IV at 44820 but dubia regex missed the garbled header. Check PDF p. ~234 |
| 6 | d.15 | Missing p1-q1 | No `d15-p1-a1-q1` exists | FIND-Q | QUAESTIO I under ARTICULUS UNICUS garbled between lines 47889-48229. Check PDF p. ~243 |
| 7 | d.15 | Missing p0-dubia | `d15-p0-dubia.md` exists but boundary-fix didn't produce one | VERIFY | Old file at lines 47508-47787 — this is a dubia between the littera and p1 commentary. Keep or merge into littera? |
| 8 | d.15 | Missing p2-dubia | No `d15-p2-dubia` exists | FIND-Q | Running head "DIST. XV. P. II. DUBIA." at raw line 50245 suggests dubia exist. Check PDF p. ~255 |
| 9 | d.16/17 | Rename p2→d17-p1 | `bon-sent-I-d16-p2-divisio.md` | RENAME to `bon-sent-I-d17-p1-divisio.md` | COMMENTARIUS at line 52650 = d.17 P. I |
| 10 | d.16/17 | Rename p2→d17-p1 | `bon-sent-I-d16-p2-a1-q1.md` | RENAME to `bon-sent-I-d17-p1-a1-q1.md` | |
| 11 | d.16/17 | Rename p2→d17-p1 | `bon-sent-I-d16-p2-a1-q2.md` | RENAME to `bon-sent-I-d17-p1-a1-q2.md` | |
| 12 | d.16/17 | Rename p2→d17-p1 | `bon-sent-I-d16-p2-a1-q4.md` | RENAME to `bon-sent-I-d17-p1-a1-q4.md` | Also update frontmatter `distinctio: 17` |
| 13 | d.16/17 | Rename p3→d17-p2 | `bon-sent-I-d16-p3-divisio.md` | RENAME to `bon-sent-I-d17-p2-divisio.md` | COMMENTARIUS at line 54957 = d.17 P. II |
| 14 | d.16/17 | Rename p3→d17-p2 | `bon-sent-I-d16-p3-a1-q1.md` | RENAME to `bon-sent-I-d17-p2-a1-q1.md` | |
| 15 | d.16/17 | Rename p3→d17-p2 | `bon-sent-I-d16-p3-a1-q3.md` | RENAME to `bon-sent-I-d17-p2-a1-q3.md` | |
| 16 | d.16/17 | Rename p3→d17-p2 | `bon-sent-I-d16-p3-a1-q4.md` | RENAME to `bon-sent-I-d17-p2-a1-q4.md` | Also update frontmatter `distinctio: 17` |
| 17 | d.16 | Oversized chunk | `bon-sent-I-d16-p1-a1-q2.md` | SPLIT | 10,411w — likely contains q3, q4, dubia for d.16. Check PDF pp. ~260-268 |
| 18 | d.17 | Missing q3 (p1) | No `d17-p1-a1-q3` | FIND-Q | Between q2 (line 53399) and q4 (line 54016). Check PDF pp. ~272-274 |
| 19 | d.17 | Missing q2 (p2) | No `d17-p2-a1-q2` | FIND-Q | Between q1 (line 55022) and q3 (line 55905). Check PDF pp. ~280-282 |
| 20 | d.18 | Missing q1, q3 | No `d18-a1-q1` or `d18-a1-q3` | FIND-Q | Only q2 and q4 detected. Markers garbled between lines 57304-57594 and 58053-58054. Check PDF pp. ~290-295 |
| 21 | d.18 | Missing q5 files | `d18-a1-q5.md` and `d18-a1-q5-v2.md` exist | VERIFY | Old boundary files — check if content is inside new q4 chunk or separate |
| 22 | d.18 | Missing dubia | No dubia chunk | FIND-Q | Check if d.18 has dubia at all — PDF pp. ~298-300 |
| 23 | d.19 | Missing p1-q2, p1-q3 | Only p1-q1 and p1-q4 exist | FIND-Q | Markers garbled between lines 60285-61083. Check PDF pp. ~305-310 |
| 24 | d.20 | Missing a2-q1 | No `d20-a2-q1` exists | FIND-Q | ARTICULUS II at line 64638 but no QUAESTIO I detected before q2 at 64922. Check PDF p. ~328 |
| 25 | d.20 | Missing dubia | No dubia chunk | FIND-Q | Check PDF pp. ~330-332 |
| 26 | d.21 | Duplicate a1-q1 | Two `d21-a1-q1.md` files | RENAME | Second one (lines 66437-66677) is actually `d21-a2-q1` — ARTIGULUS IL at line 66413 = Art. II |
| 27 | d.23 | Missing a1-q2, a1-q3 | Only `d23-a1-q1` detected (6,324w) | SPLIT/FIND-Q | Oversized — likely contains q2+q3. Check PDF pp. ~356-362 |
| 28 | d.23 | Missing dubia | No dubia chunk | FIND-Q | Check PDF pp. ~366-368 |

## Priority 2 — Vision OCR Pass (after structural fixes)

All non-Tier-2 chunks need vision cleanup, but prioritize by distinction order:

| Dist | Chunks needing vision | Est. pages |
|------|----------------------|------------|
| d.10 | a1-q2, a1-q3, a2-q1, a2-q2, a2-q3, dubia | ~14 |
| d.11 | littera, divisio, a1-q1, a1-q2, dubia | ~10 |
| d.12 | littera, divisio, a1-q1(?), a1-q2, a1-q3, a1-q4, dubia | ~12 |
| d.13 | littera, divisio, a1-q1, a1-q2+q3, a1-q4, dubia | ~14 |
| d.14 | littera, divisio, a1-q1, a1-q2, a2-q1, a2-q2, dubia | ~14 |
| d.15 | littera, p1-divisio, p1-q1–q4, p2-divisio, p2-q1–q3, dubia | ~22 |
| d.16 | littera, p1-divisio, p1-q1–q4(?), dubia(?) | ~16 |
| d.17 | p1-divisio, p1-q1–q4, p1-dubia(?), p2-divisio, p2-q1–q4 | ~20 |
| d.18 | littera, q1–q5(?), dubia(?) | ~16 |
| d.19 | littera, p1-divisio, p1-q1–q4, p1-dubia, p2-divisio, p2-q1–q2, p2-dubia | ~24 |
| d.20 | littera, divisio, a1-q1, a1-q2, a2-q1, a2-q2, dubia(?) | ~12 |
| d.21 | littera, divisio, a1-q1, a2-q1, a2-q2, dubia | ~12 |
| d.22 | littera, divisio, a1-q1, a1-q2, a1-q3, a1-q4, dubia | ~14 |
| d.23 | littera, divisio, a1-q1–q3, a2-q1, a2-q2, a2-q3, dubia(?) | ~16 |
| **Total** | | **~216 pages** |

## Priority 3 — After Vision Pass

- Run `python3.11 tools/translate-batch.py vol1/ --estimate` to get API cost
- Run translation when funded
- Review translated chunks for quality
- Deploy to site

## PDF Page Reference

Vol I pt 1: PDF page = printed page + 102. So p. 200 = PDF p. 302.

Printed page ranges by distinction (approximate):
- d.9: 177–192 ✅ Tier 2
- d.10: 192–206
- d.11: 206–214
- d.12: 214–224
- d.13: 224–236
- d.14: 236–248
- d.15: 248–262
- d.16: 262–276 (shares littera with d.17)
- d.17: 276–296
- d.18: 296–310
- d.19: 310–334
- d.20: 334–342
- d.21: 342–350
- d.22: 350–362
- d.23: 362–376
