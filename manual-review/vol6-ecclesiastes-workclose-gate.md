# Vol VI — *Commentarius in Ecclesiasten* WORK-CLOSE GATE (printed pp. 3–103)

Run 2026-10-11, after `bon-eccl-schemata` (`8571e59`), on Wilson's go. Scope: **45 chunks, pp. 3–103, 847
numbered apparatus entries** (`check-vol5-apparatus.py --volume=vol6`). The Cap. I shakedown gate
(`vol6-cap1-shakedown-gate.md`) ran at p. 20; this is the work's second and closing gate.

**Procedure (the *perfectione* procedure): census first, then rulings.** Every disputed term was counted over
the LIVE REGION of every chunk (`## Latin` / `## English` + `## Apparatus`, frontmatter and `## Notes`
stripped), Latin and English side by side, before any question was put. Wilson ruled all items in one sitting
(two rounds), **every one as recommended.** The carry-list was assembled from the resume note's five items
PLUS everything the chunks and the shakedown gate had addressed "to the p. 103 gate" — the resume note's
list was short by five items (heading nest, tr- indexing, p. 11 italics, the exact expositio count, *iucunditas*).

**Result: rulings 20–26 + four housekeeping rulings. 18 rendered lines changed across five chunks; one tool
change (`build-citations.py`); one build change (`build-content.mjs`); one measurement closed.**

---

## Rulings

### Ruling 20 — *poenalitas* → "penalty", *poena* → "punishment" (the majority system)

Census (live region): *poenalitas* → "penalty" ×13 (`prooem`, `scholion`, `c1-v2-7` ×4, `c1-v12-15`, `c12-v1-14` ×5)
against "penality" ×5 (`c7-v24-30` ×3, `schemata` ×2). *poena* → "punishment" in ~40 sites across 15 chunks;
"penalty" only in `c7-v24-30` ×3, `c7-v2-7` ×2, `schemata` ×3. *supplicium* → "punishment" already (4 body sites).
**Applied (10 edits):** `c7-v24-30` — Pars III heading, *vanitate poenalitatis*, *prima poenalitate* → penalty;
*duplex est poena*, membrum I heading, *poena, quae est peccati occasio* → punishment. `schemata` — Schema I's
third member and Schema IV's part-title → penalty; Schema III's `» poena` and Schema IV's two branch roots →
punishment. ⚠ **`c7-v2-7`'s two *poena* → "penalty" sites stand** (legal liability, Mt 5:22 *reus*: "not liable
to any penalty") — outside the vanity triad, ruled as such. *supplicium* shares "punishment" with *poena*, as it
already did in the body; the Schemata's line 552 is the only place they stand near each other.
▶ Cost knowingly accepted: `c7-v24-30` now reads *"the vanity of penalty. And since punishment is twofold"* —
Bonaventure's own shift from *poenalitas* to *poena*, now visible in English.

### Ruling 21 — *mutabilitas* → "mutability" everywhere

"Mutability" ~45 sites incl. `c1-v2-7`'s Pars I heading and five in the Prooemium itself; "changeableness" only in
the triad and Gregory's three species. **Applied (4 edits, not 5):** `prooem` ×3 (*triplex est vanitas, scilicet
mutabilitatis*; *de vanitate mutabilitatis sive naturae*; *tres species vanitatis, scil. mutabilitatis*), `scholion`
×1. ⚠ The census's fifth hit was **"unchangeableness" = *intransmutabilitatis*** (prooem § 4), a different word —
kept. `c12-v1-14`'s "changeableness" = *volubilitas* — kept.

### Ruling 22 — the c12 pairs split to match the Schemata

**Applied (3 edits in `c12-v1-14`):** *commotionem ossium* → "shaking of the bones" (was "trembling", colliding
with *tremor*); *corporis resolutio* → "resolution of the body"; *resolutio venarum* → "resolution of the veins"
(both were "dissolution", colliding with *nervorum dissolutionem*). *signum resolutionis* (p. 94, physiological
"slackening") is not part of the pair and stands.

