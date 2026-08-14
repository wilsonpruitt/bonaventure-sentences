# Work-close polish gate — *De reductione artium ad theologiam* (pp. 319–325)

Run 2026-08-14, immediately after `bon-red` landed (`92bddec`). A 7-page work fires
**exactly one gate, at its close**, per the frozen rule that a work shorter than the
~100-page interval gets one and never zero. All four passes run; **zero corpus defects.**

⚠ **This gate is unusual in one respect and it changes pass 3:** the work is a **single
chunk**, so it has **no chunk boundaries at all**. The boundary sweep therefore becomes a
**page-joint sweep** — the six interior leaf joints plus the two work edges — which is the
same hazard (text lost at a seam) approached from the only side this work offers.

## Pass 1 — `[?]` flag resolution: NOTHING TO RESOLVE, verified not assumed

`grep '\[?\]' vol5/bon-red.md` returns **one hit, and it is prose declaring the absence** —
the `transcription_status` string's own words "zero [?] flags". No inline flag exists in
either language block or in the apparatus. Recorded as a **checked negative**: the work was
written with every ambiguity settled at the plate rather than parked, and the four digit
settlements (p. 321 n. 3's `1`/`4`, p. 322 n. 1's `13, 8`, p. 324 n. 2's `Ps. 118`,
p. 325 n. 3's `2, 5`) were each closed against an independent witness at writing time.

## Pass 2 — style/formatting audit: vol5 CLEAN; the Vols III–IV residue is UNCHANGED

- `polish-style-scan.py --volume 5` → **CLEAN, 90 files.**
- Full corpus (2,024 files) → **10 PAIR issues / 5 chunks**, every one of them an orphaned
  def in **Vol III or Vol IV**. This is the known **J4 class-B residue**, and the count is
  **identical to what the Itinerarium gate recorded on 2026-08-01** — it has not grown.
  Recorded and deliberately **NOT fixed**: this gate authorises no edit under `vol3/` or
  `vol4/`.
- **✅ One real defect was found by this pass and fixed inside `vol5/`:** the English block
  opened without its `<!-- page 319 -->` marker while the Latin block carried it. The
  closest precedent (`bon-itin-c6`) puts the opening marker at the head of both blocks, so
  the marker was added. Suite re-run after the fix: apparatus 90/890 passed, style scan
  CLEAN, build **2023/2023**.

## Pass 3 — page-joint sweep: SIX INTERIOR JOINTS, ALL CONTINUOUS, COUNTED BY HAND

`seam-screen.py` is structurally blind to leaf crossings and has, in this work, **nothing to
see at all** — there are no chunk boundaries. Every joint below was read directly out of the
file and checked in **both languages**.

| joint | falls inside | Latin break | continuous? |
|---|---|---|---|
| 319→320 | ¶ 2 | *…sic est agri-* \| *cultura; si quantum ad sensibilia…* | ✅ mid-word |
| 320→321 | ¶ 4 | *…ut sic illuminetur* \| *homo ad veritatem vitae…* | ✅ mid-clause |
| 321→322 | ¶ 5 / ¶ 6 | *…Hugo vero omnia haec.* \| *6. Ex praedictis colligitur…* | ✅ paragraph boundary |
| 322→323 | ¶ 12 | *…per quam artifex exco-* \| *gitat, antequam producat…* | ✅ mid-word |
| 323→324 | ¶ 17 | *…ut sit modificata* \| *per modestiam in exteriori opere…* | ✅ mid-clause |
| 324→325 | ¶ 22 | *…nisi sit spi-* \| *ritualis per contemptum…* | ✅ mid-word |

**Four of six break mid-word**, which is the ordinary Quaracchi shape and is exactly why the
raw's silent line-drop at a page foot is the failure the audits cannot see; each joint was
therefore checked against the band at transcription time as well as against the file here.
Both language blocks carry the same six markers at matching positions.

**Work edges, both fixed positively.**
- Front: p. 317 half-title (verified at the Itinerarium scholion's scouting) · **p. 318
  MEASURED BLANK, 146 ink px** — the page had never been checked before this session.
- Back: ¶ 26 ends *…qui est benedictus in saecula saeculorum. Amen.*, then the bare centred
  **`EXPLICIT.`**, and the end is fixed from the **`COLLATIONES IN HEXAEMERON` half-title**
  (raw L57174) — never from the white space below the columns.

**Register contiguity.** `check-vol5-apparatus.py` confirms every one of the seven pages runs
**1..N with no gap, no double-claim and no unowned page**, agreeing with the `KNOWN_TOTALS`
entries fed from the bands (319:6 · 320:8 · 321:8 · 322:8 · 323:11 · 324:9 · 325:9 = **59**).
**No page is PENDING**: being one chunk, the work forwards nothing and inherits nothing.
✅ **The page-crossing-runover negative was checked leaf by leaf** — pp. 320–325 each open
their left footer block **numbered ¹** — and the corpus page-crossing total is **unchanged
at 7**.

## Pass 4 — disk

The vol5 450 dpi plates for pp. 317–325 and the `/tmp/colcrop` bands are **regenerable**
from the gitignored PDF (`extract-pages.py --volume vol5 --pages 317-325 --dpi 450`, then
`colcrop.py vol5 <page> <split>` with the adopted splits recorded in the scouting file and in
the chunk's `## Notes`). Reclaimed at the close of this gate. ⚠ **Re-extract before any later
plate work on this work** — the same warning the Itinerarium gate left, and it was needed.

## Verdict

**PASSED — zero corpus defects.** One formatting defect found and fixed (the missing English
page marker); one pre-existing out-of-scope residue recorded (Vols III–IV, 10 PAIR issues,
unchanged). Suite at the gate: **90 chunks / 890 apparatus entries · census 90/90 · style
CLEAN · build 2023/2023 · 73 citation records from `bon-red`, 0 dangling, 2 QA flags** (the
tome-inheritance parser class, which authorises no `vol*/` edit).

⛔ **The deploy at p. 325 is the one trigger still unfired, and it is protected** — as is the
push. Both need Wilson's explicit per-action OK.
