# Vol IV (Book IV) — d.41–d.50 decade gate, Pass 1: `[?]` flag resolution

**Date:** 2026-07-21
**Scope:** Vol IV only, distinctions 41–50. Vol I's own d.41–d.50 log is a separate file
(`manual-review/d41-d50-polish-resolution-log.md`) and was not touched.
**Method:** 600 dpi eyes-on, `pdftoppm -r 600` at `pdf = printed + 20`, cropped to per-page
column bands. **Gutter measured per page** rather than assumed — the parity finding in
`manual-review/vol4-column-gutter-parity.md` is confirmed across this whole range at 600 dpi
(odd pages ≈ 1975–2100, even pages ≈ 2840–2950; scale the 450 dpi figures by 4/3).
**Standard:** every flag is either RESOLVED with a page citation, or formally ACCEPT-ILLEGIBLE
with a stated reason. Nothing was guessed silently. No chunk was committed and no build was run.

---

## A. Briefed flags — inline `[?]` in reader-facing text

### A1. `bon-sent-IV-d41-littera`, p.857 — Lombard Cap. VIII `consanguinearum[?]`
**RESOLVED.** p.857 left column, top (PDF p.877). The definition prints unambiguously:
*« Incestus est **consanguinearum** vel affinium abusus; unde incestuosi dicuntur qui consanguineis
vel affinibus suis abutuntur ».* The feminine genitive plural is what Quaracchi set. That it
differs from the more familiar masculine *consanguineorum* of the canon is an edition-level fact,
not a transcription doubt. `[?]` removed; text unchanged.

### A2. `bon-sent-IV-d42-a2-q2` — Respondeo, `alis[?]` / "such[?] kinship"
**RESOLVED.** p.875 left column, in the Respondeo (PDF p.895), magnified to the individual word.
The print shows four letters — **a-l-i-s** — at the head of the line, with no *t* and no
hyphenation carried over (the preceding line ends *…et quoniam*). So *alis* is genuinely what is
set, and the raw OCR at L93147 was faithful. It is an evident dropped-*t* for **talis**: the exact
phrase stands a few lines above on the same page in argument 3, *talis cognatio legalis nulli bono
matrimonii repugnat*. The emendation is Quaracchi's to make, not ours — Latin left as printed,
English keeps the sense-reading "such kinship". `[?]` removed from **both** occurrences, because
the *reading* is no longer in doubt.

### A3. `bon-sent-IV-d44-p2-a3-q1` — scholion §I, `Scot., infra d. 49[?]. q. 13. n. 10.`
**RESOLVED.** p.931 left column, foot (PDF p.951). The line prints: *De hac 1. quaestione praeter
laudatos: Scot., infra d. **49**. q. 13. n. 10. — B. Albert., hic a. 39. — Petr. a Tar., hic q. 2.
a. 3.* The digit is clean. `[?]` removed from Latin and English.

### A4. `bon-sent-IV-d44-p2-a3-q1` — scholion §II, Henry of Ghent, `vim[?]`
**RESOLVED.** p.931 right column (PDF p.951). The quotation prints: *…quod Deus naturae spiritus
angelici et humanae **vim**, qua pati possit ab igne corporali, imprimit supernaturaliter…*, with
*vim* set in italic. `[?]` removed and the italics restored.

---

## B. Flags parked in earlier sessions' notes

### B5. `bon-sent-IV-d42-a1-q1` — the "pag. 868, nota 11" cross-reference
**RESOLVED — it is an edition-internal numbering slip, not a lost note.** Both pages re-imaged.
- **p.869** (PDF p.889), right-column footer: note 7 prints verbatim *Vide supra pag. 868, nota 11.*
  Page number and note number are both unambiguous, so the reference itself was transcribed
  correctly.
- **p.868** (PDF p.888) carries **exactly ten** numbered footers. Left-column register: 1, 2, 3, 4,
  5 (note 5 running long, into the Glossa enumeration). Right-column register: the runover of 5,
  then 6, 7, 8, 9, 10, ending *…textu originali consentiente, additur in poenitentia.* The register
  below note 10 is blank, and the last body anchor on the page is superscript 10.

