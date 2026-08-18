# `bon-hex-c13` — plate scouting (2026-08-18)

Banked before writing. Everything below is read off the 450 dpi bands unless marked otherwise.

## Span — both ends fixed positively

- Raw **L66161 → L66936** (~776 lines). Printed **pp. 387–392**, PDF 463–468.
- Collatio XIII **opens part-way down p. 387** (heading, subtitle and Summarium full measure;
  ¶ 1 resumes in two columns near the foot) and **closes part-way down p. 392** at
  *…ad quae reducuntur omnia, quae in Scriptura continentur.*
- Far end fixed from the real **`COLLATIO XIV.`** header on p. 392's band (raw L66937).
  ⚠ p. 387's running head already read `COLLATIO XIII.` while Collatio XII still filled the upper
  third; p. 391's read `COLLATIO XIII.` correctly. The head was not used either way.
- **Heading carries NO apparatus anchor.** Thirteenth opening read; only `COLLATIO I.` has one.
- **Subtitle, confirmed on the band:** *De tertia visione, quae est intelligentiae per Scripturam
  eruditae, tractatio prima, in qua agitur de Scripturae intelligentiis spiritualibus.*
  (c12's resume note carried this provisionally from a ⅓-scale read; it is now verified.)

## Paragraph count

**33 numbered ¶¶, 1..33, no gaps, identical in both languages**, and the Summarium's last reference
is **`30-33`**. Exact agreement — the fifth chunk running. ★ **Unlike c11, the closing epilogue is
NOT a separate unnumbered paragraph:** the marginal gloss `Epilogus` sits on the last sentence of
**¶ 33** itself (*Hae sunt quatuor facies animalium et duodecim lumina…*). Rendered inside ¶ 33, as
printed. **The epilogue's form is decided per collatio, never carried forward.**

## Gutters — every one confirmed against the direct per-column ink profile

| page | region | band | centre rule | value |
|---|---|---|---|---|
| 387 | Collatio XIII's ¶ 1 band, rows .700–.743 | 1131–1192 (62 px) | 1160–1164, peak 1162 | **1161** |
| 388 | body | 1352–1416 (65 px) | centred | **1384** |
| 389 | body | 1163–1226 (64 px) | 1192–1196, heavily inked | **1194** |
| 390 | body | **SKEWED — see below** | — | **crop L at 1362, R at 1350** |
| 391 | body | 1143–1213, drifting ~8 px | 1177–1183 | **1177** |
| 392 | Collatio XIII's body, rows .08–.40 | 1325–1391 (67 px) | centred | **1358** |

### ★★★ p. 390 IS MONOTONIC SCAN SKEW, AND A NARROW AGGREGATE BAND IS ITS SIGNATURE

`gutter-profile.py` returned **1378 on a 19 px band** — far under the 60 px floor. The frozen rule
says a narrow run "usually means the printed centre rule inked heavily on that leaf." **Here it
means the gutter MOVED.** Profiled in eight row slices down the leaf, the band walks steadily right:

| rows | .08–.17 | .17–.25 | .25–.34 | .34–.42 | .42–.51 | .51–.59 | .59–.67 | .68–.76 |
|---|---|---|---|---|---|---|---|---|
| band | 1304–1362 | 1309–1371 | 1317–1377 | 1322–1382 | 1332–1389 | 1338–1397 | 1345–1404 | 1350–1410 |
| mid | 1333 | 1340 | 1347 | 1352 | 1360 | 1367 | 1374 | 1380 |

**A 47 px walk** — far larger than p. 323's attested 27 px. Each slice still shows the rule splitting
the band into two sub-runs, so the leaf is normal in every way except that it was scanned askew.

**Why the aggregate band goes NARROW rather than wide:** the whole-body profile reports the
*intersection* of the shifting bands, not their union. **So a sub-60 px band has two distinct
causes now — a heavily inked rule, and skew — and they are told apart by profiling in slices,
which costs nothing.** The default 1378 is the value at the FOOT of the leaf; using it would have
pulled right-column text into the left crop at the head of the page.

**The remedy, and it needs no new tool:** crop twice. The left column's right edge never exceeds
**1350**; the right column's left edge never falls below **1362**. So `colcrop … 1362` gives a left
crop that holds all left-column text and no right-column text, and `colcrop … 1350` gives the
mirror for the right. Both were read and both are clean at every height.

## Register — 40 entries owned

| page | notes | block split | anchor split | relation |
|---|---|---|---|---|
| 387 | **NONE — all four are Collatio XII's** | — | XIII's ¶ 1 carries **no anchor at all** | inherited nothing |
| 388 | nn. 1–9 | 1–3 L, 4–9 R | 1–4 L, 5–9 R | left block **underruns by one** |
| 389 | nn. 1–8 | 1–4 L, runover + 5–8 R | 1–5 L, 6–8 R | left block **underruns by one** |
| 390 | nn. 1–7 | 1–4 L, 5–7 R | 1–4 L, 5–7 R | they **coincide** |
| 391 | nn. 1–9 | 1–5 L, runover + 6–9 R | 1–3 L, 4–9 R | left block **OVERRUNS by two** |
| 392 | nn. 1–7 | 1–2 L, 3–7 R | 1–4 L, 5–7 R | left block **underruns by two** |

**★★ THE DIRECTION REVERSED TWICE INSIDE ONE CHUNK** — underrun, underrun, coincide, **overrun**,
underrun. The frozen warning against inferring the next leaf from the run is exactly right, and
p. 391 is the leaf that would have been got wrong.

## ⚠ Nothing is inherited, and that is a verified statement

p. 387's whole footer register belongs to Collatio XII, because **Collatio XIII's ¶ 1 — the entire
Genesis lemma *Congregentur aquae, quae sub caelo sunt…* — carries no apparatus anchor.** Confirmed
at full magnification on the band, not at ⅓ scale. c12's `KNOWN_TOTALS` entry `387: 4` stands.

## ⚠ Nothing is forwarded either — and for the same structural reason, one leaf on

On p. 392 **Collatio XIV contributes only its heading, subtitle and Summarium** — its body has not
begun, so it carries no anchor and claims none of p. 392's register. All seven notes are
Collatio XIII's. This is the second of the three boundary shapes recorded at c1–c4 (the mid-leaf
where the next collatio claims none of the register; attested at pp. 342 and 348). **`bon-hex-c14`
inherits nothing, and its body opens on p. 393.**

