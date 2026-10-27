# Vol VI *Ioannem* MID-WORK GATE (p. 371, ruling 76): EVIDENCE SHEET

Compiled 2026-10-27 by a read-only agent on Wilson's go. **Nothing here is settled. Wilson rules off this sheet.** No file
under `vol*/` was edited; no tool, ledger, registry or resume note was touched; nothing pushed, deployed or stashed; no plate
deleted. Passes 1–3 are in `manual-review/vol6-ioannem-midwork-gate-passes.md`.

**Scope: 40 chunks, `bon-ioan-c2-v1-11` … `bon-ioan-c8-v51-59`, pp. 269–372** (p. 269 nn. 2–13 after `c1-v43-51`'s n. 1; p. 372
nn. 1–5, nn. 6–12 pending for Cap. IX). **1,244 numbered entries + 1 unnumbered closing note (`[^p357-nota]`) = 1,245 defs,
+ 35 `tr-` notes** (`tr-doctrina` 24 · `tr-lumen` 8 · `tr-vacare` 3). The brief's "~1,300" was an estimate; the count is derived
(`check-vol5-apparatus.py` per-chunk rows summed; independently, KNOWN_TOTALS pp. 270–371 = 1,227 + 12 + 5).

⛔ **Every census is over the LIVE region only** (`## Latin`, `## English`, and the `**La.**`/`**En.**` halves of `## Apparatus`;
footnote labels stripped; frontmatter and `## Notes` excluded). Paragraph parity La = En holds in all 40 chunks (673 numbered lines),
so body sites were aligned paragraph by paragraph. Scripts: scratchpad `gate/sweep.py`, `gate/census.py`, `gate/live.py`.
Each banked item was checked against the built file (live-region grep) and, for resolver items, against `index/citations.tsv`
(byte-identical to a fresh `build-citations.py` run). **Every banked item's description was CONFIRMED as stated; none was found
wrong.** One was REFUTED in its open hypothesis ((23)/(39): our paragraph numbering is not off by one — p. 302 prints `84.`).

---

## ▶ ONE-SCREEN SUMMARY

