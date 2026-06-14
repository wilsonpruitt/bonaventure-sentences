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
