# Vol V — *Collationes in Hexaëmeron*: MID-WORK GATE (2026-08-15)

The **second** of this work's three gates. Fired **deliberately, not by arithmetic**: the frozen
cadence's ~100-printed-page trigger would not have fired again before the work close, which would
have left the work with two gates instead of three. Scope: **`bon-hex-c5` … `bon-hex-c8`, printed
pp. 353–372, 20 leaves, 106 numbered paragraphs, 152 apparatus entries.**

**Result: ONE corpus defect, found and fixed** — and its cause is the finding worth keeping.
Everything else below is a measurement, a checked negative, or a pre-existing issue in another
volume that this gate authorises no edit to.

⚠ This gate ran **after** the push and deploy of the same material (Wilson OK'd both before it),
so the defect it caught was briefly live. It is fixed in the corpus and will ship with the next
deploy; nothing else in the span needed correction.

---

## Pass 1 — `[?]` flag resolution: NOTHING TO RESOLVE IN THE SPAN, and the instrument was rebuilt

**★★ THE OBVIOUS INSTRUMENT IS USELESS AND HAS BEEN SILENTLY USELESS AT EVERY PRIOR GATE.**
`grep -n "\[?\]" vol5/*.md` returns **100+ hits**, of which — corpus-wide — only a handful are
real. Nearly every chunk's `## Notes` *discusses* flags in prose (*"No `[?]` flags."*, *"TWO `[?]`
FLAGS TRAVEL FORWARD…"*), and every Tier-2 `transcription_status` says *"zero [?] flags"*. A gate
that greps and eyeballs the result is not checking anything it can defend.

**A flag is LIVE only if it stands in rendered text** — `## Latin`, `## English`, `## Apparatus`.
`## Notes` is never rendered (no component reads it) and frontmatter is metadata. **New tool:
`tools/check-live-flags.py`**, which strips both and reports what is left. Derived, not
hand-carried, per the standing rule.

**Result in the span: `bon-hex-c5`–`c8` carry ZERO live flags.** The only live flag in all of
vol5 is `bon-brev-p6-c13`'s p. 280 n. 6 (the defective final word of *…homo non separe*, where
Quaracchi dropped the `t`) — **outside this span, correctly dispositioned by the chunk that raised
it, and deliberately left standing** because the reading is certain and the text is not.

**★ A NUMBER NOBODY HAD:** live-flag counts by volume, now derivable —
**vol1 = 150 · vol2 = 9 · vol3 = 2 · vol4 = 66 · vol5 = 2** occurrences (a flag mirrored in Latin
and English counts twice), **229 in all across 2,033 chunks.** Vols I and IV carry essentially the
whole backlog. **This gate authorises no edit under `vol1/`–`vol4/`;** it is a scoped defect list
for a session of its own, like the apparatus backlog and the dangling-citation list — jobs, not a
blob.

## Pass 2 — style/formatting audit, full corpus

`polish-style-scan.py` over all 2,032 chunks: **vol5 CLEAN (98 files).** Corpus-wide **10 PAIR
issues across 5 chunks, all pre-existing, all Vols III–IV** — `bon-sent-III-d31-a3-q3`,
`III-d32-a1-q2`, `III-d5-a2-q4`, `IV-d14-p2-a2-q1`, `IV-d16-p2-a2-q2`. This is the known **J4
class-B residue** (orphaned defs), identical to what the shakedown and Itinerarium gates found.
**Recorded, deliberately NOT fixed.**

## Pass 3 — boundary integrity sweep

**Five chunk boundaries, counted BY HAND.** `seam-screen.py --volume 5` reports **two** of them
(p. 353 and p. 368) and is structurally blind to the rest, exactly as the frozen rule says:

| boundary | shape | tool sees it? |
|---|---|---|
| c4 \| c5 at **p. 353** | mid-leaf, register **splits** 3/1 | yes |
| c5 \| c6 at **359 \| 360** | **leaf edge** | **no** |
| c6 \| c7 at **364 \| 365** | **leaf edge** | **no** |
| c7 \| c8 at **p. 368** | mid-leaf; c8 contributes heading + Summarium only and claims **none** of the register | yes |
| c8 \| c9 at **p. 372** | mid-leaf, register **splits** 1/2 | **no** — c9 does not exist yet |

