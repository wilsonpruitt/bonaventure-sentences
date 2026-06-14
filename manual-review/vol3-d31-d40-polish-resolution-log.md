# Vol III — d.31–d.40 Decade-Polish Gate, PASS 1 of 3: `[?]`-flag resolution

**Date:** 2026-06-14
**Scope:** Vol III, distinctions 31–40 (chunks `bon-sent-III-d31-*` … `bon-sent-III-d40-*`).
**Gate:** First of the three locked-in passes (CLAUDE.md "Polish-blocker cadence"), fired by the close of Vol III d.40 (d40-dubia, commit `3d2dc55`) — the FINAL decade gate for Vol III (Book III now fully Tier 2). Pass 2 (full-corpus style/formatting audit) and Pass 3 (cross-chunk boundary-integrity sweep d.31–d.40) follow separately and remain blockers for any further work (Vol IV / Book IV).
**Method:** 600 dpi PDF eyes-on via `pdftoppm -r 600 -f PDF -l PDF -png raw/doctorisseraphic03bona.pdf …`, offset **pdf = printed + 22**. Full-page renders staged in `/tmp/hires/`, cropped to column-footer bands with PIL (capped under the API base64 limit).

> **Filename note.** The generic `manual-review/d31-d40-polish-resolution-log.md` name is reserved for the Vol II convention. Per the established Vol III convention (cf. `vol3-d1-d10-…`, `vol3-d11-d20-…`, `vol3-d21-d30-polish-resolution-log.md`) this log lives at `manual-review/vol3-d31-d40-polish-resolution-log.md`.

---

## Pre-scan: d.31 and d.32 — CLEAN

