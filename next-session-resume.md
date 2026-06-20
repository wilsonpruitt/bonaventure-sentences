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

## d.2 progress (COMPLETE 2026-06-18)
**★ DISTINCTIO II COMPLETE — all 9 chunks Tier 2 (2026-06-18). Build: 1313 translated.** Single pars (no P.I/II split). Chunks: `d2-littera` (pp.47–48, 10 app), `d2-divisio` (NEW — auto-chunker missed it; p.48, 2 app, DIVISIO TEXTUS + TRACTATIO), `d2-a1-q1` (utrum omne tempus idoneum, pp.48–50, 18 app, art-scholion I–II covers q1–q3), `d2-a1-q2` (utrum diversa institui, pp.50–52, 15 app), `d2-a1-q3` (de numero Sacramentorum, pp.52–54, 13 app), `d2-a2-q1` (Art.II *De baptismo Ioannis* — a quo institutus, pp.54–55, 9 app, art-scholion I–III covers a2 q1–q3), `d2-a2-q2` (ad quid institutus, pp.55–56, 14 app), `d2-a2-q3` (de usu/efficacia, pp.57–58, 19 app), `d2-dubia` (DUB.I–V, pp.59–60, 18 app). Fixed a footer-split error: `d2-littera [^8]` had wrongly taken the divisio's NOTAE-1 (commit 09f3897). No open `[?]` flags in d.2.

## d.3 progress (COMPLETE 2026-06-19)
**★ DISTINCTIO III COMPLETE — all 17 chunks Tier 2 (2026-06-19). Build: 1330 translated, 1883 questions.** Two-pars. **Pars I (9):** littera (pp.61–63, *De circumcisione/baptismo*, 9 caps), divisio (p.63–64), a1-q1 (*quid sit baptismus a parte elementi*, pp.64–66, art-scholion I–II covers a1 q1–q3), a1-q2 (*expressio vocalis verbi*, pp.67–68), a1-q3 (*fides alicuius articuli*, pp.68–69 — had a dropped-footer off-by-one, FIXED commit 23b2e20), a2-q1 (Art.II *De forma verbi* — *verbum exprimens actum baptizandi*, pp.70–71, art-scholion I–III), a2-q2 (*expressio totius Trinitatis*, pp.71–73), a2-q3 (*de variatione formae*, pp.73–74), dubia (DUB.I–VI, pp.74–76). **Pars II (8):** divisio (*De institutione baptismi*, pp.76–77), a1-q1 (*institui in aqua*, pp.76–78, art-scholion I–II), a1-q2 (*vis collata aquis*, pp.78–80), a2-q1 (Art.II *De administratione* — *quoties immergi*, pp.80–81, art-scholion), a2-q2 (*quantum immergi*, pp.81–82), a3-q1 (Art.III *De cessatione circumcisionis* — *utrum debuerit cessare*, pp.82–86, art-scholion), a3-q2 (*cessaverit ante promulgationem Evangelii*, pp.86–88), dubia (DUB.I–III, pp.89–90).
**⚠ AUTO-CHUNKER LESSON (d.3 Pars II):** the entire `d3-p2-a1-*` + `d3-p2-a2-*` skeleton family was mislabeled with **d.4 content** (line_starts pointed into d.4 ~L10944+); all rebuilt from correct raw ranges (Pars II = raw L8854–10386). 11 stale `-dup2/-dup3` skeletons + 4 `q3` artifacts deleted. **For d.4+: do NOT trust skeleton line_start/body — always grep-verify the raw range first.**
**Open d.3 [?] flags for d.10 polish gate:** (1) littera/divisio p.63 L-col footer attribution seam (Gregory/Augustine notes — verify at 600dpi); (2) d3-p2-dubia [^11] "Cfr. III Sent. d.18 q.[?]" OCR question-number clip.

