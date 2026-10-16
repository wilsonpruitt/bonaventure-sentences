# Ruling 57 (C1): the coordinate `ibid.` fix, before/after ledger diff

> **For Wilson's review before the p. 235 deploy.** Tool change only: `tools/build-citations.py`.
> **No chunk under `vol*/` was touched** (`git status` over vol1–vol6 is empty).
> Built 2026-10-16. Before = the ledger at `ab4c176` (28,709 records, reproduced byte-identical before
> the change). After = this commit's `index/citations.tsv`.
> Full list of every changed record: **`manual-review/ruling57-c1-changes.tsv`** (387 rows, with the Latin context of each).

## 1. What changed in the tool

- **Capture.** In `scan_relative`, a lower-case `ibid.` followed by `C, V` (with an optional `-V` range) or
  `v. N` (also `ibid v. N` with the point dropped) now records its own coordinates, and its `raw_text`
  becomes the printed form (`ibid. 41, 3`). It is never treated as a Sentences inheritance: Sentences
  coordinates always carry `d.`, so `IV. Sent. d. 15 …; ibid. 5, 3` is not a Sentences reference.
  A bare number (`ibid. 54.`) is **not** captured, because it could be a chapter or a verse and the
  ledger does not guess. Those stay under the bare-`ibid.` rule.
- **Resolve (`resolve_coord_ibid`).** `ibid. C, V` takes the antecedent's **book** and its own C:V.
  `ibid. v. N` takes the antecedent's book **and chapter** and its own verse. The antecedent is tried
  in this order, and if none qualifies the record is **left unresolvable**:
  - (a) **The nearest scripture locus in the same note.** The walk skips non-scripture and Sentences
    loci. Index rule 3 applies: a locus inside a closed parenthesis is an aside. Index rule 5 applies:
    if an author siglum is named between that locus and the `ibid.`, the chain belongs to that author,
    so the record is left unresolvable. A siglum inside a closed parenthesis does not count. A
    `Libr. N.` barrier stops the walk, and so does an intervening `loc. cit.`.
  - (b) **The body-ordinal join through the note's own anchor.** This covers `Vers. 21; ibid. 6, 3`,
    where the note's first locus is the body's `Genesis octavo`[^n]. The join must give one book, and
    for `v. N` it must also give one chapter.
  - (c) **The last citation of the previous note.** This is allowed only when the `ibid.` opens its
    note with nothing numeric before it, and only onto a scripture record. In this corpus it fired
    **zero times**, because every lower-case coordinate `ibid.` stands after some locus of its own.
  - **Cross-chunk.** An `ibid.` crosses a chunk boundary only on the same terms as (c). It also fired
    zero times.
- **Confidence.** A coordinate `ibid.` resolved in the same note (a) or from the previous note (c) is
  **A**. One resolved by the body join (b) is **B**, the same tier as the join it rests on.
- **Bare `ibid.` is unchanged.** Its rule is untouched. Section 5 lists the six places where it now
  shows a different record because its input changed.
- **C2 override table (`PRINTED_SLIPS`).** Six printed slips are **filed as printed**. Each gets a QA
  line naming the passage meant, in a new QA-report section. Each entry is keyed by chunk + section +
  anchor + filed target, and must match exactly one record, otherwise it reports itself as stale. All
  six matched: c1 Job 6:2 (6:25), c3 p. 126 n. 1 Job 24:19 (5:19), c5 Cor* 12:30 (I Cor 12:31),
  c11 p. 180 Prov 16 (24:16), c16 Ecclus 11:3 (Eccles 11:3), c18 Ezech 20:30 (22:30).
- **Out of scope, not touched, reported here:** capital `Ibid. C, V` (section 7), body `ibidem` (section 7),
  `loc. cit. v. N`, and the rest of the C3–C5 classes.

## 2. The C1 class, before → after

Measure: every lower-case `ibid.` + `C, V` / `v. N` in a Latin apparatus entry. That gives **380 sites**
(none in the body or scholia). This is wider than the mid-work gate's 251, which counted only the sites
then filed as scripture, before c13–c19 were built, and probably with a narrower pattern. The
**302 old scripture records** below correspond to it: I 5 · II 29 · III 29 · IV 61 · V 88 · VI 90.
The gate counted I 4 · II 24 · III 23 · IV 49 · V 88 · VI 63, plus the c13–c19 sites.