Plus **17 page joints interior to the four chunks**, each read against the band at write time and
recorded in its chunk's page-break map. **22 seams in all; the tool sees 2.**

- **Both leaf edges verified independently by ink-row profile**, not by re-reading the earlier
  session's note: **p. 359** runs body → blank (72–74 %) → footer rule (76 %) → register → blank,
  and **p. 364** the same. **No orphaned matter stands between the last transcribed line and the
  footer rule on either leaf.**
- **Both split registers re-read at magnification.** p. 372's left block holds n. 1 alone,
  complete; its right block holds nn. 2–3, both complete and both Collatio IX's. The 1/2 split is
  confirmed from the plate, and `check-vol5-apparatus.py` reports p. 372 as a legitimate PENDING
  rather than a GAP.
- `seam-screen.py`: **0 tail-not-terminal suspects** across all 84 vol5 mid-page boundaries.

### ⚠ THE ONE CORPUS DEFECT — and the habit that caused it

**`bon-hex-c8`, p. 372 n. 1: the English read *Dieta salutis* where the Latin reads, and the plate
prints, `Dictae salutis`.** The English had silently normalised Quaracchi to the work's usual
modern title. **Corrected.** Quaracchi is never silently emended, in either language.

**★★ THE CAUSE IS THE FINDING: this was the ONE apparatus entry in the whole span transcribed
from a whole-page (⅓-scale) read instead of a magnified footer band.** Every other entry across
the four chunks came off a 1.7–2.2× band crop. The defect rate is 1-for-1 on low-magnification
transcription and 0-for-151 on band transcription. **A whole-page read is for STRUCTURE — where
the heading falls, whether a block opens numbered, whether a column is short. It is not good
enough to transcribe an apparatus entry from, and no future chunk should do it.**

### A mechanical sweep for the same class, and its one false positive

Because the defect was a **La/En divergence**, the gate swept the class: for all 152 apparatus
entries in the span, compare the multiset of Arabic digits in the `**La.**` half against the
`**En.**` half. **One hit, and it is a false positive** — `bon-hex-c7`'s `p365-4`, where Latin
`a. 2. … (2. opinio)` renders as English `a. 2 … (the second opinion)`, an ordinal correctly
spelled as a word. **Known false-positive class; the check is still worth running** — it is cheap
and it is the only mechanical instrument that can see this defect family at all.

## Pass 4 — disk cleanup

**242 MB reclaimed** (22 leaves at 450 dpi in `raw/vision/vol5/` plus all `/tmp/colcrop` bands),
both fully regenerable from the gitignored PDF.

⚠ **NEW, AND IT MATTERS FOR THE NEXT DEPLOY: the build+deploy cycle transiently costs ~5 GB of
disk.** Free space went **7.0 GB → 1.5 GB** across `vercel build --prod` + `deploy --archive=tgz`
and one command failed with `ENOSPC` during cleanup. Deleting `site/.next` and
`site/.vercel/output` after a successful deploy (both regenerable; keep them only while a
`fetch failed` retry is still possible) returned it to **3.1 GB**. **Check free space before the
next deploy, and clear the previous one's artifacts first.** Per the standing rule, the phantom
Xcode footprint was NOT investigated.

## Verification suite at the close of the gate

`check-vol5-apparatus.py` **98 chunks / 1,248 entries**, all passed, p. 372 a legitimate PENDING ·
`check-vol5-census.py` rosters agree **98/98**, 107 runovers (95 gutter-crossing, 12
page-crossing) · `polish-style-scan --volume 5` **CLEAN** · `build-content.mjs` **2031/2031, 8
books** · `build-citations.py` corpus QA **228, unchanged** · `check-live-flags.py` vol5 **2
occurrences, both outside the span**.

## What this gate did not do

- **No push, no deploy.** Both are protected; the material was already pushed and deployed before
  the gate ran, and the `Dictae salutis` fix is therefore **not yet live** — it ships with the
  next deploy.
- **No edit under `vol1/`–`vol4/`.** The 229-occurrence live-flag backlog and the 10 PAIR issues
  are recorded and scoped, not touched.
