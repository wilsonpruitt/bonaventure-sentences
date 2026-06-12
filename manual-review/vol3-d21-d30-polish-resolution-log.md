# Vol III — d.21–d.30 Decade-Polish Gate, PASS 1 of 3: `[?]`-flag resolution

**Date:** 2026-06-11
**Scope:** Vol III, distinctions 21–30 (chunks `bon-sent-III-d21-*` … `bon-sent-III-d30-*`).
**Gate:** First of the three locked-in passes (CLAUDE.md "Polish-blocker cadence"), fired by the close of Vol III d.30 (d30-dubia, commit 5a640e0). Pass 2 (full-corpus style/formatting audit) and Pass 3 (cross-chunk boundary-integrity sweep d.21–d.30) follow separately and remain blockers for d.31+.
**Method:** 600 dpi PDF eyes-on via `pdftoppm -r 600 -f PDF -l PDF -png raw/doctorisseraphic03bona.pdf …`, offset **pdf = printed + 22**. Crops staged under `/tmp/hires/` (footer bands + targeted body-column zooms, all under the API base64 cap).

> **Filename note.** The generic `manual-review/d21-d30-polish-resolution-log.md` is already in use as the **Vol II** d.21–d.30 log (2026-05-30). To avoid clobbering that history this Vol III log follows the established Vol III convention (cf. `vol3-d1-d10-…`, `vol3-d11-d20-polish-resolution-log.md`) and lives at `manual-review/vol3-d21-d30-polish-resolution-log.md`.

---

## Pass 1 — `[?]`-flag dispositions (the nine parked flags + the d27-q6 backfill)