| Vol | sites | **before**: scripture (honoured) · false crossref · authority · no record | **after**: honoured (A / B) · left unresolvable |
|---|---|---|---|
| I | 9 | 5 (0) · 3 · 0 · 1 | **7** (5 / 2) · 2 |
| II | 34 | 29 (0) · 4 · 1 · 0 | **26** (14 / 12) · 8 |
| III | 42 | 29 (0) · 9 · 1 · 3 | **34** (18 / 16) · 8 |
| IV | 82 | 61 (0) · 17 · 1 · 3 | **66** (26 / 40) · 16 |
| V | 111 | 88 (0) · 12 · 0 · 11 | **82** (72 / 10) · 29 |
| VI | 102 | 90 (1) · 9 · 0 · 3 | **86** (22 / 64) · 16 |
| **all** | **380** | **302 (1)** · 54 · 3 · 21 | **301** (157 / 144) · **79** |

- **Honoured: 1 → 301.** Of the 250 records that were scripture before and scripture now, **138 + 20
  kept their book and moved to their own C:V**. **92 changed BOOK.** These were the wrong-book
  cross-note bindings, and every one was repaired by the body join, e.g. c12 p. 186 n. 2 Ps 73:12 → Gen 6:3.
- **54 false cross-references are gone.** For example, c10 p. 177 n. 4 → `II:d40` is now Exod 15:6,
  and III d18 p. 392 n. 2 → `IV:d45` is now Gen 42:38. 30 of them became scripture verses and 24 became
  unresolvable. **3 false authority records** became scripture verses (II d28 a1 q1 n. 1, III d1 a2 q2 n. 2,
  IV d23 a1 q1 n. 1).
- **21 sites had no record before.** `dedupe()` had collapsed them into an earlier `ibid.` in the same
  note that carried the same `raw_text` and the same copied target. Now 17 are honoured and 4 are unresolvable.
- **79 left unresolvable, rather than guessed:**

  | why | n |
  |---|---|
  | the note has a locus of its own the ledger did not capture (`Cap. 7, 25. — … ibid. v. 26`, where the body names the book without an ordinal, or `Vers. 27; ibid. v. 21` with the body at an internal `supra decimo sexto`, the parked C4 class) | 69 |
  | no scripture locus in the note, and an author named before it (Beda, August., Anselm., Alex. Hal., Bonav.) | 5 |
  | an author named between the locus and the `ibid.` (August., Chrysost.) | 2 |
  | a `loc. cit.` intervenes (III d9 a1 q5 n. 4) | 1 |
  | `Libr. II.` barrier: the book is named only in the body (don-c3 p. 472 n. 4) | 1 |
  | opens its note, and the previous note's last citation is not scripture (III d32 a1 q3 n. 15) | 1 |

  The full list, with chunk and raw text, is the new QA-report section *Coordinate `ibid.` left unresolvable*.
  **53 of the 79 were scripture records before.** They were all at a wrong verse, because only 1 of 302
  was honoured. Some were at the right book: their notes cite a book the body names without an ordinal.
  Those 53 entries leave the scripture index. The remaining 26 were false crossrefs or authority records,
  or had no record.

## 3. Ledger counts

**Records: 28,709 → 28,736 (+27). 360 changed · 27 added · 0 removed.**

| Vol | records before → after | changed | added |
|---|---|---|---|
| I | 2,331 → 2,332 | 8 | 1 |
| II | 4,829 → 4,829 | 34 | 0 |
| III | 5,058 → 5,063 | 39 | 5 |
| IV | 6,511 → 6,516 | 80 | 5 |
| V | 5,012 → 5,025 | 100 | 13 |
| VI | 4,968 → 4,971 | 99 | 3 |

- **What the 360 changed records are:** 359 coordinate-`ibid.` sites that had a record before, plus 1
  bare-`ibid.` knock-on (section 5).
- **What the 27 added records are:** 17 honoured and 4 unresolvable coordinate sites (dedupe no longer
  collapses them), plus **6 bare `ibid.`s** that dedupe had collapsed into a coordinate `ibid.` at the
  same note. They surfaced because the two `raw_text`s now differ (section 5).

**By class:** scripture 15,667 → 15,671 (+4) · crossref 11,878 → 11,904 (+26) · authority 1,164 → 1,161 (−3).