| § | items | recommendation (mine) | text lines | kind |
|---|---|---|---|---|
| **1** | ⭐ **NEW N1 + (78), (67), (32): the scholastic formula labels drift by capitulum** — *Respondeo* → "I respond" 77 · **"I answer" 16 (Cap. VIII, 5 chunks)** · **left in Latin `Respondeo:` 15 (Cap. IV, 4 chunks)**; *Contra*/*Sed contra* → "On the contrary" 36 · **left in Latin 7 (Cap. IV)** · "Against" 2 (78) · "Against this" 1 · "To the contrary" 1 | **Conform all to the CLAUDE.md formula table** ("I respond:", "On the contrary:"). **Sap ruling 41 already called an English `**Contra:**` a DEFECT and repaired it** — so the 22 Latin-left labels are defects by precedent, the 20 drifts are conformances | **42** | mechanical |
| **2** | misprint / failing-impression class: (2) (8) (17) (20) (25) (27) (40) (43) (55a) (56) (57) (63) (68) (69) (74) + **NEW N2 bracket-form drift** (six bracket shapes in scope) | Ratify the class as built (Sap ruling 45; rulings 85/86). **Conform the bracket FORM** to ruling 45's two shapes + ruling 86's name shape (≈5 lines). (17): re-read *cx* beside the failed-eye *e*'s at the close — keep or conform (0 or 2). (27): keep unmarked (a medieval title form, not a misprint) | 5 (+0–2) | mechanical / per-site |
| **3** | Quaracchi cross-reference slips: (23)+(39) `n. 83` (off-by-one in our build REFUTED on the plate), (18) `infra n. 39`, (41-Bede) | (23)/(39): **ruling 38 bracket** ("[so printed; the question is n. 84]") ×2, or record-only; (18), (41): record only | 2 or 0 | per-site |
| **4** | schemata and unnumbered notes inside the apparatus: (1) (19) (38) (42) (51-schema) (52) (58) (60) (65) (71-schema) | **Ratify as one rule:** a full-measure schema in a note is rendered inside its entry, as ruling 18's nested outline (multi-level) or label + flat list (one brace); a note whose own text introduces the schema keeps it inside the numbered entry; an unanchored schema last on its PAGE takes the frozen closing-note label `[pN-nota]` (60). (19) ` / ` for a verse break inside an entry: ratify | 0 | record-only |
| **5** | titles, headings, structure, index: (10) (11) (37) (49-title) (50) (72) (33) (80) (3) (38-tr) | Ratify all as built: ruling 79(b) covers a stack inside ¶ 1 and a three-deep stack; **a ruling-17 "first sentence" runs to the full stop through colon and semicolon alike** (11/49); (50) record as an index page misprint (82(d) extended); (72) as printed, no label supplied; (3)/(38) `tr-lumen` in an `**En.**` half is ruling 13 working | 0 | record-only |
| **6** | register — unruled renderings by nearest precedent: (5) (7) (15) (16) (21) (22) (26+12 rest) (28) (29) (30) (35) (41) (45) (46) (49) (51) (53) (54) (59) (64) (70) (76) (77) (82) + NEW N3 *intellectus* → "intellect" (c7-v40-53), N4 roman `d.` numerals | **Ratify the block** (the (46)/(49) "Douay adjusted where the exposition leans on the word" move is now a rule in fact: ~12 sites). **One real split: (26)/(12) *eruditio* → "instruction" ×5 vs "erudition" ×3** — conform to "erudition" (5 lines). (53): ratify the womb/belly sense split. (59): ratify the verse test over the Vol V exemption. N4 optional (1 line) | 5 (+1) | per-site / record-only |
| **7** | resolver docket: (4) (6) (9) (13) (14) (24) (31) (34) (36) (44) (47) (48) (55-res) (61) (62-res) (66) (75) (81) + 15 unresolved-anaphora QA lines | **No text edit** (ruling 82(a)). All confirmed in the ledger. **Six tool jobs**, dangerous classes first: **D1 cross-note anaphora binding `ibid.`/`loc. cit.` onto Scripture at A or a wrong `chunk` (10 sites)** and **D2 *primae Ioannis* read as the Gospel (8 sites)** | 0 | tool |
| **8** | documentation: (79) | Correct `c8-v37-50`'s Notes `n. 47` → `n. 17` (2 Notes lines) at the close, or leave the resume-note record as sufficient | 0 (+2 Notes) | record-only / doc |

**Item count: 80 open, every one placed once by its PRIMARY question** (secondary parts noted in place, e.g. (55)'s restoration in § 2,
its renderings in § 6, its unemitted `II. Paralip.` in § 7):
§ 1: (32) (67) (78) = 3 · § 2: (2) (8) (17) (20) (25) (27) (40) (43) (55) (56) (57) (63) (68) (69) (74) = 15 · § 3: (18) (23) (39) = 3 ·
§ 4: (1) (19) (38) (42) (52) (58) (60) (65) = 8 · § 5: (3) (10) (11) (33) (37) (50) (72) (80) = 8 · § 6: (5) (7) (15) (16) (21) (22) (26) (28) (29) (30)
(35) (41) (45) (46) (49) (51) (53) (54) (59) (64) (70) (71) (76) (77) (82) = 25 · § 7: (4) (6) (9) (13) (14) (24) (31) (34) (36) (44) (47) (48) (61) (62)
(66) (75) (81) = 17 · § 8: (79) = 1. **Total 80.**

**By kind (80 banked items):** mechanical 4 ((2)'s bracket form, (57), (63), (78)) · per-site 4 ((17), (23), (39), (26)) · tool 17 · record-only 55
(incl. (79), doc only).
**Plus 4 new findings** (N1 mechanical, N2 mechanical, N3 record-only, N4 optional).
**If every recommendation is taken: ~54 English lines (42 formula labels + ~5 brackets + 5 *eruditio* + 2 ruling-38 brackets), 0–2 Latin
lines ((17) only, if conformed), 2 Notes lines. No `## Latin` text changes otherwise; no resolver edit.**

⚠ **For Wilson first:** § 1 (42 lines, and Cap. IX onward should be briefed "I respond:" / "On the contrary:" before the next chunk);
§ 7's D1/D2 classes are now 10 + 8 silent wrong records inside this scope alone.

---

## 1. THE SCHOLASTIC FORMULA LABELS — DRIFT BY CAPITULUM (NEW N1; absorbs (78), (32), (67))

**The rule.** CLAUDE.md § Scholastic formulae: *Sed contra / Contra* → "On the contrary"; *Respondeo* → "I respond". **Sap ruling
41** (Vol VI, 2026-10-16): *"DEFECT REPAIRED: c2 English `**Contra:**` at pp. 123 and 125 → '**On the contrary:**' (c1's form and
the formula table's). The Latin keeps `**Contra:**`."* So an English half that leaves the Latin label is a defect by ruled
precedent, not a style choice.

**Census — every bold label in the 40 English bodies** (Latin labels: `Respondeo:` 102 + 6 other forms; `Contra:` 26, `Sed contra:` 4,
`Contra hoc:` 1, `Sed contra` 1; plus running italic *— Contra:* inline):

| English form | sites | chunks | verdict |
|---|---|---|---|
| **I respond:** | 77 (71 bold + 6 `**I respond**` run-in) | Cap. II–III, `c4-v1-6`, Cap. V–VII, `c8-v31-36` | ✓ table |
| ⚠ **Respondeo:** (Latin left in the English) | **15** | `c4-v7-14` 4 · `c4-v15-27` 2 · `c4-v28-42` 6 · `c4-v43-54` 3 | **DEFECT** (Sap 41's class) |
| ⚠ **I answer:** | **16** | `c8-v1-11` 3 · `c8-v12-20` 2 · `c8-v21-30` 2 · `c8-v37-50` 4 · `c8-v51-59` 5 | drift from the table |
| **On the contrary:** (display + running) | 36 | Cap. III, V–VII, `c8-v31-36`, `c8-v51-59` | ✓ table |
| ⚠ **Contra:** / *— Contra:* (Latin left) | **5** | `c4-v7-14` ¶ 25 (display), ¶¶ 26, 27 (running); `c4-v15-27` ¶ 44; `c4-v28-42` ¶ 64 | **DEFECT** (Sap 41 exactly) |
| ⚠ **Sed contra:** / **Sed contra** hoc est (Latin left) | **2** | `c4-v28-42` ¶ 68; `c4-v43-54` Quaest. II | **DEFECT** |
| ⚠ **Against:** / *— Against:* | 2 | `c8-v12-20` ¶ 27; `c8-v21-30` ¶ 44 | **= banked (78)** |
| ⚠ **Against this:** (*Contra hoc:*) | 1 | `c4-v43-54` ¶ 84 | drift |
| ⚠ *— To the contrary:* | 1 | `c5-v10-18` ¶ 34 | drift |

Running "I answer otherwise" (`c7-v14-18`, *Vel aliter respondeo*-type prose) is prose, not the label, and is not counted. `c6-v1-9`
¶ 2's *sed contra:* (lower case, inside a sentence) → "on the *contrary:*" is prose, not counted.

**Why it went unseen.** Every chunk reports the census its own builder thought of; nobody censused labels across chunks. (78) was
banked only because `c8-v51-59`'s builder noticed its two predecessors. Cap. IV's four chunks (one session's run) kept the Latin
labels throughout; Cap. VIII's builders adopted "I answer" from `c8-v1-11` onward and carried it forward as the "previous-chunk
format reference" — the session loop's format-reference step propagates a drift exactly as it propagates a convention.

| option | cost |
|---|---|
| **(a) Conform all to the table** — "I respond:" ×31, "On the contrary:" ×11 (incl. *Contra hoc* → "On the contrary:", the Latin's *hoc* is the formula's own) | **42 En lines**, mechanical; Latin untouched |
| (b) Conform only the 22 Latin-left sites (the Sap 41 defects); ratify "I answer"/"Against" as variants | 22 lines; leaves three English forms for one Latin label |
| (c) Leave | 0; contradicts Sap ruling 41 |

**⭐ Mine: (a).** (32) (¶ 89's *Respondeo* printed roman, not small caps — transcribed plain) and (67) (Quaest. IV's running italic
*— Contra:* kept inline, not lifted to a `**Contra:**` label, the `bon-qsc-q4` precedent) are **ratify as built** — they are about the
Latin face, which (a) does not touch; (67)'s English is (78)'s `— *Against:*` and goes with (a). ⚠ **Brief the Cap. IX builder**
with the two strings before the next dispatch, whatever is ruled.

---

## 2. THE MISPRINT / FAILING-IMPRESSION CLASS (Sap ruling 45, rulings 37/38/48/85/86)

**Ruling 45** (ratified the class): identifiable wrong sort or slip → as printed + English bracket — `[so printed: X for Y]` for a
letter fault, `[so printed; the verse/passage is …]` for a locus slip; unnameable sort → read plain + disclosed (the
`necessarium`/*sementia* rule); compositor's blank → reproduced + `[*sic*]`. Ruling 85: borderline faint letters restored in brackets.
Ruling 86: misprints in NAMES marked "[*so printed*]", not corrected.

| # | site | built (verified in the live region) | recommendation | lines | kind |
|---|---|---|---|---|---|
| (2) | `c5-v31-39` p. 314 n. 1 `Vers. 18.` (for 8:13) | Latin as printed; En "Verse 18 [*so printed*]"; ledger John 8:18 B | ratify as printed; **form → ruling 37's** "[so printed; the verse is John 8:13]"; a `PRINTED_SLIPS` (ruling 57 C2) row for the tool job | 1 | mechanical + tool |
| (8) | `c6-v1-9` p. 319 n. 3 `pag. 318, nota 11` (for n. 14) | En bracket "[*so printed*; … is p. 318 n. 14]" present | ratify | 0 | record |
| (17) | `c6-v22-33` ¶ 42 *cx panibus* | Latin *cx*; En "[so printed: *cx* for *ex*]"; builder: "at 10× no eye and no bar … full strength, no ghost" | **the one open classification.** A failed-eye italic *e* is, by definition, a *c*-shape with no bar — (20)/(25)/(40) read four such plain. Re-read *cx* beside `c6-v34-40` *spiritualem*/*desccndi* and `c7-v1-13` *scd* at the close: if the *c* has the *e*'s width and terminal, conform to plain *ex* (Latin 1 + English 1); else keep | 0 / 2 | per-site |
| (20) (25) (40) | ¶ 55 *spiritualem*, ¶ 59 *descendi* (`c6-v34-40`), p. 330 n. 8 *Deus* (roman, `c6-v41-52`), ¶ 13 *sed* (`c7-v1-13`) | read plain, pixel maps in Notes | ratify (the Vol V *sementia* rule; ruling 45's second branch), roman and italic alike | 0 | record |
| (27) | `c6-v41-52` ¶ 77 *de Bono perseverantiae* | unmarked | **keep unmarked**: *De bono perseverantiae* is the title the work commonly bore in scholastic citation, so it is not a misprint and ruling 86 does not reach it (to the best of my knowledge — Wilson may know otherwise) | 0 | record |
| (43) | `c7-v14-18` p. 343 n. 4 *Est … iudex* (body reads *iustus*) | En "*iudex* [*so printed*; the text above reads *iustus*]" | ratify — ruling 45 inside a variant note | 0 | record |
| (55a) | `c7-v40-53` ¶ 74 *iniq[u]itas* | brackets | ratify (ruling 85) | 0 | record |
| (56) | `c8-v1-11` p. 355 n. 6 unclosed `[B Non est bonum,` | as printed; En "[*so printed*]" | ratify as ruling 86's form extended to a garbled phrase | 0 | record |
| (57) | `c8-v1-11` p. 355 n. 9 *aliambue* (turned *q*) | En "*aliambue* [*so printed*]" (the NAME form) | ratify the reading; **form → ruling 45's letter-fault shape** "[so printed: *aliambue* for *aliamque*]" | 1 | mechanical |
| (63) | `c8-v21-30` ¶ 30 lemma *orediderunt*; p. 361 n. 6 *hoe* | En "[*so printed*, for *crediderunt*, "believed"]", "[*so printed*, for *hoc*]" | ratify (**a wrong sort in a LEMMA takes the bracket like any other** — ruling 48: the bracket marks a certain slip wherever it stands); **form → ruling 45's shape** | 2 | mechanical |
| (68) | `c8-v31-36` p. 364 n. 5 compositor's blank 〈 〉 | reproduced + "[*sic*]" | ratify (ruling 45, third branch) | 0 | record |
| (69) | `c8-v31-36` p. 364 n. 7 `Vers. 13.` under Deut. 6 | as printed, no bracket; ledger Deut 6:13 B | ratify (ruling 49: no bracket where a slip is possible but not shown) | 0 | record |
| (74) | `c8-v37-50` ¶ 71 *p[at]er* | brackets | ratify (ruling 85) | 0 | record |

**NEW N2 — the bracket FORM has drifted into six shapes in scope** (all 19 brackets in the 40 English halves listed):
`[so printed: X for Y]` ×7 (`c2-v1-11` ×3, `c2-v12-17` ×2, `c3-v17-21` *lueem*, `c6-v22-33` *cx*) ✓ ruling 45 · `[*so printed*]` ×5 (`c4-v15-27`
*Forceilini* ✓ ruling 86; `c5-v31-39` n. 1; `c8-v1-11` ×2) · `[so printed: *X*]` ×2 (`c4-v43-54` *Galileam*, `c5-v31-39` *alligantur*) ·
`[so printed]` ×1 (`c4-v43-54`, Mark 9:32) · `[*so printed*, for *X*]` ×2 (`c8-v21-30`) · `[so printed; …]` ×1 (`c5-v1-9` ✓ ruling 37) · `[*sic*]` ×1
(`c8-v31-36` ✓). Plus `c6-v1-9`'s `[*so printed*; …]` (ruling 37 shape, italic). **Recommendation: conform (2), (57), (63) ×2 now (4
lines, above) and ratify the rest** — `*Galileam*`/`*alligantur*` are name/reading forms where "for Y" adds nothing; `c4-v43-54`'s
bare `[so printed]` at Mark 9:32 could take ruling 37's "the verse is …" (1 line, optional). The roman/italic "so printed" difference
is cosmetic; leave it.

