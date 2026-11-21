# Vol VII — load + pilot setup (2026-11-14, Fable; scouting session, nothing built)

Everything below is **MEASURED** (on the plate, or on the text layer and said so) unless labelled **PREDICTION**.
Nothing here is a chunking decision or a ruling: the proposals are in `manual-review/lucam-pilot-scouting.md`, and
they are proposals until Wilson answers. **Vol VII ruling numbering restarts at 1 in this file** (Vol VI's ran 1–156
in `vol6-pilot-setup.md`); rulings are appended below the Traps section as they are given.
Standing warning: *a work map's description of an unopened work is a guess wearing a table cell.*

## Loaded

- Source: Internet Archive `doctorisseraphic07bona` (identity confirmed by its own contents leaf, "INDEX EORUM QUAE
  IN SEPTIMO TOMO CONTINENTUR", and by the sheet signature `S. Bonav. — Tom. VII.` at the page feet).
  `raw/doctorisseraphic07bona.pdf` (120.6 MB, **892 pp**) + `raw/doctorisseraphic07bona_djvu.txt` (6.7 MB,
  161,973 lines), both gitignored.
- **`pdf = printed + 26`.** Verified on the running-head folio of every 25th leaf from printed 24 to 604, and on the
  boundary leaves 3 / 11 / 604 / 607 / 652 / 655 / 657 / 858.
- Pages are **2476 × 3921 px at 300 dpi NATIVE.** ⚠ This is not the project's 450 dpi: Vols V and VI were 450-dpi
  scans, this one is 300. Extracting at 450 only upsamples. Two-column with a **printed centre rule**, outer-margin
  marginalia, per-page footnote register: the same Quaracchi furniture as Vols V and VI.
- Tooling wired (both edits uncommitted until this session's commit): `tools/extract-pages.py --volume vol7`
  (offset 26, printed 1–858) and `tools/colcrop.py` (`auto` gutter for `vol7`, as for `vol5` / `vol6`). `vol7/` and
  `raw/vision/vol7/` created. **NOT yet wired:** `site/scripts/build-content.mjs` `VOL_DIRS` and the registry entry
  (next free `book:` is **19**), `tools/build-citations.py` `VOLUME_COMPLETE` (stays `{1..6: True}`), the
  `check-vol5-*` / census `VOLUMES` lists, `site/scripts/build-progress.mjs`. Do these when the first chunk lands,
  not before.
- Plates pulled at 300 dpi (regenerable, gitignored): pp. 1, 2, 3, 7, 11, 13, 43, 112, 128, 252, 604, 605, 606,
  607, 652, 655, 657, 858; and the Prolegomena leaf p. XVIII (PDF 24) and two full-resolution crops of p. 858 in
  the session scratchpad only.

## The volume: one work and a two-piece appendix

Front matter (PDF 1–26): PDF 12 `OPERA HUIUS TOMI`; **Prolegomena pp. VII–XVI** (PDF 13–22; C. I on the genuine
Luke commentary, C. II *De pluribus opusculis illegitimis vel saltem dubiis*); **p. XVII** (PDF 23) the Tabula
codicum (Luke: codd. A–L, eleven; Lament.: A = Paris BN 14260, B = Prague; Orat. Dom.: A, B, C; edd. 1, 2);
**p. XVIII** (PDF 24) the `TABULA DIVISIONUM PRINCIPALIUM` (transcribed below). Prolegomena are editorial and are
not chunked, as in Vols V and VI.

| # | Work | Half-title | Blank | **Body** | Notes |
|---|---|---|---|---|---|
| 1 | *Commentarius in Evangelium S. Lucae* | p. 1 | p. 2 | **3–604** (PDF 29–630; 602 pp) | Prooemium 3–7 · Prologus S. Hieronymi + expositio 7–10 · Commentarius, 24 capitula, 11–604. p. 604 is a short last page. |
| 2 | Appendix: *Expositio Threnorum Ieremiae Prophetae* | p. 605 (`APPENDIX DUORUM OPUSCULORUM SALTEM DUBIORUM…`) | p. 606 | **607–651** (45 pp) | Prooemium 607–609 · `INCIPIT EXPOSITIO THRENORUM` + Cap. I 610 · Cap. II 625 · Cap. III 637 · Cap. IV 647. ≈ 42.8K words incl. apparatus (text layer). **No `Capitulum V` heading found on the text layer** (PREDICTION: the exposition stops at c. 4, or c. 5's heading failed OCR; read p. 651 before saying either). |
| 3 | Appendix: *Expositio Orationis Dominicae* | none of its own | — | **652–655** (4 pp) | ≈ 3.1K words. Shares the Appendix half-title at p. 605. |
| — | Indexes | — | p. 656 | 657–858 | p. 657 the volume index · pp. 659–857 the combined *Index rerum* for Tomes VI **and** VII (cites `VII 580 49` = tome / page / paragraph number) · p. 858 `CORRIGENDA ET ADDENDA`. |

**The volume index (p. 657) gives NO chapter or pericope lines for Luke.** It reads only: Prooemium 3 · Prologus
S. Hieronymi eiusque expositio 7 · Commentarius 11. ⚠ This is the one large difference from Vol VI: the Ioannem's
109 chunks were the index's own verse-pericopes; Luke's index offers no unit at all. The unit has to come from the
body (see "What the pilot has to decide").

### The Luke commentary by capitulum (text layer: running heads + `(Vers. N.)` tags; chapter ends by plate where marked)

`CAPITULUM N.` headings are full-measure and fall mid-page, so a chapter's last paragraphs share the next chapter's
opening page (plate p. 43: c. 1 ¶ 144 stands above `CAPITULUM II.`). First page = the page carrying the heading.

| Cap. | Pages | Last ¶ (text layer) | | Cap. | Pages | Last ¶ |
|---|---|---|---|---|---|---|
| I | 11–43 | 144 (v. 80) | | XIII | 336–358 | ~73–74 |
| II | 43–69 | **111** (corrected at manifest stage 1: ¶ 111 is an un-versed epilogue, 69R) | | XIV | 358–381 | **69** (corrected at manifest stage 4: ¶ 68 is Vers. 35, ¶ 69 closes on 381R; amended in this table at the p. 381 gate, ruling 89) |
| III | 69–88 | 63 (plate, 87R) | | XV | 381–402 | ~50+ |
| IV | 88–112 | 98 (v. 44 at ¶ 97) | | XVI | 402–425 | 61 |
| V | 112–134 | 85 (v. 39) | | XVII | 425–448 | 62 |
| VI | 134–165 | 109 | | XVIII | 448–472 | 66 |
| VII | 165–188 | 84 | | XIX | 472–501 | 75 |
| VIII | 188–216 | 98 | | XX | 501–520 | ~53 |
| IX | 216–252 | ~110–111 | | XXI | 520–540 | ~54+ |
| X | 252–277 | ~79 | | XXII | 540–565 | 84 |
| XI | 277–309 | 102 | | XXIII | 565–587 | ~71–72 |
| XII | 309–336 | ~87–88 | | XXIV | 587–604 | 66 |

Chapters run **18–37 pp, mean ~25.** **≈ 1,950 numbered paragraphs (PREDICTION; "~" rows are text-layer estimates,
the rest read off chapter-final pages), ≈ 3.3 per page.** 1,162 `(Vers. N.)` tags. The Luke band is ≈ 497K words
of text layer, apparatus included.

### `TABULA DIVISIONUM PRINCIPALIUM` (Prolegomena p. XVIII, read on the plate)

The editors' own outline of Bonaventure's division. Legend: *Evangelium S. Lucae, licet principaliter prosequatur
Christi sacerdotium et passionis remedium, dividitur in quatuor partes principales.* The editors note that only the
principal members are shown and that the rest stand in the margins of the text. Bracketed verse numbers are where
the Tabula's printed reference looks wrong against the body; **check on the plate before using either.**

- **Pars I. De incarnationis mysterio (c. 1–3).**
  - *nativitas in utero* (c. 1): de duplici fecundatione, Praecursoris (c. 1, 5) / Salvatoris (c. 1, 26); de
    gratiarum actione (c. 1, 30 [39]), pro conceptu Salvatoris / pro conceptu Praecursoris (c. 1, 56).
  - *nativitas ex utero* (c. 2): nativitatis Christi veritas; nascentis humilitas, factus sub Lege sacramentali /
    caeremoniali / morali.
  - *nativitas extra uterum* (c. 3): de baptismo et praedicatione Ioannis in generali; in speciali (c. 3, 10); in
    singulari (c. 3, 21), Christi regeneratio sacramentalis / genealogia temporalis (c. 3, 23).
- **Pars II. De praedicationis magisterio (c. 4–21).**
  - *Primo explicatur veritas doctrinae quadrupliciter* (c. 4 – 11, 13):
    - doctrinae Christi authenticatio: per meritum vitae in victoria tentationum; per testimonium Scripturae
      (c. 4, 14); per miraculum potentiae (c. 4, 31).
    - discipulorum vocatio (c. 5, 1): de statu iustitiae; de statu culpae (c. 5, 27).
    - vocatorum institutio (c. 6, 12): communis; specialis (c. 8, 1).
    - institutorum delegatio (c. 9, 1): missio Apostolorum; discipulorum (c. 10, 1), forma praedicandi / vivendi /
      orandi.
  - *Secundo confutatur falsitas Iudaeorum adversantium quadrupliciter* (c. 11, 14 – c. 21):
    - dolositas calumniantium miracula: ex parte causae efficientis; informatio discipulorum (c. 12, 1); ex parte
      temporis (c. 13, 21 [10]).
    - impietas (c. 15, 1): expressio impietatis Iudaicae; manifestatio pietatis divinae (c. 15, 3) per parabolam de
      perdita ove / drachma / patre ac duobus filiis; commendatio pietatis humanae (c. 16, 1).
    - curiositas duplex (c. 17, 20): in perscrutando; in possidendo (c. 18, 18), commendatur paupertas
      quadrupliciter, approbatur liberalitas dupliciter (c. 19, 11).
    - incredulitas (c. 19, 29): confutatur per facta; per verba et documenta (c. 20, 1), Pharisaei, Saducaei,
      informantur discipuli ad tria.
- **Pars III. De passionis medicamento (c. 22–23).** Quatuor antecedentia: machinatio proditoris; institutio
  Sacramenti altaris (c. 22, 7); eruditio discipulorum (c. 22, 24); devota supplicatio (c. 22, 39). Sex
  concomitantia (c. 22, 47).
- **Pars IV. De resurrectionis tropaeo (c. 24).** Revelatio; apparitio duorum discipulorum (c. 24, 13); certitudo
  (c. 24, 33); divulgatio (c. 24, 48).

## Structure signals (plates pp. 11, 13, 43, 252; counts from the text layer)

**The heading hierarchy, five tiers (MEASURED on plates):**

| Tier | Typography | Examples (page, column) |
|---|---|---|
| 0 | full-measure small caps; in-column small caps | `CAPITULUM I.` (11) · `PROLOGUS EVANGELISTAE.` (11) · `DIVISIO GENERALIS` (12R) |
| 1 | large roman, centred | `Pars. I. De incarnationis mysterio agitur tripliciter.` (13L) · `Pars II. De praedicationis magisterio agitur dupliciter.` (88L) |
| 2 | italic, centred | `Primo, de nativitate in utero dupliciter.` (13L) · `Secundo, de nativitate ex utero dupliciter.` (43, directly under `CAPITULUM II.`) · `Tertio, de nativitate extra uterum tripliciter.` (69L) |
| 3 | roman semi-bold, centred | `Primo, de duplici fecundatione.` (13L) · `Secundo, de gratiarum actione pro utraque conceptione.` (27R) · `Primo explicatur veritas doctrinae quadrupliciter.` (88R) · `Secundo determinatur discipulorum vocatio per duo.` (112L) · `Secundo confutatur falsitas Iudaeorum adversantium quadrupliciter.` (288L) |
| 4 | small bold, centred | `Tria dicuntur de conceptu praecursoris.` · `Primo describitur parentum conditio quadrupliciter.` (≈ 110–120 of these) |

- **These headings are the editors'.** The Corrigenda calls one of them "secunda nostra rubrica" (p. 252). They
  are the Tabula's members set into the column, plus a finer tier the Tabula omits.
- **Total headings ≈ 160–180 (PREDICTION).** Three text-layer detection passes returned 98 / 542 / 158 hits: the
  bold rubrics OCR badly ("desoribitar", "tiiplicitei"), footnote lines are mis-heighted as body, and whole tiers
  drop out. ⛔ The true inventory is a plate job; no count here is a denominator.
- **Between stacked headings stand UN-NUMBERED divisio paragraphs of Bonaventure's own text** ("Prima pars, quae
  prosequitur incarnationis mysterium, tres habet partes…"). On p. 13, ¶ 7 (begun under `DIVISIO GENERALIS` on
  p. 12R) continues across **five** headings before `8. (Vers. 5.)`. So a heading can fall INSIDE a numbered
  paragraph, and a section can open on un-numbered text.
- Elsewhere a pericope opens on a **numbered, un-versed divisio paragraph** of the form "lemma *etc.* Supra egit… /
  Postquam… / Terminata parte illa…" (c. 2 ¶ 1; c. 5 ¶¶ 1, 24, 40, 63, 75). These are Bonaventure's own joints.
- Marginalia: ordinals (*Primum. Secundum.*) and topic labels. Small-type verse set centred (the hymn on p. 43R).
- **No Quaestiones, no Scholion, no Schemata, no Explicit in the Luke commentary** (text layer; none on the plates
  read). The Ioannem's three special chunk types have no counterpart here.
- Paragraph numbers restart at each capitulum. Internal apparatus cites `supra n. 1`, `infra c. 11. n. 1`,
  `supra pag. 259, nota 8`, `tom. VI. pag. 266, nota 9` (≈ 301 `supra / infra n.` references).
- Running head `COMMENT. IN EVANGELIUM LUCAE C. N.`; Appendix `EXPOSITIO THRENORUM C. N.` and
  `EXPOSITIO ORATIONIS DOMINICAE.`

## `CORRIGENDA ET ADDENDA` (p. 858; read on full-resolution plate crops)

**Vol VII, 17 entries.** Sixteen fall in the Luke commentary, one in the Threni.

| Page, col., line | Printed | Corrected |
|---|---|---|
| 9, col. 2, l. 16 | comma after *David* | comma moves to after *naturalis* |
| 16, col. 2, notes l. 2 | *veritatis* | add *vel exigentiam veritatis* after it |
| 22, col. 1, l. 14 | *a Virgine et domo* | *a Virgine et Deo* (codd. C F G, and Bernard) |
| 23, col. 1, l. 2 from foot | *omnis viri ingressus … omnis viri aspectus* | *omnes … omnes* (Bede's original) |
| 95, col. 1, penult. | *prosequitur* | *persequitur* |
| 114, col. 2, notes l. 2 | *sesvet* | *servet* |
| 168, col. 1, l. 4 from foot | *dignitatem* | "melius" *indignitatem* |
| **252, col. 1, the second rubric** | *Prima pars* etc. | "sic reformanda est": *Prima pars, quae agit de forma praedicandi, tractat de missione comitantium discipulorum, de informatione euntium, de consolatione redeuntium.* |
| 294, col. 2, note 13 | *ubi cum Vulgata* | delete *cum Vulgata* |
| 300, col. 2, notes l. 5 | *suam* | *suum* |
| 320, col. 2, l. 18 | *insiderat* | *insederat* |
| 333, col. 2, ll. 15 and 17 | *exterioris iudicii* | *exterioris indicii* (twice) |
| 343, col. 2, l. 7 | *similiter* | *simul* |
| 346, col. 1, l. 16 | *Manducit* | *Manuducit* |
| 361, col. 2, note 13 | *nota 3* | *nota 13* |
| 533, col. 2, l. 11 | *poterunt* | *poterant* |
| 624, col. 2, note 9 (Threni) | — | add: *Tota ista expositio sumta est ex Bernardo, Serm. 93. de Diversis n. 2…* |

**Index rerum, 7 entries** (pp. 661, 690, 704, 711, 833, 834, 835). Out of scope: the index is not built.

**"IN PRAECEDENTI SEXTO VOLUMINE", 6 entries, each checked against the built and deployed `vol6/` chunks:**

| Vol VI site | Correction | State in `vol6/` |
|---|---|---|
| p. 220, col. 2, penult. | delete *sibi* before *sibilans* | **UNAPPLIED.** `bon-sap-c17.md` l. 89 reads "*spiritus* sibi *sibilans*". |
| p. 252, col. 1, l. 5 | "ante verba *in mundo erat*, quae sunt de textu Evangelii, incipiendus est numerus 25" | **UNAPPLIED.** `bon-ioan-c1-v9-14.md` has "unde in mundo erat per praesentiam" inside ¶ 24, with ¶ 25 beginning later at "(Vers. 10.). *In mundo erat*, per *effectum*". Moves a paragraph number and italicises a lemma; the chunk's `paragraphs:` range is unaffected. |
| p. 447, col. 2, l. 17 | *separatus extra* for *separatus. Extra* | **UNAPPLIED.** `bon-ioan-c15-v1-11.md` l. 53 "a vite separatus. Extra vineam proiicitur"; English l. 141 "separated from the vine. He is thrown outside the vineyard". Changes the English. |
| p. 501, col. 1, l. 2 | *Augustinus de hoc: « Non* | **UNAPPLIED.** `bon-ioan-c19-v28-37.md` l. 52 "Augustinus[^p501-1]: « De hoc non dicit *vulneravit*"; English l. 112. Moves a quotation boundary. |
| p. 551, col. 1, l. 14 | *inclucit* → *includit* | **Already flagged** in the `bon-cioan-*` chunk holding p. 551 as "[so printed: *inclucit* for *includit*]". Caught independently; now confirmed by the editors. |
| p. 573, col. 2, last line | *cogitationum* → *cogitationibus* | **UNAPPLIED.** `bon-cioan-c8.md` l. 39 "inter se invicem cogitationum accusantibus". |

**✅ APPLIED 2026-11-14, commit `b804dec` (rulings 8–9): all six rows, each read on its Vol VI plate first.** The "State" column above
is the state AS FOUND at scouting and is kept as the record. p. 551 lost its `[so printed]` bracket for the
corrigenda convention like the other five. Two of the Corrigenda's own column references are loose against the
plates (p. 551 *in-|clucit* stands at col. 2 ll. 13–14, not col. 1; p. 573 *cogitatio-|num* breaks across the
column foot), and p. 252 needed three decisions the entry does not spell out (verse tag moves with the number;
lemma capitalised at the paragraph head; the printed break before the second *In mundo erat* closed), all
recorded in each chunk's `## Notes`. Local only: live when Wilson next pushes and deploys.

**Five of six were unapplied in a deployed volume (as found).** And the wider finding: Vol V's raw has its own
`CORRIGENDA ET ADDENDA` leaf (`doctorisseraphic05bona_djvu.txt` L99769, ≈ 20 entries), and the Vol II / III / IV
raws each mention `CORRIGENDA` (1 / 2 / 2 hits). **The corpus has no corrigenda convention at all** (`CLAUDE.md`
has none). Proposal 9 in the scouting sheet.

## Mechanics (MEASURED)

- **Plates at 300 dpi**, the scan's native resolution. `tools/extract-pages.py --volume vol7 --dpi 300`.
- **Gutter:** the band is ≈ 62–63 px wide with a **6-px printed centre-rule ink island** in the middle of it
  (low-ink runs of 29 + 28 px either side). Gutter x moves by leaf: p. 11 → 1179/1180, p. 252 → 1299/1300, p. 604
  (irregular short last page) ≈ 1301–1304. `auto` split is required, never a fixed x. No meaningful skew on p. 252.
- `tools/gutter-profile.py` needs numpy: run it with `python3.11`, not `python3` (3.14 has no numpy). Arguments are
  positional, `<page> [row_lo] [row_hi] [volume]`: `python3.11 tools/gutter-profile.py 252 0.45 0.80 vol7`.
- **The raw does NOT carry footnote numerals.** p. 115: twelve notes, numerals OCR'd as `' ° * »`, two legible.
  Apparatus counts come from the plates, always.
- The scan is very clean in body type. Bold rubrics OCR badly; **never take a rubric's wording from the raw.**
- Text-layer geometry (`pdftotext -bbox-layout`, in points): body lines h ≈ 11; footnotes and small-bold rubrics
  h ≈ 9; marginalia h ≈ 7 at x < 40 or x > 520; left column x ≈ 44–273, right ≈ 290–520. Useful for locating
  paragraph starts and `(Vers. N.)` tags; useless for classifying headings.
- **Inbound citations (MEASURED):** ≈ 24 built chunks already cite this work (vol1 5 files, vol3 2, vol4 1, vol5 3,
  vol6 13), in the forms "Comment. in Lucam c. 9. v. 34", "c. 22, 19", "ad 18, 25", "17, 4", "IX, 28".
  `index/citations.tsv` has no class for it yet. **The cross-volume citation unit is chapter + verse; the
  in-volume and Index unit is page + paragraph, or c. + n.** (Ambrose's *Expositio in Lucam* is a different and
  heavily cited authority: do not let a resolver confuse them.)

## What the pilot has to decide (the proposals are in `lucam-pilot-scouting.md`)

1. **The chunk unit.** The index gives none; the capitulum is 18–37 pp. The body offers two kinds of joint: the
   editors' rubrics and Bonaventure's own divisio paragraphs.
2. **Whether the chunk boundaries are fixed once, up front** (a manifest), or found chunk by chunk at build.
3. **The front matter:** Prooemium, the *Prologus S. Hieronymi* (set in italic, unnumbered) and its expositio.
4. **How five tiers of editorial headings are rendered**, and what `paragraphs:` means when a heading falls inside
   a numbered paragraph.
5. **The Tabula divisionum:** not text of Bonaventure; whether it is used at all.
6. **The Appendix:** two works the editors themselves call *saltem dubia*. In scope or not.
7. **The Corrigenda:** a corpus-level convention, the 17 Vol VII entries, the 5 unapplied Vol VI sites, and the
   uninventoried leaves of Vols I–V.
8. **Register:** what carries from Vols V and VI, and the Luke-heavy terms (*pietas*, *misericordia*, *paupertas*,
   the *praedicatio* family, *magisterium*, *medicamentum*, *tropaeum*).
9. **Gates, deploy boundaries, and the size of the build** (a token-burn hard stop on its own).

## Traps (do not re-derive)

- ⛔ **300 dpi, not 450.** Every pixel figure carried from Vols V and VI is wrong here by a factor of 1.5.
- ⛔ **A page is not a chapter boundary.** `CAPITULUM N.` falls mid-page; the last paragraphs of the chapter before
  it are on the same plate, above it. Fix every span end positively on the plate (the standing rule).
- ⛔ **A numbered paragraph is not a section boundary.** Headings interrupt ¶ 7 of c. 1 five times.
- ⛔ **Do not trust the raw for a rubric, a footnote numeral, or a heading count.**
- ⛔ **The Tabula's verse references are the editors' and at least two look misprinted** (c. 1, 30 for 39;
  c. 13, 21 for 10). Read the body.
- ⚠ **The printed rubric on p. 252 is wrong by the editors' own Corrigenda.** A builder reading only the plate will
  transcribe the superseded wording. The Corrigenda table above has to reach the builder of each affected chunk.
- ⚠ The Threni's Cap. V is unlocated (see the work table). Do not write "five chapters" or "four chapters" anywhere
  until p. 651 is read.
- Everything in `vol6-pilot-setup.md` § Traps still binds (worn-digit folio misreads, blank-leaf ink percentages,
  the incremental-append discipline, never `git stash`).

---

# *LUCAM* PILOT (pp. 3–604) — RULINGS 1–16 (Wilson, 2026-11-14; "All as recommended")

Binding summary. Evidence, alternatives and their costs: `manual-review/lucam-pilot-scouting.md` § PROPOSED RULINGS
1–16 (the proposal text there is the ruling text; nothing was amended).

- **1. Chunk unit = Bonaventure's own pericope, bounded by joints the print marks.** (a) Never across a
  `CAPITULUM` heading; `division:` = the capitulum. (b) Every boundary is an editorial heading, or, where headings
  stand more than ~8 pp apart, one of Bonaventure's divisio paragraphs. (c) Not every rubric is a boundary: sibling
  rubric sections stay together up to **3–6 pp, cap 8, one-pass build to 10**; a stacked heading cascade opens one
  chunk. (d) **A boundary always falls at the START of a numbered paragraph** (or at a heading standing between
  paragraphs), never inside one. (e) id `bon-luc-c{N}-v{a}-{b}`, `verses: "a-b"`, `type: pericope`,
  `paragraphs: "40-70"`. Refused: the capitulum; every rubric a chunk; verse-pericopes of our own.
- **2. The chunk manifest is drawn BEFORE the build, in stages, and is the build's only source of spans.**
  `manual-review/lucam-chunk-manifest.tsv`, one row per chunk, a plate crop read at every boundary. Stage 1 =
  Cap. I–III before any chunk; thereafter complete through the NEXT gate before that interval's first chunk. A
  builder who finds a row wrong on the plate STOPS and reports; the manifest is amended in its own commit.
- **3. Front matter = two chunks, division 0:** `bon-luc-prooem` (section 1, `type: prooemium`, pp. 3–7) and
  `bon-luc-prol` (section 2, `type: expositio`, pp. 7–10: the *Prologus S. Hieronymi* transcribed and translated
  as text, italic as printed, + the expositio ¶¶ 1–11). **[Two facts corrected on the plates at manifest stage 1,
  2026-11-14; the ruling itself stands: the chunk runs pp. 7–11 (expositio ¶ 11 crosses the top of p. 11, above the
  display stack), and the Prologus is printed in ROMAN, a smaller face, not italic, so "as printed" means roman.]** The p. 11 display stack, `CAPITULUM I.` and `PROLOGUS
  EVANGELISTAE.` go to `bon-luc-c1-v1-4`.
- **4. Headings: all five tiers transcribed in place, both languages, with their typography; editorial, said once
  in each chunk's Notes.** `CAPITULUM N.` → `### Capitulum N.`; tiers 1–4 → `####`, italic kept for tier 2; the
  size/weight difference among tiers 1, 3, 4 is accepted as flattened. No `pars:` field; breadcrumb `Cap. N, Vers.
  a-b`. `title_la` = the governing rubric **as amended by the Corrigenda**, else the lemma + Bonaventure's dividing
  words.
- **5. `paragraphs:` = the numbered paragraphs that BEGIN in the chunk;** numbers verbatim at paragraph heads in
  both languages; un-numbered divisio text between headings is transcribed where it stands and belongs to the
  paragraph it continues.
- **6. The `TABULA DIVISIONUM PRINCIPALIUM` is NOT a chunk.** Manifest skeleton and gate positions only. (An
  English outline on the work's landing page is a later, optional call; not ruled.)
- **7. The Appendix is IN SCOPE, AFTER Luke closes,** as two separate small works (*Expositio Threnorum*,
  *Expositio Orationis Dominicae*), each labelled as the editors label it (*saltem dubia*), each with its own
  registry entry and its own short scouting sheet when it comes up. Nothing about their chunking is ruled.
- **8. CORRIGENDA CONVENTION (corpus-level). Quaracchi's own Corrigenda are the edition's text.** The Latin
  carries the corrected reading; the English translates the corrected reading; **one numbered translator's note,
  anchored at the word,** records the printed reading and the source ("Printed: … ; corrected by the editors,
  Corrigenda, t. VII p. 858."). Addenda to the apparatus are added to the note they extend, marked the same way.
  `[so printed: …]` stays the mark for a misprint WE caught and the editors did not. The 16 Luke entries are
  applied at build; the manifest names them per chunk.
- **9. The five unapplied Vol VI corrigenda are fixed now, as one bounded job** (`bon-sap-c17`,
  `bon-ioan-c1-v9-14`, `bon-ioan-c15-v1-11`, `bon-ioan-c19-v28-37`, `bon-cioan-c8`; + the p. 551 note updated from
  bracket to confirmed corrigendum). Each site read on its plate first. Local commit; live with the next deploy
  Wilson calls; no deploy asked on their account.
- **10. Vols I–V: INVENTORY the Corrigenda leaves, apply nothing.** One short Sonnet-shaped session →
  `manual-review/corrigenda-inventory.md` (applied / unapplied per entry). Queued behind the Luke manifest.
  Applying is a later ruling.
- **11. Register carried unchanged from Vols V and VI** (the list in the scouting sheet's proposal 11), and
  **Luke takes the Ioannem's spellings** (Vol VI ruling 155's per-work scope).
- **12. Register new to Luke, adopted as the working register; reviewed at the shakedown gate with sites in
  view.** The six mercy nouns stay six words (*misericordia* mercy · *pietas* piety · *benignitas* kindness ·
  *clementia* clemency · *compassio* compassion · *miseratio* "commiseration" in Bonaventure's own prose, the
  Douay's wording inside a quotation). ⭐ ***pietas divina* in cc. 15–16: the "piety" rule HOLDS, with `tr-pietas`
  at the first site of each chunk where the *pietas* is God's; reviewed with sites in view at the p. 381 gate.**
  *praedicare* preach / *praedicatio* preaching / *praedicator* preacher, never "proclaim"; ~~*evangelizare* → the
  Douay's "preach the gospel".~~ **[AMENDED by ruling 18, p. 27 gate, 2026-11-14: *evangelizare* → "preach the
  gospel", never bare "preach"; the Douay's "bring good tidings" stands where the Douay has it (1:19, 2:10), with
  `tr-evangelizare`. The struck sentence is kept visible.]** **[p. 88 gate: the "where the Douay has it" clause is AMENDED by ruling 29 (OT verses
  included); ruling 30 adds: *praeconium* → "proclamation", the only home of "proclaim / proclamation";
  *praeco* → "herald". Ruling 31 reads the *pietas divina* sentence work-wide.]** *magisterium* → "teaching office". *Praeceptor* → "Master" + `tr-praeceptor` at
  5:5. *paupertas* poverty · *mendicus* beggar · *mendicitas* beggary · *eleemosyna* alms · *avaritia* avarice ·
  *liberalitas* liberality. *remedium* remedy / *medicamentum* medicine · *tropaeum* trophy · *mysterium* mystery
  / *sacramentum* sacrament. *informatio*, *informare* → "formation", "to form". Sense labels: Morally,
  Spiritually, mystically, allegorically, "according to the letter". *publicanus* publican · *legisperitus*
  lawyer · *sacerdos* priest. The canticles keep their Latin incipits as names. **Title: "Commentary on the
  Gospel of Luke".**
- **13. Registry and ids:** slug `lucam`, prefix `bon-luc-`, **book 19**, tome 7, initial "L",
  `divisionLabel: "Capitula"`, divisions `0: Prooemium`, `1..24: Capitulum N`; title builder's `ioannem` branch
  takes `lucam`; a citation class for "Comment. in Lucam c. N. v. M". Goes in with `bon-luc-prooem`, not before.
- **14. EIGHT gates:** shakedown **p. 27** · **p. 88** (Pars I closes) · **p. 188** (close of c. 7) · **p. 288**
  (c. 11 v. 13) · **p. 381** (close of c. 14; the *pietas* review) · **p. 472** (close of c. 18) · **p. 540**
  (Pars II closes) · **work close p. 604**. Every gate runs on Wilson's go, never as a side effect of the loop.
  **ONE deploy by default, at p. 604; every gate is a legitimate deploy boundary Wilson may call, per action.**
  The recommendation to call **p. 88** (Luke 1–3 live for Advent) stands on the record; **the deploy itself is
  still asked for, on its own, when the p. 88 gate closes.**
- **15. Build cadence:** one Opus agent per chunk, incremental-append, the Vol VI session loop unchanged; plates
  at 300 dpi; apparatus counted from the plates. ⛔ **The burn is NOT approved by this ruling.** "Which model, and
  go?" is asked, with the figure restated for the interval, before `bon-luc-prooem` is dispatched. **[Cadence note, Wilson 2026-11-14 (p. 27 gate session): one Opus agent per chunk,
  SEQUENTIALLY; a parallel pilot was proposed and declined. See the note after ruling 26.]**
- **16. Manifest stage 1 (Cap. I–III + the two division-0 rows) is the next job, drawn on Opus;** low-confidence
  rows flagged for Wilson or a Fable look at the shakedown gate.

### MANIFEST STAGE 1 — DRAWN 2026-11-14 (`lucam-chunk-manifest.tsv`, 22 rows; notes in `lucam-chunk-manifest-notes.md`)

Read on 35 plate crops, one at every boundary. **Corrections to this sheet and to the scouting sheet, all MEASURED:**

- Prooemium = ¶¶ 1–24 (not ≈ 27). `bon-luc-prol` = pp. 7–**11**. The *Prologus S. Hieronymi* is in **roman**
  (re-read by the coordinator on the p. 7 plate), and its heading carries footnote anchor 2; `DIVISIO GENERALIS`
  carries anchor 8. Anchored headings do occur in this work.
- Last paragraph per capitulum: **I = 144, II = 111, III = 63.** `Pars II.` stands BELOW `CAPITULUM IV.` on p. 88
  and belongs to c. 4.
- c. 1: the 17R rubric stands above ¶ 29, so the chunks are ¶¶ 7–28 and 29–39.
- Tabula divisionum: "c. 1, 30" is a misprint for v. 39, and "c. 1, 56" is one off (the body has v. 57).
- The text layer misses every tier-3 heading in Cap. II–III; builders count headings on the plate.

**The shakedown interval (gate p. 27) is SIX chunks:** `bon-luc-prooem` (3–7) · `bon-luc-prol` (7–11) ·
`bon-luc-c1-v1-4` (11–12) · `bon-luc-c1-v5-17` (12–17) · `bon-luc-c1-v18-25` (17–20) · `bon-luc-c1-v26-38` (20–27).

**Two readings fixed by the coordinator (Fable) under the rulings as given, no new ruling:**

- **[RESTATED by ruling 22, p. 27 gate: `title_la` = the LOWEST heading of the opening stack, whole (*Ioannem*
  ruling 79(b)), whatever its scope; the wording that follows is superseded and kept for the record.]**
  **`title_la` under ruling 4 ("the governing rubric")** = the most specific heading in the chunk's opening
  cascade whose scope covers the WHOLE chunk; where no heading stands (c. 2 vv. 25–39), the lemma + Bonaventure's
  dividing words. This is how the manifest is drawn.
- **The two `low` rows, `bon-luc-c2-v25-35` / `bon-luc-c2-v36-39` (pp. 58–65, no in-column heading; the editors'
  divisions stand in the margin):** the cut at **¶ 81** (Anna, 62R) is kept. It is the higher-order joint, Simeon
  and Anna are the two witnesses the passage itself divides into, and the pieces are 4.4 + 2.7 pp. The marginal
  labels go to the Marginalia list in `## Notes` (standing convention), not into the body. The rows stay `low`
  in the TSV until their builder has read pp. 58–65 on the plates; Wilson may overrule at the p. 88 gate.

# *LUCAM* SHAKEDOWN GATE (p. 27) — RULINGS 17–26 (Wilson, 2026-11-14; "Approve all")

Binding summary. Docket items 1–10 of `manual-review/vol7-lucam-shakedown-gate-evidence-sheet.md` (each ⭐
recommendation taken) became rulings 17–26; the evidence, censuses and alternatives are there, by item number, and
are not repeated. Gate record: `manual-review/vol7-lucam-shakedown-gate.md`. Mechanical passes:
`manual-review/vol7-lucam-shakedown-gate-passes-draft.md`. **No Latin line changed.**

- **17. Ruling 12 is RATIFIED as the Luke register at every site, and the carried rulings bind over it** (sheet
  § 1). A builder renders: ***eruditio* → "erudition" everywhere** (ruling 11 carrying Vol VI ruling 93; it must
  stay off *instructio* "instruction"); **"Holy Spirit" everywhere, Douay quotations included** (Vol VI ruling
  80(b)); ***intelligentia* → "intelligence" in body prose** (ruling 11, *septem donis*), wherever *intellectus*
  stands in the chunk, not only in the sentence. *documentum*: plural *documenta* "lessons", singular "instruction",
  ratified by number. Applied: `prooem` ¶ 17, `c1-v5-17` ¶ 7 ("teaching office of erudition"); `prooem` ¶ 18
  (Acts 10:38 "Holy Spirit"); `prooem` ¶ 24 ("general intelligence"). Doc: `c1-v18-25`'s claim that III Kings
  1:42 "bringest good tidings" is the Douay's is corrected (Douay: "good news"; the adjustment is licensed by ruling
  93 because ¶ 31 leans on *bona nuntiatio*).
- **18. *evangelizare* (amends ruling 12's sentence; sheet § 2).** Ruling 12 now reads: ***evangelizare* → "preach
  the gospel", never bare "preach"** (the Douay's bare "preach" at 3:18, 4:43, 16:16 is adjusted, so the word stays
  off *praedicare*); ~~**where the Douay itself says "bring good tidings" (1:19, 2:10: an angel bringing a message,
  with an object), the Douay stands, with `tr-evangelizare` at each chunk's first site.**~~ **[AMENDED by ruling 29,
  p. 88 gate, 2026-11-14: "where the Douay itself says 'bring / preach good tidings' (Luke 1:19, 2:10; Ps. 67:12,
  Isa. 40:9, Nah. 1:15), the Douay stands, with `tr-evangelizare` at each chunk's first site; an echo of such a verse
  follows it." The struck clause is kept visible.]** 8:1 *praedicans et
  evangelizans* keeps the Douay's "preaching and evangelizing". Both *bona nuntiatio* renderings stand ("good
  announcement" where the gloss hangs on *annuntiare*, prooem ¶ 14; "good tidings" where it hangs on
  *evangelizare*, `c1-v18-25` ¶ 31). `c1-v18-25` ratified as built, 0 lines; the prooem Notes' claim that 4:43
  "preach the gospel" is the Douay's wording is corrected. **(Passive form added by ruling 101, p. 472 gate: *regnum
  Dei evangelizatur* (Luke 16:16) "is preached as gospel".)**