**By resolution level:**

| | before | after | Δ |
|---|---|---|---|
| scripture `verse` | 13,518 | 13,533 | +15 |
| scripture `chapter` | 2,128 | 2,118 | −10 |
| scripture `unresolvable` | 11 | 10 | −1 |
| crossref `chunk` | 8,664 | 8,627 | −37 |
| crossref `page-multi` | 1,358 | 1,352 | −6 |
| crossref `distinctio` | 776 | 772 | −4 |
| crossref `work` | 213 | 211 | −2 |
| crossref `dangling` | 227 | 225 | −2 |
| crossref `unresolvable` | 190 | 267 | +77 |
| `articulus` 276 · `ambiguous` 171 · `forward` 3 · authority `excluded` | — | — | unchanged (excluded −3) |

**By confidence tier (scripture):** A 10,279 → 10,176 (−103) · B 3,242 → 3,360 (+118) · C 2,135 → 2,125 (−10).
A falls and B rises because the 144 body-joined records are B. The 92 wrong-book records among them were
filed at A before, inherited from an unrelated apparatus locus.

**Anaphora line:** 2,192 within + 89 cross-chunk (unresolved 180) → 2,146 within + 86 cross-chunk
(unresolved 257). The +77 unresolved are the 79 coordinate sites above, less 2 that were already unresolved.

**Site index** (`build-index-json.py`): scripture 15,646 → 15,651 indexed citations, 77 books.
Cross-reference **1,732 → 1,732 chunks cited**, **10,560 → 10,559 backlinks**. The backlink total barely
moves: the false crossrefs that are gone (54) mostly duplicated a backlink pair already present, and one
false crossref surfaced (section 5).

## 4. QA flags

- **Dangling / out-of-range: 208 → 208, and the QA tuples are identical as a multiset**, checked by
  position diff. No QA line is new and none was removed. No honoured coordinate falls beyond its book's
  chapter count. The 2 old `dangling` records were anaphor copies of a dangling antecedent, whose own QA
  line is unchanged.
- **New section *Printed slips filed as printed*: 6 lines**, the C2 table above, 0 stale.
- **New section *Coordinate `ibid.` left unresolvable*: 79 lines** (section 2).
- **The existing *Unresolved anaphora* list: 180 → 257.** The +77 are the coordinate sites. Their rows
  now show the printed coordinates in `raw`.

## 5. Changes I believe WRONG or doubtful

None of the 301 honoured coordinate records is known to be wrong. The faults below all come from the
**unchanged bare-`ibid.` rule**, which now sees a different input.

| # | record | before → after | verdict |
|---|---|---|---|
| 1 | IV d15 p1 littera n. 2, bare `ibid.` after *C. Ignis succensus est (43.)* (Gratian) | 2Reg 24:1 → **Ios 22:20** | **WRONG both times.** It is a canon-law `ibid.` filed as scripture. Its cross-chunk tail (IV d14 p2 dubia n. 47) is now Ios 22:20, which is right there, and the bare rule copies it. |
| 2 | don-c9 p. 500 n. 6, bare `Cfr. ibid. VI. c. 12` (Aristotle, *Ethic.*), **surfaced** | — → crossref `bon-sent-I-d1-a3-q2` | **WRONG.** The same wrong target was carried before by the note's `ibid. 7, 8`, which is now correctly unresolvable (`Cap. 8, 2` = Wisdom 8:2, with the book only in the body). The wrong crossref moved from one record to the other. Net: still one false backlink. |
| 3 | III d40 a1 q2 n. 19, bare `Et ibid. n. 128` (Isidore/Augustine section), **surfaced** | — → Ioan 5:46 | **WRONG** (bare class). |
| 4 | IV d43 littera p. 881 n. 3, bare `Explicatio Hieronymi est ibid.`, **surfaced** | — → Cor* 4:5 | **WRONG.** The note is about `Cap. 65, 17. 18` = Isaiah. The coordinate `ibid. v. 16` beside it held the same wrong Cor* 4:5 before and is now unresolvable. |
| 5 | don-c3 p. 470 n. 3, bare-number `ibid. 37. et 41.`, **surfaced** | — → Gen 6 (chapter) | Book right, chapter wrong (the passage is Gen 37 and 41). This is the bare-number class left out of scope. |
| 6 | IV d14 p1 littera n. 2, `ex Glossa ordinaria ibid.`, **surfaced** | — → Matth 3:2 | **Doubtful.** The Glossa is more likely on Matth 4:17, the coordinate `ibid.` just before it. |
| 7 | III d34 p1 littera n. 9, `apud August. ibid. Enarrat.`, **surfaced** | — → Ps 5:8 | Doubtful but harmless. It means Augustine's *Enarratio* on that psalm. |

