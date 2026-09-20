# Vol VI — Capitulum I shakedown gate: EVIDENCE SHEET

Compiled 2026-09-20 by a read-only agent. **Nothing here is settled. Wilson rules off this sheet.**
No chunk under `vol6/` was edited; no commit, no push, no deploy, no stash.

**Live region = pp. 3–20, SEVEN chunks, roster derived from `ls vol6/` + frontmatter, not from the resume note:**

| chunk | division/section | printed_pages | apparatus entries |
|---|---|---|---|
| `bon-eccl-prooem` | 0 / 1 | 3–8 | 55 |
| `bon-eccl-prol` | 0 / 2 | 8–9 | 2 |
| `bon-eccl-c1-v1` | 1 / 1 | 9–10 | 11 |
| `bon-eccl-c1-v2-7` | 1 / 2 | 10–15 | 49 |
| `bon-eccl-c1-v8-11` | 1 / 3 | 15–17 | 17 |
| `bon-eccl-c1-v12-15` | 1 / 4 | 17–19 | 15 |
| `bon-eccl-c1-v16-18` | 1 / 5 | 19–20 | 7 |

⛔ **Every census below is taken over the BUILT files in `vol6/`, never over `raw/`, and over the
RENDERED regions only** (`## Latin`, `## English`, `## Apparatus`; `## Notes` and frontmatter
stripped, as `check-live-flags.py` strips them). A census that counts `## Notes` inflates every
stem in this sheet three- to fivefold, because the Notes *discuss* the very words being counted.

Reproduce the rendered extracts with:

```
python3 - <<'EOF'   # writes <stem>.{Latin,English,Apparatus,Notes,RENDERED}.txt
import sys, re, pathlib
src = pathlib.Path('vol6'); out = pathlib.Path('/tmp/r'); out.mkdir(exist_ok=True)
for f in sorted(src.glob('*.md')):
    txt = f.read_text()
    if txt.startswith('---'): txt = txt.split('---', 2)[2]
    secs, cur = {}, 'head'
    for line in txt.splitlines():
        m = re.match(r'^## (Latin|English|Apparatus|Notes)\s*$', line)
        if m: cur = m.group(1); secs.setdefault(cur, []); continue
        secs.setdefault(cur, []).append(line)
    for k in ('Latin','English','Apparatus','Notes'):
        (out/f'{f.stem}.{k}.txt').write_text('\n'.join(secs.get(k, [])))
    (out/f'{f.stem}.RENDERED.txt').write_text('\n'.join(
        secs.get('Latin',[]) + secs.get('English',[]) + secs.get('Apparatus',[])))
EOF
```

---

## ▶ STRUCTURAL VERIFICATION (derived from the files, not from the resume note)

**Spans, from `printed_pages` in frontmatter — all five Cap. I pericopes match the frozen record
digit for digit:** v1 = 9–10 · v2-7 = 10–15 · v8-11 = 15–17 · v12-15 = 17–19 · v16-18 = 19–20.
Prooemium chunks: prooem 3–8, prol 8–9 (ruling 2 as frozen).

**pp. 3–20 are contiguous** (union of all `printed_pages` = `range(3, 21)` exactly).

**Every page owned, register contiguous 1..N on all eighteen leaves**, derived by parsing every
`[^pN-n]: **La.**` definition and bucketing by page. Six leaves are shared and the split is exactly
as each chunk's Notes record it:

| page | entries | split | 1..N |
|---|---|---|---|
| 3–8 | 7 · 11 · 9 · 12 · 8 · 8 | prooem alone (p. 8 = prooem alone; `prol` inherits none) | OK |
| 9 | 6 | prol 2 / c1-v1 4 | OK |
| 10 | 10 | c1-v1 7 / c1-v2-7 3 | OK |
| 11–14 | 13 · 10 · 10 · 9 | c1-v2-7 alone | OK |
| 15 | 6 | c1-v2-7 4 / c1-v8-11 2 | OK |
| 16 | 7 | c1-v8-11 alone | OK |
| 17 | 11 | c1-v8-11 8 / c1-v12-15 3 | OK |
| 18 | 9 | c1-v12-15 alone | OK |
| 19 | 9 | c1-v12-15 3 / c1-v16-18 6 | OK |
| 20 | 1 written (+ `PENDING n.2–8`) | c1-v16-18 | OK |

`KNOWN_TOTALS_VOL6` (7·11·9·12·8·8·6·10·13·10·10·9·6·7·11·9·9·8) matches the measured totals on
all eighteen pages. **No discrepancy anywhere in the structural record.**

---

## ▶ THE SUITE, WITH DENOMINATORS (a verdict is worthless until you read what it counted)

