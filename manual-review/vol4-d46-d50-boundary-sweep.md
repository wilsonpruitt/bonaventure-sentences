# Vol IV — d.46–d.50 cross-chunk boundary integrity sweep

**Pass 3 of the d.41–d.50 decade gate.** Scope: `vol4/bon-sent-IV-d4{6,7,8,9}-*.md` and
`vol4/bon-sent-IV-d50-*.md` — 74 chunks. (d.41–d.45 covered by a separate agent.)

Date: 2026-07-21. Method: chunk frontmatter line ranges + apparatus claim map vs
`raw/bonaventure_vol4_raw.txt`, with 450 dpi column-band reads on five sampled pages.

## Result

**56 mid-page seams checked. 56 CLEAN. Zero defects. Nothing rewritten.**

No cascade-merge splice found anywhere in the range. This is consistent with the
two-sided seam derivation used to build d.46–d.50 (both adjacent writers derived each
shared page independently and reconciled) — the re-check found no disagreement.

## (a) Grammatical continuity — 56/56 CLEAN

Every one of the 56 mid-page seams was dumped as `prior-chunk Latin tail (230 chars)` /
`receiving-chunk Latin head (200 chars)` and read.

- **Every prior tail parses as a complete sentence** and terminates on a full stop. No
  broken splice — the cascade-merge signature is absent from the whole range.
- **Every receiving head opens on a proper structural heading** (`Articulus`, `Quaestio`,
  `Dubia/Dubium`, `Commentarius`, `Sectio II`, `Pars II`) followed by a fresh sentence
  (`Secundo quaeritur…`, `Consequenter…`, `Quantum ergo ad primum…`).
- Tails that end in bibliographic matter (`Scot., hic q. 4. — S. Thom., …`) are scholion
  closings, not truncations — normal for this corpus.

**Line-range contiguity: perfect.** Sorting all 74 chunks by `line_start`, every chunk's
`line_start` equals the previous chunk's `line_end + 1`. Zero raw-line coverage gaps, so
no body text fell between chunks.

### One tail examined and cleared

`d49-p2-s1-a1-q2` (seam p.1015) ends `…sicut dicitur calor animalis sive … ab anima.` The
ellipsis reads oddly, but it is **Quaracchi's own elliptical text**, not a loss: raw
L108065 ends the column at `…calor animalis sive`, and the page's note 1 records exactly
this — `Cod. K (I a secunda manu) esse, edd. esse vel exire.` The editors flag the missing
verb themselves. **Not a defect; no flag needed.**

## (b) Shared-page footer accounting — 33/33 shared pages CLEAN

Vol IV chunks label apparatus with page-qualified markers (`p{page}-{n}`), which makes the
split mechanically auditable. Built a full claim map across all 74 chunks:

- **No note claimed twice** on any page.
- **No gap** in any page's register — every page runs a contiguous `1 … max`.
- 33 pages are shared between two chunks; three are shared by three chunks
  (p.999, p.1035, p.1053). All split cleanly by body anchor.

### Two-register pages — confirmed NOT double-claimed

Five pages carry two independent footer registers (Lombard littera / commentarius notae
alongside the main numbered register). The chunks namespace them separately, so neither
register is double-claimed:

| page | main register | second register | holder |
|---|---|---|---|
| 968 | 1–7 → `d46-dubia` | `p968n-1..3` (NOTAE AD LIBR. SENTENTIARUM) | `d47-littera` |
| 981 | 1–7 → `d47-dubia` | `p981n-1` | `d48-littera` |
| 983 | 1–3 → `d48-littera` | `p983c-1` | `d48-divisio` |
| 997 | 1–8 → `d48-dubia` | `p997n-1..2` | `d49-p1-littera` |
| 1035 | 1–2 → `d50-p2-littera` | `p1035c-1` (NOTAE AD COMMENTARIUM) | `d50-p1-a1-q1` |

p.968 and p.981 were the two flagged in the brief. **Both confirmed clean — no double
claim in either direction.**

### Pages a chunk covers but claims zero notes on (9 cases) — all correct

`d47-littera`/p.970, `d47-a2-q1`/p.977, `d48-a2-q1`/p.991, `d49-p1-divisio`/pp.999+1000,
`d49-p1-a1-q1`/p.1002, `d49-p1-a1-q4`/p.1008, `d49-p2-s2-a4-q1`/p.1030,
`d50-p1-divisio`/p.1035.

