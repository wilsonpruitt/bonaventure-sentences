# Vol II d.11–d.20 — Pre-Promotion Boundary Sweep

**Date:** 2026-05-23 (after d11-divisio promoted).
**Method:** 4 parallel Explore agents reading raw OCR + chunk frontmatter for each distinction's running heads (`DIST. N. (P. X.)? ART. X. QUAEST. Y.`), `DIVISIO TEXTUS`, `TRACTATIO QUAESTIONUM`, `COMMENTARIUS`, `DUBIA CIRCA LITTERAM`, `Cap.` markers. No file edits.
**Purpose:** Catch auto-chunker boundary bugs and dup-ID artifacts before per-chunk Tier-2 promotion, so each session doesn't discover them mid-promotion. Distinct from the d.10-style **decade polish-blocker Pass 3** (cascade-merge splice sweep), which fires after a decade is fully Tier-2.

## Per-distinction findings

### d.11 — CLEAN, promote as-is
- 9 chunks, single-pars, 2×ART × 3×QUAEST + dubia.
- d11-divisio promoted 2026-05-23 (line_start raised 19633→19629 to recover dropped COMMENTARIUS).
- ARTICULUS openers at lines 19658–19661 (Art I) and 20038–20049 (Art II) sit in skeleton-gap between chunks; per locked Vol II convention they fold into the next q1 — extend the receiving chunk's `line_start` at promotion time (same gesture that worked for d.10 throughout).
- **No structural blockers.**

### d.12 — minor `line_start` extensions at promotion
- 9 chunks, single-pars, 2×ART × 3×QUAEST + dubia.
- **d12-divisio:** auto-chunker dropped the COMMENTARIUS IN DISTINCTIONEM XII + *De conditione naturae corporalis.* subtitle + opening prose. Extend `line_start: 20740 → 20733` at promotion.
- **d12-a2-q1:** ARTICULUS II opener at lines 21397–21404 (header + *Circa materiae informatitate.* subtitle + sub-divisio) sits in skeleton-gap. Extend `line_start: 21405 → 21397` at promotion.
- Both fixes are the same gesture used for d11-divisio — no separate re-chunk script needed; just expand on promotion. **No standalone blockers.**

### d.13 — **CRITICAL: a1-q1 contains both q1 AND q2; need to split**
- 8 chunks. Auto-chunker collapsed `DIST. XIII. ART. I. QUAEST. II.` (running head at raw line 22293) into the a1-q1 chunk (currently lines 22053–22436).
- **Action before promoting a.1:** create `bon-sent-II-d13-a1-q2.md` from raw lines 22293–22436; truncate `d13-a1-q1` to lines 22053–22292.
- a2/a3/dubia/littera/divisio boundaries CLEAN.

