# Tier-2 ambiguities — bon-sent-I-d24-a1-q2

Source: `raw/bonaventure_vol1_pt2_raw.txt` lines 687–820. Printed pp. 423–424 (vol1pt2 PDF pp. 13–14; offset = printed − 410, verified by direct PDF inspection of running heads at 400 dpi).

No `[?]` flags raised in the chunk body. The OCR for this question was severely garbled by the heavy two-column layout (the OCR reflowed the two body columns A-then-B inconsistently), so the body Latin was reconstructed by reading the high-res PDF crops (300–400 dpi extracts) directly and cross-checking against `raw/bonaventure_vol1_pt2_raw.txt` 687–820 line by line. All silent corrections below resolved unambiguously by that cross-check.

## Silent OCR corrections (logged for transparency)

- `pns` (OCR for `ens` in argument 1) → `ens` — confirmed by PDF.
- `imus`, `mius`, `unns` → `unus` (multiple occurrences; standard Quaracchi OCR collapse of `un` ligatures).
- `Pliilosophus` → `Philosophus`.
- `pi'oprietas` → `proprietas`.
- `soh =` (corrupted "soli ⁵" with footnote marker) → `soli` + footnote anchor `[^5]`.
- `notimaliter` → `notionaliter`.
- `Si substan- '-, habeo propositum` (OCR garbled the line break and inserted spurious glyphs) → `Si substantialiter, habeo propositum` — cross-checked against PDF.
- `essentialif` → `essentialis` (CONCLUSIO box first line).
- `tum perso- nalis` line break joined → `tum personalis`.
- `attribuit-mn&attribuitur` (OCR doubled the word at column wrap) → `tunc unitas attribuitur` — verified against PDF.
- `unitati personali unitati` OCR repetition collapsed to `attribuitur personali unitati` (CONCLUSIO box).
- `essentialis` vs `essentiali` in CONCLUSIO box: PDF reads `unum autem essentiali` (dative), retained.
- `Cum` (Respondeo opener, OCR `cum`) capitalised.
- `essenliam`, `essentiis` retained as `essentiam`, `essentiis`.
- `signiflcatio`, `signifi-cationem` → `significatio`, `significationem`.
- `diviiiis` → `divinis`.
- `iila` → `illa`.
- `imitas` → `unitas` (multiple occurrences in the Respondeo).
- `additm` → `additur`.
- `concretum` retained.
- `uihilominus` → `nihilominus`.
- `diversitatera` → `diversitatem`.
- `varietur`, `variari` retained as in OCR (matches PDF).
- `figurae dictionis ex commutatione` — OCR garbled `commutatione` with `^`; resolved against PDF.
- `pi'oprietas` → `proprietas` (Ad 4).
- `noraen` → `nomen`.
- `personaest*` → `persona est` + footnote anchor `[^15]` (PDF shows the asterisk-as-footnote-marker pattern).
- `\` and `'` glyphs scattered through the OCR resolved as footnote anchors per their PDF positions.
- `coDciuiio`, `concinsio`, `cODcinsio`, `concinsio-2`, `coDcinsio 3`, `concinsio 1` — these are marginal "Conclusio 1/2/3" labels printed in the Quaracchi margin, not part of the body. Stripped (the conclusio is rendered once as a blockquote at the top per CLAUDE.md template).
- `soii.ui ''°" °"` and similar floating glyphs → marginal labels (`Soluti opp.` etc.), stripped from body.
- `obiicitur'` → `obiicitur` + `[^14]`.
- `fallacia figurae dictionis ex commutatione ^ istius termini tinus.` — `tinus` was OCR for `unus` continued from prior line; the body word `unus` (italic) appears in PDF.
- `seAper-sonalem` (OCR collapsed `sed personalem`) → `sed personalem`.
- `subaudi` retained in apparatus fn 13.
- Apparatus footer `Athanasiano.` (fn 4) is the entire entry — extremely brief gloss that the [Symbolo] referenced in the body is the Athanasian Creed.