- **Items 2–7 are not new errors.** Each is a bare `ibid.` that `dedupe()` used to collapse into the
  coordinate `ibid.` of the same note, because both had `raw_text` "ibid." and the same copied target.
  A distinct occurrence now gets its own record, which is the ledger's "one record per occurrence"
  principle. All of them belong to the bare-`ibid.` class: non-scripture `ibid.`s copying the previous
  record (the C1 evidence named this class: *Moralia* → Ps 77:42, *Comment. dub. 6* → Apoc 20:12).
- **Two losses I accepted, and they are worth your eye.**
  - II d18 a1 q2 n. 1 `De formatione mulieris ibid. v. 21` was Gen 2:2 and is now unresolvable. An
    `August.` quotation stands between it and its locus. Gen 2:21 is surely meant, but the governance rule
    cannot know that.
  - IV d4 littera n. 5c `(Levit. 21, 13.). Est etiam apud Lyranum ibid. v. 12` is now unresolvable,
    because its only locus is inside a closed parenthesis.

  Both are the rules working as written.

## 6. Representative sample, hand-checked against the note text (25 records, all six volumes)

| # | chunk · note | Latin (abridged) | before → after | check |
|---|---|---|---|---|
| 1 | I d11 littera · n. 6 | `Ioan. 14, 26 et sequens locus ibid. 15, 26, ubi Vulgata: a Patre procedit` | Ioan 14:26 → **Ioan 15:26** (A) | ✓ the Vulgate words are 15:26 |
| 2 | I d45 a1 q1 · n. 5 | body *Ad Ephesios primo*; `Vers. 11. — Textus sequens habetur ibid. v. 5.` | crossref I d47 a1 q1 → **Eph 1:5** (B) | ✓ |
| 3 | I d31 p2 a2 q2 · n. 1 | body *primae ad Corinthios tertio*; `Vers. 8. … cfr. ibid. v. 6.` | Cor* 6 → **Cor* 3:6** (B) | ✓ (I Cor 3:6; the bucket is inherited from the body record) |
| 4 | I d37 littera · n. 23 | `Primus locus respicit Sap. 8, 1; secundus ibid. 7, 25.` | Sap 8:1 → **Sap 7:25** (A) | ✓ |
| 5 | II d22 a1 q1 · n. 6 | body *ad Romanos quinto*; `Vers. 19 … Seq. textus est ibid. v. 12: Sicut per unum hominem peccatum…` | Gen 3:5 → **Rom 5:12** (B) | ✓ the quotation is Rom 5:12; it was the wrong book before |
| 6 | II d28 a1 q3 · n. 1 | body *Deuteronomii trigesimo*; `Vers. 11 … Seq. textus est ibid. v. 14` | Cor* 13:3 → **Deut 30:14** (B) | ✓ |
| 7 | II d33 a1 q2 · n. 13 | `Eph. 1, 22: Et ipsum dedit caput…; et ibid. 5, 23: Sicut Christus caput est Ecclesiae` | Eph 1:22 → **Eph 5:23** (A) | ✓ |
| 8 | II d31 littera · n. 7 | `Comment. in Epist. ad Rom. 7, 18. (inter opera S. Ambros.). Seq. locus est ibid. v. 22.` | Rom 7:18 → **Rom 7:22** (A) | ✓ (the parenthetical siglum is masked) |
| 9 | III d18 a2 q3 · p. 392 n. 2 | `Cfr. IV. Sent. d. 45 … Gen. 37, 35: Descendam… ; nec non illa eiusdem, ibid. 42, 38: Deducetis canos meos` | crossref IV:d45 → **Gen 42:38** (A) | ✓ the false crossref is gone |
| 10 | III d38 a1 q2 · n. 7 | body *Genesis vigesimo secundo*; `Vers. 5. — Seq. textus est ibid. 26, 7; tertius ibid. 42, 9 …, et quartus ibid. 44, 15` | Iudic 9:8 → **Gen 26:7** (B), + Gen 42:9, Gen 44:15 added | ✓ the lies of Isaac and Joseph; wrong book before |
| 11 | III d40 a1 q2 · n. 6 | `Rom. 7, 7 … Cfr. ibid. 3, 20, et August.` | Rom 7:7 → **Rom 3:20** (A) | ✓ |
| 12 | III d9 a1 q5 · n. 4 | `Psalm. 5, 8. — Seq. … loc. cit. v. 17. Cfr. ibid. 6, 19, nec non II. Cor. 6. 16.` | Ps 5:8 → **unresolvable** | ✓ correct refusal: it is I Cor 6:19 (via the *loc. cit.*); "Ps 6:19" would have been wrong |
| 13 | IV d22 a2 q1 · n. 7 | body *Matthaei quarto*; `Vers. 17. — Seq. locus est ibid. 3, 2; tertius ibid. 8, 4: Vade, ostende te sacerdoti` | crossref IV d17 → **Matth 3:2** (B) | ✓ (Matth 8:4 likewise) |
| 14 | IV d6 p1 a1 q4 · n. 9 | `B. Albert. … pro secunda II. Reg. 23, 8. seqq.; de tertia cfr. ibid. 15, 24` | 2Reg 23:8 → **2Reg 15:24** (A) | ✓ (Sadoc and the Levites) |
| 15 | IV d33 a1 q1 · p. 748 n. 3 | body *primae ad Corinthios sexto*; `Vers. 9. seq. … Seq. textus est ibid. 7, 2` | Deut 5:18 → **Cor* 7:2** (B) | ✓ wrong book before |
| 16 | IV d44 p2 a1 q1 · p. 921 n. 6 | `Hic error describitur Sap. 2, 1. seqq. Cfr. ibid. 5, 1. seqq.` | Sap 2:1 → **Sap 5:1** (A) | ✓ |
| 17 | bon-brev-prol · p. 202 n. 3 | `Respicitur Ioan. 6, 69 … et ibid. 20, 31: Haec autem scripta sunt` | Ioan 6:69 → **Ioan 20:31** (A) | ✓ |
| 18 | bon-don-c3 · p. 468 n. 4 | `de Manasse vide IV. Reg. 21, 1. seqq.; ibid. 22, 1. seqq. de Iosia … Octo annorum erat Iosias` | 4Reg 21:1 → **4Reg 22:1** (A) | ✓ |
| 19 | bon-hex-c14 · p. 398 n. 1 | `Apoc. 1, 13 … De gladio acuto ibid. 1, 16. et de falce acuta ibid. 14, 14. — De caelo novo … ibid. 21, 1.` | (collapsed) → **Apoc 1:16, 14:14, 21:1** added (A) | ✓ |
| 20 | bon-qpe-q2-a3 · p. 160 n. 10 | body *Exodi primo*; `Vers. 13, seq. … Seq. locus est ibid. 5, 4.` | 1Tim 5:17 → **Exod 5:4** (B) | ✓ wrong book before |
| 21 | bon-red · p. 319 n. 4 | `Epist. ad Pisones sive de Arte poetica, v. 333; seq. versus est ibid. v. 343.` | Prov 8:24 → **unresolvable** | ✓ it is Horace; the false scripture entry is removed |
| 22 | bon-sap-c12 · p. 186 n. 2 | body *Genesis octavo*; `Vers. 21; ibid. 6, 3. est seq. locus, in quo post homine Vulgata addit in aeternum.` | Ps 73:12 → **Gen 6:3** (B) | ✓ (resume list) |
| 23 | bon-sap-c15 · p. 205 n. 3 | body *ad Romanos quinto*; `Vers. 1; ibid. 4, 3. est seq. locus.` | Sap 15:10 → **Rom 4:3** (B) | ✓ (resume list) |
| 24 | bon-sap-c18 · p. 223 n. 6 | `Exod. 12, 28 … cfr. ibid. v. 50. (ibid. v. 11: Sic autem comedetis illum…` | Exod 12:28 → **Exod 12:50**, + **Exod 12:11** added (A) | ✓ (resume list; the `v. 23. et 29.` continuations are still C3) |
| 25 | bon-eccl-c2-v4-10 · p. 21 n. 5 | body *tertii Regum decimo*; `Vers. 23 … Sequitur ibid. 9, 10. De domo filiae Pharaonis cfr. ibid. 7, 8.` | Eccli 6:23 → **Reg* 9:10** (B), + **Reg* 7:8** added | ✓ (III Kings 9:10 and 7:8, in the numbered bucket) |

