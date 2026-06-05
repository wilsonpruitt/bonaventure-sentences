# Vol III — d.11–d.20 Decade-Polish Gate, PASS 1 of 3: `[?]`-flag resolution + carried-item dispositions

**Date:** 2026-06-05
**Scope:** Vol III, distinctions 11–20 (all chunks `bon-sent-III-d11-*` … `bon-sent-III-d20-*`).
**Gate:** First of the three locked-in passes (CLAUDE.md "Polish-blocker cadence"), fired by the close of Vol III d.20. Pass 2 (full-corpus style/formatting audit) and Pass 3 (cross-chunk boundary-integrity sweep d.11–d.20) follow separately and remain blockers for d.21+.
**Method:** 600 dpi PDF eyes-on via `pdftoppm -r 600 -f PDF -l PDF -png raw/doctorisseraphic03bona.pdf …`, offset **pdf = printed + 22**.

> **Filename note.** The generic `manual-review/d11-d20-polish-resolution-log.md` was already in use as the **Vol II** d.11–d.20 log (created 2026-05-25). To avoid clobbering that history, this Vol III log follows the established Vol III convention (cf. `vol3-d1-d10-polish-resolution-log.md`) and lives at `manual-review/vol3-d11-d20-polish-resolution-log.md`.

---

## 1. `[?]` flags found in d.11–d.20 chunks

**Genuine unresolved `[?]` flags: ZERO.**

`grep -rn '\[?\]' vol3/bon-sent-III-d1[1-9]-*.md vol3/bon-sent-III-d20-*.md` returns only:

- **"no `[?]` flags" / "NONE" disposition statements** inside each chunk's `## Notes` block (and several `transcription_status` frontmatter lines), confirming each chunk was promoted clean at 450 dpi; and
- **non-flag prose** that merely contains the token — e.g. d16-a2-q1 ("Not flagged `[?]` — the editorial attribution is settled…"), d17-a1-q3 ("preserved verbatim, not a [?] flag"), d13-divisio ("No `[?]` flags"), d19-a2-q1 ("No `[?]` flags — both pages legible…").

No chunk in d.11–d.20 carries an inline `[?]` in its Latin or English body. **Nothing to resolve or accept-illegible in this pass; no chunk was edited on account of a `[?]` flag.**

> Reproduced editorial queries (NOT transcription flags; left verbatim, correctly handled at promotion): d17-a1-q3 `[^p369-2]` *(contrariae?)* and `[^p369-6]` *fuit talis tristitia (?)* are **Quaracchi's own** parenthetical queries, transcribed as printed. Not `[?]` flags; no action.

---

## 2. Carried KNOWN open items (from `next-session-resume.md`)

### (a) p.426 footer-marker 6 — alleged source skip in `d20-a1-q4`

**Verdict: NOT a source skip. It was a genuine dropped footnote in the chunk. RESOLVED by backfill. (Chunk edited.)**

**Evidence (600 dpi, PDF p.448 = printed p.426; crops `raw/vision/vol3/crop-p426-Rfoot.png` + `crop-p426-Rbody.png`):**
- The printed p.426 footer apparatus runs **1–10, contiguous**: the L footer column carries nn.1–4; the R footer column carries nn.5–10.
- Note **6 IS printed** in the right footer column: `⁶ Vide II. Sent. d. 21. a. 3. q. 3. et d. 33. a. 1. q. 2.`
- Its body anchor `⁶` sits on *…non sic autem est in peccatis actualibus⁶* (R-column body, close of *Solutio ad 1*; Eng. "but it is not so in actual sins").
- The committed `d20-a1-q4` held only nn.1–5, 7–10 — it had **dropped n.6** while (wrongly) recording in its page-split map that the *source* skips marker 6.