So nothing was dropped by the IA scan or by the OCR — there is no eleventh footer in the print.
The cross-reference is preserved verbatim and **no `[^p868-11]` is created.** Recorded but *not*
acted on: the anchor sits on *in aqua et Spiritu sancto*, which is precisely what p.869's own
note 1 glosses (*Ioan. 3, 5: Nisi quis renatus fuerit ex aqua et Spiritu sancto etc.*), so the
editors most likely meant their own page's note 1. We do not emend Quaracchi's citation.

### B6. `bon-sent-IV-d42-a2-q1` — p.874 note 1, *transumtum* codex sigla
**RESOLVED, and the earlier reading was wrong.** p.874 left-column footer (PDF p.894). The entry
reads, in full and cleanly: *Vide supra a. 1. q. 1. — Pro **transumtum** cod. **P** **transumtivum**,
cod. **Q** **transumtive**.* Two sigla, P and Q; no third variant.

The supposed second variant *sumtivum* was an artifact of the clipped band: the line breaks
*tran-* / *sumtivum*, and the old crop lost the *tran-*. **The cause was exactly the diagnosed one**
— p.874 is an even page whose true gutter is x≈2873 at 600 dpi (≈2155 at 450 dpi), and the old
`colcrop.py` default of 1880 cut ~270 px into the left column's line-ends. The spurious
`[al. sumtivum]` has been removed from Latin and English.

### B7. `bon-sent-IV-d42-littera` — p.865 note 5, `Matth. 19, 5; 6, 32.`
**RESOLVED as printed.** p.865 right-column footer (PDF p.885). The entry reads *Can. Ad limina
(7.), ibid.; et citantur Matth. 19, 5; 6, 32.* — the line breaking after `6,` with `32.` opening
the next line. The reading is certain, so `[?]` is removed. The *oddity* is Quaracchi's, not ours:
the glossed clauses answer to Matt 19:6 (*Quod Deus coniunxit*) and Matt 5:32 (the fornication
exception), so `19, 5; 6, 32` looks like a compressed or mis-set reference. Recorded here;
transcribed as printed; not emended.

### B8. `bon-sent-IV-d45-a2-q3` — p.946 note 6 ending at *pro divite*
**RESOLVED — and it was a real text loss, ~120 words.** The predicted defect class was right, but
one column earlier than predicted: this is a **same-page, column-to-column footer runover**, not a
cross-page one.

p.946 (PDF p.966): the **left-column** footer register carries notes 1–6 and breaks off
mid-sentence at the foot of the column (*…ad similitudinem candelae, quae accenditur pro divite*).
The **right-column** footer register then opens with an **unnumbered continuation of that same
note** — *in domo et illuminat omnes circumstantes… Et hoc mihi placere magis confiteor.* — before
its own numbered note 7. The join is seamless.

The recovered span carries the whole point of Praepositivus's candle analogy (the alms profiting
those for whom it is *not* offered), the Jerome quotation *Cum pro defunctis psallimus animabus…*,
the editorial bracket *[Vide infra in solut. ad 4.]*, and the objection-and-answer about general
versus special prayers (*identitas enim mater est fastidii, sicut econtra varietas desiderii*). It
is now restored in both the Latin and the English. p.947's footer register was also checked and is
clean — it opens directly at its own note 1.

**Lesson for the corpus:** the footer runover can be **intra-page**. Check the facing column's
footer head, not only the next page's.

