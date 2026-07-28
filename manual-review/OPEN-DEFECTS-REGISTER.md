# Open defects register — what must be addressed, and when

**Created 2026-07-19**, consolidating everything left open by the d.45–d.47 work and the four-screen
detection sweep. This is the single place to look before publishing a volume or deciding what to
repair. **Nothing here is in progress; every item awaits Wilson's go.**

> **★ 2026-07-28 — the actionable subset of this register is now sequenced, with model
> routing, in `manual-review/NEXT-SESSION-QUEUE.md`. Start there.** Two entries below
> were retired the same day as stale (B1, C1); read their CLOSED banners before acting
> on anything nearby.

Two categories, because they have different urgency:

* **§A — DEBT IN ALREADY-PUBLISHED VOLUMES.** Vols I, II, III are live on
  bonaventure.wrootpress.com. These are reader-facing now.
* **§B — GATES BEFORE THE NEXT VOLUME PUBLISHES.** Book IV is not yet complete; these should be
  closed before it ships.
* **§C — TOOLING BLIND SPOTS.** Not defects in the text, but reasons a defect could hide.

---

# §A — Debt in already-published volumes

## A1. ★ 108 unresolved `[?]` flags rendering in reader-facing text

Counted inline in the `## Latin` / `## English` bodies (excluding `## Notes` discussion and the
`transcription_status` boilerplate, both of which mention `[?]` harmlessly):

| vol | inline body flags | files | status |
|---|---|---|---|
| **I** | **88** | **19** | **PUBLISHED** |
| II | 0 | 0 | published, clean |
| III | 0 | 0 | published, clean |
| IV | 20 | 9 | in progress |

`[?]` is plain body text, so it renders literally on the site — a reader of Vol I sees `[?]` in the
Latin. Worst offenders: `bon-sent-I-d42-a1-q4` (18), `I-d31-p2-a1-q3` (12), `I-d14-a2-q2` (10),
`I-d24-a2-q1` (8).

**Note the shape of this table:** Vols II and III are at zero because the decade-polish gate's flag
resolution pass was applied to them. **Vol I predates that discipline.** This is a known, bounded,
19-file job — the cheapest large win available.

## A2. ★ J4 Class D/E — ~38 chunks, and the sample found real content loss

From the 2026-07-17 J4 session. 4 of the 42 repeated-anchor chunks were checked against page images;
**none was the benign "legitimate double anchor" the handoff predicted — all 4 needed real repair**,
and two involve text that was never transcribed at all:

* `II-d23-a2-q2` — **~17 real footnotes across pp.540–541 never transcribed.** The file's own `## Notes`
  self-confesses mapping p.540/541 anchors "by position" onto p.539's scheme. **Vol II is published.**
* `IV-d4-p1-a2-q1` — **genuine content loss**: ~8 of 19 real p.100–101 footnotes absent, including a
  citation of Constantine's edict (Eusebius); several anchors bound to the WRONG note across the
  page-restart boundary.
* `I-d37-littera` — a mislabeled cluster (~5 adjacent markers) needing Class-A reconciliation.
* `IV-d21-p1-littera` — not a defect; a classifier + renderer false positive (see C3).

**The remaining ~38 have not been checked.** The 4-for-4 hit rate on the sample is the reason this
ranks high. Budget it like Class A+B: one subagent per chunk, page images required.

## A3. Transcription-variant class — ~0.5–1 per page, apparatus and citations

Surfaced incidentally by the detection screens, in **both Vol I and Vol III**. None touches
Bonaventure's argument; all are in notes/citations. Concrete instances found in ~11 sampled pages:

| chunk / page | printed | rendered |
|---|---|---|
| III-d4-a1-q2, p.101 scholion III | `t. IV. q. 32.` | `l. IV. q. 32.` |
| III-d19-dubia, p.413 n.5 | `Eccli. 15, 14` | `Eccli. 13, 14` |
| III-d27-a1-q4, p.601 app. | `habent bis diligat` | `habent his diligat` |
| III-d31-a2-q3, p.687 schol. II | `a. 4` (×2) | `a. 1` (×2) |
| III-d11-a1-q1, p.243 | marginal rubric `Pro parte negativa.` | omitted |
| I-d39-a1-q2, p.689 n.7 | `Quae afferuntur` | `Quae allegantur` |
| I-d39-a1-q2, p.689 n.9 | `in elicienda cognitione` | `in eliciendo cognitione[m]` |
| **I-d39-a1-q2 `[^15]`** | ? | **`Quae litterantur…` — not a Latin word. Suspected garble; needs the p.690 band.** |

A rate, not a list: extrapolating ~0.5/page over ~2,600 published pages implies order-1,000
low-severity variants. **Do not extrapolate that into a repair plan without a bigger sample** — 11
pages is too few to size anything. But it is the honest reading of what was seen.

