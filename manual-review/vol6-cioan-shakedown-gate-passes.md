# Vol VI *Collationes in Evangelium S. Ioannis* SHAKEDOWN GATE (p. 559, ruling 123): passes 1–3 (read-only agent, 2026-11-06)

Run on Wilson's order (2026-11-06). No chunk, tool, ledger, registry or resume note was edited; nothing committed, pushed,
deployed or deleted. `build-citations.py` was pointed at scratch paths (`--out`/`--qa`), so `index/` was not rewritten; `git status
--short` afterwards shows only the pre-existing untracked `.claude/settings.local.json`. `colcrop.py` wrote its bands to `/tmp/colcrop/`
(outside the repo, as usual). Register and form questions are in the parallel `…-evidence-sheet.md` and are not repeated here.

**Scope: 4 chunks, `bon-cioan-c1` … `bon-cioan-c4`, pp. 535–559, 202 numbered apparatus entries (80 / 45 / 36 / 41), + 6 `tr-` notes**
(c1 `tr-lumen`, `tr-doctrina` · c3 `tr-doctrina`, `tr-lumen` · c4 `tr-lumen`, `tr-vacare`; c2 none; Latin `tr-` = 0 in all four).
202 = the sum of `KNOWN_TOTALS_VOL6` for pp. 535–559, re-derived independently of the checker (below).

| chunk | division | pages | entries | Collationes | Annotationes |
|---|---|---|---|---|---|
| `bon-cioan-c1` | 1 | 535–545 | 80 (p. 545 n. 1 only) | I–VII | 1–3 |
| `bon-cioan-c2` | 2 | 545–550 | 45 (p. 545 nn. 2–7 … p. 550 nn. 1–4) | VIII–X | 4–6 |
| `bon-cioan-c3` | 3 | 550–554 | 36 (p. 550 n. 5 … p. 554 nn. 1–8) | XI–XIII | 7–11 |
| `bon-cioan-c4` | 4 | 554–559 | 41 (pp. 555–559; none on p. 554) | XIV–XIX | 12–17 |

---

## PASS 1: live flags. **CLEAN (two expected hits only)**

`python3.11 tools/check-live-flags.py vol6` → **scanned 181 chunks in vol6; LIVE [?] FLAGS: 2 occurrence(s)**:
`vol6/bon-cioan-c2.md:243` (`[^p545-6]` La) and `:245` (its En mirror). Both are the editors' own printed `[?]` in the Bede quotation
of p. 545 n. 6 (*id est in caelo [?] transmigrationis*), gate item S5, **confirmed on the 450 dpi plate in this pass** (p. 545 right
footer block, line 5). No other flag in vol6. Denominator 181 = all of vol6 as built, the four in scope included. (The tool exits 1
because it found hits; that is the expected behaviour, not a failure.)

## PASS 2: mechanical suite + parity. **CLEAN; 3 digit-multiset mismatches, all false positives**

| tool | denominator / result | verdict |
|---|---|---|
| `check-vol5-apparatus.py --volume=vol6` | header `volume: vol6 (181 chunks, 542 known page totals)`; **181 chunks, 5,813 entries, all checks passed**; La = En in all four (80/80, 45/45, 36/36, 41/41); pp. 535–559 every page `ok`, nothing PENDING | CLEAN |
| `check-vol5-census.py` | **vol6 181 on disk / 181 in ledger, "Rosters agree"**; vol6 295 runovers (272 gutter / 23 page), 144 positive / 37 negative; vol5 167/167 | CLEAN |
| ↳ in scope | **13 runovers (12 gutter / 1 page) in 4 positive chunks** (c1 5 · c2 3 + 1 page · c3 3 · c4 1); page-crossing list includes p. 549 n. 10 | see Pass 3 |
| `polish-style-scan.py` | **11 issues / 6 chunks / 2,300 scanned** (PAIR 10 / 5 chunks, V5LABEL 1 / 1), all pre-existing, outside Vol VI; **0 in `bon-cioan-*`** | CLEAN |
| `validate-chunk.py vol6/bon-cioan-c{1..4}.md` (takes paths; no `--help`) | **4 checked, 0 failed** | CLEAN |
| `build-citations.py --out/--qa` (scratchpad) | **2,300 chunks → 33,254 records; QA flags 211**; anaphora unresolved 285; coordinate ibid. 446 (honoured 339 / unresolvable 107); printed slips 6 annotated, 0 stale. Ledger **byte-identical** to `index/citations.tsv`; QA report **byte-identical** to `manual-review/citation-qa-report.md` (`cmp` silent on both) | CLEAN |
| ↳ **attributable to this scope** | **666 records** (c1 249 · c2 137 · c3 123 · c4 157): scripture 652 (A 324 · B 125 · C 203), crossref 14 (chunk 11 · page-multi 1 · forward 2). **QA flags ours: 0 of 211** (no `bon-cioan` row in any QA section: dangling, anaphora, printed slips, coordinate ibid.). The two `forward` records are both `bon-cioan-c4` p. 556 n. 8 (`infra pag. 567`, `annotat. 22`), pointing into Capitulum V+, not yet built: expected | CLEAN |

