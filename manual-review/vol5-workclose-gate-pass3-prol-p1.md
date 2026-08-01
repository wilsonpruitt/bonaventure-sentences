# Vol V work-close gate — PASS 3 (cross-chunk boundary integrity), Prologue + Pars I

**Scope:** `bon-brev-prol`, `bon-brev-prol-s1`…`-s6`, `bon-brev-p1-c1`…`-c9` — 16 chunks,
printed pp. 201–218 (pdf 277–294; offset `pdf = printed + 76`). Plus the outgoing seam
`p1-c9 → p2-c1` (receiving side belongs to the Pars II agent).

Run 2026-08-01, as pass 3 of the Breviloquium work-close gate (CLAUDE.md § "Polish-gate
cadence for Vols V–X", trigger 2 — work boundary, unconditional). Pass 1 and pass 2 ran
separately. **Nothing was edited; no `KNOWN_TOTALS` entry changed.**

Derived counts (not carried): **16 chunks, 130 apparatus entries** in scope
(`re` walk of the 16 `## Apparatus` sections). Corpus-wide, `check-vol5-apparatus.py`
reports **79 chunks, 681 apparatus entries — All checks passed**; `check-vol5-census.py`
reports **79 on disk / 79 in ledger, rosters agree**.

---

## Method actually used

1. **Gutters re-measured fresh, every page, no constant** — `colcrop.py`'s own
   `measure_gutter` profile, read over three independent row windows
   (45–92 %, 30–70 %, 50–80 %) and with the two zero-ink runs on either side of
   Quaracchi's printed centre rule **merged into one band** before taking the midpoint.
   This is the CLAUDE.md rule 5 case (the in-gutter obstruction is the column rule) and
   it is present on essentially every leaf in this range.
2. **Body continuity established POSITIVELY from the next heading**, never from white
   space (CLAUDE.md's `p2-c4` rule). For each boundary the raw djvu was walked to the
   receiving unit's heading (`§ N.` / `Cap. N.`) and the ~12 lines immediately preceding
   it compared word-for-word against the prior chunk's tail. Every unit heading in the
   range is present and in order in the raw (`§ 1`…`§ 6`, `Cap. I`…`Cap. IX`,
   `PARS SECUNDA`), so no heading was inferred.
3. **Footers read off the 450 dpi bands, page by page** (bands-only rule). For every one
   of the eighteen printed pages the *last* footer entry of the right block was read at
   `n=6, scale 2.6` and its number compared against `KNOWN_TOTALS`; left/right block
   structure and split points were read where the ownership split was not otherwise
   obvious. The raw was used for body prose only.

### Gutters measured (all runs 51–64 px; cross-window spread ≤ 6 px on every page)

| p. | split_x | | p. | split_x | | p. | split_x |
|---|---|---|---|---|---|---|---|
| 201 | 1133 | | 207 | 1164 | | 213 | 1123 |
| 202 | 1376 | | 208 | 1372 | | 214 | 1394 |
| 203 | 1190 | | 209 | 1156 | | 215 | 1155 |
| 204 | 1374 | | 210 | 1355 | | 216 | 1381 |
| 205 | 1172 | | 211 | 1170 | | 217 | 1181 |
| 206 | 1379 | | 212 | 1336 | | 218 | 1379 |

Three of `colcrop.py`'s bare defaults would have been adopted on a weak run and are
**rejected here**: p.208 (default 1326 on a 328 px run — a failure of the loud kind),
p.215 (default 1171 on a **22 px** run, true 1155), p.206 (default 1372 on a 48 px run,
true 1379). p.201 opens the work and p.202/204/206 carry mid-column `Cap./§` headings;
in each the merged-band midpoint over three windows agreed to ≤ 3 px. Parity is *not*
used as a predictor anywhere here — it is only noted after the fact that the odd/even
clusters happen to hold across pp. 201–218.

---

## Boundary table

Every boundary in this scope falls **inside a printed page** except two, marked as leaf
crossings. "Shakedown" = whether the 2026-07-28 Pars I shakedown gate
(`breviloquium-pars1-polish-resolution-log.md`) claimed it settled.

| # | Prior → Receiving | Shared page / crossing | Body continuity — evidence | Footer split (page total) | Shakedown said | Verdict |
|---|---|---|---|---|---|---|
| 1 | `prol` → `prol-s1` | p. 202 (mid-page, left col) | prol tail `…in multitudine[^p202-8] mysticorum sensuum et intelligentiarum.` sits immediately above the `§ 1. De latitudine sacrae Scripturae.` heading; s1 opens `Si igitur velimus latitudinem…` — contiguous, nothing between | 8 / 2 (10) | clean (tool-only) | **CLEAN** |
| 2 | `prol-s1` → `prol-s2` | p. 203 (mid-page) | s1 tail `…sacram Scripturam consummando veritatis notitiam dilatarent.` directly precedes `§ 2. De longitudine…` | 6 / 2 (8) | clean (tool-only) | **CLEAN** |
| 3 | `prol-s2` → `prol-s3` | p. 204 (mid-page) | s2 tail `…cuius longitudo commetitur se decursui regiminis universi.` directly precedes `§ 3. De sublimitate…` | 7 / 2 (9) | clean (tool-only) | **CLEAN** |
| 4 | `prol-s3` → `prol-s4` | p. 205 (mid-page) | s3 tail `…assuefacit ad divinorum spectaculorum contuitus et anagogias.` directly precedes `§ 4. De profunditate…` | 4 / 4 (8) | clean (tool-only) | **CLEAN** |
| 5 | `prol-s4` → `prol-s5` | p. 206 (mid-page) | s4 tail `…perveniamus tandem ad bravium felicitatis aeternae.` directly precedes `§ 5. De modo procedendi…` | 7 / 4 (11) | clean (tool-only) | **CLEAN** |
| 6 | `prol-s5` → `prol-s6` | p. 207 (mid-page) | s5 tail `…hic magnus vocabitur in regno caelorum.` directly precedes `§ 6. De modo exponendi…` | 3 / 5 (8) | clean (tool-only) | **CLEAN** |
| 7 | `prol-s6` → `p1-c1` | **leaf crossing** p. 208 → p. 210 (p. 209 + p. 210 top = unchunked capitula table) | s6 runs to `**EXPLICIT PROLOGUS.**`, verified complete against the raw from `Ad hoc autem, quod per sacrarum Scripturarum silvam…` through `…septuaginta duobus capitulis distinguuntur.`; the table then runs pp. 209–210 top; `PARS PRIMA / De Trinitate Dei / Cap. I.` follows | p. 208 total 7, all `s6`, n. 7 (`Epist. I. Tim. 1, 17`) complete on the page — **nothing forwarded**; p. 210 register restarts at 1 | clean (tool-only) | **CLEAN** |
| 8 | `p1-c1` → `p1-c2` | p. 210 (mid-page) | c1 tail `…quod intelligimus, rationi ».` directly precedes `Cap. II. Quid tenendum est de trinitate personarum…` | 6 / 2 (8) — blocks split 3/5, so the capitulum boundary falls **inside the right footer block**, between nn. 6 and 7 (the p. 247 shape) | clean (tool-only) | **CLEAN** |
| 9 | `p1-c2` → `p1-c3` | p. 211 (mid-page) | c2 tail `…simul stare cum beatissima Trinitate.` directly precedes `Cap. III. De istius fidei intelligentia sana.` | 5 / 2 (7); n. 6 `De duabus emanationibus et tribus hypostasibus` is c3's opening anchor | clean (tool-only) | **CLEAN** |
| 10 | `p1-c3` → `p1-c4` | p. 212 (mid-page) | c3 tail `…ad fidei Trinitatis intelligentiam sanam.` directly precedes `Cap. IV. De istius fidei expressione catholica.` | 4 / 3 (7); **p. 212 n. 7 is a page-crossing runover** onto p. 213 (`De seq. regula cfr. I. Sent.` continues unnumbered) — already logged by `check-vol5-census.py` as one of the five page-crossers, **not re-logged here** | clean (tool-only) | **CLEAN** |
| 11 | `p1-c4` → `p1-c5` | p. 213 (mid-page) | c4 tail `…qualiter loquendum sit de summa trinitate divinarum personarum.` directly precedes `Cap. V. De unitate divinae naturae in multiformitate apparitionum.` | 7 / 0 (7) — Cap. V opens on p. 213 and **claims no note there**; confirmed on the band: the register's last entry is n. 7 (`Cfr. I. Sent. d. 30. q. 1. seqq.`), which is c4's `[^p213-7]` | clean (tool-only) | **CLEAN** |
| 12 | `p1-c5` → `p1-c6` | p. 214 (mid-page) | c5 tail `…ratione productionis aeternae interius importatae.` directly precedes `Cap. VI. De unitate divinae naturae in multiplicitate appropriatorum.` | 8 / 1 (9); n. 9 `Libr. II. de Trin. n. 1` is c6's | clean (tool-only) | **CLEAN** |
| 13 | `p1-c6` → `p1-c7` | p. 215 (mid-page) | c6 tail `…de his aliquid dicendum est breviter et summatim.` directly precedes `Cap. VII. De omnipotentia Dei.` | 5 / 1 (6); n. 6 (`Libr. I. Cur Deus homo, c. 20 … Superius pro male velle A malum velle`) is c7's `[^p215-6]` | clean (tool-only) | **CLEAN** |
| 14 | `p1-c7` → `p1-c8` | p. 216 (mid-page) | c7 tail `…aliquorum impossibilitas simul stet cum vera omnipotentia.` directly precedes `Cap. VIII. De Dei sapientia, praedestinatione et praescientia.` **The running head on p. 216 reads `PARS I. C. VIII` while the top of the page is still Cap. VII's body** — the asymmetric-witness case; the boundary was set from the `Cap. VIII.` heading itself, not the head | 3 / 3 (6) | clean (tool-only) | **CLEAN** |
| 15 | `p1-c8` → `p1-c9` | p. 217 (mid-page) | c8 tail `…potest esse similitudo expressiva multorum.` directly precedes `Cap. IX. De voluntate Dei et providentia.` | 6 / 1 (7); n. 7 (`August., III. de Trin. c. 4. n. 9 … De voluntate Dei cfr. I. Sent. d. 45-48`) is c9's | clean (tool-only) | **CLEAN** |
| 16 | `p1-c9` → `p2-c1` | **leaf crossing** p. 218 → p. 219 (Pars II opens) | c9 tail `…Ipsi gloria in saecula saeculorum. Amen.` is the last body on p. 218; `PARS SECUNDA / De creatura mundi / Cap. I` opens p. 219. **The `Amen.`-shaped ending is corroborated by the following display heading, not accepted on its own** | p. 218 total **7**, all c9's; n. 7 (`Rom. 11, 33-36. Cfr. I. Sent. d. 41. a. 1. q. 2.`) **ends complete on p. 218 — nothing forwarded into p. 219**. Reported to the Pars II agent from this side | clean (tool-only) | **CLEAN** |

**16 boundaries swept (14 mid-page, 2 leaf crossings). 16 CLEAN, 0 DEFECT.**

---

## Footer accounting — every page re-read off the band

| p. | plate's last numbered entry (band) | `KNOWN_TOTALS` | agree? | ownership |
|---|---|---|---|---|
| 201 | 5 (`Cfr. Aristot., I. Poster. c. 7. seqq.`) | 5 | ✅ | all `prol` |
| 202 | 10 (`Quinque libri legales sunt: Genesis…`, runs to page foot) | 10 | ✅ | `prol` 1–8 · `s1` 9–10 |
| 203 | 8 (`August., IV. de Gen. ad lit. c. 11. n. 21`) | 8 | ✅ | `s1` 1–6 · `s2` 7–8 |
| 204 | 9 (`Psalm. 138, 6`) | 9 | ✅ | `s2` 1–7 · `s3` 8–9 |
| 205 | 8 (`Ioan. 1, 3. — Col. 2, 3`) | 8 | ✅ | `s3` 1–4 · `s4` 5–8 |
| 206 | 11 (`Aristot., I. Poster. c. 7`, runs over to p. 207) | 11 | ✅ | `s4` 1–7 · `s5` 8–11 |
| 207 | 8 (`Libr. III. c. 10. n. 14. seqq.`) | 8 | ✅ | `s5` 1–3 · `s6` 4–8 |
| 208 | 7 (`Epist. I. Tim. 1, 17`) | 7 | ✅ | all `s6`; nothing forwarded |
| **209** | one unnumbered editorial note, ending `…occurrentes lectiones variantes.` + signature `27` | *(absent)* | ✅ | **unowned by design** — p. 209 is the unchunked capitula table (frozen convention). Its footer is an editorial note about that table, complete on the page, forwarding nothing into p. 210 |
| 210 | 8 (`R addit substantiae et, B H divinae`) | 8 | ✅ | `c1` 1–6 · `c2` 7–8 (blocks 3/5) |
| 211 | 7 (`Vat. hic et paulo inferius perfecti`) | 7 | ✅ | `c2` 1–5 · `c3` 6–7 |
| 212 | 7 (`Boeth., de Trin. c. 6`, runs over to p. 213) | 7 | ✅ | `c3` 1–4 · `c4` 5–7 |
| 213 | 7 (`Cfr. I. Sent. d. 30. q. 1. seqq.`) | 7 | ✅ | all `c4`; Cap. V opens here and claims none |
| 214 | 9 (`Libr. II. de Trin. n. 1`) | 9 | ✅ | `c5` 1–8 · `c6` 9 |
| 215 | 6 (`Libr. I. Cur Deus homo, c. 20`) | 6 | ✅ | `c6` 1–5 · `c7` 6 |
| 216 | 6 (`Cfr. I. Sent. d. 39. a. 2. q. 1-3`) | 6 | ✅ | `c7` 1–3 · `c8` 4–6 |
| 217 | 7 (`August., III. de Trin. c. 4. n. 9`) + signature `28` | 7 | ✅ | `c8` 1–6 · `c9` 7 |
| 218 | 7 (`Rom. 11, 33-36`) | 7 | ✅ | all `c9`; nothing forwarded |

**No page's true total differed from `KNOWN_TOTALS`. No register was dropped, none
double-claimed, and no page in scope is unowned except p. 209, which is unowned by the
frozen chunking convention and not by oversight.**

Digit reads worth recording (the `3/5` and `6/8` classes are both live on these leaves):
p. 212's right block reads `⁶ Ex Aristot., de Praedicam.` then `⁷ Boeth., de Trin. c. 6`
— the `6` prints very close to an `8` at 450 dpi and was settled by run order, not by
glyph. p. 216's `⁶` is the same sort. No transcription change follows from either; both
chunks already carry the correct labels.

---

## What the Pars I shakedown log had settled, and whether this read agrees

The shakedown log's pass 3 (2026-07-28) recorded, in full:

> `seam-screen.py --volume 5`: **14 mid-page boundaries, 0 tail-not-terminal suspects.**
> … `check-vol5-apparatus.py`: **16 chunks, 130 apparatus entries** … `All checks passed.`

**Its verdicts are confirmed, but its evidence was not sufficient to support them, and
this is worth stating plainly rather than filed as agreement.**

- Both of its instruments are **structural, not plate-derived**. `seam-screen.py` tests
  whether a tail clause parses; `check-vol5-apparatus.py` tests 1..N continuity of
  ownership *against `KNOWN_TOTALS`, which is itself a hand-entered band read*. Neither
  can see a note the raw never had, and neither can see a body paragraph the chunk was
  written short of. The 130-entry figure is re-derived here and matches; the totals are
  re-derived **from the bands** here and match. That is the check the shakedown did not
  perform.
- Its count of **"14 mid-page boundaries"** is right for the mid-page class but is not
  the boundary count for this scope: there are **16 boundaries**, the extra two being the
  leaf crossings p. 208 → p. 210 (across the unchunked capitula table) and p. 218 → p. 219.
  Both are exactly the seams where a forwarded note goes missing, and neither was in the
  shakedown's denominator. Both are clean.
- Its closing generalisation — "nothing forwarded from p.218's footer, so the first Pars
  II chunk starts clean" — is **confirmed on the band** (p. 218 n. 7 ends complete on the
  page). Per the CLAUDE.md rule that a structural generalisation is the least reliable
  line in any Notes block, it was re-derived rather than quoted.
- Its pass-2 line ("Vol V contributes zero flags") is out of this pass's scope and is not
  endorsed here either way.

---

## Disposition

**PASS 3 CLEAN for the Prologue and Pars I. Zero defects, zero repairs, no chunk edited,
`KNOWN_TOTALS` unchanged.** Nothing is forwarded to the Pars II agent: the
`p1-c9 → p2-c1` seam is clean from this side, p. 218's register is exhausted by `p1-c9`,
and `p2-c1` correctly opens its own page-219 register at n. 1.
