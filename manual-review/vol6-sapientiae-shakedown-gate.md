# Vol VI — *Commentarius in librum Sapientiae*, SHAKEDOWN GATE at p. 125 (printed pp. 107–125) — CLOSED

**STATUS: CLOSED 2026-10-16.** Docket ruled by Wilson in one sitting ("all as recommended") → Vol VI rulings 36–43 in `manual-review/vol6-pilot-setup.md`. One defect repaired (2 lines); 4 English lines changed in all; no Latin line changed.

Ruling 34 placed this gate at p. 125, after Capitulum II. Wilson gave the go on 2026-10-15. ⛔ **Per ruling 34 this gate carries
NO deploy** (there is one deploy for the work, at p. 235). Push stays separate and is Wilson's per action.

**Procedure (the `perfectione` / `serm` / Eccl. Cap. I precedent):** a read-only agent compiled the evidence sheet FIRST —
`manual-review/vol6-sapientiae-shakedown-evidence.md` — giving, for each docket item, the site count by chunk over the live
region, the decisive sentence in both languages, the realistic alternatives with a one-line cost, and a recommendation. Wilson
rules in one sitting; the four passes then close.

**Scope: FOUR chunks, pp. 107–125 with no gap, 173 numbered apparatus entries, 8 `tr-` notes.**

| chunk | division / section | type | pages | entries |
|---|---|---|---|---|
| `bon-sap-prooem` | 0 / 1 | prooemium | 107–109 | 22 |
| `bon-sap-prol` | 0 / 2 | expositio | 109–110 | 4 |
| `bon-sap-c1` | 1 / 1 | pericope `"1-15"` | 110–118 | 83 |
| `bon-sap-c2` | 2 / 1 | pericope `"1-25"` | 118–125 | 64 |
| **total** | | | **19 pp.** | **173** |

Every census is over the BUILT files and the RENDERED regions (`## Latin`, `## English`, `## Apparatus`), never over `raw/`.

---

## PASS 1 — live flags: **CLEAN**

`python3.11 tools/check-live-flags.py vol6` → **49 vol6 chunks scanned, no live `[?]`.**

## PASS 2 — style scan + mechanical suite: **CLEAN in scope; one register DEFECT found by census (docket 6a)**

