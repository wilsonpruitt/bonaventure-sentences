# Next session — Vol I polish-blocker (d.41-d.48) + Vol II kickoff

Updated 2026-05-13 at close of d.47+d.48 session.

## 🎉 VOL I COMPLETE — 411/411 questions Tier-2

Head commit `3fffa93`. 13 chunks promoted today (1 dry-run + 4 parallel waves of 3). All d.1-d.48 distinctions complete; site build clean at 411/411.

Major findings from this session:
- d.47 had no auto-chunked Q.II (OCR-garbled `QUAESHO II.` at line 42030) — gap-filled mid-session after wave 1 agent surfaced it.
- d.48 ART.II had no auto-chunked Q.II (OCR-garbled `QLIAESTIO U.` at line 43539) — gap-filled pre-flight.
- d.48 had 4 dubia (I-IV), not the 2 anticipated. Agent verified against PDF.
- d.47 dubia was severely mis-chunked: `p1-dubia` had Q.IV scholion, `p2-dubia` had only DUB.I; rebuilt as 5-dubia chunk (DUB I-V).
- d.48 a1-q2 printed_pages OCR-garbled as `834` (actual 854) — caught post-hoc, fixed.

Audits at commit: 0 critical paraphrase / 0 high (4 false-positive smell flags on descriptive "gap-fill"/"auto-chunked" substrings in status strings). 0 header flags. 0 apparatus flags.

## Decision point — polish-blocker cadence

CLAUDE.md says polish-blocker runs every 10 distinctions (after d.30, d.40, d.50…). Vol I ends at d.48, so the d.41-d.50 blocker is now a **d.41-d.48 blocker** without the full decade.

Carry list: ~30 [?] flags from d.43-d.46 + ~19 new flags from this session's d.47-d.48 promotions. Per-chunk carry log at `manual-review/d41-d50-polish-resolution-log.md`. New flags from today (audit at promotion-time, not full polish-pass):

- d47-littera: 3 [?] (apparatus 5, 6, 8 — codex garbles, Psalm citation)
- d47-a1-q1: 1 [?] (apparatus 15 cod. sigil at p.840)
- d47-a1-q2: 3 [?] (apparatus 12 sentence-cut, Scholion II "Petr. a Tar. hic [?]")
- d47-a1-q3: 2 [?] (apparatus 1 *Iob* citation, 14 garbled cross-ref)
- d47-a1-q4: 2 [?] (apparatus 1 `filios fornicariae`, 13 editorial note)
- d47-dubia: 0
- d47-divisio: 0
- d48-littera: 1 [?] (apparatus 12 corrupt fn 5 tail)
- d48-a1-q1: 3 [?] (Scholion I `q. 45. q. 2`, `sanum`, `modo volendi`)
- d48-a1-q2: 0
- d48-a2-q1: 1 [?] (apparatus 8 cod. column split)
- d48-a2-q2: 3 [?] (body: `velle aliquia velle proprie`, `si Deo placet`, Scholion II `m. 4. § 6.`)
- d48-dubia: 0
- d48-divisio: 0

Total: ~49 flags to disposition.

**Ask Wilson** before next session which path to take:
- (a) Run the d.41-d.48 polish-blocker as the standard 600dpi PDF eyes-on pass before Vol II.
- (b) Defer polish-blocker to a dedicated Vol I closing session and start Vol II Tier-2 first.
- (c) Treat Vol I as KDP-ready immediately (mirror Ambrose Ps 118 single-volume pipeline at `~/wroot-press/`) and run polish as a separate track.

## Open scope nudges (out of this session's commit, future work)

Reported by promotion agents but not actioned:
- d47-a1-q2: `line_end` could be extended ~42255 to formally cover its own apparatus footnotes (currently 42212; Quaracchi p.843 footer entries 9-15 anchor on body in chunk but live past line bound). Cosmetic — apparatus content was still captured.
- d48-a1-q2: agent initially set printed_pages from OCR-garble running head `834` (actual 854). Fixed in this commit. Watch for similar `8`-prefix OCR garbles in vol2.

## After polish (or in parallel) — Vol II kickoff

- Raw OCR for vol2 at `~/bonaventure-sentences/raw/bonaventure_vol2_raw.txt` (verify exists; INDEX QUAESTIONUM TOC starts at vol1-pt2 line 44057, suggests vol2 chunks need new boundaries).
- CLAUDE.md is vol1-scoped; needs a sibling for vol2 with new pt offsets (vol2 pt1/pt2 will have different `pdf_page = printed − N` constants).
- Auto-chunker (`chunk_vol1.py`) needs a vol2 variant.
- Site copy: switch the corpus-status banner from "Vol I in progress" → "Vol I complete" / "Vol II in progress". Live at https://bonaventure.wrootpress.com.
- Wroot Press KDP candidate: Vol I English single-volume — mirror the Ambrose Ps 118 pipeline (513pp, $30, symmetric 0.875" margins after Typst parity-bug fix). Or English+Latin facing-page edition.

## Tools cheat sheet (unchanged)

```bash
# Audit gates (after edits)
python3.11 tools/audit-paraphrase.py --min-d N --max-d N
python3.11 tools/audit-headers.py --min-d N --max-d N
python3.11 tools/audit-apparatus-count.py --min-d N --max-d N

# Build smoke
cd site && node scripts/build-content.mjs
```

pt2 offset: `pdf_page = printed − 410`.
