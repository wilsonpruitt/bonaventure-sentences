# Vol VI *Collationes in Evangelium S. Ioannis* SHAKEDOWN GATE (p. 559, ruling 123): EVIDENCE SHEET

**STATUS: CLOSED 2026-11-06 — Wilson ruled "Approve all"; applied and recorded as rulings 124–135 (`manual-review/vol6-pilot-setup.md`); closed gate record `manual-review/vol6-cioan-shakedown-gate.md`.** (Original status: OPEN — awaiting Wilson's ruling.) Compiled 2026-11-06 by a read-only agent on Wilson's go. No file under `vol*/` was
edited; no tool, ledger, registry or resume note was touched; nothing committed, pushed, deployed or stashed; no plate deleted
(the plates pp. 533–560 were already on disk at 450 dpi and were cropped into the scratchpad only).

**Scope: `bon-cioan-c1` … `bon-cioan-c4`, pp. 535–559** (p. 560 only as c4's END leaf). **202 numbered apparatus entries**
(c1 80 · c2 45 · c3 36 · c4 41) **+ 6 `tr-` notes** (`tr-lumen` c1, c3, c4 · `tr-doctrina` c1, c3 · `tr-vacare` c4).

⛔ **Every census is over the RENDERED regions only** (`## Latin`, `## English`, `## Apparatus` with its `**La.**`/`**En.**` halves;
frontmatter and `## Notes` excluded). La/En paragraph parity holds in all four chunks (85/85 · 47/47 · 43/43 · 60/60), so body
sites were read paragraph against aligned paragraph, apparatus sites entry by entry. **Plates read** (crops of the on-disk 450 dpi
leaves): p. 537 n. 6 · p. 543 n. 4 and the Horace line · p. 545 n. 6 · p. 548 n. 6 · p. 551 n. 5 · p. 556 n. 1 · p. 559 R (Annot. 15, 16).

**Carried statements REFUTED or corrected as worded:**
- S8: "c1 rendered quoted *lumen* 'lumen' … per ruling 2 **as applied in *Ioannem***" (c1 Notes L810) — **refuted**: *Ioannem* applied
  the verse test and gave the Douay "light" at **both** of c1's exempt verses, Eph. 5:13 (`bon-ioan-c3-v17-21`, `c16-v5-15`) and
  Tob. 5:12 (`bon-ioan-c2-v1-11`). And Isa. 60:1 is **not** a verse-test failure: the prose leans on it (§ S8).
- S8: c2's "no `tr-lumen` … the site is apparatus, not body" (c2 Notes L468) — **contrary to practice**: three chunks with an
  apparatus-only *lumen* carry the note (`bon-ioan-c5-v31-39`, `bon-ioan-c7-v1-13`, `bon-sap-c16`; ruling 92 "`tr-lumen` in an
  `**En.**` half is ruling 13 working"). c2 is the only chunk in Vol VI with a live *lumen* and no note.
- S8: c4's `tr-lumen` says the Douay "light" stands "**wherever this Psalm verse is quoted in these volumes**" — **false**: ruling 93
  ((59)) kept Ps. 35:10 → "lumen" in *Ioannem* where the exposition leans on it.
- S2: "matches `Hexaem. coll. N` but not `collat. N`" — true but **not the cause** at p. 541 n. 5: the note prints **`Hexaëm.`**
  (diaeresis), which no works abbrev matches at all, and a `(tom. V.)` stands between it and `collat.`; and the works entry's
  `chunk_pattern` names ids that do not exist (§ S2).
- S4: c1 Notes cite "*culpa* → 'fault' and *reatus* → 'guilt' (**Vol VI ruling 20**)" — ruling 20 is *poenalitas / poena / supplicium*.
  The *culpa* precedent is Sap ruling 63; *reatus* has no ruling (three Vol VI sites, all "guilt").
- **NEW, not on the S-list:** c2–c4 set the ordinal citation **"the Nth chapter of Book"** at **250 sites**, against ruling 98's
  printed form **"Book, the Nth chapter"** (c1 152/0; *Ioannem* 2,035/6). See § N1 — the largest item on this sheet.

---

## ▶ ONE-SCREEN SUMMARY

| item | finding | recommendation (mine) | edits if adopted | kind |
|---|---|---|---|---|
| **S8** *lumen* in quotations | 9 sites; **c1 Eph. 5:13 and Tob. 5:12 fail the verse test as built** (both are verses nothing leans on; *Ioannem* gave "light" at both); c1's marker is not at its first site; **c2 lacks `tr-lumen`**; c4's note overclaims | **Conform c1 to the test** (2 → "light"); move c1's marker to ¶ 2; write c2's note; fix c4's sentence | 3 English lines + 1 marker line (c2) + 1 new note + 2 note rewrites + 2 Notes records | per-site |
| **S1/S7/S9** slips | all four **confirmed on the plate**; Ps. 75:3, AP 343, Ovid *Met.* 1.415, Luke 16:19 | **PRINTED_SLIPS: 2 rows** (Ps. 75:2, Luc. 16:10 — the only two that move a ledger record), queued with ruling 113's owed rows · Horace bracket ratified · c4's bracket conformed to ruling 89's shape · ⚖ Silius | 1 line (c4) (+1 if ⚖ Silius bracketed) · 2 tool rows | per-site / ⚖ |
| **S2** resolver | `collat\.` alone ADDS **0**, refines 1; the real gap is **`Hexaëm.` + `collat. N`: 83 sites (Vol V 72, Vol VI 11) with no record**; ⚠ `chunk_pattern` `bon-hex-coll{coll}` ≠ on-disk `bon-hex-cN` | Queue as a tool job **with the pattern fix in the same diff** (otherwise 84 false `forward`s) | 0 text · tool job | tool |
| **S3** breadcrumb | every branch renders Arabic (`Cap. 3, Vers. 1-19`, `Coll. 5`, itin `Cap. 2`) | **Keep `Cap. 1`** | 0 | ratify |
| **S4** register | *culpa* → fault 26/26 · *reatus* → guilt 1/1 · Coll. V *manere* → "remain" with Douay adjusted (I John 4:16, John 14:16–17, **and Luke 24:29, undisclosed**) — matches *Ioannem* at the same verse (John 1:33, `c1-v31-34`) | **Ratify**; correct c1's Notes attribution + disclose Luke 24:29 | 0 text · 1 Notes line | ratify |
| **S5** printed `[?]` | confirmed on the plate (p. 545 n. 6); first editors' bare `[?]` in the corpus (precedent for editors' queries: Sap c4 `[et?]`, c3 here `[*esse ?*]`) | **Keep as printed; teach the checker an allowlist** (`PRINTED_QUERIES`, keyed chunk + label), reported on its own line | 0 text · tool job | tool |
| **S6** verse in a note | p. 548 n. 6 six centred lines → ` / ` | **Ratify** (ruling 91, item (19)); **plus** c1's Horace body line lacks the `> ` that c3's Ovid line and Sap c11's Boethius carry — conform | 2 lines (c1) | ratify / per-site |
| **S10** Coll. XVI `(Cap. VI, 27.)` | address as printed, n. 8 explains it, no capitulum break on the plate; `annotat. 22` → `forward` | **No convention**; record-only; c6 to note the pairing when built | 0 | record |
| **S11** *vacare* / *quies* | note meets the dikaisune rule's text point by point; one note per chunk = ruling 111 | **Ratify** | 0 | ratify |
| **S12** guillemets / faces | both `»` absent on the plate (p. 559 R); roman/italic split recorded | **Record-only** (ruling 9 + COLLECTION CHANGE; Vol V `bon-praec-c4` p. 520 n. 3 precedent) | 0 | record |
| **Register census** | *poena* 11/11 · *magister* 2/2 · *dilectio* 2/2 · *caritas* 17/17 · *signum* 16/16 · *Item* 13/13 · *doctrina* 5/5 + notes 2/2 · *collatio/annotatio* all · **1 bare ordinal** (c1 ¶ 5 "and the sixtieth") | Conform the one bare ordinal | 1 line (same line as S8's marker) | per-site |
| ⭐ **N1** ordinal word order | **c2–c4: "the Nth chapter of Book" ×250 on 80 lines** vs ruling 98's "Book, the Nth chapter" (c1 ×152, *Ioannem* ×2,035) | ⚖ **Conform c2–c4 to ruling 98's form** (Appendix A; 246 mechanical + 4 by hand) | 80 lines | ⚖ DECISION, mechanical |

**If every recommendation is taken: ~87 English lines (80 of them N1), 0 `## Latin` lines except c1's one Horace blockquote line, 0
`**La.**` halves; 1 new `tr-` note (c2) + 2 rewritten (c1, c4); ~4 `## Notes` record lines; and three tool jobs queued, not run
(PRINTED_SLIPS +2 rows, the Hexaemeron resolver job, the printed-query allowlist).**

⚠ **Real decisions for Wilson:** **N1** (does ruling 98 fix the word order, or only the noun?), **S7** (does an editors'
misattribution take a bracket?), and S8's marker placement (letter of ruling 74 vs. the note reading best at ¶ 5). Everything else
is a conformance to a rule already made, a record, or a tool job.

---

## S8. *LUMEN* INSIDE SCRIPTURE QUOTATIONS — THE REAL INCONSISTENCY

**The rule, verbatim.** CLAUDE.md § Vol V ruling 2 (the *mysterio Trinitatis* shakedown gate, Wilson 2026-09-06): ***"a received
scriptural wording is exempt only where the verse is quoted AS A VERSE and no surrounding body prose leans on the term."***
Ratified for Vol VI as **ruling 46** (Sap: Job 37:3, Col. 1:12, Isa. 50:11 keep "light") and **ruling 61** ("decides by passage, not
by verse": Job 24:13 "light" at c14, "lumen" at c17), carried by **ruling 74** ("the verse test at every scriptural site"; the
Vulgate-lemma exemption, alt (c), REFUSED) and **ruling 93** ("the Douay is adjusted to Bonaventure's word where the exposition … leans
on that word; where nothing leans, the Douay stands"; Ps. 35:10 → "lumen" where leaned on), and **ruling 121** for this work.

**Census, c1–c4, `lumen/lumin-` (Latin body + `**La.**` halves): 9 sites in 6 units.** (*illuminare / illuminat* are not *lumen*
sites; *luminaria*-type words do not occur.)

| # | chunk · place | Latin | English as built | class | test result | consistent? |
|---|---|---|---|---|---|---|
| 1 | c1 Coll. I ¶ 2 (E237) | Eph. 5:13 « Omnia enim, quae arguuntur, **a lumine** manifestantur » | "made manifest **by the lumen**" | verse adduced for ***arguit malos***; prose turns on *lux arguens* and *arguere* | **exempt → Douay "by the light"** | ❌ |
| 2 | c1 Coll. I ¶ 5 (E249) | *triplicem lucem sive **lumen**: **lumen** scientiae* | "a threefold light or lumen: the lumen of knowledge" | body prose | rule | ✓ |
| 3 | c1 Coll. I ¶ 5 | ***Lumen** gratiae* … Isa. 60:1 « Surge, illuminare … quia venit **lumen** tuum » | "The lumen of grace … for thy lumen is come" | Isa. 60:1 is the proof-text of the prose's own *Lumen gratiae* — **the prose leans** | rule (not exempt) | ✓ |
| 4 | c1 Coll. I ¶ 5 | ***Lumen** laetitiae spiritualis;* Ps. 4:7 « Signatum est super nos **lumen** vultus tui » | "The lumen of spiritual gladness … The lumen of thy countenance" | leaned on; and Ps. 4:7 is ruled "lumen" (ruling 121) | rule | ✓ |
| 5 | c1 Coll. I ¶ 7 (E257) | Tob. 5:12 « … in tenebris sedeo et **lumen** caeli non video » | "see not **the lumen** of heaven" | verse adduced for ***tenebrae miseriae***; prose turns on *tenebrae* | **exempt → Douay "the light of heaven"** | ❌ |
| 6 | c1 Annot. 2 (E400) | John 1:7 *ut testimonium perhiberet de **lumine*** (*habetur hic*, italic lemma text) | "to give testimony of the lumen" | the chapter's own Gospel text | ruling 74: the test fails at John 1:7–8 by its own terms; alt (c) refused; *Ioannem* `c1-v6-8`, `c1-v19-23` "lumen" | ✓ |
| 7 | c2 p. 549 n. 1 (L371) | Bede, *quasi suscepto **lumine** solis* | "the lumen of the sun" | not Scripture | rule | ✓ (but **no `tr-lumen`**) |
| 8 | c3 Annot. 10 (E211) | Job 24:13 « Ipsi fuerunt rebelles **lumini** » | "rebellious to the light[^tr-lumen]" | verse for the lemma's *lux*; prose turns on *lux* (*lucem odiunt … Odit piger lucem*) | exempt | ✓ (`bon-ioan-c3-v17-21` precedent; Sap ruling 61) |
| 9 | c4 Coll. XIV ¶ 2 (E173) | Ps. 35:10 « … in **lumine** tuo videbimus **lumen** » | "in thy light we shall see light[^tr-lumen]" | adduced for *fons vitae*; *lux* absent from c4 (0 body, 0 apparatus) | exempt | ✓ |
| (10) | c4 p. 555 n. 3 | variant *A **lumen*** | "A has *lumen* (lumen)" | a cited variant (gloss of a mentioned word) | n/a | ✓ |

**The decisive sentences.**
- Site 1: *Est autem secundum quod homo lux **arguens** … — **Arguit malos;** ad Ephesios quinto: « Omnia enim, quae arguuntur, a lumine
  manifestantur »; et ideo oditur a malis; Ioannis tertio: « Omnis, qui male agit, odit lucem ».* / "*He reproves the wicked;* to the
  Ephesians, the fifth chapter: « For all things that are reproved are made manifest by the lumen »; and therefore he is hated by the
  wicked; John, the third chapter: « Every one that doth evil hateth the light »." — the proof is for *arguit*; the noun the prose uses
  is *lux*. *Ioannem* `c16-v5-15`'s note, same verse: "adduced … for what *arguere* means … so the Douay's 'light' stands."
- Site 5: *De tenebris miseriae, Tobiae quinto: « Quale gaudium mihi erit, qui in tenebris sedeo et lumen caeli non video »?* / "Of the
  *darkness of misery*, Tobias, the fifth chapter: « What manner of joy shall be to me, who sit in darkness, and see not the lumen of
  heaven »?" — *Ioannem* `c2-v1-11`'s note, same verse: "adduced … for the defects of knowledge … the exposition turns on those words,
  not on *lumen*. So the Douay's 'light' stands."
- Site 3 (for contrast): *Lumen **gratiae**; Isaiae … et sexagesimo: « Surge, illuminare, Ierusalem, quia venit lumen tuum »* — the
  verse proves the prose's own *lumen gratiae*; "light" here would make "the lumen of grace" prove itself by "thy light is come".

**What the builder did.** c1's Notes (L810) apply the test to none of the four quotation sites, saying "per ruling 2 as applied in
*Ioannem* they take 'lumen'". The *Ioannem* record is the opposite at both exempt verses. c3 (Job 24:13) and c4 (Ps. 35:10)
applied the test correctly, so **the work is inconsistent with itself between c1 and c3/c4.**

**`tr-lumen` per chunk (ruling 74: "at the first site of each chunk").** c1: present, but anchored at site 2 (¶ 5), **not at the first
site** (¶ 2, Eph. 5:13). c2: **absent** with a live site (row 7). c3: at its one site ✓. c4: at its first site ✓ (the body precedes the
apparatus variant). Vol VI census of chunks with a live *lumen* and no note: **c2 only** (`bon-eccl-c1-v2-7`, `bon-ioan-c1-v1-2`,
`bon-sap-c8` have only *luminaria / luminosior*, other words).

**Alternatives.**
- **(a) Conform c1 to the test** — Eph. 5:13 and Tob. 5:12 → Douay "light". Cost: 2 English lines; c1's `tr-lumen` text must name the
  exception, as c3's and c4's do.
- (b) Keep c1 as built and ratify "lumen" at all quoted sites for this work. Cost: departs from rulings 46/61/74/93 and from *Ioannem*'s
  decision at the same two verses; makes c3/c4 the inconsistency (2 conforms the other way plus two notes).
- (c) Record only. Cost: the work reads "lumen" in Eph. 5:13 in Cap. I and "light" in the same kind of verse in Caps. III–IV.

**▶ RECOMMENDATION: (a).** Plus: move c1's marker to its first site (¶ 2); write c2's note; correct c4's overclaim.
⚖ *Marker alternative:* keep c1's marker at ¶ 5, where the note's "Latin has two words here" reads best. Cost: the letter of ruling 74
("first site"), which *Ioannem* `c2-v1-11` followed by anchoring at an exempt verse.

**Exact edit list if adopted (English only, no Latin touched):**
1. `bon-cioan-c1` L237: `are made manifest by the lumen »;` → `are made manifest by the light »[^tr-lumen];`
2. `bon-cioan-c1` L249: `a threefold light or lumen[^tr-lumen]:` → `a threefold light or lumen:` (marker moved; same line also takes the N0 ordinal edit below)
3. `bon-cioan-c1` L257: `and see not the lumen of heaven »?` → `and see not the light of heaven »?`
4. `bon-cioan-c1` L752 `[^tr-lumen]` rewritten, proposed text: "**En.** Translator's note: Latin has two words for light where English has one. *Lux* is light in its source — the lemma of the first collation, *Lux in tenebris lucet*, and Christ who « est lux vera » — while *lumen* is light as it is sent forth and received. The fifth paragraph of this collation puts the two side by side in one phrase: Christ *emittit interius triplicem lucem sive lumen: lumen scientiae… lumen gratiae… lumen laetitiae spiritualis*, and its proof-texts for the second and third members are Isa. 60:1, *venit lumen tuum*, and Ps. 4:7, *Signatum est super nos lumen vultus tui*. Collapsing the words would leave Bonaventure saying that light sends forth "a threefold light or light". *Lux* is therefore "light" throughout and *lumen* is left standing, those two verses included. The exception is a verse quoted only as a verse, where no surrounding prose leans on the word: here Eph. 5:13, *a lumine manifestantur*, adduced for what *arguere* does, and, in the seventh paragraph, Tob. 5:12, *lumen caeli non video*, adduced for the darkness of misery. Both keep the Douay's "light"."
5. `bon-cioan-c2` L371 (p. 549 n. 1 `**En.**`): `as though having received the lumen of the sun,` → `as though having received the lumen[^tr-lumen] of the sun,`
6. `bon-cioan-c2`: new note after `[^p550-4]` (after L424), last in `## Apparatus`: "[^tr-lumen]: **En.** Translator's note: this translation keeps *lux* as "light" and *lumen* as "lumen", except where a verse is quoted as a verse and no surrounding prose leans on the word. This chapter's one *lumen* is not Scripture but Bede's prose in the note on the temple's windows (p. 549, n. 1), *quasi suscepto lumine solis*, so it stays "the lumen of the sun"; the chapter's one *lux*, in the tenth collation, is "light"."
7. `bon-cioan-c4` L461, last sentence: `…the received wording "in thy light we shall see light" therefore stands, as it does wherever this Psalm verse is quoted in these volumes.` → `…the received wording "in thy light we shall see light" therefore stands, as it does wherever this verse is quoted only as a verse.`
8. Notes records: c1 L810 (the four quotation sites: test applied, Eph. 5:13 / Tob. 5:12 "light", Isa. 60:1 / Ps. 4:7 leaned on, John 1:7 ruling 74); c2 L468 ("no `tr-lumen`" superseded).

---

## S1 / S7 / S9. THE QUARACCHI SLIPS

**All four confirmed on the 450 dpi plate.**

| item | chunk · note | plate reads | source | English as built |
|---|---|---|---|---|
| S1a | c1 p. 537 n. 6 | `Ps. 75, 2` ✓ | body quotes *In pace factus est locus eius, et habitatio eius in Sion* = **Ps. 75:3** (75:2 is *Notus in Iudaea Deus*) | "Ps. 75:2 [so printed; the verse is Ps. 75:3]" |
| S1b | c1 p. 543 n. 4 | `v. 243.` ✓ | body line *Omne tulit punctum qui miscuit utile dulci* = Horace, ***Ars poetica* 343** | "v. 243 [so printed; the line is v. 343]" |
| S7 | c3 p. 551 n. 5 | `Silii Italici … lib. XV. 128.` ✓ (128 at the head of the next line) | *Et documenta damus, qua simus origine nati* = **Ovid, *Met.* 1.415** (with 1.414 *Inde genus durum sumus experiensque laborum*). No Silius text is on disk; I know of no such line in *Punica* XV, but did not verify a negative | as printed, unbracketed |
| S9 | c4 p. 556 n. 1 | `Luc. 16, 10. seqq.` ✓ | body: *Exemplum de divite epulone, Lucae decimo sexto*; the parable opens at **Luke 16:19** (16:10 is *Qui fidelis est in minimo*) | "Luke 16:10 ff. [so printed; the rich glutton's parable opens at Luke 16:19]" |

**`PRINTED_SLIPS`** (`tools/build-citations.py` L897; rule in its comment: "Add a row only for a slip a chunk's Notes have recorded and
a gate has ruled on"; keyed (chunk, section, anchor, filed target) → exactly one record). Ledger, measured:
- `bon-cioan-c1 · apparatus:p537-6 · p537-6 · Ps 75:2` — **one record, filed as printed** → qualifies.
- `bon-cioan-c4 · apparatus:p556-1 · p556-1 · Luc 16:10` — **one record** → qualifies.
- Horace and Silius: **no ledger record** (non-Scripture, no works entry) → record-only; a row would match 0 records and be reported stale.

The table today holds only the six *Sapientiae* rows; *Ioannem*'s five owed citation rows (ruling 113) are **queued, not added**.

**English bracket practice.** Ruling 89 (shapes): `[so printed: X for Y]` (letter), `[so printed; the verse/passage is …]` (locus),
`[*so printed*]` (name); ruling 100 added "[so printed; the note is …]"; ruling 108 applied them (e.g. "[so printed; the verse is
I Cor. 15:53]", "[so printed; the verses are Acts 4:3 and 5:18]"). Corpus census of the locus shape's noun: *verse* 32 · *passage* 15 ·
*note* 6 · *question* 2 · *line* 2 (both c1, the bracket and its Note). c4's "the rich glutton's parable opens at …" is the one bracket
in the corpus outside the shapes.

**Alternatives and costs.**
- PRINTED_SLIPS: (a) queue the 2 rows with ruling 113's owed rows (one tool diff, ledger diff reviewed) — cost 0 now; (b) add now — a
  tool edit outside a gate-run job; (c) none — the two records stay silently filed at the wrong verse.
- Horace: (a) ratify "the line is" as a shape of ruling 89's second, as ruling 100 did "the note is" — 0 lines; (b) conform to "the
  verse is v. 343" — 1 line, and "verse" is ambiguous beside Scripture verses.
- Luke: (a) conform to "[so printed; the passage is Luke 16:19 ff.]" — 1 line; (b) ratify the free form — a sixth shape.
- ⚖ **Silius (S7):** (a) record-only, as built — the bracket class is for a certain *printed* slip (sort, locus, name), and an
  attribution is an editorial judgement, not a printing error; 0 lines. (b) bracket "[so printed; the line is Ovid, *Metamorphoses*
  1.415]" — 1 line; extends ruling 89's class from locus to attribution, a new precedent for every later editors' misattribution.

**▶ RECOMMENDATION:** PRINTED_SLIPS (a), 2 rows: `("bon-cioan-c1", "apparatus:p537-6", "p537-6", "Ps 75:2", "Ps 75:3", "gate p. 559 — p. 537 n. 6 prints `Ps. 75, 2`")` and `("bon-cioan-c4", "apparatus:p556-1", "p556-1", "Luc 16:10", "Luc 16:19", "gate p. 559 — p. 556 n. 1 prints `Luc. 16, 10. seqq.`")`. Horace (a). Luke (a). Silius ⚖ — mine (a), record-only.

**Edit list:** `bon-cioan-c4` L335: `Luke 16:10 ff. [so printed; the rich glutton's parable opens at Luke 16:19] is adduced.` → `Luke 16:10 ff. [so printed; the passage is Luke 16:19 ff.] is adduced.` (c4 Notes L489/L539 follow). If Silius (b): `bon-cioan-c3` p. 551 n. 5 `**En.**` after "book XV, 128" insert ` [so printed; the line is Ovid, *Metamorphoses* 1.415]`.

---

## S2. THE RESOLVER GAP — `collat. N` AFTER ANOTHER WORK'S NAME (count only)

**How `scan_work` behaves** (`build-citations.py` L656): for each works entry abbrev it matches `abbrev` + optional `p. N` +
optional `(c|coll|q)\. N`. **`collat.` is not `coll.`** (the regex needs a point after `coll`), so `Hexaem. collat. 23` yields a
**work-level** record (`work:hexaemeron`). **`Hexaëm.` (diaeresis) matches no abbrev at all** (`Hexaem.`, `Hexaemer.`, `Collat. in
Hexaem.` are all ASCII), so it yields **nothing**. p. 541 n. 5 is `in Hexaëm. (tom. V.) collat. 1.` — diaeresis + an interposed
parenthesis; that, not `collat.`, is why it has no record.

**Census, `**La.**` halves of every `vol*/` apparatus (Latin bodies: 0 such sites):**

| form | sites | records today | a `collat\.` keyword alone | `collat\.` + `Hexa[eë]m` + `(tom. V.)` tolerance |
|---|---|---|---|---|
| `Hexaem. collat. N` (ASCII) | **1** (`bon-serm-s3` p. 555 n. 9) | 1 work-level | refines 1, **adds 0** | refines 1 |
| `Hexaëm. collat. N` / `Collat. in Hexaëm. collat. N` | **80** (Vol V 72 · Vol VI 8) | 0 | 0 | **adds 80** |
| `Hexaëm. (tom. V.) collat. N` | **3** (Vol VI `bon-cioan-c1` p. 541 n. 5, `bon-ioan-c1-v24-28` p. 259 n. 12, `bon-ioan-c6-v22-33` p. 325 n. 15) | 0 | 0 | **adds 3** |
| **total** | **84** | 1 | **+0 / ~1** | **+83 / ~1** |

Vol VI's 11: `bon-cioan-c1` p. 541 n. 5 · `bon-ioan-c1-v24-28` p. 259 n. 12 · `c1-v3-5` p. 249 n. 6 · `c14-v25-31` p. 445 n. 1 ·
`c6-v22-33` p. 325 n. 15 · `c6-v34-40` p. 328 n. 1 · `c6-v41-52` p. 331 n. 6 · `c9-v1-11` p. 373 n. 12 · `bon-sap-c6` p. 149 n. 1 ·
`bon-sap-c7` p. 155 n. 7 · `bon-sap-prooem` p. 108 n. 4.

⚠⚠ **A trap the job must close in the same diff:** the `hexaemeron` works entry's `chunk_pattern` is **`bon-hex-coll{coll}`**, but the
Hexaemeron's chunks are **`bon-hex-c1` … `bon-hex-c23`** (frontmatter `collatio: N` = the number). `resolve_work` returns `forward` for
any constructed id not on disk, so all 84 would land as **false `forward`s into a closed volume** — a confident wrong answer. The
pattern has never fired (all 39 existing Hexaemeron work records are cap-less), which is why it was never noticed.

⚠ **Do not add a bare `Hexaëm.` abbrev:** 123 `Hexaëm` sites in all, ~40 of them without `collat.`, many of them Ambrose's, Basil's or
Bede's *Hexaemeron* (`Ambros., I. Hexaëm. c. 10`, `Beda, *Hexaëm.* ad v. 6`). Key the extension on `Hexa[eë]m\w*\.\s*(\(tom\. V\.\)\s*)?collat\.\s*N`.

**Related, out of scope, counted:** bare `collat. N` inside a collationes work refers to that work's own units — `bon-hex` 70,
`bon-praec` 19, `bon-don` 3 — the ruling-116 problem for the Vol V works (a scoped scanner per work, not this extension). The
ruling-116 guard (`Hexaem\w*` before `collat.`) also misses `Hexaëm` and a `(tom. V.)` interposition; latent only — the raw text of
pp. 560–634 has no Hexaemeron reference and every `Collat. N` there is this work's own.

**▶ RECOMMENDATION:** queue as a resolver job beside D1–D6 (rulings 94/103/113): the keyed extension + `chunk_pattern` → `bon-hex-c{coll}`
+ the guard widened to `Hexa[eë]m`, with a before/after ledger diff for Wilson (expected **+83 records, 1 refined**). No text edit. 0 lines.

---

## S3. BREADCRUMB `Cap. 1` vs `Cap. I`

`site/scripts/build-content.mjs` `buildWorkChunkTitle`: `collationes-ioannem` → `` `Cap. ${meta.division}` `` (Arabic). Every sibling branch
is Arabic too: `ecclesiasten` / `sapientiam` / `ioannem` → `Cap. N, Vers. a-b`; `itinerarium` → `Cap. N`; the collationes works →
`Coll. N`; quaestiones → `Quaest. N`; Breviloquium → `Pars N, Cap. N`. Roman appears only in the registry's *division titles*
(`Capitulum I: In principio erat Verbum`), as in every work.

**Alternatives:** (a) keep Arabic — 0 lines, consistent with all works; (b) Roman for this work — 1 code line, the only Roman
breadcrumb on the site. **▶ RECOMMENDATION: (a).** ⓘ Banked for later: division 19 (the joint XVIII–XIX unit) will render "Cap. 19"
and division 22 "Cap. 22" under this branch — the code comment already defers both to when they land.

---

## S4. REGISTER ADDITIONS: *culpa*, *reatus*, Coll. V *manere*

| term | sites (c1–c4) | English | precedent |
|---|---|---|---|
| *culpa* | **26** (c1 3 · c2 7 · c3 5 · c4 11) | "fault" 26/26 | Sap ruling 63 (*de merito culpae* → "on the merit of fault") |
| *reatus* | **1** (c1 Coll. VI ¶ 4 *maculam, reatum et offensam … Reatus ad poenam intolerabilem obligat*) | "guilt" | no ruling; Vol VI's 3 other sites all "guilt" |
| *manere* family | **28** (c1 22 · c3 1 · c4 5) | see below | — |

**Coll. V *manere*.** The collation's frame is *Spiritum descendentem et manentem* (John 1:33) and its proofs of *manet* — *Manet autem
Deus non ubique … Qui manet in caritate in Deo manet* / "Now God remains not everywhere … He that remaineth in charity remaineth in God".
English "remain" throughout, the Douay adjusted at **I John 4:16** ("abideth" → "remaineth"), **John 14:16–17** ("abide with you" →
"remain with you") **and Luke 24:29** ("Stay with us" → "Remain with us", *Mane nobiscum*) — the last **not disclosed** in c1's Notes.
This is ruling 93's rule in fact (the prose leans on the word). *Ioannem* at the same verse (`bon-ioan-c1-v31-34`) has *manentem* →
"remaining" ×7. Elsewhere c1 keeps the Douay where nothing leans: Coll. II ¶ 6 John 15:4 « Abide in me » (the prose there turns on
*habitare*, "dwells"; *Ioannem* `c15-v1-11` "abide" throughout John 15), John 12:46 "may not remain" (Douay). *permanet* keeps the
Douay: Ps. 118:89 "standeth firm", John 6:27 "endureth" ×3; Luke 1:80 *manebat in desertis* "was in the deserts". ⓘ One noun split,
inside c1: *mansio* → "abiding" (L134, *stabat in signum mansionis*, the cloud of Num. 9) and → "remaining" ×2 (L162, Coll. V, beside
*manentem*); *Ioannem* `c1-v31-34` has *descensio et mansio* → "the descent and the abiding".

**Alternatives:** (a) ratify as built — 0 text lines; (b) conform Coll. V's two *Mansio* to "abiding" (*Ioannem*'s noun) — 2 lines, and
it breaks the verb–noun echo the collation is built on (*Mansio, cum additur: Et manentem*).
**▶ RECOMMENDATION: (a)**, and correct c1's Notes: "*culpa* → 'fault' (Sap ruling 63) and *reatus* → 'guilt' (Vol VI practice, no
ruling)", and add Luke 24:29 to the adjusted-Douay list. 0 text lines · 1 Notes line (L761).

---

## S5. THE EDITORS' PRINTED `[?]` (p. 545 n. 6)

**Plate:** p. 545 R, n. 6, line 7: `id est in caelo [?] transmigrationis perpetratae` — the editors' bracket, roman, ✓. Transcribed in
`bon-cioan-c2` p. 545 n. 6 both halves ("in the heaven [?] of a passing-over"). (Context, not for the record: the note is about
*Cana* = *zelus*; the editors seem to query *caelo*.)

**`tools/check-live-flags.py vol6`** now reports **2 occurrences** (c2 L243, L245) — both this one site. Corpus: 241 live `[?]` in
Vols I–IV, **all ours**; **no earlier editors' bare `[?]`**. Editors' queries are otherwise printed with a word and are invisible to the
checker: Sap c4 p. 134 n. 5 `[et?]` ("Not our flag"), c3 here p. 551 n. 3 `[*esse ?*]`, *Ioannem* `c10-v22-42` `[autem ?]`, `c18-v13-23`
`[ubi?]`, etc.

**Alternatives (mechanism suggested, not implemented):**
- **(a) An allowlist in the checker,** `PRINTED_QUERIES = [("vol6/bon-cioan-c2.md", "p545-6", "in caelo [?]"), …]` — skip a `[?]` only
  when the line belongs to that apparatus entry and the context string matches, and print them on their own line ("printed by the
  editors, not ours: 2"). Cost: ~10 tool lines; 0 text; a new printed query cannot be absorbed silently (the context must match).
- (b) Annotate the text, e.g. `[?]<!-- printed -->`. Cost: a comment inside a footnote definition (the build strips only page
  comments, untested here), and the transcription is no longer the print plus markup we already use.
- (c) A typographic variant (`[?]` with a zero-width character, or `[ ? ]`). Cost: invisible/false transcription — refused by ruling 9.
- (d) Rule a rendering (`[*sic, ?*]`). Cost: changes what was printed.

**▶ RECOMMENDATION: keep as printed, (a) as a queued tool job.** 0 text lines.

---

## S6. VERSE INSIDE AN APPARATUS ENTRY (p. 548 n. 6, Sedulius)

**Plate:** six centred lines — *Domus pudici pectoris / Templum repente fit Dei, / Intacta nesciens virum / Virgo creavit filium. /
(in Breviar. Romano: / Concepit alvo filium).* — matched by the transcription line for line, with ` / `.
**Precedent:** ruling 91 (*Ioannem* p. 371 gate § 4) — "(19)'s ` / ` for a verse break inside an entry ratified" (`c6-v22-33` p. 326
n. 10, the Vatican couplet; the evidence sheet's reason: "a hard break inside a footnote def is fragile in the build").
**▶ RECOMMENDATION: ratify. 0 lines.**

**Related, found in the census (verse in the BODY):** the body precedent is a `> ` blockquote line per verse line (`bon-sap-c11` the
Boethius tercet, L143–145 / 273–275; Vol V uses the same form). c3 sets Ovid that way (`> Et documenta damus…`). **c1 sets Horace as a plain
paragraph** (L180 `Omne tulit punctum qui miscuit utile dulci.`, L374 the English) though the plate (p. 543 L) sets it as an indented
verse line. **▶ Conform: c1 L180 and L374 prefixed `> `.** 2 lines.

---

## S10. COLL. XVI `(Cap. VI, 27.)` INSIDE CAPITULUM IV

Built as printed (c4 L67–69): `### Collatio XVI.` / `(Cap. VI, 27.). *Operamini non cibum…*[^p556-8]`; the editors' n. 8 (*S. Bonav. hic
anticipando exponit versum capituli sexti … eam a praecedente etiam numeratione distinximus. Vide infra pag. 567, annotat. 22.*) is in
full both halves; c4's Notes record the plate (no `Cᴀᴘɪᴛᴜʟᴜᴍ` heading on pp. 555–559; running heads `CAP. IV. COLL. XVI.`).
`collationes: [14, 15, 16, 17, 18, 19]` ✓. Ledger: `annotat. 22` → `work:collationes-ioannem:annot22` **forward** ✓, `infra pag. 567` →
`tom6:p567` forward ✓; the address itself is not a citation (lemmas are not indexed, ruling 5).

**Alternatives:** (a) no convention — the address and n. 8 already tell the reader, and the breadcrumb names the chunk (`Cap. 4`), not
the section; 0 lines. (b) a translator's note at the address — 1 note; duplicates n. 8. (c) a breadcrumb/title rule for a section whose
verse is another chapter's — site code for one unit in 79+ sections. **▶ RECOMMENDATION: (a)**, and brief `bon-cioan-c6` to record in its
Notes that Annot. 22 (p. 567) is the pairing named by p. 556 n. 8, and that `annotat. 22` resolves to it on the next ledger build. 0 lines.

---

## S11. *VACARE* (Acts 17:21) AND *QUIES* IN c4

**The rule's text** (CLAUDE.md, ruled 2026-09-15): "*vacatio*/*vacare* falls under the DIKAISUNE RULE … choose the English by context
each time and footnote the word — say what the Latin holds together and which side the English took … no `vaca-` word is ever rendered
'rest'." Ruling 111: one note per chunk carrying the word (*Ioannem* 5/5).

**c4's note against it:** what the Latin holds — "being at leisure, being free, being free *for* something and being free *from*
something" ✓; which side — "what they were free for and gave their time to, so the English keeps the Douay 'employed themselves'" ✓;
never "rest" — "No *vaca-* word is rendered 'rest' … because *quies* and *requies* take that word" ✓; and it names c4's *quies* site
(Coll. XIV ¶ 1 *documentum inveniendi quietem … si delectat quies* → "a lesson in finding rest … if rest delights us") ✓. Census c1–c4:
*vaca-* 1, *quies* 2 (one unit), *requies* 0. The wording follows *Ioannem* `c19-v16-27`'s note almost verbatim.

**▶ RECOMMENDATION: ratify the wording and one note per chunk. 0 lines.**

---

## S12. ABSENT CLOSING GUILLEMETS; ROMAN vs ITALIC JOHN 4

**Plate p. 559 R:** Annot. 15 `Psalmus: « Sitivit anima mea ad Deum fortem, vivum. — Est sitis gloriae` — **no `»`** ✓; Annot. 16
`Genesis decimo quinto⁵: « Noli timere, Abraham, ego protector tuus sum, et merces tua magna nimis. — Merces multa` — **no `»`** ✓. Both
transcribed without, both halves. The face split (John 4:13, 4:36 italic unguillemeted; 4:16, 4:47, 6:27 roman in guillemets in the same
chapter) is banked in c4's Notes (the italic-exceptions list, item 1).

**Rules:** ruling 9 (transcribe as printed, normalise nothing, claim no discriminator); the COLLECTION CHANGE block (italic exceptions
banked, not explained); precedent Vol V `bon-praec-c4` p. 520 n. 3 (a quotation "opened and never closed, and that is the printing") and
Vol IV `d48-littera` (a stray closing guillemet). **Alternatives:** (a) record-only — 0; (b) supply `»` in the English only — splits the
halves and is a silent emendation of punctuation (ruling 108 dropped even a bracket for a missing stop). **▶ RECOMMENDATION: (a). 0 lines.**

---

## REGISTER CENSUS OVER c1–c4 (the carried rulings)

| ruling | Latin sites | English | non-conforming |
|---|---|---|---|
| *poena* → punishment (20/109) | 11 (c1 1 · c2 5 · c3 1 · c4 2 · + *poenalitas* c3 ×2 → "penalty", ruling 20) | "punishment" 9/9 | none |
| *supplicium* → penalty (59) | 0 | — | — |
| *magister* → teacher (74) | 2 (II Tim. 4:3 *magistros* → "teachers"; p. 545 n. 5 *lit. Magistri* → "the Master's text") | ✓ | none |
| *dilectio* → dilection (74/109) | 2 (c2 *zelum dilectionis*, c3 *foedus dilectionis*) | ✓ | none |
| *caritas* → charity | 17 | ✓ | none |
| *signum* → sign (74) | 16 (John 2:23 *Signa* Douay "miracles" adjusted to "signs") | ✓ | none |
| ordinals (98/106) | Latin book-before-ordinal 392 / ordinal-before-book 3 | c1 "the Nth chapter" 152 · c2 78 · c3 84 · c4 92 | **1 bare:** c1 L249 *et sexagesimo* → "and the sixtieth" · **⭐ word order: N1** |
| Psalm ordinal (106) | bare *Psalmus* only | "the Psalm" | none |
| *Item* → Likewise (99/107) | 13 sentence-head (c1 4 · c4 9) + c1 5 mid-sentence *item* | "Likewise" 13/13; "likewise" 5/5 | none |
| *doctrina* + `tr-doctrina` (53/111) | 5 (c1 3 body + p. 536 n. 2 variant · c3 1) | "teaching" 5/5; notes c1 ✓ c3 ✓ (c2, c4 have none) | none |
| *collatio* / *annotatio* (121) | every `###` heading (Coll. I–XIX, Annot. 1–17, the work heading) + 5 prose/apparatus sites | "Collation" / "Annotation" | none |
| *moraliter*, *praedicator*, *tropologicus*, *pietas* (121) | 1 · 1 (+ p. 535 n. 1) · 2 · 1 (+ c4 *pietas medici*) | morally / preacher / tropological / piety | none |
| *lux* → light | c1 34 + 4 · c2 1 · c3 10 · c4 0 | "light" | none |

**Edit (N0):** `bon-cioan-c1` L249 `« Thy light shall rise up in darkness »; and the sixtieth:` → `…; and the sixtieth chapter:` (ruling 98;
the same line as S8 edit 2). 1 line.

---

## ⭐ N1. THE ORDINAL CITATION'S WORD ORDER DRIFTS AT c2 (NEW)

**The rule.** Ruling 98: "*Isaiae vigesimo quarto* → **'Isaias, the twenty-fourth chapter'**"; the CLAUDE.md formula table carries the
same form. Ruling 98's reason for choosing a form at all: "the two forms flip mid-chapter in runs, which a reader sees."

**Census, `## English` body (apparatus `**En.**` halves: 0 of either form):**

| | "Book, the Nth chapter" | "the Nth chapter of/to Book" |
|---|---|---|
| `bon-cioan-c1` | **152** | **0** |
| `bon-cioan-c2` | 3 | **78** |
| `bon-cioan-c3` | 10 | **81** |
| `bon-cioan-c4` | 4 | **91** |
| *Ioannem* (109 chunks) | 2,035 | 6 |
| Ecclesiastes / Sapientia | 577 / 46 | 0 / 0 |

The Latin is uniform in all four chunks (book-then-ordinal 392 : 3), so the flip is the translator's. Its origin is in the Notes: c2
L472, c3, c4 each record "**Ordinals (ruling 98):** 'the Nth chapter of …' at every book-and-chapter locus" — a reading of ruling 98 as
governing the noun, not the order. c1 → c2 is a flip at a chapter boundary, inside one work.

**Decisive sentences (one each):** c1 "Isaias, the fifty-eighth chapter: « Thy light shall rise up in darkness »" · c2 "the sixth chapter
of the first to the Corinthians: « For they shall be, saith he, two in one flesh »" (*primae ad Corinthios sexto*).

**Alternatives.**
- **(a) Conform c2–c4 to "Book, the Nth chapter"** (ruling 98's printed form): **250 sites on 80 lines** (c2 78 / 30 lines · c3 81 / 22 ·
  c4 91 / 28). 246 are a mechanical reorder (`the ORD chapter of X` → `X, the ORD chapter`; `the ORD chapter to the Romans` → `to the
  Romans, the ORD chapter`), dry-run in Appendix A; **4 need a hand** (Appendix A "HAND": c2 L211, c3 L139, c4 L255 "it is said" /
  "concerning" follow the locus, and c4 L215 is sentence-initial "The thirteenth chapter of Proverbs").
- (b) Ratify the inverted form for this work and conform c1 the other way: 152 sites, and a cross-work divergence from *Ioannem*'s
  2,035, the work this one supplements.
- (c) Ratify both as free variation — 0 lines; the flip ruling 98 was made to remove stays, at a capitulum boundary.

**▶ RECOMMENDATION: ⚖ (a)**, run once over c2–c4 now (the work is 4 chunks in; every later chunk inherits whichever form this gate
leaves), and brief `bon-cioan-c5` onward with ruling 98's exact form. It is Wilson's call because it settles what ruling 98 binds.
**Edit list:** Appendix A, all 250 rows; verify after the run that "the Nth chapter of" = 0 in c2–c4 bodies and "Book, the Nth chapter"
rises by 250. Notes: c2/c3/c4 "Ordinals (ruling 98)" lines corrected.

---

## WHAT IS NOT ON THIS SHEET (checked, nothing to report)

`check-live-flags.py vol6` → the 2 S5 occurrences and no others · apparatus counts by the chunks' own Notes 80/45/36/41 (202) and
markers/definitions in order · heading parity (`### Collatio/Annotatio` ↔ `### Collation/Annotation`) equal in every chunk · `tr-` notes 6, each
where its chunk carries the word except c2 (S8).

---

## APPENDIX A — N1 SITE LIST (dry run; English only; `## English` line numbers as of commit `a20683e`)

Columns: chunk · line · OK (mechanical) / HAND · as built · proposed. Multiple rows on one line are applied left to right.

| chunk | line | kind | as built | proposed |
|---|---|---|---|---|
| c2 | L145 | OK | the second chapter of Genesis | Genesis, the second chapter |
| c2 | L149 | OK | the fourteenth chapter of Wisdom | Wisdom, the fourteenth chapter |
| c2 | L153 | OK | the second chapter of Esther | Esther, the second chapter |
| c2 | L157 | OK | the nineteenth chapter of the Apocalypse | the Apocalypse, the nineteenth chapter |
| c2 | L159 | OK | the sixth chapter of the first to the Corinthians | the first to the Corinthians, the sixth chapter |
| c2 | L159 | OK | the sixth chapter of the first to the Corinthians | the first to the Corinthians, the sixth chapter |
| c2 | L159 | OK | the twelfth chapter to the Romans | to the Romans, the twelfth chapter |
| c2 | L159 | OK | the seventeenth chapter of John | John, the seventeenth chapter |
| c2 | L161 | OK | the twenty-seventh chapter of Genesis | Genesis, the twenty-seventh chapter |
| c2 | L161 | OK | the seventeenth chapter of Luke | Luke, the seventeenth chapter |
| c2 | L163 | OK | the nineteenth chapter of Matthew | Matthew, the nineteenth chapter |
| c2 | L165 | OK | the fourteenth chapter of Luke | Luke, the fourteenth chapter |
| c2 | L165 | OK | the twenty-second chapter of Matthew | Matthew, the twenty-second chapter |
| c2 | L167 | OK | the twenty-second chapter of Matthew | Matthew, the twenty-second chapter |
| c2 | L167 | OK | the fourteenth chapter of Luke | Luke, the fourteenth chapter |
| c2 | L169 | OK | the twenty-fifth chapter of Matthew | Matthew, the twenty-fifth chapter |
| c2 | L169 | OK | the nineteenth chapter of the Apocalypse | the Apocalypse, the nineteenth chapter |
| c2 | L179 | OK | the thirty-first chapter of Ecclesiasticus | Ecclesiasticus, the thirty-first chapter |
| c2 | L179 | OK | the thirty-first chapter of Ecclesiasticus | Ecclesiasticus, the thirty-first chapter |
| c2 | L179 | OK | the thirty-first chapter of Ecclesiasticus | Ecclesiasticus, the thirty-first chapter |
| c2 | L179 | OK | the thirty-first chapter of Ecclesiasticus | Ecclesiasticus, the thirty-first chapter |
| c2 | L179 | OK | the twenty-first chapter of Proverbs | Proverbs, the twenty-first chapter |
| c2 | L181 | OK | the thirty-second chapter of Deuteronomy | Deuteronomy, the thirty-second chapter |
| c2 | L181 | OK | the sixth chapter of Amos | Amos, the sixth chapter |
| c2 | L181 | OK | the second chapter of Wisdom | Wisdom, the second chapter |
| c2 | L181 | OK | the fifth chapter to the Ephesians | to the Ephesians, the fifth chapter |
| c2 | L181 | OK | the twentieth chapter of Proverbs | Proverbs, the twentieth chapter |
| c2 | L181 | OK | the fourth chapter of Proverbs | Proverbs, the fourth chapter |
| c2 | L181 | OK | the twenty-seventh chapter of Ezechiel | Ezechiel, the twenty-seventh chapter |
| c2 | L181 | OK | the second chapter of Habacuc | Habacuc, the second chapter |
| c2 | L181 | OK | the seventeenth chapter of the Apocalypse | the Apocalypse, the seventeenth chapter |
| c2 | L183 | OK | the twenty-third chapter of Proverbs | Proverbs, the twenty-third chapter |
| c2 | L183 | OK | the fourteenth chapter of the Apocalypse | the Apocalypse, the fourteenth chapter |
| c2 | L183 | OK | the twenty-fifth chapter of Jeremias | Jeremias, the twenty-fifth chapter |
| c2 | L183 | OK | the third chapter of the third of Esdras | the third of Esdras, the third chapter |
| c2 | L183 | OK | the thirty-first chapter of Ecclesiasticus | Ecclesiasticus, the thirty-first chapter |
| c2 | L185 | OK | the fifth chapter of the Canticles | the Canticles, the fifth chapter |
| c2 | L185 | OK | the eighth chapter of the Canticles | the Canticles, the eighth chapter |
| c2 | L185 | OK | the first chapter of the Canticles | the Canticles, the first chapter |
| c2 | L187 | OK | the twenty-eighth chapter of Isaias | Isaias, the twenty-eighth chapter |
| c2 | L187 | OK | the twenty-first chapter of Proverbs | Proverbs, the twenty-first chapter |
| c2 | L187 | OK | the thirty-first chapter of Ecclesiasticus | Ecclesiasticus, the thirty-first chapter |
| c2 | L187 | OK | the twenty-third chapter of Proverbs | Proverbs, the twenty-third chapter |
| c2 | L189 | OK | the tenth chapter of Luke | Luke, the tenth chapter |
| c2 | L189 | OK | the third chapter of the third of Esdras | the third of Esdras, the third chapter |
| c2 | L189 | OK | the fifth chapter of the first to Timothy | the first to Timothy, the fifth chapter |
| c2 | L189 | OK | the first chapter of the Canticles | the Canticles, the first chapter |
| c2 | L195 | OK | the last chapter of Ecclesiastes | Ecclesiastes, the last chapter |
| c2 | L195 | OK | the nineteenth chapter of Matthew | Matthew, the nineteenth chapter |
| c2 | L195 | OK | the eighth chapter of Matthew | Matthew, the eighth chapter |
| c2 | L195 | OK | the thirteenth chapter of John | John, the thirteenth chapter |
| c2 | L197 | OK | the eleventh chapter of the Apocalypse | the Apocalypse, the eleventh chapter |
| c2 | L197 | OK | the third chapter of Malachias | Malachias, the third chapter |
| c2 | L197 | OK | the third chapter of the first to the Corinthians | the first to the Corinthians, the third chapter |
| c2 | L197 | OK | the forty-third chapter of Ezechiel | Ezechiel, the forty-third chapter |
| c2 | L199 | OK | the second chapter of Jonas | Jonas, the second chapter |
| c2 | L203 | OK | the sixth chapter of the third of Kings | the third of Kings, the sixth chapter |
| c2 | L205 | OK | the forty-third chapter of Ezechiel | Ezechiel, the forty-third chapter |
| c2 | L207 | OK | the forty-seventh chapter of Ezechiel | Ezechiel, the forty-seventh chapter |
| c2 | L209 | OK | the fifth chapter of the third of Kings | the third of Kings, the fifth chapter |
| c2 | L209 | OK | the second chapter to the Ephesians | to the Ephesians, the second chapter |
| c2 | L209 | OK | the thirtieth chapter of Jeremias | Jeremias, the thirtieth chapter |
| c2 | L211 | OK | the fifth chapter of the first of Esdras | the first of Esdras, the fifth chapter |
| c2 | L211 | OK | the forty-fifth chapter of Ecclesiasticus | Ecclesiasticus, the forty-fifth chapter |
| c2 | L211 | HAND | the ninth chapter of the first of Paralipomenon | the first of Paralipomenon, the ninth chapter |
| c2 | L215 | OK | the third chapter of the first to the Corinthians | the first to the Corinthians, the third chapter |
| c2 | L217 | OK | the third chapter of the first to the Corinthians | the first to the Corinthians, the third chapter |
| c2 | L217 | OK | the eighth chapter of the third of Kings | the third of Kings, the eighth chapter |
| c2 | L217 | OK | the sixth chapter of the second to the Corinthians | the second to the Corinthians, the sixth chapter |
| c2 | L219 | OK | the second chapter of Nahum | Nahum, the second chapter |
| c2 | L219 | OK | the second chapter of the first of Machabees | the first of Machabees, the second chapter |
| c2 | L225 | OK | the fourth chapter of John | John, the fourth chapter |
| c2 | L225 | OK | the tenth chapter of John | John, the tenth chapter |
| c2 | L231 | OK | the tenth chapter of John | John, the tenth chapter |
| c2 | L231 | OK | the twenty-third chapter of Luke | Luke, the twenty-third chapter |
| c2 | L231 | OK | the last chapter of Luke | Luke, the last chapter |
| c2 | L237 | OK | the third chapter of the first to the Corinthians | the first to the Corinthians, the third chapter |
| c2 | L237 | OK | the ninth chapter of Wisdom | Wisdom, the ninth chapter |
| c3 | L135 | OK | the fifth chapter of Job | Job, the fifth chapter |
| c3 | L135 | OK | the fourteenth chapter of Job | Job, the fourteenth chapter |
| c3 | L137 | OK | the second chapter of Wisdom | Wisdom, the second chapter |
| c3 | L137 | OK | the fifth chapter of Wisdom | Wisdom, the fifth chapter |
| c3 | L137 | OK | the fourth chapter of Ecclesiastes | Ecclesiastes, the fourth chapter |
| c3 | L139 | OK | the third chapter of Job | Job, the third chapter |
| c3 | L139 | OK | the seventeenth chapter of Proverbs | Proverbs, the seventeenth chapter |
| c3 | L139 | HAND | the sixteenth chapter of Ezechiel | Ezechiel, the sixteenth chapter |
| c3 | L139 | OK | the forty-first chapter of Ecclesiasticus | Ecclesiasticus, the forty-first chapter |
| c3 | L139 | OK | the fifth chapter of Wisdom | Wisdom, the fifth chapter |
| c3 | L141 | OK | the third chapter of John | John, the third chapter |
| c3 | L141 | OK | the first chapter of John | John, the first chapter |
| c3 | L141 | OK | the third chapter of John | John, the third chapter |
| c3 | L145 | OK | the eighth chapter to the Romans | to the Romans, the eighth chapter |
| c3 | L145 | OK | the third chapter of John | John, the third chapter |
| c3 | L147 | OK | the first chapter of John | John, the first chapter |
| c3 | L147 | OK | the fifth chapter of the first of John | the first of John, the fifth chapter |
| c3 | L147 | OK | the third chapter of the first of John | the first of John, the third chapter |
| c3 | L147 | OK | the fifth chapter of the first of John | the first of John, the fifth chapter |
| c3 | L147 | OK | the fifth chapter of the first of John | the first of John, the fifth chapter |
| c3 | L149 | OK | the second chapter of the first of John | the first of John, the second chapter |
| c3 | L157 | OK | the third chapter of John | John, the third chapter |
| c3 | L157 | OK | the twelfth chapter of John | John, the twelfth chapter |
| c3 | L157 | OK | the ninth chapter of John | John, the ninth chapter |
| c3 | L157 | OK | the fourth chapter of the first of Peter | the first of Peter, the fourth chapter |
| c3 | L159 | OK | the twelfth chapter of Ecclesiastes | Ecclesiastes, the twelfth chapter |
| c3 | L159 | OK | the twentieth chapter of the Apocalypse | the Apocalypse, the twentieth chapter |
| c3 | L159 | OK | the third chapter of John | John, the third chapter |
| c3 | L161 | OK | the fifth chapter of John | John, the fifth chapter |
| c3 | L161 | OK | the nineteenth chapter of Matthew | Matthew, the nineteenth chapter |
| c3 | L161 | OK | the third chapter of Wisdom | Wisdom, the third chapter |
| c3 | L161 | OK | the twelfth chapter of Matthew | Matthew, the twelfth chapter |
| c3 | L161 | OK | the eleventh chapter of Luke | Luke, the eleventh chapter |
| c3 | L167 | OK | the fifth chapter to the Romans | to the Romans, the fifth chapter |
| c3 | L167 | OK | the seventh chapter of John | John, the seventh chapter |
| c3 | L167 | OK | the fifth chapter to the Galatians | to the Galatians, the fifth chapter |
| c3 | L183 | OK | the second chapter of Luke | Luke, the second chapter |
| c3 | L183 | OK | the third chapter of the first of Kings | the first of Kings, the third chapter |
| c3 | L183 | OK | the tenth chapter of Esther | Esther, the tenth chapter |
| c3 | L183 | OK | the twenty-fourth chapter of Ecclesiasticus | Ecclesiasticus, the twenty-fourth chapter |
| c3 | L187 | OK | the last chapter of Matthew | Matthew, the last chapter |
| c3 | L187 | OK | the second chapter of Daniel | Daniel, the second chapter |
| c3 | L189 | OK | the fourth chapter of Mark | Mark, the fourth chapter |
| c3 | L189 | OK | the seventeenth chapter of the second of Paralipomenon | the second of Paralipomenon, the seventeenth chapter |
| c3 | L189 | OK | the first chapter of Exodus | Exodus, the first chapter |
| c3 | L189 | OK | the first chapter of Luke | Luke, the first chapter |
| c3 | L189 | OK | the first chapter of Genesis | Genesis, the first chapter |
| c3 | L189 | OK | the twenty-sixth chapter of Genesis | Genesis, the twenty-sixth chapter |
| c3 | L189 | OK | the first chapter to the Colossians | to the Colossians, the first chapter |
| c3 | L191 | OK | the eighth chapter of Job | Job, the eighth chapter |
| c3 | L191 | OK | the twenty-first chapter of Ecclesiasticus | Ecclesiasticus, the twenty-first chapter |
| c3 | L191 | OK | the forty-ninth chapter of Genesis | Genesis, the forty-ninth chapter |
| c3 | L191 | OK | the thirteenth chapter of Matthew | Matthew, the thirteenth chapter |
| c3 | L191 | OK | the eighth chapter of Luke | Luke, the eighth chapter |
| c3 | L191 | OK | the thirteenth chapter of Matthew | Matthew, the thirteenth chapter |
| c3 | L193 | OK | the first chapter of Exodus | Exodus, the first chapter |
| c3 | L193 | OK | the nineteenth chapter of Ezechiel | Ezechiel, the nineteenth chapter |
| c3 | L193 | OK | the second chapter of the first of Peter | the first of Peter, the second chapter |
| c3 | L193 | OK | the forty-first chapter of Genesis | Genesis, the forty-first chapter |
| c3 | L195 | OK | the ninth chapter of the second to the Corinthians | the second to the Corinthians, the ninth chapter |
| c3 | L195 | OK | the sixth chapter of Matthew | Matthew, the sixth chapter |
| c3 | L197 | OK | the fourth chapter to the Ephesians | to the Ephesians, the fourth chapter |
| c3 | L197 | OK | the third chapter of the second of Peter | the second of Peter, the third chapter |
| c3 | L197 | OK | the first chapter to the Colossians | to the Colossians, the first chapter |
| c3 | L197 | OK | the fourth chapter of Proverbs | Proverbs, the fourth chapter |
| c3 | L197 | OK | the ninth chapter of Esther | Esther, the ninth chapter |
| c3 | L199 | OK | the third chapter of the second of Peter | the second of Peter, the third chapter |
| c3 | L199 | OK | the fourth chapter to the Ephesians | to the Ephesians, the fourth chapter |
| c3 | L199 | OK | the first chapter of Job | Job, the first chapter |
| c3 | L199 | OK | the first chapter of Luke | Luke, the first chapter |
| c3 | L205 | OK | the eighth chapter of the Canticles | the Canticles, the eighth chapter |
| c3 | L205 | OK | the fifty-fifth chapter of Isaias | Isaias, the fifty-fifth chapter |
| c3 | L205 | OK | the fiftieth chapter of Isaias | Isaias, the fiftieth chapter |
| c3 | L205 | OK | the sixth chapter of John | John, the sixth chapter |
| c3 | L205 | OK | the second chapter of the Apocalypse | the Apocalypse, the second chapter |
| c3 | L211 | OK | the twenty-fourth chapter of Job | Job, the twenty-fourth chapter |
| c3 | L211 | OK | the third chapter of the first of Kings | the first of Kings, the third chapter |
| c3 | L211 | OK | the third chapter of John | John, the third chapter |
| c3 | L217 | OK | the first chapter of John | John, the first chapter |
| c3 | L217 | OK | the third chapter of John | John, the third chapter |
| c3 | L217 | OK | the first chapter of John | John, the first chapter |
| c4 | L171 | OK | the fourth chapter of the Canticles | the Canticles, the fourth chapter |
| c4 | L171 | OK | the second chapter of Genesis | Genesis, the second chapter |
| c4 | L173 | OK | the first chapter of Ecclesiasticus | Ecclesiasticus, the first chapter |
| c4 | L173 | OK | the thirteenth chapter of Zacharias | Zacharias, the thirteenth chapter |
| c4 | L173 | OK | the second chapter of Jeremias | Jeremias, the second chapter |
| c4 | L175 | OK | the fifteenth chapter of Ecclesiasticus | Ecclesiasticus, the fifteenth chapter |
| c4 | L175 | OK | the thirty-sixth chapter of Ezechiel | Ezechiel, the thirty-sixth chapter |
| c4 | L175 | OK | the twelfth chapter of Isaias | Isaias, the twelfth chapter |
| c4 | L175 | OK | the twenty-fifth chapter of Proverbs | Proverbs, the twenty-fifth chapter |
| c4 | L175 | OK | the seventh chapter of the Apocalypse | the Apocalypse, the seventh chapter |
| c4 | L175 | OK | the twelfth chapter of Isaias | Isaias, the twelfth chapter |
| c4 | L183 | OK | the tenth chapter of Matthew | Matthew, the tenth chapter |
| c4 | L183 | OK | the fourteenth chapter to the Romans | to the Romans, the fourteenth chapter |
| c4 | L183 | OK | the thirtieth chapter of Proverbs | Proverbs, the thirtieth chapter |
| c4 | L183 | OK | the sixth chapter of John | John, the sixth chapter |
| c4 | L183 | OK | the sixth chapter of John | John, the sixth chapter |
| c4 | L183 | OK | the twelfth chapter of Tobias | Tobias, the twelfth chapter |
| c4 | L191 | OK | the tenth chapter of Matthew | Matthew, the tenth chapter |
| c4 | L193 | OK | the last chapter of the second to the Thessalonians | the second to the Thessalonians, the last chapter |
| c4 | L193 | OK | the third chapter of Genesis | Genesis, the third chapter |
| c4 | L193 | OK | the fourth chapter of Ezechiel | Ezechiel, the fourth chapter |
| c4 | L193 | OK | the thirty-seventh chapter of Ecclesiasticus | Ecclesiasticus, the thirty-seventh chapter |
| c4 | L193 | OK | the twentieth chapter of Job | Job, the twentieth chapter |
| c4 | L193 | OK | the sixteenth chapter of Luke | Luke, the sixteenth chapter |
| c4 | L195 | OK | the first chapter of Lamentations | Lamentations, the first chapter |
| c4 | L195 | OK | the eleventh chapter of Leviticus | Leviticus, the eleventh chapter |
| c4 | L195 | OK | the thirtieth chapter of Job | Job, the thirtieth chapter |
| c4 | L195 | OK | the first chapter of Lamentations | Lamentations, the first chapter |
| c4 | L195 | OK | the fifty-fifth chapter of Isaias | Isaias, the fifty-fifth chapter |
| c4 | L197 | OK | the sixteenth chapter of Wisdom | Wisdom, the sixteenth chapter |
| c4 | L197 | OK | the nineteenth chapter of the third of Kings | the third of Kings, the nineteenth chapter |
| c4 | L197 | OK | the sixteenth chapter of Wisdom | Wisdom, the sixteenth chapter |
| c4 | L199 | OK | the nineteenth chapter of the second of Kings | the second of Kings, the nineteenth chapter |
| c4 | L199 | OK | the thirty-third chapter of Job | Job, the thirty-third chapter |
| c4 | L199 | OK | the twenty-first chapter of Numbers | Numbers, the twenty-first chapter |
| c4 | L207 | OK | the thirteenth chapter of the second of Kings | the second of Kings, the thirteenth chapter |
| c4 | L207 | OK | the eleventh chapter of Numbers | Numbers, the eleventh chapter |
| c4 | L207 | OK | the first chapter of Daniel | Daniel, the first chapter |
| c4 | L209 | OK | the twelfth chapter of Osee | Osee, the twelfth chapter |
| c4 | L209 | OK | the twenty-third chapter of Proverbs | Proverbs, the twenty-third chapter |
| c4 | L209 | OK | the seventh chapter of Leviticus | Leviticus, the seventh chapter |
| c4 | L209 | OK | the twenty-third chapter of Proverbs | Proverbs, the twenty-third chapter |
| c4 | L209 | OK | the thirteenth chapter of Ecclesiasticus | Ecclesiasticus, the thirteenth chapter |
| c4 | L209 | OK | the nineteenth chapter of Judges | Judges, the nineteenth chapter |
| c4 | L215 | OK | the fifteenth chapter of Ecclesiasticus | Ecclesiasticus, the fifteenth chapter |
| c4 | L215 | OK | the twenty-fourth chapter of Matthew | Matthew, the twenty-fourth chapter |
| c4 | L215 | OK | the fourteenth chapter of Ecclesiasticus | Ecclesiasticus, the fourteenth chapter |
| c4 | L217 | OK | the fourth chapter of John | John, the fourth chapter |
| c4 | L217 | OK | the fifth chapter to the Hebrews | to the Hebrews, the fifth chapter |
| c4 | L219 | OK | the sixth chapter of John | John, the sixth chapter |
| c4 | L223 | OK | the first chapter of Matthew | Matthew, the first chapter |
| c4 | L223 | OK | the second chapter of Luke | Luke, the second chapter |
| c4 | L223 | OK | the third chapter to the Philippians | to the Philippians, the third chapter |
| c4 | L225 | OK | the seventh chapter of Luke | Luke, the seventh chapter |
| c4 | L225 | OK | the fourth chapter of the first of Machabees | the first of Machabees, the fourth chapter |
| c4 | L225 | OK | the tenth chapter of Matthew | Matthew, the tenth chapter |
| c4 | L231 | OK | the second chapter of Ecclesiastes | Ecclesiastes, the second chapter |
| c4 | L233 | OK | the twenty-second chapter of Isaias | Isaias, the twenty-second chapter |
| c4 | L233 | OK | the second chapter of Wisdom | Wisdom, the second chapter |
| c4 | L233 | OK | the second chapter of Wisdom | Wisdom, the second chapter |
| c4 | L233 | OK | the fourteenth chapter of Ecclesiasticus | Ecclesiasticus, the fourteenth chapter |
| c4 | L233 | OK | the seventeenth chapter of the Acts | the Acts, the seventeenth chapter |
| c4 | L233 | OK | the fourth chapter of the second to Timothy | the second to Timothy, the fourth chapter |
| c4 | L235 | OK | the fourteenth chapter of Luke | Luke, the fourteenth chapter |
| c4 | L247 | OK | the first chapter of the first of Machabees | the first of Machabees, the first chapter |
| c4 | L247 | OK | the first chapter of Lamentations | Lamentations, the first chapter |
| c4 | L247 | OK | the fifth chapter of Ecclesiastes | Ecclesiastes, the fifth chapter |
| c4 | L247 | OK | the first chapter of Lamentations | Lamentations, the first chapter |
| c4 | L247 | OK | the first chapter of Lamentations | Lamentations, the first chapter |
| c4 | L249 | OK | the fourth chapter of Osee | Osee, the fourth chapter |
| c4 | L249 | OK | the thirty-seventh chapter of Ecclesiasticus | Ecclesiasticus, the thirty-seventh chapter |
| c4 | L249 | OK | the fortieth chapter of Isaias | Isaias, the fortieth chapter |
| c4 | L255 | OK | the second chapter of James | James, the second chapter |
| c4 | L255 | HAND | the fourth chapter of the fourth of Kings | the fourth of Kings, the fourth chapter |
| c4 | L259 | OK | the fourth chapter of the fourth of Kings | the fourth of Kings, the fourth chapter |
| c4 | L259 | OK | the seventh chapter of Luke | Luke, the seventh chapter |
| c4 | L259 | OK | the eighth chapter of Luke | Luke, the eighth chapter |
| c4 | L259 | OK | the eleventh chapter of John | John, the eleventh chapter |
| c4 | L267 | OK | the first chapter of Lamentations | Lamentations, the first chapter |
| c4 | L271 | OK | the eighth chapter of Matthew | Matthew, the eighth chapter |
| c4 | L271 | OK | the fourth chapter of John | John, the fourth chapter |
| c4 | L271 | OK | the third chapter of Exodus | Exodus, the third chapter |
| c4 | L277 | OK | the fourth chapter of John | John, the fourth chapter |
| c4 | L277 | OK | the twenty-sixth chapter of Ecclesiasticus | Ecclesiasticus, the twenty-sixth chapter |
| c4 | L277 | OK | the sixty-fifth chapter of Isaias | Isaias, the sixty-fifth chapter |
| c4 | L277 | OK | the twenty-fourth chapter of Ecclesiasticus | Ecclesiasticus, the twenty-fourth chapter |
| c4 | L283 | OK | the fifteenth chapter of Genesis | Genesis, the fifteenth chapter |
| c4 | L283 | OK | the sixth chapter of Luke | Luke, the sixth chapter |
| c4 | L283 | OK | the fourth chapter of John | John, the fourth chapter |
| c4 | L289 | OK | the tenth chapter of John | John, the tenth chapter |
| c4 | L215 | HAND (sentence-initial) | The thirteenth chapter of Proverbs | Proverbs, the thirteenth chapter |

**Appendix A total: 250 rows (c2 78 · c3 81 · c4 91) on 80 distinct lines; 4 HAND.**
