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
