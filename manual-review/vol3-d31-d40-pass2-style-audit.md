# Vol III — d.31–d.40 Decade-Polish Gate, PASS 2 of 3: Style/Formatting Audit (full corpus)

**Date:** 2026-06-14
**Scope:** FULL-CORPUS programmatic scan (all of `vol1/`, `vol2/`, `vol3/`), per CLAUDE.md "Polish-blocker cadence" §2 ("Style/formatting audit — full corpus every time"). Fixes applied this pass are confined to d.31–d.40 (the active decade gate) plus the explicit known fix; pre-existing cosmetic drift in earlier-decade chunks (already past their own gates) is **logged, not fixed**.
**Method:** `tools/audit-style-formatting.py` (8 checks: required Tier-2 frontmatter, `Phase C Tier 2 complete —` status prefix, standard `## Latin`/`## English`/`## Apparatus` sections, apparatus marker pairing, page-break presence, `### Scholion`-last ordering, legacy/dup files, `**En.**` indent mix) + a supplemental `/tmp/pass2_scan.py` adding **item 8** (suffix-letter apparatus scheme `[^Nx]`) and **git-tracked-backup** detection.

> **Filename note.** Per the Vol III convention (`vol3-d21-d30-pass2-style-audit.md`) this focused report lives here; the `audit-style-formatting.py` self-report still writes to the d21-d30 path (its hardcoded `REPORT_PATH`), which was restored untouched after the run.

---

## Scan coverage

- **1287 chunks** walked across Vol I + Vol II + Vol III. **1260 Tier-2** audited; **27 skeletons** skipped (status not `Phase C Tier 2 complete —` / `auto-chunked`).
- Per-volume Tier-2: Vol I = 406, Vol II = 448, Vol III = 406.

---

## KNOWN FIX (item 8) — APPLIED: `d39-a3-q3` apparatus renumbered to continuous integers

`vol3/bon-sent-III-d39-a3-q3.md` used a per-page-band suffix scheme `[^1b]`–`[^9b]` for its p.880 footer band, appended after the pp.878–879 band `[^1]`–`[^12]`. **NORMALIZED** to a single continuous integer sequence: `[^1b]→[^13]`, `[^2b]→[^14]`, …, `[^9b]→[^21]`. All apparatus content preserved verbatim; only the numbers changed. Updated in BOTH bodies, BOTH `[^N]:` defs, the apparatus blockquote intro, the frontmatter `transcription_status`, and the `## Notes` provenance/hand-off prose. The stale `Marker pairing: 27/27` line in Notes was corrected to `21/21`.

**Re-verified:** defs `[^1]`–`[^21]` continuous; La anchors = En anchors = defs = {1..21}. **Pairs 21/21 N/N.** No `[^Nb]` token remains in the file.

---

## Findings by category

### Frontmatter / status-prefix / sections / page-breaks — CLEAN
No chunk (any volume) flagged for `missing_frontmatter`, `status_prefix`, `missing_section`, or `no_page_breaks`. Every Tier-2 chunk carries the full required field set, the `Phase C Tier 2 complete —` prefix, the three standard sections (or `has_apparatus: false`), and ≥1 `<!-- page N -->`.

### `scholion_not_last` (1) — LOGGED (out of scope, pre-existing)
- `bon-sent-I-d27-p1-a1-q2.md` (Latin, English). **Pre-existing Vol I drift** — flagged once already in the d.21–d.30 Pass-2 log. The parser gotcha (scholion-above-body silently empties the body) would have shown as a `hasTranslation:false` / translated-count stall; the count is a healthy 1287/1287, so this is almost certainly a **false positive** (a `### …` subheading *inside* the scholion text, not a body subsection after it). Out of the d.31–d.40 scope; left for a Vol I re-gate / Pass-3 spot check. **No build impact.**

### `orphan_app_defs` (10) — INVESTIGATED → all benign (unanchored editorial notes + blockquote-literal false positives)
The flagged chunks are: `d26-a2-q5`(9), `d31-a2-q3`(18,19), `d31-a3-q3`(1–10), `d32-a1-q1`(11–13), `d32-a1-q2`(13–21), `d33-a1-q3`(23–32), `d33-dubia`(17–32), `d34-p2-a1-q1`(9–11), `d37-a2-q1`(10–12,15,16), `d5-a2-q4`(11).
- Eyes-on: every "orphan" def is a **Quaracchi unanchored editorial / cross-reference / parallel-loci note** (`Vide supra…`, `Cfr. …`, `Idem dub. solvit Alex. Hal.…`) — the recognized Tier-2 pattern where source/cross-ref notes carry a `[^N]:` def but no body word-anchor (cf. Pass-1 d38-dubia nn.3/5 disposition). In `d31-a3-q3` the *leading* notes 1–10 are this kind (body anchors legitimately run 11–25); La==En throughout.
- `d33-dubia` additionally showed a spurious `anchor_only_la=[33]`: this is a **false positive** — the literal `` `[^33]` `` appears inside the apparatus-intro blockquote (which sits in the `## Latin` block), not as a real body anchor. `[^33]` is itself an unanchored parallel-loci note. No defect.
- **Disposition: ACCEPTED.** These are not errors and are not "fixed" (anchoring an editorial cross-ref to an arbitrary body word would falsify the apparatus). The audit's pairing check cannot distinguish unanchored editorial notes; treat this flag class as triage-only for Vol III. **No build impact** (count 1287/1287).