## d.4 progress (COMPLETE 2026-06-19)
**★ DISTINCTIO IV COMPLETE — all 17 chunks Tier 2 (2026-06-19).** Two-pars, *De effectu baptismi*. **NO d.4 skeletons existed** (auto-chunker had merged all d.4 body into d.3-p2 + d.5 skeletons) — every chunk CREATED FRESH from raw. `DISTINCTIO lY.` (garbled) at raw L10387, runs to L13556. **Pars I (9):** littera (Caps I–VII *De effectu baptismi*, pp.90–93), p1-divisio (pp.93–94, 0 app — footers split to littera+q1), a1 *De digne suscipientibus* q1 (*deleat omnem culpam*, pp.94–96, art-scholion I–III)/q2 (*omnem poenam*, pp.96–98)/q3 (*aequalem efficaciam*, pp.98–99), a2 *De ficte suscipientibus* q1 (*invitus/coactus*, pp.100–102, art-scholion)/q2 (*recipiat Sacr. non rem*, pp.102–103)/q3 (*recedente fictione*, pp.103–104), dubia (DUB.I–IV, pp.104–105). **Pars II (8):** p2-divisio (*De his qui suscipiunt rem tantum*, pp.105–106), a1 *De sanctificatione adultorum* q1 (*baptismus flaminis sine fluminis*, pp.106–108, art-scholion)/q2 (*aquae an sanguinis* — header restored from OCR garble L12461)/q3 (*sanguinis sit Sacramentum*, pp.109–111), a2 *De sanctificatione parvulorum* q1 (*recipiant sanctificationem*, pp.111–113, art-scholion)/q2 (*plene rem*, pp.113–115)/q3 (*aequalis gratia*, pp.115–116), dubia (DUB.I–VII, pp.116–118).
**Open d.4 [?] flags for d.10 polish gate:** (1) littera printed-page offset reads pp.90–93 not 91–94 (running head DIST.IV.P.II appears on p.91 — documented in littera Notes); (2) a1-q2 (Pars I) dropped its p.98 note 7 (*Vide scholion ad praec. quaest.* at *praestito in se ipso*) — add at decade sweep; (3) p1-divisio stray *In prima¹* superscript on p.94 w/ no footer; (4) d4-p2-dubia omitted p.116 note 6 (illegible inner-margin variant fragment).

## d.5 progress (COMPLETE 2026-06-20)
**★ DISTINCTIO V COMPLETE — all 9 chunks Tier 2 (2026-06-20). Build: 1356 translated, 1900 questions, 4 books.** Single-pars (like d.2), *De ministris / potestate baptizandi* (baptism by comparison to those who give it). `DISTINCTIO V.` raw L13556→L15111. Chunks: littera (Cap.I–III, pp.118–120; took p.118 R-col NOTAE), divisio (p.120, 3 app), a1 *De extensione potestatis* q1 (*utrum soli sacerdotes habeant potestatem baptizandi*, pp.120–123, art-scholion I–II)/q2 (*utrum haeretici baptizent*, pp.123–124), a2 *De intensione/efficacia* q1 (*mali ministri dent rem*, pp.124–126, art-scholion — q2 header garbled, found at raw L14334/body L14342)/q2 (*haeretici dent rem*, pp.126–127), a3 *De potestate per comparationem ad dantem* q1 (*quae sit illa potestas*, pp.127–129, art-scholion I–IV)/q2 (*utrum Christo data potestas dimittendi peccata*, pp.130–131), dubia (DUB.I–V, pp.131–132).

