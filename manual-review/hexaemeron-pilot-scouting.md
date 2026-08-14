# *Collationes in Hexaëmeron* — mini-pilot scouting (work 8, Vol V)

Evidence gathered 2026-08-14, immediately after `de-reductione` shipped. **This file is the
evidence base, not the conventions freeze** — the freeze (chunk unit + register + what
happens to the Summarium) is the pilot's own decision and is listed at the end as OPEN,
with a recommendation and the argument for it.

Slug `hexaemeron`, **book id 11**, already reserved in the `WORKS` registry comment block.

## Banked — do NOT re-derive

- **✅ p. 326 MEASURED BLANK — 1,546 ink px** at 450 dpi (a text leaf on this stock runs
  565,000–790,000). Checked, not assumed.
- **✅ p. 327 IS THE HALF-TITLE**, read on the plate: `SERAPHICI DOCTORIS / SANCTI
  BONAVENTURAE / COLLATIONES IN HEXAËMERON / SIVE ILLUMINATIONES ECCLESIAE`.
  ★ **Two things to carry:** the title prints with a **diaeresis — HEXAËMERON** — and the
  work has a **transmitted alternate title**, *sive Illuminationes Ecclesiae*, which p. 329
  n. 1 then documents from the codices.
- **✅ p. 328 MEASURED BLANK — 3,527 ink px** (twice p. 326's, still ~0.5 % of a text leaf;
  the excess is show-through from the half-title's heavy type).
- **✅ THE BODY OPENS ON p. 329**, not 327 as the work map's "~327–454" implied. The map's
  range is an estimate and the front matter eats two leaves of it.
- **Raw range: L57174 → ~L76290.** `COLLATIONES IN HEXAEMERON` half-title at **L57174**,
  `COLLATIO I.` at **L57180**, and the ***Collationes de septem donis*'s own `COLLATIO I.`
  at ~L76291**, which fixes the far end. **~19,100 raw lines — about 17× `de-reductione`,
  and the largest single work in Vol V by a wide margin.**
- **✅ TWENTY-THREE COLLATIONES (I–XXIII)**, counted from the bare `COLLATIO N.` headers in
  the raw and cross-checked against the volume's own index, which lists exactly these.
  Raw offsets of the headers (relative to L57174): I +7 · II +1054 · III +2088 · IV +3041 ·
  V +3792 · VI +4844 · VII +5590 · VIII +6145 · IX +6680 · X +7386 · XI +7747 · XII +8533 ·
  XIII +8988 · XIV +9764 · XV +10622 · XVI +11344 · XVII +12263 · XVIII +13060 ·
  XIX +13858 · XX +14603 · XXI +15623 · XXII +16527 · XXIII +17635.
  ⚠ The running head `IN HEXAËMERON COLLATIO N.` fires far more often than the real header
  and garbles hard (`IN HEXAiiMERON`, `IN IIKX/VKMEKON`, `IN HEWKiMERON`). **The real header
  is the bare `COLLATIO N.` on its own line**, itself OCR-garbled (`COLLATIO L` = I,
  `COLLATIO IL` = II, `COLLATIO IIL` = III, `COLLATIO lY` = IV, `COLLATIO VL` = VI …).
- **Gutters, first leaves:** 329 = **1201** (62 px run) · 330 = **1347** (63 px) ·
  331 = **1249** (61 px) — all three healthy and the tool's default plausible on each.
  ⚠ **pp. 327 and 328 return 450 px and 463 px "runs"** — the min-collection artifact on a
  page with no columns at all. **A wide run on a front-matter leaf is the tool telling you
  there is no gutter, not that it found a wide one.**

## The shape of a collatio, read off p. 329

Four regions, stacked, in three different measures:

1. **`COLLATIO I.` — and it carries apparatus anchor ¹.** The note documents the work's
   title in the codices (*Illuminationes Ecclesiae in Hexaëmeron*; Vat., Argentina 1495,
   Venice 1504, and the ascription question) — i.e. **the edition annotates the collatio
   division itself.**
2. **The subtitle**, full measure, two lines — the same words the volume index gives
   (*De qualitatibus in auditoribus divini verbi requisitis et de Christo omnium
   scientiarum medio*).
3. **★★ THE `SUMMARIUM` — a full-measure editorial synopsis in small italic, keyed to the
   collatio's paragraph numbers** (*Ex textu eruitur materia trium priorum collationum
   tripliciter divisa, numero 1. — Pars I. In auditoribus tria requiruntur, 2. — De his
   tribus specialiter, 3-5. — … Pars II. De Christo, qui est medium omnium scientiarum,
   10. — …*). **Nothing in the Sentences, the Breviloquium or the Itinerarium has this
   shape.** ⚠ Note it uses *Pars I / Pars II* for the collatio's matter — **a division that
   exists in the synopsis and, so far as p. 329 shows, nowhere in the text.**
