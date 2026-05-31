# d.31–d.40 — VOL II decade polish-blocker resolution log

> **This is the VOLUME II log.** It is distinct from `manual-review/d31-d40-polish-resolution-log.md`, which covers **Volume I**'s d.31–d.40. Do not merge the two. This file records the Vol II (`book: 2`, `bon-sent-II-…`) decade polish dispositions only.

Decade: **Vol II d.31 → d.40** (closes with `bon-sent-II-d40-dubia`, committed c87d0cb). Polish performed **2026-05-31**.

Vol II offset: `pdf_page = printed_page + 22`. Raw OCR: `raw/bonaventure_vol2_raw.txt`. 600 dpi reads via `tools/extract-pages.py --volume vol2 --pages N --dpi 600` + `tools/colcrop.py`.

---

## Pass 1 — `[?]` flag resolution (last 10 distinctions, 600 dpi eyes-on)

Three substantive Notes-documented apparatus caveats carried over from the build sessions. All three RESOLVED at 600 dpi (none required an ACCEPT-ILLEGIBLE).

### 1. `bon-sent-II-d35-a2-q3` — p.835 (PDF 857) Solutio footer markers

**Caveat (a): [^19]/[^20] anchor positions in the Solutio ad-1.2.3 band.** The prior 450 dpi pass logged the three close superscripts (`tanto peccato` / `pars aliquota` / `Dionysius`) as approximate and the markers possibly off.

**RESOLVED.** 600 dpi read of p.835 left + right column bands showed the printed superscripts unambiguously, and revealed that **all five Solutio markers were shifted by one position** (a cascade off-by-one). Corrected to the printed superscripts ¹–⁶:

| sup | printed lemma | footer note | marker |
|---|---|---|---|
| ¹ | Conclusio *Hoc enim modo* | Vat. addit *culpa* | `[^19]` |
| ² | *eius pars aliquota* | *Id est, quae aliquoties replicata mensurat totum* (gloss on *aliquota*) | `[^20]` |
| ³ | *dicit Dionysius* | De Div. Nom. c. 4 § 32 | `[^21]` |
| ⁴ | ad-4 *dicit Augustinus* | Serm. 151 | `[^22]` |
| ⁵ | ad-5 *in ea* | Edd. *in eo* | `[^23]` |
| ⁶ | ad-5 *ad bonum* | Vide supra d. 7. p. 1. a. 1. q. 1. | `[^24]` |

Footer note 6 (`Vide supra d. 7…`) had been **dropped entirely** from the apparatus; added as `[^24]` with a body anchor at *gratiam iuvantem ad bonum* in both La and En. The Conclusio sentence *Hoc enim modo illi habilitati opponitur* had **no anchor at all**; `[^19]` placed there (La + En). All six markers now mirror La/En 1:1.

**Caveat (b): [^22] (Serm. 151) tail `…Contra Iulian. Pelagian. c. 16. n.`** — the section number after `n.` was logged as cut off the plate.

**RESOLVED (ACCEPT-AS-PRINTED).** 600 dpi crop of the footer line shows it genuinely ends `…c. 16. n.` with blank page to the right — the section number is **absent in the printed page itself**, not a crop/OCR truncation. The speculative `[—]` placeholder was removed; the entry reproduces the print faithfully ending at `c. 16. n.`.

### 2. `bon-sent-II-d39-a2-q2` — p.911 (PDF 933) source-footer `inclinantis/inchoantis`

**Caveat.** The note `Cum Vat. et cod. bb lectionem inclinantis praeferendam duximus lectioni inchoantis…` was logged unanchored in q2; the build agent suspected it belonged to "the q1 Gloss region."

**RESOLVED.** 600 dpi read of p.911 left column confirms the footer's superscript ² sits on the word *inclinantis* in **q1's tail body** ("…et alterius sicut *inclinantis*. Nam conscientia dictat…"), **not** in q2. The note records the editors' preference of *inclinantis* over *inchoantis* in that q1 clause (its own cross-ref "hic in corp. et ad 3" points to q1's corpus + reply ad-3).