## d.6 progress (COMPLETE 2026-06-20)
**★ DISTINCTIO VI COMPLETE — all 17 chunks Tier 2 (2026-06-20). Build: 1373 translated, 1902 questions.** **TWO-PARS** (the running-head "DIST. VI. P. I" early on hid Pars II, which begins at raw L16889 — *De his quae requiruntur ad baptismum*; Pars I chunks were built first under single-pars naming then RENAMED to `d6-p1-*` + `pars:1` once Pars II was discovered, commit b5a0148). `DISTINCTIO VI.` raw L15111→d.7 at L18616. **Pars I (9):** p1-littera (Caps I–VII, pp.133–135), p1-divisio (COMMENTARIUS+DIVISIO+TRACTATIO, pp.135–136), Articulus Unicus *De charactere* p1-a1-q1 (*quid sit secundum essentiam*, pp.136–139, art-scholion block at p.139)/q2 (*ad quid sit*, pp.139–141)/q3 (*in quo sit sicut in subiecto*, pp.141–142)/q4 (*per quid imprimatur*, pp.142–144 — **holds the p.144 art-scholion block I=q4/II=q5/III=q6 in full**; q5/q6 render none)/q5 (*delebiliter an indelebiliter*, pp.144–145)/q6 (*utrum baptismus possit iterari*, p.146), p1-dubia (DUB.I–IV, pp.147–148). **Pars II (8):** p2-divisio (COMMENTARIUS Pars II+DIVISIO+TRACTATIO, pp.148–149, 3 articles: idoneitas/intentio/sacramentalia annexa), a1 *De idoneitate ex parte baptizati* q1 (*utrum in utero possit baptizari*, pp.149–151, art-scholion)/q2 (*utrum sanctificatus in utero debeat baptizari*, pp.151–152), a2 *De intentione baptizantis* q1 (*utrum intentio sit de necessitate baptismi*, pp.152–154, art-scholion)/q2 (*utrum recta intentio sit necessaria ad baptismum*, pp.154–155), a3 *De sacramentalibus annexis* q1 (*utrum parvuli debeant catechizari*, pp.155–157, art-scholion)/q2 (*utrum exorcismus habeat efficaciam*, pp.157–159), p2-dubia (DUB.I–VII, pp.159–162).
**⚡ CADENCE CHANGE (2026-06-20):** the 8 Pars II chunks were built using a **coordinator + parallel-writers** pattern (4 write-only subagents at once) — ~4× faster, quality held. Recipe: coordinator maps the distinction + pre-generates ALL colcrop bands serially (the only heavy/8GB-bound step) + computes an explicit footer/scholion ownership rule per chunk → fans out N write-ONLY agents (no git/build/extract; they may colcrop) each given raw range + band paths + "claim footnotes anchored in YOUR body; render only the scholion section keyed to your q#" → coordinator runs build+3 audits+commit ONCE. All 4 seams reconciled with zero double-claims/drops. **Use this for d.7–d.10.**
**Open d.6 [?] flags for the d.10 decade polish gate:** (1) **`d6-p1-dubia` OFFSET ERROR** — originally built reading pdf 147–148 (should be pdf 167–168; +20 holds). Body is from correct OCR raw range L16776–16888 so text is sound, but PDF cross-checks were on wrong pages AND there is a cascade-merge splice in DUB.I ("[Continuatio Dub. I:] *tem*…") — re-verify Respondeo + footers vs correct pdf 167–168 at 600dpi. Metadata already corrected to pdf_pages [167,168]. (2) `d6-p2-divisio` body footnote markers run 2,3,5,4,6 (content-anchored, not ascending) — re-verify superscript-to-lemma keying at 600dpi. (3) `d6-p2-a1-q2` two minor variant-anchor flags (cod. aa *peccatum→meritum*; cod. M *respicit* gutter clip). (4) `d6-p2-dubia` Hugo de S.V. (Dub.VI) ambiguous superscript (assigned n.9 by content) + Dub.IV *ioculariter*/OCR *iocularie*.

## NEXT ACTION
Begin **Distinction VII** (*De confirmatione*). `COMMENTARIUS IN DISTINCTIONEM VII.` at raw **L18616**; the d.7 LITTERA (Lombard) precedes it at ~raw **L18489–18615** (printed ~p.162). FIRST grep raw from ~L18489 to the next DISTINCTIO for `ARTICULUS`/`QUAESTIO`/`DUBIA`/`DIVISIO TEXTUS` + `DIST. VII. P. I/II` running-heads to map structure (single- vs two-pars) before scaffolding — **d.6 proves the early running-heads can hide a Pars II; scan the WHOLE distinction's running heads, not just the first pages.** Then apply the parallel-writers cadence above. Offset +20, colcrop split 1880 (vol4), two-column VOL II override. **NEXT DECADE GATE = d.10.**
[superseded d.6 bootstrap pointer below kept for reference]

## (superseded) d.6 bootstrap
Begin **Distinction VI**. `DISTINCTIO VI.` at raw **L15111** (printed ~p.133). FIRST grep raw from L15111 to the next DISTINCTIO for `ARTICULUS`/`QUAESTIO`/`DUBIA`/`DIVISIO TEXTUS` + any `DIST. VI. P. I/II` running-heads to map structure (single- vs two-pars) before scaffolding. **Skeleton line_starts are UNRELIABLE in Vol IV** — verify each chunk's raw range by eye (the d.4 family was mislabeled with neighbors' content; d.5 skeletons were column-shattered). Cadence: one-chunk-per-subagent, offset +20, colcrop split_x 1880 (p.120 needed 2050; pp.121–123 area needed 1780/2050 — adjust if a column clips), two-column VOL II override. **NEXT DECADE GATE = d.10** (after d.10 closes, run the three polish passes over Vol IV d.1–d.10, clearing the [?] flags listed under d.1/d.3/d.4 above).

**Open d.1 [?] flags for the d.10 decade polish gate:** (1) `d1-p1-littera` p.10 markers — resolved by divisio (refs in p.10 L-col footer), retire; (2) `d1-p2-a2-q3` [^6c] OCR "ad 4. huius articuli quaest" digit-mangle.