## Footer-marker → numbered-apparatus mapping (p.423, fns 1–7; p.424, fns 8–15)

p.423 has 7 footnotes plainly numbered in the printed page. The body markers in OCR were degraded (` ' ^ ` etc.); positions verified against PDF:

- `Philosophus '` → fn 1 (Aristotle IV *Metaph.* + Boethius).
- `substantialiter -` → fn 2 (Magister Lombard cross-ref).
- `in neutro^` → fn 3 (`Vat. cum uno alterove cod. adiicit genere`).
- `in Symbolo ^` → fn 4 (`Athanasiano`).
- `« quod convenit uni soh = »` → fn 5 (Porphyry *de Praedicabilibus* + variant `quia` pro `quod`).
- `distinctione vigesima secunda'` → fn 6 (`In lit. Magistri, c. 4, et dub. 2`).
- `quod est unus '` → fn 7 (`Sequimur communiorem mss. et ed. 1 lectionem, addendo quod est`).

p.424 has 9 footnotes, but fn 9 (`In Vat. et cod. cc hic desideratur de secundo articulo, scilicet`) belongs to ARTICULUS II's opening sentence (outside our chunk). The 8 in-chunk fns map as follows:

- `ponamus et '` → fn 8 (Vat. omits *et*).
- `tunc^ necesse est` → fn 9 (`Ita maior pars mss., dum ceteri… ponunt enim`).
- `sub indistinctione, in neutro genere` → fn 10 (the long variant note on *tunc/genere/se ipso/sine distinctione*).
- `Et ideo patet \` → fn 11 (`In ed. 1 additur primum`).
- `ex commutatione ^` → fn 12 (`Vat. … mutatione… diversificari pro variari`).
- `sed unitas''` → fn 13 (`Supple etiam… speciale`).
- `Ad illud quod obiicitur'` (Ad 3) → fn 14 (`In cod. Y additur quod unus. — De notione personali`).
- `«persona est* una»` → fn 15 (`Ex plurimis mss. et ed. 1 adiecimus est`).

## Translation choices

- *Suppositum certum* → "determinate supposit" (per CLAUDE.md key-terminology table: *suppositum* → "supposit"; *certum* here = "determined / fixed").
- *Concretum / abstractum* (Respondeo) → "concrete / abstract" — Bonaventure is using the grammar-philosophy distinction (concrete *unus* vs. abstract *unitas*); rendered in scare-italic to flag.
- The CONCLUSIO box translation preserves the masculine/feminine/neuter gender distinction crucial to the question: bracketed glosses on `unitas [unity, fem.]` and `unum [one, neut.]` to make the gender point legible in English.
- *Nomen partitivum et habens in se articulum* (final paragraph) → "a partitive name and has the article in itself" — the speakers are alluding to the Greek/vernacular article that "the one" implicitly carries; rendered literally per project policy on technical scholastic vocabulary.
- *Sub ratione propria* / *communiter* in Ad 4 → "under [its] proper account / commonly" — preserves the proprie/communiter pair.

## Notes for future verification

- The Scholion is unusually brief here (a single bibliographical paragraph, no Roman-numeral subdivisions), unlike sibling q.1 which has three. Has-scholion frontmatter is `true` accordingly.
- The vol1pt2 printed-to-PDF offset is **−410** (printed page N = PDF page N − 410), verified by direct PDF inspection of the running head "DIST. XXIV. ART. I. QUAEST. II. — 423" on PDF page 13. Sibling chunk d24-a1-q1 has incorrect `pdf_pages: [522, 523, 524]` in its frontmatter (those values exceed the pt2 PDF's 468-page count and reflect the +102 pt1 offset wrongly applied). Correct sibling values would be `pdf_pages: [10, 11, 12]` for printed 420–422. A separate cleanup pass should fix that.
