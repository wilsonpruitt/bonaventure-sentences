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

## 4. ★ J4 Class D/E — ~38 chunks, the largest genuine item

**Brief already exists: `manual-review/J4-CLASS-DE-HANDOFF.md`.**

~38 chunks carry repeated body anchors. Sampling was **4-for-4 needing repair,
and two had content that was never transcribed at all.** All in published
volumes, so it is reader-facing debt.

**Model split — this is the one item that genuinely needs both tiers:**
- **Triage = Sonnet.** Classify each chunk: is the repeated anchor legitimate
  (a note referenced twice), a duplicate def, or missing content? Mechanical
  against the page bands.
- **Repair = Opus** wherever the finding is *untranslated content*. Restoring a
  dropped passage means writing Latin transcription + literal English, which is
  authored prose — per [[feedback_opus-for-authored-prose]] do not let voice
  consistency degrade on a cheaper tier just because the surrounding task looks
  like cleanup.

The old `J4-HANDOFF.md` was written as a Sonnet brief before the sample came back
4-for-4 with content loss. **Re-read it against that finding before assuming the
routing still holds.**

---

## 5. Cross-page footer runover sweep on Vol IV (Sonnet to run, escalate on finds)

Newly possible: **`seam-screen.py` had no `vol4` entry until 2026-07-28** — it had
never been runnable on Book IV at all. It now is:

```bash
python3.11 tools/seam-screen.py --volume 4 1 50
```

(The `--volume 4 41 50` space form also works now; it previously leaked the flag
value into the positional args and silently scanned d4–d41.)

This is the detection tool for the register's **unquantified corpus-wide
cross-page footer runover class**. Vol V just showed **ten runovers in sixteen
chunks**, which is a strong prior that Vols I–IV carry many undetected ones. The
screen only surfaces candidates — dispositioning each one is eyes-on against the
450 dpi bands.

---

## 6. Assess (do not assume) `--volume 5` for the last two audits (Sonnet)

`audit-paraphrase.py` and `audit-headers.py` still have no Vol V support.
**Assess whether they are worth extending before extending them.** Paraphrase
detection scores word-prefix Jaccard against the raw OCR, and **Vol V's raw is
missing every footnote numeral**, so its baseline is not comparable to the
Sentences — the audit may be structurally uninformative here rather than merely
unimplemented. `audit-apparatus-count.py` is already known to be permanently
blind to Vol V; `check-vol5-apparatus.py` replaces it.

Report the assessment; only implement if it earns it.

---

## Not in scope, deliberately

- **A3 transcription-variant class** (~0.5–1 per page, corpus-wide). Real, but
  unbounded and not a discrete task. Needs Wilson to scope it, not a session to
  start it.
- **The Vol IV d.1–d.40 gutter-parity sampling question.** The `transumtum` case
  proved the old 1880 default produced at least one real corpus error. A sampling
  pass would establish the rate. **Needs Wilson's go-ahead; scope is potentially
  large.**
