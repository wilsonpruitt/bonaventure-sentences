# Next-session work queue — Vols I–V cleanup

**Written 2026-07-28.** Self-contained: hand a session **this file** and it can start.
Deeper detail lives in `OPEN-DEFECTS-REGISTER.md` and the per-item briefs named below.

> ### ⚠️ Start this session on **Sonnet**.
> Almost everything queued here is mechanical or well-briefed pattern-following.
> Three items escalate to Opus, and each says so inline with the reason. Nothing
> here is Fable-shaped — the convention decisions were made 2026-07-28 (gate
> cadence) and are already frozen in CLAUDE.md.

**Do items in this order.** 1 and 2 are cheap and unblock the rest; 3 must precede
any work on the `[?]` backlog; 4 is the largest genuine item.

---

## 0. Housekeeping — do first, ~10 minutes (Sonnet)

**0a. Retire two stale register entries.** `OPEN-DEFECTS-REGISTER.md` will mislead
the next reader:
- **C1** (`audit-style-formatting.py` never scans Vol IV) — **false since
  2026-07-13**, and the tool now scans Vol V too. Mark CLOSED.
- **B1** (d.41–d.50 decade gate) — **closed 2026-07-21**. Mark CLOSED.

**0b. Rendered check on the Vol V heading anchor.** `vol5/bon-brev-prol-s6.md`
puts an apparatus marker **inside a `###` heading** (§ 6's title carries n.4 on
*exponendi*) — the first heading anchor in Vol V. Label pairing balances and the
build is clean, but `site/src/app/.../text-reader.tsx`'s heading+subtitle regex has
never been tested against a marker in a heading. **Look at the rendered page.**
Per [[feedback_playwright-over-claude-in-chrome]] use Playwright, not the Chrome
extension. If it renders wrong, the fix is in the reader, not the chunk — do NOT
move the marker out of the heading, because the pairing check depends on it.

---

## 1. Close the Breviloquium Pars I gate (Sonnet)

Passes 1–3 are **already discharged**; only the log and the cleanup remain.

- **Pass 1 — nothing to do.** Zero `[?]` flags across all 16 Vol V chunks.
- **Pass 2 — done, and now decoupled** (runs every commit per the revised cadence).
  Vol V clean on `polish-style-scan.py`, `audit-style-formatting.py`, `seam-screen.py`.
- **Pass 3 — screen clean.** `seam-screen.py --volume 5` → 14 mid-page boundaries,
  0 suspects. `check-vol5-apparatus.py` independently shows all 17 printed pages
  owned 1..N with no gaps. Runover joins are documented per-chunk in `## Notes`.
- **Pass 4 — TO DO:** `rm -f raw/vision/vol5/*.png` (56 MB, regenerable from the
  gitignored PDF at 1–2 min/page). `/tmp/colcrop/vol5-*` already cleared.

**Deliverable:** `manual-review/breviloquium-pars1-polish-resolution-log.md`
recording the above dispositions. Every gate lands a resolution log; this one
doesn't have one yet.

Then the front is **Pars II, opening p.219** — nothing forwarded from p.218, so
the first chunk starts clean. Gutters for p.219+ are NOT measured; measure per page.

---

## 2. Pass-2 style-scan findings — 8 chunks, 14 issues (Sonnet, with one escalation)

Reproduce with `python3.11 tools/polish-style-scan.py`. All pre-existing; none in
Vol V. **Most of these are probably NOT defects** — read the classification before
touching anything.

**⚠ The load-bearing lesson (J3): "unanchored apparatus" is THREE different bugs
that look identical.** (1) genuinely missing English markers → mirror from the
Latin; (2) anchors transcribed as literal Unicode superscripts instead of `[^N]`
→ convert in place; (3) **apparatus filed under the WRONG CHUNK**, already
correctly anchored in the sibling littera → **DELETE the duplicate, do not invent
an anchor.** Always diff against the sibling and verify the sibling is complete
first.

**Class A — likely legitimate, needs annotation not repair (Sonnet).**
Orphaned defs that are *cross-references*, not body notes — e.g.
`III-d31-a3-q3` nn.1–3 are `Vide supra d. 28. q. 6.` / `Vide scholion ad
praecedentem quaest.` / `Cfr. supra d. 29. q. 3.` This is an **established
documented class**: `III-d5-a2-q4`'s orphan carries the explicit marker
`*(Scholion source-reference — no body marker.)*`, and **14 chunks corpus-wide**
already carry that annotation. Verify each against the printed page, then annotate
to match the existing convention.
- `III-d31-a3-q3` (nn. 1, 2, 3) · `III-d32-a1-q2` (nn. 13, 14) ·
  `III-d5-a2-q4` (n. 11, already annotated — confirm and leave) ·
  `IV-d14-p2-a2-q1` (nn. 15, 17) · `IV-d16-p2-a2-q2` (n. 6)

**Class B — small and real (Sonnet).**
- `IV-d1-p2-a2-q2` — def `[^2b]` anchored in **Latin only**, not English. Mirror it.
- `IV-d1-p1-littera` — no `<!-- page N -->` markers at all. Add from the frontmatter
  page span, verified against the raw.