| tool | what it COUNTED | verdict |
|---|---|---|
| `python3.11 tools/check-vol5-apparatus.py --volume=vol6` | **7 chunks, 156 entries, 18 known page totals**; La/En label pairing per chunk (11·15·7·49·17·2·55, each La = En); footer ownership on pp. 3–20 | **All checks passed.** p. 20 trailing `PENDING n.2,3,4,5,6,7,8` (Cap. II's, correctly unwritten) |
| `python3.11 tools/check-vol5-census.py` | **vol5 167/167 · vol6 7/7** chunks on disk vs ledger; vol6 **12 runovers across 7 chunks (11 gutter, 1 page: p. 16 n. 7); 6 chunks positive, 1 negative** | **Rosters agree** |
| `python3.11 tools/polish-style-scan.py` | **2,126 chunks scanned, all six volume dirs in scope** (vol1–vol6) | 11 issues / 6 chunks — 10 PAIR (Vol III/IV Sentences), 1 V5LABEL (`bon-hex-c23`). **ZERO in vol6** |
| `python3.11 tools/check-live-flags.py vol6` (bare positional) | **7 chunks in vol6** — confirms it scanned the volume, not zero | **no live `[?]` flags** |
| `python3.11 tools/build-citations.py` | **2,126 chunks → 23,956 ledger records** (scripture 11,200 · crossref 11,592 · authority 1,164 excluded); vol6 = **211 records** across 6 chunks (`bon-eccl-prol` contributes none) | **corpus QA 206** — see item 3; **none is ours** |
| `cd site && node scripts/build-content.mjs` | **15 books, 2,125 questions** | 2,125 translated |

⚠ `build-citations` scripture confidence corpus-wide: A = 8,131 (73 %) · B = 2,284 (20 %) · C = 774 (7 %).
Crossref resolution: chunk 73 % · page-multi 11 % · dangling 2 % · unresolvable 2 % · ambiguous 1 %.
Anaphora: 2,033 within-chunk + 89 cross-chunk resolved, **180 unresolved** (corpus-wide).

---

# (1) THE ITALIC CONVENTION

### Counts by leaf, over the built Latin, live region

Derived two ways. (i) The per-chunk counts each builder recorded on the plate, re-read out of the
chunks' own `## Notes` — **these are the authoritative figures** where they exist. (ii) An
independent mechanical re-count over the built `## Latin` of opening guillemets (`«`) per page and
of colon-introduced italic runs, page-bucketed on the `<!-- page N -->` markers.

⚠ **(ii) is a FLOOR, not an exact count**, and must be read as one: it requires a recognised
scripture cue immediately before the colon, so it misses a quotation introduced by *unde*, by a
bare *ibi*, or by a continuation, and its raw `«` tally double-counts p. 13's nested guillemets.
Where (i) and (ii) differ, (i) governs. **(ii) agrees with (i) on every leaf a builder counted**
(p. 15 = 7, p. 16 = 4, p. 17 Quaestiones = 3 italic + 1 roman control, p. 18 = 17, p. 19 = 9,
p. 20 = 2 + 1 control), which is why it can be trusted on **p. 9 and p. 10, the two leaves no
builder counted.** (ii) is:

```
python3 -c "
import re,pathlib
for f in sorted(pathlib.Path('/tmp/r').glob('*.Latin.txt')):
    t=f.read_text(); parts=re.split(r'<!-- page (\d+) -->', t)
    for i in range(1,len(parts),2):
        pg,seg=int(parts[i]),parts[i+1]
        print(f.name.split('.')[0], pg, seg.count(chr(171)),
              len(re.findall(r':\s*\*[^*]{15,}\*', seg)))"
```

| leaf | region | roman in guillemets | italic unguillemeted | chunk |
|---|---|---|---|---|
| 3, 4, 5, 6, 8 | **Prooemium** (outside the inversion) | 0 | **33** | prooem |
| 8, 9 | Prologus + Expositio prologi | **POSITIVE ZERO — no scriptural quotation exists** | 0 | prol |
| **9** | **expositio** | **3** (floor; no builder counted this leaf) | 0 | **c1-v1** |
| **10** | expositio | 0 (c1-v1's portion) / ≥1 (c1-v2-7's) | 0 | c1-v1 / c1-v2-7 |
| **11** | **expositio** | **2 (both Hugh, non-scriptural)** | **10 (see extent below)** | c1-v2-7 |
| 12 | expositio | ≥11 | 0 | c1-v2-7 |
| 13 | expositio | ≥17 (raw `«` = 24; p. 13 nests three quotations inside Hugh's) | 0 | c1-v2-7 |
| 14–15 | **Quaestiones** | 0 | **6** | c1-v2-7 |
| 15 | expositio | 7 | 0 | c1-v8-11 |
| 16 | expositio | 4 | 0 | c1-v8-11 |
| 16 | Quaestiones | positive zero | positive zero | c1-v8-11 |
| 17 | **Quaestiones** | 1 (Hugh, non-scriptural) | **3** | c1-v8-11 |
| 17 | expositio | positive zero | positive zero | c1-v12-15 |
| 18 | expositio | **17** | 0 | c1-v12-15 |
| 18, 19 | Quaestiones | positive zero (**2 non-scriptural roman controls**) | positive zero | c1-v12-15 |
| 19 | expositio | 9 | 0 | c1-v16-18 |
| 20 | expositio | 2 (+1 Hugh control) | 0 | c1-v16-18 |

**Totals over the live region, on the builders' plate counts where they exist and the floor
elsewhere: expositio ≥ 72 roman / 10 italic (all ten on p. 11); Quaestiones 0 roman / 9 italic,
plus 3 non-scriptural roman-in-guillemets controls.** The exact expositio figure depends on
`c1-v2-7`'s pp. 10/12/13, which its Notes give as "« Avis nascitur… » … **and ~25 more**" rather
than as a number — **the one leaf-group in the live region with no hard count.**

⚠ **CONTRADICTS the resume note's docket, item (1), in two ways.**

- **`c1-v1` is omitted from the expositio side entirely.** p. 9 carries **three**
  roman-in-guillemets expositio quotations (the first in the volume; the Notes quote one,
  `« Quomodo si nascatur spina… »`). The note lists pp. 8–9 as "POSITIVE ZERO … not evidence
  either way (`prol`)" — true of `prol`'s upper ~31 % of the leaf, **false of the leaf**, whose
  lower two-thirds is `c1-v1`'s expositio and is positive. **Five chunks have measured the
  inversion, not four.**
- **The note's own arithmetic is soft.** "~58 + 11 ≈ 69" carries a tilde and an approximately-equal
  sign through three successive hand-offs; ⭐ **nobody has ever counted pp. 10/12/13 exactly.**
  The mechanical floor for those three leaves is 29; the Notes' prose implies ~32.

### p. 11's exception — exact extent

**Ten italic unguillemeted runs in the running expositio**, against **two roman-in-guillemets
non-scriptural quotations on the same leaf** (Hugh of St Victor ×2). So a same-leaf control DOES
exist on p. 11, and it behaves exactly as the expositio rule predicts for non-Scripture.

The ten, read out of the built Latin in printed order:

1. Ier. 10:15 *…in tempore visitationis suae peribunt*
2. Rom. 8:20 `[^p11-2]`: *Vanitati subiecta est creatura non volens*
3. **Eccl. 3:19–20** (*et infra tertio*): *Cuncta subiacent vanitati, et omnia pergunt ad locum unum*
4. Ps. 38:6 `[^p11-4]`: *Universa vanitas omnis homo vivens*
5. Ps. 143:4: *Homo vanitati similis factus est, dies eius sicut umbra praetereunt*
6. Ps. 93:11: *…cogitationes hominum, quoniam vanae sunt*
7. Iob 14:1: *Homo natus de muliere, brevi vivens tempore, repletur multis miseriis*
8. Ioan. 21:24 `[^p11-5]`: *Hic est discipulus ille, qui testimonium perhibet de his*
9. Num. 24:4 `[^p11-6]`: *Dixit auditor sermonum Dei*
10. **counted as ten only if item 3 counts** — nine of the ten are third-party Scripture; the tenth
    (**Eccl. 3:19–20**) is the commented book quoting itself.

⚠ **A count discrepancy inside the corpus's own record:** `c1-v2-7`'s Notes say "**ten** scriptural
quotations" and then enumerate **nine** references. The tenth is recoverable — it is the
*infra tertio* self-quotation — but the sentence as written does not name ten things.

⛔ **A candidate discriminator suggested by that breakdown is DEAD, measured, not theorised.**
"Italic marks a self-quotation of Ecclesiastes" fails on p. 16: `c1-v8-11` prints
*…propter tempus, quod inducit oblivionem; infra secundo:* « Futura tempora oblivione cuncta
operient » — **a self-quotation of Ecclesiastes, roman, in guillemets, in the expositio.** Command:

```
grep -n "infra secundo" /tmp/r/bon-eccl-c1-v8-11.Latin.txt
```

**Five builders have failed to find a discriminator; this sheet does not propose one either.** The
above is offered only to close off the one hypothesis the count breakdown might otherwise suggest.

### Decisive sentence — Quaracchi states the rule in its own words (p. 9 n. 4, `c1-v1`)

**La.** *Observamus, quod in expositione textus non potuimus retinere solitum morem, verba
Scripturae litteris italicis exprimendi; alioquin expositio non bene distingueretur a textu.*

**En.** "We observe that in the exposition of the text we could not keep our usual practice of
setting the words of Scripture in italic letters; otherwise the exposition would not be well
distinguished from the text."

▶ The note's own scope is *in expositione textus*, and that scope is exactly where the measured
inversion holds and exactly where it stops. **p. 11 stands inside the scope and breaks it.**

### Alternatives and cost

| option | cost | mechanical or per-site |
|---|---|---|
| **A. Leave p. 11 as printed, record the exception** (status quo — nothing written) | **0 Latin lines, 0 English lines.** One paragraph already stands in `c1-v2-7`'s Notes | n/a |
| **B. Normalise p. 11 to roman-in-guillemets** to match the other 70 sites | **10 Latin runs + 10 English runs on one leaf** (`c1-v2-7`, p. 11 region only) | **PER-SITE** — each run must be re-read on the plate to fix its extent before the guillemets go on; italic markers are not co-extensive with quotation boundaries |
| **C. Note the leaf** with a `tr-`-style editorial note | 1 added def + 1 anchor in `c1-v2-7`; 0 text lines change | MECHANICAL |
| **D. Defer to the p. 103 work-close gate**, when eleven more capitula have been measured | 0 now; the sample grows by ~80 leaves | n/a |

**Type: DECISIVE-SENTENCE question, not a count question.** p. 9 n. 4 is the sentence that chains
the whole distinction, and no count of roman sites — 70 or 700 — can settle whether p. 11 is a
compositor's lapse or an unstated sub-rule. ⛔ Option B is the only one that alters printed text and
it is the one the transcription standard forbids without a discriminator (Quaracchi is never
silently emended).

---

# (2) *magister* · *doctor* · *doctrina*

### *magister* — counts by chunk, over the rendered regions

```
grep -oinE "magistr[a-z]*|magister" /tmp/r/*.Latin.txt /tmp/r/*.Apparatus.txt
```
⚠ Do NOT use `magist?r?[a-z]*` — it false-positives on *magis* (`c1-v8-11` p. 15).

| chunk | site | Latin | English | class |
|---|---|---|---|---|
| `c1-v1` | p. 10 n. 1 apparatus (Jerome) | *aequalis **magister** est* | "the **teacher** is an equal" | the ruling |
| `c1-v8-11` | p. 15 body (II Tim. 4:3) | *coacervabunt sibi **magistros*** | "heap to themselves **teachers**" | the ruling (Douay agrees, nil cost) |
| `c1-v12-15` | p. 19 n. 1 apparatus (Lombard) | *His verbis complectitur **Magister** in II. Sent.* | "In these words the **Master**, in II *Sentences*" | the named exception |

**n = 3. Two of the ruling, one of its named exception.** No site is ambiguous; the exception is
identified by its own object (`in II. Sent. d. XXXVI. c. 1`), not by inference.

### *doctor* — ⚠ CONTRADICTS the resume note

The note says *doctor* is "**ZERO** in every Vol VI chunk". Measured over the rendered regions:
**n = 1.**

```
grep -inE "\bdoctor[a-z]*\b" /tmp/r/*.Latin.txt /tmp/r/*.English.txt /tmp/r/*.Apparatus.txt
```

`bon-eccl-prooem` p. 5 n. 6: *ubi Vulgata post* vaniloquium *addit* **volentes esse legis doctores**.
It is a Vulgate variant reading quoted as Latin, and the En. half **repeats it untranslated**, so
*doctor* has still never been rendered into English in this volume and the two words have still
never met in the translation. **The zero is true of the English, false of the Latin.** That
distinction matters: a later chunk that meets *doctor* in Bonaventure's own prose will be told
by the docket that it is the first, and it will be the second.

### *doctrina* — ⚠⚠ THE LARGEST CONTRADICTION ON THE SHEET

The note discloses *doctrina* → "learning" as **NEW, 3 sites**. Measured over the rendered regions,
*doctrina* occurs **NINE times in FIVE chunks and takes THREE different English words.**

```
python3 -c "
import re,pathlib
for f in sorted(pathlib.Path('/tmp/r').glob('*.Latin.txt')):
    for m in re.finditer(r'doctrin[a-z]*', f.read_text()): print(f.name, m.group(0))"
```

| chunk | leaf | Latin | English | n |
|---|---|---|---|---|
| `prooem` | 6, 7 | *scientia et **doctrina*** (×4, the *scientia/doctrina* pair of Quaestio II) | "**doctrine**" | 4 |
| `prooem` | 5 n. 6 apparatus | — | "**doctrine**" (mirrors the body) | 1 |
| `c1-v1` | 9 | *omnibus **doctrinam** parabolarum tradidit* | "the **teaching** of parables" | 1 |
| `c1-v8-11` | 16–17 | *duplex est cognitio: per inventionem et **doctrinam*** | "by finding out and by **teaching**" | 1 |
| `c1-v16-18` | 19 | *atque **doctrinam*** · *contra **doctrinam*** · ***doctrinam** magis quam aurum* | "**learning**" (×3) | 3 |

⚠ One English "doctrine" in `c1-v1` is a **false positive** for this census — its Latin is
*de utilitate **sententiae** huius libri*, not *doctrina*. Counted out above.

▶ So the item is not "ratify a new choice at 3 sites". It is: **one Latin noun currently takes
"doctrine" (4), "teaching" (2) and "learning" (3) inside eighteen printed pages**, and the three
renderings were chosen by three different builders who did not know of each other's sites.

### Decisive sentence — Prov. 8:10, `c1-v16-18` p. 19, the site the note names

**La.** *…haec utile est scire, quando modo debito inquiruntur; unde Proverbiorum octavo*[^p19-6]:
« Accipite disciplinam et non pecuniam; **doctrinam** magis quam aurum eligite ».

**En.** "…these things are useful to know, when they are inquired into in the due manner; whence
Proverbs, the eighth chapter[^p19-6]: « Receive instruction and not money; choose **learning**
rather than gold »."

▶ The Douay's "knowledge" was released because *scientia* is "knowledge" four lines later, at the
chunk's close: *Qui addit **scientiam** addit et dolorem* → "he that **addeth knowledge** addeth
also labour" (verified, both halves present in `c1-v16-18`). **That reasoning is sound and local —
and it is the identical reasoning that would force "doctrine" at `prooem` pp. 6–7, where the pair
is literally *scientia et doctrina* in one clause.** The two solutions to the same collision differ.

### Alternatives and cost

| option | cost | mechanical or per-site |
|---|---|---|
| **A. One English word for *doctrina* throughout ("doctrine")** | **5 English lines** — 3 in `c1-v16-18` p. 19, 1 in `c1-v1` p. 9, 1 in `c1-v8-11` pp. 16–17. Latin unchanged | **PER-SITE** — "choose doctrine rather than gold" and "by finding out and by doctrine" both read badly; each needs a reader |
| **B. One English word ("learning")** | **5 English lines** — 4 in `prooem` (incl. 1 apparatus), 1 `c1-v1`, 1 `c1-v8-11`; but *scientia et doctrina* → "science and learning" loses the received term-of-art pair | **PER-SITE** |
| **C. CONTEXTUAL under the dikaisune rule**, as *vacatio* was ruled 2026-09-15: "doctrine" for the *scientia/doctrina* term-of-art pair, "teaching" for the act, "learning" for the object learned — **with a `tr-doctrina` note at first occurrence** | **0 text lines change**; 1 added def + 1 English anchor in `prooem` | **MECHANICAL** |
| **D. Ratify the three as they stand, no note** | 0 lines | n/a — but the split then becomes invisible at the work-close gate |

**Type: *magister* is a COUNT question, decided at n = 3 (2 + 1 exception) — the same shape as
*dominium* at n = 2. *doctrina* is a DECISIVE-SENTENCE question**, and the decisive sentence is
`prooem`'s *de tali potest esse scientia et **doctrina*** ("of such a thing there can be science and
doctrine"), because that one clause is what makes "learning" unavailable at four sites and
therefore what makes a single English word impossible.

---

# (3) RESOLVER ARTEFACTS — all five CONFIRMED LIVE

Re-derived by running `python3.11 tools/build-citations.py` (2,126 chunks → 23,956 records) and
reading `index/citations.tsv`. **Chunks were not edited.** ⚠ These belong to the separate resolver
docket, which Wilson has not scheduled. Nothing below is a proposed fix.

**Vol VI ledger denominator: 211 records across 6 chunks** (`bon-eccl-prol` contributes none — it is
listed in the QA report's "chunks contributing no citation record", correctly: its two entries are
a Vallarsi edition note and a codex note, neither citable).

| # | artefact | actual `index/citations.tsv` line | live? |
|---|---|---|---|
| 1 | `c1-v1` p. 10 n. 5, `supra pag. 8, nota 5` → `page-multi` though `p8-5` is unique | `bon-eccl-c1-v1  6  apparatus:p10-5  p10-5  crossref  page  supra pag. 8, nota 5  bon-eccl-prol+bon-eccl-prooem   page-multi` | **YES** |
| 2a | **cross-note anaphora**, `c1-v2-7` p. 11 n. 13 `ibid. v. 5. et 6.` | `bon-eccl-c1-v2-7  6  apparatus:p11-13  p11-13  crossref  anaphor->page  ibid.  bon-eccl-prooem   chunk  yes  supra pag. 5, nota 7` | **YES** — antecedent taken from the PRECEDING note (`supra pag. 5, nota 7`); the note's own `Cap. 1, 8` stands one clause earlier in the same entry |
| 2b | **cross-note anaphora**, `c1-v16-18` p. 19 n. 5 `ibid. 31, 1.` | `bon-eccl-c1-v16-18  6  apparatus:p19-5  p19-5  scripture  anaphor->apparatus-explicit  ibid.  Eccli 47:15  A  verse  yes  Eccli. 47, 15` | **YES — and it is filed confidence A on a wrong target.** The true referent is Prov. 31:1 |
| 3 | `c1-v8-11` p. 17 n. 5, a named FOREIGN edition's tome read as Quaracchi's | `bon-eccl-c1-v8-11  6  apparatus:p17-5  p17-5  crossref  page  tom. III. pag. 39  bon-sent-III-d2-a1-q1+bon-sent-III-d2-a1-q2   page-multi` | **YES** — source reads `Cfr. Plato, Timaeus (ed. Serrani tom. III. pag. 39)`; ⚠ the string "Serrani" **never reaches the ledger** (`grep -i serran index/citations.tsv` = 0 hits), so the parser drops the one token that would disambiguate it |
| 4 | `c1-v12-15` p. 19 n. 3, that class's MIRROR — a bare tome-and-page that really IS ours | `bon-eccl-c1-v12-15  6  apparatus:p19-3  p19-3  crossref  page  tom. II. pag. 655, nota 3  bon-sent-II-d27-a1-q1   chunk` | **YES**, and **correctly resolved** — which is why #3 cannot be fixed by suppressing bare tome-and-page |
| 5 | lemma shorthand `Cap. N, M`, invisible to the index **by accident** | `grep -cE "Cap\. [0-9]+, *[0-9]+" over vol6 records = **0**` against **28 occurrences** of the form in `vol6/*.md` (13 distinct `Cap. N, M` addresses across 5 chunks) | **YES** |

**Corpus QA flags: 206.** `grep -c bon-eccl manual-review/citation-qa-report.md` = **1**, and that
one line is `bon-eccl-prol` under "Chunks contributing no citation record".
⭐ **NONE of the 206 is ours.** (The 206 is the Vol V unmasking that followed `VOLUME_COMPLETE[5]`
going True — five Vol V danglers became visible; that is verified as unchanged, not as a
regression, and no inbound line moved.)

### Decisive line — artefact 2b, the one that is wrong rather than merely coarse

Source, `c1-v16-18` p. 19 n. 5 (`vol6/bon-eccl-c1-v16-18.md`), **La.**: the entry names
`Eccli. 47, 15` earlier in its own text and then writes `ibid. 31, 1.` The resolver reaches back to
the **previous note** for `ibid.`, not to the antecedent standing **inside** the same note.

**The missing rule is the same in 2a and 2b: an apparatus note's `ibid.` takes its antecedent from
WITHIN the note, never from the preceding note.** ⛔ Not this gate's to write.

### Alternatives and cost

| option | cost |
|---|---|
| **A. Record, schedule nothing** (status quo) | 0 |
| **B. Schedule the resolver docket** as its own job with a before/after ledger diff | 5 Vol VI artefacts + the Vol V carry-overs; touches `tools/build-citations.py` only, **zero chunk lines**; needs a full 23,956-record diff to prove no collateral movement |
| **C. Fix only 2a/2b** (the best-attested and the only wrong one) | one rule in the anaphora resolver; **MECHANICAL** — but it moves every `anaphor->` record in the corpus (2,033 within-chunk + 89 cross-chunk), so the diff is not small even though the change is |

**Type: COUNT question for the docket as a whole** (five confirmed, none ours, none blocking);
**2b alone is a correctness question**, because it is the only one filed confidence A on a wrong
target — the others are coarse, not false.

⛔ **NOT an artefact** (verified, so it is not re-raised): the body ordinal *tertii Regum quarto* →
`Reg* 4:30` is the settled corpus-wide treatment (48 `Reg*` records against 1–4Reg 34/29/40/35).

---

# (4) HEADING CLASSES

### Every heading in the live region, with class and markdown level

```
grep -nE "^#{2,6} " vol6/*.md   # then bucket on <!-- page N --> markers
```

**21 headings, live region, `## Latin`:**

| leaf | heading | typographic class | md |
|---|---|---|---|
| 3 | `Prooemium commentarii in Ecclesiasten.` | 1 — letter-spaced small capitals | `###` |
| 3 | `Introductio generalis.` | 1 | `####` |
| 5 | `De quadruplici causa huius libri.` | 1 | `####` |
| 6 | `Quaestio I. *De fine libri Ecclesiastes.*` | 2 — roman-and-italic centred label | `###` |
| 6 | `Quaestio II. *De materia eiusdem.*` | 2 | `###` |
| 7 | `Quaestio III. *De modo agendi in eodem.*` | 2 | `###` |
| 8 | `Quaestio IV. *De causa efficiente eiusdem.*` | 2 | `###` |
| 8 | `Prologus commentarii S. Hieronymi in Ecclesiasten.` | 1 | `###` |
| 9 | `Expositio huius prologi.` | 1 | `###` |
| 9 | `Commentarius in librum Ecclesiastes.` | **display, full measure** | `###` |
| 9 | `Capitulum I.` | 1 | `###` |
| 9 | `De titulo.` | 1 | `####` |
| 9 | `Quaestiones.` | 1 | `###` |
| 10 | `Sequitur huius libri tractatus.` | **1** | **`###`** |
| 10 | `Propositio rei probandae.` | **1** | **`####`** |
| 11 | `Divisio totius probationis.` | 1 | `####` |
| 11 | `Pars I. Probatur vanitas *mutabilitatis* quoad duo.` | 2 | `####` |
| 11 | `*Partis primae membrum I.*` | 2 | `####` |
| 11 | `Art. 1. *Probatur mutabilitas…*` | 2 | `####` |
| 12 | `Probatur vanitas mutabilitatis secundum esse rerum…` | 3 — letter-spaced roman u&lc sentence-form | `####` |
| 14 | `Quaestiones.` | 1 | `###` |
| 15 | `Secundo consideratur vanitas mutabilitatis rerum…` | 3 | `####` |
| 16 | `Quaestiones.` | 1 | `###` |
| 17 | `Art. 2. *Ex consideratione duplicis vanitatis…*` | 2 | `####` |
| 17 | `Primo manifestat suam curiositatem…` | 3 | `####` |
| 17 | `Describitur curiositas philosophiae, primo quidem…` | 3 | `####` |
| 18 | `Quaestiones.` | 1 | `###` |
| 19 | `Describitur curiositas philosophiae secundo…` | 3 | `####` |

### Measured cap-heights (original pixels, all read at ≥1.7×; ⚠ never bound-box a `Q`)

| heading | leaf | md | cap-height |
|---|---|---|---|
| `COMMENTARIUS` | 9 | `###` | **41** |
| `IN LIBRUM ECCLESIASTES.` | 9 | `###` | **51** |
| `PROLOGUS COMMENTARII S. HIERONYMI` | 8 | `###` | 26 |
| `CAPITULUM I.` | 9 | `###` | **26** |
| `DE TITULO.` | 9 | `####` | **25** |
| `EXPOSITIO HUIUS PROLOGI.` | 9 | `###` | **25** |
| `SEQUITUR HUIUS LIBRI TRACTATUS.` | 10 | **`###`** | **27** |
| `PROPOSITIO REI PROBANDAE.` | 10 | **`####`** | **27** |
| `Secundo consideratur vanitas…` | 15 | `####` | **28** |
| `QUAESTIONES.` | 16 | `###` | **26** (Q bowl; 32 with tail) |
| `Art. 2.` | 17 | `####` | **25** |
| `Primo manifestat…` | 17 | `####` | **28** |
| `Describitur curiositas… rerum naturalium` | 17 | `####` | **21** |
| `QUAESTIONES.` | 18 | `###` | **26** (Q bowl; 34 with tail) |
| `Describitur curiositas… moralium` | 19 | `####` | **21** |

**The size test has inverted four times, and the record is unambiguous.** (i) p. 9: `EXPOSITIO
HUIUS PROLOGI.` 25 at `###` beside `DE TITULO.` 25 at `####` — identical, different levels.
(ii) p. 10: `SEQUITUR` 27 at `###` and `PROPOSITIO` 27 at `####` — identical, different levels,
**and they are the same typographic class (class 1, small capitals) on the same leaf.**
(iii) `c1-v8-11`: `####` 28 vs `###` 26. (iv) `c1-v12-15`: `####` 28 vs `###` 26.
**The `####` divisio heading is TALLER than the `###` unit heading at every leaf where both stand.**

⚠ **CONTRADICTS the resume note's docket, item (4)**, on a detail that matters for the framing.
The note says "**All three classes are flattened to `####`**". Measured: **class 1 (small capitals)
takes BOTH levels** — `###` for `Sequitur huius libri tractatus.`, `Prologus…`, `Expositio huius
prologi.`, `Capitulum I.`, `Quaestiones.`, and `####` for `Introductio generalis.`, `De quadruplici
causa…`, `De titulo.`, `Propositio rei probandae.`, `Divisio totius probationis.` Class 2 likewise
takes both (`Quaestio I–IV` at `###`, `Pars I.`/`Art. 1.`/`Art. 2.` at `####`). Only **class 3 is
uniformly `####`** — and class 3 itself carries two sizes (28 and 21 px, both on p. 17).

▶ So the real state is not a flattening of three classes onto one level. It is: **level tracks
FUNCTION (ruling 4) and is uncorrelated with both class and size** — which is what ruling 4 says it
should do, and which is why four size-based challenges have each inverted.

### Decisive evidence — the p. 10 pair

`SEQUITUR HUIUS LIBRI TRACTATUS.` (27 px, `###`) and `PROPOSITIO REI PROBANDAE.` (27 px, `####`)
**stand on one leaf, in one column, in one typographic class, at one size, three lines apart, and
take different markdown levels.** No typographic measurement can separate them; only function can.

### The actual question: is flattening right for a five-deep nest?

The nest the live region exercises, deepest branch, `c1-v12-15`:
`Capitulum I` → `Art. 2.` → `Primo manifestat…` → `Describitur curiositas…` → `(Vers. 12.)` — with
`Quaestiones` hanging beside it. **Levels 2–5 of that nest all render `####`.**

| option | cost | mechanical or per-site |
|---|---|---|
| **A. Keep the flattening** (status quo) | 0 | n/a |
| **B. Deepen to `#####`/`######` by nest depth** | **~14 heading lines in 5 chunks, Latin AND English = ~28 lines**; requires a depth model that does not yet exist and that `build-content.mjs` has never been asked to render | **PER-SITE** — depth is a reading of Quaracchi's nest at each heading, not a property of the string |
| **C. Split by CLASS** (`###` class 1+2, `####` class 3) | ~10 heading lines ×2 languages; ⛔ **contradicted by the p. 10 pair above** | MECHANICAL but demonstrably wrong |
| **D. Defer to the p. 103 work-close gate**, when 12 capitula have been seen and the deepest nest is known | 0 now | n/a |

**Type: DECISIVE-SENTENCE question** (here, decisive *pair*): the p. 10 pair settles that size and
class cannot decide it, so the question is a design question about the reader, not a count.
n = 21 headings adds nothing further.

---

# (5) REGISTER SITES FOR RATIFICATION

Counts over the rendered regions. Command pattern:
`python3 -c "import re,pathlib; [print(f.name, m.group(0)) for f in sorted(pathlib.Path('/tmp/r').glob('*.RENDERED.txt')) for m in re.finditer(r'<STEM>', f.read_text())]"`

| word | stem searched | sites | chunks | rendering | type |
|---|---|---|---|---|---|
| *dignitates* | `dignitat[a-z]*` | **1** | `c1-v8-11` p. 16 | "**axioms**" | COUNT, n = 1 |
| *iucunditas* | `iucundit[a-z]*` | **2** | `c1-v8-11` p. 16, p. 17 | "**pleasantness**" ×2 | COUNT, n = 2 |
| *doctrina* | `doctrin[a-z]*` | **9** | 5 chunks | **split 3 ways** — see item (2) | DECISIVE-SENTENCE |
| *vaca-* | `vaca[a-z]*` | **2** | `c1-v8-11` p. 16 body; `c1-v12-15` p. 18 n. 1 **apparatus** | both "**free for**" | see below |

⚠ *delectabilium* → "delightful" (`c1-v16-18` p. 19) is a **different Latin word** and is not an
*iucunditas* site. Excluded by inspection.

### *dignitates* — decisive sentence

**La.** *…quia sensus non fallitur circa proprium obiectum — et principiorum intelligibilium, sicut
**dignitatum***[^p16-4]*; et talia facile est cognoscere.*
**En.** "…because sense is not deceived about its proper object — and of intelligible principles,
such as the **axioms**; and such things it is easy to know."
▶ *dignitates* as the Euclidean/Boethian "axioms", the Itinerarium precedent, at its only site.

### *iucunditas* — decisive sentence (Hugh, p. 17)

**La.** *Unde Hugo*[^p17-1]: « *Omnis pulcritudo, omnis **iucunditas**, omnis suavitas rerum
conditarum afficere cor humanum potest, satiare non potest…* »
**En.** "Whence Hugh: « All the beauty, all the **pleasantness**, all the sweetness of created
things can affect the human heart, but cannot fill it… »"
▶ The three-term *pulcritudo / iucunditas / suavitas* series is what forces a third English word;
"delight" and "sweetness" are both already spoken for in the same clause.

### ⭐ *vaca-* IN THE APPARATUS — `c1-v12-15` p. 18 n. 1

**La.** *…non potest etiam bene cogitare de huiusmodi, qui sustinet paupertatis inopiam, nec
**vacare** etiam **ad hoc** potest qui non habet pacem et concordiam.*

**En.** "…nor can he think well about such matters who endures the want of poverty, nor can he
even be **free for** this who has not peace and concord."

**The site is already translated correctly and consistently.** Under the ratified dikaisune ruling
(2026-09-15) *vacare* is CONTEXTUAL, and this is `ad` + accusative — the "free **for**" construction,
the identical construction `c1-v8-11`'s `[^tr-vacare]` was written for (*ad nihil aliud vacabant*,
Acts 17:21, p. 16). **No English text needs to change under any option below.** The only question
is whether the ruling's required translator's note can be attached.

### The mechanism gap, stated precisely

The word stands inside an apparatus entry's **En.** half — a quotation of the Vatican edition's
addition — which lives in `## Apparatus`, not in `## English`.

`tools/polish-style-scan.py` lines 158–175 define the regions:

```python
eng = re.search(r"## English(.*?)(?:## Apparatus|## Notes|\Z)", body, re.S)
...
missing_lat = {d for d in def_set - lat_markers if not d.startswith("tr-")}
tr_in_lat   = {m for m in lat_markers if m.startswith("tr-")}
if tr_in_lat: issues.append((name, "PAIR", "translator's note anchored in Latin: …"))
missing_eng = def_set - eng_markers        # <- NO tr- exemption
```

▶ **`tr-` is exempted from the LATIN anchor requirement and FAILS if anchored in the Latin — but it
is NOT exempted from the ENGLISH anchor requirement, and `## Apparatus` is explicitly outside the
English region.** So a `tr-vacare-2` whose only anchor stood beside the word it is about would fire
`PAIR: defs not anchored in English`, in a scan that is currently **zero in vol6 out of 2,126
chunks scanned**. `tools/check-vol5-apparatus.py` line 3054 has the same `tr-` carve-out and the
same shape. **This is a real gap in the mechanism, not a builder's lapse.**

### Alternatives and cost — ⛔ NOT CHOSEN HERE

| option | cost | mechanical or per-site |
|---|---|---|
| **A. Leave unnoted; record the site in the ledger and in the gate sheet** | **0 Latin lines, 0 English lines, 0 tool lines.** The dikaisune ruling's "requires a translator's note" goes unhonoured at 1 of the volume's 2 *vaca-* sites; the next apparatus site inherits the same silence | n/a |
| **B. Extend the mechanism** — exempt `tr-` from `missing_eng` when the anchor is found in the `## Apparatus` region | **~3 lines in `polish-style-scan.py`**, plus confirm `check-vol5-apparatus.py`'s La/En pairing tolerates a nested footnote marker inside a definition, plus confirm the site renderer resolves a marker inside a footnote def. **2 added lines in `c1-v12-15`** (1 anchor, 1 def) | **MECHANICAL** on the tool side; the renderer check is a one-off |
| **C. Anchor in the English BODY of the nearest anchor** (`c1-v12-15` p. 18) | **1 English line.** ⛔ `c1-v12-15`'s body carries **no** *vaca-* word at all (verified: the only body *vaca-* in the volume is `c1-v8-11`'s). The note would attach to a sentence it was not written for — the precise failure mode CLAUDE.md's notes rule exists to prevent | **PER-SITE**, and structurally unsound here |
| **D. Extend `c1-v8-11`'s existing `[^tr-vacare]` text** to name the apparatus construction | **1 English line** (the note's own prose, in a different chunk). Notes do not reach across chunks on the site, so a reader of `c1-v12-15` never sees it | MECHANICAL |