**Per-chunk parity (Latin vs English, counted over the rendered `## Latin` / `## English` regions):**

| chunk | paragraphs La/En | `### ` headings La/En | `<!-- page N -->` La = En | `[^…]` markers La/En, order | ¶ numbers La = En |
|---|---|---|---|---|---|
| c1 | 84 / 84 | 12 / 12 | 535–545 (11), identical | 80 / 80, identical order | 48, identical |
| c2 | 46 / 46 | 7 / 7 | 545–550 (6), identical | 45 / 45, identical order | 29, identical |
| c3 | 42 / 42 | 9 / 9 | 550–554 (5), identical | 36 / 36, identical order | 18, identical |
| c4 | 59 / 59 | 13 / 13 | 554–559 (6), identical | 41 / 41, identical order | 22, identical |

(`tr-` anchors are English-only by design and excluded from the marker comparison.) No def without an anchor and no anchor without a
def (`check-vol5-apparatus.py` pairing, and the marker lists equal the def lists).

**La/En digit multiset per apparatus entry: 3 mismatches of 202, all false positives, 0 defects.** All three are translator's
`[so printed; …]` brackets in the **En.** half that add the true locus beside a printed slip (the ruling-89 bracket class); the
**La.** half transcribes the print in every case:
- `bon-cioan-c1.md:500–502` p. 537 n. 6: `Ps. 75, 2` → En adds `[so printed; the verse is Ps. 75:3]` (Vulgate 75:3 *et factus est in pace locus eius*, the verse the body quotes). En extra digits `75`, `3`.
- `bon-cioan-c1.md:676–678` p. 543 n. 4: Horace, *Ars poetica* `v. 243` → En adds `[so printed; the line is v. 343]` (*omne tulit punctum…*). En extra `343`.
- `bon-cioan-c4.md:333–335` p. 556 n. 1: `Luc. 16, 10. seqq.` → En adds `[so printed; the rich glutton's parable opens at Luke 16:19]` (the body's *Exemplum de divite epulone*). En extra `16`, `19`. **The print's `10` was confirmed on the 450 dpi plate in this pass** (p. 556 left footer, n. 1), so the bracket is a true printed-slip note, not a misread.
NOTE (not a defect, for the docket, not decided here): none of the three is in `build-citations.py`'s ruling-57 C2 printed-slip table (it reports 6 annotated, 0 ours), so the ledger records the printed loci as given.

**Frontmatter (4 of 4 CLEAN):**
- `printed_pages` contiguous in all four (535–545, 545–550, 550–554, 554–559), and the set of `<!-- page N -->` markers = `printed_pages` in 4/4.
- `pdf_pages` = printed + 42 in 4/4.
- `collationes:` = the `### Collatio N.` headings actually present, and = the English `### Collation N.` headings: c1 [1–7] · c2 [8–10] · c3 [11–13] · c4 [14–19]. **Contiguous I–XIX across the four, no gap, no repeat.**
- `annotationes:` = the `### Annotatio N.` / `### Annotation N.` headings present: c1 [1–3] · c2 [4–6] · c3 [7–11] · c4 [12–17]. **Contiguous 1–17.**
- `division` = 1, 2, 3, 4.

**Registry (`site/scripts/build-content.mjs`, `"collationes-ioannem"`, book 18, tome 6, `divisionLabel: "Capitula"`): divisions 1–4
against the in-place headings: 4 of 4 MATCH.**
1 `Capitulum I: In principio erat Verbum` = `### Capitulum I. *In principio erat Verbum.*` · 2 `Capitulum II: Nuptiae factae sunt` =
`### Capitulum II. *Nuptiae factae sunt.*` · 3 `Capitulum III: Erat autem homo ex Pharisaeis` = `### Capitulum III. *Erat autem homo
ex Pharisaeis.*` · 4 `Capitulum IV: Ut autem cognovit` = `### Capitulum IV. *Ut autem cognovit.*`. `title_la` agrees in all four. The
p. 545, 550 and 554 headings were also read on the plate in this pass (Pass 3), and the p. 560 `Cᴀᴘɪᴛᴜʟᴜᴍ V. *Post haec…*` too. The
`buildWorkChunkTitle` branch returns `Cap. ${division}` for the work.

## PASS 3: boundary sweep. **CLEAN**

**Ownership.** Every `[^pP-N]` def in all 181 vol6 chunks was parsed and checked against `KNOWN_TOTALS_VOL6` (parsed out of
`tools/check-vol5-apparatus.py`): **every page 535–559 carries exactly its run 1..N, each entry owned once, 0 mismatches on 25 pages**;
p. 560 has no KNOWN_TOTALS line and no entry, as built. Per page: 535 5 · 536 9 · 537 6 · 538 8 · 539 5 · 540 9 · 541 10 · 542 8 ·
543 10 · 544 9 · 545 7 · 546 9 · 547 8 · 548 8 · 549 10 · 550 5 · 551 8 · 552 8 · 553 11 · 554 8 · 555 9 · 556 10 · 557 9 · 558 7 ·
559 6 = **202**.

**Seams (each leaf read on the 450 dpi plate, `colcrop.py vol6 <p> <gutter> 4` bands only, gutters as recorded in the chunks' Notes;
p. 560 profiled fresh: band 1154–1200, centre-rule island 1174–1180, midpoint 1177):**

| seam | split by anchor (plate) | owned in files | outgoing tail | incoming head | verdict |
|---|---|---|---|---|---|
| **p. 545** c1→c2 | n. 1 anchors Annot. 3's *deserto*¹ (right col. head, c1); nn. 2–7 below `Cᴀᴘɪᴛᴜʟᴜᴍ II.` (c2) | c1 n. 1 · c2 nn. 2–7 | *…Illum oportet crescere, me autem minui ».* complete, directly above the full-measure heading | `### Capitulum II. *Nuptiae factae sunt.*` → `### Collatio VIII.` → `(Vers. 1.)` | CLEAN |
| **p. 550** c2→c3 | n. 4 anchors Annot. 6's *in Psalmo*⁴ (c2); n. 5 anchors c3 ¶ 2's *Iob quinto*⁵, below `Cᴀᴘɪᴛᴜʟᴜᴍ III.` | c2 nn. 1–4 · c3 n. 5 | *…quae a te facta est ».* complete | `### Capitulum III. *Erat autem homo ex Pharisaeis.*` → `### Collatio XI.` → `(Vers. 4.)` | CLEAN |
| **p. 554** c3→c4 | n. 8 anchors Annot. 11's *Ioannis primo*⁸, the leaf's last anchor (c3); Cap. IV's body on the leaf (¶ 1 *Notandum hic…* / *…summo descendens;*) carries **no anchor** | c3 nn. 1–8 · c4 none | *…« Verbum caro factum est ».* complete | `### Capitulum IV. *Ut autem cognovit.*` → `### Collatio XIV.` → `(Vers. 6.)` | CLEAN |
| **p. 559 / 560** c4→c5 | p. 559's last anchor is Annot. 17's *supra secundo*⁶ = n. 6 of 6; white below Annot. 17 (~0.75 of the right column). p. 560 opens at its head on full-measure `Cᴀᴘɪᴛᴜʟᴜᴍ V. *Post haec…*`, `COLLATIO XX.`, `(Vers. 2.)`, ¶ 1 *Moraliter*; **its register opens numbered `¹ Psalm. 59, 4.`** | c4 p. 559 nn. 1–6; nothing on p. 560 | *…operibus credite » etc.* complete (as printed) | (c5 not built) p. 560 starts at n. 1 | CLEAN (leaf edge) |

No seam shows a splice; every outgoing tail is a complete sentence; every incoming body opens on its `Capitulum` heading.

**Ledger vs plates.** `manual-review/vol6-runover-ledger.tsv` lines 195–198:
`bon-cioan-c1` p.535 n.1 · p.538 n.5 · p.540 n.6 · p.543 n.6 · p.544 n.5 (all gutter) · `bon-cioan-c2` p.545 n.6 · p.546 n.4 · p.548 n.6
(gutter), p.549 n.10 (page) · `bon-cioan-c3` p.551 n.4 · p.552 n.4 · p.554 n.6 (gutter) · `bon-cioan-c4` p.556 n.8 (gutter).
**The head of BOTH footer blocks was read on all 25 leaves** (a strip of the first lines of each block below the footer rule, plus the
colcrop bands at the seams). **Unnumbered block heads found: exactly 13** = the 13 ledger rows:
- right block opens unnumbered (gutter runover) on pp. 535 (*sunt Commentarii in Ioannem…*), 538 (*Legimus in Actibus…*), 540 (*quando pendebat in cruce…*), 543 (*Glossa (B Nota)…*), 544 (*bet, non quod…*), 545 (*Ipse est qui in alio Evangelista…*), 546 (*bae offenderant animum…*), 548 (*signatus et porta…*), 551 (*here. Subinde…*), 552 (*attribuitur Hieronymo…*), 554 (*quod amor erga Deum…*), 556 (*pando exponit versum capituli sexti…*);
- left block opens unnumbered (page-crossing) on p. 550 only (*rium etc.: Emunitas, Hostiensi…*, the tail of p. 549 n. 10).
Every other block head, left and right, opens on a numeral (left `¹` on all 25 leaves; right on 536 ⁶, 537 ⁴, 539 ⁴, 541 ⁴, 542 ⁵,
547 ⁸, 549 ⁶, 550 ², 553 ⁷, 555 ⁵, 557 ⁵, 558 ⁵, 559 ⁴). p. 559's left block ends complete at n. 3 (*…Exod. 3, 7. seq.*) and its right
block at n. 6 (*…B quod alii.*), and p. 560's left block opens on `¹`, so **nothing leaves c4 across the leaf edge**, matching c4's
single-runover ledger line. Ledger CONFIRMED, 4 of 4 rows.

---

## Plate inventory (for PASS 4; nothing deleted)

`raw/vision/vol6/`: **32 files, 67 MB** (`du -sh`):
- `p-533.png` (278 KB), `p-534.png` (192 KB): the pilot's leaves before the work (small files);
- `p-535.png` … `p-559.png` (25 plates, the whole scope, ~1.7–2.4 MB each);
- `p-560.png` (2.0 MB): Capitulum V opens on it, so by the *Ioannem* gate precedent (`p-269.png` kept) it is the one to keep;
- `p-604.png`, `p-615.png`, `p-632.png`, `p-634.png` (~1.8–2.3 MB each): later leaves pulled at the pilot, belonging to later chunks.

`/tmp/colcrop/`: **92 MB** after this pass. vol6 bands present include pp. 427, 440, 467 (old), 535, 536, 544, 545, 548, 550, 554,
559, 560 (this pass added 545, 548, 550, 554, 559, 560), 615, 632. Scratch strips and parity scripts are in the session scratchpad only.
