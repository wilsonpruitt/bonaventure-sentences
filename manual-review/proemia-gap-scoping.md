# The Sentences Proemia are missing from all four books — scoping (2026-08-19)

Raised by Wilson. Confirmed: **every one of Books I–IV begins its chunk set at Distinction I.**
Nothing before d. 1 has ever been chunked, translated, or given a slot in the site's data model.

This is not an apparatus defect or a quality problem. It is **missing text** — including the two
most-quoted passages in the entire commentary (Book I's four-rivers prologue, Book II's
*pauper et tenuis compilator*). Book III has been LIVE for months without its proemium.

**It does NOT block the Hexaemeron front.** `bon-hex-c20` and the work-close gate are untouched by
any of this. Do not fork the front to do it.

---

## The evidence

First chunk in each volume, with the gap it leaves in front of it:

| Vol | First chunk on disk | Printed | PDF | Offset | **Gap in front** |
|----:|---|---:|---:|---:|---|
| I   | `bon-sent-I-d1-divisio`     | 29 | 131 | +102 | **pp. 1–28** |
| II  | `bon-sent-II-d1-littera`    | 11 |  33 |  +22 | **pp. 1–10** |
| III | `bon-sent-III-d1-divisio`   |  7 |  29 |  +22 | **pp. 1–6**  |
| IV  | `bon-sent-IV-d1-p1-divisio` | 10 |  30 |  +20 | **pp. 1–9**  |

⚠ **The printed page ranges are DERIVED from those offsets, not read off a plate.** Every start
line below *was* read on the raw text and is quoted. Verify the page numbers on the plate before
setting `printed_pages` in any chunk — `tools/extract-pages.py --volume vol2 --pages 1-10 --dpi 450`
and so on.

`site/src/data/content.json` confirms the gap downstream: Books I–IV carry **48 / 44 / 40 / 50
distinctions and no pre-distinction node of any kind.** There is nowhere for a proemium to render
even if one were translated tomorrow. The site schema is `{id, title, distinctions[]}`.

---

## What is actually sitting in the raw text

### Book I — raw `bonaventure_vol1_raw.txt` L8900–12784, ~22,900 OCR words

Display heading `IN LIBRUM PRIMUM SE^^TENTIARUM.` at **L8900**, then the lemma (OCR-damaged, as
display lines usually are): `Profunda flmiorani s… dita produxit in lucem` = *Profundum fluviorum
scrutatus est, et abscondita produxit in lucem*, Job 28:11. Running heads in print order:

| Region | Raw lines | What it is |
|---|---:|---|
| Proemium | 8900–~9820 | The four causes of the *Liber Sententiarum*; the four rivers of Paradise (Phison/Gehon/Tigris/Euphrates) mapped onto the four books |
| `PROOEMII QUAEST. I`–`QUAESTIO IV` | ~9823–11100 | The four *quaestiones prooemiales* — theology as a science — each with `CONCLUSIO` and `SCHOLION` |
| `IN LIBROS SENTENTIARUM` | 11104–11284 | Lombard's own Prologue (littera) |
| `CAPITULA PRIMI LIBRI` | 11285–12196 | Lombard's chapter list |
| `COMMENTARIUS IN PROLOGUM` | 12197–12780 | Bonaventure on Lombard's Prologue: `DIVISIO TEXTUS`, `DUB. I`–`DUB. III`, `NOTAE`, divisio of the second part, `DUBIA CIRCA LITTERAM SECUNDAE PARTIS`, `DIVISIO TEXTUS ULTIMAE PARTIS`, `DUBIUM ULTIMAE PARTIS` |
| `DE DEI UNITATE ET TRINITATE` / `DISTINCTIO I.` | 12782/12785 | — where the corpus currently begins |

### ⛔ And Book I's is HIDDEN, which is why it never surfaced

All of the above lives inside **`vol1/bon-sent-I-proleg.md`** — 7,803 lines, `word_count_latin:
77473`, `line_start: 1`, `line_end: 12784`, titled **"Prolegomena to Book I of the Sentences."**