| # | Chunk / location | Disposition |
|---|---|---|
| 1 | `d26-a2-q3` `[^7]` (p.573 n.9) | **RESOLVED @600dpi** (`p573-foot-R.png`). The *Mox pro dirigat … dirigit* clause is the **tail of a regular numbered note n.9** — `⁹ Cap. 7. n. 2. De propos. seq. cfr. infra q. 5; d. 27. a. 1. q. 1. et supra a. 1. q. 1. ad 1. — Mox pro dirigat non pauci codd. dirigit.` — NOT an "n. ad 9" addendum or n.9-bis. The prior def wrongly duplicated n.7's Augustine *Soliloquia* Latin and tagged `(P.573, n. ad 9.)`; def replaced with the true n.9 text, tag → `(P. 573, n. 9.)`. Body anchor on *caritas* (obj. 3) unchanged. |
| 2 | `d26-a2-q4` `[^7]` (p.576 n.3) | **RESOLVED @600dpi** (`p576-foot-L.png`). Footer prints `³ Vide infra d. 34. p. II. a. 2. q. 3.` exactly; cross-ref digits (d.34, p.II, a.2, q.3) confirmed correct. `[?]` removed; def unchanged. |
| 3 | `d27-a1-q2` (p.595 nn.5–11) | **RESOLVED @600dpi → BACKFILL** (`p595-foot-{L,R}.png`, `p595-Lbody-mid.png`, `p595-Rbody-mid.png`, `p595-Rtop.png`, `p595-Rad45.png`, `p595-n9full.png`). The prior "nn.5–11 are unanchored contextual cross-refs" claim was WRONG: each carries a distinct **printed body superscript** — ⁵ *illorum* (Ad-3), ⁶ *diversificari* (Ad-3), ⁷ *regulantur* (Ad-4), ⁸ *distinctione nona* (Ad-4), ⁹ *principalis obiecti* (Ad-5), ¹⁰ *praecedentibus* (Ad-6), ¹¹ *de Moribus Ecclesiae* (Ad-6). All seven were backfilled as `[^20]`–`[^26]` with matching La + En body anchors; apparatus 19 → **26 entries**; status updated. |
| 4 | `d28-a1-q2` `[^12]`,`[^13]` (p.625 nn.7,8) | **RESOLVED @600dpi** (`p625-foot-R.png`, `p625-n78-zoom.png`). n.7: the word edd. 1,2 add after *hinc est, quod caritas* is **`nihil`** (NOT *affectum*), then `Vat. naturalis` → `edd. 1, 2 addunt *nihil,* Vat. *naturalis.*`. n.8: `Mox pro *sub nomine* edd. *sub ratione.*` (also `pauci`→`non pauci codd. omittunt esse`). Both bracketed `[?]` cruxes corrected. |
| 5 | `d28-a1-q3` `[^13]` (p.627 n.9) | **RESOLVED @600dpi** (`p627-foot-R.png`, `p627-n9-zoom.png`/`p627-n9b-zoom.png`). Footer reads `⁹ Edd. addunt *et habilitate* et mox pro *ex hoc non sequitur* exhibent *ex hoc tamen non sequitur.*` Second variant lemma corrected to *ex hoc non sequitur* (from the conservative reconstruction *non sequitur, quod mali sint odiendi*); `[?]` removed. |
| 6 | `d24-littera` ⁶-vs-⁸ on *octavo libro de Trinitate* (p.507) | **RESOLVED @600dpi → ACCEPT (documented edition mis-set)** (`p507-sup8.png`, `p507-quoad.png`, `p507-foot.png`). The printed superscript is unambiguously **⁶** (single closed loop — a 6, not an 8), so it is NOT an OCR slip for ⁸. But by content the clause *octavo libro de Trinitate* is glossed by NOTAE **n.8** (`Libr. VIII. de Trin. c. 4. n. 6.`), while NOTAE **n.6** (`Cap. 4. n. 6. — Pro quo ad…`) is the *quo ad eum videndum* variant — and *quo ad eum videndum* carries **no printed in-text marker** (next printed digit is ⁷ on *diligatur*). This is a genuine **Quaracchi edition-level print mis-set**. Content-correct anchoring retained ([^p507-8] = source citation on *Trinitate*; [^p507-6] = *quo-ad* variant); the ⁶/⁸ discrepancy is documented, not silently emended. |
| 7 | `d30-a1-q5` `[^19]` (p.667 n.9) *ratione[?]* | **RESOLVED @600dpi → ACCEPT (Quaracchi's own printed query)** (`p667-foot-R.png`). The `[?]` is **Quaracchi's OWN printed editorial query mark**, not our transcription ambiguity: the footer prints `…quod homo est animal **ratione [?]** amicis benefaciens et inimicis malefaciens…`, the editors themselves setting `[?]` after *ratione* (they could not certainly read Albert's source). The word IS *ratione*; the `[?]` is reproduced verbatim (re-spaced `ratione [?]` to match the print). Not a flag to clear — a faithful transcription of an editorial query. |
| 8 | `d30-a1-q6` `[^15]` (p.669 n.7) | **RESOLVED @600dpi** (`p669-foot-R.png`). Footer prints `⁷ Ille in lit. Magistri. — Mox post *potest* cod. Z inserit *sic*.` exactly; provisional *inserit sic* confirmed; `[?]` removed. |
| 9a | `d30-dubia` `[^2]` (p.670 n.4) "pag. 311" | **RESOLVED @600dpi** (`p670-foot-L.png`). Footer prints `⁴ Cfr. supra pag. **311**, nota 1. — In fine arg. multi codd. et edd. 1, 2 omittunt *amicum et.*` The cross-ref page **311** is confirmed; reading correct as printed; `[?]` removed. |
| 9b | `d30-dubia` `[^10]` (p.671 n.6) "Codd. Z aa" | **RESOLVED @600dpi** (`p671-foot-R.png`, `p671-n6b-zoom.png`). Footer prints `⁶ Codd. **Z aa** adiungunt *sibi*.` — the second siglum is clearly **aa** (the doubled-minuscule codex siglum cited elsewhere on this page), NOT "ad". Reading correct as printed; `[?]` removed. |

**Tally:** **6 RESOLVED (corrected/confirmed reading)**, **2 ACCEPT-as-printed** (flag #6 documented edition mis-set; flag #7 Quaracchi's own printed query), **1 RESOLVED-via-backfill** (flag #3, 7 new apparatus entries). All nine parked `[?]` markers cleared from the chunk bodies/apparatus; each chunk's `## Notes` carries the disposition.

---

## d27-q6 p.615 footer backfill — verification

The `d27-a2-q6` "p.615 footer backfill (2026-06-11)" restored p.615 nn.1–4 as `[^14]`–`[^17]` (q6's tail share). **VERIFIED at 600 dpi** (`/tmp/hires/p615-foot-L.png`): the p.615 footer sequence runs nn.1–17 contiguously, split by body anchor at the top-of-page q6 tail vs the DUBIA below —
- **n.1** = `…pro in quo potest cod. Z quia potest. Inferius etiam pro iustis omnibus codd. A K Z et edd. iustis hominibus.` → q6 `[^14]` ✓
- **n.2** = `Cfr. August., de Spiritu et littera, c. 36. n. 66.` → q6 `[^15]` ✓ (the d27-dubia stale note's "n.196" was wrong; correct is **n.66**)
- **n.3** = `Hic c. 6.` → q6 `[^16]` ✓
- **n.4** = `Vide scholion ad praecedentem quaest.` → q6 `[^17]` ✓
- **n.5** = `Secundum Aristot., VI. Topic. c. 3. (c. 4.). Vide supra pag. 504, nota 2.` → d27-dubia `[^p615-5]` ✓ (first Dubia note)

The backfill is **correct**. The now-stale open-flag bullet in `d27-dubia` (`[?] q6 p.615 footers nn.1–4 … appear genuinely dropped`) was updated to mark the gap RESOLVED/backfilled and verified; d27-dubia's own apparatus (nn.5–17) was NOT otherwise altered.

---

## Build + audit status

- `cd site && node scripts/build-content.mjs`: parses clean; translated count held at **1186** (resolving flags + backfilling apparatus does not change translated-chunk count).
- Three guard-rail audits `--volume 3 --min-d 21 --max-d 30` (paraphrase / headers / apparatus-count): **no NEW flags**.

**Pass 1 status: CLOSED.** No unresolved `[?]` flags remain in Vol III d.21–d.30. Passes 2 and 3 still pending — d.31+ dispatch remains blocked until all three close.