## A4. `DISTmCTIO` littera-truncation class — closed for Book IV only

The IN→m ligature garble truncated `d28-littera` and `d37-littera` in Book IV (repaired 2026-07-18).
The class is recorded as **CLOSED FOR BOOK IV**. **Vols I–III were never swept for it.** Detection
recipe exists and is cheap: `grep -nEi "d[i1l]st[inml1]{1,2}[cg]t[il1]o"` then compare hits against
each volume's expected distinction count.

---

# §B — Gates before Book IV publishes

## B1. ~~d.41–d.50 decade gate — hard blocker, the last of Book IV~~ — **CLOSED**

> **CLOSED 2026-07-21** (commit `448ef76`, 16 chunks repaired; log at
> `manual-review/vol4-d41-d50-polish-resolution-log.md`). Book IV completed the same
> day and is pushed and deployed. The queued items below were all dispositioned
> there — including the p.946 note-6 ~120-word loss (restored) and the `transumtum`
> misread (an artifact of the wrong gutter, corrected). Kept as history.



Fires when d.50 closes. Three passes (flag resolution at 600 dpi, full-corpus style audit, boundary
sweep). Known items already queued into it:

* **d.45 a2-q3** — `[?]` flag: p.946 note 6 ends abruptly at *pro divite*, no continuation printed.
* **`bon-sent-IV-d45-dubia.md`** — two logged-not-fixed misreads: `[^p953-6]` reads *nota 3* where the
  band shows **nota 5**; `[^p953-7]` reads *d. 33. q. 1.* where the band shows **d. 35. q. 4.**
* **d.42** — several open `[?]` flags (a1-q1 `[^p869-7]` cross-ref to a nonexistent "pag. 868, nota 11";
  a2-q1 clipped codex sigla; a2-q2 "alis[?] cognatio"; littera apparatus completeness at 600 dpi).
* **The 20 remaining inline `[?]` flags in Vol IV** (9 files) — see A1.

## B2. d.49 dubia — unverified, and the chunking assumes none

**No dubium header is greppable anywhere in d.49's range, and `rechunk_d49.py` created no dubia chunk.**
This is exactly the d.45 shape (9 printed, 3 greppable). **Verify off the bands — the foot of p.1032
especially — before accepting that d.49 has none.** If dubia exist, add `d49-p2-dubia` and shorten
`s2-a4-q2`.

## B3. Vol IV low notes-per-page distinctions — not spot-checked

The §1a screen flagged **IV d.19 (5.7)** and **IV d.34 (6.2)** alongside Vol I d.38/d.39. Vol I's two
were checked and came back clean (long editorial notes, genuine page design). **Vol IV's two were not
checked.** Same cheap method: read the footer off the band, count, compare.

---

# §C — Tooling blind spots

## C1. ~~`audit-style-formatting.py` never scans Vol IV~~ — **CLOSED**

> **CLOSED 2026-07-28.** Stale on two counts: vol3/vol4 were added to the walk on
> 2026-07-13, and **vol5 was added 2026-07-28** along with the tier-2 tally, the
> volume-key lookup and the report header. Verified: the tool now reports
> `Vol I 406 | Vol II 448 | Vol III 406 | Vol IV 633 | Vol V 16`. The filename-regex
> concern below is also stale — the alternation was reordered longest-first
> (`IV|III|II|I`) at the same 2026-07-13 fix. Everything from here to the next `##`
> is kept only as history.



`tools/audit-style-formatting.py:263` walks **vol1, vol2, vol3 only**, and its filename regex at
line 213 is scoped `bon-sent-(?:I|II)-`. So Vol IV is invisible to it, and the legacy-duplicate
detector only ever matched Vol I/II names.

**This is the same class of bug as the `polish-style-scan.py` hardcoded `DIRS=["vol1","vol2"]` defect
found at the d.31–d.40 gate — the one that made every prior "Pass 2 CLEAN" in the vol3/vol4 gate logs
false.** `polish-style-scan.py` was fixed (now `DIRS = ["vol1","vol2","vol3","vol4"]`);
`audit-style-formatting.py` was not. **Fix before the d.41–d.50 gate runs, or that gate's Pass 2 will
report a clean it has not earned.**

Also note it rewrites `manual-review/vol3-d21-d30-pass2-style-audit.md` in place on every run,
clobbering that historical gate log.

## C2. `line_start` missing from most Tier-2 chunks — blocks detection

| vol | missing / total Tier-2 |
|---|---|
| I | 2 / 410 |
| II | **246 / 464** |
| III | **368 / 412** |
| IV | **319 / 594** |