It is a **bare OCR dump**. Its only headings are `# I Sent., Prolegomena` and `### Latin`. There is
**no `### English` section at all**, no apparatus, no `printed_pages`, no `transcription_status`.

**The title is the whole problem.** It reads as editors' front matter, so ~22,900 words of
Bonaventure got filed behind a label that says "not his text." `translations/checklist.md:14`
carries it as one unchecked box — `- [ ] bon-sent-I-proleg` — so the miss shows up in the corpus as
a single deferred item rather than as thirty absent chunks. Nothing in `PLAN.md`, `progress.md`,
`CLAUDE.md`, `next-session-resume.md`, or `OPERA-OMNIA-TRACKER.md` mentions a proemium anywhere.

⚠ **The file genuinely does contain real prolegomena too** — the editors' apparatus, the codex
tables (`TABULA COLLATORUM CODICUM ET EDITIONUM`), the roman-paginated front matter. Those are
correctly out of scope. Only L8900–12784 is Bonaventure and Lombard.

### Books II–IV — no file of any kind

| Vol | Raw start | Heading as printed | Lemma | ~OCR words |
|----:|---:|---|---|---:|
| II  | L704  | `PRAELOCUTIO / SANCTI BONAVENTURAE / PROOEMIO IN SECUNDUM LIBRUM SENTENTIARUM PRAEMISSA` | *Salvatoris opitulante gratia…* | 7,673 |
| III | L702  | `PROOEMIUM. / IN TERTIUM LIBRUM SENTENTIARUM.` | *Deus autem, qui dives est in misericordia* (Eph 2:4) | 3,413 |
| IV  | L862  | `PROOEMIUM / IN QUARTUM LIBRUM SENTENTIARUM.` | *Unguentarius faciet pigmenta suavitatis* (Ecclus 38:7) | 4,591 |

**Book II's is the *Praelocutio*** — the passage where Bonaventure disclaims originality: *Nec
quisquam aestimet, quod novi scripti velim esse fabricator; hoc enim sentio et fateor, quod sum
pauper et tenuis compilator* (L710–715). It is the single most-cited sentence about his own method
and it is not in the corpus.

⚠ **Word counts are raw-OCR and inflated** — they include the apparatus and, in Vols II–IV, column
bleed. Vols II–IV raw are column-interleaved in this region (Vol IV's right column is truncated
mid-word at L946ff), so **these are Tier 2 plate jobs regardless of the word count.** Do not
estimate from the Latin body alone.

---

## The four jobs, in order

### J1 — Books II, III, IV proemia. **Do these first.** ◐ Book III done 2026-08-19.

> **✅ `bon-sent-III-proem` is Tier 2** (commit `9a95a17`) — pp. 1–2, 18 apparatus entries, no
> `[?]` flags. **⚠ Scope correction: Book III's gap is three units, not one.** Past the proemium,
> printed p. 3 is Lombard's `LIBER TERTIUS SENTENTIARUM` opening (a `littera`, raw L832) and
> pp. 4–6 are `CAPITULA TERTII LIBRI`, his chapter list for all 40 distinctions (raw L887–1058).
> Same shape as Book I's gap, in miniature. **Expect the same for Books II and IV — check the raw
> between the proemium's end and `DISTINCTIO I.` before calling either one done.**
> ⛔ **The three guard-rail audits cannot see a proemium chunk**: they select by the filename regex
> `bon-sent-III-d(\d+)-`, so a chunk with no `-dN-` segment never matches at any `--min-d`, and
> all three print a clean verdict on **0 chunks audited**. Either extend the regexes or verify
> front-matter chunks by marker-pairing + plate discipline and say so.

Three chunks, one per volume: `bon-sent-{II,III,IV}-proem`. Self-contained, each is one continuous
argument with its own apparatus register, each roughly the size of a long `divisio`. Standard Tier 2
per-chunk recipe, no new conventions needed. Book III first — it is live and reader-visible.

**Cost:** ~1 session each. **Book IV needs the plate**, its raw is unusable in this region.

### J2 — The site schema needs a pre-distinction slot. ✅ **DONE 2026-08-19** (commit `b1c7758`).