### d.14 — **HEAVY rationalization: dup-IDs need triage**
1. **`p1-divisio-dup2` (24796–24835) is actually `p2-divisio`** — it contains the P. II DIVISIO TEXTUS + TRACTATIO QUAESTIONUM. **Rename + update id + adjust frontmatter (`pars: 2`, drop `-dup2` suffix).**
2. **`p1-a1-q2-dup2` (24240–24407) is a true duplicate** of canonical `p1-a1-q2` (23961–24143; same content, shifted lines). **Delete.**
3. **`p1-a1-q1-dup2` (24144–24239) is mislabeled** — opens with "An caelum sit figurae orbicularis", which is NOT a1-q1's topic. Needs eyes-on inspection at promotion time; likely belongs to a different article or is a stray fragment. **Investigate, don't delete yet.**
4. **`p2-dubia` + `p2-dubia-dup2` + `p2-dubia-dup3` are three slices of one continuous dubia block** (raw 25805–26203, ~5140 words total) split across OCR page-break re-announcements of the `DUBIA CIRCA LITTERAM MAGISTRI` running head. **Merge into single `p2-dubia` covering 25805–26203; delete dup2 + dup3.**
5. **P. II has no `littera` chunk** in the source (Bonaventure's pars II opens directly with COMMENTARIUS — Lombard's pars II text isn't re-extracted in the Quaracchi printed edition). Genuine absence; do not reconstruct.
- a1/a2/dubia P. I chunks otherwise CLEAN.

### d.15 — minor dubia merge
- 9 chunks listed (`dubia` + `dubia-dup2` are two halves of one block, not a true dup).
- `d15-dubia` (27417–27452) captures the preamble before the `DUBIA CIRCA LITTERAM MAGISTRI` header at 27453; `d15-dubia-dup2` (27453–27615) captures from the header onward.
- **Action:** merge — either extend `d15-dubia`'s `line_end` to 27615 + delete `-dup2`, or extend `-dup2`'s `line_start` to 27417 + delete the original and rename. Cleaner to keep the canonical filename and absorb the dup2 range.
- **a2 genuinely has only q1 + q2** (no a2-q3 running head exists in d.15 range).

### d.16 — **CRITICAL: a1-q2 lost during chunking**
- 7 chunks present (jumps from `a1-q1` straight to `a1-q3`).
- Running head `DIST. XVI. ART. I. QUAEST. II.` at raw line 27980 falls inside a1-q1's body (currently 26314–28074, ~4321 words = a1-q1 + a1-q2 combined).
- **Action before promoting a.1:** truncate `d16-a1-q1` to lines 26314–27979; create `bon-sent-II-d16-a1-q2.md` from lines 27980–28074; verify `d16-a1-q3`'s line_start 28075 lines up.

### d.17 — CLEAN, promote as-is
- 9 chunks, single-pars, 2×ART × 3×QUAEST + dubia. Boundaries align with running heads.
- (Agent's report said "8 chunks" in inventory line but listed 9 with word counts — typo; `ls vol2/bon-sent-II-d17-*.md` confirms 9.)
- **No structural blockers.**

### d.18 — **CRITICAL: dubia chunk missing**
- 8 chunks present; expected 9.
- Raw OCR has a `DUBIUM CIRCA LITTERAM MAGISTRI` block at lines 31978–32016 (~1500 words on Bonaventure's commentary on Lombard's chapter on woman's formation). Auto-chunker line-count algorithm missed it.
- **Action before promoting d.18:** create `bon-sent-II-d18-dubia.md` from raw lines 31978–32016. Frontmatter `type: dubia`, `line_start: 31978`, `line_end: 32016`.

### d.19 — **CRITICAL: littera chunk missing**
- 7 chunks present; expected 8 (no `d19-littera.md`).
- Lombard's `Cap. I.–Cap. VI.` text exists in raw lines 32025–32183 (~550 words), between the `DISTINCTIO XIX.` header and Bonaventure's COMMENTARIUS opener. Auto-chunker skipped it.
- **Action before promoting d.19:** create `bon-sent-II-d19-littera.md` from raw lines 32025–32183. Frontmatter `type: littera`, `line_start: 32025`, `line_end: 32183`. d19-divisio's existing `line_start: 32184` is correct.

### d.20 — CLEAN, promote as-is
- 9 chunks, **single article (`ART. UNICUS`)** with 6 quaestiones, + dubia + littera + divisio.
- Running-head pattern `DIST. XX. ART. UNICUS QUAEST. I.–VI.` confirms no Article II exists. Auto-chunker correctly handled the unicus structure.
- **No structural blockers.**

## Priority blocker list (deal with before promoting affected chunks)

| Distinction | Blocker | Effort | When |
|---|---|---|---|
| d.13 | Split `d13-a1-q1` → `d13-a1-q1` + `d13-a1-q2` at line 22293 | small re-chunk | before promoting d.13 a.1 |
| d.14 | Rename `p1-divisio-dup2` → `p2-divisio`; delete `p1-a1-q2-dup2`; merge p2-dubia ×3; investigate `p1-a1-q1-dup2` | medium triage | before promoting d.14 |
| d.15 | Merge `dubia` + `dubia-dup2` into single canonical | trivial | before promoting d.15 dubia |
| d.16 | Split `d16-a1-q1` → `d16-a1-q1` + `d16-a1-q2` at line 27980 | small re-chunk | before promoting d.16 a.1 |
| d.18 | Create `d18-dubia.md` from raw 31978–32016 | small scaffold | before promoting d.18 dubia |
| d.19 | Create `d19-littera.md` from raw 32025–32183 | small scaffold | before promoting d.19 |

## CLEAN — no pre-promotion fix needed

- d.11, d.17, d.20 (promote each chunk on its own session in normal Vol II workflow).
- d.12 only needs two `line_start` expansions, done naturally at promotion time (same gesture as d11-divisio).

## What this sweep does NOT cover

- Cascade-merge splice detection (the d.10-style decade polish-blocker Pass 3 task). That happens *after* a decade is fully Tier-2, by reading the 450 dpi PDF column bands at each mid-page chunk boundary. This pre-promotion sweep only catches structural / inventory issues from running heads.
- `[?]` flag resolution. That's also part of the post-decade polish-blocker, against 600 dpi PDF.