**Action taken — `vol3/bon-sent-III-d20-a1-q4.md` EDITED:**
- Added def `[^p426-6]: **La.** Vide II. Sent. d. 21. a. 3. q. 3. et d. 33. a. 1. q. 2. / **En.** See II Sentences, d. 21, a. 3, q. 3, and d. 33, a. 1, q. 2.` (between `[^p426-5]` and `[^p426-7]`).
- Added the Latin body anchor on *…peccatis actualibus[^p426-6].*
- Added the English body anchor on *…in actual sins[^p426-6].*
- Rewrote the page-split-map paragraph (it had asserted a source skip) and the forwarded-hand-off line; appended a backfill note to `transcription_status`.
- p.426 footers are now nn.1–10, complete and contiguous; marker pairing verified (1 La anchor + 1 En anchor + 1 def).

### (b) "Manifestum est" scholion — ownership between `d18-a1-q3` and `d18-a2-q1`

**Verdict: `d18-a2-q1` is the CORRECT owner. NO change needed; NO duplication exists.**

**Duplication check:** The "Manifestum est, quod passio in se considerata…" scholion appears **only in `d18-a2-q1`** (§I). `d18-a1-q3`'s own scholion is a *different* text — "**Cum secundum actionem** *divinae* naturae…" (§I–III, the Lateran-649 *deivirilis operatio* note). The two are not duplicates; nothing to remove from either chunk.

**Ownership evidence (600 dpi):**
- **PDF p.409 = printed p.387** (`raw/vision/vol3/crop-p387-top.png`): page head carries running head **DIST. XVIII. ART. II. QUAEST. I.**, then **SCHOLION** (§I "Manifestum est…", §II "De hac quaestione: Alex. Hal…"), then the **ARTICULUS II** header + subtitle (*De merito Christi quoad fructum vel praemium*) + the 3-question listing, then **QUAESTIO I**. The scholion sits *above* the ART. II body but *under* the ART. II QUAEST. I running head.
- **PDF p.408 = printed p.386** (`crop-p386-bottom.png`): a1-q3's body **concludes here** ("…utrum passionibus contingat mereri, vel demereri.") with its footers nn.1–9; **no scholion prints at the foot of p.386.**
- **Decisive parallel — PDF p.407 = printed p.385** (`crop-p385-top.png`): page head carries running head **DIST. XVIII. ART. I. QUAEST. III.** with **SCHOLION** (§I "Cum secundum actionem…" §II §III) printed directly beneath it, *above* q3's body. This fixes the Quaracchi convention operative in this very distinction: **a scholion printed at a page head, under that page's running head, belongs to the question named in the running head.**