---

## 3. QUARACCHI'S OWN CROSS-REFERENCE SLIPS

| # | site | evidence | recommendation | lines | kind |
|---|---|---|---|---|---|
| **(23) + (39)** | `c6-v41-52` p. 329 n. 11 `Cfr. ibid. n. 83.`; `c7-v1-13` p. 340 n. 8 `Cfr. supra c. 4. n. 83.` — both for *propheta in patria* | **The off-by-one hypothesis is REFUTED.** Read on the plate here: p. 302 prints **`84. Quaest. I. Quaeritur de hoc quod dicit, quod propheta in patria sua honorem non habet.`** (1.0× crop; the `4` with its crossbar); the raw agrees (L48175 `84.`, L48042 `83. Prima hora`); `c4-v43-54` numbers ¶¶ 69–86 contiguously and its ¶ 83 is the *Moraliter*'s *Prima hora est incarnatio*. The verse is expounded at ¶ 70 and questioned at ¶ 84; nothing at 83 fits | **Quaracchi slip, twice, the same way** (the editors' drafting numbering, presumably). **Ruling 38 bracket** at both: "[so printed; the question is n. 84]" — ruling 38 covers a locus slip whose target is identifiable, and both notes point at the *propheta in patria* question. Or record-only if Wilson reads "n. 70 or n. 84" as not identifiable (ruling 49) | 2 / 0 | per-site |
| (18) | `c6-v22-33` p. 325 n. 2 `De praeced. propositione cfr. infra n. 39.` (anchored in ¶ 38) | ¶ 39 is the next paragraph (*Aliae vero supervenerunt naves*), not about *considerationem* | record only (target not identifiable, so no bracket); resolver: ruling 73's paragraph job will file it to `c6-v22-33` mechanically | 0 | record (+tool) |
| (41-Bede) | `c7-v1-13` p. 340 n. 11 Bede `in Ioan. 6, 6` for a gloss on 7:6 | as printed, no bracket | ratify (ruling 49) | 0 | record |