**Type: DECISIVE-SENTENCE question**, and the decisive sentence is the apparatus entry above,
because `ad hoc` is what puts it inside `tr-vacare`'s existing scope rather than opening a fourth
construction. **n is irrelevant here** — one site in an unreachable position is the whole item.

---

# (6) POSITIVE ZEROS — each one CHECKED, not assumed

Every line below was re-derived over the **rendered** regions of all seven built chunks.
⚠ Three of the note's six zeros do not survive the check.

| claim | command | measured | verdict |
|---|---|---|---|
| ***lumen* is ZERO across all seven chunks** | `grep -oinE "\blumen\b\|\bl[uū]min[a-z]*\b" /tmp/r/*.RENDERED.txt` | **ZERO `lumen`.** Three `lumin-` hits, all in `c1-v2-7`: *luminaria* (Gen. 1:16, p. 12), "luminaries", "luminous" | ✅ **CONFIRMED.** Ruling 2 is one-sided throughout; **no `tr-lumen` is owed in this volume** |
| ⚠ the *flumen* trap | `grep -coiE "lumen\|lumin" /tmp/r/*.RENDERED.txt` (substring) | **26 hits in `c1-v2-7` alone**, nearly all *flumina/flumine* (Eccl. 1:7, *Omnia flumina intrant in mare*), plus *flumen* in `c1-v16-18` (Eccli. 47:15) | ✅ **TRAP CONFIRMED LIVE.** A bare substring sweep reports `lumen` as non-zero in 2 chunks. **Always use `\b`** |
| *lux* → "light" | `grep -coiE "\blux\b\|\bluc(is\|em\|e)\b" vol6/*.md` | present in all seven chunks | ✅ one-sided ruling 2 exercised, `lumen` never meeting it |
| **ruling 5 / `fundam.` not reached in 156 entries** | `grep -inE "fundam" /tmp/r/*.Apparatus.txt` | **ZERO in the apparatus.** The 2 rendered `fundam-` hits are Latin **body** words — `prooem` p. 3 *Primae **fundamentum** est caritas ordinata* and `c1-v2-7` p. 12 *Quando appendebat **fundamenta** terrae* (Prov. 8:29) — neither is a ruling-5 site | ✅ **CONFIRMED.** Ruling 5 is unreached at 156/156 entries. ⭐ This is exactly the `bon-serm-s2` census taken the right way: over the built apparatus, where `fundam.` lives, not over the cascade-fragmented raw |
| ***contuit-* zero** | `grep -coiE "contuit" /tmp/r/*.RENDERED.txt` | **ZERO in all seven** (7 hits exist, every one inside `## Notes` discussing the zero) | ✅ **CONFIRMED** |
| ***pietas* zero** | `grep -coiE "pieta[st][a-z]*" /tmp/r/*.RENDERED.txt` | **ZERO in all seven** (all hits in `## Notes`) | ✅ **CONFIRMED** |
| ***intelligentia* zero** | `grep -inE "intelligenti" /tmp/r/*.Latin.txt` | **n = 1, NOT zero.** `bon-eccl-prooem` Quaestio II *Respondeo*: ***Respondeo:** ad **intelligentiam** praedictorum uno modo potest dici sic…* → "**I respond:** for the **understanding** of the foregoing it can be said in one way thus…" | ⛔ **CONTRADICTS the note.** ⭐ But the site is **already covered by a frozen precedent**: *Ad intelligentiam* as the ordinary idiom → "for the understanding of…", ruled at `bon-qsc-q2` (CLAUDE.md L1424–1426), explicitly *not* a departure from *intelligentia* → "intelligence", which governs the term of art. **Precedent-covered, not a lapse — but it is not a zero, and the next chunk will be told it is** |
| ***intellectus* met twice, both → "understanding"** | `grep -oinE "\bintellect(us\|u\|um\|ui)\b" /tmp/r/*.Latin.txt` | **n = 3, not 2.** `c1-v8-11` ×2 (p. 15 divisio heading and p. 15 body, both *in intellectu humano* → "in the human understanding") and `c1-v12-15` ×1 (p. 18, *intellectus humani libidinosa prostitutio* → "the lustful prostitution of the human understanding"). **All three → "understanding"** | ⚠ **count off by one; the ruling holds at 3/3** |
| **bare English "intellect" zero** | `grep -oinE "\bintellects?\b" /tmp/r/*.English.txt` | **ZERO** | ✅ **CONFIRMED** |
| ***doctor* zero** (note's item 2) | `grep -inE "\bdoctor[a-z]*\b" /tmp/r/*.{Latin,English,Apparatus}.txt` | **n = 1 Latin, 0 English** — `prooem` p. 5 n. 6, *volentes esse legis **doctores***, a Vulgate variant quoted and left untranslated in the En. half | ⛔ **CONTRADICTS the note.** True of the English, false of the Latin |

⭐ **Why this item exists, restated from the evidence:** the three zeros that failed
(*intelligentia*, *doctor*, and *intellectus*' n) all failed **quietly**. Each looks identical, in a
handover note, to a zero that was checked. Two of the three are harmless once seen
(precedent-covered; untranslated); the third is a count, not a ruling. **None is a defect in a
chunk. All three are defects in the docket's summary.**

---

## ▶ SUMMARY OF CONTRADICTIONS BETWEEN THIS SHEET AND THE RESUME NOTE'S DOCKET

Per CLAUDE.md, the resume note's **summaries** are its least reliable lines, and per-note data beats
a narrative summary. Six discrepancies, all measured over the built files:

1. **(1)** The inversion has been measured by **FIVE chunks, not four** — `c1-v1`'s three roman
   quotations on p. 9 are omitted from the docket's region list, and p. 9 is called a positive zero
   when only `prol`'s portion of it is. ⭐ And the roman total is **approximate in the record**:
   pp. 10/12/13 have never been counted exactly, so "~58 + 11 ≈ 69" is the only figure anyone has.
2. **(1)** `c1-v2-7`'s Notes say "ten scriptural quotations" on p. 11 and **enumerate nine**; the
   tenth is the *infra tertio* self-quotation of Ecclesiastes.
3. **(2)** *doctrina* is **9 sites in 5 chunks taking 3 English words** (doctrine 4 / teaching 2 /
   learning 3), not "3 sites, a new working choice".
4. **(2)/(6)** *doctor* is **not zero in the Latin** — 1 site, `prooem` p. 5 n. 6, untranslated.
5. **(4)** The three typographic classes are **not all flattened to `####`** — classes 1 and 2 each
   take both `###` and `####`; only class 3 is uniform. Level tracks function, per ruling 4.
6. **(6)** *intelligentia* is **not zero** (n = 1, precedent-covered), and *intellectus* is **n = 3,
   not 2** (all three → "understanding", so the ruling itself is unaffected).

⛔ **None of these six is a text defect.** Every one is a defect in a carried summary. The chunks
themselves are internally consistent, fully owned, flag-free and style-clean.

---

## ▶ WHAT THIS SHEET DOES NOT DO

It settles nothing. It recommends nothing. It edited no chunk under `vol6/`. No commit, no push,
no deploy, no `git stash`. The resolver docket remains unscheduled and unfixed. Per ruling 6 as
amended (2026-09-20), **this gate carries NO deploy** — the one deploy for this work is at p. 103.
