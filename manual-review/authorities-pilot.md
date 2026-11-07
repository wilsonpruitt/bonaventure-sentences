# Authorities index — conventions pilot (SITE-PLAN Phase 4), 2026-11-06

**Deliverable:** frozen conventions (repo `CLAUDE.md` § "Authorities conventions"), measured rates, a priced full
pass. Not coverage. Tools: `tools/authorities.json` (the normalization table) and `tools/build-authorities.py`
(the deterministic extractor). Records from the slice: `manual-review/authorities-pilot-records.tsv`.

## Slice

Three citation cultures, 213 chunks, **3,436 apparatus entries** (~8% of the corpus's 41,262):
Vol I d. 1–10 (*Sentences*: sources plus scholastic parallels), the Breviloquium (a compendium), and
Ecclesiastes (a Scripture commentary: exegetes *in hunc locum*).

## What the data showed (and what it changed)

1. **Two kinds of authority, one syntax.** Sources Bonaventure uses (Aristotle 3,363 records corpus-wide, Augustine
   4,283, Gregory, Damascene, Anselm, …) and **parallel commentators** Quaracchi adds (*S. Thom., hic q. 5. a. 2*;
   *B. Albert., hic a. 21*; *Richard. a Med., hic*). → `role`: `cited` vs `same-passage` (the scope opens *hic* /
   *in hunc locum*), assigned mechanically. 1,824 same-passage records corpus-wide.
2. **The author is easy; the work title is the work.** *August., XIII. de Trin. c. 19. n. 24*: siglum, optional
   book numeral, abbreviation (italic only sometimes), locus. Titles are matched **per author**, case-sensitively
   (*Serm. 362* is a work; *in Ps. 118, serm. 13* is a locus), longest first. The same *S.* is Alexander's *Summa*
   after *Alex. Hal.* and Aquinas's after *S. Thom.*
3. **Table-driven, not discovered.** An open "Capitalized-word + comma" detector found 954 distinct author-shaped
   strings, heavy with noise (*Vat.*, *Edd.*, *Codd.*, *Migne*, *Magistri*, *Dei*, *Hal.*). Only table sigla count.
4. **⭐ IMPLICIT CITATIONS are ~a fifth of the whole.** A note giving only a locus (*Libr. X. c. 33. n. 50*;
   *Cap. 1. n. 2*; *Quaest. 35*) whose author and often work are named in the BODY at the anchor (*Augustinus in
   libro decimo de Trinitate[^n]*) — the Scripture index's "the verse is not where the citation is", again. 189
   such notes in the slice; corpus-wide the body join yields **2,943 records** (21%). Left out, the index would be
   silently short by a fifth. Join rule: nearest body name form within 220 chars before the anchor; work from the
   note's title, else the body title **nearest the anchor**; book from a Latin ordinal beside it.
5. **Rejected at the pilot:** a generic "note opens with a capitalized word + point" trigger for implicit notes. It
   admitted *Vat.*, *Multi codd.*, *Exod. 3, 14* and produced 5 wrong joins in 14. Only a real locus label or a
   title actually in the table now qualifies.
6. **Apparatus criticus is not an authority.** *Forte cod. X … licet falso alleget libr. IV. Phys.* reports a
   manuscript's mis-citation. A work matched where the editors report a witness's reading is skipped.
7. **Attribution follows Quaracchi.** `pseudo` where modern consensus and Quaracchi's own notes agree
   (*de Spiritu et anima*, *de Fide ad Petrum* — the note itself says *nunc communiter tribuitur Fulgentio*),
   and **`Serm. N. in Appendice`** = the Maurists' appendix of spurious sermons → pseudo.
8. **Gregory IX is not Gregory the Great.** *Decret. Gregor. lib. II. tit. 1* is the Decretals. A siglum that names
   its own work takes `default_work`.

## Precision (report → fix → report; every sample drawn fresh after the fixes it measures)

| sample | what | author + work right | locus right |
|---|---|---|---|
| 1 (seed 1106, before fixes) | 50 random records | 49/50 (one table error: Jerome *in I. Reg.* is the *Prologus galeatus*) | ~43/50 (bleed into next numeral; prose tails) |
| 2 (seed 20261107) | 50 fresh | 48/50 (witness reading; Gregory IX) | 43/48 |
| 3 (seed 808) | 30 body-join records | author 30/30, work 28/30 (one wrong: first title not nearest; one missed prose form) | many missing → fixed |
| **4 (seed 1999, final)** | **50 fresh, all record types** | **50/50** (49 to the right work, 1 honest author-level `loc. cit.`) — **0 wrong attributions** | 49/50 (*prosa 2*, since fixed) |

## Recall

- Random 30 slice entries: no explicit citation missed; surfaced the implicit class (item 4).
- 30 author-bearing entries: explicit-citation recall ~90% before the last table additions (misses: Gilbert of
  Poitiers, a *de Genes.* variant), title-without-siglum citations resolved since by unique-title inference.
- **Authors not in the table, corpus-wide: 558 author-shaped mentions (~4%), 263 distinct strings**; the top 41
  (≥3 each) cover 303: Theophylact, Tertullian, Alcuin, Basil, Haymo, Irenaeus, Peter of Poitiers, William of
  Auxerre, Athanasius, Epiphanius, Gregory of Tours, Cyprian, Horace, Ovid, Macrobius, Praepositinus, Justin,
  Maximus, John of La Rochelle, Leo, Eusebius, Pliny, Euclid… plus spacing variants of known sigla (*Vict.*,
  *Hispan.*, *Hug.*). Implicit citations of unknown authors are not measured (they cannot be seen without the name).

## Whole corpus (deterministic run, no tokens, scratch output only)

- **13,969 authority records; 12,911 (92.4%) to a work.** Per volume 91–94% — the slice table generalizes.
- via: title 8,807 · same-passage 1,824 · body-join (note title 1,327 · body title 950 · author only 666) ·
  anaphor 139 (+92 unresolved) · unique-title 90 · no-title 68 · default-work 6.
- **Residue to close:** 826 author-level records (758 distinct strings; Augustine 334, Aristotle 73, Gregory 53,
  Bernard 44, Hugh 44 …) + 232 same-passage records whose author has no commentary in the table + the 263
  unknown-author strings.
- Table now: **52 authors · 284 works · 676 abbreviations**. Runtime 11 s for the corpus.

## The full pass, priced

| step | what | model | est. tokens |
|---|---|---|---|
| A | Close the residue: ~760 author-level strings → works (mostly Augustine's long tail), with context | Opus | 150–250K |
| B | Add the ~40 recurring missing authors and their works; spacing variants | Opus | 80–150K |
| C | Exegetes' commentaries for the 232 same-passage records (Haymo, Alcuin, Bede, Rabanus, Theophylact, …) | Opus | 30–50K |
| D | Verify: a fresh 50-record sample **per volume** (300) + a recall check per volume; report → fix → report | Opus | 80–120K |
| E | Ledger `index/authorities.tsv`, `site/src/data/index-authorities.json`, `/authorities` pages (author → work → locus → citing chunks), cross-links from chunk pages | Opus | 80–120K |
| | **Total** | | **≈ 420–690K** |

Opus, not Sonnet: steps A–C are identification work that needs the patristic and scholastic bibliography (which
*Alexandr., in hunc locum* is meant; which Augustine work *contra Epist. Manichaei* is), and a wrong identification
is silent. The extraction itself costs nothing.

## Rulings asked of Wilson (recommendations in bold)

1. **R1 Two roles, shown separately** — `cited` (the sources) and `same-passage` (other doctors on this passage).
2. **R2 Attribution follows Quaracchi**, `pseudo` only where Quaracchi's notes agree (and *in Appendice*); English
   display may use the modern name (*Pseudo-Dionysius*).
3. **R3 The index unit is author → work**; the locus kept as printed with a sort key; no mapping to modern editions.
4. **R4 Implicit (body-join) citations included**, audited through `via`, displayed like the rest.
5. **R5 Excluded**: the Lombard's *Sentences* (cross-reference ledger's), Bonaventure himself, editions and
   manuscripts, witnesses' readings.
6. **R6 A separate ledger** `index/authorities.tsv`, not the `authority` class of `index/citations.tsv`
   (different grammar; the verified cross-reference ledger stays untouched; its 1,166 `authority` rows remain the
   exclusion guard). ⚠ This departs from SITE-PLAN's wording ("ledger class `authority` filled out").
7. **R7 Titles in canonical Latin**; English for authors now, for works optional (top ~100 later).
