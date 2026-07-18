# Session setup — Vol IV d.46 → d.50 (the end of Book IV)

**Written 2026-07-18** at the close of the d.45 session. Hand a fresh session THIS FILE plus
`CLAUDE.md` and `next-session-resume.md`. Everything below is already verified against the raw OCR —
do not re-derive it, but **do** re-verify anything you are about to depend on.

**State at handoff:** d.1–d.45 of Book IV are COMPLETE & Tier 2. Build **1859 translated / 1927
questions**. Nothing pushed — `master` is ahead of `origin` and pushing is a protected action
needing Wilson's per-action OK.

---

## 0. Read this first — the two lessons that cost the d.45 session the most

**(1) NEVER `grep DISTINCTIO` to find a distinction header.** The OCR garbles it via an IN→m
ligature (`DISTmCTIO`, `DISTIECTIO`, `MSTINOTIONEM`, `DI8T1NCTI0NEM`). Use:

```bash
grep -nEi "d[i1l]st[inml1]{1,2}[cg]t[il1]o" raw/bonaventure_vol4_raw.txt
```

A **real** header is a bare `DISTINCTIO N.` alone on its line with no page number. Anything carrying
a page number or `P. I`/`ART.`/`QUAEST.` furniture is a **running-head bleed**. Getting this wrong
silently deletes the front of a littera — it did exactly that to d.28, d.37 and d.45 (see
`manual-review/distmctio-garble-littera-truncation.md`).

**(2) NEVER count dubia off the OCR.** d.45 printed **9** dubia; a `DUB\.` grep found **3**, because
six were cased `DuB.`. Grep case-insensitively (`grep -niE 'd[uv]b[il1]'`) **and then count them off
the 450 dpi bands anyway.** The header audit reported `DUB raw 0 / chunk 9` for d.45 — the OCR
simply does not carry them.

Corollary that bit d.45 twice: **a chunk's apparatus can be printed outside its raw line range.**
The two-column cascade can put the *next* distinction's body text ahead of the *current* page's
footer block. d.45's p.953 footers sit at L101441–101462, past the d.46 header.

---

## 1. Verified boundaries for the rest of Book IV

Real headers, ligature-tolerant scan, cross-checked against the following `Cap. I` / COMMENTARIUS:

| d. | real header | range | notes |
|---|---|---|---|
| 46 | **L101428** | L101428–102920 | bleeds at L101372 and L101572 — neither is the header |
| 47 | **L102921** | L102921–104391 | bleed at L102981 (`DISTINCTIO XLVII. 969`) |
| 48 | **L104392** | L104392–106122 | ⚠ bleed at L104305 sits *before* the real header |
| 49 | **L106123** | L106123–109978 | bleed at L106068 (`DISTINCTIO XUX. P. I. 997`) |
| 50 | **L109979** | L109979–112356 | bleed at L109974; body ends at INDEX QUAESTIONUM L112357 |

Offset `pdf = printed + 20`. Colcrop split 1880 default; **expect gutter clipping** — d.45 needed
regeneration at 2120 (L clipped) or 1620 (R clipped) on pp. 942/943/944/946/949/950. Check bands
before transcribing.

---

## 2. d.46 — fully mapped, ready to dispatch

*De valde malis / de mitigatione poenae damnatorum* — whether the utterly wicked feel any mitigation
of punishment; mercy and justice in God's works. **Single-pars. 12 chunks.** Printed pp. 953–968.

Count-check passed: TRACTATIO (L101688) says *"duo principaliter quaeruntur"* → 2 articles;
*"Circa primum quaeruntur quatuor"* → Art I has 4; Art II's opener (L102266) says
*"circa hoc quaeruntur quatuor"* → Art II has 4.

| chunk | raw range | title (from the line AFTER the header) |
|---|---|---|
| littera | 101428–101659 | Caps I–V; header garbled `DISTINCTIO XLYI.`, `Gap. I.` at L101429 |
| divisio | 101660–101702 | COMMENTARIUS L101660, DIVISIO TEXTUS L101666, TRACTATIO L101688 |
| a1-q1 | 101703–101934 | *Utrum per suffragia Ecclesiae aliqua mitigatio fiat damnatis* |
| a1-q2 | 101935–102023 | *Utrum fiat mitigatio damnatis propter misericordiae pietatem* |
| a1-q3 | 102024–102144 | *Utrum Deus misericordius agat cum uno quam cum alio* |
| a1-q4 | 102145–102261 | *Utrum Deus agat iustius cum uno quam cum altero* |
| a2-q1 | 102262–102399 | *Utrum in aliquo opere Domini sit misericordia et veritas* |
| a2-q2 | 102400–102498 | *Utrum in eodem opere Domini sit misericordia et veritas* |
| a2-q3 | 102499–102591 | *Utrum in omni opere Domini sit misericordia et veritas, secundum quod proprie…* |
| a2-q4 | 102592–102792 | *Utrum Deus possit aliquem pure remunerare ex iustitia, vel pure ex misericordia* |
| dubia | 102793–102920 | count off the bands |

