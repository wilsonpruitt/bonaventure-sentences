---
id: "bon-sap-scholion"
volume: 6
work: "sapientiam"
division: 20
type: scholion
title_la: "Scholion"
title_en: "Scholion"
printed_pages: [233]
pdf_pages: [275]
source: "S. Bonaventurae, Opera Omnia, Tomus VI (Quaracchi, 1893), p. 233"
has_scholion: false
has_apparatus: false
transcription_status: "Phase C Tier 2 complete — the work-level SCHOLION of the Commentarius in librum Sapientiae, p. 233 only (ruling 30: its own chunk, division 20, type scholion). Opens at the full-measure letter-spaced display heading SCHOLION. (~0.46 of the leaf, rows y 1380–1412), standing below the unanchored colophon Explicit postilla in librum Sapientiae., which stays with bon-sap-c19; six lines in two columns of smaller type (~0.51–0.55, three per column), closing on *…possunt suppleri.* at the foot of the RIGHT column (y 1632); below it only p. 233's footer rule (y 2056, x 676–1138) and white to the register (y 2448). End fixed positively from p. 234, extracted alone and read: its heading is SCHEMA I. (division 21, bon-sap-schemata). Profiled as its OWN region (the bon-itin-c7 rule): rows 0.51–0.55 give band 878–929 (52 px), centre-rule island 902–904, midpoint 903. Latin set from the 450 dpi plate on full-width and 1.5x column crops (raw L37995 SCHOLIOK). NO apparatus: no anchor in the six lines, and p. 233's whole register (nn. 1–6) is bon-sap-c19's. Zero marginalia, zero translator's notes, zero [?] flags (2026-10-16)."
format_version: 1
---

# Commentarius in librum Sapientiae — Scholion
## *Scholion*

---

## Latin
<!-- page 233 -->

### SCHOLION

Duo schemata, quae sequuntur, exhibent sub uno conspectu *principales* divisiones duarum partium, in quas auctor hunc librum dividit. Pro more commentatorum illius aetatis distinctio membrorum divisionis extenditur fere usque ad minimas particulas. Ob rationes typographicas pluries omisimus ultimas divisiones, quae facile ex notis marginalibus possunt suppleri.

## English
<!-- page 233 -->

### SCHOLION

The two schemata which follow exhibit under one view the *principal* divisions of the two parts into which the author divides this book. According to the custom of the commentators of that age, the distinction of the members of the division is extended almost down to the smallest particles. For typographical reasons we have several times omitted the last divisions, which can easily be supplied from the marginal notes.

---

## Notes

**SPAN — p. 233 ONLY, BOTH ENDS POSITIVE.** **Start:** the full-measure, centred, letter-spaced display heading `SCHOLION.` (rows y 1380–1412, ~0.46 of the leaf), set alone below the small-cap colophon `Explicit postilla in librum Sapientiae.` (~0.33), which carries no anchor and is rendered in `bon-sap-c19` (ruling 30). Between colophon and heading, and between heading and text, white. **Text:** six lines in two columns of smaller type, rows y 1534–1632 (~0.51–0.55), three lines per column: LEFT *Duo schemata… illius aetatis di-*, RIGHT *-stinctio membrorum… possunt suppleri.* — read on a full-width crop of rows 1360–1660 at 1.0× and on per-column crops at 1.5×. **What stands below the last line (measured, ink < 200 over rows 1640–2440, sheet-edge band excluded):** only the leaf's short centred footer rule at y 2056–2058 (x 676–1138, a 462 px run), then white to the register, which opens at y 2448. No ornament, no colophon. **End fixed from the next unit:** p. 234 extracted ALONE (450 dpi, 2067×2985, pHYs checked) and read on a ¼-scale view for structure only: running head `COMMENT. IN SAPIENTIAM.`, then the centred small-cap heading **`Schema I.`** at the head of the leaf, an upright bracket tree, and the part-title rotated up the left margin (*Pars I. Hortatio ad exercendam iustitiam sapientem*, read at ¼ scale only — for `bon-sap-schemata` to read properly). The prediction (Scholion ends on p. 233, `Schema I` on p. 234) measured TRUE.