---

## 4. SCHEMATA AND UNNUMBERED NOTES INSIDE THE APPARATUS

Ruling 18 (Eccl): the Schemata render as **nested indented outlines** in both languages. It was made for the standalone Schemata
chunks; *Ioannem* now has **seven** schemata inside apparatus entries, all built on (1)'s precedent:

| # | site | form built | note |
|---|---|---|---|
| (1) | `c5-v31-39` p. 315 n. 6 *Testimonia Christo exhibita* | nested outline inside the entry | first |
| (38) | `c7-v1-13` p. 339 n. 1 *Verbum Dei fructum habet in comparatione* (4 × 3) | nested outline | + `tr-lumen` in its `**En.**` half (see § 5, (3)) |
| (42) | `c7-v14-18` p. 343 n. 6 *commendabilis comparate* (rotated label) | nested outline | |
| (51) | `c7-v32-39` p. 350 n. 5 braced schema | label + flat list | one brace → flat |
| (52) | `c7-v40-53` p. 353 n. 4 *Est iudicium laudandum* | two-level outline; the unlabelled summing paragraph as a fifth item of group 1 | placement by nearest form |
| (65) | `c8-v21-30` p. 363 n. 2 *est derelictio* | label + flat list INSIDE the numbered entry (the note introduces it) | |
| (71) | `c8-v31-36` p. 365 n. 5 *[S]ermo Dei est efficax* (13 members) | header + label + flat list inside the entry | second of (65)'s kind |
| (60) | `c8-v12-20` `[^p357-nota]` *Sola ed. habet … loquitur nobis Dominus* (unnumbered, full measure, foot of p. 357) | label + flat list; anchored after the page's last body word (behind n. 9) | the closing-note rule was for a note last in its UNIT; this is last on its PAGE |
| (58) | `c8-v1-11` the editors' supplement paragraph *Iesus autem, inclinans se* (p. 354 R) | own unnumbered paragraph, both languages | + (60)'s forwarding outside `KNOWN_TOTALS` |
| (19) | `c6-v22-33` p. 326 n. 10 Vatican couplet run on with ` / ` | inline | no hard break inside an entry |