Promotion sessions dropped the range fields (the `rechunk_d23.py` bug, generalised). This is why the
dubia audit covered **0%** of Vol III, and why the sharper per-page footer-dropout detector cannot be
built. Backfill is mechanical (match each chunk's opening line against the raw) and would unlock both.

## C3. `[^N]` inside backticks renders as a live footnote link

The site's `text-reader.tsx` inline-token regex does not respect code spans, so a backtick-quoted
`` `[^1]–[^14]` `` in an explanatory note renders as live, spurious footnote links and steals bindings.
3 files were repaired 2026-07-18; the ~27 other blockquote `[^N]` hits were judged **legitimate
Conclusio anchors and must not be touched**. **Open question: teach the renderer + the §6 classifier
to respect code spans**, rather than relying on authors avoiding the notation.

## C4. CLAUDE.md teaches a marker-order rule that is only sometimes true

The d.20 lesson (footers numbered in **column** order while anchors fall in **reading** order) is
recorded as a general rule. **d.47 found pp.973/979/980 binding in straight reading order.** The order
**varies per page**. CLAUDE.md should say so; presenting the d.20 rule as universal invites exactly
the position-based relabelling that corrupts text.

---

# Suggested order

1. **C1** — one-line fix, and it is a prerequisite for trusting the d.41–d.50 gate.
2. **C4** — wording fix, no sweep, stops teaching a half-true rule.
3. **B2** — must happen before d.49 is written; it is on the critical path.
4. **A1** — 19 Vol I files, bounded, removes `[?]` from published reader-facing text.
5. **A2** — the only item with confirmed content loss; expensive (~38 chunks, one agent each).
6. **C2** — unlocks A3-sizing and the footer detector.
7. **A3 / A4 / B3** — screens and samples, cheap, do when convenient.

---

## Added 2026-07-19 from the d.49 run

### ⚠⚠ NEW CLASS — CROSS-PAGE FOOTER RUNOVER (corpus-wide, unquantified)

A Quaracchi footnote can continue onto the **following printed page's** footer, as an *unnumbered
fragment sitting above that page's note 1*. Two instances found in d.49:

* **p.1029 note 5** breaks off on a comma (*…insinuatur responsio,*) and completes at the head of
  **p.1030's** left footer column.
* **p.1028 note 10** runs onto **p.1029's** head — found ONLY because a writer was explicitly asked to
  sweep every register head and tail after the first case surfaced.

**Why it matters:** no audit checks this. A writer reading only its own pages' footers renders a
truncated note and never knows — the note looks complete because it ends in plausible Latin. This is
distinct from the within-page gutter overflow (common, already documented).

**Scope: UNKNOWN and potentially large.** Every chunk built before 2026-07-19 was written without this
check. Any of them may hold silently truncated notes at page boundaries. **Needs a sampling pass to
establish a rate before anyone decides on a sweep** — same discipline as the gutter-parity question,
which sampled to 0 errors and correctly warranted no sweep.

**Standing instruction going forward (d.50 and any re-verify):** check the HEAD of each footer register
for an unnumbered opening fragment belonging to the previous page, and the TAIL of each for a note that
breaks off mid-sentence.

### ★ DETECTION HEURISTIC — negative apparatus diff = raw footer dropout

`audit-apparatus-count` compares raw footer-openers against chunk defs, so it is blind to the
whole-register dropout class when the RAW is the empty side. **But read inverted it DOES see it:** a
**negative** diff (chunk defs > raw openers) means the writer recovered footers the raw never had.

d.49's five: `s2-a3-q2` 1 vs 11 · `s2-a4-q2` 2 vs 11 · `p1-a1-q2` 8 vs 17 · `s2-a1-q2` 7 vs 14 ·
`s1-a2-q2` 6 vs 9. Useful as a post-write triage screen, and as a way to hunt the class retroactively
across already-built chunks.

### ⚠ THE "108 INLINE `[?]` FLAGS" FIGURE NEEDS RE-DERIVING BEFORE ANYONE ACTS ON IT

A naive `grep '\[?\]'` over d.49's 24 chunks returns 30 hits and looks alarming. **All 30 are false
positives** — every one is the writer's own sentence "**`[?]` flags: none.**" inside its `## Notes`
block, a backtick-quoted mention rather than an inline flag in reader-facing text. d.49 has **zero**
genuine flags.

The register's headline figure (108 inline flags, 88 of them in published Vol I across 19 files) was
presumably counted the same way. **Re-derive it with a method that excludes `## Notes` and backtick
code spans before scheduling any repair work** — the real number may be materially lower. Note this is
the same family as the known J4 Class D/E false positive, where backtick-quoted `[^N]` ranges in intro
notes both miscounted AND rendered as live footnote links.