**REGION — PROFILED AS ITS OWN (the `bon-itin-c7` rule).** `python3.11 tools/gutter-profile.py 233 0.51 0.55 vol6`: region too thin for the window consensus (step 3 decides); low-ink runs 878–901 (24) + 905–929 (25), **BAND 878–929 (52 px), midpoint 903**, centre-rule island 902–904 (3 px, peak 93). The 14 px-overlap column crops were cut at 903; no word lost at the cut. ⚠ **Correction to the resume note / `bon-sap-c19` Notes:** the "Scholion region 901 (rows 0.25–0.33)" figure there was taken over rows that hold the chapter's close and the `Explicit`, not the Scholion — the Scholion's text lies at rows 0.51–0.55. The body above measures 900/901 and the Scholion 903: two measures on one leaf, within 3 px. Recorded here; c19's file not edited.

**APPARATUS — NONE, MEASURED (the `bon-itin-scholion` shape).** The six lines were re-read for an anchor at 1.0× full width and 1.5× per column: **no superscript anywhere**; the one italic, *principales*, is unanchored. p. 233's footer register prints six notes (L nn. 1–4 head, R n. 4 tail + nn. 5–6), all answering anchors in Cap. XIX above the `Explicit`, all `bon-sap-c19`'s. `has_apparatus: false`, no anchors, no defs; `KNOWN_TOTALS_VOL6` unchanged (`233: 6`). Ledger row **`-`** (no footers, no runover possible).

**PRINTED FORMS:** `con-|spectu` and `di-|stinctio` (the second across the gutter) joined; the print sets a thin space before the commas after *partium* and *divisiones* (Quaracchi's spacing, not a mark) — not reproduced; *quatuor* does not occur (the Scholion says *Duo schemata*, against Ecclesiastes' four). *Pluries* → "several times".

**WHAT THE SCHOLION CLAIMS ABOUT THE SCHEMATA (for the `bon-sap-schemata` builder):** (1) **two** schemata (*Duo schemata*) = `Schema I` (p. 234) and `Schema II` (p. 235); (2) **one view of the principal divisions of the two parts** (*sub uno conspectu principales divisiones duarum partium*) — so Schema I = Pars I, Schema II = Pars II (ruling 30); (3) the distinction of the members runs **almost to the smallest particles** in the medieval manner; (4) ⚠ **the editors have SEVERAL TIMES OMITTED THE LAST DIVISIONS for typographical reasons, to be supplied from the marginal notes** — so a schema branch that stops short of the built chunks' marginalia is the editors' stated omission, not a defect to repair. ⚠ At ¼ scale Schema I visibly carries *supplicium* in its branches (*tangendo praemium iustitiae — supplicium iniustitiae*; *supplicium reproborum*) — gate item 1's census belongs to that chunk.

### Italic — expositio exceptions
Not applicable: the Scholion is editorial matter, not *expositio*.

### Italic — non-expositio sites
**A measured positive zero for SCRIPTURE:** the Scholion quotes no verse and has no guillemets. Its one italic, *principales*, is editorial emphasis on a term, not a quotation — so nothing is banked under the COLLECTION CHANGE.

### Register — sites censused over the BUILT file
- ***supplicium*: ZERO** (no *supplic-* form) — gate item 1 still five sites.
- ***lumen*/*lux*: ZERO** (no *lum-*/*luc-* form) — no `tr-lumen`.
- ***doctrina*: ZERO** — no `tr-doctrina` (ruling 53 not reached).
- ***studium*: ZERO** — ruling 54 not reached.
- ***vaca-*: ZERO**; *quies* family ZERO.
- *schema/schemata* ×1 → "schemata"; *divisio* ×3 → "division(s)"; *membrum* ×1 → "members"; *particula* ×1 → "particles"; *notae marginales* → "the marginal notes"; *conspectus* → "view" (the Ecclesiastes Scholion's *in uno conspectu* → "within a single view"); *auctor* → "the author"; *intellect-*, *magister*, *fundam.* ZERO.

### Marginalia
**ZERO, measured:** the region's ink (threshold 110) runs x = 121–1686 — the left column's flush lines to the right column's line-ends — with nothing outboard of either column across rows 0.51–0.55 (the colophon above and the body's marginalia belong to `bon-sap-c19`).

### For the p. 235 gate
No resolver sites: the Scholion cites nothing. Nothing forwarded to `bon-sap-schemata` but the claims above.
