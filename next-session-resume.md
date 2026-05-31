# Bonaventure Sentences — Next Session Resume

**Last updated:** 2026-05-31 (d41-a2-q2 promoted -> Tier 2, commit 76408f3)

**Branch:** master

## NEXT ACTION -> `bon-sent-II-d42-littera` (d.41 is now COMPLETE)

**d.41 is fully Tier 2.** `bon-sent-II-d41-a2-q2` was the last skeleton and shipped 2026-05-31 (commit 76408f3): printed **pp. 951-953** (PDF 973-975), 17-entry apparatus (per-page restart 951:1-6 / 952:1-6 / 953:1-5), `has_scholion: false` (Art. II article scholion is held by a.2-q.1, whose §II forward-references this quaestio), marker pairing 1-17 clean, build (875 q / 848 translated) + all three `--volume 2` audits clean.

> **PAGE-NUMBER LESSON (q2, 2026-05-31):** the OCR running-head digits near d.41 a.2 are garbled -- `981 / 9S2 / 953` were really **951 / 952 / 953**. **Printed pp. 980-983 are DIST. XLIII (de peccato in Spiritum sanctum), NOT d.41.** The auto-chunker's stale `line_start: 66064` did not point at the true quaestio title either (the raw file has a corrupted/duplicated d.40<->d.41 concordance region ~66900-66930). **Always confirm printed_pages via a low-dpi PDF render of the running head before committing.**

### d.41 unit inventory (all Tier 2 as of 2026-05-31)

| Unit | Status |
|---|---|
| `d41-littera` | Tier 2 complete |
| `d41-a1-q1` / `q2` / `q3` | Tier 2 complete |
| `d41-a2-q1` | Tier 2 complete |
| `d41-a2-q2` | Tier 2 complete (commit 76408f3, pp.951-953) |
| `d41-a2-q3` | Tier 2 complete |
| `d41-dubia` | Tier 2 complete (commit c81c137) |

### Next: d.42

`bon-sent-II-d42-littera`:
- d.42 starts at `DISTINCTIO XLII` at raw **66472/66481** (printed p.957 R-col, Cap. I `An voluntas et actio mala in eodem et circa idem sint unum peccatum, vel plura`). The Lombard littera (Caps. I-VIII: *unum/plura peccatum*, *reatus*, *septem vitia principalia*, *superbia*) runs through ~p.959 where `DIST. XLII. DIVISIO TEXTUS.` / `COMMENTARIUS IN DISTINCTIONEM XLII.` begins (raw ~66594/66628). Grep raw for those headers to fix the littera's exact end.
- **Offset:** `pdf = printed + 22`; OCR running-head digits in the p.955-959 band are mangled -- trust running-head *text* + offset, not OCR digits, AND confirm with a low-dpi PDF render per the q2 lesson above.

**Polish gate:** d.41 is NOT a decade boundary. The d.31-d.40 polish gate already closed; next gate fires at d.50. No polish blocker now.

---

## Standard per-chunk recipe (Vol II)

See project `CLAUDE.md` → "VOL II OVERRIDE" + "Efficient single-chunk subagent dispatch". In brief: PDF-priority inversion (450 dpi column bands authoritative for Respondeo/Solutio/footers; OCR base for clean prose + marker spacing); `extract-pages.py --volume vol2 --dpi 450` then `colcrop.py vol2 <page>`; backup → re-set Latin column-by-column → literal English → full per-page-restart apparatus → frontmatter Tier-2 + `## Notes` → three `--volume 2` audits + smoke build → two commits (chunk+content.json; then resume).