Plate (Pass 3 agents): p. 339 n. 1 and p. 343 n. 6 stand full measure inside the register, as built; p. 357's unnumbered note
stands full measure below the two-column block (see the passes file).

**⭐ Mine: ratify as ONE rule, 0 lines, record-only:** *a schema printed inside a note is rendered inside that note's entry —
nested outline where the print nests, label + flat list where it braces once; a note whose own words introduce the schema keeps it
inside the numbered entry; an unanchored note standing last on its PAGE takes `[pN-nota]`, anchored after the page's last body
word.* (19): ratify ` / ` (a hard break inside a footnote def is fragile in the build). (58): ratify.

---

## 5. TITLES, HEADINGS, STRUCTURE, INDEX

| # | item | verified | recommendation | lines | kind |
|---|---|---|---|---|---|
| (10) | `c6-v1-9`: the stacked lower heading stands INSIDE ¶ 1 | title = lowest heading, whole | ratify: ruling 79(b) applies wherever the lowest heading over the unit stands | 0 | record |
| (37) | `c7-v1-13`: a THREE-deep stack (Pass 3 read `CAPITULUM VII.` + *Tertio, Filius Dei se manifestat …* on p. 338) | lowest, whole | ratify (79(b)); kin of (10) | 0 | record |
| (11) + (49-title) | ruling-79(a) titles run through a COLON (`c6-v10-13`, `c6-v41-52`) and through a SEMICOLON (`c7-v25-31`, also `c8-v51-59`) to the full stop | as built | **ratify: ruling 17's "first sentence" ends at the full stop** (its own exemplar runs through a semicolon) | 0 | record |
| (50) | index *Vers. 40-53 … 352*; ¶ 58 and `(Vers. 40.)` stand on p. 350 | `c7-v40-53` `verses: "40-53"` verbatim | record as an index PAGE misprint; 82(d)'s recording extended to cover it | 0 | record |
| (72) | `c8-v37-50` ¶ 70 printed without `Quaest. III.` | confirmed: Quaest. I, II, [¶ 70], IV–VII, both languages | ratify (dropped ordinal; nothing supplied) | 0 | record |
| (33) | p. 334 R two *Ad 1.* glosses | marginalia, Notes only | ratify | 0 | record |
| (80) | the `4` of *Vers. 54-59* | moot under ruling 87 | record | 0 | record |
| (3) + (38-tr) | `tr-lumen` written in an apparatus `**En.**` half (`c5-v31-39` p. 316 n. 11; `c7-v1-13` p. 339 n. 1) | 8 chunks carry Latin *lumen* in the live region; all 8 have `tr-lumen` (census below) | ratify (ruling 13's extension; Sap ruling 53's apparatus-only branch) | 0 | record |

