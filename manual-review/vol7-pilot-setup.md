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
| II | 43–69 | **111** (corrected at manifest stage 1: ¶ 111 is an un-versed epilogue, 69R) | | XIV | 358–381 | 68 |
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
  `tr-evangelizare`. The struck sentence is kept visible.]** *magisterium* → "teaching office". *Praeceptor* → "Master" + `tr-praeceptor` at
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
  off *praedicare*); **where the Douay itself says "bring good tidings" (1:19, 2:10: an angel bringing a message,
  with an object), the Douay stands, with `tr-evangelizare` at each chunk's first site.** 8:1 *praedicans et
  evangelizans* keeps the Douay's "preaching and evangelizing". Both *bona nuntiatio* renderings stand ("good
  announcement" where the gloss hangs on *annuntiare*, prooem ¶ 14; "good tidings" where it hangs on
  *evangelizare*, `c1-v18-25` ¶ 31). `c1-v18-25` ratified as built, 0 lines; the prooem Notes' claim that 4:43
  "preach the gospel" is the Douay's wording is corrected.
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