**⚠ a2-q4 nearly went missing.** Its header is `QUAESTiO IV.` (lowercase i) at L102592 and is invisible
to a `QUAESTIO` grep. It was found only by the ordinal-opener cross-check (`Quarto quaeritur` at
L102598). Art I's headers are clean; Art II's `ARTICULUS 11.` (L102262) is digit-garbled.

**Scholia** (one per article, in that article's q1, covering all of its questions):
a1-q1 → L101867 (garbled `SCHOLIOK`); a2-q1 → L102368 (`SCHOLION.`).

**⚠ INHERITED HAZARD — d.45's apparatus is inside d.46's range.** Raw **L101441–101462** is printed
p.953's footer block and is **already claimed by `bon-sent-IV-d45-dubia.md`** (10 entries). d.46's
littera must NOT claim it. Verify against that file before writing.

---

## 3. d.47 and d.48 — structure scanned, titles still to collect

Both are **2 articles × 4 questions + littera + divisio + dubia = 11 chunks**. Pull each real title
from the line *after* its QUAESTIO header, and re-run the full count-check before dispatching.

**d.47** (L102921–104391): COMMENTARIUS L103093 (`C0MMENTARIU8 IN MSTINOTIONEM XLVIL`),
DIVISIO L103101, TRACTATIO L103133. Art I L103174 → q1 L103177, q2 L103339 (`QUAESTIO 11.`),
q3 L103435, q4 L103574. Art II L103677 (`ARTICULUS 11.`) → q1 L103690, q2 L103926,
q3 L104051 (`QUAESTIO ni.`), q4 L104153. Dubia L104264 (`DUBIA CIRGA LITTERAM MAGISTRI.`).
Scholia: a1-q1 L103303 (`SCHOLIOK`), a2-q1 L103885.

**d.48** (L104392–106122): COMMENTARIUS L104642, DIVISIO L104648, TRACTATIO L104663,
`NOTAE AD COMMENTARIUM` L104682. Art I L104696 (`ARTIGULUS I.`) → q1 L104699, q2 L104903,
q3 L105061, q4 L105151. Art II L105280 (`ARTIGULUS 11.`) → q1 L105291, q2 L105475,
q3 L105611 (`QUAESTIO lU.`), q4 L105767. Dubia from L105868 (`DIST. XLV[n. DUBIA. 99r`).
Scholia: a1-q1 L104867, a2-q1 L105417 (both `SCHOLIOK`).

---

## 4. d.49 — ⚠ STOP AND GET A CONVENTION DECISION BEFORE CHUNKING

**d.49 is the largest distinction in Book IV (~3,855 raw lines) and it introduces a structural level
that the chunk-id scheme cannot currently express.**

Running heads include **`DIST. XLIX. P. II. SECT.`** — Pars II is divided into **SECTIONS**, each with
its own ARTICULUS I…N. That is why `ARTICULUS I` appears twice inside Pars II's range (L107691 and
L108791). No other distinction in Books I–IV has a sectio level.

Observed skeleton:
- **Pars I** — COMMENTARIUS L106350, DIVISIO L106363, TRACTATIO L106424,
  **ARTICULUS UNICUS** L106437 with **6 questions**: L106440, 106713, 106834, 107078, 107275, 107473.
- **Pars II** — COMMENTARIUS L107630, DIVISIO L107643, TRACTATIO L107655.
  - *Sect. I(?)*: Art I L107691 (q1 L107694, q2 L107897), Art II L108070 (q1 L108081, q2 L108296),
    Art III L108359 (q1 L108392, q2 L108611).
  - *Sect. II(?)*: Art I L108791 (q1 L108801, q2 L109015), Art II L109111 (q1 L109120, q2 L109283),
    Art III L109392 (q1 L109404, q2 L109698), Art IV L109755 (q1 L109787, …).
- **No DUBIA header found** anywhere in d.49's range. Verify off the bands before concluding there
  are none — that is exactly the d.45 failure mode.

**The decision to put to Wilson before writing any d.49 chunk:** how to express sectio in the id.
Options are (a) `d49-p2s1-a1-q1` style, (b) treat each section as its own pars (`p2`/`p3`) and record
the real structure in frontmatter + Notes, or (c) add a `sectio:` frontmatter field and leave ids flat.
Option (b) is least invasive to `build-content.mjs` and the site router; option (c) is most faithful.
**Do not improvise this** — it is the kind of convention that is expensive to change once ~30 chunks
exist. Map the pars/sectio boundaries off the running heads first so the choice is made against real
structure.

---

## 5. d.50 — the last distinction, and it triggers the decade gate

