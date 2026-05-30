# Decade Polish-Blocker Resolution Log — d.21–d.30 (Vol II)

**Date:** 2026-05-30. Fired after d.30-a3-q2 (last unit of DISTINCTIO XXX) shipped, per CLAUDE.md "Polish-blocker cadence." Three passes, all blockers for d.31+. Tooling added this session: `tools/polish-style-scan.py` (Pass 2 full-corpus invariant scan) and `tools/seam-screen.py` (Pass 3 mid-page-boundary continuity screen).

---

## Pass 1 — `[?]`-flag resolution (d.21–d.30 only)

A repo-wide sweep (`grep '[\^?]'` / pre-`## Notes` body scan) found that **almost all** `[?]` matches in d.21–d.30 chunks are the boilerplate "no `[?]` flags" string in `transcription_status` / `## Notes`. Only **one genuine inline-flagged ambiguity** plus the one **parked** numbering-gap item:

1. **d28-dubia — DUB. IV footnote-to-marker assignment (the single genuine `[?]` flag).** RESOLVED (PDF p.692, 450 dpi, via subagent). p.692 footer numbering restarts at page-top and runs continuously 1–5 (L-col band) then 6 (R-col). **Footer 1 (`Cur Deus homo I, c. 24`) anchors at the printed ¹ on *Anselmus* in DUB. III's tail** (the servant/market/pit example — Anselm *Cur Deus homo* I.24), **not** the DUB. IV opener. The DUB. IV dictum *Nihil tam est in nostra potestate quam ipsa voluntas* carries **no printed marker** (Lombard flags it *in littera*); no Augustine source footer was missed. "Cur Deus homo c.24" does **not** belong to DIST. XXIX (whose first NOTA is the separate centred *NOTAE AD LIBR. SENTENTIARUM* block on *Enchiridio*). **Action:** `[^18]` moved from the DUB. IV opener to *Anselmus* in DUB. III (both bodies); def text unchanged (En. clarified to "[Anselm,]"); `[^19]`–`[^23]` confirmed correct. The chunk's "[?] flags (1)" note was rewritten to a RESOLVED disposition; per-dubium footer count corrected (DUB. III = 6, DUB. IV = 5).

2. **d29-a3-q1 — deliberate `[^3]` numbering gap (parked item (b)).** CONFIRMED INTENTIONAL / ACCEPT. The gap is already documented in the chunk's own `## Notes`: p.704 L-footer "*In cod. Q secunda manus annotavit scilicet in originali iustitia sive rectitudine*" is a marginal/textual note on the article's running *iustitia* heading with **no in-text anchor**, so it is omitted as non-anchorable editorial marginalia, leaving a numbering gap. Body + apparatus both correctly carry `[^1],[^2],[^4]–[^10]` (9 entries); all retained entries have matching La/En + body anchors. No action needed.

**Pass 1 status: CLOSED.** No remaining unresolved `[?]` flags in d.21–d.30.

---

## Pass 2 — Style/formatting audit (FULL CORPUS, vol1 + vol2)

Ran `tools/polish-style-scan.py` across **every** Tier-2 chunk (vol1 + vol2) for: required frontmatter fields, `## Latin`/`## English`/`## Apparatus` structure, apparatus marker pairing (every `[^N]:` def anchored in **both** La + En bodies; no orphan body markers; no duplicate defs), page-break presence, `transcription_status` prefix, and legacy auto-chunked pars/divisio duplicates. Also ran the three guard-rail audits for d.21–d.30 (paraphrase 0 critical / 1 high = the known d21-a1-q1 OCR-garble false positive; headers no LOSS; apparatus-count 0 flagged) and `build-content.mjs` (parses clean: 2 books, 884 questions, 748 translated).

**Initial scan: 9 issues / 7 chunks. Fixed:**

| Chunk | Issue | Fix |
|---|---|---|
| `vol1/d11-littera` | missing `pdf_pages` | added `pdf_pages: [309, 310]` (printed 207–208, pt1 offset +102) |
| `vol2/d18-dubia` | missing `has_apparatus` | added `has_apparatus: true` (chunk has 8 apparatus entries) |
| `vol2/d21-a3-q2` | `[^13]` anchored in La but dropped from En | added `[^13]` at "an inclining [cause]" in English (parallel to `inclinativum[^13]`) |
| `vol2/d21-a1-q2` | def `[^16]` (Petr. Comestor) not anchored in either body | added `[^16]` after "*et reliquum corpus erat serpentis*" / "the rest of the body was that of a serpent" (the *ut sic* textual-variant lemma) in both bodies |
| `vol2/d24-p1-a2-q2` | defs `[^17]`,`[^18]` not anchored + `[^11]–[^16]` 2-position drift | **(parked item — invasive)** PDF p.564 (subagent): the prior "all 18 verified paired" note was WRONG. Re-anchored from the image: `[^17]` (*Sive secundum modum intelligendi*, footer 8) → *dici*; `[^18]` (Anselm *De Concord.*, footer 9) → *Anselmus*; footers 2/3 carry no printed superscript and are co-anchored to their lemmas (`[^11]` at *adiutorium simile sibi*, `[^12]`=*sensualitatem* variant at *sensibilitatem*) — hence the legitimate out-of-numerical-order body sequence 10,12,11,13,…. Every placement semantically verified vs its def (`[^13]`=Gen 2:18 at *adiutorium simile sibi*, etc.). |
| `vol2/d27-littera` | parked item (a): Cap. XII footers `[^24]`,`[^25]` dropped | PDF p.652 (subagent): `[^24]` La = `Quaest. 39. n. 1.` at "*Quaestionum Evangelii*"; `[^25]` La = `Cap. 2. n. 5. — Paulo inferius ante illud quo codd. B C et edd. 1, 8 addunt est.` at "*de Trinitate*". Markers added in both bodies; defs appended (La + literal En); status/Notes → 25 entries. |
| `vol2/d28-a1-q2` | parked item (c): p.679 L-col footers 1–2 lost between q2/q3 | PDF p.679 (subagent): confirmed footer block runs 1,2,3(=Deut 30:11),4… so footers 1–2 **precede** q3's footer 3 and belong to q2 (q3's back-reference flag was right). `[^9]` La = `Vat. cum edd. 3, 4 bono.` at q2 *Ad 5*; `[^10]` La = `Cfr. supra pag. 170, nota 2.` Markers added both bodies; q2 apparatus now 10 entries. |

