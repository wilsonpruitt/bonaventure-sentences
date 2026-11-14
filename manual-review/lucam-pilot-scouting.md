# Vol VII — *Commentarius in Evangelium S. Lucae*: pilot evidence sheet (2026-11-14, Fable)

Everything below is **MEASURED** (on the plate, or on the text layer and said so) unless labelled **PREDICTION**.
The decisions at the end are **PROPOSALS for Wilson**; nothing here is a ruling until he answers. Vol VII ruling
numbering starts at 1 (`vol7-pilot-setup.md`). The load, the work map, the Tabula divisionum, the full heading
table, the Corrigenda and the mechanics are in `vol7-pilot-setup.md` and are not repeated here.

**No chunk was built, no Vol VI text was touched, nothing was pushed or deployed.**

## What is on the leaves (plates pp. 3, 7, 11, 13, 43, 112, 128, 252, 604)

- **p. 3** opens `PROOEMIUM COMMENTARII IN LUCAM`; numbered ¶¶ from 1, running to the top of p. 7 left column
  ("…totius Libri generalis intelligentia"), ≈ 27 ¶¶ (text layer).
- **p. 7** `PROLOGUS SANCTI HIERONYMI`: the prologue itself is **set in italic and unnumbered**, followed by
  Bonaventure's expositio of it, ¶¶ 1–11, to p. 10.
- **p. 11** the display stack `COMMENTARIUS IN EVANGELIUM S. LUCAE` / `CAPITULUM I.`, then `PROLOGUS EVANGELISTAE.`
  (Luke 1:1–4), ¶¶ 1–6; **p. 12R** `DIVISIO GENERALIS`, where ¶ 7 begins.
- **p. 13** is the hardest leaf seen: ¶ 7 continues across **five stacked headings** (Pars I, tier 2, tier 3, two
  tier-4 rubrics) with un-numbered divisio sentences of Bonaventure's between them, before `8. (Vers. 5.)`.
- **p. 43** c. 1 ¶ 144 (v. 80) closes above a full-measure `CAPITULUM II.`, with a tier-2 heading directly under
  it; a hymn in small type set centred in the right column.
- **pp. 112, 128** the two members of the Tabula's *discipulorum vocatio* open on tier-3 rubrics exactly where the
  Tabula says (c. 5, 1 and c. 5, 27).
- **p. 252** carries the rubric the Corrigenda rewrites.
- **p. 604** a short, irregular last page; no Explicit, no colophon.

## The unit problem, and what the print offers

**The volume index gives no unit** (three lines for the whole commentary). The capitulum is 18–37 pp. So the unit
must come off the body, which marks its joints in two ways:

1. **The editors' rubrics** (tiers 1–4; ≈ 160–180, PREDICTION). They are the Tabula's members plus one finer tier.
2. **Bonaventure's own divisio paragraphs**: a numbered, un-versed paragraph that quotes the lemma and divides it
   ("*Factum est autem* etc. Supra egit de… hic agit de…"). These are the author's joints, and the rubrics are the
   editors' restatement of them.

Where both are present they coincide (checked at c. 1 ¶ 7, c. 2 ¶ 1, c. 5 ¶¶ 1 / 24 / 40 / 63 / 75). So the
proposal is the Ioannem's unit in substance, Bonaventure's pericope, found from the body instead of the index.

**Two draft demonstrations (¶ and page figures from the text layer: PREDICTION until fixed on the plate).**