**The Sapientiae sites logged since the mid-work gate (resume ⛔ block), checked one by one:**
- **Honoured as logged:**
  - c14: p. 197 nn. 6, 7, p. 198 n. 2 (Col 1:20), p. 199 n. 13 (II Kings 12:16 → `Reg* 12:16`).
  - c15: p. 205 n. 3, p. 207 n. 8.
  - c16: p. 210 nn. 7, 8, 9, p. 215 nn. 5, 12.
  - c17: p. 217 n. 8, p. 221 n. 5.
  - c18: p. 222 n. 10, p. 223 nn. 2, 6, p. 225 n. 10, p. 226 n. 6.
  - c19: p. 228 nn. 6, 8.
  - Also: c12 p. 186 n. 2, p. 187 n. 5, p. 185 n. 2; c4 p. 132 n. 2; c11 p. 180 n. 4; c10 p. 177 n. 4;
    c8 p. 164 n. 11; c2 p. 121 n. 2.
- **Left unresolvable:** **c19 p. 232 n. 8** `Vers. 27; ibid. v. 21` (the logged target is Sap 16:21). Its body
  locus is the internal *supra decimo sexto*, which the ledger does not parse (C4, parked), so there is no
  book to inherit. It was Sap 16:17 before (right book, wrong verse), and it is now absent from the index.