### Ruling 23 — *iucunditas*: no fixed term

21 Latin sites in 11 chunks; English varies pleasantness / joyfulness / delight / gladness by context. Nothing in
the work sets it against *commodum* (the chain that forced "joyfulness" in *De perfectione evangelica*), so the
`bon-serm` ruling-6 release applies. `c1-v8-11`'s disclosed "pleasantness" stands as a context choice. 0 edits.

### Ruling 24 — translator's notes are NOT indexed

`tools/build-citations.py`: apparatus sections with a `tr-` label are no longer scanned. Ledger **25,584 → 25,573,
exactly 11 records dropped, all `apparatus:tr-*`** (Vol V: `bon-serm-s3` ×3, `bon-serm-tract` ×1 — deployed; Vol VI:
`c1-v16-18`, `c2-v1-3` ×2, `c2-v18-26` ×2, `c7-v11-16`, `c9-v4-10`). QA flags unchanged. Goes live with the deploy.
Closes the shakedown gate's item 5 and corrects the CLAUDE.md `tr-` convention text.

### Ruling 25 — p. 11's italic Scripture: reproduced as printed, CLOSED

Single-leaf exception, no discriminator (the self-quotation hypothesis is dead on p. 16). Ruling 9 governs.
**The exact count the record owed, derived from the built files:** scriptural quotations roman-in-guillemets on
pp. 10 / 12 / 13 = **0 / 11 / 23 = 34**, plus three non-scriptural guillemeted quotations (Aristotle p. 10; the two
*Oritur sol* glosses p. 12). The carried "~58 + 11 ≈ 69" was an over-estimate; the stated floor of 29 held.
⚠ Classification by identification of each quotation's text, not by apparatus pairing — sufficient for a closed
question, not offered as a ledger.

### Ruling 26 — heading depth: keep flat, CLOSED

Deepest nest measured (Schemata depth 7); the Schemata now carry the hierarchy *in uno conspectu*. 0 edits.

### Housekeeping (all as stated)

(a) The Schemata's wording differences (*perpetuitas*/*immutabilitas*, *titulus*/*prologum*, *culpae*/*iniquitatis*)
recorded as printed, not harmonised. (b) The Schemata's 12 printed verse ranges stay out of the scripture index.
(c) **The trailing ` ---` bug fixed in `site/scripts/build-content.mjs`** (`parseApparatus` strips a closing rule):
**961 apparatus entries corpus-wide changed, 960 a pure trim + 1 the ruling-21 edit in `prooem` p. 5 n. 7; zero
entries still end in `---`.** (d) `tr-studium` confirmed as built.

---

## Suite after the rulings

| tool | counted | verdict |
|---|---|---|
| `check-vol5-apparatus.py --volume=vol6` | 45 chunks, 847 entries | all passed |
| `check-vol5-census.py` | vol6 45/45; 48 runovers (47 gutter, 1 page) | rosters agree |
| `polish-style-scan.py` | 2,164 chunks | 11 issues / 6 chunks — the standing Vol III/IV/V baseline, zero ours |
| `check-live-flags.py vol6` | 45 chunks | no live `[?]` |
| `build-citations.py` | 25,573 records (was 25,584) | QA 208 unchanged; −11 = ruling 24 |
| `build-index-json.py` | 1,700 chunks cited, 10,386 backlinks | regenerated |
| `build-content.mjs` | 2,163 / 2,163 translated | built |

**Pass 4 (plates):** none extracted this session; nothing to delete.

**Committed locally; NOT pushed, NOT deployed.** The deploy carries the deploy-only batch, the ruling-24 ledger, the
`---` fix and the `text-reader.tsx` nested-list rendering (first real build). Order: `build-citations.py` →
`build-content.mjs` → `build-index-json.py` → `build-content.mjs` (per the resume note's ordering fix).