| Cap. I, 8 chunks | ¶¶ | pp. | Opens on |
|---|---|---|---|
| vv. 1–4 | 1–6 | 11–12 | `PROLOGUS EVANGELISTAE.` |
| vv. 5–17 | 7–30 | 12–17 | `DIVISIO GENERALIS` + the p. 13 stack; parentum conditio, angelica annuntiatio |
| vv. 18–25 | 31–39 | 17–20 | confirmatio, impletio |
| vv. 26–38 | 40–70 | 20–27 | conceptus Salvatoris (≈ 6.8 pp; could split at `Secundo describitur executio ministerii`, p. 22L, or `Tertio … assecutio propositi`, p. 26L) |
| vv. 39–45 | 71–85 | 27–30 | `Secundo, de gratiarum actione pro utraque conceptione.` |
| vv. 46–56 | 86–103 | 30–34 | the Magnificat + `Tertio subditur obsequium benevolentiae` |
| vv. 57–66 | 104–~118 | 34–38 | nativitas Ioannis |
| vv. 67–80 | ~119–144 | 38–43 | the Benedictus (`De laude et gratiarum actione ponuntur duo`, p. 38L) + `De educatione pueri…` |

| Cap. V, 5 chunks | ¶¶ | pp. | Opens on |
|---|---|---|---|
| vv. 1–11 | 1–23 | 112–118 | `Primo, quomodo vocentur discipuli de statu iustitiae` (112R) |
| vv. 12–16 | 24–39 | 119–123 | divisio ¶ 24 |
| vv. 17–26 | 40–62 | 123–128 | divisio ¶ 40 |
| vv. 27–29 | 63–74 | 128–131 | `Secundo, quomodo vocentur discipuli de statu culpae` (128R) |
| vv. 30–39 | 75–85 | 131–134 | divisio ¶ 75 |

**Scaled to the work: ≈ 140 commentary chunks + 2 front-matter chunks ≈ 142, mean ≈ 4.2 pp (PREDICTION).** For
comparison: ≈ 165 at the Ioannem's 3.6 pp; ≈ 280 if every rubric were a chunk; 24 if the capitulum were.

## What a chunk costs, measured on the Ioannem (this session; 108 Opus chunk-agent transcripts matched to `vol6/` chunks)

| Chunk span (pages touched) | Agents | Median turns | Output tokens | Cache-write | Cache-read | Cache-read per page |
|---|---|---|---|---|---|---|
| 2 | 15 | 73 | 5.5K ⚠ | 239K | 13.4M | 6.7M |
| 3 | 31 | 94 | 71K | 298K | 20.6M | 6.9M |
| 4 | 32 | 88 | 87K | 336K | 19.9M | 5.0M |
| 5 | 22 | 112 | 100K | 359K | 24.8M | 5.0M |
| 6 | 7 | 85 | 107K | 420K | 28.9M | 4.8M |

(⚠ the 2-page row's output median is implausibly low; some transcripts under-record output. The cache columns are
the reliable ones.) **Ioannem total across the 108: 6.7M output · 35M cache-write · 2.17B cache-read.**

Two things follow. **A chunk of 4–6 pages costs about 30 % less per page than one of 2–3 pages** (fixed
per-agent overhead), which is a measured reason for the 3–6 pp target, on top of the structural one. And the Luke
build can be priced: see proposal 15.

## Register census (text layer over pp. 3–604, apparatus INCLUDED, stems; approximate. ⛔ Census the BUILT text at every gate)

| | | | |
|---|---|---|---|
| Glossa 1,232 | Beda 1,011 | Augustinus 384 | Gregorius 357 |
| Hieronymus 315 | Ambrosius 311 | Chrysostomus 152 | Bernardus 124 |
| praedicare 432 | praedicatio 95 | praedicator 82 | evangeliza- 45 |
| signum 286 | pauper- 277 | paupertas 82 | mendic- 49 |
| caritas 242 | amor 160 | dilectio 87 | eleemosyn- 64 |
| misericordia 234 | pietas 155 | impiet- 53 | benignit- 47 · clementi- 32 · compassi- 23 · miserati- 13 |
| doctrina 221 | doctor 75 | magister 72 | magisterium 13 · praeceptor 19 |
| lux 151 | lumen 92 | humilitas 176 | sacerdot- 188 |
| poenitentia 148 | poena 107 | supplicium 38 | publican- 75 |
| parabola 142 | mysterium 125 | sacramentum 30 | erudi- 98 · informat- 73 |
| contemplat- 104 | perfectio 78 | praelat- 67 | religios- 19 |
| mystic- 34 | Spiritualiter 14 | allegoric- 11 | Moraliter 7 · anagogi- 6 · tropologi- 3 |
| remedi- 59 | medicament- 5 | tropae- 8 | "Et nota / Nota" 203 |
| Vat. 1,461 | codd. 857 | Vulgata 551 | Lyranus 208 · Card. Hugo 163 · Greek 54 |

