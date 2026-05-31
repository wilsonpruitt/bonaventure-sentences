# Bonaventure Sentences — Next Session Resume

**Last updated:** 2026-05-31 (d41-dubia promoted → Tier 2, commit 4d75432)

**Branch:** master

## NEXT ACTION → `bon-sent-II-d41-a2-q2` (the LAST skeleton in d.41)

**Important correction:** d.41 is **NOT** fully complete. The dubia (final structural unit) shipped 2026-05-31, but **`bon-sent-II-d41-a2-q2` is still an auto-chunked skeleton** (status `auto-chunked 2026-05-30`, 0 apparatus entries; flagged SKELETON-SUSPECT by `audit-apparatus-count --volume 2`, raw=22 / chunk=0 / diff +22). Promote it next.

### d.41 unit inventory (verified 2026-05-31)

| Unit | Status |
|---|---|
| `d41-littera` | Tier 2 complete |
| `d41-a1-q1` | Tier 2 complete |
| `d41-a1-q2` | Tier 2 complete |
| `d41-a1-q3` | Tier 2 complete |
| `d41-a2-q1` | Tier 2 complete |
| **`d41-a2-q2`** | **auto-chunked skeleton — NEXT ACTION** |
| `d41-a2-q3` | Tier 2 complete |
| `d41-dubia` | Tier 2 complete (commit 4d75432) |

### d41-a2-q2 facts (for the dispatch)

- **Title:** `Utrum omne peccatum sit circa voluntatem sicut circa subiectum proprium` (Whether every sin is about the will as about its proper subject) — Art. II, q. 2 (the SECOND of Art. II's three sub-questions).
- **Frontmatter range:** `line_start: 66064`, `line_end: 66236` (raw `bonaventure_vol2_raw.txt`). `QUAESTIO II.` header at raw **66064**; ends just before `QUAESTIO III` at raw **66237** (which is q3, already Tier-2).
- **Printed pages:** q2 opens on printed **p.931** (`QUAESTIO II.` follows the q1 scholion on p.931) and runs to the foot of **p.932**, ending just before q3 opens on p.933. OCR running heads in this band: `DIST. XLI. ART. II. QUAEST. II.` (raw 66078), `981` (raw 66079, = printed 931 digit-mangled... verify), `9S2` (raw 66146, = printed 932). **Verify the printed span at 450 dpi** — `pdf = printed + 22`, so printed 931–932 = pdf 953–954.
- **Verify opener alignment:** confirm `Secundo quaeritur, utrum omne peccatum sit circa voluntatem sicut circa subiectum proprium` — the SECOND quaeritur. (The auto-chunker has known q-swap bugs; STOP and report if misaligned.)
- **has_scholion:** check the raw range for a `SCHOLION.` header between q2's Respondeo and `QUAESTIO III` (~raw 66230). q1 and q3 both carry scholia; q2 may or may not.
- **Cross-chunk hand-offs:** q2's tail and q3's head share printed p.932/933 — verify the p.932 footer split against `d41-a2-q3` (which opens on p.933). q3 already documents its picked-up/forwarded hand-offs in its `## Notes`.

### After d41-a2-q2 → d.42

Once d41-a2-q2 is Tier-2, **d.41 is fully complete**; next is `bon-sent-II-d42-littera`:
- d.42 starts at `DISTINCTIO XLII` at raw **66472/66481** (printed p.957 R-col, Cap. I `An voluntas et actio mala in eodem et circa idem sint unum peccatum, vel plura`). The Lombard littera (Caps. I–VIII: *unum/plura peccatum*, *reatus*, *septem vitia principalia*, *superbia*) runs through ~p.959 where `DIST. XLII. DIVISIO TEXTUS.` / `COMMENTARIUS IN DISTINCTIONEM XLII.` begins (raw ~66594/66628). Grep raw for those headers to fix the littera's exact end.
- **Offset:** `pdf = printed + 22`; OCR running-head digits in the p.955–959 band are mangled (936/937/9b8/9b9 = 956/957/958/959) — trust running-head *text* + offset, not OCR digits.

**Polish gate:** d.41 is NOT a decade boundary. The d.31–d.40 polish gate already closed; next gate fires at d.50. No polish blocker now.

---

## Standard per-chunk recipe (Vol II)

See project `CLAUDE.md` → "VOL II OVERRIDE" + "Efficient single-chunk subagent dispatch". In brief: PDF-priority inversion (450 dpi column bands authoritative for Respondeo/Solutio/footers; OCR base for clean prose + marker spacing); `extract-pages.py --volume vol2 --dpi 450` then `colcrop.py vol2 <page>`; backup → re-set Latin column-by-column → literal English → full per-page-restart apparatus → frontmatter Tier-2 + `## Notes` → three `--volume 2` audits + smoke build → two commits (chunk+content.json; then resume).
