# Manual Review Queue — Vol I boundary issues

_Generated 2026-04-17 from `tools/boundary-audit.py` after automated cleanup passes._
_Sources: `vol1/boundary-audit-pt1.json`, `vol1/boundary-audit-pt2.json`._

## How to use this queue

For each `[ ]` item: fill in the underlined slots as you find the answer, then check `[x]`. When a distinction's slots are filled, run the helper:

```bash
python3.11 tools/manual-fill.py --part {1|2} --chunk-id bon-sent-I-dNN-type --type {littera|divisio|dubia} --lines START-END
```

The helper writes the skeleton from the raw text. Then re-audit: `python3.11 tools/boundary-audit.py --part {1|2}`.

**Where to look:**
- PDF: `raw/doctorisseraphic11bona.pdf` (pt1, printed page = PDF page − 102) or `raw/doctorisseraphic12bona.pdf` (pt2)
- Raw text: `raw/bonaventure_vol1_raw.txt` (pt1) or `raw/bonaventure_vol1_pt2_raw.txt` (pt2)
- Use `grep -n "<distinctive phrase>" raw/...` to match a PDF passage to a raw line number.

---

## Status

| Pass | pt1 | pt2 |
|---|---:|---:|
| Before automation | 89 issues, 2 clean | 44 issues, 7 clean |
| After automation passes (2026-04-17) | 49 issues, 9 clean | 8 issues, 17 clean |

---

## A. pt2 missing divisios (4 chunks)

No COMMENTARIUS / DIVISIO TEXTUS marker in raw — locate Divisio Textus section manually from PDF.

- [ ] **d.30 divisio** — printed pages ______ · PDF pages ______ · lines ______–______  
      (littera occupies 10160–10377; divisio lives somewhere between divisio-end and first quaestio at line 10378)
- [ ] **d.43 divisio** — printed pages ______ · PDF pages ______ · lines ______–______  
      (littera 33889–34230; first quaestio at 34238 — divisio is in that gap)
- [ ] **d.44 divisio** — printed pages ______ · PDF pages ______ · lines ______–______  
      (littera 35693–35889; first quaestio at 35890 — divisio absent or embedded)
- [ ] **d.46 divisio** — printed pages ______ · PDF pages ______ · lines ______–______  
      (littera 39069–39654; first quaestio at 39662 — minimal gap, verify)

---

## B. pt2 pars-transition gaps (4 chunks)

Content between end of one pars and start of next. Usually the next pars's commentarius intro + divisio block. Decide: absorb into next pars's divisio, or create a dedicated `p{K}-intro` chunk.

- [ ] **d.27 gap (lines 6282–6359, 78 lines)** — decision: ☐ absorb into `d27-p2-divisio` · ☐ new `d27-p2-intro` · ☐ other: ______
- [ ] **d.31 gap (lines 12049–12165, 117 lines)** — decision: ☐ absorb · ☐ new intro · ☐ other: ______
- [ ] **d.37 gap (lines 23034–23365, 332 lines)** — ⚠ sequence jumps p1 → p3; verify pars count first (see Task C). Decision: ______
- [ ] **d.40 gap (lines 29715–29878, 164 lines)** — ⚠ sequence jumps p3 → p1-a4; verify pars structure first (see Task C). Decision: ______

---

## C. pt2 pars-count verification (2 distinctions)

`-dup`-based auto-labeling may have over-split. Check PDF table of contents for each distinction.

- [ ] **d.37** — auto-labeled 4 pars. Actual pars count from PDF: ______  
      If fewer: which `-p{K}-` chunks to merge? ______  
      Files currently labeled p1: d37-p1-divisio, d37-p1-a1-q1, d37-p1-a1-q2, d37-p1-a2-q1, d37-p1-a2-q2, d37-p1-a2-q3, d37-p1-dubia  
      Files p2: d37-p2-divisio, d37-p2-a2-q1, d37-p2-a2-q2, d37-p2-a2-q3, d37-p2-dubia  
      Files p3: d37-p3-a2-q1  
      Files p4: d37-p4-a2-q1
- [ ] **d.40** — auto-labeled 3 pars. Actual pars count from PDF: ______  
      The sequence `d40-p3-a1-q1` (29358–29714) then `d40-p1-a4-q2` (29879–30214) is suspicious.  
      Files p1: d40-p1-divisio, d40-p1-a1-q1, d40-p1-a1-q2, d40-p1-a4-q2  
      Files p2: d40-p2-divisio, d40-p2-a1-q1  
      Files p3: d40-p3-a1-q1  
      Fix: ______

