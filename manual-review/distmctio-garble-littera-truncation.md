# Systematic defect: `DISTmCTIO` ligature garble → truncated littera chunks (Vol IV)

**Found 2026-07-18** during the d.45 build. **STATUS: CLOSED 2026-07-18 — d.45 fixed in `a0cc786`, and
d.28 + d.37 repaired in `b22cd1c`. All known instances of this defect class in Book IV are resolved.**
Kept as the reference for the detection recipe and for the d.48 boundary.

## The bug

The IA djvu OCR garbles `DISTINCTIO` via the IN→m ligature, exactly as already documented for
Vol II's `DISTmCTIO 11.` (CLAUDE.md, "Vol II structure notes"). A plain `grep DISTINCTIO` therefore
**misses the real distinction header** and finds only the page-top running-head bleed further down.
Chunking from the bleed silently truncates the front of that distinction's **littera** — Lombard's
Cap. I and sometimes Cap. II — and the dropped text falls into the *preceding* chunk's nominal
line range without ever being rendered by it. Net effect: **text vanishes from the corpus with no
audit flag**, because the three guard-rail audits fire on whole-chunk dropouts, not on a distinction
head-seam.

The decade polish gates did not catch this: Pass 3's boundary-integrity sweep checks seams
*between chunks*, and both of these are the seam *at the distinction header itself*.

## Detection recipe (use this, not `grep DISTINCTIO`)

```bash
grep -nEi "d[i1l]st[inml1]{1,2}[cg]t[il1]o" raw/bonaventure_vol4_raw.txt
# real header  = bare `DISTINCTIO N.` on its own line, no trailing page number
# running head = has a page number, and/or `P. I`/`ART.`/`QUAEST.` furniture
```

All 8 garbled bare headers in Vol IV raw:

| raw line | as OCR'd | distinction |
|---|---|---|
| 18492 | `DISTmCTIO VII.` | d.7 |
| 24038 | `DISTmCTIO X.` | d.10 |
| 72761 | `DISTmCTIO XXVII.` | d.27 |
| 74209 | `DISTIECTIO XXVIII.` | d.28 |
| 76939 | `DISTmCTIO XXXI.` | d.31 |
| 85728 | `DISTmCTIO XXXVII.` | d.37 |
| 99598 | `DISTmCTIO XLV.` | d.45 |
| 104392 | `DISTmCTIO XLVIII.` | d.48 |

## Status per distinction

| d. | real header | chunk `line_start` | verdict |
|---|---|---|---|
| 7 | 18492 | *(none — pre-dates line-bounds)* | body opens at the DISTINCTIO VII header — **looks OK**, but see anomaly below |
| 10 | 24038 | *(none)* | body opens at `Cap. I` — **OK** |
| 27 | 72761 | 72761 | **OK** (the archived resume pointer's L72893 was the bleed; whoever built it caught that) |
| 28 | 74209 | ~~74279~~ → **74209** | ✅ **FIXED** `b22cd1c` (+ misplaced-English-block defect) |
| 31 | 76939 | 76939 | **OK** |
| 37 | 85728 | ~~85793~~ → **85728** | ✅ **FIXED** `b22cd1c` |
| 45 | 99598 | ~~99733~~ → **99598** | ✅ **FIXED 2026-07-18** (this session) |
| 48 | 104392 | *(not yet built)* | ⚠ use **104392**, not the p.981 bleed at L104305 |

## The two defects (both now repaired — kept for the record)

### `vol4/bon-sent-IV-d28-littera.md` — printed p.687
Dropped raw **L74209–74278**: the `DISTINCTIO XXVIII.` header line, **Cap. I** and its rubric
*Si consensus de futuro etiam iuramento firmatus faciat coniugium*, and the chapter's body.
The chunk renders `### DISTINCTIO XXVIII.` and then jumps straight to Cap. II.

**Second, separate defect in the same file:** the paragraph sitting where Cap. I's Latin belongs is
**English prose inside the `## Latin` block** ("…what ought to be done or to be, not what is then
done…"). So the file is both truncated *and* has a language-block contamination. Repair must fix
both.

### `vol4/bon-sent-IV-d37-littera.md` — printed p.800
Dropped raw **L85728–85792**: the `DISTINCTIO XXXVII.` header line and all of **Cap. I**
*In quibus ordinibus nequeat contrahi matrimonium* (the Carthaginensi Concilium material on orders
impeding marriage). The chunk currently opens mid-stream on p.801 at a `**Notula.**` paragraph,
then Cap. II.

## Repair shape (as executed)

Same as the d.45 littera repair done this session: one subagent per chunk, prepend the missing
Cap. I material re-set from 450 dpi column bands, claim that printed page's
`NOTAE AD LIBR. SENTENTIARUM` footers with page-qualified `[^pNNN-M]` labels, check the preceding
chunk for double-claim, correct `line_start`/`printed_pages`/`source`/`transcription_status`, and
correct the preceding chunk's over-extended `line_end`. Budget ~2 chunks.

## Unrelated anomaly noticed in passing

`vol4/bon-sent-IV-d7-littera.md`'s apparatus intro blockquote is written in **Italian**
("Le note numerate qui sotto corrispondono ai richiami nel testo latino…") before repeating itself
in English. Cosmetic, reader-visible, one-line fix. Not part of this defect class.