- **19. *verecundia* (sheet § 3).** ***verecundia* → "shamefastness", *verecundus* → "shamefast", for the whole
  work** (the Hexaemeron's *modestia, verecundia* precedent; `c1-v26-38` ¶¶ 50–51 as built). ***pudicitia* →
  "purity"** (the QPE rendering). So *modestia* alone takes "modest(y)", and *pudor* "shame". Applied:
  `c1-v18-25` ¶ 35, ¶ 38 ("the shamefast concealment"; "of humility and of purity"), p. 20 n. 3 ("shamefastness or
  shame").
- **20. Ps. 118:173 *Fiat manus tua* → "Let thy hand be done" RATIFIED** (sheet § 4; `c1-v26-38` ¶ 69, p. 26
  n. 7). Vol VI ruling 93's test applies: where the exposition leans on the word, the Douay is adjusted to it,
  **silently in the English and disclosed in the chunk's `## Notes`**; no `tr-` note and no bracket for a Douay
  adjustment (`[so printed]` stays for misprints).
- **21. *praedicabilis* and Cant. 6:8 (sheet § 5).** *praedicabilis* keeps **"worthy to be preached"** (ruling 12's
  family). **Cant. 6:8 *beatissimam praedicaverunt* → "preached her most blessed"** (Douay "declared" adjusted,
  ruling 93: ¶ 49 proves ¶ 46's *praedicabilis* from it). Applied: `c1-v26-38` ¶ 49. The ten other banked items
  (sheet § 5b) need no text edit and stand as recorded.
- **22. `title_la` = the LOWEST heading of the opening stack, whole** (*Ioannem* ruling 79(b) applied to Luke;
  sheet § 6), even where its scope over- or under-covers the chunk; a sentence title (lemma + dividing words) only
  where no heading stands. `c1-v18-25` kept as built. The stage-1 coordinator's gloss ("whose scope covers the
  WHOLE chunk", § MANIFEST STAGE 1 above, and `lucam-chunk-manifest-notes.md`) is restated to this; no stage-1
  title changes. Governs `c1-v46-56` and every later two-sibling row.
- **23. A Corrigenda addendum inside an apparatus note keeps ruling 8's shape** (sheet § 7): the corrected Latin
  in the note, and `tr-corrigenda[-N]` anchored at the word inside the note's **En**. It renders (code path read
  end to end). **One browser look at the next local preview is owed** (`bon-luc-c1-v5-17`, p. 16 n. 8, click
  "tr."). ~5 more uses are coming (pp. 114, 294, 300, 361; Threni p. 624).
- **24. Ruling 13's citation class = the INBOUND "Comment. in Luc." class, keyed CHAPTER + VERSE** (sheet § 8):
  `Comment.? in Luc(am)?` + `c.`/roman/bare chapter + verse (`ad` allowed), resolving to the chunk whose `verses:`
  holds the verse (`forward` until built); the one `c. 6. n. 20` site resolves by `paragraphs:`; other authors'
  "in Luc." excluded by the `governed_by_author` guard; the page+note branch fixed to break a shared page by its
  note (`pag. 7, nota 5` → `bon-luc-prol`). ~22 sites in Vols I–VI, today filed as Gospel verses at confidence A.
  **No in-work `supra n. N` class yet** (waits with the *Ioannem*'s identical docket item, ruling 82(a)). **A TOOL
  JOB, run after the gate and separately; 0 text lines. QUEUED, not run at this close.**
- **25. `TOMES[7]` = `{ title: "Book VII: Commentarius in Evangelium S. Lucae", initial: "7" }`** (the title-page
  wording; sheet § 9). Added to `site/scripts/build-content.mjs` at this close. Live only with whatever deploy
  Wilson calls.
- **26. The ¶ 81 cut between `bon-luc-c2-v25-35` and `bon-luc-c2-v36-39` is KEPT** (sheet § 10; read on the p. 62
  plate: ¶ 81 opens at the head of 62R, ¶ 80 closes at 62L's foot, marginale *De testimonio Annae*). The rows stay
  `low` until their builder reads pp. 58–65, then are promoted to `high`.

**Cadence note under ruling 15 (Wilson, this session, 2026-11-14):** the build continues **one Opus agent per chunk,
SEQUENTIALLY**. A parallel pilot was proposed and **declined**; do not re-propose it as a default.

### MANIFEST STAGE 2 — DRAWN 2026-11-14 (Cap. IV–VII, pp. 88–188; 19 rows appended to `lucam-chunk-manifest.tsv`; notes in `lucam-chunk-manifest-notes.md` § Stage 2)

Rows per capitulum: **IV 5 · V 4 · VI 6 · VII 4**. Every boundary and every heading candidate was read on a 300 dpi
crop. The candidates came from a centred-line screen over the plates of pp. 88–188, checked against stage 1's
known headings. The p. 188 gate interval is these 19 chunks, `bon-luc-c4-v1-13` through `bon-luc-c7-v36-50`.

**Corrections made by stage 2 (all MEASURED):**

- **Cap. VI's last ¶ is 111, not 109** (165R). Last ¶ of the other three as predicted: **IV = 98, V = 85, VII =
  84**. Each capitulum's first and last pages are as predicted, and **none overran.**
- **Cap. V is 4 chunks, not the scouting sheet's 5.** Its ¶ 75 cut is unlicensed (the 128R heading and
  `CAPITULUM VI.` stand ~5.9 pp apart), so ¶¶ 63–85 is one row. The ¶ 24 and ¶ 40 cuts hold (no heading; marginalia).
- **No heading stands under `CAPITULUM VI.`** The 140R t3 *Tertio determinatur vocatorum instructio per duo.*
  stands ABOVE ¶ 24 and is missed by the text layer.
- **The c. 7 verse joint is v. 16 / 17:** ¶ 33's lemma *Et exiit hic sermo* is v. 17. **c. 4 v. 22 is shared**
  by two rows (¶¶ 46 and 48 are both tagged Vers. 22).
- The headings in cc. 5–6 stand 16 pp and 25 pp apart, so those rows are cut at Bonaventure's divisio paragraphs
  (ruling 1b). Each cut is named in a higher paragraph's own division.

**Corrigenda:**

- p. 95 → `c4-v1-13`.
- p. 114 → `c5-v1-11`.
- p. 168 → `c7-v1-16`.

**`low` rows (5).** The alternatives for each are in the notes.

- `c4-v31-37` / `c4-v38-44`: the ¶ 79 cut of an ~8.1 pp member. Alternatives: ¶ 87, or no cut.
- `c5-v1-11`: kept whole at ~6.4 pp. Alternative: ¶ 9, giving 2.7 + 3.7.
- `c6-v27-31` / `c6-v32-38`: the ¶ 77 cut of a ~7.5 pp member.
- `c7-v1-16`: kept whole at ~7.6 pp over 9 printed pp. The ¶ 20 cut, between the two miracles, is unlicensed
  because the headings stand ~7.6 pp apart, under 8.

**One title needs a word from Wilson.** Under ruling 22, `c6-v1-11` takes a sentence title, because no heading
stands under the capitulum.

# *LUCAM* p. 88 GATE — RULINGS 27–40 (Wilson, 2026-11-14; "approve all")

Binding summary. Docket items 1–12 of `manual-review/vol7-lucam-p88-gate-evidence-sheet.md` (each ⭐ recommendation
taken) became rulings 27–38; items 13–14 were the coordinator's (manifest stage 2) and became rulings 39–40. The
evidence, censuses and alternatives are in the sheet, by § number, and are not repeated. Gate record:
`manual-review/vol7-lucam-p88-gate.md`. Mechanical passes: `manual-review/vol7-lucam-p88-gate-passes-draft.md`.
**Two English lines changed (`c3-v23-38` ¶ 63, `c1-v18-25` ¶ 38) + one manifest cell; no Latin line changed.**

- **27. The conspicuous ruling-20 Douay departures are RATIFIED as built** (sheet § 1): Luke 2:32 "A lumen to the
  revelation of the Gentiles" + `tr-lumen` (`c2-v25-35` ¶ 71); Luke 2:25 *timoratus* "God-fearing"; Isa. 52:7
  *annuntiantis* "him that announceth … that announceth good things" (`c3-v15-20` ¶ 44); the *complacere* triad kept
  apart (Matt. 3:17 "well pleased to myself" / Mark 1:11 / Luke 3:22 "it hath well pleased me"; Col. 1:19 without "the
  Father"; `c3-v21-22` ¶¶ 55–56); Prov. 31:28 "preached her most blessed" (`c1-v46-56` ¶ 91). **A builder applies
  ruling 20 to famous and liturgical verses exactly as to any other:** if the exposition leans on Bonaventure's word,
  the Douay is adjusted; there is **no canticle exception** (the *Magnificat*, *Benedictus* and *Nunc dimittis* are
  expounded verse by verse). The Vol V *lumen* test (verse quoted AS A verse and no body prose leaning) decides the
  *lumen* exemption.
- **28. One verse or proposition may take two renderings at two sites; the splits are KEPT** (sheet § 2): Luke 2:19
  "pondering" (`c2-v15-20` ¶ 40) / 2:51 "Conferring" (`c2-v40-52` ¶ 109, the Gal. 2:2 *contuli* chain); v. 54 *puerum*
  "child" (`c1-v46-56` ¶ 99) / v. 69 *pueri* "servant" (`c1-v67-80` ¶ 124); Col. 1:13 "dilection" (`c3-v21-22` ¶ 55) /
  "love" (`c3-v23-38` ¶ 63). Ruling 20 produces these by design; each split is disclosed in its chunk's Notes.
  **Separately, the Douay base follows Quaracchi's actual wording where the two differ, even where nothing leans:**
  applied at `c3-v23-38` ¶ 63, Col. 1:13 *filii dilectionis* (no *suae*) "the Son of his love" → **"the Son of love"**
  (1 line).
- **29. *evangelizare* in the Old Testament (AMENDS ruling 18's clause; sheet § 3).** Ruling 18's clause now reads:
  **where the Douay itself says "bring / preach good tidings" (Luke 1:19, 2:10; Ps. 67:12, Isa. 40:9, Nah. 1:15), the
  Douay stands, with `tr-evangelizare` at each chunk's first site; an echo of such a verse (Bede, p. 50 n. 12) follows
  it.** The rest of ruling 18 stands: *evangelizare* → "preach the gospel", never bare "preach". Isa. 40:9 (`c1-v39-45`
  ¶ 77) ratified as built. The *annuntiare* verses take ruling 12's "announce", inside quotations too: Isa. 52:7
  "him that announceth", Isa. 61:1 *ad annuntiandum* "to announce" (`c3-v1-9` ¶ 7). ⚠ Forward: Luke 4:18 quotes
  Isa. 61:1 as *evangelizare pauperibus* → "to preach the gospel to the poor", beside "announce" at Isa. 61:1; that
  is correct as ruled.
- **30. *praeconium* → "proclamation" (WRITTEN INTO ruling 12; sheet § 4).** "Proclaim / proclamation" belongs to
  ***praeconium*** alone in this translation; ***praeco*** → "herald"; ***praedicare*** is never "proclaim" (ruling 12,
  unchanged). 15 sites ratified as built (all "proclamation"; zero "proclaim" in the 22 chunks).
- **31. `tr-pietas` goes at the first site of ANY chunk where the *pietas* is God's, work-wide** (sheet § 5; ruling
  12's cc. 15–16 sentence is read work-wide). `c1-v46-56` ¶ 93 and `c2-v25-35` ¶ 69 ratified. Human *pietas* takes
  "piety" with no note. **The p. 381 gate still reviews the rule itself** with the cc. 15–16 sites in view.
- **32. The new house renderings are RATIFIED as a batch** (sheet § 6). Builders apply this table; the Douay's own
  wording stands inside a quotation wherever ruling 20 does not adjust it:

  | Latin | English |
  |---|---|
  | *poenitentia*, *poenitere* | "penance", "do penance" |
  | *vacare* (with dative) | "free for" + `tr-vacare` at each chunk's first site; never "rest"; *vacare a* "free from"; absolute *vacare* "to be free" (`c10-v38-42` ¶ 67); `tr-vacare` reaches an apparatus verse where the note's own sentence leans (Ps. 45:11 "Be free, and see", as Vol VI) (**clauses added by ruling 68**, p. 288 gate) |
  | *quies* (noun), *requies* | "rest"; *requiescere* "rest"; *quietus* "quiet" |
  | *lumen* in Bonaventure's prose (the angelic *lumen*) | "lumen" + `tr-lumen` (Vol V *lux* / *lumen* rule); *lux* "light" |
  | *claritas* | the Douay's word at the verse ("brightness" at Luke 2:9; "glory" in Wis., II Cor. 3:18) |
  | *clarificatio* | "glorification" (shares its root with *glorificare* "glorify"; recorded, not a defect) |
  | *timoratus* | "God-fearing" |
  | *corripere* / *correptio* · *arguere* | "correct" / "correction" · "reprove"; scope: *arguere* the logical act (*potest ex hoc argui*) "argue" (`c7-v1-16` ¶ 13, `c12-v13-34` ¶ 36, `c20-v27-40` ¶ 42) (**added by ruling 113**, p. 540 gate) |
  | *erudire* (body prose) · *eruditor* · *eruditio* | "school" ("we are schooled") · "schoolmaster" · "erudition" (ruling 17) |
  | *instruere* · *instructio* · *docere* | "instruct" · "instruction(s)" · "teach" |
  | *documentum* · *documenta* | "instruction" · "lessons" (ruling 17) |
  | *largitas* · *liberalitas* | "largess" · "liberality" |
  | *benedictus* · *beatus* · *beatitudo* | "blessed" · "blessed" · "beatitude" |
  | *admirabilis* · *mirabilis* · *mirari* | "wonderful" · "marvellous" · "wonder" (into quotations too) |
  | *cohortatio* / *exhortatio* · *comminatio* / *increpatio* / *admonitio* | split by prefix · "threatening" / "rebuke" / "admonition" |
  | *praeceptum* · *consilium* · *mandatum* | "precept" · "counsel" · "commandment" (*decem praeceptis* ruling) |
  | *purgatio* · *purificatio* | "purgation" · "purification" |
  | *ortus* · *partus* · *nativitas* | "birth" · "bringing forth" (or "offspring" where it is the child) · "nativity"; scope: *ortus* "birth" also of faith (`c17-v5-10`) and of man under the figure of a tree (`c21-v28-38` ¶ 50); the sun's *ortus* and *ortum habere* "rising / take its rise" (**added by ruling 115**, p. 540 gate) |
  | *cultus* | "worship"; scope: *cultus* (of God) "worship"; *cultus vestium / corporis* "adornment" (`c2-v1-7`); of the soil "tillage"; *cultor* "worshipper" or the Douay's word at a verse ("husbandman" Luke 20:10, "dresser" Luke 13:7), and *cultura* "worship" / "cultivation", by sense (**added by ruling 112**, p. 540 gate) |
  | *exsultare* | "exult" (Douay "rejoice" adjusted) |
  | *divulgare* · *profiteri* · *egenus* · *dominatrix* · *comprehendere* · *eventus* | "spread abroad" · "profess" · "needy" · "mistress" · "lay hold of" · "proceeds" |
  | *baptismus fluminis, flaminis, sanguinis* | Vol IV house rendering |
  | *femina est vir occasionatus* | "woman is a misbegotten man" (reported formula; not softened) |
  | *status* · *situs* (¶ 61's seven differences) | "stopping-place" · "position" |
  | *intellectus* · *intelligentia*; *in intellectu … in affectu* | "understanding" · "intelligence"; "in the intellect … in the affection" (ruling 17; Vol VI ruling 101); scope: the locative formula *in intellectu … in affectu* (and the faculty named so) "intellect"; elsewhere *intellectus* "understanding" even beside *affectus*, an echo of a Douay verse following the verse (**added by ruling 97**, p. 472 gate) |
  | *benignitas* · *benignus* | "kindness" · "kind", into quotations too (**added by ruling 45**, p. 188 gate) |
  | *caritas* | "charity", into quotations too (**added by ruling 52**) |
  | *curare* / *curatio* · *sanare* / *sanatio* | "cure" · "heal" / "healing" in Bonaventure's prose; the Douay's "heal" in a verse where nothing leans; an echo of the lemma follows it (**added by ruling 53**) |
  | *credulitas* · *incredulitas* | "belief" · "unbelief" (**added by ruling 55**) |
  | *redarguere* | "convict" (beside *arguere* "reprove") (**added by ruling 56**) |
  | *otium* | "leisure" (kept off *vacatio*) (**added by ruling 57**) |
  | *excessus* | mental / contemplative sense (*mentis, contemplationis, admirationis excessus*, *in excessum*) "transport", the Itinerarium register; measure exceeded "excess" (Vol VI practice; Luke 9:31 at `c9-v28-31` ¶ 54, where Bonaventure reads the word so, `tr-excessus` at the chunk's first site); a death named *excessus vitae* "departure from life" (**added by ruling 67**, p. 288 gate); the adjective *excessivus* follows the noun's sense: mental / contemplative (mystical theology, *excessiva contemplatio*) "transporting" (`c13-v18-21` ¶ 46; Vol V *Sermones*); measure "excessive", including a desire Bonaventure glosses by *nimietas* (`c9-v32-36` ¶ 61) (**added by ruling 81**, p. 381 gate) |

  Applied: `c1-v18-25` ¶ 38 *erudimur* "we are taught" → **"we are schooled"** (1 line).
- **33. `title_la`: every title RATIFIED as built** (sheet § 7). **The sentence title (lemma + dividing words,
  `c2-v25-35`, `c2-v36-39`) is the precedent for every later heading-less span** (see ruling 40). Ruling 22 is
  applied as written: the opening stack is one stack and the lowest heading is taken (`c2-v1-7`, `c3-v1-9`,
  `c3-v10-14`, `c3-v21-22`). Applied (doc): the `bon-luc-c2-v21-24` manifest `title_la` / `title_la_source` cells
  corrected from the 54L t3 to the 54R t4 *Qualiter factus sit sub lege sacramentali.* (`rubric-t4 p.54R`), as built.
- **34. The two builder edits of the manifest's `confidence` cell (`c2-v25-35`, `c2-v36-39`, `low` → `high`) are
  RATIFIED as ruling 26 carried out** (sheet § 8). **Standing rule: a builder may change only its own row's
  `confidence` cell, and only when a ruling names that edit; every other manifest change goes through a gate** (or
  its own commit after a STOP, ruling 2).
- **35. The work's NAMES POLICY** (sheet § 9): biblical proper names in the English take **the Douay's spelling at
  the verse**; the Latin keeps **Quaracchi's form**; a name cited AS A WORD (etymology, variant, *nomen*) stays
  **Latin and italic in both**. Luke's named persons keep the *Ioannem*'s spellings (ruling 11). Applies to Cap. IV
  (the temptation) and Cap. VI (the Twelve) next. **(Clarified by ruling 54: the Douay governs the spelling of the name Quaracchi prints; where Quaracchi prints a different name form, e.g. *Abraham* for *Abram*, ruling 28 keeps Quaracchi's.)**
- **36. The records, misprints and banked evidence (G38–G39, G41–G49) are RATIFIED as recorded** (sheet § 10). No
  text edit. Quaracchi slips transcribed as printed; `[so printed]` only for misprints we caught; the collection-change
  bank (G45–G46) asks no ruling and none is made.
- **37. ONE bounded tool job, after the gate, QUEUED, NOT RUN** (sheet § 11). Scope: **T1** (the "Esth. 98" guard)
  · **T3, T8** (file as Quaracchi printed slips, r.57 class) · **T4** (unresolvable-with-reason, not a wrong `chunk`)
  · **T6** (ruling 24's break-a-shared-page-by-its-note fix for every `pag. N, nota M`; 11 sites) · **T7** (let
  `S. Bonav.` through the author guard for the work's own author) · **T9** (parenthetical page after a named Vol V
  work resolves in Vol V) · **T10** (stop the anaphor pass at a note boundary) · **T11** (*Ecclesiastae N* and comma
  body ordinals) · **T13** (roman `d.`) · **T12 + `bon-sent-IV-d21-p1-a1-q2` n. 8**, the two own-commentary
  *Exposit. in Luc.* inbounds, through an **explicit two-row site table, NOT a wider `LUC_RE`** (the row for
  `bon-ioan-c3-v13-16` p. 283 n. 2 says it lands on an apparatus variant, p. 83 n. 3; the reciprocal p. 83 n. 3 →
  p. 283 n. 2 resolves under T6). **T5 stays deferred** (ruling 24 / *Ioannem* 82(a)); the job only counts it.
  **T2 closes** (never recurred). Report → fix → report, a before/after table per site; `tools/build-citations.py`
  (+ the site table) only, then `build-citations.py` → `build-index-json.py`. No chunk file, no
  `tools/authorities.json`.
- **38. The p. 88 deploy: preconditions RECORDED, no recommendation either way** (sheet § 12; ruling 14). Before any
  deploy: (D1) `build-citations.py` → **`build-authorities.py`** → `build-index-json.py` → `build-content.mjs` (the
  authorities ledger holds zero vol7 records today); (D5, D7) a local `npm run build` and preview, opening `/tome/7`,
  `/lucam`, one pericope page and `/lucam/c1-v5-17` p. 16 n. 8 "tr." (vol7 has never been through a site build;
  ruling 23's look is owed); (D9) the push and the deploy each take Wilson's own OK and carry every unpushed commit
  (the Vol VI corrigenda and the lucam citation class included); one deploy per OK. The gate's edits and, if it is
  to be live, the tool job (ruling 37) land first. **The deploy question is asked by the coordinator separately.**
- **39. The `low` rows of manifest stage 2 (`caae173`) are ACCEPTED as drawn** (coordinator's item 13; the docket said "five": the TSV holds **six** `low` rows, four decisions).
  Alternatives recorded, not taken: `c4-v31-37` / `c4-v38-44` cut at ¶ 79 (alt. ¶ 87, giving 5.0 + 3.1 pp; or no
  cut, ~8.1 pp) · `c5-v1-11` kept whole at ~6.4 pp (alt. a cut at ¶ 9, 2.7 + 3.7 pp) · `c6-v27-31` / `c6-v32-38`
  cut at ¶ 77 (alt. no cut, ~7.5 pp; or ¶ 82 / ¶ 86) · `c7-v1-16` kept whole at ~7.6 pp over 9 printed pp (alt. a
  cut at ¶ 20, `c7-v1-10` + `c7-v11-16`). **Each row's builder reads its boundary plates; if they agree, it promotes
  its own row's `confidence` cell to `high` (the edit ruling 34 permits, named here); if not, it STOPS and reports
  (ruling 2).**
- **40. `bon-luc-c6-v1-11` takes a SENTENCE TITLE, not "Capitulum VI."** (coordinator's item 14). Under `CAPITULUM
  VI.` no heading stands, so the opening stack holds no heading in ruling 22's sense and the `c2-v25-35` precedent
  (ruling 33) applies: lemma + dividing words, as the manifest cell already has it (*Factum est autem in Sabbato.
  Supra egit Evangelista de discipulorum vocatione; in parte ista agit de ipsorum defensione.*). **A `CAPITULUM N.`
  heading is never itself a `title_la`.**

**The p. 188 gate** (ruling 14: close of c. 7) is the next gate; its interval is the 19 stage-2 rows.

### MANIFEST STAGE 3 — DRAWN 2026-11-15 (Cap. VIII–XI v. 13, pp. 188–288; 22 rows appended to `lucam-chunk-manifest.tsv`; notes in `lucam-chunk-manifest-notes.md` § Stage 3)

Rows per capitulum: **VIII 7 · IX 8 · X 5 · XI 2**. Every boundary and every heading candidate was read on a 300 dpi
crop. The candidates came from a divisio sweep (the region above every lemma paragraph), a vertical-gap screen over
the plates of pp. 188–288, and the text layer. The p. 288 gate interval is these 22 chunks, `bon-luc-c8-v1-10` through
`bon-luc-c11-v5-13`.

**Corrections made by stage 3 (all MEASURED):**

- **Cap. VIII's last ¶ is 99, not 98** (216R). **Cap. X's last ¶ is 80, not ~79** (277R). **Cap. IX's is 111** (251R).
  Each capitulum's first and last pages are as predicted (188–216, 216–252, 252–277), and **none overran.**
- **The p. 288 gate falls at ¶ 35 / ¶ 36 on 288L (~0.41).** ¶ 35 closes v. 13; ¶ 36 opens with the v. 14 lemma.
  The italic t2 *Secundo confutatur falsitas Iudaeorum adversantium quadrupliciter.* and the 288R t3 / t4 cascade stand
  INSIDE ¶ 36, below its opening lines, so the next interval's first chunk opens at ¶ 36 (ruling 1d).
- The 216L delegatio heading is a **t3** (larger roman). Headings stand ~8.5–18 pp apart in cc. 8–11, so most rows
  are cut at Bonaventure's divisio paragraphs (ruling 1b). Each cut is named in a higher paragraph's own division.

**Corrigenda:**

- p. 252 (the second rubric, *sic reformanda est*) → `c10-v1-3`, whose `title_la` takes the reformed wording (ruling 4).

**`low` rows (8, four decisions).** The alternatives for each are in the notes.

- `c8-v26-33` / `c8-v34-39`: the ¶ 60 cut of a ~7.0 pp member. Alternatives: no cut, or ¶ 55 / ¶ 65.
- `c8-v40-48` / `c8-v49-56`: the ¶ 87 cut of a ~7.7 pp member. Alternative: no cut.
- `c9-v46-56` / `c9-v57-62`: a cut is required (~8.9 pp); ¶ 102 chosen, 5.6 + 3.3. Alternative: ¶ 94, 3.1 + 5.8.
- `c10-v1-3` / `c10-v4-16`: both named joints taken, leaving a ~2.7 pp first row. Alternatives: ¶ 14 instead of ¶ 7,
  or no cut at ¶ 7 (~9.1 pp).

**One cut sits near the threshold:** `c9-v1-9` / `c9-v10-17` (¶ 15) is licensed because 216 to 225L measures ~8.5 pp,
just over ruling 1b's ~8. Both rows are `high` on that reading.

# *LUCAM* p. 188 GATE — RULINGS 41–62 (Wilson, 2026-11-15; "aprove all")

Binding summary. Every ⭐ recommendation of `manual-review/vol7-lucam-p188-gate-evidence-sheet.md` was taken, the
sheet's recommendations against the builders (items 25, 32, 33, 42) and its "Found by the sheet" fixes F1–F9 included.
The evidence, censuses and alternatives are in the sheet, by § and item number, and are not repeated. Gate record:
`manual-review/vol7-lucam-p188-gate.md`. Mechanical passes: `manual-review/vol7-lucam-p188-gate-passes-draft.md`.
**18 English lines changed across 9 chunks (F1–F9) + Notes in 10; 1 manifest cell; no line in any `## Latin` body or
`**La.**` half changed.** Ruling 32's table gains six rows (below, marked); ruling 35 gains a clarifying sentence.

- **41. Batch A (items 1–5) RATIFIED** (sheet § A): the six stage-2 `low` → `high` promotions as ruling 39 carried out;
  last ¶ per capitulum IV 98 · V 85 · VI 111 · VII 84; every title as built (rulings 22, 33, 40); the p. 119 hand-off
  correction. Applied (doc): the `bon-luc-c4-v1-13` manifest `headings` cell corrected to
  `capitulum@88;t1@88L;t2@88R (italic);t3@89L;t4@89L` (the 89L t3 was missing; span, end, `title_la` unaffected).
- **42. Batch B (items 6–8), the three Corrigenda of pp. 88–188, RATIFIED as applied** (`c4-v1-13` p. 95; `c5-v1-11`
  p. 114 inside apparatus n. 5; `c7-v1-16` p. 168 *indignitatem*).
- **43. Batch C (items 9–24), the ruling-20 lemma and adduced-verse adjustments, RATIFIED as built.**
- **44. *suasio* "persuading" / *persuasio* "persuasion" and *authenticatio* "authentication" / *auctorizatio*
  "authorization" are the WORK'S PAIRS** (item 25). Applied (F1): `c4-v1-13` ¶ 15 "In which persuading", ¶ 16 "the
  diabolical persuading" (2 lines), so p. 92 n. 9 and p. 93 n. 7 can be read off the English.
- **45. Prov. 1:20 "crieth aloud" and Ps. 64:12 "the year of thy kindness" RATIFIED** (item 26). **Written into ruling
  32's table: *benignitas* "kindness", *benignus* "kind", into quotations too.**
- **46. Amos 5:10 "him that rebuketh", Prov. 9:8 "Rebuke", John 8:46 "convince" RATIFIED** under ruling 32's preface
  (item 27). Recorded (F10): Amos 5:10 is "him that correcteth" at `c3-v15-20` ¶ 46 (the exposition leans) and "him
  that rebuketh" at `c4-v22-30` ¶ 57 (nothing leans), ruling 28's split; now disclosed in `c4-v22-30`'s Notes.
- **47. *potentia* / *virtus* / *potestas* all "power"; *auctoritas* "authority" — CONFIRMED** (item 28). **Tie-breaks:
  where two stand together in a verse, the Douay's own pair at that verse decides (Luke 4:36 *in potestate et virtute*
  "with authority and power", and the gloss that follows it); *potentia* in the faculty sense, beside *virtus*, is
  "potency"** (`c7-v1-16` ¶ 27). *virtus* the moral virtue stays "virtue".
- **48. *solitudo* "solitude" / "wilderness" — the split RATIFIED as ruling 28's** (item 29): "solitude" where the
  prose names *solitudo* against *desertum* (`c4-v1-13` ¶¶ 1, 3), the Douay's "wilderness" where nothing leans.
  Recorded: **Osee 2:14** is a second split ("solitude" `c4-v1-13` / "wilderness" `c3-v1-9` ¶ 7), with Ps. 54:8.
- **49. `tr-praeceptor` RATIFIED as the work's note; *magister* "Master" beside *Praeceptor* "Master" and Wis. 8:16
  "repose" / "rest" RATIFIED** (items 30, 38). **Forward:** the first chunk where *Praeceptor* and *magister* stand in
  one paragraph (Luke 9:33 / 9:38 is the likely place) adds to its `tr-praeceptor`: "*magister* is also 'Master' (the
  Douay's word); the two Latin words share it."
- **50. `tr-lumen`'s reach RATIFIED as built, all four parts** (item 31). **Scope sentence: in the Vol V test, "the
  surrounding body prose" is the expository unit the verse is adduced in (here `c5-v17-26` ¶¶ 60–62, one argument);
  the *lux* / *lumen* rule reaches the editors' quotations in the apparatus** (the Vol VI practice; `c4-v38-44` p. 110
  n. 8, `c6-v32-38` p. 159 n. 7). Rom. 2:19 "a light" with no note stands (the test as written). Recorded (F11): Isa.
  60:1 "thy lumen is come" (`c5-v17-26` ¶ 62, leans) / "thy light is come" (`c6-v12-19` ¶ 47, does not), ruling 28's
  split; `c7-v1-16` ¶ 17 carries a fifth `tr-lumen` the docket omitted.
- **51. Human *pietas* inside quotations CONFORMED to "piety"** (item 32; the *septem donis* ruling carried by ruling
  11, and ruling 31). Applied: F4 `c6-v12-19` ¶ 40 II Tim. 3:5 "an appearance indeed of piety"; F5 `c5-v17-26` ¶ 44
  Ecclus. 44:10 "whose pieties have not failed"; F6 `c4-v38-44` p. 110 n. 8 **En.** Augustine's *pios* "the pious"
  (3 lines). **Recorded, not ruled (the passes draft's observation):** *impius* in Bonaventure's prose follows the
  nearest Douay word ("ungodly" `c6-v27-31` ¶ 73 after Ecclus. 12:4; "wicked" `c6-v39-49` ¶ 96 after Prov. 17:15);
  *impietas* "impiety". The *pietas* rule binds the positive word only; no edit.
- **52. Douay kept against a house word: four sites RATIFIED, two CONFORMED** (item 33 + F2). Ratified: Prov. 15:17
  "with charity" (`c5-v27-39` ¶ 73); Eph. 5:2 "Walk in love" (`c5-v17-26` ¶ 62); "what thanks are to you?"
  (`c6-v32-38` ¶¶ 78–80); Rom. 2:20 "an instructor of the foolish" (`c6-v39-49` ¶ 93). Conformed where the paragraph
  leans on *dilectio* (the ruling-28 Col. 1:13 precedent; ruling 27: no famous-verse exception): F3 `c6-v27-31` ¶ 65
  "Walk in dilection" / "dilection without dissimulation"; F2 `c7-v36-50` ¶ 76 Cant. 8:6 "Dilection is strong as death"
  (2 lines). **Written into ruling 32's table: *caritas* "charity", into quotations too.**
- **53. *curare* / *sanare* is a WORK-LEVEL split** (item 34 + F7). **Ruling sentence: *curare* / *curatio* "cure",
  *sanare* / *sanatio* "heal" / "healing" in Bonaventure's prose; the Douay's "heal" stands in a verse where nothing
  leans (the lemma is adjusted only where the exposition leans, ruling 20, as `c6-v1-11` Luke 6:7 / Matt. 12:10), and
  an echo of the lemma follows it** (so `c4-v22-30` ¶¶ 49–50 "Physician, heal thyself" stands). Applied (F7):
  `c7-v1-16` ¶¶ 1, 9, 16, 17, 18, 20 — nine sites, 6 lines (the sheet said ten; the file holds 8 *curatio* + 1
  *curatus*). Written into ruling 32's table.
- **54. *puer* "boy" (prose) / "servant" (the Douay's verses) and Gen. 15:6 *Credidit Abraham* "Abraham" RATIFIED**
  (item 39). **Clarifies ruling 35: the Douay's spelling at the verse governs the orthography of the name Quaracchi
  prints; where Quaracchi prints a different name form (*Abraham* for *Abram*), ruling 28 keeps Quaracchi's.**
  **(Clarified by ruling 93, p. 472 gate: *puer* the servant "boy" in prose / "servant" in the Douay's verses
  (`c7-v1-16`, Luke 12:45); *puer* the child "child(ren)", the work's ~60 sites from Cap. I on (`c18-v15-17` conformed
  at the p. 472 gate).)**
- **55. *credulitas* → "belief", WORK-WIDE** (item 42 + F9); *incredulitas* "unbelief"; *fides* "faith". Applied:
  `c1-v26-38` ¶ 67 ×2, ¶ 69 → "belief" (3 sites, 3 lines; the sheet said 2 lines — ¶ 67 stands on two). Written into
  ruling 32's table.
- **56. *redarguere* → "convict", beside *arguere* "reprove"** (sheet § X, F8). Applied: `c7-v24-35` ¶ 47 "is
  convicted", ¶ 57 "he convicts … he convicts in four ways" (2 lines). Written into ruling 32's table.
- **57. RATIFIED as built:** *Iudam Iacobi* "Jude of James" (item 35; ruling 28, the body leans); `tr-vacare` "free
  for" at a vice and *exsultatio* "exultation" (item 36; the site is ¶ 60, F12b); the lending vocabulary, *foenerator*
  "lender upon usury" at Luke 7:41 included (item 37); passive *evangelizantur* (item 40); *delectabilia* /
  *deliciosus* "delightful" and Luke 7:32 "We have piped" (item 41). **Written into ruling 32's table: *otium*
  "leisure"** (keeps "leisure" off *vacatio*).
- **58. Batch E (items 43–51), the Quaracchi citation slips, RATIFIED as transcribed** (r.57 class; ruling 36); the
  `c5-v12-16` p. 122 n. 5 *(n. 36-40.)* recorded, undecidable from Quaracchi alone.
- **59. Batch F: items 52–55 (`[so printed]`) RATIFIED; item 56, the live `[?]` at `c5-v12-16` p. 122 n. 11, STAYS
  OPEN** — not a deploy blocker; settled only by a second copy of Tom. VII (F or H), never by a guess.
- **60. Batch G (items 57–61, readings as printed) RATIFIED as recorded; Batch H (items 62–64, collection change)
  BANKED, no ruling.**
- **61. Records (F10–F12):** F10, F11 under rulings 46, 50. F12, docket errors, no text effect: (a) item 4's
  sentence-title list omitted three (`c4-v38-44` ¶ 79, `c5-v12-16` ¶ 24, `c5-v17-26` ¶ 40) — nine in all; (b) item
  36's *exsultatio* is ¶ 60, not ¶ 61; (c) the resume's "tool item T-11" for the wrong *ibid.* is **T-4**; (d)
  `c7-v24-35`'s Notes licence for Ecclus. 3:1 "love" is ruling 32's preface, not ruling 12's quotation clause
  (corrected in that chunk's Notes). Also corrected in the resume: the ruling-37 tool job **has run** (`187bc15`), and
  manifest stage 3 **is drawn** (`f03a544`).
- **62. T-1..T-9: ONE bounded tool job, after the gate, QUEUED, NOT RUN** (sheet § T). Order: T-4 (the wrong *ibid.*
  resolution; anaphora unresolved should rise by one) → T-1 (accusative *notam M*, 5 sites) → T-2 (measure Vol II / IV
  per-note anchors first) → T-6 → T-9 (*Incendium amoris* as other-author) → T-7 → T-8 (count) → T-3 (a Vol I data
  question; report only) → T-5 (stays deferred; count). Report → fix → report, before/after table per site;
  `tools/build-citations.py` only, then `build-citations.py` → `build-index-json.py`. No chunk file.

**Manifest stage 3 (`f03a544`, 22 rows, pp. 188–288) stands as drawn; its 8 `low` rows (four decisions) are settled at
build time by ruling 39's procedure** (each builder reads its boundary plates, promotes its own row's `confidence` cell
or STOPS). **The p. 288 gate** (c. 11 v. 13, ¶ 35 / ¶ 36 on 288L) is the next gate; its interval is the 22 stage-3 rows.

### MANIFEST STAGE 4 — DRAWN 2026-11-15 (Cap. XI v. 14 – Cap. XIV, pp. 288–381; 19 rows appended to `lucam-chunk-manifest.tsv`; notes in `lucam-chunk-manifest-notes.md` § Stage 4)

Rows per capitulum: **XI 4 · XII 5 · XIII 5 · XIV 5**. Every boundary and every heading candidate was read on a 300 dpi
crop. The candidates came from a vertical-gap screen over the plates of pp. 288–381, a divisio sweep and the text
layer. The p. 381 gate interval is these 19 chunks, `bon-luc-c11-v14-26` through `bon-luc-c14-v25-35`.

**Corrections made by stage 4 (all MEASURED):**

- **Cap. XIII's last ¶ is 76, not ~73–74** (358L). **Cap. XIV's last ¶ is 69, not 68** (381R; ¶ 68 is Vers. 35).
  Cap. XI's is 102 (309R) and Cap. XII's 88 (335R), as the table has them. Each capitulum's first and last pages are as
  predicted (277–309, 309–336, 336–358, 358–381); **none overran.**
- **The p. 381 gate falls at ¶ 69 / `CAPITULUM XV.` on p. 381 (~0.52 / ~0.55 of the leaf).** The last row ends there.
- **`CAPITULUM XIII.` has no heading under it** (ruling 40: `c13-v1-9` takes a sentence title).
- The blasphemantium member's improbatio joint is **¶ 43** (290R), not ¶ 41 as the text layer suggests.

**Corrigenda:** seven entries fall in pp. 288–381 (pp. 294, 300, 320, 333, 343, 346, 361), each assigned to its row's
`corrigenda` cell; none touches a title (ruling 4). p. 300's stands inside n. 8's gutter runover.

**`low` rows (7, three decisions).** The alternatives for each are in the notes.

- `c11-v14-26` / `c11-v27-32` / `c11-v33-41` / `c11-v42-54`: three sibling t4 sections of ~9.7 / ~2.1 / ~9.6 pp. Cut at
  ¶ 58 (the tentantium section joined to the blasphemantium tail across the 298L t4) and ¶ 85. Alternatives: ¶ 36–63 kept
  whole (~9.7) then ¶ 64–76 / ¶ 77–102; or ¶ 43 + ¶ 58 (first row ~2.5 pp). ⚠ `c11-v27-32` is the first divisio-opened
  row carrying an interior t4.
- `c12-v1-7` / `c12-v8-12`: the 313R cut, 3.6 + 2.7 pp (the edge of the ≥ 2.7 test). Alternative: one row ~6.3 pp.
- `c12-v13-34` kept whole at ~7.8 pp (headings ~7.8 apart, just under ruling 1b's ~8). Alternative: cut at ¶ 32.

**The p. 381 gate** (ruling 14: close of c. 14; the *pietas* review) closes this interval.

# *LUCAM* p. 288 GATE — RULINGS 63–76 (Wilson, 2026-11-15; "Approve all")

Binding summary. Every ⭐ recommendation of `manual-review/vol7-lucam-p288-gate-evidence-sheet.md` was taken, its
"Found by the sheet" fix F1 and its records F2–F12 included, and the one defect found by Passes 1–3
(`manual-review/vol7-lucam-p288-gate-passes-draft.md`). The evidence, censuses and alternatives are in those two
documents, by § and item number, and are not repeated. Gate record: `manual-review/vol7-lucam-p288-gate.md`. **14
English lines changed across 6 chunks + Notes records in 9; no line in any `## Latin` body or `**La.**` half changed; no
manifest cell changed.** Ruling 32's table gains one row (*excessus*) and two clauses on its *vacare* row; the repo
CLAUDE.md's Itinerarium *excessus* line gains a one-clause scope note (Wilson's approval; no other CLAUDE.md change).

- **63. D-1 and D-2 APPLIED** (sheet § "The three defects"). D-1: `c8-v49-56` English verse tags `(V. N.).` →
  `(Vers. N.).` at ¶¶ 88, 89, 90, 92, 93, 94, 95, 98 (8 lines); its Notes' "`(Vers.` 8 = 8 in each language", false
  as built (F2), amended in place, struck wording kept. D-2: `c9-v1-9` "appointed" → "designated" at **both** sites
  (F3: ¶ 1's forward reference and p. 216 n. 9 **En.**; 2 lines), conformed to `c10-v1-3`'s Luke 10:1. The apparatus
  **En.** form `V. N` is the house form and is untouched.
- **64. *dilectio* → "dilection" outside a Douay verse, WORK-WIDE** (F1; ruling 11's register, ruling 52). Applied:
  `c9-v10-17` ¶ 19 *perfectio dilectionis* "the perfection of dilection"; `c10-v1-3` p. 253 n. 2 **En.** "the two
  commandments of dilection" ×2 (2 lines). These were the only two non-verse sites in pp. 3–288.
- **65. Batches A (items 1–5), B (item 6) and C (items 7–14) RATIFIED, item 25 with B.** All 22 stage-3 rows as
  drawn; ruling 39's eight `low` → `high` promotions; last ¶ VIII 99 · IX 111 · X 80, XI v. 13 at ¶ 35; titles as built.
  The p. 252 Corrigenda rubric and `tr-corrigenda` on the `####` heading: ruling 8's "at the word" reads "at the rubric"
  when the Corrigenda reform a whole rubric; the preview look `/lucam/c10-v1-3` (the "tr." on the second heading) is
  added to ruling 23's owed look. The ruling-20 adjustments as built, **Luke 11:2 "Sanctified be thy name" included**
  (item 7(a)); Matt. 6:9 "Hallowed be thy name" (`c1-v46-56` ¶ 93) recorded as a ruling-28 split (`c11-v1-4` Notes).
- **66. `c9-v32-36` ¶ 69 Ambrose *praedica post consummationem* "proclaim" → "preach" APPLIED** (ruling 30:
  "proclaim" is *praeconium*'s alone; 1 line). Found by Passes 1–3; the builder's item (90) had recorded the rendering
  without naming it a departure (amended in place, struck wording kept).
- **67. *excessus* KEPT AS BUILT** (item 15(a); D-3 no edit): Luke 9:31 and `c9-v28-31` ¶ 54 "excess", ¶ 47 / `c9-v32-36`
  ¶ 62 / `c8-v49-56` ¶¶ 97–98 "transport"; `tr-excessus` kept. **Written into ruling 32's table** (the sense split).
  The split is inside `c9-v28-31`, by sense (F4). **CLAUDE.md scope note** beside the Itinerarium "NEVER 'excess'" line:
  that rule is the mental / contemplative *excessus*. Recorded, outside the gate's reach: Vol V's three "excess" sites
  against its own Itinerarium rule (`bon-brev-p5-c6` + p. 260 n. 3; `bon-praec-c4` p. 521 n. 4) belong to a later
  Vol V errata list; not edited.
- **68. *vacare*: absolute "to be free" and Ps. 45:11 "Be free, and see" RATIFIED** (item 17(a)); **written into ruling
  32's *vacare* row.** Recorded (F6): Ps. 45:11 is "Be still and see" at `c4-v14-22` p. 96 n. 10 (Bede; nothing leans),
  a ruling-28 split; the licence at `c11-v1-4` is the Vol VI `bon-cioan-c21` precedent + ruling 20.
- **69. Ruling 49's forward clause DISCHARGED at `c8-v40-48`** (¶ 82); **its sentence is now the standing text of
  `tr-praeceptor` wherever *magister* stands in the same paragraph** (item 16(a); ~~one *Praeceptor* left in the work,
  Luke 17:13~~ **[corrected by ruling 110, p. 540 gate: two, Luke 17:13 and 21:7 (`c21-v5-11` ¶ 12); the struck text is kept
  visible]**). `c8-v40-48` ¶ 82 *magister et praeceptor* "master and preceptor" RATIFIED. An OT *praeceptor* takes the
  Douay unless the exposition leans (ruling 20): Isa. 30:20 "thy master" `c5-v1-11` ¶ 10 / "teacher" `c9-v57-62`
  ¶ 103, p. 249 n. 2 — a ruling-28 split (F7; recorded in `c9-v57-62`'s Notes).
- **70. Items 18–23 RATIFIED as built:** *intellectus / intelligentia / notitia / cognitio* (ruling 17 holds; F10
  recorded, no conformation — *cognitio* "knowledge" at 5 of 16 interval sites, no *notitia* / *scientia* beside them);
  `tr-lumen` (F8: Matt. 10:27 "in the lumen" `c8-v11-21` ¶ 24 / "in the light" `c10-v4-16` ¶ 18, rulings 27 / 50 as
  written); *claritas* "brightness" (ruling 32's row); human *pietas* with no note, **carried to the p. 381 review** with
  the sheet's § 21 list, `tr-pietas` at `c9-v37-45` ¶ 77 ratified; *virtus / potestas / potentia* (ruling 47; F12a);
  the cross-chunk ruling-28 splits (D-4 no edit; F9's wider census recorded in the gate record).
- **71. Item 24, the interval's new house words, RATIFIED as a batch, with F1 applied** (ruling 64). **Item [99]:
  *infidelitas* "faithlessness", kept off *incredulitas* "unbelief" (ruling 55).** Applied (the passes draft's
  observation, folded in): `c10-v4-16` ¶ 19 *excusationem de infidelitate* "no excuse for unbelief" → "for
  faithlessness" (1 line), the one split site. *infidelis* "unbeliever" at a Douay verse stands.
- **72. Batch E (item 26), the Quaracchi citation slips, RATIFIED as transcribed** (r.57 class; ruling 36). They feed
  J-3 / J-7 as printed slips, not resolver faults.
- **73. Batch F: the five `[so printed]` and p. 195 n. 10's *Locus videtur esse corruptus* RATIFIED; the live `[?]`
  (`c5-v12-16` p. 122 n. 11) STAYS OPEN** (ruling 59). Zero `[?]` in the 22 interval chunks.
- **74. Batch G (items 30–32) RATIFIED as recorded (ruling 36); Batch H (items 33–34, collection change) BANKED, no
  ruling** (rulings 36, 60).
- **75. Records (F2–F12) and docket errors, no text effect:** F4 (the *excessus* split is inside one chunk); F5 (Luke
  8:1 "evangelizing" was already ruled by ruling 18; `c10-v38-42` ¶ 66 follows it as an echo, ruling 29); F9 (the
  ruling-28 splits are wider than the docket listed; gate record); F11 (p. 201 n. 6 joins J-5); F12 (a) Luke 9:1
  "power and authority" is the Douay's own pair, not an adjustment; (b) the docket's tool numbers collided with ruling
  62's (resolved by ruling 76). Also: the passes draft's "undisclosed" for the ¶ 69 *praedica* is half right (the
  builder's item (90) names the rendering but not as a departure).
- **76. ONE tool job J-1..J-11, QUEUED, NOT RUN** (sheet § T; supersedes ruling 62's T-numbering, which is kept only as
  a crosswalk). One bounded job after the gate, report → fix → report, before / after table per site; order wrong edges
  → coverage → counts; `tools/build-citations.py` only, then `build-citations.py` → `build-index-json.py`; no chunk file,
  no `tools/authorities.json`. **Crosswalk:** J-1 = r.62 T-4 + docket T-4 (wrong *ibid. / loc. cit.*: p. 183 n. 6,
  p. 263 n. 11) · J-2 = docket "Misreads" (p. 237 n. 8) · J-3 = r.62 T-6 + docket T-7 (author guard both ways) · J-4 =
  r.62 T-1 + docket T-1 (accusative *notam M*, 11 sites) · J-5 = r.62 T-2 + docket T-6 (+ F11; `page-multi` by note;
  measure Vols II / IV per-note anchors first) · J-6 = r.62 T-9 + docket "No record" (report each first) · J-7 =
  docket "No record" (commentator guard, p. 277 nn. 7, 12; expect none) · J-8 = r.62 T-7 · J-9 = r.62 T-8 + docket
  T-4 / T-10 (count, classify) · J-10 = r.62 T-3 (Vol I p. 104; report only) · J-11 = r.62 T-5 + docket T-5 (stays
  deferred; count). Baseline: QA 213, anaphora unresolved 379.

**Manifest stage 4 (`c478c25`, 19 rows, pp. 288–381) stands as drawn; its 7 `low` rows (three decisions) are settled at
build time by ruling 39's procedure.** The front is `bon-luc-c11-v14-26` (stage-4 row 1, `low`), opening at ¶ 36 on
288L; p. 288 nn. 4–11 are its. **The p. 381 gate** (close of c. 14; the *pietas* review) closes the interval.

# *LUCAM* p. 381 GATE — RULINGS 77–92 (Wilson, 2026-11-16; "Approve all")

Binding summary. Every ⭐ recommendation of `manual-review/vol7-lucam-p381-gate-evidence-sheet.md` was taken: D-1..D-7
as specified (D-2 no edit; D-5 kept as built with the adjective clause; D-6 a tool item), the "Found by the sheet" fixes
F1–F7 and F13 (the five pre-interval lines included), the records F8–F12, the *pietas* review closed, every batch
ratified. The passes draft (`manual-review/vol7-lucam-p381-gate-passes-draft.md`) found no defect beyond the sheet's (its
N-1..N-4 are F3, F4, F5, F10). The evidence, censuses and alternatives are in those two documents, by § and item number,
and are not repeated. Gate record: `manual-review/vol7-lucam-p381-gate.md`. **42 English lines changed (37 in 13
interval chunks, 5 in 4 pre-interval chunks; three of the 42 are new `tr-lumen` definitions and one is a `title_en`) +
Notes records in 19 chunks; no line in any `## Latin` body or `**La.**` half changed; no manifest cell changed.** Ruling
32's *excessus* row gains the adjective clause (ruling 81). The setup table's Cap. XIV cell is corrected 68 → 69 (ruling
89). No CLAUDE.md change.

- **77. D-1 and D-4 APPLIED** (sheet § D-1, § D-4). D-1: `c13-v1-9` ¶ 6 *defectus credulitatis* "lack of *credulity*" →
  **"lack of *belief*"** (ruling 55, work-wide; the one "credulity" in the rendered region of all 82 chunks; 1 line);
  the Notes' "New here" entry amended in place, struck wording kept; item (85) answered. D-4: `c11-v14-26` ¶ 36's
  forward reference *Nemo lucernam accendit* "a candle" → **"a lamp"** (a forward reference follows its lemma,
  `c11-v33-41` ¶¶ 70–71; the ruling-63 precedent; 1 line); its "Kept on the Douay" line amended in place.
- **78. D-2: NO EDIT** (F8). `c12-v49-59` ¶ 84 Ps. 4:7 *lumen vultus tui* keeps "light": the verse is quoted as a verse
  and nothing leans (the *mysterio Trinitatis* shakedown test, ruling 27, its unit fixed by ruling 50). The CLAUDE.md
  line keeping "lumen" at Ps. 4:7 is that test applied to the two Vol V attestations, where the body leans; it decides
  those two sites and does not exempt the verse elsewhere. Fixing the verse at "lumen" corpus-wide would be a new
  ruling (and would reopen the four Vol V "light" sites); not made. Item (71) answered in `c12-v49-59`'s Notes.
- **79. D-3 APPLIED at the two Fathers' sites** (F9). `c12-v8-12` p. 316 n. 2 **En.** Augustine's *veritas lumenque
  animae rationalis* "the truth and the **lumen**"; `c14-v16-24` p. 373 n. 12 **En.** Gregory's *nullum ingenii lumen*
  "no **lumen** of wit"; each chunk gains one `tr-lumen` in the `c4-v38-44` form (4 lines). **`c13-v1-9` p. 339 n. 5,
  Isa. 9:2 *lumen ortum est eis* inside the Gloss, is EXEMPT** (a verse quoted as a verse; the Gloss leans on *umbra
  mortis*, not on *lumen*; the Rom. 2:19 shape of ruling 50): "light" stands; item (87) answered.
- **80. F4 APPLIED** (= passes N-2; rulings 32 / 50). `c12-v1-7` ¶ 2 *tenebra per lumen expellitur* "driven out by
  **lumen**"; ¶ 6 *Lumen enim solis* "the **lumen** of the sun", and the lemma it glosses, Luke 12:3 *in lumine
  dicentur*, follows: "shall be spoken in the **lumen**" (the Matt. 10:27 shape, `c8-v11-21` ¶ 24); one `tr-lumen` at ¶ 2
  naming ¶ 6 (3 lines). These were the only *lumen* of Bonaventure's prose rendered "light" in the work. Item 7's Luke
  12:3 verb ("spoken" for the Douay's "published") is untouched. **With rulings 79–80, item 12 ([18], [57], [99]) is
  ratified as built**: no *lumen* of Bonaventure's or a Father's prose in the interval stands outside `tr-lumen`'s reach.
- **81. D-5: *excessivus* KEPT AS BUILT at all four sites** (F10 = passes N-4). `c13-v18-21` ¶ 46 *dilectio excessiva*
  "transporting dilection" (Dionysian mystical theology: the mental / contemplative sense); `c12-v49-59` ¶ 72
  *adhaerentiam excessivam* "an excessive adherence" and `c9-v32-36` ¶ 61 + p. 236 n. 7 *excessivum desiderium* "excessive"
  (the measure sense; ¶ 61 glossed by Bonaventure *prae nimietate desiderii*). **Written into ruling 32's *excessus* row:
  the adjective *excessivus* follows the noun's sense — mental / contemplative "transporting", measure "excessive".**
  Recorded: ¶ 72 is the one site where the reading could go either way (the sheet's alternative (b), not taken).
- **82. D-7 and F2 APPLIED: *eruditio* "erudition", *erudire* "school"** (ruling 17; ruling 32's row). D-7: `c14-v12-15`
  ¶ 26 *spiritualem eruditionem* "spiritual **erudition**" (1 line; the one exception in 36 *eruditio* sites). F2: the
  participle is the verb, so the docket's rider ("*erudiens* 'teaching' stands") is not taken: `c14-v12-15` ¶¶ 26, 27 "the
  exhortation **schooling**"; `c14-v25-35` `title_en`, the 375L `####` "Third the multitudes following are **schooled**",
  ¶ 51 "**schooled** the guests … he **schools** … Now **schooling**" (5 interval lines); **and the two pre-interval
  lines**, `c9-v10-17` ¶ 16 *ut Dominum erudirent* "that they might **school** the Lord" and `c9-v32-36` ¶ 64 *erudiuntur
  contemplativi* "contemplatives are **schooled**" (the sense exception offered for ¶ 16 not taken). `c14-v12-15` and
  `c14-v25-35`'s Notes amended in place, struck wording kept. ¶ 51 *informat* "forms" (ruling 12) untouched.
- **83. F1 APPLIED: "Holy Ghost" → "Holy Spirit"** (ruling 17, Douay quotations included). 16 occurrences on 12 interval
  lines (`c12-v8-12` ×7 lines, `c12-v13-34` ×2, `c13-v18-21` ×2, `c13-v31-35` ×1) and 4 occurrences on 2 pre-interval
  lines (`c10-v17-24` ¶¶ 36, 39; Luke 10:21, Rom. 14:17). After it the rendered region of all 82 chunks holds no "Holy
  Ghost"; the phrase survives only inside five older chunks' `## Notes` (`prooem`, `c1-v18-25`, `c1-v26-38`, `c1-v39-45`,
  `c3-v1-9`), outside the rule's reach, not edited. `c12-v8-12`'s Notes headline amended in place.
- **84. F3, F5, F6, F7 APPLIED** (one word each). F3 (= N-1; ruling 45): *benignitas* "kindness" at `c13-v1-9` ¶ 12 (Rom.
  2:4, the Douay's "benignity" adjusted, as at Ps. 64:12), `c14-v16-24` ¶ 37, `c14-v25-35` ¶ 52 (3 lines; "benignity" now
  0 in the work). F5 (= N-3; ruling 56): `c11-v42-54` ¶ 87 and p. 305 n. 6 **En.** *Arrogantiam redarguit* "He
  **convicts** arrogance" (2 lines; *redarguere* "convict" at all 20 regions). F6: `c14-v12-15` ¶ 28 Prov. 23:21 *dantes
  symbola* "and that **club together**", the Douay, as at `c12-v13-34` ¶ 29 (nothing leans; 1 line). F7: `c14-v7-11`
  p. 365 n. 15 **En.** *operationes mirabiles* "**marvellous** operations" (ruling 32's row; 1 line). Recorded, not
  re-read: `c2-v40-52` p. 67 n. 11 is the other apparatus *mirabilis* "wonderful" (pre-interval).
- **85. F13 APPLIED: *accidia* → "acedia" WORK-WIDE; *desidia* "sloth"; *pigritia* "sluggishness"** (the capital vice;
  the work's `c8-v11-21` ¶ 23 and `c8-v26-33` p. 203 n. 11 already so). `c11-v14-26` ¶ 56, `c14-v1-6` ¶ 11, `c12-v13-34`
  p. 318 n. 4 **En.** (3 interval lines) and `c6-v1-11` ¶ 21 (pre-interval; 1 line). Item (140) answered: *desidia* and
  *accidia* no longer meet in "sloth". **This overturns the p. 288 sheet's item 24 claim ("acedia at every Bonaventure /
  Du Cange site")**, which `c6-v1-11` belied. Recorded: *pigritia* "sloth" at `c9-v10-17` ¶ 22 (record only, no edit).
- **86. THE *pietas* REVIEW CLOSES: ruling 12 / 31 HOLDS for cc. 15–16** (item 11(a); ruling 70's carried review).
  *pietas* "piety", *pius / pie* "pious / piously", human and divine; `tr-pietas` at the first divine site of each chunk;
  *impietas / impius* "impiety / impious" in prose, the nearest Douay word in verses (ruling 51). **In the Cap. XV chunks
  `tr-pietas` names Cap. XV ¶ 1's divisio at its first site:** *impietas* / *pietas divina* / *pietas humana*, one English
  root ("impiety … divine piety … human piety"). Interval census 22 / 22; the three divine `tr-pietas` (`c12-v35-48` ¶ 57,
  `c13-v10-17` ¶ 25, `c13-v31-35` ¶ 74) ratified. Recorded: Titus 2:12 is "godly" in Vol V `bon-don-c1` and Vol VI
  `bon-cioan-c8`, "piously" in `bon-don-c3` and Lucam ×2 — a cross-volume split; ruling 51 governs Lucam.
- **87. Item 10 RATIFIED: *anima* "soul" where the exposition leans, the Douay's "life" where nothing leans; the other
  ruling-20 / ruling-28 splits as a batch** (*ubera*, *sacculus*, *monumentum / sepulcrum*, *nuptiae*, *convivium*,
  ~~*supplicium*~~ **[the *supplicium* clause REPLACED by ruling 94, p. 472 gate: *supplicium* → "penalty", the house
  rule `CLAUDE.md:3502`; the struck word is kept visible]**, *remittetur*, *dispensator*, Mark 3:2 / Luke 14:3, Matt. 4:4, Ecclus. 1:39, Rom. 1:21). Recorded: F12(b)
  Luke 14:26 "his own **life**" `c12-v49-59` ¶ 75 (adduced) / "his own **soul**" `c14-v25-35` ¶ 52 (the lemma; ¶ 53
  leans), a cross-chunk ruling-28 split (both chunks' Notes); F12(c) John 12:25 "soul" at all three Lucam sites, each on
  a leaning paragraph. F6 (ruling 84) was the one unlicensed split.
- **88. Items 12–18 RATIFIED** (after rulings 77–85): *lumen* rest (item 12; ruling 80); *lucerna* — Matt. 5:15 "lamp"
  `c14-v25-35` ¶ 59 [174] (item 13); *excessus* — p. 379 n. 4 Aristotle's *per excessum et defectum* "excess" [179], the
  measure sense (item 14); *intellectus / intelligentia / notitia / cognitio / scientia* (item 15; ruling 17 holds;
  recorded `c13-v22-30` ¶ 58 *cognitionis* ×2 + *negatio notitiae* all "knowledge", no conformation, ruling 70); *vacare /
  quies* (item 16: [5] `tr-vacare`, [133] *quies* "rest", [109] *quietari* "be set at quiet"); the house words as a batch
  (item 17), **recording [121]**: `c13-v22-30` ¶ 56 *serotinam poenitudinem* "late repentance" beside the Douay's Wis. 5:3
  "repenting" and Heb. 12:17 "repentance" (nothing leans on *poenitentia*) — "repentance" names two Latin words in one
  paragraph, which ruling 20 permits; ruling 32's *poenitentia* "penance" row stands; the new house words (item 18) with
  rulings 82 and 84 applied.
- **89. Batches A, B, C RATIFIED** (items 1–9). All 19 stage-4 rows as built; last ¶ XI 102 · XII 88 · XIII 76 · XIV 69
  (ruling 36). **The setup table's Cap. XIV cell (§ "The Luke commentary by capitulum") is corrected 68 → 69**, where the
  stage-4 record (§ MANIFEST STAGE 4) had corrected it without amending the cell. The seven Corrigenda pp. 294–361 as
  applied (`c11-v14-26`'s `tr-corrigenda`, ruling 23's shape). The ruling-20 adjustments and Douay base as built, with
  F12(a) recorded: Luke 12:20 "this night do they require thy soul" is the Douay's own wording, not an adjustment; and
  Luke 12:3's lemma "lumen" applied (ruling 80).
- **90. Batches E, F, G RATIFIED; H BANKED.** E (item 19): the Quaracchi citation slips as transcribed (r.57 class;
  ruling 36); p. 366 n. 4 *caritatem divinam* from H is the editors' text (record); p. 295 n. 15's ledger side is J-12
  (ruling 92). F (items 20–22): `[so printed]` *eautelam*, *rimediando* ratified; **¶ 10 *quinque ova*: no mark**
  (Bonaventure's market analogy, not a misprint; `[so printed]` is for misprints only, ruling 36); zero new `[?]`; **the
  live `[?]` (`c5-v12-16` p. 122 n. 11) STAYS OPEN** (rulings 59, 73). G (items 23–26): guillemets and points as
  recorded, supply nothing; codex H read for `II` ratified (rulings 36, 60, 74). H (item 27): collection change banked,
  no ruling.
- **91. Records F8–F12 and docket errors, no text effect.** F8 (D-2's framing: the docket's "defect" is not one under
  the test); F9 (D-3 is two defects, not three); F10 (*excessivus* at four sites); F11 (D-6's cause located in
  `scan_page()`; four direction slips in the whole ledger); F12 (a)–(d) (Luke 12:20; Luke 14:26; John 12:25; T-e's
  *notam 11* not captured). **Not on the docket, not ruled (passes draft observations O-1..O-3; carried open, no edit):**
  O-1 `c13-v1-9` ¶ 17 *arguitur* "convicted" (*arguere*, ruling 32 "reprove") filed under ruling 56; O-2 `c13-v1-9` ¶ 12
  Augustine's *quare vacatis?* "why are you idle?" against ruling 32's *vacare* row; O-3 `c14-v25-35` ¶ 66 and p. 379
  n. 9 **En.** Ps. 18:6 *Exsultavit* "rejoiced" against *exsultare* "exult". O-4 is F6 (ruling 84); O-5 is item 15.
- **92. J-12 ADDED to ruling 76's ONE tool job, QUEUED, NOT RUN** (sheet § T; D-6 / T-g). J-12: a `CROSSREF_SLIPS` row
  `("bon-luc-c11-v14-26", "apparatus:p295-15", "supra pag. 297, nota 7", "printed slip — *supra* from p. 295; the locus
  is p. 294 n. 7 (Jerome on Matt. 12:43); filed as printed, not retargeted")` (the ruling-37 T3 / T4 shape: verdict →
  `unresolvable`, listed in the QA slips table; never retargeted, rulings 37 / 57) **+ a report-only direction screen**
  (`supra pag. N` with N > citing page, `infra` with N < citing page, same volume) printed in the QA report; it finds 4
  today (F11), the three outside Vol VII (`bon-ioan-c13-v21-30` p. 432 n. 9; `bon-sent-III-d27-dubia` p. 615 n. 15, p. 619
  n. 1) reported, not fixed. **The interval's tool sites fold into the existing J-items, no new job:** J-1 + T-b (p. 342
  nn. 11, 12; p. 348 nn. 2, 5; p. 370 n. 13; p. 378 n. 6); J-2 + T-c (p. 320 n. 3); J-4 / J-5 + T-e (p. 373 n. 5); J-6 +
  T-d (p. 360 n. 3); J-9 + T-a (12 sites; anaphora unresolved 391 today); J-11 + T-f (count only). Same discipline as
  ruling 76: report → fix → report; `tools/build-citations.py` only, then `build-citations.py` → `build-index-json.py`;
  no chunk file. Baseline: QA 213, anaphora unresolved 391.

**The front is `bon-luc-c15-v1-7`** (manifest stage 5, `21637e0`, pp. 381–472): it opens at Cap. XV ¶ 1 on p. 381, and
p. 381 nn. 12–13 and the t4 *Impietas Iudaeorum…* are its. Under ruling 86 its first divine `tr-pietas` names the
*impietas / pietas divina / pietas humana* divisio.

# *LUCAM* p. 472 GATE — RULINGS 93–104 (Wilson, 2026-11-17; "Approve all")

Binding summary. Every ⭐ recommendation of `manual-review/vol7-lucam-p472-gate-evidence-sheet.md` was taken as
written, including the four the sheet marked as needing Wilson's own judgment: § 1 *puer* "child(ren)"; § 3
*supplicium* → "penalty", which re-opens one clause of ruling 87; the ~25 pre-interval lines go in now; D-3's scope
clause in ruling 32's row. The passes draft (`manual-review/vol7-lucam-p472-gate-passes-draft.md`) found no defect beyond
the sheet's (its N-1..N-3 are F2, F3, F4; R-1 is F10; O-1 is in § 1). The evidence, censuses and alternatives are in
those two documents, by § and item number, and are not repeated. Gate record: `manual-review/vol7-lucam-p472-gate.md`.
**60 English lines changed: 35 in 13 interval chunks + 25 in 14 pre-interval chunks (one of the 60 is a `tr-`
definition) + Notes records in 28 chunks; no line in any `## Latin` body or `**La.**` half changed.** Four manifest
cells corrected in three rows (ruling 100). Ruling 32's *intellectus* row gains a scope clause (ruling 97); ruling 54 a
clarifying sentence (ruling 93); ruling 18 the passive form (ruling 101); ruling 87's *supplicium* clause is replaced
(ruling 94). No CLAUDE.md change: **`CLAUDE.md:3502` stands.**

- **93. § 1: *puer* the child → "child(ren)"; ruling 54 CLARIFIED** (item 12 [239]; F5; passes O-1). Ruling 54 was
  ratified on the centurion's *puer* (`c7-v1-16`, a servant) and its reason was to keep *puer* off *servus*; it was
  never put to a *puer* who is a child, whom the work had already rendered "child" ~60 times. `c18-v15-17` conformed
  through the pericope, ¶¶ 29–33 (**12 lines**: 6 body, 6 apparatus **En.**): the lemma Luke 18:16–17, the prose, the
  Gloss, and the adduced verses, which return to the Douay's "child(ren)" or are adjusted to it (ruling 20; ¶¶ 29–31
  lean); ¶ 29 *infantium puerorum* "infant children"; p. 460 n. 2 *puer* ("child"), matching p. 283 n. 7. **The three
  "servant" verses keep the Douay** (Job 29:5, Ps. 104:42, Matt. 12:18: the *puer*-as-servant of ruling 54's own verse
  half); Luke 1:54 "his child" stays with `c1-v46-56` ¶ 99 (ruling 28); *infantes* "infants", *parvuli* "little ones"
  unchanged. This closes the four cross-chunk splits the build made (Luke 11:7 at `c11-v5-13` and `c18-v1-8` ¶ 8; Osee
  11:1; I Cor. 14:20; Luke 1:76). **Ruling 54 now reads, with its clarification: *puer* the servant "boy" in prose /
  "servant" in the Douay's verses (`c7-v1-16`, Luke 12:45); *puer* the child "child(ren)".**
- **94. § 3: *supplicium* → "penalty", THE HOUSE RULE RESTORED; `e810ccc` (D-4) RATIFIED** (item 14 [166, 190, 225, 272];
  F1). **The binding rule is `CLAUDE.md:3502`: *poena* → "punishment"; *supplicium* → "penalty"** (Vol VI rulings 20,
  59, 101, 109; carried into Luke by ruling 11). **It stands.** Vol VI ruling 59 made it so because one English word for
  both produced "the punishment of punishment", and refused "torment" as *tormentum* / *cruciatus*'s word. **The
  "*supplicium* 'punishment' / 'torment' by sense; never 'penalty'" line that every builder of the interval carried did
  not come from any ruling.** It came from the orchestrator's briefs for chunks 14–19 of stage 5 and from the
  `e810ccc` correction's framing. Ruling 87 ratified "*supplicium*" as one item of a batch of ruling-20 / 28 splits and
  said nothing about "never 'penalty'"; the p. 381 docket did not put `CLAUDE.md:3502` or Vol VI ruling 59 before
  Wilson. **Ruling 87's *supplicium* clause is therefore replaced by this ruling** (struck in place, kept visible).
  `e810ccc` (the `c17-v20-30` *poena* "punishment" conformation, 2026-11-16) applied `CLAUDE.md:3502` correctly and is
  ratified after the fact. Applied: **16 interval lines** (`c16-v22-31` ×5, `c17-v1-4` ×2, `c17-v20-30` ×3,
  `c17-v31-37` ×2, `c18-v1-8` ×1 (p. 452 n. 1 **En.**), `c18-v9-14` ×1, `c18-v28-43` ×2; 19 Latin sites) **+ 11
  pre-interval lines** (`c9-v37-45` ¶ 83, `c10-v4-16` p. 260 n. 6 **En.**, `c12-v1-7` ¶ 8 ×2 lines, `c12-v49-59` ¶ 87,
  `c13-v1-9` ¶¶ 1–2 ×2 lines, `c13-v22-30` ¶¶ 48, 59, 63, `c14-v16-24` ¶ 49; 16 Latin sites, plus `c12-v1-7`'s elided
  *spirituale* [sc. *supplicium*], whose English supplies the noun). The ten Cap. I–VII "penalty" sites needed no edit.
  Item 14's collision is gone: `c17-v20-30` ¶ 45 "the *punishment*" / ¶ 49 "the *penalty*"; Gregory's ¶ 58 "tormented
  the more in penalties … the punishment of those"; ¶ 52 / ¶ 55 "the bitterness of the penalty". *tormentum* /
  *cruciatus* keep "torment". Builders' register lines saying otherwise are superseded and left as written (each
  chunk's gate paragraph says so). After it the work has one English word for each Latin word, as Vol VI.
- **95. F2 APPLIED: *poena* "penalty" → "punishment"; F3 RECORDED as a sense exception** (passes N-1, N-2). F2, 6
  regions on **1 interval + 5 pre-interval lines**: `c16-v1-8` p. 405 n. 3 **En.** "that I may avoid the
  punishments"; `c12-v49-59` ¶ 86 "exact the punishment for the fault … that punishment is irremediable", ¶ 87 Bede
  "He pays the punishments for his sins", Augustine "not a term of the punishment" (the same line as ruling 94's ¶ 87
  edit), p. 335 n. 9 **En.** "exacts the punishment", n. 13 **En.** "the everlasting punishments"; `c1-v18-25` p. 18
  n. 6 **En.** "paid the punishment" (stiff, as the rule is). **F3: `c16-v19-22` p. 417 n. 12 Chrysostom's
  *magnitudo poenarum* "the greatness of the pains" KEPT, a recorded sense exception to the *poena* row**: Lazarus's
  bodily sores, no penal sense; the precedent is `c13-v22-30` ¶¶ 59–60 *poena sensus / poena damni* "the pain of sense
  / the pain of loss". *poena* → "pain(s)" stands in those three regions only.
- **96. F4, F6, F7, F9 APPLIED** (one word each). F4 (= passes N-3; ruling 86): `c18-v18-27` ¶ 44 Bernard's *Non sic,
  impie* "Not so, **impious one**" (1 line). F6 (ruling 88's house word *simulatio* "dissembling"): `c15-v1-7` ¶ 1, ¶ 5
  "*the dissembling of the equity of justice*", ¶ 5 "by dissembling equity" (2 interval lines) + **8 pre-interval
  lines** (`c6-v1-11` ¶ 6 "the dissembling of hypocrisy" ×2, `c6-v39-49` ¶¶ 99, 105 "a / the deceptive dissembling",
  `c9-v1-9` ¶ 7 "the doubleness of dissembling", `c9-v57-62` ¶¶ 102–105 ×4 lines); Rom. 12:9 "without dissimulation"
  (a Douay verse) and `c15-v1-7` ¶ 2's adverb *simulate* "in pretence" stand. F7 (ruling 71): `c16-v9-18` ¶ 17
  "faithlessness … faithlessness", ¶ 19 "the peril of faithlessness" (2 lines). F9: `c17-v11-19` `tr-praeceptor`
  no longer says the Douay prints "Jesus, master" (`DRC.json`: "Jesus, Master"); it reads "Quaracchi sets the word in
  lower case here; the capital follows the Douay and the earlier sites." (1 line, the one `tr-` definition changed).
- **97. D-3 RATIFIED with a scope clause in ruling 32's row; F8 APPLIED** (item 16 [138, 229, 275]). `c17-v1-4` ¶ 11
  and `c17-v5-10` ¶ 14 keep "the understanding … the affection" (faculty pairs, not the formula; ¶ 14 echoes II Cor.
  10:5 "every understanding"); `c18-v9-14` ¶ 26 (the formula, "intellect") and [275] ratified as built. **Ruling 32's
  *intellectus* row gains: "scope: the locative formula *in intellectu … in affectu* (and the faculty named so)
  'intellect'; elsewhere *intellectus* 'understanding' even beside *affectus*, an echo of a Douay verse following the
  verse"** — the narrow reading of the row, chosen over Vol VI ruling 101's wider one. F8, **2 pre-interval lines**, the
  two locative-formula sites the p. 88 interval left "understanding": `c1-v39-45` ¶ 71 "*the certification of truth* in
  the intellect and *the showing of charity* in the affection and effect"; `c1-v46-56` ¶ 96 "proud in the intellect
  through *presumption* and in the affection".
- **98. § 2: Ps. 35:10 and John 8:12 RATIFIED as built** (item 13 / D-2 [99, 184, 271]; F14). Under the test
  (ruling 27; its unit, ruling 50) `c16-v19-22` ¶ 39 "in thy lumen we shall see lumen" (the prose leans:
  *ex fonte luminis sempiterni*) and `c17-v31-37` ¶ 62 "in thy light we shall see light" (exempt: nothing leans) are
  both right, a ruling-28 split by design; John 8:12 at `c18-v28-43` ¶ 66 "the light of life" is exempt, **the unit
  being the member, ¶¶ 65–66** (*integritas sanitatis*). Recorded in the three chunks' Notes. F14: the docket's Ps.
  35:10 "inconsistency" is the test working (ruling 78's framing). 0 lines.
- **99. § 4: the *pietas* inventory RATIFIED; ¶ 21 kept literal; `tr-pietas` on the adjective RATIFIED; F10 AMENDED**
  (item 15 / D-5 [88, 201, 7, 81, 150, 220, 260]). Nine interval `tr-pietas`, each at its chunk's first divine site;
  the ten human-only chunks without one, as ruling 31 requires. **Ruling 31's "the *pietas* is God's" reads "the word,
  noun or adjective, is God's"** (`c18-v1-8` ¶ 9 *Deum pium*; already so at `c12-v35-48` ¶ 57, ruling 86, and
  `c15-v20-24`, `c15-v25-32`). `c16-v9-18` *invitando ad pietatem divinam* KEPT "inviting to divine piety", no note:
  the ambiguity is the Latin's. **F10 (= passes R-1): the site is ¶ 21, not ¶ 22** — the file and the Vol VII text
  layer agree; item (88) (and the two other "¶ 22" in that chunk's Notes) amended in place, struck wording kept. 0
  English lines.
- **100. § 5: the four manifest cells APPLIED** (item 4 / D-1 [1, 69, 72, 161]; ruling 34: the gate's edit). In
  `manual-review/lucam-chunk-manifest.tsv`: `bon-luc-c15-v1-7` `headings` + `;t4@383R` (*Parabola de ove perdita.*);
  `bon-luc-c16-v1-8` `headings` + `;t4@402R` (*Exemplum parabolicum pietatis providae.*) and `title_la` →
  *Exemplum parabolicum pietatis providae.*; `bon-luc-c17-v20-30` `headings` + `;t4@437R` (*Primo curiositas in
  perscrutando confutatur per tria.*). `bon-luc-c16-v1-8`'s `title_la_source` stays `rubric-t4 p.402R`, now naming the
  lower of the two 402R t4s (the `c18-v18-27` cell's convention). Span, END and confidence unaffected; no other cell
  touched. Batch A (items 1–3, 5–6) RATIFIED: all 19 stage-5 rows as built; ruling 39's five promotions; last ¶ XV 52 ·
  XVI 61 · XVII 62 · XVIII 66; the other 15 titles as built (ruling 36).
- **101. D-7, D-6 and the item 16–19 / 21 batches RATIFIED** (0 lines). D-7: Luke 17:19 "made thee safe" (`c17-v11-19`
  ¶ 34, leaning on *salus*) / Luke 18:42 "made thee whole" (`c18-v28-43` ¶ 65, leaning on *integritas sanitatis*), a
  ruling-28 split recorded in both Notes. D-6: `c17-v31-37` p. 444 n. 8 **La.** *Du-|cange* kept as printed (ruling 9);
  the **En.** half already "Du Cange". Item 17 *pudicitia / puritas* "purity"; item 19 II Pet. 2:5 *praeconem* "the
  preacher of justice" (ruling 32's preface; ruling 30 does not reach quotations); II Pet. 1:19 "a lamp that shineth"
  (ruling 88's lamp class); Prov. 9:8 "Rebuke not a scorner" (ruling 46); Jer. 18:8 "do penance" (the divine subject
  seen); the *Praeceptor* capital (F9 applied, ruling 96); the *dissipare* chain and Ps. 34:16 "were not pricked";
  item 18 *evangelizare* forms, **ruling 18 gaining the passive "is preached as gospel"** (Luke 16:16); Batch C (items
  8–11, the ruling-20 adjustments and ruling-28 splits) with its three records (Luke 11:7 at two chunks, closed by
  ruling 93; *mercenarius / alienigena* and *vindicta* by design; Luke 18:13 "be merciful"); the item-19 and item-21
  house words as batches, with F4, F6, F7 applied. Records: [276] *excedentia desiderii* "exceedingness", *supra nos
  excedimus* "are transported" and passes O-2 (p. 471 n. 1 Vat. *excessum* "excess") under ruling 81's sense clause.
  **Not applied: *segnitia* "slackness"** (`c16-v9-18` ¶ 31, [93]): the sheet left it to Wilson's word ("or record"),
  so it stands "sloth", recorded and carried.
- **102. Batches B, E, F, G RATIFIED; H BANKED** (items 7, 22–31). B: no Corrigenda in pp. 381–472. E: the Quaracchi
  slips as transcribed (r.57 class; ruling 36), incl. p. 471 n. 6 *Psalm. 77, 2* for 87:2 (filed as printed, a J-3
  row) and **Deut. 27:26 without *nec*** transcribed as printed, English "and fulfilleth them in work" (ruling 28),
  recorded, no `[so printed]`. F: the three `[so printed]` (*pedem*, *eundum*, *iuducere*) ratified; `c18-v9-14`
  `title_la` keeps *iuducere*, `title_en` translates "lead" unbracketed; item 24 no mark; zero new `[?]`; **the live
  `[?]` (`c5-v12-16` p. 122 n. 11) STAYS OPEN** (rulings 59, 73, 90). G: guillemets, points, marginalia, codex H,
  set-off verses as recorded; supply nothing. H (item 31): banked, no ruling.
- **103. Records, no text effect.** F13 (*mirus* "wonderful" ~17 / "marvellous" ~14 work-wide; ruling 32's row covers
  *admirabilis · mirabilis · mirari* only; no row made). F14 (ruling 98). Passes O-1 (closed by ruling 93), O-2
  (ruling 101), O-3 (`c16-v19-22` p. 417 n. 6's unglossed Latin variant; record). **Found while applying, not on the
  docket, not edited:** *infidelitas* "infidelity" also stands at `c7-v24-35` ¶ 57 ×2 (*de infidelitate*, *notam
  infidelitatis in cogitatione*) and `c8-v34-39` p. 207 n. 11 **En.** (a variant gloss), and "unbelief" at `c7-v17-23`
  ¶ 37 (Ambrose, *non ex infidelitate*) and `c1-v18-25` p. 18 n. 6 (*infidelitatis … poena*) — the sheet's F7 census ("faithlessness at every site but these three") missed them; for a later docket
  under ruling 71. The status strings (`transcription_status`) of `c15-v1-7`, `c18-v15-17`, `c18-v28-43` keep the
  build's "simulation" / "boys" / "torment" (frontmatter, not rendered).
- **104. F11, F12 and the interval's tool items FOLDED into ruling 76 / 92's ONE tool job, QUEUED, NOT RUN** (sheet
  § T). **J-1** + T-b's twelve + **F11** (`c15-v1-7` p. 386 n. 8 *ex Gregor., loc. cit. n. 15* → `Isai 49:13`, a
  thirteenth wrong anaphor edge): **13 wrong edges**. **J-3** + p. 471 n. 6 *Psalm. 77, 2*. **J-4** (accusative
  *notam M*) **10 interval sites** (F12): p. 382 n. 2 ×2, p. 418 n. 14, p. 434 n. 3, p. 440 n. 10, p. 448 n. 9, p. 463
  n. 1 ×2, p. 466 n. 2 ×2. **J-5** + p. 399 n. 1 *nota. 4.*, p. 433 n. 13, p. 409 n. 8, p. 461 n. 10. **J-6** + p. 423
  n. 1, p. 462 n. 10, p. 470 n. 8 (+3 records). **J-9** + T-a and p. 463 nn. 4, 7. **J-11** + T-f (count only).
  **J-12** + the `CROSSREF_SLIPS` row `("bon-luc-c16-v1-8", "apparatus:p405-10", "supra pag. 403, nota 20", "printed
  slip — p. 403 has 13 notes; the locus is n. 10; filed as printed, not retargeted")`; the direction screen over the
  interval's 159 crossref records finds 0 new slips. T-e by hand at the gate as the docket says. Same discipline as
  ruling 76: report → fix → report; `tools/build-citations.py` only, then `build-citations.py` →
  `build-index-json.py`; no chunk file. Baseline: QA 213, anaphora unresolved 427.

**Manifest stage 6 is NOT drawn.** Stage 5 (`21637e0`) ends at `bon-luc-c18-v28-43`; the manifest has no row past it.
The next step is drawing stage 6 (Cap. XIX ¶ 1 on p. 472 through the p. 540 gate, ruling 2), which needs Wilson's go.

### MANIFEST STAGE 6 — DRAWN 2026-11-20 (Cap. XIX – Cap. XXI, pp. 472–540; 18 rows appended to `lucam-chunk-manifest.tsv`; notes in `lucam-chunk-manifest-notes.md` § Stage 6)

Rows per capitulum: **XIX 7 · XX 5 · XXI 6**. Drawn on Opus on Wilson's go (2026-11-20). Every boundary and every heading
candidate was read on a 300 dpi crop (plates pp. 474–541 extracted this session). The candidates came from a
vertical-gap screen over the plates of pp. 472–541, a divisio sweep and the text layer. The p. 540 gate interval is
these 18 chunks, `bon-luc-c19-v1-10` through `bon-luc-c21-v28-38`. No chunk built; no existing row touched.

**Corrections made by stage 6 (all MEASURED):**

- **Cap. XX's last ¶ is 56, not ~53** (519R, printed *56..*, running across the top of p. 520). **Cap. XXI's last ¶ is
  60, not ~54+** (539R, Vers. 38, running across the top of p. 540). Cap. XIX's is 75 (500R → 501 top), as the table
  has it. Each capitulum's first and last pages are as predicted (472–501, 501–520, 520–540); **none overran.**
- **The p. 540 gate falls at ¶ 60 / `CAPITULUM XXII.` on p. 540 (~0.13 / ~0.155 of the leaf), with `Pars III. De
  passionis medicamento agitur dupliciter.` standing below it on 540L** (then ¶ 1, the italic t2 *Primo, de passione
  quoad quatuor antecedentia.*, un-numbered text, the t3 *Primo, de machinatione proditoris dicuntur quatuor.*). The
  last row ends there. p. 540 n. 1 is `c21-v28-38`'s; n. 2 on, the next interval's.
- No capitulum in the stage is bare (ruling 40 does not arise). Two lemmas print against the Vulgate with an anchor on
  the word, both inside sentence titles, transcribed as printed: c. 19 ¶ 32 *Et tertius venit* (`c19-v20-28`), ¶ 53
  *Exeunte autem illo* (`c19-v36-40`).
- Headings: one t3 (487L, the fourth member of the 288L t3, *Incredulitas Iudaeorum confutatur…*), fifteen t4, no t1
  or t2 before p. 540. The 501L t4 *Secundo confutat Iudaeorum incredulitatem per verba et documenta…* is set as a t4
  but ranks as the 487L t3's second member (the 460R / 472L pattern). Every heading, interior and stacked, is in its
  row's `headings` cell (ruling 100's lesson).

**Corrigenda:** one entry falls in pp. 472–540: **p. 533 col. 2 l. 11 *poterunt* → *poterant***, read on the plate
(Wisdom 17:5 inside c. 21 ¶ 41) → `bon-luc-c21-v25-27`'s `corrigenda` cell. It touches no title (ruling 4).

**`low` rows (9, four decisions).** The alternatives for each are in the notes.

- `c19-v29-35` / `c19-v36-40`: the 487L t3 and 495L t4 stand ~8.1 pp apart, over cap 8 within the estimate's error. Cut
  at ¶ 53, 4.5 + 3.6. Alternative: kept whole (~8.1, one-pass build to 10).
- `c20-v1-9` / `c20-v10-18`: calumnia (¶ 1–9, ~2.4) is under the 2.7 test and ¶ 1–24 (~8.2) over cap 8. Cut at ¶ 14,
  ¶ 1–13 | ¶ 14–24 (3.6 + 4.6), calumnia joined across ¶ 10 (the `c11-v27-32` shape). Alternatives: ¶ 1–9 | ¶ 10–24
  (2.4 + 5.8, Bonaventure's members and the Gospel pericopes exactly); or ¶ 1–20 | ¶ 21–33 (6.4 + 4.8).
- `c20-v27-40` / `c20-v41-47`: ¶ 34–46 | ¶ 47–56 (4.2 + 3.7), the second joined across the 518L t4. Alternatives:
  ¶ 34–51 | ¶ 52–56 (6.1 + 1.9); or ¶ 34–56 whole (~8.0).
- `c21-v1-4` / `c21-v5-11` / `c21-v12-19`: ¶ 1–8 | ¶ 9–17 | ¶ 18–27 (3.0 / 3.8 / 3.4), generaliter joined to
  persecutio and split at ¶ 18. Alternatives: ¶ 1–12 | ¶ 13–27 (4.5 + 5.6, across the 523L t4); or ¶ 9–27 whole (~7.2).

Rule applications with an alternative but not `low`: the parable cut at ¶¶ 22 and 32 (alt. ¶ 25 alone, 3.8 + 6.1);
c. 21 ¶ 41–60 cut at ¶ 48 (alt. whole, ~6.8); the 495L / 498L / 499R sibling t4s kept together in `c19-v41-48`
(alt. ¶ 63–69 | ¶ 70–75).

**The p. 540 gate** (ruling 14: Pars II closes) closes this interval.

# *LUCAM* p. 540 GATE — RULINGS 105–130 (Wilson, 2026-11-20; "Approve all")

Binding summary. Every ⭐ recommendation of `manual-review/vol7-lucam-p540-gate-evidence-sheet.md` was taken as
written, including the six the sheet marked as needing Wilson's own judgment (items 105–110). The passes draft
(`manual-review/vol7-lucam-p540-gate-passes-draft.md`) is folded into the sheet: its N-1..N-4 are items 119, 120, 121,
110; its R-1 is item 122. The evidence, censuses and alternatives are in those two documents, by item number, and are
not repeated. Gate record: `manual-review/vol7-lucam-p540-gate.md`. **18 lines changed in 8 chunks (7 interval chunks +
`c17-v11-19`): 17 English / definition lines + 1 blank line in a Latin body; no Latin word, no `**La.**` half, no
frontmatter field and no manifest row changed.** Ruling 32's table gains three scope clauses (*cultus*, *arguere*,
*ortus*: rulings 112, 113, 115); ruling 69's parenthesis is corrected in place (ruling 110). Notes records in 20 chunks
(the 18 of the interval + `c16-v1-8`, `c17-v11-19`). No CLAUDE.md change.

- **105. *virtus* in `c19-v29-35` → "power" at the eight sites; ruling 47 APPLIED** (D-1 [365]). Ruling 47 stands as
  written: *virtus* "power"; the moral virtue "virtue". **5 lines in `c19-v29-35`** (ll. 91, 99, 111, 113, 298: ¶ 44
  "in sublime power"; ¶ 46 "not by human power, but divine"; ¶ 50 "*the power of the divine precept*", "The power of
  Christ", "*the power of obedience*" (kept with its pair, not (b)), "his power laid open", "the power of the true
  possessor"; p. 490 n. 12 **En.** "the power may stand out") **+ 2 in `c21-v25-27`** (¶ 44 l. 70, p. 534 n. 11 **En.**
  l. 160: *resistendi virtus* "neither power of resisting", found by the census). ¶ 52's *doctrina virtutum* stays "the
  doctrine of the virtues". Both chunks' Notes answered; `c19-v29-35`'s register line amended in place.
- **106. Luke 16:8 "sons" (`c20-v27-40`) / "children" (`c16-v1-8`) KEPT BOTH** (item 12 / D-3 [416]). A ruling-28 split:
  `c20-v27-40` ¶ 40 leans on *filius* (five *filii* phrases read each against the next), `c16-v1-8` ¶¶ 11–12 do not.
  No work rule for *filius*; ruling 93's "child(ren)" is *puer*. Recorded in both chunks' Notes. 0 lines.
- **107. *excidium*: the split KEPT, SCOPED** (item 13 / D-4 [459]). **Scope sentence: "*excidium* 'destruction';
  'overthrow' only where *destructio* stands under it as its member (`c21-v20-24` ¶¶ 28, 35); *eversio* 'overturning'
  in that chunk is the split's cost."** "Destruction" is the work's word at the six other sites (`c19-v36-40` ¶ 62,
  `c19-v41-48` ¶¶ 63, 66, 70, `c21-v5-11` ¶ 14, `c21-v20-24` ¶ 31); "overthrow" stays *subversio* / *eversio*'s word
  elsewhere. (b) "downfall" not taken. 0 lines; Notes of `c21-v20-24` and `c19-v41-48` record it.
- **108. *simulatio* "feigning" in `c20-v41-47` → "dissembling" in the prose; the lemma keeps the Douay** (item 18
  [426]; rulings 88, 96). 4 lines (ll. 96, 98, 106, 108): ¶ 52 "*the dissembling of virtues*"; ¶ 53 "deceived by their
  dissembling"; ¶ 56 "*the dissembling of virtues*" … "on account of the dissembling, because, since dissembling and
  fraud" … "fraudulently and dissemblingly"; ¶ 56 cont. "the sevenfold dissembling". Luke 20:47 "*Feigning long
  prayer*" (l. 106, p. 520 n. 1 l. 300) unchanged: the `c20-v19-26` shape. ¶ 56 has one root for *simulatio* and
  *simulatores*. The `transcription_status` keeps "the feigning of virtues" (frontmatter; ruling 103's practice).
- **109. Ruling 39's nine promotions RATIFIED; Cap. XXI alternative 4(c) NOT TAKEN** (items 2, A-1 [351, 361, 383, 394,
  414, 424, 433, 441, 450]). All four stage-6 decisions stand as built (`c19-v29-35` / `-v36-40`; `c20-v1-9` /
  `-v10-18`; `c20-v27-40` / `-v41-47`; `c21-v1-4` / `-v5-11` / `-v12-19`). 0 lines.
- **110. `tr-praeceptor`: the false clause STRUCK; ruling 69 CORRECTED; the note ADDED at `c21-v5-11` ¶ 12** (D-2
  [443]; passes N-4). (i) `c17-v11-19` l. 347: "; it is the last *praeceptor* of the Gospel and of this commentary"
  struck; the sentence ends "… where it is the Douay's word." (ii) **Ruling 69's parenthesis annotated in place:**
  "one *Praeceptor* left in the work, Luke 17:13" struck → "two, Luke 17:13 and 21:7 (`c21-v5-11` ¶ 12)". (iii)
  `c21-v5-11`: `[^tr-praeceptor]` anchored after "Master" in ¶ 12 (l. 80) and defined ("*Praeceptor* (Luke 21:7, the
  lemma of ¶ 12, *Praeceptor, quando haec erunt*) is rendered "Master", the Douay's word at this verse, as at Luke 5:5,
  8:24, 8:45, 9:33, 9:49 and 17:13. The Latin word is built on *praecipere*, "to enjoin, command". No *magister* stands
  in the paragraph."). **Ruling 49's `tr-praeceptor` is owed at every *Praeceptor* lemma site; ruling 69 fixes one
  sentence of it where *magister* stands, and does not limit the note to those sites** (item (443)'s reading
  corrected). The new note makes no claim to be the last (Cap. XXII–XXIV unbuilt). 3 lines; Vol VII `tr-` notes
  92 → 93, `tr-praeceptor` 6 → 7.
- **111. *cautela* "caution"; the one "wariness" CONFORMED** (item 14 / D-5 [428]). `c20-v19-26` ¶ 30 (l. 82) "the
  caution of the temptation is overcome"; 19 / 19 sites. 1 line.
- **112. *cultus* RATIFIED as built; ruling 32's row gains a scope clause** (item 15 [397, 425, 435]). The row now
  reads: "*cultus* (of God) 'worship'; *cultus vestium / corporis* 'adornment' (`c2-v1-7`); of the soil 'tillage';
  *cultor* 'worshipper' or the Douay's word at a verse ('husbandman' Luke 20:10, 'dresser' Luke 13:7), and *cultura*
  'worship' / 'cultivation', by sense." 0 lines.
- **113. *arguere* the logical act "argue" RATIFIED; ruling 32's row gains the clause** (item 17 [391, 419]): "*arguere*
  the logical act (*potest ex hoc argui*) 'argue'" (`c7-v1-16` ¶ 13, `c12-v13-34` ¶ 36, `c20-v27-40` ¶ 42). 0 lines.
- **114. *denarius* "penny" KEPT; the *denarius / decimus* loss RECORDED** (item 16 [407]). `c20-v19-26` ¶ 30; the
  coin is "penny" at every site, the `c15-v8-10` ¶ 16 precedent. 0 lines.
- **115. *ortus* of trees "birth" RATIFIED** (item 20 [476]). `c21-v28-38` ¶ 50 "birth … going down … fruit". The
  clause the sheet offered is written into ruling 32's row: "*ortus* 'birth' (also of faith, `c17-v5-10`; of man under
  the figure of a tree, `c21-v28-38`); the sun's *ortus* and *ortum habere* 'rising / take its rise'." 0 lines.
- **116. *claritas* and *splendor* both "brightness" RATIFIED** (item 19 [329, 476]); Amos 5:20 keeps the Douay. 0 lines.
- **117. The interval's thirteen `tr-` notes RATIFIED as placed; `tr-lumen` at `c21-v25-27` ¶ 41 as built** (item 21).
  The *lux* / *lumen* rule is not narrowed for the plural *lumina* (alternative (b) not taken); Ps. 4:7 "The lumen of
  thy countenance" at `c20-v19-26` ¶ 30 a ruling-28 split against `c12-v49-59` ¶ 84. 0 lines.
- **118. *intellectus / intelligentia* RATIFIED as built** (item 22); zero bare "intellect" in the interval. 0 lines.
- **119. *poena* "penalty" ×2 in `c20-v27-40` → "punishment"** (passes N-1; `CLAUDE.md:3502`, ruling 94). ¶ 37 (l. 94)
  "the punishment of *unshoeing*"; p. 513 n. 8 **En.** (l. 196) "On the punishment of *discalceatio*". 2 lines.
- **120. Job 36:13 at `c20-v41-47` → "prove", the Douay** (passes N-2). ¶ 56 (l. 108) "dissemblers and crafty men prove
  the wrath of God", as at `c20-v19-26` ¶ 26. The line is one of ruling 108's four; no line added.
- **121. Paragraph shape: the one blank line INSERTED; the four stray English breaks RECORDED** (passes N-3).
  `c20-v10-18`: a blank line before the Latin ¶ 16 (l. 36), so the site no longer renders it inside ¶ 15; no word
  changed (1 line). `c19-v1-10` ¶¶ 5, 7, 9 and `c21-v12-19` ¶ 25 keep their single-newline breaks (render as a space;
  the work's tolerated residue, 102 places in 26 old-ground chunks). (c), a `validate-chunk.py` check for a numbered
  paragraph with no blank line above it, is QUEUED with the tool job (ruling 129).
- **122. The 518L t4 stands at ~0.53 — the two records CORRECTED** (item 4 / D-6 [414, 424]; passes R-1).
  `lucam-chunk-manifest-notes.md` § Stage 6 l. 980 "518L 518.36" → "518.53" (struck figure kept; stage 6's section
  lengths shift to ~2.0 and ~1.7, their sum unchanged); `c20-v27-40`'s item (414) "~0.36" → "~0.53 (plate, p. 540
  gate)" (and the same figure in its Provenance, the same record). The joint, the rows and the chunks are unaffected.
  No English line.
- **123. Batch A RATIFIED** (items 1, 3, 5, 6): all 18 stage-6 rows built as drawn; last ¶ XIX 75 · XX 56 · XXI 60; the
  titles (eight heading, ten sentence), the two lemmas printed against the Vulgate (¶ 32 *Et tertius venit*, ¶ 53
  *Exeunte autem illo*); 32 runovers ledgered (27 gutter, 5 page).
- **124. Batch B RATIFIED** (items 7, 26, 27): the one Corrigenda entry (p. 533 col. 2 l. 11 *poterunt* → *poterant*,
  `tr-corrigenda`); the three `[so printed]` (*novissorum*, *commitiendo*, *itam*); zero new `[?]`. **The live `[?]`
  (`c5-v12-16` p. 122 n. 11) STAYS OPEN** (rulings 59, 73, 90, 102).
- **125. Batch C RATIFIED, ruling 43's shape** (items 8–11): the interval's ruling-20 Douay adjustments, the verses kept
  on the Douay where nothing leans, and the ruling-28 splits (Luke 16:8, James 1:11 / Isa. 40:7, Ps. 4:7, Wis. 2:12,
  *turba* "crowd" on Luke 19:3), as tabled in the sheet.
- **126. Batch D RATIFIED, ruling 71's shape** (items 23–24): the interval's house words as listed in the sheet.
  Recorded: *mirus* stays unruled (ruling 103); *segnitia* "sloth" still carried (ruling 101).
- **127. Batches E–G RATIFIED as transcribed (rulings 36, 57); H BANKED, no ruling** (items 25–29).
- **128. Records, no text effect.** The interval's page-crossing runovers are **five**, not the resume's three: p. 478
  n. 14, p. 485 n. 15, **p. 488 n. 11** (`c19-v29-35`), p. 507 n. 15, **p. 513 n. 14** (`c20-v27-40`); interval
  runovers 32 = 27 gutter + 5 page (253 → 285). D-1 is eight sites on five lines (ruling 105); D-4 is six against two
  (ruling 107). Ruling 69's count was wrong (ruling 110). `c20-v27-40` (414) repeated stage 6's figure (ruling 122).
  **The resume's T-e list enumerates 10 of the interval's 15 newly unresolved anaphors** (the total 427 → 442 is
  right; all 15 are in the sheet's J-9 row). `c20-v41-47`'s "Kept as the Douay" Job 36:13 entry was untrue until
  ruling 120 (now amended in place). `c21-v5-11`'s (443) misread ruling 69 (ruling 110). The `c20-v41-47`
  `transcription_status` keeps "the feigning of virtues" (frontmatter). **Carried again, not on this docket, not
  edited:** *infidelitas* "infidelity" at `c7-v24-35` ¶ 57 ×2 and `c8-v34-39` p. 207 n. 11 **En.**, "unbelief" at
  `c7-v17-23` ¶ 37 and `c1-v18-25` p. 18 n. 6 (ruling 103's five old-ground lines; ruling 71). p. 538 n. 10's *infra c.
  22. n. 2. et 10* is to be checked when Cap. XXII is built.
- **129. The interval's tool items FOLDED into ruling 76 / 92 / 104's ONE job J-1..J-12, QUEUED, NOT RUN.** **J-1** +
  eight wrong edges (p. 479 n. 5 `Act 1:15`; `c19-v20-28` ¶ 37 `1Reg 16:43`, ¶ 34 `Rom 2:12`; p. 488 n. 5 → `bon-luc-c10-v1-3`;
  p. 503 n. 13 `Ps 90:11`; `c21-v1-4` ¶ 2 `Num 30:50`; `c21-v12-19` ¶ 23 `Apoc 11:3`; `c21-v28-38` ¶ 59 `2Tim 4:2`) +
  one doubtful (`c19-v1-10` ¶ 14 `2Par 36`, confidence C); **J-1 / D4** the three page-split body ordinals of
  `c21-v28-38` ¶¶ 50, 54, 57 that emit no record; **J-3** p. 511 n. 1 *Matth. 20, 20* (filed confidence A; wants a
  `CROSSREF_SLIPS`-style annotation), p. 510 n. 4, p. 524 n. 3 (no record); **J-4** the accusative *notam N* at **13**
  interval sites (four `page-multi`); **J-9** the 15 unresolvable *loc. cit. / ibid.* (427 → 442); **J-6 / D5, J-11**
  as tabled; **new:** the `validate-chunk.py` blank-line check (ruling 121). Same discipline as ruling 76: report → fix
  → report; `tools/build-citations.py` (and the one validator check) only, then `build-citations.py` →
  `build-index-json.py`; run after the gate on Wilson's word. Baseline: QA 213, anaphora unresolved 442.
- **130. Plates: pp. 472–539 DELETABLE after the close; pp. 540–541 KEPT** (they serve manifest stage 7), and the eight
  pilot / Corrigenda leaves kept. **The deletion is OWED and needs Wilson's own OK** (a hard stop): `rm
  raw/vision/vol7/p-{472..539}.png` (68 files, ~269 MB; regenerable with `python3.11 tools/extract-pages.py --volume
  vol7 --pages N --dpi 300`). Nothing deleted at this close. The pp. 88–471 plates (384 files, 1,517 MB) are likewise
  left to Wilson.

**Manifest stage 7 is NOT drawn.** Stage 6 ends at `bon-luc-c21-v28-38`; p. 540 nn. 2–10 are PENDING for Cap. XXII. The
next step is drawing stage 7 (Cap. XXII ¶ 1 on p. 540 → the work close at p. 604, ruling 2), which needs Wilson's go;
then the build to the work close, then the Appendix (ruling 7).