---

## D. pt1 d.13–19 multi-pars mess (biggest block)

These chunks were created before the current pipeline and have inconsistent boundaries. Option: delete and re-run auto-chunk + pars-relabel for just this range, then compare.

- [ ] **d.13** — OVERLAP 231 lines (`d13-a1-q2` ↔ `d13-a1-q3`); `d13-a1-q3` starts mid-content at line 44588. Real start line: ______
- [ ] **d.14** — `d14-a2-q2` mid-content at line 46569. Real start line: ______
- [ ] **d.15** — `p1-a1-q1` mid-content at 47854; `p2-a1-q3` starts at running head (49948); GAPs 341 + 411 lines. Fix plan: ______
- [ ] **d.16** — `a1-q3` mid-content at 51429; OVERLAP 288; GAPs 1058 + 359. Fix plan: ______
- [ ] **d.17** — **NO CHUNKS AT ALL.** DISTINCTIO XVII OCR-garbled in raw.  
      Real DISTINCTIO XVII line: ______  
      End line (start of d.18): ______  
      After filling: run `auto-chunk-volume.py --part 1 --min-dist 17 --max-dist 17` (add max-dist flag first) or manual skeleton.
- [ ] **d.18** — MISSING divisio; stale `d18-a1-q5-v2` file; OVERLAP 1079 lines; 2 UNCOVERED QUAESTIOs (lines 57308, 57809).  
      Divisio lines ______–______  
      Resolve `-v2` file: ☐ delete · ☐ rename · ☐ merge
- [ ] **d.19** — 6 mid-content starts, 3 OVERLAPs (368/916/232), 1 GAP 626. Multi-pars p0/p1/p2. Fix plan: ______

---

## E. pt1 d.20–23 running-head false starts (minor)

- [ ] **d.20** — GAP 285 lines between `a1-q2` (end 64637) and `a2-q2` (start 64922). Real `a2-q1` line or decision: ______
- [ ] **d.21** — `a2-q1` mid-content (66347); `q2` mid-content (66012); UNCOVERED QUAESTIO I at 65757. Fix: ______
- [ ] **d.22** — `q0` mid-content (67497); OVERLAP 212 lines. Fix: ______
- [ ] **d.23** — `a1-q2`, `a1-q3` both start at running heads. Real start lines: q2=______, q3=______

---

## F. Known false positives (no action needed)

- **d.1** MISSING divisio — Tier-2 d.1 embeds divisio inline in `d1-a1-q1`, not a separate file. Harmless.
- **d.10** GAP 38662 lines — `d10-a1-q1` is Tier-2 without line metadata, audit math breaks. Harmless.
- **d.12** UNCOVERED QUAESTIO at 42148 — `d12-divisio` covers indirectly via tractatio listing. Cosmetic.
- **d.9-dubia-v2.md** — stale legacy duplicate of `d9-dubia.md`. Safe to delete.

---

## Reference

**Tools built this pass:**
- `tools/chunk-trim.py` — shrinks chunks leaking into sub-markers (Tier-2 safe)
- `tools/chunk-fill.py` — auto-creates missing chunks from raw markers
- `tools/pars-relabel.py` — `-dup{N}` → `-p{N}-`
- `tools/manual-fill.py` — write skeleton from a manually-found line range (for the `[ ]` items above)
- `tools/auto-chunk-volume.py` — `--min-dist`, duplicate-ID suffixing, OCR-tolerant regex
- `tools/boundary-audit.py` — `--part {1|2}`, ROMAN through XLVIII, Tier-2 false-positive suppression

**Reproducible automated pipeline:** delete pt2 chunks → auto-chunk → pars-relabel → chunk-trim → chunk-fill → chunk-trim again → audit.

**Recommended order:**
1. Fill A's 4 divisios (fastest wins).
2. Verify C's pars counts (unblocks B).
3. Resolve B's transition gaps.
4. Find d.17 + fix d.18 (D).
5. Clean d.19, d.13–16 (D) — hardest.
6. Fix d.20–23 running heads (E).
7. Vision-clean Latin bodies per distinction in session.