4. **The two-column body**, numbered paragraphs (1., 2., 3. …), **with marginal glosses as
   well** (`Divisio.` · `Pars I. Ecclesia et synagoga.` · `Tria requiruntur.` · `De
   observantia legis.` · `Ecclesia columna et firmamentum.`). **So this work carries BOTH
   a Summarium and marginalia** — the marginal apparatus is not replaced by the synopsis.

**★ THE FROZEN TEST APPLIED, and it splits the two editorial elements apart:**
- **The COLLATIO carries apparatus** (anchor ¹ on the heading) → it is a division the
  edition annotates.
- **The SUMMARIUM carries NO anchor** — verified at magnification on p. 329; the numbers
  inside it are paragraph references, not footnote markers.

## ⬜ OPEN — the pilot's decisions, with recommendations and the arguments

**1. Chunk unit → RECOMMEND the collatio (23 chunks, ~5.5 printed pp each).** Three
witnesses point one way: apparatus attaches to the `COLLATIO N.` heading; Quaracchi cite the
work as `Hexaem. coll. N. n. M`, so the collatio is the citation unit exactly as the
capitulum was in the Breviloquium; and the volume index lists precisely these twenty-three
and nothing finer. ⚠ **Do not chunk on the *visiones*** — the index's descriptions group the
collationes into visions (*De prima visione tractatio prima*, …), but **a grep of the whole
work returns ZERO `VISIO` headings in the body**: the visions are a description of the
matter, not a printed division. Same class as `de-reductione`'s marginal `Pars`.
⚠ ~5.5 pp per chunk is **larger than any unit yet worked** except `bon-red` itself (7 pp),
so the incremental-append method is not optional here.

**2. What happens to the SUMMARIUM → RECOMMEND rendering it as a labelled section, NOT
trimming it to Notes.** The obvious move is to treat it like marginalia — editorial,
unanchored, trim it — but **that is the wrong precedent, and the corpus already shows why:
Quaracchi's *scholia* are equally editorial and the corpus renders them in full, in both
languages.** The real rule the corpus follows is not "editorial ⇒ trim"; it is **marginal
glosses are trimmed, display matter set in the text block is rendered.** The Summarium is
display matter set full measure in the text block, and it is the reader's only map of a
five-page reportatio. Suggested shape: a `### Summarium` section at the head of each
chunk's language block, with its paragraph references preserved verbatim.
⚠ **If it is rendered, the parser gotcha applies in reverse** — `extractLanguageBlock`
terminates the block only on known sentinel headings, and `### Scholion` must be LAST;
a `### Summarium` heading needs adding to the sentinel list or the body will parse wrong.
**Test this on the pilot chunk before the grind, not after.**

**3. Register → OPEN, and this is the judgment-dense part.** A *reportatio* register nobody
in this corpus has touched: *collatio* itself, *visio*, *theoria*, *radius*, *semen* /
*germinare* (the seeds-and-fruits language of collationes XV–XVII), *medium* in the seven
senses of Collatio I (*medium essentiae / naturae / distantiae / doctrinae / modestiae /
iustitiae / concordiae*), and the *illuminationes* of the alternate title. Settle these on a
pilot collatio and freeze them in repo CLAUDE.md before any grind dispatch.

**4. Gate cadence → three gates, not the two page count alone gives** (~128 pp), per the
frozen table, **plus a shakedown gate ~15–25 pp in** — i.e. after roughly Collatio IV.
Deploy boundary is the work close, or per-gate if Wilson wants it read sooner.

## ✅ CONVENTIONS FROZEN 2026-08-14 (`44004fa`) — see repo CLAUDE.md § HEXAEMERON

Chunk = the collatio (24 chunks: `bon-hex-c{1..23}` + `bon-hex-scholion`); the Summarium is
**rendered** as `### Summarium`, not trimmed; the visiones are never a boundary; registry
entry + a `Coll. N` title branch are wired in `build-content.mjs`. ⚠ Parser checked: an
`### Summarium` at h3 does not terminate `extractLanguageBlock`, so no sentinel change was
needed.

## ▶ PILOT CHUNK `bon-hex-c1` — IN PROGRESS, span pp. 329–336 (fixed on the raw + band)

**Collatio I runs pp. 329–336**, 39 numbered paragraphs (the Summarium's own last reference
is `37-39`); **Collatio II opens on p. 336**, so this chunk ends mid-leaf there. Raw
L57180 → L58227.

**Gutters — all eight measured; the tool's default REJECTED on two.**

