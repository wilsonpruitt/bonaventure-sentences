# Bonaventure Sentences — Next Session Resume

> **Active front: VOL IV / BOOK IV** (started 2026-06-16). Vols I, II, III are COMPLETE & published.
> History for Vols I–III (all the superseded per-chunk "NEXT ACTION" hand-off logs) was trimmed
> from this file on 2026-06-16 and archived to `manual-review/resume-archive-vol1-3.md`; it also
> lives in full in the git commit history. This file now carries ONLY the active Vol IV pointer.

# ★ VOL IV / BOOK IV — STARTED 2026-06-16 (current active front)

**Vol III (Book III) is COMPLETE & published.** Book IV (Commentarius in IV Librum Sententiarum) is now the active front.

## Bootstrap (commit f6da2aa, 2026-06-16)
- **610 chunk skeletons** auto-chunked into `vol4/` (47 distinctions detected). **d.4, d.23, d.50 merged into neighbors** via OCR-garbled DISTINCTIO headers; **101 dup-IDs** need pars relabeling — resolve per-distinction during the normal re-chunk-before-translate step. d.50 confirmed present in raw (L109979); body ends at INDEX QUAESTIONUM (L112357).
- **Two-column, same edition as Vols II/III → apply the VOL II OVERRIDE recipe** (PDF-priority inversion; `colcrop.py vol4 <page>`).
- **Offset `pdf = printed + 20`** (verified twice: printed 18→PDF 38, printed 49→PDF 69). Wired into `tools/extract-pages.py` (vol4 config). `build-content.mjs` reports 4 books. The 3 audit scripts gained `--volume 4` (commit c3571ba).
- PDF `raw/doctorisseraphic04bona.pdf` = 1094pp; raw `raw/bonaventure_vol4_raw.txt`.
- Decade polish gates fire at d.10 / d.20 / d.30 / d.40 / d.50 (Book IV's own boundaries).

## d.1 structure (CORRECTED — chunker mislabeled pars; re-chunked 2026-06-16)
The auto-chunker put Pars I's art-unicus quaestiones under `d1-p2-a1-*` and buried the real Pars II in `-dup2` files; it also MISSED the Pars I dubia entirely. True structure now on disk:
- **Pars I:** `d1-p1-littera`, `d1-p1-divisio`, `d1-p1-a1-q1..q6` (Articulus Unicus), `d1-p1-dubia` (Dub. I–XII).
- **Pars II:** `d1-p2-divisio` (*De circumcisione et annexis*), `d1-p2-a1-q1..q3` (Art. I), `d1-p2-a2-q1..q3` (Art. II), `d1-p2-dubia`.

## d.1 progress (as of 2026-06-16)
| Unit | Status |
|---|---|
| `d1-p1-littera` | ✅ Tier 2 (pp.8–10, 16 app). [?]: p.10's 3 littera markers had no printed footer — **RESOLVED by divisio** (refs are in p.10 L-col commentary footer); retire flag at d.10 gate. |
| `d1-p1-divisio` | ✅ Tier 2 (pp.10–11, 6 app) |
| `d1-p1-a1-q1` | ✅ Tier 2 — Whether the Sacraments ought to have been instituted (pp.11–13, 17 app, scholion I–IV) |
| `d1-p1-a1-q2` | ✅ Tier 2 — On the signification of the Sacraments (pp.13–15, 20 app, no scholion) |
| `d1-p1-a1-q3` | ✅ Tier 2 — On the containing power (pp.16–18, 20 app, scholion I–IV covers q3+q4) |
| `d1-p1-a1-q4` | ✅ Tier 2 — Whether the Sacraments are effective of grace (pp.19–24, 62 app, scholion in q3) |
| `d1-p1-a1-q5` | ✅ Tier 2 — Difference between old & new Sacraments (pp.24–27, 23 app, own scholion I–II) |
| `d1-p1-a1-q6` | ✅ Tier 2 — Grace conferred in the Sacraments (pp.27–28, 14 app, scholion in q5) |
| `d1-p1-dubia` | ✅ Tier 2 — Dubia I–XII on Master's text (pp.28–31, 37 app) |
| `d1-p2-divisio` | ✅ Tier 2 — Pars II divisio textus (pp.31–32, 3 app) |
| `d1-p2-a1-q1` | ✅ Tier 2 — Whether informed faith suffices (pp.32–33, 9 app, art-master scholion I–III) |
| `d1-p2-a1-q2` | ✅ Tier 2 — Whether faith alone suffices (pp.33–35, 15 app, scholion in q1) |
| `d1-p2-a1-q3` | ✅ Tier 2 — Whether sacrifice-power required in adults (pp.35–37, 22 app, scholion in q1) |
| `d1-p2-a2-q1` | ✅ Tier 2 — On the institution of circumcision (pp.37–39, 22 app, art-master scholion I–III) |
| `d1-p2-a2-q2` | ✅ Tier 2 — On the form/integrity of circumcision (pp.39–41, 25 app, scholion in a2-q1) |
| `d1-p2-a2-q3` | ✅ Tier 2 — On the efficacy of circumcision (pp.42–44, 23 app, scholion in a2-q1). [?]: [^6c] OCR "ad 4. huius articuli quaest" digit-mangle → d.10 gate |
| `d1-p2-dubia` | ✅ Tier 2 — Dubia I–VIII on Master's text (pp.44–46, 25 app). Replaced a mis-copied skeleton body. |

**★ DISTINCTIO I COMPLETE — all 17 chunks Tier 2 (2026-06-16). Build: 1304 translated.**

## NEXT ACTION
Begin **Distinction II** (*De Sacramentis novae legis* / institution of the seven sacraments). `DISTINCTIO II.` at raw **L5614** (printed ~p.47, PDF ~67). FIRST verify d.2's pars/article structure against raw + the auto-chunked skeletons (the d.1 chunker mislabeled pars and missed a dubia — DO NOT trust d.2 skeleton filenames; grep raw for `DUBIA CIRCA LITTERAM`, `ARTICULUS`, `QUAESTIO`, pars running-heads `DIST. II. P. I/II`, and re-label/scaffold before translating). Start with the d.2 littera, then divisio(s), quaestiones, dubia. Cadence: one-chunk-per-subagent, offset +20, colcrop split_x 1880, two-column VOL II override.

**Open d.1 [?] flags for the d.10 decade polish gate:** (1) `d1-p1-littera` p.10 markers — resolved by divisio (refs in p.10 L-col footer), retire; (2) `d1-p2-a2-q3` [^6c] OCR "ad 4. huius articuli quaest" digit-mangle.