- **Not in scope, so unchanged:**
  - The bare / non-coordinate sites: c15 p. 206 n. 4 `ibid. est etiam seq. locus`, c19 p. 230 n. 12
    `ibid. in nota adiecta`, c19 p. 229 n. 4.
  - The second loci of chains, which are C3: `et 2, 15`, `v. 23. et 29.`, `13. et 14.`.
  - The **body `ibidem` sites**: c15 p. 205 *item ibidem quarto*, c16 p. 210 ×2 and p. 216, c17 p. 218
    *ut patet ibidem*.

## 7. Classes found but deliberately NOT changed (for a later ruling)

- **Capital `Ibid. C, V` / `Ibid. v. N`: 98 sites** (I 1 · II 4 · III 6 · IV 5 · V 73 · VI 8). They produce
  **no ledger record at all**, because `scan_relative` matches lower-case `ibid` only. Example: hex-c14
  p. 398 n. 1 `Ibid. v. 16`. Admitting them would add up to about 98 records under the same rules. That
  would be an expansion beyond the measured class, so it is left for your go.
- **Body `ibidem` + ordinal, or `ibidem`[^n] + `Vers. N`:** about 104 body scripture anaphors copy the
  antecedent's verse. The Sapientiae logged 5 of them. This is the same defect on the body side, but it
  is not this spec.
- **`loc. cit. v. N`** (for example II d28 a1 q1 n. 1 `tertius loc. cit. v. 5`) and **bare-number `ibid. 54.`
  (9 sites)**. Both are unchanged.

## 8. Build results (unchanged except the index)

- `build-citations.py`: 2,187 chunks, 28,736 records, QA 208, 232 chunks with no citation. The run prints
  two new lines: `coordinate ibid. (r.57): 380 honoured 301 left unresolvable 79` and
  `printed slips (r.57 C2): 6 annotated, 0 stale`.
- `build-index-json.py`: 1,732 cited / 10,559 backlinks (was 10,560); 15,651 scripture citations (was 15,646).
- `build-content.mjs`: **16 books / 2,186 / 2,186 translated**, unchanged.
- `check-vol5-apparatus.py --volume=vol6`: **68 chunks / 2,208 entries, all passed**, unchanged.
- `polish-style-scan.py`: **11 issues / 6 chunks / 2,187 scanned**, unchanged.
- `git status` over `vol1`–`vol6`: **empty**.

Method: the position-keyed diff loads the old and new tool side by side and matches records by
chunk + section + character offset. That is how the 21 previously collapsed sites and the 6 surfaced bare
records are told apart from changes.