**Final scan: 2 issues remain, both pre-existing and OUTSIDE the d.21–d.30 decade — FLAGGED for the owner (each belongs to its own already-passed/own decade gate, and altering it needs the full per-chunk OCR/PDF recipe, not a mechanical edit):**

- `vol1/bon-sent-I-d1-a1-q3.md` — a stray `[^?]` footnote marker in the *bonus/malus mercenarius* reply (both La + En), no apparatus def. Belongs to the d.1–d.10 gate. The English already carries an inline `[or "the carnal"]` translator-doubt gloss at the same spot — a content ambiguity, not a mechanical drop.
- `vol1/bon-sent-I-d42-a1-q4.md` — p.758 English paragraph is heavily OCR-garbled with multiple `[?]`/`[^?]` markers ("passive power *simpliciter*…obediential potency…"); a Tier-2-incomplete remnant. Belongs to the d.41–d.50 gate; needs a full rebuild from OCR, not a polish edit.

**Pass 2 status: CLOSED for d.21–d.30** (all in-scope mechanical issues fixed; 2 out-of-decade vol1 items flagged forward).

---

## Pass 3 — Cross-chunk boundary integrity sweep (d.21–d.30 only)

Ran `tools/seam-screen.py 21 30`: enumerated every adjacent-chunk pair in canonical order, identified those sharing a printed page (**80 mid-page boundaries**), and surfaced each prior-chunk Latin-body tail + next-chunk head. The cascade-merge signature is a grammatically broken splice in the prior chunk's tail; the screen flags any tail not ending in terminal punctuation.

- **78 of 80** mid-page boundaries: tail ends in terminal punctuation (`.` / `»` / `:`), head is a fresh structural opener (*Consequenter…* / *Secundo quaeritur…* / DUBIA opener / SCHOLION). These are **structural** boundaries at quaestio/article/dubia headers that merely fall mid-page — not mid-sentence splices — so no cascade-merge risk.
- **2 flagged suspects, both verified FALSE POSITIVES:**
  - `d29-a1-q2 → d29-a2-q1` (p.699): tail is a complete parenthetical scholion-pointer note ending `…»".)*`; the screen only flagged the trailing italic `*`. Body content (*Ad 6 … non operaretur frustra … eguerit gratia*) is grammatically complete. OK.
  - `d24-p1-a2-q4 → d24-p1-dubia` (p.571): tail = SCHOLION III commentator-roll ending `…Richard. a Med., hic a. 2. q. 1. —` (trailing em-dash). Verified against raw OCR (line 40046): the roll ends **exactly** there, immediately before `DUBIA CIRCA LITTERAM MAGISTRI` (line 40048). The em-dash is Quaracchi's own end-of-roll punctuation; **nothing dropped**. Faithful. OK.

**Parked-item seams re-verified at the PDF this session (via the Pass-2 subagents):**
- **d27-littera → d27-divisio** (p.652): body ends "…ad alia properans." immediately before COMMENTARIUS IN DISTINCTIONEM XXVII — grammatically complete, no splice.
- **d24-p1-a2-q2 → q3** (p.564→565): q2 closes "…Et ista sufficiant." into the p.565 SCHOLION — clean, no dropped text.
- **d28-a1-q2 → q3** (p.679): footer block confirmed 1,2(q2) | 3,4…(q3); the footers 1–2 that had been lost are now restored to q2; seam accounted.
- **d28-dubia → d29** (p.692): tail "…non adiuvantur a gratia divina⁶." (raw 48279) is complete immediately before DISTINCTIO XXIX (raw 48282) — no broken splice / cascade-merge.

The remaining d.21–d.30 mid-page boundaries rely on (a) the programmatic terminal-tail screen above and (b) the per-chunk build-time "Cascade-dropout check PASSED — seams grammatically continuous" verification recorded for every d.21–d.30 chunk in `next-session-resume.md`.

**Pass 3 status: CLOSED.** No cascade-merge / boundary dropout detected in d.21–d.30.

---

## Decade gate

All three passes CLOSED. **d.21–d.30 polish-blocker is satisfied — d.31+ dispatch is unblocked.** Next action per resume: `bon-sent-II-d31-littera` (DISTINCTIO XXXI opens raw 51357 / p.737; d.30-a3-q2 forwarded p.737 footers 3–5 to the d.31 dubium — pick them up there).
