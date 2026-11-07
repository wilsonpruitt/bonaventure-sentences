# Authorities index — full pass (SITE-PLAN Phase 4), 2026-11-07

Follows `manual-review/authorities-pilot.md`. Wilson's go: "Opus go" (2026-11-07). Rulings R1–R7 were
applied as recommended in the pilot; they were not ruled on individually (see repo `CLAUDE.md`
§ "Authorities conventions"). Nothing pushed or deployed.

## Result

| | pilot close | full pass |
|---|---|---|
| authority records | 13,969 | **17,078** |
| to a work | 12,911 (92.4%) | **16,737 (98.0%)** |
| author-level residue | 826 | **175** |
| same-passage, no work | 232 | **166** |
| table | 52 authors · 284 works · 676 abbrev. | **87 authors · 424 works · 1,009 abbrev.** |

Ledger `index/authorities.tsv` (17,078 rows, 2.4 MB). Site: `/authorities` (87 authors), one page per
author, one per work (421), and an "Authorities cited here" panel on 1,990 text pages. **All 17,078 locus
links verified against the built site: page present and `#fn-N` anchor present, 0 misses.**

## A. Residue (826 → 175)

The residue was mostly not unknown works but **mechanics**: the body named the work and the join could
not read it.
- Note titles for the body author were matched only if ≥6 characters (`Phys.` failed); a numeral book
  swallowed `83` in *Libr. 83 Quaest.*; titles after a locus (*Tract. 27. in Ioan. Evang.*); bracketed titles.
- Body forms: table abbreviations are now read in prose (`de Lib. arb.` → *de Libero Arbitrio*,
  `Poster.` → *Posteriorum*), with a capitalised 4+-letter key word so *prior*, *confessio* never fire;
  prose forms case-free; a title just after the anchor; *in eodem libro*.
- Abbreviated words may lengthen (`concup.` → `concupisc.`); words after the first are case-free.
- 140 works added in all (with the new authors below); for existing authors mostly Augustine's long tail (de Duabus animabus, de Opere monachorum, the
  anti-Donatist works, the pseudonymous de Ecclesiasticis dogmatibus, de Mirabilibus sacrae Scripturae,
  de Vera et falsa poenitentia, Quaestiones veteris et novi Testamenti) and the Scripture commentaries
  named in the body (*super Ioannem*, *super Ezechielem*, *super Lucam*).
- What is left is honest: *Augustinus in quinto libro* with a bare *Cap. 8*; *Ex eodem loc. cit.* with no
  author in reach.

## B. Missing authors (35 added)

Theophylact, Cyril of Alexandria, Cyril of Jerusalem, William of Auxerre, William de la Mare, Tertullian,
Alcuin, Basil, Praepositinus, Nicephorus Callistus, Irenaeus, Haymo, Athanasius, Epiphanius (and the
Monk), Nemesius, Leo the Great, Peter of Poitiers, Ovid, John of La Rochelle, Gregory of Tours, Macrobius,
Maximus the Confessor, Gennadius, Horace, Eusebius, Alger of Liège, Lactantius, Cyprian, Paschasius
Radbertus, Paschasius the Deacon, Gandulph of Bologna, Hesychius, Gabriel Biel, and the anonymous *Liber
de causis* (69 records). Oblique-case sigla for the scholastics (*B. Alberto*, *S. Thoma*).
Excluded as not authorities: *Gorranus* (251 mentions, a textual witness), Cornelius a Lapide,
Forcellini, Serranus, Wrobel, Mone.

## C. Same passage

*in hunc locum* of an exegete is his commentary on the verse in question. An `exegesis` map per author
(Scripture book → work) and the verse before the siglum resolve it (147 records); in the Scripture
commentaries, the commented book, and the scholastics' commentaries on John (Thomas's *Lectura*,
Albert's *Postilla*) rather than their Sentences commentaries. *X et Y, hic* now records both (+240).

## D. Verification (report → fix → report)

**Precision** — fresh random records, author and work judged against the note and the body:

| round | sample | right | defects found (all fixed unless noted) |
|---|---|---|---|
| 1 | 50 per volume (300) | **298** | shared-title owners compared by string (*In Hexaem.*: Bede for Basil); Theophylact *in hunc locum* to Matthew from a verse inside a quotation |
| 2 | fresh Vol II, VI (100) | 97 | Lombard's Sentences filed under S. Thoma (not_authorities never consulted); *(sive de Dono perseverantiae)*; ⚠ *Cfr. V. Metaph.* after an Averroes quotation read as Averroes — **accepted ambiguity, not fixed** |
| 3 | fresh Vol VI (50) | 50 | — |
| 4 | 10 per volume (60) | 57 | prose word read as a lengthened title (*Distinctionem* → Alan ×2); *de Gen. ad lit. imperfectus* missing |
| 5 | 10 per volume (60), final code | **60** | — |
| | **total** | **562 / 570 (98.6%)** | |

Also checked by sample: every new mechanism (continued notes 25/25, shared *hic* 15/15, *inter opera*
20/20, Glossa layers 12/12, verse-resolved same-passage 15/15, new authors 30/30).

**Recall** — 20–30 random apparatus entries per volume, every authority in them checked. Gaps found and
closed: Boethius on *de Interpretatione*; *Ad Catech.*; **notes continuing in the body author's voice**
(+483 records); Albert's Aristotle paraphrases; ***X et Y, hic***; **`(inter opera August.)`** (+66);
**Glossa *ordinaria/interlinearis* had been sigla, swallowing the work** (+~480); *Card. Hugo: «…»*.
Vol V's sample found no miss.

**Fixes that were too strict, caught only by the lost-records diff:** the scope stops (first cut every
*Magistri* and *Cod.*, losing ~20 real citations and Justinian's *Codex*); the exact-match unique-title
rule (lost ~25 real titles, e.g. *de Nuptiis et concupiscentia*). Both replaced by narrower rules. Lesson
kept in CLAUDE.md: every rule change gets a diff of lost and changed records, not only a sample of new ones.

**Our own placeholders.** 118 apparatus entries carry this edition's English editorial text; 20 are
wholly ours (*OCR-bled … see ambiguities log*) and are excluded; `[Quaracchi p. N footer entry N.]`
prefixes are stripped and the entry kept.

## E. Site

`tools/build-index-json.py` → `authorities/{author}.json` (largest Augustine 2.1 MB, read from disk at
build time), `index-authorities-toc.json` (37 KB), `authorities-by-chunk.json` (458 KB). Pages render
Latin titles (R7: English for works later), the printed locus with book numeral, and flags *named in the
text*, *via loc. cit.*, *attributed*. Nav link "Authorities"; sitemap includes all 510 pages. Full build
passes (3,101 HTML, Pagefind unchanged at 2,303 indexed pages).

## Open

- Per R7, English names for works (top ~100) — not done.
- The Averroes/Aristotle *Cfr.* ambiguity class (after a quotation inside another author's scope).
- `/authorities/augustine/de-trinitate` is a 706 KB page; split by book if it matters.