**`tr-` obligation census (live region):** *lumen* in 8 chunks → `tr-lumen` 8/8 · *doctrin-* in 24 chunks → `tr-doctrina` 24/24 ·
*vaca-* in 3 chunks (`c4-v15-27` *vacabant*, `c5-v10-18`, `c6-v22-33`) → `tr-vacare` 3/3 (`c2-v1-11`'s *vacua/vacuitatis* are another word) ·
*studi-* 2 sites (`c3-v3-12` n. *discendi studium* → "an eagerness to learn"; `c8-v1-11` ¶ 6 *studio quaerendi*) → contextual, no note,
ruling 80(c) ✓. No chunk owes a note; no note stands without its word.

---

## 6. REGISTER — UNRULED RENDERINGS BY NEAREST PRECEDENT

**Ruling-74 register, censused over the 40 chunks (live region, Latin body+app → English):**

| item | Latin | English | verdict |
|---|---|---|---|
| *Spiritus sanctus* | 43 | "Holy Spirit" 47 (incl. glosses); **"Holy Ghost" 0** | ✓ 80(b) |
| *testimonium perhibere* | 49 *perhib-* | "give/gave testimony" 43+; **"bear testimony" 3 = Chrysostom's *testimonium ferunt/ferre* (`c8-v12-20` p. 359 n. 9)**; `c5-v1-9` *signa testatur* "bears witness" | ✓ 81(a) (*ferre* keeps "bear") |
| *signum* / *miraculum* | 125 / — | paragraph-aligned: **0 paragraphs** with more "miracle" than *miracul-* or fewer "sign" than *signum* | ✓ ruling 74 |
| *magister* | 36 | "teacher" 25; "the Master" = Lombard ×9 + "Master Hugh" (`c6-v14-21`, ruling 84); Wis. 12:18 *dominator* "master", servant's "master" (`c8-v31-36`) are other words | ✓ |
| *doctor* | 11 (+ *Doctor*) | "doctor" | ✓ 81(b) |
| *dilectio* | 23 | "dilection" 27 (incl. variant glosses) | ✓ |
| *intelligentia* | 21 | "intelligence" 19 + *Ad intelligentiam litterae* idiom "understanding" (`c4-v1-6`, the shakedown's accepted idiom) + participle *intelligentium* | ✓ (2026-10-23 conform holds) |
| *intellectus* | 31 | "understanding" — **except `c7-v40-53` p. 353 n. 4 schema *quantum ad intellectum* → "as to the intellect"** (faculty beside *affectus*; disclosed in that chunk's Notes, NOT banked) | ⚠ **NEW N3** |
| *munditia* / *pudicitia* | 3 / 1 | "cleanness" in the washing passages (`c4-v1-6`, ruling 83); *pudicitia* = a canon title *C. De pudicitia* in `c2-v1-11` p. 271 n. 9 (no register site) | ✓ |
| *Contra* / *Respondeo* | | see § 1 | ⚠ N1 |
| roman `d.` numerals in apparatus | 9 | kept roman in English 7; **converted to arabic 2 (`c5-v10-18` p. 308 n. 11, *d. XII … d. XV* → "d. 12 … d. 15")** | ⚠ **NEW N4** (house-style; corpus-mixed per the shakedown NOTE) |

**N3** — *intellectus* → "intellect" once, in an apparatus schema, where *intellectum* is the faculty set against *affectus*. The
Vol V rule is "in BODY PROSE"; its reason is a contrasting *intelligentia*, absent here; the `bon-praec-c2` departure was ratified on
the same discriminator. **Mine: ratify as built, record-only** (or conform to "understanding", 1 line).
**N4** — **Mine: optional conform to roman** (1 line), as 7 of 9 in scope; otherwise record.

**The banked renderings (all CONFIRMED in place; each was disclosed by its builder):**

| # | rendering | recommendation |
|---|---|---|
| (5) | *claritas* → "clarity" at 5:41 | ratify |
| (7) | *tentare* → "tempt", Douay adjusted at 6:6, Ps. 25:2, Ecclus. 13:14 | ratify |
| (15) | *virtus* → "power" at ¶ 36 (80(a) sense split); Wis. 5:17 Douay kept | ratify |
| (16) | *signare* → "sign" at 6:27 (against Douay "sealed"), ¶ 43's gloss *signavit, signo* — verified: "*For him hath God the Father signed; signed,* with the sign of his testimony" | ratify (the gloss leans on the word; ruling 74's *signum*) |
| (21) | I Cor. 13:12 "through a mirror and in an enigma" | ratify |
| (22) | *perdere* "lose" / *perire* "perish" kept apart | ratify |
| **(26) + (12)'s open half** | *erudire* → "teach" inside Prov. 9:7; ***eruditio*: 8 Latin sites, rendered "instruction" ×5 (`c2-v12-17` *verbum eruditionis*; `c3-v1-2` ×2, beside *instruens* "instructing"; `c3-v22-26`; `c5-v10-18`) and "erudition" ×3 (`c6-v10-13`)** | ⚠ **a real split, not banked as one.** `c8-v1-11` has *instructio* → "instruction", and `c3-v1-2` sets *verbo eruditionis* beside *instruens* — so "instruction" for *eruditio* collides with *instructio*'s root. **Conform the 5 to "erudition"** (per-site, 5 lines); *erudire* inside the Douay stays "teach" |
| (28) | *comedere* → "feed on" (keeps *manducare* on "eat") | ratify |
| (29) | 6:58 *propter Patrem* → "because of" | ratify |
| (30) | *litigare* → "strive" (II Tim. 2:24 adjusted) | ratify |
| (35) | *intelligentia* → "intelligence" for carnal construing ×3 | ratify (ruling as conformed 2026-10-23; cost banked) |
| (41) | *illustrator* "enlightener"; *propalatio* "disclosure"; *luminaria* "luminaries"; Job 26:12 *prudentia* "prudence" | ratify |
| (45) | *scientia* "knowledge" vs Douay "science of the saints"; Luke 2:47 *prudentia*; *doctrina* "teaching" inside Douay; John 3:33 Douay "set to his seal"; *discretive*; **II Thess. 2:4 in both faces in one chunk** | ratify; both-faces → record (see (71)) |
| (46) | *indignari* → "be indignant" at 7:23; *daemonium* "a devil" beside *diabolus* "the devil" | ratify |
| (49) | *oblocutio* "obloquy"; Jer. 8:5 "apprehended a lie"; *notitia*/*cognitio* "knowledge"; *turba* "people" | ratify |
| (51) | *venter* → "belly" at every site of Quaest. I (Ps. 39:9, Isa. 16:11 Douay overridden) | ratify |
| (53) | *venter* → "womb" at Ps. 131:11, Luke 11:27; *utero* "bowels" | **ratify the sense split** — census: *venter* 30 sites → "belly" 27, "womb" 6 (+ "bowels" 1 for *uterus*); every "womb" is the maternal sense (`c3-v3-12` John 3:4 ×2, `c6-v53-59`, `c7-v1-13`, `c7-v40-53` ×2). (51) was local, as its builder read it |
| (54) | ¶ 62 *misit … misit* one verb ("put … put forth") | ratify |
| (55b) | *doctrinaliter* "teachingly" (verified ¶ 66), *census* "wealth", *definitio*, *honestas* | ratify |
| (59) | Ps. 35:10 → "in thy lumen we shall see lumen" (`c8-v12-20`) vs "in thy light we shall see light" (`c4-v1-6`) — verified both | **ratify as built**: the test decides by passage (Sap ruling 61); the Vol V standing exemption yields where the exposition adduces the verse for *lumen* |
| (62-renderings) | *tenebrositas* "darkness"; *obliquari*; *gazophylacium*; 8:20 Douay; Jer. 23:24 to the print | ratify |
| (64) | *principium* "beginning" (Trinitarian); *verax* "true"; *derelictio* "forsaking"; *explicatio*; 8:24/28 "that I am" | ratify |
| (70) | *servus/servitus/servire/servilis* one root, Douay adjusted (8:33, II Pet. 2:19, Rom. 8:15, Deut. 6); *famulatus* "service"; Rom. 8:21; Heb. 4:12 "efficacious"; III Reg. 1:21; Job 27:19; Prov. 30:5; **[S]ermo** restored (ruling 85) | ratify |
| (71-faces) | Gal. 4:30 in both faces in one chunk (expositio roman-in-guillemets, Quaestio italic) | record (with (45)): the italic convention is by passage function, so one verse can take both faces — this is ruling 9's convention working, not a defect |
| (76) | Douay adjusted for one root: Eph. 5:1, Jer. 2:20, Exod. 23:7, John 8:46 | ratify |
| (77) | *convicium/contumelia/improperium/vituperium* kept apart; *clarificare*/*glorificare* both "glorify" | ratify (cost banked) |
| (82) | Eccle. 8:5 "keepeth the precept shall experience no evil"; 8:51 *gustabit* "taste"; *iudicium discretionis*; *impugnatio*; ¶ 76 stray *»;,* | ratify |

**⭐ Mine: ratify the block (0 lines); conform *eruditio* (5 lines, per-site); N3 ratify; N4 optional.** A rule worth writing
down from (16)/(29)/(46)/(49)/(51)/(54)/(64)/(70)/(76)/(82): *the Douay is adjusted to Bonaventure's word where the exposition or a
Quaestio leans on that word; where nothing leans, the Douay stands* — twelve applications, all disclosed, none contradicted.

---

## 7. RESOLVER DOCKET (ruling 82(a): no text edit; a follow-up TOOL job, dangerous classes first)

Every item checked against `index/citations.tsv` (in scope: **1,474 records** — scripture 1,268 (A 658 · B 357 · C 253), crossref 204
(chunk 157 · page-multi 22 · unresolvable 16 · articulus 5 · work 4), authority 2). **All 18 CONFIRMED as described.**

| class | sites (verified ledger rows) | kind |
|---|---|---|
| **D1 ⚠ cross-note anaphora: `ibid.`/`loc. cit.` bound to a neighbouring note's last locus — SCRIPTURE at A, or a wrong `chunk` that looks resolved** | (14) p. 324 n. 5 → `1Cor 13:12` A · (24) p. 329 n. 11 → `Matth 13:55` A · (34) p. 338 n. 7 → `Ioan 13:21` A · (61) p. 360 n. 9 → `Deut 19:15` A, p. 357 n. 9 → `Prov 27:2` B · (75) p. 368 n. 5 → `Ezech 16:3` A · (81) p. 371 n. 11 → `1Petr 2:23` A, p. 372 n. 5 → `Deut 6:4` A · (13) p. 322 n. 6 → `bon-sent-II-d34-a1-q1` chunk · (66) p. 362 n. 11 ×2 → `bon-brev-p1-c6` chunk · (75) p. 368 n. 8 → `bon-brev-p2-c7+c8` page-multi | **tool, FIRST** — 12 records, 7 of them at confidence A |
| **D2 ⚠ *primae/secundae Ioannis* read as the GOSPEL** (the body-ordinal parser drops the epistle numeral) | (31) ¶ 86 → `Ioan 4:16` B · (44) ¶ 22 → `Ioan 2:4` B · (62) ¶ 24 → `Ioan 5:7` B, ¶ 25 → `Ioan 2` C · (75) ¶ 61 → `Ioan 4:6` B, ¶ 64 → `Ioan 3` C · (81) ¶ 79 → `Ioan 2:4` B | **tool, FIRST** — 7 records, wrong book |
| D3 body anaphor across a heading | (48) ¶ 44 *sicut ibidem dicitur* → `Cor* 1` C (John 9:29 meant) · (47) ¶ 30 *ibidem* → `Gen 17:10` B (17:12 meant; the note's `ibid. v. 12` is right) | tool |
| D4 roman book numeral before *Paralip.* unemitted (82(a)'s class) | (55) p. 353 n. 4 `II. Paralip. 19, 6. seq.`, `19, 7` · (66) `II. Paralip. 12, 5`, `12, 1`, `I. Paralip. 28, 9` · (55) p. 352 n. 13 bare `22, 18` · (66) body *secundi Paralipomenon* → `Par* 12` C · (36) *secundae ad Corinthios* → `Cor*` 3:6 B | tool |
| D5 table / form gaps | (4) `Tom. V. pag. 54. 55.` → `bon-eccl-c7-v1` (wrong `chunk`; capital `Tom.` not read as a tome — ⚠ dangerous, put with D1) · (9) `Iud.` → Jude → `Iudae 7:13` chapter-out-of-range (the **one** QA flag in scope) · (6) point-less `pag 835` dropped · (36) `Ioan. 11. 27.` → chapter only | tool |
| D6 coordinate `ibid. v. N` / `ibid. C, V` (ruling 57 C1) | **15 unresolved-anaphora QA lines in scope** (all also in the 99 "coordinate ibid. left unresolvable"): `c2-v12-17` p273-4 · `c3-v22-26` p285-1 · `c5-v1-9` p306-6 · `c5-v19-23` p309-1, p309-6 · `c5-v31-39` p314-9 · `c5-v40-47` p317-5 · `c6-v1-9` p318-12 · `c6-v22-33` p325-14 · `c6-v34-40` p328-2 · `c7-v1-13` p340-8 · `c8-v21-30` p360-12, p361-1, p361-9 · `c8-v31-36` p363-3 | tool (not in the 210) |
| (18) | `infra n. 39` — ruling 73's `paragraphs:` job | tool (anticipated) |

**⭐ Mine: record all of it on the ruling-82 docket; run D1 + (4) and D2 first** — 20 records that file a wrong target with a
confident face. None is a text edit. The QA-flag count attributable to this scope is **1** (of 210).

---

## 8. DOCUMENTATION

| # | item | evidence | recommendation |
|---|---|---|---|
| (79) | `c8-v37-50` gives p. 369 n. 9 as `supra n. 47.` | its Notes lines 439 and 492 (hand-off); `c8-v51-59` built `n. 17.` (plate, raw, target); the resume blocks record it | correct the two Notes lines at the close (doc only) or leave; no live-region text carries `47` |
| — | claimed entry counts | every chunk's `transcription_status`/Notes count matches its file (40/40; `c8-v12-20` "39" = 38 numbered + `[p357-nota]`) | nothing owed — the shakedown's 45/46 class did not recur |

---

**Plates:** p. 302 ¶ 84 read here (one 1.0× crop); all 41 seams and 104 register leaves were read by the Pass 3 sweep (see the passes file) — CLEAN. (17)'s glyph was
not re-read. Quotations above are from the built files.