### `en_indent_mix` (1) — LOGGED (in scope, cosmetic, deferred)
- `bon-sent-III-d33-dubia.md` — mixes `**En.**` continuation indents (9 entries at 5 spaces, 24 at 6 spaces). The parser is indent-tolerant (renders fine; chunk is translated). CLAUDE.md documents 4/5 spaces as the accepted convention and explicitly says **"Don't bulk-edit between the two."** 6-space is the chunk's own majority. Per that guidance and the d.21–d.30 precedent (log-don't-churn), **left as-is and logged**; a future global indent-normalization pass (if ever desired) should harmonize the whole corpus at once, not one chunk piecemeal.

### Page-break presence — CLEAN
All multi-page Tier-2 chunks carry `<!-- page N -->` comments.

### Item 7 — legacy / duplicate / tracked-backup
- **`*-dup*.md`: NONE on disk.** The 11 `vol3/*-dup2.md` files listed in the d.21–d.30 Pass-2 report have since been removed — confirmed gone.
- **`dN-divisio.md` superseded by `dN-pM-divisio.md`:** none detected (Vol III pars-split divisios coexist correctly with their pars labels; no bare-divisio orphan).
- **Git-tracked backups (should NOT be tracked):**
  - `_backup-d43-p2-dubia-vestigial-20260513/bon-sent-I-d43-p2-dubia.md.archived`
  - `_backup-resume-pre-trim-20260522.md`
  These two stray tracked artifacts are **pre-existing Vol I-era housekeeping**, not d.31–d.40 work, and the `_backup-*` dirs are otherwise correctly untracked. **LOGGED** for a future `git rm --cached` cleanup (not done here to keep this commit scoped to the d.31–d.40 gate; deleting tracked history files is a protected-ish action best confirmed with the owner). No content/build impact.

### Item 8 — suffix-letter apparatus scheme `[^Nx]` (the corpus-wide context for the known fix)
The `[^1b]`/`[^2c]` per-page-band suffix scheme is **NOT unique to d39-a3-q3** — it is a **widespread, deliberate convention** across **39 chunks**, concentrated in **Vol III d.5, d.6, d.7** (e.g. `d6-littera`, `d5-a2-q5`, `d7-littera` run `b`/`c`/`d`/`e` bands) and present in Vol I (`d30-a1-q3` `[^1s]`…, `d30-a1-q3/q4` `[^Na]`) and Vol II (`d42-dubia` runs `b`→`e`). It encodes Quaracchi's per-printed-page footnote restart.
- **In d.31–d.40 (in scope):** besides the now-fixed `d39-a3-q3`, only **two** chunks use a *single interpolated* suffix marker inside an otherwise-continuous sequence: `d33-a1-q3` (`[^6b]` between [^6] and [^7]) and `d33-a1-q5` (`[^14b]` between [^14] and [^15]). These were both *touched in Pass 1* and are an interpolated-insertion variant (one extra mid-sequence note), not a full band restart. Renumbering them would cascade-shift ~13–26 downstream markers in both bodies — a high-churn, error-prone edit for a purely cosmetic gain. **LOGGED, deferred.**
- **Decision flagged for the owner (Pass 3 / later):** the suffix scheme is either (a) the *intended* Vol III convention to be left alone, or (b) a drift to be globally normalized to continuous integers. d39-a3-q3 was normalized **because the dispatch named it explicitly**; the other 38 are pre-existing, passed their own decade gates, and a one-off normalization of just two of them would *increase* inconsistency, not reduce it. Recommend a single deliberate corpus-wide decision rather than piecemeal fixes.

---

## Build + audit status

- `cd site && node scripts/build-content.mjs`: **clean parse — 3 books, 1287 questions, 1287 translated** (unchanged). No marker-pairing warnings emitted. d39-a3-q3's renumber preserved its translated state and 21/21 pairing.
- `python3.11 tools/audit-apparatus-count.py --volume 3 --min-d 39 --max-d 39`: **0 chunks flagged** (only `d39-littera` audited, +11 diff, under threshold). d39-a3-q3 clean after renumber.

---

## Pass 2 status: CLOSED

**Fixed:** d39-a3-q3 apparatus renumbered `[^1b]–[^9b]` → `[^13]–[^21]` (continuous 1–21, pairs 21/21), plus its stale 27/27 Notes count corrected.
**Logged-for-followup (no fix this pass):** `d27-p1-a1-q2` scholion-order flag (likely false positive, Vol I); 10 `orphan_app_defs` chunks (all benign unanchored editorial notes / blockquote false positives — accepted); `d33-dubia` En-indent 5/6 mix (cosmetic, parser-tolerant, per "don't bulk-edit"); two git-tracked backup artifacts (Vol I-era, `git rm --cached` candidate); the corpus-wide `[^Nx]` suffix-scheme convention (39 chunks incl. two in-scope d.33 interpolations) — needs a single owner decision, not piecemeal edits.

**NEXT ACTION on the polish blocker:** Pass 3 (cross-chunk boundary-integrity sweep, d.31–d.40) — still a blocker for any Vol IV / Book IV work.