This is the benign pattern where the prior chunk's tail sits above the footnote rule and
carries no anchor, so the page's note 1 legitimately belongs to the receiving chunk. Two
representatives (p.977, p.1008) were verified eyes-on against the bands — see below. Both
correct.

## (c) Cross-page / cross-column footer runover — CLEAN

Programmatic scan of every apparatus definition in the range:

- **No entry lacks terminal punctuation** (i.e. none breaks off mid-sentence unfinished).
- **No page's note 1 begins lowercase or mid-word** (i.e. no unclaimed inbound fragment).

Four runovers were then confirmed eyes-on and are **fully reassembled** in the chunks:

1. **p.976 note 8 → p.977 footer.** p.977's left footer opens with an unnumbered inbound
   fragment (`corporibus nostris corruptibilibus congruunt…`). `d47-a2-q1`'s p976-8
   carries it, joined seamlessly through to `…Superius pro mundi codd. et ed. 1 hominis.`
2. **p.1008 note 7, left → right footer.** Breaks at `Ambros., II. de Officiis ministr.`
   and resumes `c. 5. n. 18: Vita enim beata…`. Correctly joined.
3. **p.1039 note 5, left → right footer.** Breaks mid-word at `post subrepat pro-`,
   resumes `sequitur: qui ad solatium malevolentissimum…`. Correctly joined.
4. **p.1053 note 9, left → right footer.** Breaks at `multo fortius ipse`, resumes
   `remittet, si ab eo petatur venia…`. Correctly joined.

## Pages read at 450 dpi (band verification)

| page | gutter | registers found | chunk claim | verdict |
|---|---|---|---|---|
| 977 | 1530 | inbound frag + 1–2 (L), 3–5 (R) | 5 notes, all `d47-a2-q2` | ✅ verbatim match |
| 1008 | 2077 | 1–7 (L, 7 runs over), 8–10 (R) | 10 notes, all `d49-p1-a1-q5` | ✅ verbatim match |
| 1035 | pre-cut | 1–2 (littera) + NOTAE AD COMMENTARIUM 1 | 2 + `p1035c-1` | ✅ verbatim match |
| 1039 | pre-cut | 1–5 (L, 5 runs over), 6–9 (R) | 9 notes | ✅ verbatim match |
| 1053 | pre-cut | 1–9 (L, 9 runs over), 10–11 (R) | 11 notes | ✅ verbatim match |

Measured gutters match the parity table in `vol4-column-gutter-parity.md` (977 odd → 1530,
in the 1480–1700 band; 1008 even → 2077, in the 2000–2200 band). Bands for pp.1033–1054
were pre-existing and correct; not re-cut.

## Specific items from the brief — all dispositioned

- **p.1039 note count: RESOLVED — the files are right, the prose report was wrong.**
  The register holds **9** notes, not 8. Confirmed eyes-on: left footer 1–5 with note 5
  breaking mid-word at `post subrepat pro-`, completing as an unnumbered fragment opening
  the right footer, then 6, 7, 8, 9. The split is correct in the files:
  `d50-p1-a1-q2` claims notes 1–2, `d50-p1-a1-q3` claims 3–9. **No change needed.**
- **d.46 littera header repair HELD.** `d46-littera` starts at L101428 (the real header),
  not the running-head bleed at L101372. `d45-dubia` ends at L101427 — exactly contiguous,
  so the bleed region is claimed and nothing sits orphaned.
- **d.48 header repair HELD.** `d48-littera` starts at L104392 (the real `Cap. I.`),
  confirmed against raw. The p.981 bleed at L104305 is a page-top running head
  (`DISTINCTIO XLVIII. 981`) sitting inside `d47-dubia`'s range (L104264–104391), which
  correctly owns it. `d47-dubia` ends at L104391 — contiguous, no orphan.
- **d.46 dubia vs d.47 littera on p.968: no double claim.** See the two-register table.

## Note on the apparatus-count audit

Confirmed the brief's warning empirically: because `audit-apparatus-count` compares raw
openers against chunk definitions, the pages whose registers were lost from the raw and
recovered from bands (d.47 pp.972/973/975/979/981; d.48's eight pages; d.49 p.1003;
d.50 pp.1041/1050/1051) cannot be caught by it — when the raw is the empty side it reports
a match. The page-qualified claim map used here is the check that actually covers those
pages, and they are all clean.

## Actions taken

**None.** No chunk file was modified. No defect was found that required a fix.