- `IV-d16-p2-a2-q2` — a literal `[^p408-N]` token sits in `## Notes` prose, where
  it *describes* the label convention. Harmless to readers (Notes is unrendered)
  but it breaks pairing checks. Quote it without the bracket-caret.

**Class C — ★ ESCALATE TO OPUS.**
- `III-d15-divisio` — **5 apparatus defs, ZERO body anchors.** An entire apparatus
  block with nothing pointing at it, on a **live, reader-facing page**. Labels are
  `p329-1..3` plus `notae-1`, `notae-2`. This has the exact signature of J3's
  bug (3) — a divisio holding notes that answer to superscripts printed in
  Lombard's littera above the COMMENTARIUS heading. **Diff against
  `III-d15-littera` before doing anything**, and if they duplicate, delete rather
  than anchor. Deleting text is judgment work and it is published; do not let a
  cheaper tier decide it.

---

## 3. Re-derive the `[?]` flag count — BEFORE any A1 work (Sonnet)

The register's headline figure is **~108 unresolved `[?]` flags in reader-facing
text** (§A1). **That number is not trustworthy** — the register says so itself at
line ~208: it is contaminated the same way the J4 false positive was, by
backtick-quoted `[^N]` ranges and `[?]` tokens sitting in prose that never renders.

**Do the recount first.** Exclude: anything inside `## Notes` (never rendered —
`notes` is only a type field in `site/src/lib/content.ts:20`, no component reads
it), anything inside backticks, and anything in a `manual-review/` log. What
survives is the real reader-facing number. Budget A1 against *that*, not 108.

---

## 4. ~~J4 Class D/E — ~38 chunks~~ — **ALREADY CLOSED, discovered 2026-07-28**

**This item was stale — do not redo it.** It read as still-open here and in the
resume note, but the actual repair happened across 11 batches on 2026-07-17
(commits `1bb6220`..`d6811a2`, plus `81ca91c`), before this queue was even
written. A fresh corpus health-scan (2026-07-28) confirms: `fix-apparatus-labels.py`
reports 0 FIXABLE/0 SKIPPED corpus-wide, only 8 chunks remain flagged by the
strict scan, and every one is a documented deliberate disposition (2 benign
double-anchor cases, 5 refused duplicate/cross-ref cases handled under item 2's
Class A this session) **except one: `III-d15-divisio`**, which is the Class C
escalation from item 2, not Class D/E. See `OPEN-DEFECTS-REGISTER.md` § A2 for
the full accounting. **The only real Opus-shaped work left in this whole area is
that single Class C chunk** — see the register's top section / the resume note
for its handoff. There is no batch of untranslated content to restore.

---

## 5. ✅ Cross-page footer runover sweep on Vol IV — DONE 2026-07-28 (Sonnet)

```bash
python3.11 tools/seam-screen.py --volume 4 1 50
```
517 mid-page boundaries screened; **1 suspect, verified a tool false positive**
(`IV-d17-p1-a2-q1` → `-q2`: the screen grabbed the chunk's `## Notes` hand-off
text as "tail" instead of the actual last body sentence, which is complete and
grammatically terminal; q2's opening is already correctly documented in q1's own
Notes). **No real runovers found in Vol IV** — the Vol V ten-in-sixteen rate does
not generalize here, at least not via this detection method. Nothing further to do.

---

## 6. ✅ Assessed `--volume 5` for the last two audits — NOT extending (Sonnet)

**Assessment: not worth extending now.** `audit-paraphrase.py` scores 5-char
word-prefix Jaccard, which tolerates trailing OCR garble but not a stray glyph
corrupting a word's first few characters — a real but narrow risk given Vol V's
documented phantom-anchor glyphs (c6's lesson), and made worse by Vol V's small
per-chunk word count (one capitulum, not a whole distinction), where a few bad
prefixes could swing a chunk's score more than in the Sentences. `audit-headers.py`
counts QUAESTIO/ARTICULUS/DUBIA vocabulary that doesn't exist in the Breviloquium
(Cap./§ instead) — extending it is a real reimplementation, not a `--volume` flag.
Given `seam-screen.py --volume 5` and `check-vol5-apparatus.py` already cover
boundary and footer-ownership integrity for Vol V, and every chunk goes through
mandatory bands-first eyes-on verification regardless, the marginal value of
these two audits here is low. **Revisit only if the Hexaemeron's reportatio
register (larger volume, own mini-pilot) turns out to need less-supervised,
audit-driven triage** — the calculus may differ there.

---

## Not in scope, deliberately

- **A3 transcription-variant class** (~0.5–1 per page, corpus-wide). Real, but
  unbounded and not a discrete task. Needs Wilson to scope it, not a session to
  start it.
- **The Vol IV d.1–d.40 gutter-parity sampling question.** The `transumtum` case
  proved the old 1880 default produced at least one real corpus error. A sampling
  pass would establish the rate. **Needs Wilson's go-ahead; scope is potentially
  large.**