Consequence: p.911's **three left-column footers** belong to q1's tail, all previously dropped from `bon-sent-II-d39-a2-q1` (whose page-split map wrongly stated "p.911 contributes no apparatus markers"). They were recovered and added to q1 as a new p.911 group:
- `[^1c]` (`Cfr. a. 1. q. 2. arg. 1. pro I. parte`) at *habitum in anima* (sup. ¹)
- `[^2c]` (the *inclinantis/inchoantis* reading-choice note) at *alterius sicut inclinantis* (sup. ²)
- `[^3c]` (`Cod. bb alias`) at *sed eas corrigere* (sup. ³)

All three carry matching La + En anchors. q1's apparatus total updated 24 → 27. q2's footer-map and `[?]` block updated to point to q1; no orphan introduced in either chunk.

### 3. `bon-sent-II-d33-a2-q1` — p.790 (PDF 812) `[^28]` *et*-variant attribution

**Caveat.** The note `Codd. aa ee omittunt et, pro quo cod. A substituit etiam, Vat. et etiam` was assigned to q1's Ad-6 `et… in eodem genere peccati` rather than to QUAESTIO II's arg-4 `et status`; flagged to re-confirm.

**RESOLVED.** The IA djvu OCR (raw line ~55055) prints the footer superscript glued directly to q1's Ad-6 *et* — `…sicut ille qui habet minus bona, et'' in eodem genere peccati.` — placing the marker unambiguously on q1's Ad-6 *et*. QUAESTIO II's arg-4 `et status` carries no such variant note (its own p.790 footers are the *sunt* / Magister-*Alioquin* / *Aristot.* / Psalm notes). `[^28]` is correct as placed; no body text was at risk.

---

## Pass 2 — apparatus orphan-def anchoring (corpus, mechanical)

Goal: every `[^N]:` apparatus def in the d.31–d.40 Vol II chunks must have ≥1 matching body anchor in **both** the Latin and English bodies.

### Prior agent (committed `ba53fd8`) — 5 orphan-def chunks fixed (DONE, untouched here):
- `bon-sent-II-d31-a1-q3`
- `bon-sent-II-d32-a2-q2`
- `bon-sent-II-d33-a1-q2`
- `bon-sent-II-d35-a1-q3`
- `bon-sent-II-d38-a1-q3`

### This pass — `bon-sent-II-d39-divisio`: 4 apparatus-only defs anchored.

The NOTAE-AD-COMMENTARIUM-folded defs `[^4]`–`[^7]` had no body anchor. Each was anchored at its lemma word in both La and En:
- `[^4]` (Super Ezech. 1, 7 — Glossa source for the synderesis clause) → closing-clause lemma *contra malum recalcitrat* / *kicks back against evil*.
- `[^5]` (Edd. *privationis* var. + cod. Y *in* insertion) → *depravationis* / *depravation* (co-located with `[^1]`).
- `[^6]` (Edd. *voluntatis* var.) → *veritatis* / *truth* (co-located with `[^2]`).
- `[^7]` (Codd. *scientiae* var.) → *conscientiae* / *conscience* (co-located with `[^3]`).

After: every `[^N]:` def in d39-divisio has ≥1 La and ≥1 En body anchor.

---

## Final verification

- **Marker pairing, all 90 Vol II d.31–d.40 chunks:** 0 real orphan defs; La-anchor count == En-anchor count for every def. (One audit hit on `d31-divisio` `[^15]`/`[^17]` is a *prose mention* of d31-littera's footnote numbers inside the `## Notes` section, not a real marker — pre-existing, unrelated, not a target of this pass.)
- **`audit-paraphrase.py --volume 2 --min-d 31 --max-d 40`:** 0 critical, 0 high.
- **`audit-apparatus-count.py --volume 2 --min-d 31 --max-d 40`:** 0 flagged chunks (diffs within the documented ±10–18 two-column cascade noise band).
- **`audit-headers.py --volume 2 --min-d 31 --max-d 40`:** only the pre-existing, known-coarse `d.33 DUB-LOSS` triage artifact (the Vol II header audit runs positive/coarse per the CLAUDE.md calibration note; `d33-dubia` is a committed Tier-2 chunk and was not touched by this pass).
- **Smoke build** `node site/scripts/build-content.mjs`: `2 book(s), 875 questions, 839 translated` — parses cleanly.

Chunks edited this pass: `d39-divisio`, `d39-a2-q1`, `d39-a2-q2`, `d35-a2-q3`, `d33-a2-q1` (+ `content.json`).