| p. | default | run | true band | adopted |
|---|---|---|---|---|
| 329 | 1201 | 62 px | 1170–1234 | **1202** |
| 330 | 1347 | 63 px | 1314–1378 | **1346** |
| 331 | 1249 | 61 px | 1217–1280 | **1249** |
| 332 | 1349 | 60 px | 1315–1379 | **1347** |
| 333 | 1185 | 61 px | 1152–1216 | **1184** |
| 334 | 1399 | 61 px | 1367–1430 | **1398** |
| 335 | 1172 | **19 px** | 1146–1209 | **1177** — default REJECTED |
| 336 | 1316 | **8 px ⚠ flagged** | 1310–1373 | **1341** — default REJECTED |

★ p. 336 is the leaf where **Collatio II opens with its full-width heading + Summarium**, and
it produced the volume's narrowest run yet (8 px) — **the display-heading failure the frozen
rule predicts, now with a numeric floor**. Expect it on **every one of the 22 remaining
collatio-opening leaves**.

**Registers read so far (anchors only, per the standing rule):**

| p. | notes | anchors L / R | block L / R | relation | runover |
|---|---|---|---|---|---|
| 329 | 6 | 3 / 3 (¹ is on the `COLLATIO I.` heading) | 1 / 5 | **underruns by two** | n. 1 gutter |
| 330 | 8 | 4 / 4 | 6 / 2 | **overruns by two** | n. 6 gutter |
| 331 | ≥5 | 3 / … | 5 / … | **overruns by two** | n. 5 gutter |

★ **Three leaves, three different block/anchor relations, and a gutter runover on every
one** — this work's footers run longer than the Breviloquium's or the Itinerarium's, and
p. 329 n. 1 alone fills a whole block (it is the note on the work's title in the codices).

**Marginalia so far** — p. 329: `Divisio.` · `Pars I.` · `Ecclesia et synagoga.` · `Tria
requiruntur.` · `De observantia legis.` · `Ecclesia columna et firmamentum.` · p. 330:
`De cohaerentia pacis.` · `De consonantia laudis.` · `Inepti auditores propter
inobservantiam legis.` · `Item, propter violationem pacis.` · `Item, propter defectum laudis
divinae.` · `Notandum.` · `Epilogus I. partis.` · `Pars II.` · `Incipiendum a Christo, qui
est medium in omnibus.` · p. 331: `Alia ratio.` · `Medium septiforme scientiarum.` ·
`Applicatio ad Christum.` · `De 1. medio.` · `Duplex esse.`

**★ Register decisions taken at this chunk (to be frozen in CLAUDE.md when it closes):**
*collatio* → "collation" · ***medium* → "medium"**, never "mean" or "middle": the whole
collatio turns on Christ as *medium* in seven senses mapped to the seven sciences
(metaphysicus · physicus · mathematicus · logicus · ethicus · politicus seu iuristarum ·
theologus), and the word has to carry centre, mean and means at once, which the English
cognate does · *sermo* → "discourse"/"sermon" by context (⚠ *debet fieri sermo* is the
preaching act) · *artistae* → "the artists" (the arts-faculty masters — ⚠ **p. 330 n. 7 is
the crux**: the codices do not write *Aristotelis* plainly, and the Vatican edition
substitutes *per falsas opiniones et per argumenta Aristotelis* for *per falsas positiones
per artistas*; transcribe the Quaracchi text and record the variant).

**⬜ WHERE TO RESUME: p. 331's RIGHT column.** Latin transcribed through ¶ 12's opening
(*…Esse ex se est in ratione originantis; esse secundum* —), i.e. the foot of p. 331's left
column. Still to do: pp. 331 R – 336, then the English throughout, then the apparatus
(~65 entries), then `## Notes`. ⚠ **The chunk file `vol5/bon-hex-c1.md` is ON DISK AND
UNTRACKED** — deliberately, per the Péguy pattern: it is being built by incremental appends
so a crash costs a paragraph, and an incomplete chunk is never committed.

## ⚠ Hazards to carry into the grind

- **The `SUMMARIUM` header garbles as badly as `SCHOLION` did.** A case-tolerant grep over
  the whole work returns only 12 recognizable spellings (`SuMMARiuM`, `SuMMARKJM`,
  `SuMMARiUiM`, `SuMMARiiiM` …) against 23 collationes. **Find them by CONTENT — the
  em-dash-and-paragraph-number synopsis shape — never by header grep**, exactly as the
  Vol IV scholia rule requires.
- **Marginalia are dense here too** (five on p. 329's first column alone) and must be
  trimmed to the Marginalia list.
- **The plates for this work do not exist** beyond pp. 326–331 extracted for this scouting,
  and those will be reclaimed at the next gate. Re-extract per collatio, not in bulk:
  ~128 leaves at 450 dpi is ~600 MB.
- p. 329's left footer block ends on the printed signature line **`S. Bonav. — Tom. V.`** —
  printer's furniture, not apparatus, as at p. 321 of `de-reductione`.
