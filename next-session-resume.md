# Bonaventure Sentences — Next Session Resume

**Last updated:** 2026-05-31 (d42-divisio promoted -> Tier 2, commit 4a689ee)

**Branch:** master

## NEXT ACTION -> `bon-sent-II-d42-a1-q1` (d.42 divisio now Tier 2)

**`bon-sent-II-d42-divisio` shipped 2026-05-31 (commit 4a689ee):** COMMENTARIUS IN DISTINCTIONEM XLII opener + subtitle *De differentiis peccatorum in communi* + lemma *Cum autem voluntas mala et operatio etc.* + DIVISIO TEXTUS + TRACTATIO QUAESTIONUM, printed **p.959** (PDF 981), 3-entry apparatus (single p.959 footer sequence), `has_scholion: false`, marker pairing 1-3 clean, build 875 q / 850 translated. Seam with d42-littera verified clean (littera closes `…radix omnis mali.` immediately before the COMMENTARIUS opener; no leakage). TRACTATIO listing matches actual structure (3 articles actus/reatus/modus; a1 q1+q2, a2 q1+q2, a3 q1+q2). **Hand-off forwarded:** printed p.960 (PDF 982) is entirely a1-q1 (`ARTICULUS I. De comparatione peccati operis ad peccatum voluntatis. / QUAESTIO I. Utrum peccatum voluntatis et operis sint duo peccata, vel unum.`, raw 66682/66687) with its own fresh per-page footer sequence; no divisio footer belongs to a1-q1.

**`bon-sent-II-d42-littera` shipped 2026-05-31 (commit 40e550d):** Lombard littera Caps. I-VIII (De differentiis peccatorum in communi), printed **pp.957-959** (PDF 979-981), 16-entry apparatus (per-page restart 957:1-6 / 958:1-10), `has_scholion: false`, marker pairing 1-16 clean. Seam with d.41-a2-q3 verified: p.957 L-col top (`et tunc tollit... obiecta`) is the d.41 tail and its two footers stay with the d.41 dubium; littera footers begin at the `NOTAE AD LIBR. SENTENTIARUM.` divider.

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

### d.42 progress

| Unit | Status |
|---|---|
| `d42-littera` | Tier 2 complete (commit 40e550d, pp.957-959) |
| `d42-divisio` | Tier 2 complete (commit 4a689ee, p.959) |
| `d42-a1-q1` / `q2`, `a2-q1` / `q2`, `a3-q1` / `q2`, `d42-dubia` | auto-chunked skeleton (NEXT: a1-q1) |

### Next: d.42 a1-q1

`bon-sent-II-d42-a1-q1` (*Utrum peccatum voluntatis et operis sint duo peccata, vel unum*):
- `ARTICULUS I. / QUAESTIO I.` begins raw **66682/66687**, printed **p.960** (PDF 982). Question body runs to `QUAESTIO II.` at raw **66848** (that is a1-q2). Article opener `De comparatione peccati operis ad peccatum voluntatis.` folds into a1-q1 per the chunking convention (no standalone article-divisio chunk). Fresh per-page p.960 footer sequence (no divisio footer carries over).
- After a1-q1 come a1-q2 (66848+), a2-q1 (66990, after ARTICULUS II at 66981), a2-q2 (67196), a3-q1/q2, and d42-dubia -- all still auto-chunked skeletons (apparatus audit diffs +15 to +52).
- **Offset:** `pdf = printed + 22`; OCR running-head digits in the p.957-960 band are mangled -- trust running-head *text* + offset and confirm with a low-dpi PDF render before committing (verified for d42-littera + d42-divisio).

**Polish gate:** d.41 is NOT a decade boundary. The d.31-d.40 polish gate already closed; next gate fires at d.50. No polish blocker now.

---

## Standard per-chunk recipe (Vol II)

See project `CLAUDE.md` → "VOL II OVERRIDE" + "Efficient single-chunk subagent dispatch". In brief: PDF-priority inversion (450 dpi column bands authoritative for Respondeo/Solutio/footers; OCR base for clean prose + marker spacing); `extract-pages.py --volume vol2 --dpi 450` then `colcrop.py vol2 <page>`; backup → re-set Latin column-by-column → literal English → full per-page-restart apparatus → frontmatter Tier-2 + `## Notes` → three `--volume 2` audits + smoke build → two commits (chunk+content.json; then resume).