Applying that convention, the p.387-head scholion (running head ART. II QUAEST. I) belongs to **a2-q1**. The content is consistent: a2-q1 (Christ's merit as to fruit/reward) opens by restating the passion-is-meritorious-via-voluntary-acceptance principle as its premise (cross-ref *cfr. infra d. 20. dub. 3. 4.*). The earlier promotion (a1-q3 commit df9b7e1 → forwarded to a2-q1) was **correct**. a2-q1 already carries it under the bracketed provenance label `[ad Art. I, q. III — impressum in capite p. 387]`, which accurately documents the head-of-page placement without disturbing ownership. **No edit required.**

### (c) Backfill-integrity confirmations

**Verdict: BOTH backfills intact and fully paired.**

- **`d19-a2-q1` p.409 nn.1–5 (commit 8a03195):** defs `[^p409-1]`…`[^p409-5]` present; each has a Latin body anchor, an English body anchor, and a page-split-map entry (5 defs × 4 occurrences each = 20 occurrences, all accounted for). Anchors: n.1 on *opera Trinitatis sunt indivisa* (beside existing `[^p408-7]`), n.2 on *Ioannis tertio*, n.3 on *auctoritate Magistri in littera*, n.4 on *Magister dicit in littera* (Respondeo), n.5 on *sicut aspicienti apparet* (end of Respondeo). Pairing clean.
- **p.349 nn.1–2 backfill (commit aef9bad):** **correction — this backfill lives in `d16-a1-q2`, NOT `d18-a1-q2`** (the resume-note chunk label was a typo; `git show aef9bad` titles it "vol3 d.16 a.1 q.2 → backfill p.349 footers 1–2"). In `d16-a1-q2`: defs `[^p349-1]: Cod. U *immo etiam*` and `[^p349-2]: Cod. Z *articulos*` present; each paired with a Latin body anchor, an English body anchor, and a page-split-map entry. Pairing clean. (`d18-a1-q2` correctly carries no p.349 markers.)

---

## 3. Build status

`cd site && node scripts/build-content.mjs` → **`Built content.json: 3 book(s), 1276 questions, 1082 translated`**. Parse clean; translated count **not regressed** (held at 1082); chunk count unchanged (1276). The one edited chunk (`d20-a1-q4`) has clean marker pairing for the new `[^p426-6]` (1 La + 1 En + 1 def).

---

## 4. Summary

| Item | Disposition |
|---|---|
| `[?]` flags d.11–d.20 | **0 found** — all grep hits are "none/NONE" statements or non-flag prose; no body flags |
| (a) p.426 marker 6 | **RESOLVED by backfill** — note 6 *is* printed (genuine dropout, not a source skip); `[^p426-6]` added to `d20-a1-q4` |
| (b) "Manifestum est" scholion | **`d18-a2-q1` correct owner**; no duplication; no change (running-head convention confirmed by parallel p.385) |
| (c) backfills | **Both intact & paired** — `d19-a2-q1` p.409 nn.1–5; p.349 nn.1–2 (in `d16-a1-q2`, not d18-a1-q2 — resume-note typo) |
| Chunks edited | **1** — `vol3/bon-sent-III-d20-a1-q4.md` (p.426 n.6 backfill + map/status corrections) |
| Build | Clean — 1276 chunks, 1082 translated (no regression) |

> Pass 1 closes the `[?]`-flag-resolution leg of the Vol III d.11–d.20 gate. Pass 2 (full-corpus style/formatting audit) and Pass 3 (cross-chunk boundary-integrity sweep d.11–d.20) remain open and continue to block d.21+.

---

## Pass 3 — boundary-integrity sweep (2026-06-05)

**Gate:** third and final locked-in pass (CLAUDE.md "Polish-blocker cadence" §3). For every chunk boundary that falls **inside** a printed page (a quaestio/divisio/scholion split mid-page), verified against the 450 dpi PDF column bands that (a) the receiving chunk opens a unit grammatically discontinuous-by-design (fresh Quaestio/Articulus/Dubium) or continuous where mid-prose; (b) the shared page's footer notes are fully accounted across both chunks (no drop, no double-claim); (c) **no IA-OCR cascade-MERGE splice** in the prior chunk's body tail.

**Method.** Boundary list built from frontmatter `printed_pages` in reading order (littera → divisio → a*-q* → dubia); a boundary is mid-page when the receiving chunk's first `printed_pages` value equals the prior chunk's last. **d.11–d.14 (prior-session builds, never swept this gate) = primary coverage:** every body-continuation seam rendered + read at 450 dpi (`extract-pages.py --dpi 450` + `colcrop.py`); apparatus-tail seams confirmed structurally. **d.15–d.20 (this session) = spot-check** per CLAUDE.md (documented hand-offs), ≥1 band-verified seam per distinction + re-verification of the three during-session backfills.

### Mid-page boundaries checked

**d.11–d.14 — NEW COVERAGE (un-swept until now).** Total mid-page boundaries: d.11 = 7, d.12 = 6, d.13 = 8, d.14 = 8 (31). All **body-continuation seams** rendered + band-read directly; all **apparatus-tail seams** (prior chunk ends in a `— S.Thom.,…` source-citation list → fresh Quaestio opener) confirmed by structure + footer-ownership maps. Directly band-verified seams:

| Seam | Page | Verdict |
|---|---|---|
| d11 littera → divisio | p.242 | CLEAN — littera owns LIBR.SENT. nn.1–7 (L+R cols); divisio owns NOTAE AD COMMENTARIUM nn.1–2 + p.241 x-ref. Split exact; littera ends cleanly at *eum coepisse*. No splice. |
| d11 divisio → a1-q1 | p.243 | CLEAN — TRACTATIO list complete; a1-q1 opens fresh ARTICULUS I / QUAEST. I; p.243 nn.1,3–10 forwarded to a1-q1, n.2 retained by divisio (documented + consistent). |
| d11 a1-q1 → a1-q2 | p.245 | CLEAN — apparatus-tail; a1-q1 scholion complete, a1-q2 opens QUAEST. II. |
| d11 a2-q3 → dubia | p.257 | CLEAN — a2-q3 Respondeo (Ad 2–4) complete to n.20; DUBIA opens. p.257 footer nn.1–11: a2-q3 owns 1–5 (=[^16]–[^20]), dubia owns 6–11 (=[^1]–[^6]). Exact. No splice. |
| d12 a1-q2 → a2-q1 | p.265 | CLEAN — a1-q2 Solutio (Ad 1–2) ends *divinae ultionis*; ARTICULUS II / QUAEST. I opens fresh. Body complete. |
| d12 a3-q2 → dubia | p.273 | CLEAN — a3-q2 Ad 4 ends at n.5 (*omnis paternitas in caelo et in terris⁵*); DUBIUM unicum opens. p.273 footer nn.1–8: a3-q2 owns 1–5, dubia owns 6–8 (=[^1]–[^3]). Exact. |
| d13 littera → divisio | p.275 | CLEAN — littera (Lombard, ends *agnitionis esset expers*) vs divisio (COMMENTARIUS / DIVISIO TEXTUS). Two footer blocks on p.275: LIBR.SENT. nn.1–3 (littera) + NOTAE AD COMMENTARIUM nn.1–2 (divisio). Both file-scoped IDs, no cross-file collision. Exact split. |
| d13 divisio → a1-q1 | p.276 | CLEAN — TRACTATIO (*restant hic duo quaerenda…*) complete; ARTICULUS I / QUAEST. I opens fresh. |
| d13 a1-q3 → a2-q1 | p.283 | CLEAN — a1-q3 Ad 6 (*duplex ampliatio capacitatis…in cooperando*) verified continuous + complete to n.6; ARTICULUS II / QUAEST. I opens fresh. No splice. |
| d14 divisio → a1-q1 | p.295 | CLEAN — TRACTATIO (three-question list) complete; ARTICULUS I / QUAEST. I opens fresh. |
| d14 a1-q1 → a1-q2 | p.298 | CLEAN — a1-q1 Ad 2 (*…ad hoc quod ipsum cognoscat*) verified complete + scholion present; QUAEST. II opens. (Prior fix 3f91852 backfilled orphaned p.298 n.3 into a1-q1 — confirmed intact against band.) |
| d14 a3-q3 → dubia | p.325 | CLEAN — a3-q3 Ad 6 ends at n.5 (*…factus est omnisciens⁵*); DUBIA opens. p.325 footer nn.1–8: a3-q3 owns 1–5, dubia owns 6–8 (=[^p325-6,7,8], "picked up from a3-q3"). Exact. No splice. |

Remaining d.11–d.14 mid-page boundaries are apparatus-tail seams (e.g. d12 a1-q1→a1-q2 p.264, d12 a2-q1→a2-q2 p.268, d13 a1-q1→a1-q2 p.278 / a1-q2→a1-q3 p.281 / a2-q1→a2-q2 p.286 / a2-q2→a2-q3 p.288 / a2-q3→dubia p.291, d14 a1-q2→a1-q3 p.302 / a1-q3→a2-q1 p.306 / a2-q3→a3-q1 p.312, p.318 / a3-q1→a3-q2 p.321 / a3-q2→a3-q3 p.323): prior chunk's tail is a complete Quaracchi source-citation list (cascade-merge structurally impossible in a citation list), receiving chunk opens a fresh Quaestio with its own per-page footer block. Confirmed by the page-split + footer-ownership maps in each chunk's `## Notes`; pattern identical to the directly-rendered apparatus-tail seams above (p.245, p.265, p.298). **Cascade-merge check on d.11–d.14 body tails: DONE — none found.**

**d.15–d.20 — SPOT-CHECK (session builds; documented hand-offs).** ≥1 seam band-verified per distinction; three during-session backfills re-verified against bands:

| Seam | Page | Verdict |
|---|---|---|
| d15 a2-q3 → dubia | p.340 | CLEAN — a2-q3 *quadruplex ira* Respondeo continuous + complete (Gregorius⁵ quote intact); DUBIA opens. p.340 nn.1–9 → a2-q3, n.10 → dubia. |
| d16 a1-q2 → a1-q3 | p.349 | CLEAN (post-fix, aef9bad) — p.349 footer = 9 notes; a1-q2 owns 1–7, a1-q3 (QUAEST. III) owns 8–9. Backfilled nn.1–2 now part of a1-q2's complete 1–7. Verified L+R footer bands. |
| d16 a2-q2 → a2-q3 | p.357 | CLEAN — a2-q2 ends *quando consummata fuit eius gloria*; QUAEST. III opens fresh. Footer: a2-q2 nn.1–6, a2-q3 nn.7–13. Contiguous. |
| d17 divisio → a1-q1 | p.363 | CLEAN — three-way page (littera tail + COMMENTARIUS/DIVISIO + ARTICULUS I/QUAEST. I). LIBR.SENT. footer split: littera n.1, divisio nn.2–3 + COMMENTARIUM note, a1-q1 n.4 (forwarded by divisio agent, documented). |
| d18 a1-q1 → a1-q2 | p.382 | CLEAN — footer: a1-q1 nn.1–4, a1-q2 n.5. Contiguous, no overlap. |
| d19 a2-q1 → a2-q2 | p.409 | CLEAN (post-fix, 8a03195) — a2-q1 CONCLUSIO+Respondeo+SCHOLION I complete; QUAEST. II opens fresh with n.6 (Augustinus de Civ. Dei). Footer: a2-q1 nn.1–5 (backfilled), a2-q2 nn.6–8. Verified against band. |
| d20 a1-q2 → a1-q3 | p.422 | CLEAN — a1-q3 (*Utrum aliqua creatura pura potuerit satisfacere…*) opens fresh QUAEST. III; *Sed contra* args (nn.7–9) intact. Footer: a1-q2 nn.1–3, a1-q3 nn.4–10. Contiguous. |
| d20 a1-q4 p.426 n.6 backfill | p.426 | Re-confirmed present (Pass-1 / 9c1c3ef): `[^p426-6]` paired. |

### Pass 3 summary

| Item | Disposition |
|---|---|
| Mid-page boundaries checked | **d.11–d.14: 31** (all, primary coverage — 12 body/structural seams band-rendered directly, 19 apparatus-tail seams structure+footer-map confirmed); **d.15–d.20: 8 seams** spot-checked across all 6 distinctions + 3 backfills re-verified |
| Gaps FOUND this pass | **NONE.** Every seam CLEAN. |
| Cascade-merge (splice) check on d.11–d.14 tails | **DONE — 0 found.** All body-continuation tails verified continuous + complete against 450 dpi bands. |
| Prior in-session backfills | **All 3 intact & band-correct** — d16-a1-q2 p.349 nn.1–2 (aef9bad); d19-a2-q1 p.409 nn.1–5 (8a03195); d20-a1-q4 p.426 n.6 (9c1c3ef). Plus earlier d14-a1-q1 p.298 n.3 (3f91852) confirmed. |
| Chunks edited this pass | **0** — no new gaps; all seams already clean or previously fixed. |
| Build | Clean — 1276 chunks, **1082 translated** (no regression). |

> **DECADE GATE COMPLETE.** All three passes of the Vol III d.11–d.20 polish-blocker gate are closed (Pass 1 [?]-flags + Pass 2 style/formatting + Pass 3 boundary-integrity). d.21+ is unblocked; next = `bon-sent-III-d21-littera`.
