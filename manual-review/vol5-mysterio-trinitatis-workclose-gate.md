# Vol V — *QD de mysterio Trinitatis* WORK-CLOSE GATE (printed pp. 45–115)

Run 2026-09-15, immediately after `bon-qmt-q8` landed (the work's last chunk). The second of this work's two
gates, per the frozen cadence: the shakedown at p. 68 (2026-09-06,
`manual-review/vol5-mysterio-trinitatis-shakedown-gate.md`, zero defects) and **this one, at the work close
(trigger 2, unconditional)**. Modelled on `manual-review/vol5-scientia-christi-workclose-gate.md`.

**Scope: fifteen chunks, `bon-qmt-q1-a1` … `bon-qmt-q8`, pp. 45–115 with no gap, 519 apparatus entries.**
The shakedown covered q1-a1 … q2-a2 (176 entries); **the eleven chunks q3-a1 … q8 (343 entries) are audited
against the register rulings here for the first time.**

| chunk | pages | entries | | chunk | pages | entries |
|---|---|---|---|---|---|---|
| `q1-a1` | 45–51 | 54 | | `q5-a1` | 87–92 | 35 |
| `q1-a2` | 51–58 | 53 | | `q5-a2` | 93–96 | 30 |
| `q2-a1` | 59–63 | 29 | | `q6-a1` | 96–102 | 44 |
| `q2-a2` | 63–68 | 40 | | `q6-a2` | 102–106 | 28 |
| `q3-a1` | 68–73 | 34 | | `q7-a1` | 106–109 | 28 |
| `q3-a2` | 73–78 | 35 | | `q7-a2` | 109–112 | 19 |
| `q4-a1` | 78–84 | 44 | | `q8` | 112–115 | 22 |
| `q4-a2` | 84–87 | 24 | | **total** | **71 pp.** | **519** |

**Result: ONE TEXT DEFECT, repaired (a *lumen* rendered "light" against ruling 2, unrecorded) · ONE RULING
RATIFIED (*vacatio* → "leisure", Wilson) · ONE TOOL DEFECT, repaired (`build-citations.py` tome inheritance —
eleven wrong resolutions corrected corpus-wide, zero regressions, QA 202 → 201) · one cosmetic normalisation.
Passes 1–3 clean. Pass 4 done; pushed and deployed (below).**

---

## ▶ DEFECT 1 (repaired) — `bon-qmt-q3-a1`: *proprio lumine rationis* → "the proper **light** of reason"

Found by the per-chunk *lux*/"light" and *lumen*/"lumen" count sweep below: `q3-a1`'s body has **zero** *lux*
and **one** *lumen* (the *Respondeo*'s *Fatetur igitur intellectus verus proprio **lumine** rationis*), against
**one** English "light" and **zero** "lumen". Ruling 2 (*lux* → light / *lumen* → "lumen", ratified at the
*scientia Christi* shakedown, with the single Ps. 35:10 exemption for a received scriptural wording) governs
body prose without exception, and **the chunk's own `## Notes` never mention *lumen***, so this is not a
disclosed departure but an unrecorded one — the class the *scientia Christi* shakedown named (register claims
that the text does not keep). ⚠ "light of reason" is the idiomatic English, which is exactly why it slipped:
**the rule's cost is highest where the English has a stock phrase.**

**Repair:** English → "by the proper **lumen** of reason"; a line added to `q3-a1`'s Translation choices
recording the repair and pointing here. No Latin touched.

## ✅ RULING — *vacatio* / *vacare* → "leisure" / "to keep leisure", against *quies* → "rest": RATIFIED (Wilson, 2026-09-15)

Open since `bon-praec-c4`, carried untested through the *decem praeceptis* and *scientia Christi* gates, ruled on
the *quies* side at `q5-a2`, and met at the one site where the families meet — `q7-a2` p. 111, *affectus noster
non **quiescit** nisi in summe amabili **vacando*** — where the site's own note (*D potius legi deberet vetando.
Fortasse originale habuit amabili et amativo…*) makes the word textually insecure. **Put to Wilson with that
caveat stated; Wilson ratified.** The rendering was already in the text, so **no text edit anywhere**; `q7-a2`'s
Notes and the repo `CLAUDE.md` register entry now record the ratification. **It is now the corpus rule.**

## ▶ DEFECT 2 (repaired) — `build-citations.py` lost the TOME of a bare `pag. N`, in two ways

The work's carried list named two resolver artefacts of one family. Both traced to `scan_page()`:

1. **The tome lookback stopped at `;`.** `q5-a2` p. 93 n. 2 reads *tom. I. pag. 118, nota 2; pag. 120, nota 7;
   tom. IV. pag. 102, nota 3; pag. 103, nota 10* — Quaracchi states each tome once and lists its pages after `;`.
   The lookback used `CLAUSE_SPLIT_RE`, which splits on `;`, so `pag. 120` fell into the citing volume (a false
   `forward` into Vol V) and `pag. 103` resolved to **`bon-qmt-q6-a2`** (tom. V p. 103) instead of tom. IV. The
   tool's own frozen rule 6 says *`;` separates loci of the SAME author and must not stop a chain lookback*; the
   lookback now uses `CHAIN_SPLIT_RE` (stops only at `—`, `Cfr.`, `Vide`).
2. **`tom` printed without its point was not read as a tome.** `bon-hex-c5` p. 355 n. 1 *tom IV. pag. 107,
   nota 5* resolved into this work's `q7-a1`. The pattern now accepts `\btom\.?\s+`.
3. ⭐ **And the first fix exposed a third, older bug.** After (1), `pag. 103` resolved to tom. **I**: `ROMAN_RE`'s
   first alternative `I{1,3}` takes the `I` of `IV` and the unanchored lookback accepts it. **This bug predates
   the gate and silently affected every bare page after `tom. IV.` or `tom. IX.` in the corpus.** Fixed with a
   numeral boundary `(?![IVX])`. ⛔ **A first fix that "mostly works" on its diff can be hiding the next bug —
   read every moved record, not the count.**

**The whole-ledger diff, every record read against its note** (before → after):

| citing | reference | before | after |
|---|---|---|---|
| `bon-qmt-q5-a2` p93-2 | `pag. 120, nota 7` (after `tom. I.`) | `tom5:p120` forward | `bon-sent-I-d5-dubia` |
| `bon-qmt-q5-a2` p93-2 | `pag. 103, nota 10` (after `tom. IV.`) | `bon-qmt-q6-a2` ✗ | `IV-d4-p1-a2-q2`+`q3` |
| `bon-hex-c5` p355-1 | `tom IV. pag. 107, nota 5` | `bon-qmt-q7-a1` ✗ | `IV-d4-p2-a1-q1` |
| `bon-brev-p6-c8` p273-4 | `pag. 593, nota 2` (after `tom. IV.`) | `I-d34-a1-q4` ✗ | `IV-d23-a1-q3` |
| `bon-red` p324-9 | `pag. 907, nota 9` (after `tom. IV.`) | **dangling** | `IV-d44-p1-a1-q1`+divisio |
| `III-d8-a1-q2` | `pag. 197, nota 3`; `pag. 373, nota 6` (after `tom. II.`) | Vol III ✗ ×2 | `II-d7-p2-a2-q1`; `II-d15-a1-q1` |
| `III-d9-a2-q4` | `pag. 638, nota 5`; `pag. 653, nota 6` (after `tom. II.`) | Vol III ✗ ×2 | `II-d26-a1-q3`; `II-d27` |
| `IV-d12-p1-a1-q3` | `pag. 197, nota 3`; `pag. 375, nota 6` (after `tom. II.`) | Vol IV ✗ ×2 | `II-d7-p2-a2-q1`; `II-d15-a1-q1` |

**Eleven records, all eleven now land in the tome their note names; zero records moved that should not have.**
Corpus QA **202 → 201** (`bon-red`'s dangling cleared). ⚠ Six of the eleven are in **deployed Vols III–IV** —
wrong backlinks that had been live, now corrected at the next deploy. **No file under `vol*/` was edited for
this; it is a tool fix and the ledger is derived.**

## Docketed, not fixed — resolver classes needing governance logic, not a pattern fix

- **Cross-note / cross-author anaphora — 6 sites in this work:** `q5-a2` p. 94 n. 8 (`ibid.` → *scientia
  Christi* as a work), `q6-a2` p. 103 n. 2 (`Magister loc. cit.` → `q5-a2`), `q7-a1` p. 107 nn. 1, 8, 10 (`ibid.`
  after an author's name carried to the last cross-reference), `q8` p. 114 n. 3 (`contra Faustum, loc. cit.` →
  I *Sent.* d. 19). The fix is author governance for `ibid.`/`loc. cit.` (an anaphor following an author siglum
  in the same clause is that author's, i.e. `excluded`), which touches the frozen inheritance rules 1–5 and
  every volume. **A scoped job with its own before/after diff, not a gate edit.** These display "via *ibid.*".
- **`q6-a1` p. 97 n. 12 `vide IV. d. 49. p. II. sect. 2. a. 4. q. 1.`** after a `II. Sent.` chain — dangling,
  though the target exists (a book numeral without `Sent.` not taken as a new book). The work's one dangling
  record.
- **`q6-a2` p. 103 n. 2 `S. Bonav. I. Sent. d. 7. dub. 4.`** filed `authority:Magister`.
- **`q6-a1` `p. J.`** (a wrong sort in a coordinate) resolves only to distinctio level — as printed, correctly.
- **Out of scope, noticed:** `bon-don-c8`'s `de Scientia Christi q. 4.` is emitted as `forward` to slug
  `bon-sci-q4` — the works table's slug for that abbreviation is wrong (`bon-qsc-`). One line in
  `scripture-books.json`; left for the resolver job.

## Other carried items — disposed

- **`q7-a1` p. 109 unidentifiable sort (*~~n~~ecessarium*)** — the chunk read it plain with pixel-map
  controls. **Upheld**: the as-printed rule needs a nameable sort; the reading is the only Latin word the
  strokes and the sentence admit.
- **`bon-itin-c5` p. 309 n. 2 `supra pag. 109, nota 5`** — `page-multi` (`q7-a1`+`q7-a2`); correct target is
  among the two. The resolution level is honest; no edit.

---

## The register rulings — verified mechanically across all fifteen chunks

| ruling | result |
|---|---|
| ***intellectus* → "understanding"** (narrow exception unreachable — *agens*/*possibilis* occur zero times) | **ZERO bare "intellect"** in 15 bodies + apparatus. ⚠ A first sweep reported 3 in `q1-a2`: all three are the adjective ***intellectualis* → "intellectual"** (*creatura intellectualis*), which the ruling does not govern. **Write the regex against the noun.** |
| **2. *lux* → light / *lumen* → "lumen"** | **HOLDS after Defect 1.** Per chunk, *lux*-family = English "light" and *lumen*-family = "lumen(s)" in every body; the two apparatus "light"s are *Lucem* (I Tim. 6:16) and *leve* (Matt. 11:30, "my burden light"). Ps. 4:7 keeps "lumen" at both sites (shakedown ruling). **Ps. 35:10 exemption UNREACHED** — p. 115 quotes *Apud te est fons vitae*. |
| **3. `contuit-`** | zero in the work — absent, not broken. |
| **5. `fundam. N` → *fundamentum/fundamenta N* (apparatus)** | **HOLDS at all 11 sites** (`q3-a2` ×2, `q4-a1`, `q4-a2` ×3 in one note, `q5-a2`, `q6-a1`, `q7-a1` *fundamenta 13 and 20*, `q8` ×2). No "foundation"/"ground" anywhere. ⚠ `q7-a1`'s *\*fundamenta\** is italic and dodged a first regex. |
| ***vacatio* → leisure / *quies* → rest** | RATIFIED (above). Stem census: *vaca-* only at `q7-a2` (*vacando*, *vacabimus*); the *quie-* family is otherwise verbs/adjectives (*quiescit*, *quietatur*, *quietativum*, *quietissimum*), with the one noun site `q5-a2` → "rest". |

## Pass 1 — `[?]` flag resolution: NOTHING IN SCOPE, verified

`check-live-flags.py`: **237 live occurrences corpus-wide, `bon-qmt-*` ZERO** — unchanged from the shakedown
baseline in every volume; vol5's ten are the known pre-existing ones in deployed chunks.

## Pass 2 — full-corpus style/formatting scan

`polish-style-scan.py` over **2,104 chunks: 11 issues / 6 chunks, ZERO in scope** — the identical list the last
four gates recorded (`bon-hex-c23` `[V5LABEL]`, deliberate; ten `[PAIR]` J4 class-B residue in Vols III–IV).

## Pass 3 — cross-chunk boundary integrity, all FOURTEEN interior boundaries

Re-derived from the built files (labels per printed page per chunk), not from the chunks' claims:

| # | boundary | page | split | | # | boundary | page | split |
|---|---|---|---|---|---|---|---|---|
| 1 | q1-a1 \| q1-a2 | 51 | 5/1 | | 8 | q4-a2 \| q5-a1 | 87 | 3/2 |
| 2 | q1-a2 \| q2-a1 | 58→59 | **LEAF EDGE** | | 9 | q5-a1 \| q5-a2 | 92→93 | **LEAF EDGE** |
| 3 | q2-a1 \| q2-a2 | 63 | 2/8 | | 10 | q5-a2 \| q6-a1 | 96 | 5/0 (body only) |
| 4 | q2-a2 \| q3-a1 | 68 | 1/4 | | 11 | q6-a1 \| q6-a2 | 102 | 3/1 |
| 5 | q3-a1 \| q3-a2 | 73 | 4/2 | | 12 | q6-a2 \| q7-a1 | 106 | 4/4 |
| 6 | q3-a2 \| q4-a1 | 78 | 4/0 (body only) | | 13 | q7-a1 \| q7-a2 | 109 | 6/1 |
| 7 | q4-a1 \| q4-a2 | 84 | 1/6 | | 14 | q7-a2 \| q8 | 112 | 3/2 |

**All fourteen match the frozen record digit for digit — 12 forwarding / 2 leaf edges, twelve shapes.**
**(a) Grammatical continuity:** every outgoing chunk's Latin ends on a complete sentence closing its last reply
(*…et ideo in his diutius non est morandum.* etc.) and every incoming chunk opens on its heading — no splice, no
stranded fragment. **(b) Footer accounting:** every printed page 45–115 is owned, each page's register is
contiguous 1..N across its owners, **519 entries in all**, agreeing with `KNOWN_TOTALS`; `check-vol5-apparatus.py`
reports no PENDING left in the work. **(c)** The work's end was fixed positively at `q8` from p. 117's heading.

## Supplementary sweeps

**Digit multiset, all 519 entries:** 7 mismatches, **0 defects** — six are titles spelled out in English
(*83 Qq.* → *Eighty-three Questions* ×5; *Quaest. 65 dialog.* → *Dialogue of Sixty-five Questions*), one an
ordinal (`3. arg.` → "the third argument"). Classified from scratch, not from a prior list.
**Cosmetic normalisation:** `q7-a1` p. 107 n. 11's "*Eighty-Three Questions*" → "Eighty-three", the Vol V form
(15:1). Not a defect; the corpus is mixed (Vol I 15:10), and only the vol5 outlier was touched.

**Citations:** the work carries **404 ledger records — 271 chunk, 79 verse, 20 page-multi, 18 work, 5 excluded,
4 chapter, 3 articulus, 3 distinctio, 1 dangling** (the docketed `q6-a1` site). **No forward reference into
pp. 45–115 remains anywhere in the corpus.** **36 inbound records from 22 already-deployed chunks** (Itinerarium,
Hexaemeron, *scientia Christi*, *septem donis*, Breviloquium, *de reductione*, *decem praeceptis*) resolve into
this work — **none live until deploy.** `build-index-json.py` was run after the ledger rebuild (the
*scientia Christi* deploy's lesson): **1,660 chunks cited, 10,027 backlinks.**

## Pass 4 — disk: ✅ DONE (Wilson's OK, 2026-09-15), ~222 MB reclaimed

`raw/vision/vol5/` — **50 plates, 161 MB** (pp. 68–117) — and `/tmp/colcrop/` — **34 crops, 61 MB**. Gitignored,
fully regenerable from the PDF via `extract-pages.py` + `colcrop.py`. Deletion held for Wilson's per-action OK,
as at the last two gates.

## Verification suite at the gate (all re-run after both repairs)

`check-vol5-apparatus.py` **152 chunks / 3,295 entries, all passed** · `check-vol5-census.py` **rosters agree
152/152, 223 runovers (199 gutter, 24 page)** · `check-live-flags.py` **237, `bon-qmt-*` ZERO** ·
`polish-style-scan` **11 / 6, ZERO in scope** · `build-content.mjs` **12 books, 2,103 / 2,103 translated** ·
`build-citations.py` **QA 201** (was 202; the one cleared is `bon-red`'s) · `build-index-json.py` run.

## The gate's own finding

**The one text defect is the ruling whose cost is highest where the English has a stock phrase.** Every other
*lumen* in the work sits in doctrinal pairs (*lumen inditum / infusum*) where the chunk that met it knew it was
exercising ruling 2; `q3-a1`'s single *lumen rationis* sat alone in a chunk with no *lux*, took the idiom, and
nothing recorded the choice. **The count sweep caught it; no chunk-level check could, because a chunk with one
site has nothing to compare against.** ▶ For the next work: a chunk with ZERO *lux* and ONE *lumen* is the
exposed shape — run the per-chunk count as part of the chunk, not only at the gate.

## ✅ PUSHED AND DEPLOYED 2026-09-15 (Wilson's go-ahead, each action separately)

`git push origin master` (`523dee5..96b18ff`). `vercel build --prod` exit 0, "Build completed successfully", no font
404s, output **574 MB**. `vercel deploy --prod --prebuilt --archive=tgz --scope wilson-pruitts-projects` → `dpl_ByF2aLV4VhPVbeXRbTGU6K35ymU7`
**READY**, aliased to bonaventure.wrootpress.com, first attempt (no `fetch failed`). **Verified by SERVED content:**
`/browse/9/d/8/q/bon-qmt-q8` 200 with *in beatissimam Trinitatem* / "most blessed Trinity." and *fundamentum 12*;
`q3-a1` serves "proper **lumen** of reason"; `q1-a1`'s Cited-by lists the deployed Itinerarium, Hexaemeron and *septem
donis* backlinks; `q7-a1` no longer lists `bon-hex-c5` (the tome-inheritance fix is live). ⚠ The corrected Vol III/IV →
Vol II links are in the shipped index but **not displayed** on `bon-sent-II-d7-p2-a2-q1`: that page has 38 inbound and
`cited-by.tsx` shows `MAX_SHOWN = 25`. Existing design, not a deploy fault. Pass 4 then deleted `raw/vision/vol5/*.png`
(50) and `/tmp/colcrop/*` (34). ⚠ Live-state claims are DATED and expire.
