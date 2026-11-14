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
| II | 43–69 | 110 (v. 52) | | XIV | 358–381 | 68 |
| III | 69–88 | ~63 | | XV | 381–402 | ~50+ |
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

**Five of six are unapplied in a deployed volume.** And the wider finding: Vol V's raw has its own
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