### B9. `bon-sent-IV-d45-dubia` — p.953 notes 6 and 7
**BOTH CONFIRMED and corrected.** p.953 right-column footer register (PDF p.973):
- note 6: *De Div. Nom. c. 7. § 2. Cfr. tom. II. pag. 177, **nota 5**.* — the chunk read `nota 3`.
  (The entry's other cross-reference, *tom. I. pag. 714, nota 5*, was already right.)
- note 7: *Cfr. I. Sent. d. 6. dub. 5. et III. Sent. **d. 35. q. 4.** ad 2.* — the chunk read
  `d. 33. q. 1.` The preceding *I. Sent. d. 6. dub. 5.* was already right.

Both corrected in Latin and English.

---

## C. Found in this pass and NOT on the briefed list

### C1. The briefed count of inline flags was low — there were **nine**, not four
Five further inline `[?]` were sitting in reader-facing text in this decade. All five were
resolved in the same pass, at 600 dpi, and none needed accepting as illegible.

| chunk | flag | disposition |
|---|---|---|
| `d41-a1-q1` | p.859 note 9, `…cod. F *et* ponit. [?]` | **RESOLVED** (PDF p.879, right col). The entry ends *Superius pro **et post** cod. F **et ponit**.* The lemma is the two-word phrase *et post*; the earlier reading mis-split it as *pro ei / post cod. F / et ponit*, which is what made the sense opaque. Latin + English corrected. |
| `d41-a1-q2` | p.861 note 5, `Sensus [non stat] … [?]` | **RESOLVED** (PDF p.881, right col). Prints *Inferius post generationem **ex** cod. E (secunda manus) **substituimus** genus consanguinitatis pro genus affinitatis, in cod. bb gradus affinitatis. — **Sensus est:** nisi genus sumatur large pro utroque impedimento.* Two errors fixed: the verb is first-person editorial *substituimus* (the editors emended), not *substituit*; and the clause is *Sensus est:* not the conjectural *Sensus [non stat]*. |
| `d41-divisio` | `[^6]`, `codd. et ed. *gradu*[?]` | **RESOLVED** (PDF p.878, left col, p.858 note 2). Prints *Mox pro genere codd. et ed. **1** gradu, Vat. recte refragante.* The missing element was the edition numeral **1**. |
| `d43-dubia` | p.904 note 7, `n. 2. [?] et 8` | **RESOLVED** (PDF p.924, right col). Prints *Vide eius Epist. 119. (alias **152**.) n. 2. **4.** et 8, ubi docet…* Two fixes: the gap is `4.`, and the *alias* number is **152**, not the `132` the chunk carried. |
| `d44-p2-a1-q2` | p.924 note 2, `Pro *[?]* vide Matth. 22, 14` | **RESOLVED** (PDF p.944, left col). Prints *— Pro **maiori** vide Matth. 22, 14…* The lemma is *maiori*. |

### C2. `d44-p2-a3-q1` scholion §II — four unflagged misreadings
The §I/§II scholion had been set from OCR alone with no band to check it against, and the 600 dpi
p.931 read turned up four errors that had never been flagged:
- Henry of Ghent's Quodlibet reference is **q. 34.**, not `q. 31.`
- The Gotti reference is **dub. 4. § 3.**, not `dub. 1. § 3.`
- Inside the Henry quotation: *licet nobis **latet***, not `lateat`.
- *obiectum disconveniens dupliciter**:*** — colon, not semicolon.

All four corrected in Latin and English. This is the same species of risk as the gutter defect:
OCR-only text that reads as well-formed Latin and therefore survives every audit.

### C3. `d41-littera` `[^p856-4]` — a fabricated `, ibid.`, and a recovered continuation
This inline `[?]` was not on the briefed list. Two findings, both material.

**(a) The entry does continue, and the continuation was missing.** It is a **cross-page footer
runover**: unnumbered, at the head of p.857's LEFT-column footer register, immediately above
p.857's own note 1 (PDF p.877) — *(3.), ibid.; tertius (in eapp. 5-9.) C. Consanguineos (1.),
ibid.; sed ultima propositio est ex Gratiano, super C. Si duo (4.), ibid. Quae sequuntur idem habet
super C. Lex illa (2.), C. 36. q. 1.* Now folded into the entry in both languages. (A d.41 session
note had spotted this text on the page and explicitly declined to act on it as "out of scope";
it is in scope here.)

**(b) Residual — ACCEPT-ILLEGIBLE for one short span.** p.856's note-4 line (PDF p.876,
right-column footer) runs to the physical right edge of the imaged sheet and is trimmed there,
after *…Seq. locus est C. Notificamus* plus one clipped glyph. The register below it on p.856 is
blank — it is a one-line note — and the raw OCR breaks off at the identical word. So the loss is in
the **digitization of the sheet**, not in the band crop, and re-cropping cannot help. The
*Notificamus* parenthetical (and possibly a few words before the surviving `(3.),`) is
unrecoverable from this scan. `[?]` retained at exactly that point.

**(c) Correction made at the same time:** the earlier rendering read `*Notificamus* (…)[?], ibid.`
The trailing `, ibid.` appears neither on the page nor in the OCR — it was an editorial
reconstruction — and has been removed.

