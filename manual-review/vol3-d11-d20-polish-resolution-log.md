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
