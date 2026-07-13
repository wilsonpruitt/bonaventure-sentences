# Corpus-wide apparatus backlog — scoping (2026-07-13)

Discovered at the Vol IV d.31–d.40 decade gate. `tools/polish-style-scan.py` was hardcoded
`DIRS = ["vol1","vol2"]` and **never scanned Vol III or Vol IV** — so every "Pass 2 CLEAN" in the
vol3/vol4 gate logs was really reporting `audit-paraphrase.py`. Extended to all four volumes
(commit `0dbd7d2`); the backlog below is what it found.

**None of it is in Vol IV d.31–d.40** (that decade is clean and gated). It is all pre-existing,
in Vol I (2), Vol II (2), Vol III (27), Vol IV d.1–d.28 (32). **Vol III is LIVE**, so part of this
is reader-visible today. **It does NOT block d.41.**

This is **four different jobs**, not one. Do them in this order — cost rises steeply at J4.

---

## J1 — Duplicate apparatus defs: 25 chunks. **SCRIPTABLE, no LLM.** ← highest value, lowest cost

**The defect that actually loses text.** Quaracchi restarts footnote numbering on every printed
page. These chunks rendered that with bare `[^1]`, `[^2]`… so a multi-page chunk ends up with two
or three `[^1]:` definitions. **A body marker can only bind one of them → the rest render as
dropped/duplicated footnotes on the published page.** Worst: `IV-d3-p2-a3-q2` (19 dup),
`III-d27-a1-q4` (16), `III-d29-a1-q1` (16), `IV-d20-p2-dubia` (15), `IV-d6-p1-littera` (15).

**Why it is scriptable:** verified on the sample — in these chunks the **Latin marker sequence,
the English marker sequence, and the apparatus def order are positionally identical**. So relabel
by POSITION; no anchor re-derivation, no PDF, no judgement.

Fix = rename to the page-qualified `[^pNNN-M]` scheme (the convention adopted at d.31 exists
precisely to prevent this). Page attribution: segment the defs by restart (`n <= previous` ⇒ new
page group) and map group *i* → `printed_pages[i]`. **8 of the 25 already satisfy
`len(groups) == len(printed_pages)` exactly** and are a clean auto-run:
`III-d11-a1-q3`, `III-d26-a1-q2`, `IV-d17-p2-dubia`, `IV-d21-p2-dubia`, `IV-d3-p2-a3-q2`,
`IV-d3-p2-dubia`, `IV-d4-p1-dubia`, `IV-d5-a3-q1`.
The other 17 have `groups != pages` — the page-break comments are a tiebreak; where they conflict,
**trust the def-restart pattern** (page-break comments are placed a paragraph early in places).
If page attribution stays ambiguous, fall back to continuous renumbering — uniqueness is what
fixes the render bug; the page number in the label is only metadata.

**Precondition to assert per chunk before writing:** `latin_seq == english_seq == def_order`.
If it fails, kick the chunk to J4.

## J2 — Latin/English anchor mismatch: 9 chunks. **Cheap.**
One or two markers present in one language and not the other. Mirror the missing marker into the
other body at the matching position. Script or a trivial agent pass. No PDF.

## J3 — English body has ZERO apparatus markers: 7 chunks. **Small LLM job, no PDF.**
Footnotes render in the Latin and nowhere in the translation. The Latin anchors show exactly where
they belong; the agent places the mirror markers in the English.
`IV-d12-p1-divisio` (4 defs) · `IV-d14-p1-divisio` (5) · `IV-d15-p1-divisio` (2) ·
`IV-d20-p2-divisio` (3) · `IV-d21-p2-divisio` (3) · `IV-d9-a1-q1` (12) · `IV-d28-a1-q6` (23).
Five are tiny; only the last two carry real weight.

## J4 — Apparatus entries with NO body anchor: 22 chunks, **93 orphaned notes.** **EXPENSIVE.**
The apparatus entry exists but **nothing in either body points to it** — it renders as a dangling
footnote. Verified real, not a convention: `IV-d13-divisio` has **1 marker in its Latin body and 6
apparatus defs** — five codex-variant/source notes with no anchor at all.

Fixing these means going back to the **450 dpi PDF column bands** to find where each superscript
actually sits in the printed text. That is effectively a partial re-promotion per chunk — the same
cost shape as translating a chunk, minus the translation. Budget ~1 agent per chunk with PDF reads.

Worst: `III-d33-dubia` (16 orphaned / 33 defs) · `III-d31-a3-q3` (10/25) · `III-d33-a1-q3` (10/33) ·
`III-d32-a1-q2` (9/21) · `IV-d13-divisio` (5/6) · `IV-d18-p1-a3-q1` (5/14) · `III-d19-dubia` (4/20) ·
`IV-d14-p2-a2-q1` (4/17) · `IV-d16-p1-divisio` (4/6).

---

## Recommended sequencing + model

- **J1 + J2 = one scripted session, no model spend.** Fixes the render-time footnote loss, which is
  the reader-visible harm. Verify with `polish-style-scan.py` + `build-content.mjs` + the marker
  1:1:1 pairing check, then deploy.
- **J3 = one cheap agent session** (7 chunks, no PDF).
- **J4 = its own run, SONNET-shaped** (volume work against the bands; the score is written here —
  per the model-prudence rubric, a cheaper model plays it). Not Opus, not Fable.

**Guard rails for any of these:** every edit must preserve `latin anchors == english anchors ==
apparatus defs` (1:1:1). Re-run `node site/scripts/build-content.mjs` and confirm the translated
count does not move. Back up before rewriting (`_backup-*`), and delete the backups after.