> Front-matter types (`proemium` / `capitula` / `littera`) are exempted from the `distinctio === 0`
> skip; division 0 of a Sentences book titles itself **"Proemium"**; `typeOrder` ranks proemium
> before littera; and a shared `divisionHeading()` replaced the `divisionLabel ? dist.title : …`
> form on both the book page and the detail page — that form discarded `dist.title` for a Sentences
> book and fell through to `romanize(0)`, which returns the string `"0"`, so the Proemium rendered
> as **"Distinction 0"**. Build 2042 → 2043. `bon-sent-I-proleg` still excluded (verified).
>
> **★ The corpus was already citing the text that was not there.** `build-citations.py` QA flags
> fell **228 → 226**: `bon-sent-III-d1-divisio` cites `pag. 2` and `bon-sent-III-d25-a1-q1` cites
> `pag. 1` (plus a `loc. cit.` inheriting from it) — three references into printed pp. 1–2 of
> Vol III that had nowhere to land and now resolve. Quaracchi cite the proemium; the corpus had
> dangling pointers into a text nobody had built. Same lesson as the standing *empty grep ≠
> absence* rule, running in the opposite direction.

**Superseded, kept for the record:**

`content.json` works are `{id, title, distinctions[]}`. A proemium is not a distinction and should
not be faked as `d. 0` — that will sort wrong, break the citation builder's `d.` parsing, and read
wrong to any user who knows the text. Add a sibling `proemium` key on the work node and a render
branch ahead of the distinction list. Touch `build-content.mjs` and `build-citations.py` together.

**Do J2 before J1's gate**, or three finished translations sit undeployable.

### J3 — Extract Book I's proemium out of `bon-sent-I-proleg.md`. **The judgement-dense one.**
L8900–12784 becomes its own chunk family, and the region divides on the running heads above:

- `bon-sent-I-proem` — the four causes / four rivers
- `bon-sent-I-proem-q1` … `-q4` — with their `CONCLUSIO` and `SCHOLION`
- `bon-sent-I-proem-littera` — Lombard's Prologue
- `bon-sent-I-proem-capitula` — Lombard's chapter list (⚠ may not warrant translation; Wilson's call)
- `bon-sent-I-prol-divisio`, `-dubia`, `-notae` — the `COMMENTARIUS IN PROLOGUM` family

That is **~8–11 chunks**, and the four *quaestiones* carry scholia and variants, which puts them at
DEEP-tier weight — compare `bon-sent-I-d3-p1-a1-q1` (12.4) in `AUDIT-QUEUE.md`. **Budget 8–12
sessions, not one.** The chunk boundaries above are read off running heads in the OCR and must be
confirmed on the plate before any of them is cut.

⚠ **Decide before starting: does `bon-sent-I-proleg.md` get edited, or left alone?** It may be
serving as a raw OCR reference elsewhere — it is referenced by `chunk_vol1.py`,
`manual-review/citation-qa-report.md`, and `translations/checklist.md`. Safest is to leave the file
untouched, cut the new chunks from `raw/bonaventure_vol1_raw.txt` directly, and **retitle** the
proleg file to "Editors' Prolegomena + unextracted front matter (Vol I)" so it never swallows a
second thing. Retitling alone would have prevented this.

### J4 — Sweep the other volumes for the same defect class. **Cheap, do it at the J1 gate.**
The mechanism here is *a real work filed behind a front-matter label*. Vol V's opuscula each have
their own prologue and at least one (`bon-brev-prol-s4`, `-s5`) IS chunked — so the pattern was
caught there and missed here. Confirm nothing else opens at "chapter 1" with a prologue in front of
it. `grep -niE 'prooemi|praelocutio|prologus' raw/*.txt` against the first-chunk line of each work.

---

## Also found, not fixed

**`OPERA-OMNIA-TRACKER.md` is badly stale** (last updated 2026-04-14). It reports Vols II, III, IV
as raw text `❌ empty file` with `0` chunks done. All three are chunked — 464 / 412 / 646 files —
and Vol III is live. Every session estimate downstream of that table is wrong. Separate job; flagged
here so the next reader doesn't trust it.