## Runovers — two gutter-crossing

- **p. 389 n. 4** (Gregory on Ezekiel): *…in* | *Lege et Prophetis, novum vero in Evangeliis…*
- **p. 391 n. 5** (Albert on the light of the stars): *…in II. de Caelo et mundo,* | *tr. 3. c. 6.…*

Both right-hand blocks therefore open **unnumbered**. With c12's two, that is **eight of the last
ten leaves in this work**.

## ⚠ Recording the negatives — all five interior page-foot joints checked at the band

| joint | left block opens | body reads across |
|---|---|---|
| 387/388 | numbered ¹ | *…et lignum pomife-* → *rum, faciens fructum iuxta genus suum* ✓ mid-word |
| 388/389 | numbered ¹ | *…Repleta est terra* → *scientia Domini, sicut aquae maris operientes* ✓ |
| 389/390 | numbered ¹ | *…potissime tamen quan-* → *tum ad animam* ✓ mid-word |
| 390/391 | numbered ¹ | *…Quando* → *ergo Scriptura loquitur de istis* ✓ |
| 391/392 | numbered ¹ | ¶ 26 closes *…et foenum aruit.* → ¶ 27 opens ✓ paragraph boundary |

None is a page-crossing runover.

## Digits settled at the band, against the raw

| where | raw | plate | how settled |
|---|---|---|---|
| p. 388 body | *terra est **intimum** elementorum* | **infimum** | sense: earth is the *lowest* element against Scripture the most sublime |
| p. 388 n. 7 | `Matth. 11, 29` | **Matth. 14, 29** | 1/4 class; Peter walking on the sea is Mt 14:29 |
| p. 388 n. 8 | `Eccle. 7, 2.!)` | **Eccle. 7, 25** | *alta profunditas, quis inveniet eam* is Eccl 7:25 |
| p. 389 n. 4 | garbled | **Gregor., I. Homil. in Ezech. homil. 6. n. 12** | read whole off the band |
| p. 390 n. 3 | `pag. 3.56` | **pag. 356** | 3/5 class |
| p. 392 n. 1 | — | **Psalm. 18, 6** | *In sole posuit tabernaculum suum* is Ps 18:6 |

★ p. 392 n. 7 prints **`Math. 24, 29.`**, with the single `t` — transcribed as printed, not
normalised to *Matth.*, on the same discipline as the Itinerarium colophon.

## Marginalia (body order, for the Notes list)

p. 387 — Introductio.
p. 388 L — Haec visio tertiae diei. · Divisio primaria in tria membra. · Cap. I. De intelligentiis
spiritualibus in genere. · Comparantur congregationi aquarum. · Ob 3 rationes. · Prima.
p. 388 R — Secunda. · Tertia.
p. 389 L — Magis manifestabitur Scriptura. · Revelatio in Scriptura crescit.
p. 389 R — Scriptura debet esse multiformis. · Cap. II. De 4 sensibus in specie. · Triplex Dei
manifestatio.
p. 390 L — Liber creaturarum quasi emortuus. · Reparatur per Scripturam. · Confirmatur. · Figurae in
Ezechiele et Apocalypsi. · Explicantur.
p. 390 R — Sensus litteralis et 4 partes eiusdem. · Litteralis agit primo de aeternis. · Secundo, de
temporalibus tripliciter. · Facies eius quatuor. · Triplex sensus spiritualis. · In sensu anagogico
quatuor facies.
p. 391 L — Item, in allegorico. · Item, in tropologico. · Exemplum horum in sole. · Facies 4 sec.
anagogiam. · De prima anagogia. · Exemplum.
p. 391 R — De secunda. · De tertia. · De quarta. · Allegoria prima.
p. 392 L — Secunda. · Tertia. · Quarta. · Tropologia prima.
p. 392 R — Secunda. · Tertia. · Quarta. · Epilogus.