Grepped every `## Notes` block in `bon-sent-III-d31-*` (12 chunks) and `bon-sent-III-d32-*` (10 chunks) for `[?]` flag entries. **All read "None"/"none"** — the only inline `[?]` occurrences are the literal "`[?]` flags: none" status strings (frontmatter + Notes). No genuine parked flag exists in d.31 or d.32. (Two non-flag editorial asides were noted and left: `d32-a1-q4` documents that note [^4]'s `supra pag. 39` cross-ref target was not re-verified — its text is clean and this is explicitly *not* a flag.) Per dispatch, the `tier2-ambiguities-d31-*/d32-*` files in `manual-review/` are Vol I's pars-split logs, NOT Vol III — ignored. **d.31 and d.32 confirmed clean; no 600 dpi work needed.**

---

## Pass 1 — `[?]`-flag + parked-apparatus dispositions (the confirmed d.33–d.39 worklist)

| # | Chunk / location | Disposition |
|---|---|---|
| 1 | `d33-a1-q4` `[^8]` (p.719 R-col nn.8–9) | **RESOLVED @600dpi** (`/tmp/hires/v3p719-Rfoot2.png`, `v3p719-n89.png`, `v3p719-n9last.png`; PDF 741). The consolidated [^8] joins p.719 R-col **n.8** (`Pro nec videntur theologicae edd. ut videtur.`) + **n.9** (`Codd. et edd. 1, 2 non ita bene *rationales* et mox *rationalem;* multi codd., cum abbreviate scribant, sunt dubiae interpretationis.`). The formerly parked, OCR-degraded clause (provisionally `iam iste bene rationabiles… intelligunt`) was a 450 dpi garble; the true reading is the *rationales / rationalem* variant. Both clauses of [^8] re-set faithfully (La + En); `[?]` cleared; Notes corrected (the band runs nn.1–9, not nn.1–8 — L-col nn.1–6, R-col nn.7–9). |
| 2 | `d33-a1-q5` `[^23]` (p.724 L-col n.1) | **RESOLVED @600dpi → CORRECTED ANCHOR + TEXT** (`/tmp/hires/v3p724-Lfoot.png`, `v3p724-n12full.png`, `v3p723-Rfoot.png`, `v3p723-n5c.png`, `v3p723-qdigit.png`). The parked [^23] had wrongly **duplicated [^18]'s** Serm. 30 / Hypognosticon note and tagged it "p.724 n.3 / d. 26. q. 3 / Paulo ante post pag. 600 nota laudatur" (a reconstruction). On 600 dpi: the Serm. 30 note appears **once** in print, as **p.723 R-col n.5 = [^18]**; its tail is `Paulo ante posuimus ex codd. A T U equum circumducere pro equum suum ducere, quod est in aliis et edd.` and its cross-ref digit is **d. 26. q. 5** (long-tail Quaracchi 5), not q.1. The true **[^23]** = **p.724 L-col n.1** (`Cfr. II. Sent. d. 25. p. I. q. 2. ad 5. — Cod. A et Supplement. Sum. Alex. Hal. assuefit; edd. verbo assuescit praemittunt minus. Superius pro comparationes codd. A H L aa bb operationes.`), which anchors on *secundum diversas comparationes* in the q5 body. [^23] replaced with this faithful text; [^18]'s `q. 1`→`q. 5` corrected; Notes map updated; `[?]` cleared. |
| 2b | `d33-a1-q5` `[^1]` Greek string | **RESOLVED @600dpi** (`/tmp/hires/v3p721-greek2.png`; PDF 743, p.721 R-col n.6). The Aristotle Greek now reads `ἀλλὰ περισσότεροι μὲν ἡμῖν δέξασθαι αὐτάς, τελειουμένοις δὲ διὰ τοῦ ἔθους` — the missing `ἡμῖν` added and `τελειούμενοι`→`τελειουμένοις` (dat. pl.) corrected; breathings/accents confirmed (both La + En). Low-confidence flag cleared. |
| 2c | `d33-a1-q5` `[^19]` sigla | **RESOLVED @600dpi** (`/tmp/hires/v3p723-n67.png`; PDF 745, p.723 R-col n.6). Footer reads `Edd. habilitantem. Proxime post pro potentiam cod. bb potentias.` — corrected `cod. III`→**`cod. bb`** and `potentiae`→**`potentias`**. Low-confidence sigla flag cleared. |
| 3 | `d38-dubia` p.857 L-col nn.3–5 under-capture (Dub. IV Jacob/Esau) | **RESOLVED @600dpi → BACKFILL** (`/tmp/hires/v3p857-Lfoot.png`, `v3p857-Lbody.png`, `v3p857-Lbody2.png`; PDF 879). p.857 prints **two** `NOTAE AD LIBR. SENTENTIARUM` blocks: the **L-col** block (nn.1–5) is entirely the d38 Jacob/Esau dubium's (the dubium body runs the full L-col, ending *…virum simplicem, non dolosum*); the **R-col** block (nn.1–3) is d39-littera's (Cap. I/II/III). d38-dubia had stopped at L-col n.2 ([^29]). The three missing L-col notes were **backfilled as [^30]–[^32]**: n.3 `Cfr. supra pag. 570, nota 6.` → [^30]; n.4 `In edd. additur in Spiritum sanctum. Paulo inferius pro hoc modo, quod cod. K omittit, codd. A Z bb sermo, codd. G H L T primo. Subinde post aliud edd. supplent tamen.` → [^31]; n.5 `Gen. 27, 27. seqq. et 28. 3. seq. — Idem dub. solvit Alex. Hal., S. p. II. q. 123. m. 6; B. Albert., hic a. 9; S. Thom., hic a. 3. ad 1; Petr. a Tar., hic a. 5; Richard. a Med., hic q. 2. ad 2.` → [^32]. Body anchors placed at the Dub. IV close (n.3/n.5 = unanchored editorial cross-ref + parallel-loci notes per Quaracchi convention, clustered at the dubium end; n.4 = the *in Spiritum sanctum* variant, anchored on *mendacium*). Apparatus 29→**32**, marker pairing 32/32. d38-dubia Notes corrected (the old claim that nn.3–5 were d39's was wrong); **d39-littera Notes updated to mark the under-capture RESOLVED.** |
| 4 | `d38-divisio` p.839 L-col n.1 *omni* parked fix | **RESOLVED @600dpi → BACKFILL** (`/tmp/hires/v3p839-Lfoot.png`; PDF 861). p.839 L-col footer **n.1** = `Cod. K omittit omni, quod econtra Vat. paulo inferius adiungit.` This is divisio's note (it keys to the TRACTATIO's first question `utrum essentiale sit omni mendacio esse falsum`, printed at the top of p.839), which the committed divisio chunk had missed (it had wrongly recorded "p.839 carries NO footer markers"). Added as **[^4]** anchored on *omni* (La + En); apparatus 3→**4**, marker pairing 4/4. Notes (apparatus map + footer hand-off + flags) corrected; the matching retro-fix flag in `d38-a1-q1` Notes marked RESOLVED (a1-q1 correctly owns p.839 nn.2–8; its [^1] = p.839 n.2, unchanged). |

**Tally:** **6 RESOLVED** readings/corrections ([^8] variant clause; [^23] anchor+text; [^18] q-digit; [^1] Greek; [^19] sigla) **+ 2 RESOLVED-via-backfill** apparatus additions (d38-dubia [^30]–[^32]; d38-divisio [^4]). **d.31 and d.32 confirmed clean.** All inline `[?]` markers cleared from the affected chunk bodies/apparatus; each chunk's `## Notes` carries the disposition; the cross-chunk discrepancy notes (d39-littera, d38-a1-q1) updated to RESOLVED. No ACCEPT-ILLEGIBLE items — every parked item was legible at 600 dpi.

---

## Build + audit status

- `cd site && node scripts/build-content.mjs`: parses clean; translated count held at **1287** (resolving flags + backfilling apparatus does not change translated-chunk count; no new chunks). Marker pairing N/N preserved on the d33-a1-q4, d33-a1-q5, d38-dubia, and d38-divisio chunks after the apparatus edits (d38-dubia 32/32, d38-divisio 4/4).
- Three guard-rail audits `--volume 3` for the affected distinctions (`--min-d 33 --max-d 33`, `--min-d 38 --max-d 38`) + headers + apparatus-count: **no NEW flags** (the d38-dubia apparatus-count diff *improved* — the heuristic's ~31-opener flag is now matched by the corrected 32-entry truth).

**Pass 1 status: CLOSED.** No unresolved `[?]` flags remain in Vol III d.31–d.40. Passes 2 (full-corpus style/formatting) and Pass 3 (cross-chunk boundary integrity, d.31–d.40) still pending — any further work (Vol IV) remains blocked until all three close.

---

## PASS 2 of 3 — Style/Formatting Audit (full corpus) — CLOSED 2026-06-14

Full report: `manual-review/vol3-d31-d40-pass2-style-audit.md`. Programmatic scan of **1287 chunks** (1260 Tier-2; 27 skeletons) via `tools/audit-style-formatting.py` + supplemental `/tmp/pass2_scan.py` (item-8 suffix scheme + git-tracked-backup checks).

- **FIXED — known fix (item 8):** `d39-a3-q3` apparatus renumbered from per-page suffix scheme `[^1b]–[^9b]` to continuous integers `[^13]–[^21]` (full sequence now `[^1]`–`[^21]`, **pairs 21/21** La/En/defs). Content verbatim; only numbers + the descriptive prose (status string, blockquote, Notes) changed; stale `27/27` Notes count corrected to `21/21`.
- **CLEAN:** frontmatter fields, `Phase C Tier 2 complete —` prefix, standard sections, page-breaks — 0 flags corpus-wide.
- **LOGGED (no fix):** `orphan_app_defs` (10 chunks) = benign unanchored editorial/cross-ref notes + a blockquote-literal false positive (`d33-dubia [^33]`) — accepted; `d27-p1-a1-q2` scholion-order = likely false positive (Vol I, out of scope, build clean); `d33-dubia` `**En.**` 5/6-space indent mix (parser-tolerant, "don't bulk-edit"); 2 git-tracked backup artifacts (`git rm --cached` candidate); the **corpus-wide `[^Nx]` suffix convention (39 chunks** incl. two in-scope d.33 single-interpolation cases `d33-a1-q3 [^6b]`, `d33-a1-q5 [^14b]`) — deferred to a single owner decision (normalize all vs accept the per-page-restart convention); piecemeal fixes would *increase* inconsistency.
- **Build:** clean, 1287/1287 translated. **Audit:** `audit-apparatus-count --volume 3 --min-d 39 --max-d 39` → 0 flags.

**NEXT ACTION on the polish blocker:** Pass 3 (cross-chunk boundary-integrity sweep, d.31–d.40) — still a blocker for Vol IV / Book IV.

---

## PASS 3 of 3 — Boundary integrity (d.31–d.35) — CLOSED 2026-06-14

**(Pass 3a; d.36–d.40 follow in Pass 3b.)** Method per CLAUDE.md Pass 3 + VOL II/III OVERRIDE: for every chunk boundary that falls inside a printed page (two adjacent chunks sharing a `printed_pages` number), checked the three integrity criteria against 450 dpi PDF column bands (`tools/extract-pages.py --volume vol3 --pages N --dpi 450` → `tools/colcrop.py vol3 N` → `/tmp/colcrop/vol3-pNNN-{L,R}-{0..n}.png`; offset pdf = printed + 22): **(a)** receiving chunk's opening grammatically continuous with prior chunk's closing (no dropped clause); **(b)** the shared page's Quaracchi footer notes fully accounted across both chunks' `## Apparatus`/`## Notes` hand-off blocks (none dropped/double-counted; Quaracchi restarts numbering per page and per column); **(c)** no OCR cascade-merge splice signature in the prior chunk's tail.

**Boundaries checked: 51 total across d.31–d.35 (41 mid-page, requiring 450 dpi eyes-on; 10 page-aligned, continuity-glance from Notes only).** Per-distinction: d.31 = 11 (8 mid-page), d.32 = 8 (8 mid-page), d.33 = 8 (7 mid-page), d.34 = 16 (13 mid-page + inter-pars p1→p2 + 2 page-aligned), d.35 = 8 (5 mid-page + 3 page-aligned). Dispatched one subagent per distinction, each doing the full 450 dpi column-band discipline.

### Per-distinction verdict

- **d.31 — ALL CLEAN (8 mid-page seams).** littera→divisio→a1q1 are legitimate structural breaks (Lombard / COMMENTARIUS+DIVISIO / first quaestio); footer families disjoint and accounted (p.673 *Notae ad Libr. Sent.* nn.1–2 → littera, *Notae ad Comm.* n.1 → divisio, nn.2–3 → a1-q1). q-to-q seams continuous; the two-sequence footer splits on p.685 (a2q2 nn.1–7 / a2q3 nn.8–10), p.692 (a3q2 spill-notes / a3q3 nn.1–10), p.694 (a3q3 nn.1–6 / dubia nn.7–10) all verified eyes-on, no double-count. All 11 chunks' apparatus defs contiguous. No splice.
- **d.32 — ALL CLEAN (8 mid-page seams).** Every prior tail parses; every receiving head is a fresh quaestio/section header or continuous. Footer accounting exact, incl. the p.705 case where q4's scholion §III body crosses the page but carries no footer there (verified eyes-on: NOTAE restarts at n.1, entirely q5's — no q4 footer dropped). Hand-off blocks internally consistent across all 9 files. No splice.
- **d.33 — ALL CLEAN (7 mid-page + 1 page-aligned).** Independently re-confirmed the Pass-1 apparatus corrections at the q4 (p.719 nn.7–9 → [^7]/[^8]) and q5 (p.721 L nn.1–5 / R nn.6–7 split; Greek in n.6 = q5 [^1]) seams against 450 dpi bands — those were footer-text/anchor corrections internal to q4/q5, not seam dropouts; the seams themselves are intact. a1q6→dubia page-aligned (q6 closes p.727, dubia opens top of p.728). No splice.
- **d.34 — ONE FIX (13 mid-page + inter-pars + 2 page-aligned).** **Fixed a footer DOUBLE-COUNT at the p2 a1q3→a2q1 seam (shared p.761):** `d34-p2-a2-q1` had wrongly claimed p.761 nn.1–4 as its leading apparatus `[^1]–[^4]` with 4 spurious body anchors. Eyes-on `/tmp/colcrop/vol3-p761-{L,R}-{0,1}.png` (PDF 783) confirms PDF markers ¹–⁴ sit in q3's replies 2–4 (already correctly held by `d34-p2-a1-q3` as its `[^25]–[^28]`); markers ⁵–⁸ sit in a2-q1's Fundamenta args (⁵ *divisionem Magistri*, ⁶ *Augustini*, ⁷ *Magister innuit*, ⁸ *modum timendi*). Removed the 4 phantom apparatus entries + 4 spurious anchors and remapped a2-q1's real notes (p.761 nn.5–8 + p.762 nn.1–12 + p.763 nn.1–4) to a contiguous `[^1]–[^20]` (now 20 La / 20 En / 20 defs, 1:1:1). **No body Latin/English text added or lost — marker/footer accounting only.** Backup at `vol3/_backup-d34-p2-a2-q1-pre-cascade-fix-20260614/`; fix documented in that chunk's `## Notes` + a seam-confirmation note added to `d34-p2-a1-q3`'s Notes. All other 12 mid-page seams + inter-pars (p1-dubia p.752 → p2-divisio p.753, no shared page) + the 2 page-aligned seams CLEAN; footer splits on p.741, p.747, p.759 verified eyes-on.
- **d.35 — ALL CLEAN (5 mid-page + 3 page-aligned).** Interleaved-by-anchor footer split on p.775 (q1 [^15]/[^16] vs q2 [^1],[^4]–[^7], with a documented [^2]/[^3] gap) reconciled exactly; p.777, p.782 splits accounted. The article-master scholion chain (q1 §II→q2, q3 §II→q4, q5 §II→q6, each confirmed by the source's own *Vide scholion ad praecedentem quaest.* redirect markers) is intact. No splice.

### Fix summary

| Seam | Chunk(s) edited | What | PDF citation |
|---|---|---|---|
| d.34 p2 a1q3→a2q1 (shared p.761) | `d34-p2-a2-q1` (renumber [^1]–[^20], drop 4 phantom defs+anchors); `d34-p2-a1-q3` (Notes seam-confirm) | Footer double-count: p.761 nn.1–4 belong to a1-q3, not a2-q1. No body text changed; pairing now 20/20/20. | `/tmp/colcrop/vol3-p761-{L,R}-{0,1}.png`, PDF 783 (printed 761) |

No ACCEPT-ILLEGIBLE items — every band read cleanly at 450 dpi.

### Build + audit status (post-fix)

- `tools/audit-apparatus-count.py --volume 3 --min-d 31 --max-d 35`: **0 flags.**
- `tools/audit-paraphrase.py --volume 3 --min-d 31 --max-d 35`: 56 chunks, **critical 0 / high 0.**
- `tools/audit-headers.py --volume 3 --min-d 31 --max-d 35`: no LOSS flags (all diffs positive, expected for Vol III).
- `cd site && node scripts/build-content.mjs`: parses clean, **0 marker-pairing warnings, 1287/1287 translated.**

**Pass 3a status: CLOSED.** All 51 d.31–d.35 boundaries verified clean except one footer double-count (d.34 p2, fixed). **NEXT ACTION on the polish blocker:** Pass 3b — boundary-integrity sweep d.36–d.40 (still a blocker for Vol IV / Book IV).

---

## PASS 3b — Boundary integrity (d.36–d.40) — d.38 verdict (2026-06-14)

*(d.38 scope only; d.36 / d.37 / d.39 / d.40 logged by their own per-distinction agents.)* Method per CLAUDE.md Pass 3 + VOL II/III OVERRIDE, 450 dpi column bands (`/tmp/colcrop/vol3-pNNN-{L,R}-*.png`, offset pdf = printed + 22), running-head TEXT trusted over OCR digits. d.38 = single-article distinction (ARTICULUS UNICUS, a1-q1..q6). 9 chunks; **8 mid-page seams** (all share a printed page) + the two inter-distinction glances (d.37→d.38 lead-in p.836; d.38→d.39 tail p.857).

### d.38 — ALL CLEAN (8 mid-page seams)

- **littera→divisio (p.838).** Continuous: littera's Cap. VI Jacob/Esau tail (Lombard) → COMMENTARIUS opener `Sciendum tamen, tria esse genera mendaciorum etc.` (= divisio's first line). Footer: p.838 prints **two disjoint** NOTAE blocks (verified `/tmp/colcrop/vol3-p838-R-2.png`) — L-col *Notae ad Libr. Sent.* nn.1–3 → littera [^9]–[^11] (August./Enchirid./Contra Mendac.); R-col *Notae ad Commentarium* nn.1–3 → divisio [^1]–[^3] (`Scilicet infra d. XXXIX.` / `Edd. ibi…` / `Vat. peccati.`). No overlap, no double-count.
- **divisio→a1-q1 (p.839).** Continuous: TRACTATIO → `Circa primum sic proceditur… utrum essentiale sit mendacio esse falsum`. Footer (verified `/tmp/colcrop/vol3-p839-L-2.png`): p.839 L-col **n.1** = `Cod. K omittit omni…` = divisio [^4] (Pass-1 backfill, anchored on *omni*); **n.2** = `Cap. 3. n. 3… contra Mendacium…` = a1-q1 [^1]. a1-q1 correctly opens its band at n.2; the *omni* note is NOT double-claimed.
- **a1-q1→a1-q2 (p.841)** · **q2→q3 (p.845)** · **q3→q4 (p.847)** · **q4→q5 (p.850)** · **q5→q6 (p.852)** · **q6→dubia (p.854).** All six are question-boundaried (each receiving chunk opens with its TRACTATIO stem — *Secundo/Tertio/Quarto/Quinto/Sexto et ultimo quaeritur…*), so no mid-sentence cascade-merge risk; every prior tail parses. Per-page footer bands restart per question and are forwarded by body-anchor exactly as documented in each chunk's `## Notes` (q1→q2 forwards p.841 nn.3–4; q6→dubia forwards p.854 nn.5–8); no dropped/double-counted footer. The article-master scholion chain (q1 §I–III, q4 §I–III) with the *Vide scholion ad praecedentem/4./1. quaest.* redirects is intact — `has_scholion: false` on q2/q3/q5/q6 is the source's intended redirect, not a dropout.

### Pass-1 backfill re-confirmation (independent eyes-on, NOT redone)

- **(i) d38-dubia [^30]–[^32] = p.857 L-col nn.3–5.** Confirmed @450 dpi (`/tmp/colcrop/vol3-p857-L-{1,2}.png`): p.857 L-col carries **two** stacked blocks — the Jacob/Esau dubium body ends `…virum simplicem, non dolosum`, then the L-col *Notae ad Libr. Sent.* prints nn.1–5 (`Cod. A enim.` / `Gen. 25,27…` / `Cfr. supra pag. 570, nota 6.` / `In edd. additur in Spiritum sanctum…` / `Gen. 27,27. seqq.… Idem dub. solvit Alex. Hal.…`) = dubia [^28]–[^32] verbatim. d39-littera's [^1]–[^5] are the **R-col** block (Hieron./Apostolus/August. *de periurio*) — d39-littera does NOT claim the L-col notes. **Correctly anchored, no double-count across the p.857 seam.**
- **(ii) d38-divisio [^4] = p.839 n.1 *omni*.** Confirmed @450 dpi (`/tmp/colcrop/vol3-p839-L-2.png`): n.1 `Cod. K omittit omni…` is divisio's, anchored on *omni* in both bodies (La line, En `every`), def at [^4]; a1-q1's band starts at p.839 n.2 ([^1] = the *de Mendacio* note). **Correctly anchored, not double-counted at the divisio→a1-q1 seam.**

### d.38 fixes / illegible

**NONE.** All 8 mid-page seams continuous, all footer accounting exact, both Pass-1 backfills correctly anchored and singly-counted. No body text dropped, no cascade-merge splice, no ACCEPT-ILLEGIBLE (every band read cleanly at 450 dpi). No chunk files edited.

---

## PASS 3b — Boundary integrity (d.39) — verdict (2026-06-14)

*(d.39 scope only, incl. d.38→d.39 + d.39→d.40 seams and the two inter-article seams.)* Method per CLAUDE.md Pass 3 + VOL III OVERRIDE, 450 dpi column bands (offset pdf = printed + 22), running-head TEXT over OCR digits. d.39 = three-article distinction; 12 chunks. **Mid-page + inter-article seams checked (9):** littera→divisio (p.860), divisio→a1-q1 (p.861), a1-q1→q2 (p.863), a1-q2→q3 (p.865), **a1-q3→a2-q1 (p.866, INTER-ARTICLE)**, a2-q2→q3 (p.872), **a2-q3→a3-q1 (p.874, INTER-ARTICLE)**, a3-q2→q3 (p.878), a3-q3→dubia (p.880). **Page-aligned (glance only, 3):** a2-q1→a2-q2 (870), a3-q1→a3-q2 (877), d.39-dubia→d.40-littera (883). **Inter-distinction:** d.38→d.39 share p.857.

### Per-seam verdicts

- **d.38→d.39 (p.857, INTER-DISTINCTION) — CLEAN (eyes-on).** p.857 prints TWO disjoint NOTAE AD LIBR. SENTENTIARUM blocks (confirmed `/tmp/colcrop/vol3-p857-{L,R}-2.png`): L-col nn.1–5 = d38-dubia's Jacob/Esau dubium ([^28]–[^32], incl. the Pass-1 backfill [^30]–[^32]); R-col nn.1–3 = d39-littera's perjury Cap. I/II/III ([^1]–[^3], Hieron./Apostolus/August.). No overlap, no double-count. d38 closes *…virum simplicem, non dolosum*; d39-littera opens fresh `Cap. I De periurio` — correctly discontinuous at the distinction boundary. d38-dubia 32/32 paired post-backfill.
- **a1-q3→a2-q1 (p.866, INTER-ARTICLE) — CLEAN.** a1-q3 owns p.866 nn.1–5 ([^12]–[^16]); a2-q1 opens at p.866 n.6 ([^1] *Vers.34/Iac.5,12*) + n.7 ([^2] Serm.180). No double-count, no gap.
- **a2-q3→a3-q1 (p.874, INTER-ARTICLE) — CLEAN.** a2-q3 closes at p.874 n.3 ([^20]); a3-q1 opens at p.874 n.4 ([^1] *Hic c.11*). Clean split.
- **a3-q2→a3-q3 (p.878) — DEFECT FOUND + FIXED (see below).**
- **a3-q3→dubia (p.880) — CLEAN.** a3-q3 owns p.880 nn.1–9 ([^13]–[^21]); dubia's apparatus starts on p.881; p.880's footers are wholly a3-q3's (dubia opener bears no markers). Documented in dubia `## Notes`.
- **Remaining mid-page seams (littera→divisio 860, divisio→a1-q1 861, a1q1→q2 863, a1q2→q3 865, a2q2→q3 872) — CLEAN.** Each receiving chunk opens with its TRACTATIO stem / fresh per-page band; footer hand-offs documented in `## Notes` match the band; prior tails parse (no cascade-merge).
- **Page-aligned glances (870/877/883) — CLEAN.** Fresh bands; no shared-page footer.

### Post-normalization pairing check (Pass-2 carry-over)

- **a3-q3 (continuous run):** 21/21 paired AFTER the fix below; no orphans, no dup defs.
- **a2-q1 (b/c/d suffix scheme):** 27/27 paired, every def has anchors in BOTH bodies, no dup defs. NOTE: the brief stated Pass 2 normalized a2-q1's b/c/d suffixes to continuous integers; in fact the b/c/d scheme is STILL present in the file (and its `## Notes` still describe it). This is not a boundary defect — pairing is perfect — so left as-is (out of Pass-3b scope to renumber); flagging for the owner if continuous-integer normalization is desired.

### FIX — d39-a3-q3 apparatus (p.878/p.879 footer attribution)

Two seam defects at the a3-q2→a3-q3 (p.878) boundary, both corrected (backup `vol3/_backup-d39-a3-q3-pre-pass3b-20260614/`):
1. **DOUBLE-COUNT.** a3-q3 defs [^1]–[^6] held p.878 nn.1–6 (*Cfr. quaest. praec.* / II Sent. d.25 / IV Sent. d.38 / Matth 10,28 / Eph 5 / Dist.29-redirect) — these are **a3-q2's** footers (its [^10]–[^15]). 450 dpi `/tmp/colcrop/vol3-p878-{L,R}-{0,2}.png`: p.878's footer column is ONE continuous band nn.1–10; nn.1–6 key q2's Respondeo/Solutio (upper p.878), nn.7–10 key q3's body (lower p.878). q3's body markers [^1]–[^4] were thus mis-glossed with q2's notes.
2. **DROPPED FOOTERS.** p.879 nn.1–6 had been omitted ("folded away" in a prior note), but q3's p.879 body carries 8 markers and p.879 prints 8 footers (`/tmp/colcrop/vol3-p879-{L,R}-2.png`: L-col nn.1–5 + R-col nn.6–8).

Re-keyed: [^1]–[^4] = p.878 nn.7–10 (Bede-fundam. / Ambros. de Officiis / supra pag.666 / De Bono coniugali); [^5]–[^12] = p.879 nn.1–8 (Gratian Innocens credit / Hic c.9 / Isid. *sacramentum pro iuramentum* / supra pag.875 variant pair / Archidiac. Florentinum dist.85 / incauto / Cod.A repugnat); [^13]–[^21] = p.880 nn.1–9 (unchanged). Body anchors unchanged (21, already correct); only the 12 definitions [^1]–[^12] rewritten. Result 21/21 paired; each p.878 footer now appears exactly once across a3-q2+a3-q3. PDF cite: p.878 L-2/R-2 + p.879 L-2/R-2 bands.

### d.39 ACCEPT-ILLEGIBLE

NONE — pp.857–882 read cleanly at 450 dpi.

---

## PASS 3b — d.37 boundary integrity sweep (2026-06-14)

d.37 = TWO-article distinction (Art. I a1-q1/q2/q3 + Art. II a2-q1/q2/q3), not a pars-split. Chunks: littera · divisio · a1-q1/q2/q3 · a2-q1/q2/q3 · dubia.

**Boundaries checked: 9.** Mid-page (450 dpi eyes-on where a defect surfaced): divisio→a1-q1 (p.812), a1-q1→a1-q2 (p.815), a1-q2→a1-q3 (p.818), **a1-q3→a2-q1 (p.821, INTER-ARTICLE)**, a2-q1→a2-q2 (p.825), a2-q2→a2-q3 (p.827), a2-q3→dubia (p.829). Page-aligned (continuity glance): littera→divisio (811→812), dubia tail→d.38 (836).

**Per-seam verdicts:**
- littera→divisio (811→812, page-aligned): PASS. Littera closes Cap. VI (*…utrum prohibitum sit omne mendacium…*); divisio opens fresh COMMENTARIUS. Distinct works, no leak.
- divisio→a1-q1 (p.812): PASS. divisio keeps p.812 nn.1–5 [^1]–[^5]; a1-q1 [^1] = p.812 n.6 (*Vers.14 — Minor fundatur in Aristot. II Ethic*). No double-count/drop.
- a1-q1→a1-q2 (p.815): PASS. a1-q1 forwards p.815 nn.1–5; a1-q2 [^1] = p.815 n.1 (*Vers.20 persequeris/exsequeris*). Clean.
- a1-q2→a1-q3 (p.818): PASS. a1-q2 forwards nothing; a1-q3 [^1] = p.818 n.1 (*Boeth. de Divisione*). Clean.
- **a1-q3→a2-q1 (p.821, INTER-ARTICLE): PASS.** a1-q3 closes its incidental-question reply at the top of p.821 and keeps p.821 n.1 (*Vide scholion ad praecedentem quaest.*) as [^25]; a2-q1 opens fresh with the ARTICULUS II header + opener + QUAESTIO I, picking up p.821 n.2-onward as its [^1] (*Vers.8 … via magis*). No mid-sentence splice, no double-count across the article seam.
- a2-q1→a2-q2 (p.825): PASS. a2-q1 forwards nothing (own band closes p.824, scholion p.824–825 has no footers); a2-q2 [^1] = p.825 n.1 (*Cfr. supra d.27 a.2 q.4*). Clean.
- a2-q2→a2-q3 (p.827): PASS. a2-q2 keeps p.827 nn.1–3; a2-q3 [^1] = p.827 n.4 (*Libr.III Antiq. c.6 Iosephus*). Clean.
- **a2-q3→dubia (p.829): FIXED (see below).**
- dubia tail→d.38 (p.836): dubia closes Dub. VIII at *…ad obiecta responderi* before DISTINCTIO XXXVIII (Cap. I *De triplici genere mendacii*); p.836 `NOTAE AD LIBR. SENTENTIARUM` block belongs to d.38. Tail continuity OK — BUT an internal dubia p.835–836 apparatus defect was found (see FLAG below).

### FIX — d37-a2-q3 apparatus at the a2-q3→dubia (p.829) seam
Backup `vol3/_backup-a2-q3-pre-pass3b-20260614/`. Eyes-on `/tmp/colcrop/vol3-p829-{L,R}-{0,2}.png`: p.829 footer band = L-col nn.1–5 + R-col nn.6–9 (9 notes).
1. **DROPPED footer recovered.** p.829 L-col **n.4** (*Cfr. supra lit. Magistri, d. XXXVI. c. 3. — …insinuabantur codd. GHKLTVZ aa bb insinuabant*) had been omitted (chunk skipped n.3→n.6). Re-set as **[^19]**, anchored in both bodies at body word *insinuabantur*.
2. **DOUBLE-COUNT removed.** a2-q3 [^22] held p.829 **n.9** (*De hoc axiomate … Senecae Epist. 65 … exemplare*), which keys to the **Dub. I** body and is correctly **dubia [^1]**. Removed from a2-q3.
Renumbered [^19]–[^22]; result 22/22 paired both bodies, each p.829 footer now appears once across a2-q3+dubia. PDF cite: p.829 L-2/R-2 bands.

### RESOLVED (tail-repair dispatch, 2026-06-14) — d37-dubia p.834 + p.835–836 tail apparatus
Initially FLAGGED as the [^59] triple-merge; a dedicated follow-up dispatch FIXED it. Final count **62 defs** (not 61 — the band read surfaced a second, distinct loss). Two losses recovered eyes-on (`/tmp/colcrop/vol3-p83{4,6}-{L,R}-*.png`, pp.829–836 = PDF 851–858):
- **p.834 n.5** (*Vers. 28 — Glossa est Rabani*, the Dub. VI *Matthaei quinto*/Glossa note) had been **dropped entirely** → restored as **[^43]**.
- **the collapsed [^59]** split into **[^60]** (*Quapropter Aristot., de Virtut. et vitiis c.7* → *decipiendo*), **[^61]** (*Supra dub. 2 … mendacium/mandatum* → *de periurio*), **[^62]** (*Cod. G patet solutio ad obiecta — Alex. Hal. q.37* → *ad obiecta responderi*).
The body-anchor drift ran deeper than first estimated (Dub. II–VIII in BOTH languages; English carried only 54 of 62) — every Dub. II–VIII marker was re-anchored to its PDF footer lemma. **Result 62/62 paired in both bodies; frontmatter restored to `Phase C Tier 2 complete —`.** Backup `vol3/_backup-d37-dubia-pre-pass3bfix-20260614/`. d.37-dubia is fully Tier 2.

### RESOLVED (tail-repair dispatch, 2026-06-14) — d37-a2-q1 five unanchored defs
Initially FLAGGED; FIXED in the same follow-up dispatch. The 5 anchors were placed in BOTH bodies (no renumber) at: **[^10]** → *sicut intuenti satis apparet*; **[^11]** → *actus cordis, oris et operis*; **[^12]** → *rationem principii* (and the file's pre-existing mislabeled [^9] near that lemma was corrected — [^9] moved to its true spot at the first-table *ex parte obiecti* conclusion); **[^15]** → *temporalis subsidii*; **[^16]** → *mandatorum ordinantium hominem ad Deum*. **Result 23/23 paired in both bodies** (now true). Backup `vol3/_backup-d37-a2-q1-pre-pass3bfix-20260614/`.

### d.37 ACCEPT-ILLEGIBLE
NONE — pp.810–836 read cleanly at 450 dpi.

---

## PASS 3b — d.36 boundary integrity sweep (2026-06-14)

d.36 = single-article distinction (ARTICULUS UNICUS, a1-q1..q6) + littera/divisio/dubia. **Boundaries checked: 9** — 5 mid-page (450 dpi eyes-on) + 4 page-aligned (continuity glance). Method per CLAUDE.md Pass 3 + VOL III OVERRIDE.

**Per-seam verdicts:**
- **littera→divisio (p.790) — CLEAN.** NOTAE AD LIBR. SENT. closes at littera [^15] (n.6 *Enchirid.*); NOTAE AD COMMENTARIUM family opens for divisio [^1]–[^2]. Two disjoint footer families, no drop.
- **divisio→a1-q1 (p.791) — CLEAN.** divisio band closes at COMMENTARIUM n.1 = [^3] (*Edd. omittunt totalis*); a1-q1 opens fresh at n.2 (*Vers.14* Glossa).
- **a1-q1→a1-q2 (p.794) — CLEAN.** a1-q1 contributes only scholion body (no footers) to p.794; a1-q2 owns the whole p.794 footer band nn.1–3.
- **a1-q2→a1-q3 (p.796) — CLEAN.** a1-q2 closes at R-col n.7 = [^21] (scholion redirect); a1-q3 opens fresh at n.8.
- **a1-q3→a1-q4 (p.799) — DEFECT FOUND + FIXED (see below).**
- **Page-aligned (a1-q4→a1-q5 801→802, a1-q5→a1-q6 804→805, a1-q6→dubia 807→808, d.36-dubia→d.37-littera 809→810) — CLEAN.** Each receiving chunk opens a fresh per-page footer band; Notes consistent.

### FIX — d36-a1-q4 (+ d36-a1-q3) at the shared p.799 footer band
Two failure modes at p.799 (eyes-on; backups `vol3/_backup-d36-a1-q{3,4}-pre-pass3b-20260614/`):
1. **DOUBLE-COUNT.** a1-q4 had wrongly claimed a1-q3's p.799 nn.1–2 (*Cfr. supra q.1* / *De Praedicam.* denomination note) as its own leading [^1]–[^2] — removed.
2. **DROPPED FOOTERS (3).** Recovered eyes-on: p.799 n.5 (August. *Epist. 167* c.2 n.9, arg 4 *universitas virtutum*), p.799 n.6 (*de Duabus Animabus* c.6 n.6, arg 4 *imaginem deformat*), p.801 n.1 (Hieronym. *in Eccl.* 9,18, Ratio 4 *assequendam* — the first word of p.801, previously mis-tagged). Re-anchored *Vers.18*→arg 1, *Vers.10*→arg 2. Renumbered continuous; **a1-q4 now 21/21 paired**.
3. **a1-q3 [^21]** had a wrong truncated cite ("Aristot. I. *Ethic.*") for the p.799 n.2 *Philosophus* note → restored the full *De Praedicam.* (Categories) text (La+En); **a1-q3 now 21/21 paired**. Both Notes + status updated with crosswalks. PDF cite: p.799 / p.801 bands.

### d.36 ACCEPT-ILLEGIBLE
NONE — pp.789–801 read cleanly at 450 dpi. No new `[?]` flags.

---

## PASS 3b — d.40 boundary integrity sweep (2026-06-14)

d.40 = ARTICULUS UNICUS (a1-q1/q2/q3) + littera/divisio/dubia — the LAST distinction of Vol III. **Boundaries checked: 6** (1 page-aligned inter-distinction + 5 internal: 4 mid-page, 1 page-aligned). **No fixes required — all clean.** Method per CLAUDE.md Pass 3 + VOL III OVERRIDE.

**Per-seam verdicts:**
- **d.39-dubia→d.40-littera (PAGE-ALIGNED, 882/883) — CLEAN.** d39-dubia closes its own Dub. IV (self-contained); d40-littera opens fresh at `DISTINCTIO XL / Cap. I` top of p.883. Discrete, not a continuation.
- **littera→divisio (p.884) — CLEAN.** littera holds p.883 NOTAE nn.1–7 + the Magister's `EXPLICIT LIBER TERTIUS SENTENTIARUM`; divisio opens `COMMENTARIUS IN DIST. XL` on p.884.
- **divisio→a1-q1 (p.884, THREE-CHUNK OVERLAP) — CLEAN.** divisio has `has_apparatus:false` (0 defs) and forwards the entire p.884 footer band nn.1–6 to a1-q1, which holds it as [^1]–[^6] (verified literal: *Codd. R W Y aa / Contra Adimant. / Vers.15 / de Civ. Dei / supra pag.555 / Cod. U sit*). littera's band = p.883 only. No drop, no double-count.
- **a1-q1→a1-q2 (PAGE-ALIGNED 886/887; scholion/p.887-band question) — CLEAN.** a1-q1 carries Scholion §I–§IV (the p.887 upper note-band prose) as the LAST `## Latin` subsection (parser-safe body-then-scholion). a1-q2 opens its own `Quaestio II` with [^1] a genuine q2 footnote (*Hic c.2 — II Cor.3,6*), NOT scholion text. p.887 band NOT double-claimed.
- **a1-q2→a1-q3 (p.890) — CLEAN.** q2 takes p.890 n.1 only ([^23] *Cod. U dicatur*); q3 picks up p.890 nn.2–10 ([^1] = *Vers.30*).
- **a1-q3→dubia (p.892) — CLEAN.** q3 closes at [^21] (*Edd. hic subiungunt… Vide scholion ad 1. quaest.*); dubia picks up p.892 nn.5–9 as [^1]–[^5] ([^1] = *Cfr. supra pag.815 nota 6*, matching q3's documented first-excluded footer).

**END of Book III:** d40-dubia 41/41/41 marker pairing (Latin = English = defs), gaps at 13/25/30 as documented (per-page restart across pp.892–896); `Dcb. III` OCR garble correctly rendered `Dub. III.` in the body; closes with the doxology + `EXPLICIT LIBER TERTIUS FRATRIS BONAVENTURAE SUPER SENTENTIAS` (INDEX QUAESTIONUM excluded).

### d.40 ACCEPT-ILLEGIBLE
NONE — pp.882–896 read cleanly at 450 dpi. No files edited.

---

## PASS 3b — CLOSING SUMMARY (d.36–d.40) — 2026-06-14

**Boundaries checked: 42 across d.36–d.40** (≈29 mid-page / inter-article requiring 450 dpi eyes-on; ≈13 page-aligned, continuity-glance). Per distinction: d.36 = 9 (5 mid-page), d.37 = 9 (7 mid-page incl. 1 inter-article), d.38 = 8 (all mid-page) + 2 inter-dist glances, d.39 = 12 (9 mid-page/inter-article + 3 page-aligned), d.40 = 6 (4 mid-page + 2 page-aligned). One subagent per distinction, full 450 dpi column-band discipline.

**Per-distinction verdict:**
- **d.36 — 1 FIX** (a1-q4 footer double-count of a1-q3's p.799 nn.1–2 + 3 dropped footers recovered [p.799 nn.5–6, p.801 n.1] → 21/21; a1-q3 [^21] truncated cite restored → 21/21). All other seams clean.
- **d.37 — 2 FIXES.** (a) a2-q3 seam: 1 dropped footer (p.829 L n.4 *insinuabantur* → [^19]) + 1 double-count removed ([^22] = Dub. I's note) → 22/22. (b) Follow-up tail-repair: d37-dubia 1 dropped footer (p.834 n.5 → [^43]) + collapsed [^59] split into [^60]–[^62], full Dub. II–VIII re-anchoring in both bodies → **62/62, status restored to Tier 2 complete**; d37-a2-q1 5 unanchored defs anchored → true 23/23. All seams clean.
- **d.38 — ALL CLEAN.** 8 mid-page seams continuous; both Pass-1 backfills independently re-confirmed correctly anchored and singly-counted ((i) d38-dubia [^30]–[^32] = p.857 **L-col** nn.3–5, with d39-littera owning only the **R-col** block; (ii) d38-divisio [^4] = p.839 n.1 *omni*).
- **d.39 — 1 FIX** (a3-q3 footer attribution at p.878: double-count of a3-q2's p.878 nn.1–6 + dropped p.879 nn.1–6; re-keyed [^1]–[^12] → 21/21). All other seams clean, incl. both inter-article seams and the d.38→d.39 p.857 inter-distinction seam.
- **d.40 — ALL CLEAN.** No fixes; the p.884 three-chunk overlap and the a1-q1 scholion/p.887-band case both verified correct. d40-dubia 41/41/41 closes Book III.

**No ACCEPT-ILLEGIBLE items across d.36–d.40 — every band read cleanly at 450 dpi.**

**Note (deferred, not a defect):** d39-a2-q1 retains a b/c/d suffixed apparatus scheme (27/27 paired, every def anchored) — pairing is perfect, so left as-is; flagged for the owner if continuous-integer normalization is desired. d37-dubia frontmatter/header audit shows the dubia is a long 8-Dub. chunk spanning 8 pages (header audit `apparatus-incomplete` wording fully removed).

**Build + audit status (post-fix, d.36–d.40):**
- `audit-apparatus-count.py --volume 3 --min-d 36 --max-d 40`: **0 flags.**
- `audit-paraphrase.py --volume 3 --min-d 36 --max-d 40`: 45 chunks, **critical 0 / high 0.**
- `audit-headers.py --volume 3 --min-d 36 --max-d 40`: **no LOSS flags** (all diffs positive, expected for Vol III).
- `cd site && node scripts/build-content.mjs`: parses clean, **0 marker-pairing warnings, 1287/1287 translated.**

**Pass 3b status: CLOSED.** With Pass 1 (`e2dcfb0`), Pass 2 (`e95d777`), Pass 3a (`859b3e2`) and Pass 3b (this commit), the **d.31–d.40 DECADE POLISH GATE is COMPLETE** — and with it **Vol III (Book III, all 40 distinctions) is fully Tier 2.** The gate no longer blocks Vol IV.