**Two pars.** Printed range ends at INDEX QUAESTIONUM (L112357).
- **Pars I** — COMMENTARIUS L110249, DIVISIO L110261, TRACTATIO L110272,
  `NOTAE AD COMMENTARIUM` L110301. Art I L110284 (q1 L110288, q2 L110495, q3 L110671),
  Art II L110810 (q1 L110826, q2 L110926, q3 L111162).
- **Pars II** — COMMENTARIUS L111262, DIVISIO L111272, TRACTATIO L111291.
  Art I L111302 (q1 L111305, q2 L111642, q3 L111798 `QUAESTIO 111.`),
  Art II L111914 (q1 L111929, q2 L112039 `QUAESTiO II.` — lowercase i, same garble as d.46's a2-q4,
  q3 L112238).
- **`DUBIUM CIRCA LITTERAM MAGISTRI.` at L112272 — singular.** Confirm off the bands whether there is
  genuinely one dubium or whether more are hidden by casing.

**★★ AFTER d.50 CLOSES, RUN THE d.41–d.50 DECADE GATE** — it is a hard blocker and it is the LAST
gate of Book IV. Three passes per `CLAUDE.md` "Polish-blocker cadence", logged to
`manual-review/vol4-d41-d50-polish-resolution-log.md`:
1. `[?]` flag resolution at 600 dpi over d.41–d.50. **Known open flag: d.45 a2-q3, p.946 note 6 ends
   abruptly at *pro divite* with no continuation printed.** Plus d.42's flags (already listed in
   `next-session-resume.md`).
2. Full-corpus style/formatting audit — `tools/polish-style-scan.py`. **Confirm it still scans all
   four volumes**; it was silently hardcoded to vol1+vol2 until 2026-07-13.
3. Cross-chunk boundary-integrity sweep over d.41–d.50 seams. **Add the distinction-header seam to
   this pass** — the d.21–d.30 and d.31–d.40 gates both missed the `DISTmCTIO` truncations precisely
   because Pass 3 only swept seams *between* chunks.
4. Then `rm -f raw/vision/vol4/*.png /tmp/colcrop/*`.

---

## 6. The cadence that worked (d.45 shipped 12 chunks this way)

Coordinator does **no** translating and reads **no** PDFs. It maps, rechunks, pre-generates all bands
serially, dispatches, reconciles, then builds/audits/commits.

1. Verify the boundary with the ligature-tolerant grep. Run the **full count-check**: ordinal openers
   (`(Primo|Secundo|Tertio|Quarto|Quinto) quaeri`), TRACTATIO "quaeruntur N", scholion "De N.
   quaestione", case-insensitive DUBIA grep, digit-tolerant COMMENTARIUS.
2. Copy `tools/rechunk_d45.py` (current template — single-pars, page-qualified apparatus, keeps
   `line_start`/`line_end` so all three audits run). Page assignments from raw lines are only
   estimates; writers correct them from running heads.
3. `rm -f raw/vision/vol4/*.png /tmp/colcrop/*` → extract the range at 450 dpi → colcrop every page
   at 1880 serially.
4. Dispatch **write-only subagents, one chunk each, in batches of 4** (8 GB machine — do not exceed).
   Give each the shared brief plus its chunk's specifics, its scholion owner, its raw range and pages,
   and both hand-offs. Reuse
   `manual-review/vol4-writer-brief-template.md` as the template — it is generic apart from its
   header, and it encodes every trap: band authority, page-qualified labels, no `[^…]` in prose, no
   positional relabelling, scholion-last, seam continuity, verify-the-body-after-an-API-error.
5. **Reconcile every shared page from both sides.** Adjacent writers derive their apparatus split
   independently; in d.45 all seven shared pages agreed. A disagreement is a real finding — chase it.
6. `node site/scripts/build-content.mjs` → confirm the translated count rose by exactly the chunk
   count and every chunk shows `translated=True` with the apparatus count its writer reported.
7. Three audits `--volume 4 --min-d N --max-d N`. Positive header/apparatus diffs are normal for
   two-column Vol IV; **flags** are what matter.
8. **Two commits**: (a) chunks + tools + manual-review, (b) `next-session-resume.md` advanced.
   `site/src/data/content.json` is gitignored — do not try to add it.
9. **Do NOT push and do NOT deploy.** Both are protected actions requiring Wilson's per-action OK.

## 7. Open items not owned by this run

- **Renderer hardening (optional).** `text-reader.tsx:282` matches `\[\^([^\]]+)\]` with no code-span
  awareness, so any literal `[^…]` token in prose renders as a live link. The 3 real instances were
  fixed 2026-07-18 (`81ca91c`) and the writer brief forbids new ones, but the renderer is unchanged.
- **J4 Class D/E** — ~38 repeated-anchor chunks still unrepaired. Sampling found genuine content loss
  in `II-d23-a2-q2` and `IV-d4-p1-a2-q1`. Needs one-subagent-per-chunk with page-image verification;
  do not bulk-edit. Awaiting Wilson.