- `polish-style-scan.py`: **2,168 chunks, vol1–vol6** → 11 issues / 6 chunks, all outside Vol VI (10 PAIR Vols III–IV, 1 V5LABEL `bon-hex-c23`). **ZERO in vol6.**
- `check-vol5-apparatus.py --volume=vol6`: **49 chunks, 1,020 entries, 117 known totals — all checks passed**; La = En in all four (22 · 4 · 83 · 64); p. 125 `PENDING n.4–11` (c3's).
- `check-vol5-census.py`: vol5 167/167 · **vol6 49/49**; in scope **9 runovers, all gutter, zero page-crossing.**
- `build-citations.py` (run into the scratchpad; ledger byte-identical to the tracked one): **2,168 chunks → 25,957 records; ours 384; corpus QA 208; ZERO QA flags ours.**
- **La/En digit multiset over all 173 entries: 2 mismatches, both known false positives** (number words: c2 p. 120 n. 2 *tertia*, p. 121 n. 3 *83 Qq.*).
- **Page markers and anchor sequences identical La/En in all four chunks.**
- Site build not run by the read-only agent; run it at the gate's close.

## PASS 3 — boundary sweep: **CLEAN**

Every page 107–125 owned exactly once, each register contiguous 1..N, `KNOWN_TOTALS_VOL6` matching on all 19. Seams: **107** open
(prooem on its display heading) · **109** prooem 1–5 / prol 6–8 · **110** prol 1 / c1 2–7 · **118** c1 1–3 / c2 4–8 · **125** c2 1–3,
nn. 4–11 forwarded to c3. Every outgoing tail is a complete sentence and every incoming body opens on a printed heading; every
hand-off and runover matches the forwarding chunk's Notes and the ledger. No plate was needed for any seam.

**Plates checked for the docket (not for seams):** p. 115 n. 6 reads `Sequitur Iob 6, 2.` (clean, 4×); p. 121 n. 3 reads
`de Doctr. christ. c. 3. n. 4` (clean, 3×).

## PASS 4 — plate cleanup: **DONE 2026-10-16**

To delete: `raw/vision/vol6/p-107…p-124` (18, ~48 MB) · `p-001…p-106` Ecclesiastes leftovers (106, ~206 MB) · pilot extras
(15, ~12 MB) · `/tmp/colcrop/*` (231, ~148 MB) — **~414 MB.** ⚠ **Keep `p-125.png` (~3 MB)** — `bon-sap-c3` opens on it — or
re-extract it for c3.

**Done:** 139 plates deleted from `raw/vision/vol6` (260 MB → 2.1 MB, `p-125.png` kept for c3) and 201 crops from `/tmp/colcrop` (94 MB) — **~352 MB reclaimed** (the draft's ~414 MB estimate pre-dated an earlier partial clean).

---

## THE DOCKET — RULED 2026-10-16

| # | item | recommendation | lines | ruling |
|---|---|---|---|---|
| 1 | `title_la` rule (c1 above-heading; c2 second-below-heading) | ratify as a procedure: first heading below `Capitulum N.`; descend if it governs a run (XIII, XVI, XVIII will); heading above if none below | 0 | **36 — ratified** |
| 2 | c1 p. 115 n. 6 `Iob 6, 2` for Job 6:25 (ledger: Job 6:2 at A) | Latin as printed; En. `[so printed; the verse is Job 6:25]` (`bon-qpe-q4-a1` form); no `[?]`; ledger → resolver docket | 1 | **37 — applied** |
| 3 | c2 p. 121 n. 3 `c. 3. n. 4` for *De doctr. christ.* I.4.4 | same as 2 | 1 | **38 — applied** |
| 4 | marginal `Quaestio.` density — **c1 9, c2 4 by marginale** (Notes/resume say "seven" for c1) | keep ruling 31; add a `### Marginal quaestiones` Notes table from c3 on | 0 | **39 — kept; table from c3; "seven" → nine corrected** |
| 5 | p. 121 n. 2 `ibid. 37, 20` → phantom crossref to p. 118, and Gen 37:20 lost | ruling-14 docket as artefact "2c"; also `d. 38. q. 5. et 6.` (q6 dropped), `[I: Cor.` → `Cor*` | 0 | **40 — to docket** |
| 6a | ⚠ **DEFECT:** c2 English `**Contra:**` ×2 (pp. 123, 125) untranslated, against c1, its own Notes and the formula table | conform to "**On the contrary:**" | 2 | **41 — REPAIRED** |
| 6b | c2 p. 122 *malorum* → "wicked men" | optional → "evil men" | 0/1 | **42 — declined** |
| 6c | c2 Sap 5:6 "hath not shone" vs Eccl. "hath not shined" | optional conform | 0/1 | **42 — declined** |
| 6d | c1 Vers. 16 under `"1-15"` | keep | 0 | kept |
| 6e | c2 roman `Secundo, de iustitia…` heading (brief said italic) | record only | 0 | recorded |
| — | out of scope: deployed Eccl. English `**Contra:**` ×14 / `**Sed contra:**` ×2 | separate decision | (16) | **43 — parked as a scoped job** |

**If all recommendations are taken: 4 English lines change (2 a defect repair); 6 with both options. No Latin line changes.**

## DEFECTS FOUND

1. **`bon-sap-c2` p. 123 and p. 125, English: `**Contra:**` left in Latin** where the house form is "On the contrary:" — and c2's
   own Notes (*"`Cᴏɴᴛʀᴀ:` → `**Contra:**` ("On the contrary:", c1's house form)"*) assert the rendering the text does not have.
2. Documentation only: `bon-sap-c1`'s Notes and the resume note count c1's marginal quaestiones as "seven"; the chunk's own
   marginalia list carries nine `Quaestio` marginalia.

## CLOSE — suite re-run after the edits (2026-10-16)

- live flags: **49 vol6 chunks, none** · apparatus `--volume=vol6`: **49 chunks, 1,020 entries, all passed** (p. 125 PENDING n.4–11, c3's)
- census: **vol6 49/49, rosters agree**, 57 runovers (56 gutter, 1 page)
- style scan: **11 issues / 6 chunks / 2,168 scanned, ZERO in vol6** (unchanged)
- `build-citations.py`: QA **208**, ours 384 records, **`index/citations.tsv` byte-identical** (the edits are English-only brackets and labels; the La. halves are untouched)
- `build-content` → `build-index-json` (1,706 cited, 10,416 backlinks) → `build-content`: **2,167/2,167 translated**

Front advances to `bon-sap-c3`. No push, no deploy (ruling 34: one deploy, at p. 235).