Reading it: this is a **preacher's commentary** (the *praedic-* family is over 600 sites, with *praelatus* and
*paupertas* behind it), built on the **Glossa and Bede** (over 2,200 named sites between them, against the
Ioannem's Augustine-and-Chrysostom base), and its apparatus is dense (≈ 12 notes per page on the plates read).
The mercy vocabulary is the Luke-specific register load: *misericordia*, *pietas*, *benignitas*, *clementia*,
*compassio*, *miseratio* are six nouns the English has to keep apart, and the Tabula makes *impietas / pietas
divina / pietas humana* the frame of cc. 15–16.

## Inbound and internal citation shapes (MEASURED)

≈ 24 already-built chunks cite this work by **chapter + verse** ("Comment. in Lucam c. 9. v. 34", "c. 22, 19").
The work cites itself by **c. + n.** (≈ 301 `supra / infra n.` sites) and the Index rerum by **page + paragraph**.
A verse-range id with a `paragraphs:` field serves all three.

---

# PROPOSED RULINGS 1–16 (for Wilson; recommendation first, alternatives with their cost)

**1. Chunk unit = Bonaventure's own pericope, bounded by joints the print marks.**
(a) A chunk never crosses a `CAPITULUM` heading (`division:` = the capitulum).
(b) Every boundary is a joint the print itself marks: an editorial heading, or, where headings stand more than
~8 pp apart, one of Bonaventure's divisio paragraphs.
(c) Not every rubric is a boundary. Sibling rubric sections stay together up to the size target: **3–6 pp, cap 8,
one-pass build to 10.** A stacked heading cascade (p. 13) opens one chunk, never several.
(d) **A boundary always falls at the START of a numbered paragraph** (or at a heading standing between
paragraphs), never inside one, even where the editors set a heading inside it (c. 1 ¶ 7 stays whole).
(e) id `bon-luc-c{N}-v{a}-{b}`, `verses: "a-b"`, `type: pericope`, `paragraphs: "40-70"`.
— *Alt A: the capitulum (24 chunks of 18–37 pp).* Cost: every chunk a two-pass build larger than anything the
corpus has made; refused for Ecclesiastes and the Ioannem on smaller chapters.
— *Alt B: every rubric a chunk (≈ 280).* Cost: about twice the agents, many chunks under one page, and by the
measurement above roughly 30–40 % more tokens per page.
— *Alt C: fixed verse-pericopes of our own (a lectionary's, say).* **Refused in principle:** it would cut where
neither Bonaventure nor the editors cut.

**2. The chunk manifest is drawn BEFORE the build, in stages, and it is the build's only source of spans.**
`manual-review/lucam-chunk-manifest.tsv`: one row per chunk (id, verses, ¶ range, pages, the opening joint and
its tier, `title_la` source, Corrigenda entries falling in it, a confidence flag). Drawn from the text layer
(paragraph starts, `(Vers. N.)` tags) with **a plate crop read at every boundary** (≈ 150 column crops for the
work, not a page-by-page read). **Stage 1 = Cap. I–III (Pars I) before any chunk is built; after that the
manifest stays complete through the NEXT gate before that interval's first chunk is built.** You rule on the
rule; the rows are mine to draw and yours to spot-check at each gate. A builder who finds a row wrong on the
plate stops and reports; the manifest is amended in its own commit.
— *Alt: no manifest; each builder finds its own END (the Ioannem method).* Cost: the Ioannem builders had the
index's pericopes to aim at. Here each agent would be choosing a boundary by judgment, 140 times, by 140 agents of
different rigor, and a boundary chosen badly is invisible afterwards.
— *Alt: the whole manifest up front.* Cost: ≈ 150 crops before the shakedown has tested the rule once.

**3. Front matter = TWO chunks, division 0** (the Ioannem's ruling 70): `bon-luc-prooem` (section 1,
`type: prooemium`, pp. 3–7) and `bon-luc-prol` (section 2, `type: expositio`, pp. 7–10: the *Prologus S.
Hieronymi* **transcribed and translated as text**, in italic as printed, followed by Bonaventure's expositio
¶¶ 1–11). **The p. 11 display stack, `CAPITULUM I.` and `PROLOGUS EVANGELISTAE.` go to `bon-luc-c1-v1-4`.**
— *Alt: one chunk, pp. 3–10.* Cost: 8 pp with two paragraph-number sequences in one file, so `paragraphs:` would
be ambiguous in the one place the work restarts its numbering outside a capitulum.

**4. Headings: all five tiers transcribed in place, in both languages, with their typography; editorial, and said
so once.** `CAPITULUM N.` → `### Capitulum N.`; tiers 1–4 → `####`, keeping the print's italic (tier 2) and plain
roman (tiers 1, 3, 4), as the Ioannem did on p. 250 (`#### Pars. II. …` / `#### *Primo tractatur…*`). Each
chunk's Notes state that the headings are the Quaracchi editors'. **No `pars:` field; breadcrumb `Cap. N, Vers.
a-b`** (ruling 71 of Vol VI). `title_la` = the chunk's governing rubric, **as amended by the Corrigenda**; where
a chunk opens on a divisio paragraph with no rubric, the lemma plus Bonaventure's own dividing words.
— *Alt: drop tier 4 as furniture.* Cost: tier 4 is where the reader finds the argument's joints, and Quaracchi's
own apparatus refers to them ("secunda nostra rubrica").
— ⚠ Tiers 1, 3 and 4 differ in the print only by size and weight, which `####` flattens. **Recommended: accept
the flattening** (the Ioannem did). *Alt: a fifth heading level.* Cost: a renderer change for a distinction the
wording already carries (*Pars…*, *Primo…*, *Primo describitur…*).

**5. `paragraphs:` = the numbered paragraphs that BEGIN in the chunk.** With 1(d) every numbered paragraph
belongs to exactly one chunk, so `c. N. n. M` resolves to one file. Paragraph numbers are kept verbatim at
paragraph heads in both languages. Un-numbered divisio text standing between headings is transcribed where it
stands and belongs to the paragraph it continues.

**6. The `TABULA DIVISIONUM PRINCIPALIUM` is NOT a chunk.** It is Prolegomena, the editors' diagram; Prolegomena
are not chunked in this corpus. It is the manifest's skeleton and the source of the gate positions (proposal 14).
— *Optional, later, your call:* an English outline of the four Partes on the work's landing page, built from the
Tabula after the work closes. Not proposed now.
— *Alt: chunk it as `bon-luc-tabula`.* Cost: an editorial table presented beside Bonaventure's text as if it
were his, in a corpus that has refused that twice (the Breviloquium's capitula table; the Vol VI Prolegomena).

**7. The Appendix (pp. 605–655): IN SCOPE, AFTER Luke closes, as two separate small works, each labelled as the
editors label it.** *Expositio Threnorum Ieremiae* (45 pp, ≈ 10–12 chunks, PREDICTION) and *Expositio Orationis
Dominicae* (4 pp, 1 chunk). The editors print both under `APPENDIX DUORUM OPUSCULORUM SALTEM DUBIORUM`: "at the
least doubtful." Each gets its own registry entry carrying that status in its title line and landing text, and
its own short scouting sheet when it comes up. Nothing about their chunking is decided here.
— *Alt A: skip them.* Cost: Tome VII would be the first volume on the site not translated entire, 49 pp short.
— *Alt B: do the Oratio Dominica now as a warm-up.* Cost: a different genre's register ahead of the work the
session is tuned for; no saving.
— **This is a scope decision and it is yours.** It can also simply wait: nothing in the Luke build depends on it.

**8. CORRIGENDA CONVENTION (corpus-level; there is none today). Quaracchi's own Corrigenda are the edition's
text.** Where the Corrigenda correct a reading: the **Latin carries the corrected reading**, the **English
translates the corrected reading**, and **one numbered translator's note, anchored at the word,** records the
printed reading and the source: *"Printed: … ; corrected by the editors, Corrigenda, t. VII p. 858."* Addenda to
the apparatus (p. 16, p. 624) are added to the note they extend, marked the same way. This is distinct from
`[so printed: …]`, which stays the mark for a misprint **we** caught and the editors did not.
The 16 Luke entries are applied at build; the manifest names them per chunk so the builder is handed them (a
builder reading only the plate would transcribe the superseded text, the p. 252 rubric above all).
— *Alt: print as printed, corrigendum in a note.* Cost: the site would carry readings the editors themselves
withdrew, *a Virgine et domo* for *et Deo* among them, and the English would translate a known error.

**9. The five unapplied Vol VI corrigenda are fixed now, as one bounded job** (five edits in `bon-sap-c17`,
`bon-ioan-c1-v9-14`, `bon-ioan-c15-v1-11`, `bon-ioan-c19-v28-37`, `bon-cioan-c8`; one note updated in the
`bon-cioan` chunk holding p. 551, where the bracket becomes a confirmed corrigendum). Three of the five change
the English (p. 252 moves ¶ 25's number and makes *In mundo erat* a lemma; p. 447 joins two sentences; p. 501
moves a quotation's opening). Each site is read on its plate first. **This is a located cause, six named sites,
not a repass.** Vol VI is pushed and deployed (2026-11-07), so the fixes are a local commit that goes live
with the next deploy you call (proposal 14 recommends p. 88); no deploy is asked for on their account.
— *Alt: leave Vol VI as deployed.* Cost: five readings live on the site that the edition corrects in print.

**10. Vols I–V: INVENTORY the Corrigenda leaves, apply nothing.** Vol V's raw has a `CORRIGENDA ET ADDENDA`
leaf of ≈ 20 entries; the Vol II / III / IV raws mention `CORRIGENDA` (1 / 2 / 2 hits); Vol I unchecked. One
short session (Sonnet-shaped: locate each leaf, transcribe its entries off the plate, check each against the
built chunk, write `manual-review/corrigenda-inventory.md` with applied / unapplied per entry). You rule on
applying when you see the count. It is queued behind the Luke manifest, not ahead of it.
— *Alt: skip.* Cost: unknown, which is the problem; Vol VI's rate was five unapplied of six.

**11. Register carried unchanged from Vols V and VI** (restated so the builders have one list): *lux* → light /
*lumen* → "lumen" with `tr-lumen` and the verse test (ruling 2) · *magister* → "teacher", inside the Douay
quotations too; Lombard "the Master" in the apparatus · *signum* → sign, *miraculum* → miracle · *caritas* →
charity / *dilectio* → "dilection" / *amor* → love · *doctrina* and `tr-doctrina` (ruling 11) · the *vacare*
rule and `tr-vacare` · ***pietas* → "piety" everywhere** · *eruditio* → "erudition" (it collides with
*instructio* → "instruction"; Vol VI ruling 93) · *supplicium* → penalty / *poena* → punishment · *intellectus* /
*intelligentia* · *Glossa* → "the Gloss" · *Evangelista* → "the Evangelist" · the lemma = Douay adjusted to
Quaracchi's Vulgate · spelling as ruled for the Ioannem (ruling 155: scoped per work; **recommend Luke takes the
Ioannem's spellings**, the two Gospel commentaries reading as one hand).

**12. Register new to Luke (adopt as the working register; the shakedown gate reviews it with sites in view):**
- **The mercy nouns stay six words:** *misericordia* → mercy · *pietas* → piety · *benignitas* → kindness ·
  *clementia* → clemency · *compassio* → compassion · *miseratio* → "commiseration" in Bonaventure's own prose
  (13 sites, most of them inside psalm quotations, where the Douay's wording at that verse stands).
- ⭐ ***pietas divina* in cc. 15–16.** The standing rule gives "the impiety of the Jews / the divine piety /
  human piety" for the Tabula's triad. **Recommended: the rule holds**, with a `tr-pietas` note at the first
  site of each chunk where the *pietas* is God's, saying that the Latin word covers a father's tenderness toward
  his own and that Bonaventure sets it against *impietas*. Reason: the triad is one word turned three ways, and
  only one English root shows that. **Reviewed with the sites in view at the gate before c. 15 (p. 381).**
  — *Alt: release it for God's pietas alone* ("the divine tenderness"). Cost: the hinge of cc. 15–16 disappears
  in English, and a rule ratified at every gate since the *De septem donis* gets its first carve-out.
- ***praedicare* → to preach, *praedicatio* → preaching, *praedicator* → preacher**, never "proclaim" (*praedicare
  de* in the logical sense stays "to predicate"). ***evangelizare* → the Douay's "to preach the gospel"**, which
  keeps it apart from *praedicare* by the word "gospel".
- ***magisterium* → "teaching office"** (the majority rendering in the built Vols V–VI, 11 sites against 8 "magisterium"); the Pars
  II heading reads "On the teaching office of preaching". — *Alt: "magisterium".* Cost: the modern ecclesial
  sense arrives with it.
- ***Praeceptor*** (Luke's own vocative, 5:5, 8:24, 9:33 …; 19 sites) → **"Master"**, the Douay's word, which
  *magister* → "teacher" has left free. One `tr-praeceptor` note at 5:5.
- *paupertas* → poverty, *pauper* → poor / "the poor man", *mendicus* → beggar, *mendicitas* → beggary,
  *eleemosyna* → alms, *avaritia* → avarice, *liberalitas* → liberality.
- *remedium* → remedy / *medicamentum* → "medicine" (Pars III: "the medicine of the passion") · *tropaeum* →
  "trophy" (Pars IV) · *mysterium* → mystery / *sacramentum* → sacrament, never interchanged.
- *informatio*, *informare* (73 sites; the Tabula's *informatio discipulorum*) → **"formation", "to form"**,
  kept apart from *instructio* → instruction and *eruditio* → erudition.
- The sense labels: *Moraliter* → "Morally", *Spiritualiter* → "Spiritually", *mystice* → "mystically",
  *allegorice* → "allegorically", *ad litteram* → "according to the letter".
- *publicanus* → publican, *legisperitus* → lawyer (Douay), *sacerdos* → priest, *sacerdotium* → priesthood.
- The canticles keep their Latin incipits as names in the English (*Magnificat*, *Benedictus*, *Nunc dimittis*);
  their text is the Douay adjusted, as any lemma.
- **Title:** `Commentarius in Evangelium S. Lucae` (half-title and p. 11 display form; running head `Comment. in
  Evangelium Lucae` recorded) → **"Commentary on the Gospel of Luke"**.

**13. Registry and ids.** Slug **`lucam`** (the accusative, as `ioannem`), id prefix **`bon-luc-`**, **book 19**,
tome 7, initial "L", `divisionLabel: "Capitula"`, divisions `0: Prooemium`, `1..24: Capitulum N`; the title
builder's `ioannem` branch (`Cap. N, Vers. a-b`) takes `lucam`. Goes in with `bon-luc-prooem`. A new citation
class for "Comment. in Lucam c. N. v. M" so the ≈ 24 existing inbound sites land on chunks as they are built
(forward-resolving until then). (Not really yours; on the record.)

**14. Cadence = EIGHT gates, placed on the Tabula's joints.** Shakedown at **p. 27** (prooem, prol and the first
four chunks of c. 1, through the Annunciation: 25 pp, with the p. 13 heading stack, the Glossa-and-Bede
apparatus and the Annunciation's register inside it) · **p. 88** (Pars I closes; c. 1–3) ·
**p. 188** (close of c. 7) · **p. 288** (c. 11 v. 13: the first half of Pars II closes) · **p. 381** (close of
c. 14; the *pietas* review sits here, before c. 15) · **p. 472** (close of c. 18) · **p. 540** (Pars II closes)
· **work close at p. 604** (Pars III and IV). Intervals 61–100 pp, the Ioannem's spacing.
**Deploys: ONE by default, at p. 604; every gate is a legitimate deploy boundary you may call, per action.**
**I recommend you call p. 88:** Pars I is Luke 1–3, the Annunciation to the genealogy, and at the Ioannem's pace
(109 chunks in 18 days) its ≈ 21 chunks would be gated in early December (PREDICTION), in time to be live for
Advent and Christmas.
— *Alt: five gates (drop pp. 188, 472, 540).* Cost: runs of 200 pp reviewed only once.

**15. Build cadence, and what it will burn.** One Opus agent per chunk, incremental-append from the start, the
Vol VI session loop unchanged (one chunk, two commits, next chunk; STOP at each gate). Plates at 300 dpi.
Apparatus counted from the plates, never the raw. Planning figure ≈ 12 notes per page, so ≈ 40–60 entries per
chunk: a prompt to recount, never a gate.
**PREDICTION for the whole commentary, scaled from the measured Ioannem (602 pp against 294; ≈ 142 agents):
≈ 12–14M output tokens, ≈ 60–70M cache-write, ≈ 3.5–4.5B cache-read, on Opus. About twice the Ioannem.**
⛔ **This is a big token burn and a hard stop of its own: nothing launches on this sheet.** The question "which
model, and go?" is asked when the manifest's first stage is drawn and the shakedown chunks are ready to
dispatch, with the figure restated for that interval.

**16. The manifest's first stage is the next job, and it is small.** Cap. I–III: ≈ 20 boundaries (PREDICTION), ≈ 25 column
crops, one session. Model: the rule is written here, so drawing rows is rule-application with a plate check;
**Opus is enough**, with any row it flags as low-confidence left for you or a Fable look at the shakedown gate.
— *Alt: Fable draws stage 1.* Cost: premium tier for work whose judgment is already spent in proposal 1.

---

**The front after the rulings:** (1) record the rulings in `vol7-pilot-setup.md`; (2) if 9 is approved, the five
Vol VI fixes (their own commit); (3) the manifest, stage 1 (`manual-review/lucam-chunk-manifest.tsv`, Cap. I–III,
plus the two division-0 rows); (4) the registry entry and tool wiring that the first chunk needs; (5) STOP for
"which model, and go?" before `bon-luc-prooem` (pp. 3–7; fix its END on p. 7 alone first, from the `PROLOGUS
SANCTI HIERONYMI` heading).

**Still open on the evidence (assigned, not blocking):** the true heading inventory (manifest) · the last ¶
numbers of cc. III, IX, X, XII, XIII, XV, XX, XXI, XXIII (manifest) · whether the Threni has a Cap. V (the
Appendix's own scouting) · the Tabula's two suspect verse references, c. 1, 30 and c. 13, 21 (manifest).
