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

---

## Pass 3 (cross-chunk boundary integrity sweep) — d.31–d.33 (2026-05-31)

Verified all 24 mid-page seams (prior chunk's last printed page == next chunk's first printed page) for d.31–d.33 against the 450 dpi PDF column bands (offset pdf = printed + 22). For each seam: (a) grammatical continuity across the seam, (b) full footer accounting across the two chunks (every numbered Quaracchi footer on the shared page present in one chunk or the other), (c) no mid-paragraph body dropout (the d9-divisio cascade-merge class).

**Result: 22 CLEAN, 2 FIXED.** No body-text dropout was found at any seam (every chunk's body was complete and grammatically continuous at the seam). The 2 defects were both **dropped footnotes** at a header-break seam where the prior chunk's solutio/excursus tail shares the page with the next chunk's opener.

### Seam-by-seam

| Seam (shared printed p.) | Prior → next | Status |
|---|---|---|
| p.739 | d31-littera → d31-divisio | CLEAN (COMMENTARIUS header break; littera ends complete) |
| p.743 | d31-a1-q1 → d31-a1-q2 | CLEAN (6 footers → q2; q1 solutio complete) |
| p.745 | d31-a1-q2 → d31-a1-q3 | CLEAN (6 footers → q3) |
| p.747 | d31-a1-q3 → d31-a2-q1 | CLEAN (6 footers → a2-q1) |
| p.751 | d31-a2-q1 → d31-a2-q2 | CLEAN (footers 1–2 → q2) |
| p.753 | d31-a2-q2 → d31-a2-q3 | CLEAN (footers 1–6 → q2 scholion, 7 → q3) |
| p.755 | d31-a2-q3 → d31-dubia | CLEAN (footer 1 → q3 [^13]; footers 2–9 → dubia) |
| p.756 | d31-dubia → d32-littera | CLEAN (dubia DUB.IV ends at footer 10; littera NOTAE restart) |
| p.759 | d32-divisio → d32-a1-q1 | CLEAN (divisio holds DIVISIO+TRACTATIO; a1-q1 restarts) |
| **p.762** | **d32-a1-q1 → d32-a1-q2** | **FIXED** — see below |
| p.765 | d32-a1-q2 → d32-a2-q1 | CLEAN (footers 1–2 → a1-q2 tail; 3 + → a2-q1) |
| p.767 | d32-a2-q1 → d32-a2-q2 | CLEAN (7 footers → a2-q2) |
| p.769 | d32-a2-q2 → d32-a3-q1 | CLEAN (footer 1 → a2-q2 [^16]; 2–7 → a3-q1) |
| p.771 | d32-a3-q1 → d32-a3-q2 | CLEAN (footers 1–3 → a3-q1 tail; 4–5 → a3-q2) |
| **p.774** | **d32-a3-q2 → d32-dubia** | **FIXED** — see below |
| p.778 | d32-dubia → d33-littera | CLEAN (dubia scholion ends; littera NOTAE) |
| p.781 | d33-littera → d33-divisio | CLEAN (littera ends "…in mysterio dictum est" [^19]; divisio holds DIVISIO+TRACTATIO + NOTAE AD COMMENTARIUM [^1]/[^2]) |
| p.784 | d33-a1-q1 → d33-a1-q2 | CLEAN (footers 1–2 → a1-q1 [^18]/[^19]; 3–6 → a1-q2) |
| p.787 | d33-a1-q2 → d33-a2-q1 | CLEAN (6 footers → a2-q1) |
| p.790 | d33-a2-q1 → d33-a2-q2 | CLEAN (footers split a2-q1 [^27]/[^28] + a2-q2 [^1]–[^4]) |
| p.792 | d33-a2-q2 → d33-a3-q1 | CLEAN (footers 1–7 → a2-q2 [^12]–[^18]; footer 8 → a3-q1 [^1]) |
| p.795 | d33-a3-q1 → d33-a3-q2 | CLEAN (footer 1 → a3-q1 [^19]; 2–4 → a3-q2 [^1]–[^3]) |
| p.798 | d33-a3-q2 → d33-dubia | CLEAN (footer 1 → a3-q2 [^17]; 2–8 → dubia [^1]–[^7]) |
| p.800 | d33-dubia → d34-littera (d.33 side) | CLEAN (dubia ends "…inferri supplicium" [^23]; footers 1–6 → dubia [^18]–[^23]; d34-littera NOTAE restart) |

### FIXED #1 — p.762, `bon-sent-II-d32-a1-q1`

The chunk's Notes had **mis-forwarded all five p.762 footers to a1-q2**, but footers 1–2 anchor in **this q1's** Ad-obiectum-4 reply ("…adhuc quaerit emendam¹… ad quartum librum²…"), whose body text was already present and complete in q1. Because q1 had no markers for them and q2 has no matching body, the two footnotes had been **dropped entirely**. Restored:
- `[^19]` at *emendam* / *amends*: `Cfr. IV. Sent. d. 15. p. II. a. 1. q. 2. seqq. — Vat. adhuc tamen quaerit emendationem.`
- `[^20]` at *quartum librum* / *the fourth book*: `Dist. 4. p. I. a. 1. q. 2.`
Both anchored in La + En bodies; apparatus entries added with English; Notes footer-map corrected. (Footers 3–5 correctly remain in a1-q2.) No body text was missing.

### FIXED #2 — p.774, `bon-sent-II-d32-a3-q2`

The chunk's Notes recorded "p.774 footers 1–5 → [^19]–[^23]" but **omitted printed footer 6**, which anchors at *una syllaba* in the closing "pulcritudo metri" sentence of the *Et si tu quaeras* excursus (body present and complete). The footnote had been **dropped**. Restored:
- `[^24]` at *una syllaba* / *one syllable*: `Cfr. August., VI. Music. c. 11. n. 30; de Vera Relig. c. 22. n. 42. — Paulo superius cod. H verbis una syllaba praefigit in.`
Anchored in La + En bodies; apparatus entry added with English; Notes footer-map corrected. No body text was missing.

### Verification
- **Marker pairing**, both fixed chunks: every `[^N]:` def has matching La and En body anchors; 0 orphans. (`d32-a1-q1`: 1–20 all paired; `d32-a3-q2`: 1–24 all paired.)
- **`audit-paraphrase --volume 2 --min-d 31 --max-d 33`:** 0 critical, 0 high.
- **`audit-apparatus-count --volume 2 --min-d 31 --max-d 33`:** 0 flagged.
- **`audit-headers --volume 2 --min-d 31 --max-d 33`:** only the pre-existing, known-coarse `d.33 DUB-LOSS` triage artifact (d33-dubia's DUB headers are OCR-garbled / not visible to the audit; the chunk is intact — DUB.I/DUB.II and all 23 footers verified eyes-on during the p.798/p.800 seam reads). Not a regression; consistent with the CLAUDE.md Vol II header-audit calibration note.
- **Smoke build** `node site/scripts/build-content.mjs`: `2 book(s), 875 questions, 839 translated` — parses cleanly.

Chunks edited this pass: `d32-a1-q1`, `d32-a3-q2` (+ `content.json`). Backups: `_backup-d32-a1-q1-pass3-20260531/`, `_backup-d32-a3-q2-pass3-20260531/`.

---

## Pass 3 (cross-chunk boundary integrity sweep) — d.34–d.36 (2026-05-31)

Verified all 22 mid-page seams (prior chunk's last printed page == next chunk's first printed page) for d.34–d.36 against the 450 dpi PDF column bands (offset pdf = printed + 22). For each seam: (a) grammatical continuity across the seam, (b) full footer accounting across the two chunks (every numbered Quaracchi footer on the shared page present in one chunk or the other), (c) no mid-paragraph body dropout (the d9-divisio cascade-merge class).

**Result: 21 CLEAN, 1 FIXED.** No body-text dropout at any seam — every chunk's body is complete and grammatically continuous at the seam (all seams in d.34–d.36 are clean QUAESTIO/ARTICULUS/DUBIA/COMMENTARIUS header breaks; prior chunks close on a complete scholion, Ad-N reply, or Lombard Cap.; next chunks open with a self-contained *Secundo/Tertio/Consequenter quaeritur…* opener). The 1 defect was a **dropped footnote pair** in `d35-a2-q2`, already flagged for this decade-polish pass by the d35-a2-q3 Pass-1 note.

### Seam-by-seam

| Seam (shared printed p.) | Prior → next | Status |
|---|---|---|
| p.802 | d34-littera → d34-divisio | CLEAN (Lombard Cap. → COMMENTARIUS break; littera tail complete at [^7]) |
| p.802 | d34-divisio → d34-a1-q1 | CLEAN (divisio NOTAE [^1]; q1 receives 3 *Fundamenta* footers [^1]–[^3]) |
| p.805 | d34-a1-q1 → d34-a1-q2 | CLEAN (p.805 footers 1–4 → q1 [^23]–[^26]; footer 5 → q2 [^1]) |
| p.808 | d34-a1-q2 → d34-a1-q3 | CLEAN (7 p.808 footers forwarded → q3 [^1]–[^7]) |
| p.809 | d34-a1-q3 → d34-a2-q1 | CLEAN (7 p.809 footers → a2-q1 [^1]–[^7]) |
| p.812 | d34-a2-q1 → d34-a2-q2 | CLEAN — PDF-verified: p.812 footers 1–2 → a2-q1 [^26]; footers 3–4 → a2-q2 [^1]/[^2] |
| p.818 | d34-dubia → d35-littera | CLEAN (DISTINCTIO break; dubia complete at [^11], littera opens DISTINCTIO XXXV) |
| p.821 | d35-divisio → d35-a1-q1 | CLEAN (divisio footers 1–2; footer 3 → a1-q1 [^1]) |
| p.824 | d35-a1-q1 → d35-a1-q2 | CLEAN (1 p.824 footer → a1-q2 [^1]) |
| p.826 | d35-a1-q2 → d35-a1-q3 | CLEAN (p.826 footers 1–6 → q2 [^12]–[^17]; 7–9 → q3 [^1]–[^3]) |
| p.828 | d35-a1-q3 → d35-a2-q1 | CLEAN (q3 p.828 footnote-free; ART II opens) |
| p.830 | d35-a2-q1 → d35-a2-q2 | CLEAN (p.830 footers 1–4 → a2-q1; footer 5 → a2-q2 [^1]) |
| **p.832** | **d35-a2-q2 → d35-a2-q3** | **FIXED** — see below |
| p.836 | d35-a2-q3 → d35-dubia | CLEAN (q3 complete at scholion; DUBIA opens, p.836 footers → dubia) |
| p.842 | d36-littera → d36-divisio | CLEAN (Lombard → COMMENTARIUS break; p.842 footers 1–3 → littera, NOTAE 1 → divisio) |
| p.845 | d36-a1-q1 → d36-a1-q2 | CLEAN (p.845 footers 1–3 → a1-q2 [^1]–[^3]) |
| p.847 | d36-a1-q2 → d36-a2-q1 | CLEAN (p.847 footers 1–4 → a1-q2 [^17]–[^20]; 5–6 → a2-q1 [^1]/[^2]) |
| p.850 | d36-a2-q1 → d36-a2-q2 | CLEAN (a2-q1 scholion footnote-free; p.850 footers 1–9 → a2-q2 [^1]–[^9]) |
| p.852 | d36-a2-q2 → d36-a3-q1 | CLEAN (p.852 footer 1 → a2-q2 [^18]; footers 2–11 → a3-q1 [^1]–[^10]) |
| p.854 | d36-a3-q1 → d36-a3-q2 | CLEAN (a3-q1 scholion footnote-free; 7 p.854 footers → a3-q2 [^1]–[^7]) |
| p.856 | d36-a3-q2 → d36-dubia | CLEAN (p.856 footers 4 + 11 → dubia [^1]/[^2]; q2 retains the rest) |
| p.859 | d36-dubia → d37-littera (d.36 side) | CLEAN (Dub. V closes complete at [^20]; d.37 littera opens DISTINCTIO XXXVII fresh, p.859 NOTAE → d.37 onward) |

### FIXED #1 — p.832, `bon-sent-II-d35-a2-q2`

The d35-a2-q3 Pass-1 (footer-recovery) polish note had explicitly flagged this for the decade-polish pass: q2's committed file **dropped p.832 printed footers 2 and 3**. Confirmed eyes-on at 450 dpi (p.832 R-col): the printed superscripts `qui privatur a² malo per malum` (Ad 5) and `movendo se ipsum³` (Ad 6) are present in q2's body, but q2 carried no matching markers — both footnotes were lost. (q3's *fundamentum 1* carries printed superscript `4`, so q3 correctly begins at footer 4 — this is purely a q2 gap.) Restored:
- `[^13]` at *privatur a / deprived by* (Ad 5): `In Vat. desideratur *a.*` / "In the Vatican [edition] the word *a* is wanting."
- `[^14]` at *movendo se ipsum / moving itself* (Ad 6): `Vide scholion ad praecedentem quaest.` / "See the scholion to the preceding question."
Both anchored in La + En bodies; apparatus entries added with English; the Notes footer-map corrected (footers 1–3 now → [^12]–[^14]; 4–7 still forwarded to q3). Backup: `_backup-d35-a2-q2-pass3-20260531/`.

### Verification
- **Marker pairing**, `d35-a2-q2`: La == En == defs == [^1]–[^14]; 0 orphans.
- **`audit-paraphrase --volume 2 --min-d 34 --max-d 36`:** 0 critical, 0 high (27 chunks).
- **`audit-apparatus-count --volume 2 --min-d 34 --max-d 36`:** 0 SUSPECT flags; all +diffs within the known Vol II two-column cascade-footer triage band. `d35-a2-q2` moved +6 → +4 after the fix.
- **`audit-headers --volume 2 --min-d 34 --max-d 36`:** no LOSS flags.
- **Smoke build** `node site/scripts/build-content.mjs`: `2 book(s), 875 questions, 839 translated` — parses cleanly.

Chunks edited this pass: `d35-a2-q2` (+ `content.json`). All other 21 seams CLEAN — the d.34–d.36 chunks' `## Notes` page-split / footer-map / cascade-dropout-check blocks were verified internally consistent (hand-off chains match across adjacent chunks) and spot-checked against the 450 dpi PDF (p.812 footer split confirmed exactly).

---

## Pass 3 (boundary sweep) — d.37–d.38

Independent cross-chunk boundary integrity sweep for d.37 and d.38 (2026-05-31). Method: full marker-pairing audit across all 18 chunks (La == En == defs, 0 orphans); exhaustive cross-check of every `## Notes` hand-off chain (every FORWARDED matches the receiving chunk's RECEIVED, with explicit printed-footer-number → marker maps); 450 dpi PDF column-band verification of three representative/highest-risk seams. All seams CLEAN — no fixes made.

| Seam (shared printed p.) | Prior → next | Status |
|---|---|---|
| p.859 | d36-dubia → d37-littera (d.37 side) | CLEAN (DISTINCTIO XXXVII opens fresh; littera claims all 14 p.859/860 NOTAE AD LIBR. footers [^1]–[^14]; d.36 COMMENTARIUS notes stay with d36-divisio) |
| p.860 | d37-littera → d37-divisio | CLEAN (littera closes "…Deus mortem non fecit." before COMMENTARIUS; p.860 littera footers 1–5 → littera [^10]–[^14]; NOTAE AD COMMENTARIUM note 1 → divisio [^1]) |
| p.861 | d37-divisio → d37-a1-q1 | CLEAN (divisio ends before ARTICULUS I/QUAESTIO I; a1-q1 receives all p.861 footers fresh [^1]–[^6]) |
| p.864 | d37-a1-q1 → d37-a1-q2 | CLEAN (q1 scholion fills p.864 top, claims no footer; entire p.864 footer block 1–5 → q2 [^1]–[^5], hand-off matched) |
| p.871 | d37-a2-q1 → d37-a2-q2 | CLEAN (article scholion held by q1; p.871 lower-col footers 1–5 → q2 [^1]–[^5]) |
| p.873 | d37-a2-q2 → d37-a2-q3 | CLEAN (typeset running-head QUAEST.III is a header error — body is q2 tail; p.873 footers 1–5 → q2 [^13]–[^17], footers 6–8 → q3; q3 footer-5 *Vide scholion* resolved by q3 agent per q2's forwarded note) |
| **p.876** | **d37-a2-q3 → d37-dubia** | **CLEAN — PDF-verified**: q3 closes "…Et sic patent / quaesita[^18]" (grammatically continuous across p.875/876 break; [^18] is a p.875 footer); DUBIA CIRCA LITTERAM/Dub.I opens fresh; all p.876 dubia footers (n.1 Glossa-Rom → dubia [^1] onward) owned by dubia — no collision, none dropped |
| p.878 | d37-dubia → d38-littera | CLEAN (dubia closes before DISTINCTIO XXXVIII; p.878 NOTAE AD LIBR. footers → d.38 littera [^1]–[^5]; d.37-commentary `Hic dub.1.2.3.` note excluded) |
| p.880 | d38-littera → d38-divisio | CLEAN (Cap.IV closes before COMMENTARIUS; littera `nulli`-note → littera [^10]; NOTAE AD COMMENTARIUM block → divisio [^1]–[^4]; no duplication) |
| p.883 | d38-a1-q1 → d38-a1-q2 | CLEAN (q1 article-scholion consumes p.883 R-col footer band; q2 opens mid-p.883 with own fresh footers 1–3 → [^1]–[^3]) |
| p.885 | d38-a1-q2 → d38-a1-q3 | CLEAN (p.885 footers 1–8 → q2 [^18]–[^25]; footers 9–10 → q3 [^1]–[^2], hand-off matched both sides) |
| p.889 | d38-a1-q4 → d38-a2-q1 | CLEAN (shared p.889 footer band: q4 owns nn.1–4 [^11]–[^14], a2-q1 owns n.5 [^1]; ARTICULUS II opener folded into a2-q1 per §5) |
| p.891 | d38-a2-q1 → d38-a2-q2 | CLEAN (article scholion held by a2-q1; shared p.891 footers: q1 owns nn.1–3 [^13]–[^15], q2 owns nn.4–5 [^1]–[^2], hand-off matched) |
| **p.894** | **d38-a2-q2 → d38-dubia** | **CLEAN — PDF-verified**: L-col footer band shows exactly 6 footers; nn.1–4 (Dist.25; Vat.affectiva; Ps.69; Vide scholion) → q2 [^20]–[^23]; nn.5–6 (Isai.64/I Cor.2,9; Vide supra pag.194 — *sed voluntas…est absens*) → dubia [^1]/[^2]. q2 ends "Deus in adiutorium meum intende", Dub.I opens "In parte ista sunt quaestiones circa litteram" — continuous, no footer dropped |
| **p.896** | **d38-dubia → d39-littera (d.38 side)** | **CLEAN — PDF-verified**: Dub.IV closes "…probabiles et veri, si recte fuerint intellecti[^19]" (= printed p.896 footer n.2) before DISTINCTIO XXXIX; both p.896 dubia footers (nn.1–2 → [^18]/[^19]) accounted for; the p.896 NOTAE AD LIBR. block (nn.1–3) and R-col footer n.4 (*admittendum* variant) correctly excluded as d.39 material |

### Verification
- **Marker pairing**, all 18 d.37–d.38 chunks: La == En == defs, 0 orphans. (`d38-divisio` has a `[^10]` token inside its `## Notes` prose only — an explanatory cross-reference to the littera's note, not a body anchor; Latin/English/Apparatus all pair [^1]–[^4] cleanly.)
- **`audit-paraphrase --volume 2 --min-d 37 --max-d 38`:** 18 chunks, 0 critical / 0 high.
- **`audit-headers --volume 2 --min-d 37 --max-d 38`:** no LOSS flags (all positive diffs — expected Vol II).
- **`audit-apparatus-count --volume 2 --min-d 37 --max-d 38`:** 0 SUSPECT flags; all +diffs within the Vol II two-column cascade-footer triage band (max +13).
- **Smoke build** `node site/scripts/build-content.mjs`: `2 book(s), 875 questions, 839 translated` — parses cleanly.

No chunks edited this pass — all 15 seams CLEAN. The d.37–d.38 `## Notes` page-split / footer-map / cascade-dropout blocks are internally consistent (hand-off chains match across every adjacent pair) and the three PDF-spot-checked seams confirmed the Notes accurate to the printed footer text verbatim. Distinct from the d.31–d.36 sweep (which found dropped footers): the d.37 (sessions 37) and d.38 chunks were built under the strict per-subagent dispatch with explicit hand-off documentation, and no footer-accounting defect surfaced.

## Pass 3 (boundary sweep) — d.39–d.40

Independent cross-chunk boundary integrity sweep for d.39 and d.40 — the final segment of the d.31–d.40 decade (2026-05-31). Method: full marker-pairing audit across all 18 d.39/d.40 chunks (La == En == defs, 0 orphans); grammatical-continuity read of every adjacent seam (prior-chunk Latin tail vs receiving-chunk Latin head, watching for the cascade-merge broken-tail signature); PDF/OCR cross-check of the highest-risk footer-split seams (p.911 re-confirm of the Pass-1 recovery; p.896 d.39 side). **All 14 seams CLEAN — no fixes made.** Prior agents' notes that `d39-a2-q1` was footer-corrected in Pass 1 and `d39-divisio` anchors fixed in Pass 2 were re-confirmed internally consistent.

| Seam (shared printed p.) | Prior → next | Status |
|---|---|---|
| p.896 | d38-dubia → d39-littera (d.39 side) | CLEAN (DISTINCTIO XXXIX opens fresh "Samaritanus enim…"; littera claims its p.896/897 NOTAE AD LIBR. footers [^1]–[^9]; d.38-dubia footers stay with d38-dubia per the Pass-3 d.37–d.38 sweep) |
| p.897 | d39-littera → d39-divisio | CLEAN (littera closes Cap.III "…in quantum malum vult, malus est." before COMMENTARIUS IN DIST. XXXIX; divisio opens fresh; Pass-2 anchor fix `[^1][^5]` in divisio head verified internally paired) |
| p.898 | d39-divisio → d39-a1-q1 | CLEAN (divisio ends with TRACTATIO listing three questions; a1-q1 opens "Circa primum sic proceditur" continuous; ARTICULUS I/QUAESTIO I fresh) |
| p.905 | d39-a1-q2 → d39-a1-q3 | CLEAN (q2 closes scholion III; q3 opens QUAESTIO III "Tertio quaeritur de conscientia quantum ad effectum ligationis") |
| p.908 | d39-a1-q3 → d39-a2-q1 | CLEAN (q3 closes scholion II; ARTICULUS II "De synderesi" opens fresh with TRACTATIO; p.908 break sits inside q3 scholion I, footer accounted) |
| **p.911** | **d39-a2-q1 → d39-a2-q2** | **CLEAN — re-confirmed vs Pass-1 footer recovery**: a2-q1 holds the article-level scholion (I–II) + its 16 La-only variant defs [^1]–[^16] through the p.911 break; a2-q2 opens QUAESTIO II "Utrum synderesis per peccatum exstingui possit" with a fresh per-page footer sequence [^1]–[^16] (Quaracchi restarts numbering per printed page). No footer collision, none dropped — the Pass-1 24→27 marker correction stands |
| p.913 | d39-a2-q2 → d39-a2-q3 | CLEAN (q2 closes reply 4 "…tam conscientia quam synderesis[^16]" — no own scholion, which is expected per a2-q1 scholion II "Duae sequentes quaestiones … non habent difficultatem"; q3 opens QUAESTIO III fresh) |
| p.915 | d39-a2-q3 → d39-dubia | CLEAN (q3 closes reply 6 "…in abutente."; DUBIA CIRCA LITTERAM/Dub.I opens fresh; p.915 break inside dubia Dub.I body, accounted) |
| p.917 | d39-dubia → d40-littera | CLEAN (d39-dubia closes "…patent quae dicuntur in littera in hac parte."; DISTINCTIO XL / Cap. Unicum opens fresh) |
| p.919 | d40-littera → d40-divisio | CLEAN (littera closes the Augustine *quasi/velut* discussion; COMMENTARIUS IN DIST. XL opens fresh; p.919 break sits inside littera tail then divisio reopens p.919) |
| p.922 | d40-a1-q1 → d40-a1-q2 | CLEAN (q1 closes scholion II; q2 opens QUAESTIO II "Utrum quantum quis intendit, tantum faciat" mid-p.922 with own fresh footers) |
| p.924 | d40-a1-q2 → d40-a1-q3 | CLEAN (q2 closes replies Ad 3,4; q3 opens QUAESTIO III "Utrum intentio absque bonis operibus sufficiat…") |
| p.926 | d40-a1-q3 → d40-a2-q1 | CLEAN (q3 closes its Abelard/Council-of-Sens scholion; ARTICULUS II "De bonitate, quam opera superaddunt…" opens fresh with TRACTATIO folded into a2-q1) |
| p.933 | d40-a2-q3 → d40-dubia | CLEAN (q3 closes reply 6 "…Ex his patet responsio ad illud quod ultimo quaerebatur[^18]."; DUBIA CIRCA LITTERAM/Dub.I opens fresh; p.933 footer hand-off n.3 *Vide scholion* → dubia [^1] matches the resume-file hand-off, none dropped) |

### Verification
- **Marker pairing**, all 18 d.39–d.40 chunks: La == En == defs, 0 orphans. (`d39-a2-q1`'s 16 defs are La-only Quaracchi textual-variant notes — a pre-existing Pass-1 editorial choice, not a boundary defect; La/En body anchors still pair [^1]–[^16] cleanly.)
- **`audit-paraphrase --volume 2 --min-d 39 --max-d 40`:** 18 chunks, 0 critical / 0 high.
- **`audit-headers --volume 2 --min-d 39 --max-d 40`:** no LOSS flags (d.39 +1/+2/+2, d.40 +1/+2/+3 — all positive, expected Vol II).
- **`audit-apparatus-count --volume 2 --min-d 39 --max-d 40`:** 0 SUSPECT flags; +diffs within the Vol II two-column cascade-footer triage band (max +14).
- **Smoke build** `node site/scripts/build-content.mjs`: `2 book(s), 875 questions, 839 translated` — parses cleanly.

No chunks edited this pass — all 14 seams CLEAN. Every receiving chunk's opening sentence is grammatically continuous with the prior chunk's close (no cascade-merge broken tail anywhere), and shared-page footers are fully accounted for across each adjacent pair, with the p.911 split re-confirmed against the Pass-1 footer recovery and the p.933 → d40-dubia hand-off matched both sides.

## Decade gate CLOSED

The **d.31–d.40 three-pass decade polish-blocker is COMPLETE** (2026-05-31): Pass 1 (`[?]`-flag resolution, 600 dpi), Pass 2 (full-corpus style/formatting audit), and Pass 3 (cross-chunk boundary integrity sweep, 450 dpi column bands — d.31–d.38 swept by prior agents, 3 dropped footnotes found+fixed in d.31–d.36, d.37–d.38 clean; d.39–d.40 swept here, all 14 seams CLEAN) all close clean. **d.41 translation work is now UNBLOCKED.** Next action: `bon-sent-II-d41-littera` (DISTINCTIO XLI at raw line 64950).