### C4. `d44-p2-a1-q2` p.924 note 3 — a silent emendation reverted
The chunk rendered Jerome's bracketed reference as `[Matth. 12, 40.]`, with a Notes entry saying
the OCR's `12, 14` had been "resolved by scriptural context." At 600 dpi **the page plainly prints
`[Matth. 12, 14.]`** — the OCR was faithful and the emendation was ours. Matt 12:40 is indeed the
*in corde terrae* verse, so the editors' intent is not in doubt, but the project rule is to
transcribe as printed and record the anomaly, not to correct Quaracchi silently. Restored to
`12, 14` in both languages, with the intended locus noted in `## Notes`.

---

## Dispositions at a glance

| # | flag | disposition |
|---|---|---|
| A1 | d41-littera `consanguinearum` | RESOLVED — p.857 L |
| A2 | d42-a2-q2 `alis` | RESOLVED — p.875 L |
| A3 | d44-p2-a3-q1 `d. 49` | RESOLVED — p.931 L |
| A4 | d44-p2-a3-q1 `vim` | RESOLVED — p.931 R |
| B5 | d42-a1-q1 "pag. 868, nota 11" | RESOLVED — edition slip; p.868 has exactly 10 footers |
| B6 | d42-a2-q1 *transumtum* sigla | RESOLVED — cod. P / cod. Q; `[al. sumtivum]` was a crop artifact |
| B7 | d42-littera `Matth. 19, 5; 6, 32` | RESOLVED — as printed |
| B8 | d45-a2-q3 p.946 note 6 | RESOLVED — intra-page column runover recovered (~120 words) |
| B9 | d45-dubia p.953 notes 6, 7 | CONFIRMED + corrected (`nota 5`; `d. 35. q. 4.`) |
| C1a | d41-a1-q1 p.859 note 9 | RESOLVED — *pro et post … et ponit* |
| C1b | d41-a1-q2 p.861 note 5 | RESOLVED — *substituimus* / *Sensus est* |
| C1c | d41-divisio p.858 note 2 | RESOLVED — *codd. et ed. 1 gradu* |
| C1d | d43-dubia p.904 note 7 | RESOLVED — *(alias 152.) n. 2. 4. et 8* |
| C1e | d44-p2-a1-q2 p.924 note 2 | RESOLVED — lemma *maiori* |
| C3b | d41-littera `[^p856-4]` tail | **ACCEPT-ILLEGIBLE** — sheet trimmed in the scan; no second line exists; OCR breaks at the same word |

**One flag accepted as illegible; all others resolved.**

---

## Chunk files edited

- `vol4/bon-sent-IV-d41-littera.md`
- `vol4/bon-sent-IV-d41-divisio.md`
- `vol4/bon-sent-IV-d41-a1-q1.md`
- `vol4/bon-sent-IV-d41-a1-q2.md`
- `vol4/bon-sent-IV-d42-littera.md`
- `vol4/bon-sent-IV-d42-a1-q1.md`
- `vol4/bon-sent-IV-d42-a2-q1.md`
- `vol4/bon-sent-IV-d42-a2-q2.md`
- `vol4/bon-sent-IV-d43-dubia.md`
- `vol4/bon-sent-IV-d44-p2-a1-q2.md`
- `vol4/bon-sent-IV-d44-p2-a3-q1.md`
- `vol4/bon-sent-IV-d45-a2-q3.md`
- `vol4/bon-sent-IV-d45-dubia.md`

Each carries a dated `transcription_status` note and a rewritten flag paragraph in `## Notes`.
No apparatus marker was renumbered or relabelled. Nothing was committed; the build was not run.

## Carried into Pass 2 / Pass 3

- **Not inline, but worth a band check in the boundary sweep:** `d44-p1-a3-q2` p.915 note 4
  (`c. 4` final digit), `d44-p1-a2-q1` p.911 note 10 (`q. 3` vs the parallel `q. 5` at p.910
  note 8) and its p.912 scholion *quoad secundas*, `d44-p1-a1-q1` scholion (`n. 15` vs OCR `13`),
  `d44-p1-littera` p.906 note 1 (reconstructed variant clause), `d44-p2-a2-q2` p.928 note 2
  (`q. 9. n. 1`). These are logged in their chunks' `## Notes` as judgment calls rather than
  parked `[?]`, so they are outside Pass 1's remit — but each is one 600 dpi crop away.
- **Pass 3 should look specifically for more footer runovers**, now that both variants are
  confirmed in this decade: cross-page (p.856→p.857) and intra-page column-to-column (p.946 L→R).
