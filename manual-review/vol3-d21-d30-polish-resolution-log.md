# Vol III — d.21–d.30 Decade-Polish Gate, PASS 1 of 3: `[?]`-flag resolution

**Date:** 2026-06-11
**Scope:** Vol III, distinctions 21–30 (chunks `bon-sent-III-d21-*` … `bon-sent-III-d30-*`).
**Gate:** First of the three locked-in passes (CLAUDE.md "Polish-blocker cadence"), fired by the close of Vol III d.30 (d30-dubia, commit 5a640e0). Pass 2 (full-corpus style/formatting audit) and Pass 3 (cross-chunk boundary-integrity sweep d.21–d.30) follow separately and remain blockers for d.31+.
**Method:** 600 dpi PDF eyes-on via `pdftoppm -r 600 -f PDF -l PDF -png raw/doctorisseraphic03bona.pdf …`, offset **pdf = printed + 22**. Crops staged under `/tmp/hires/` (footer bands + targeted body-column zooms, all under the API base64 cap).

> **Filename note.** The generic `manual-review/d21-d30-polish-resolution-log.md` is already in use as the **Vol II** d.21–d.30 log (2026-05-30). To avoid clobbering that history this Vol III log follows the established Vol III convention (cf. `vol3-d1-d10-…`, `vol3-d11-d20-polish-resolution-log.md`) and lives at `manual-review/vol3-d21-d30-polish-resolution-log.md`.

---

## Pass 1 — `[?]`-flag dispositions (the nine parked flags + the d27-q6 backfill)

| # | Chunk / location | Disposition |
|---|---|---|
| 1 | `d26-a2-q3` `[^7]` (p.573 n.9) | **RESOLVED @600dpi** (`p573-foot-R.png`). The *Mox pro dirigat … dirigit* clause is the **tail of a regular numbered note n.9** — `⁹ Cap. 7. n. 2. De propos. seq. cfr. infra q. 5; d. 27. a. 1. q. 1. et supra a. 1. q. 1. ad 1. — Mox pro dirigat non pauci codd. dirigit.` — NOT an "n. ad 9" addendum or n.9-bis. The prior def wrongly duplicated n.7's Augustine *Soliloquia* Latin and tagged `(P.573, n. ad 9.)`; def replaced with the true n.9 text, tag → `(P. 573, n. 9.)`. Body anchor on *caritas* (obj. 3) unchanged. |
| 2 | `d26-a2-q4` `[^7]` (p.576 n.3) | **RESOLVED @600dpi** (`p576-foot-L.png`). Footer prints `³ Vide infra d. 34. p. II. a. 2. q. 3.` exactly; cross-ref digits (d.34, p.II, a.2, q.3) confirmed correct. `[?]` removed; def unchanged. |
| 3 | `d27-a1-q2` (p.595 nn.5–11) | **RESOLVED @600dpi → BACKFILL** (`p595-foot-{L,R}.png`, `p595-Lbody-mid.png`, `p595-Rbody-mid.png`, `p595-Rtop.png`, `p595-Rad45.png`, `p595-n9full.png`). The prior "nn.5–11 are unanchored contextual cross-refs" claim was WRONG: each carries a distinct **printed body superscript** — ⁵ *illorum* (Ad-3), ⁶ *diversificari* (Ad-3), ⁷ *regulantur* (Ad-4), ⁸ *distinctione nona* (Ad-4), ⁹ *principalis obiecti* (Ad-5), ¹⁰ *praecedentibus* (Ad-6), ¹¹ *de Moribus Ecclesiae* (Ad-6). All seven were backfilled as `[^20]`–`[^26]` with matching La + En body anchors; apparatus 19 → **26 entries**; status updated. |
| 4 | `d28-a1-q2` `[^12]`,`[^13]` (p.625 nn.7,8) | **RESOLVED @600dpi** (`p625-foot-R.png`, `p625-n78-zoom.png`). n.7: the word edd. 1,2 add after *hinc est, quod caritas* is **`nihil`** (NOT *affectum*), then `Vat. naturalis` → `edd. 1, 2 addunt *nihil,* Vat. *naturalis.*`. n.8: `Mox pro *sub nomine* edd. *sub ratione.*` (also `pauci`→`non pauci codd. omittunt esse`). Both bracketed `[?]` cruxes corrected. |
| 5 | `d28-a1-q3` `[^13]` (p.627 n.9) | **RESOLVED @600dpi** (`p627-foot-R.png`, `p627-n9-zoom.png`/`p627-n9b-zoom.png`). Footer reads `⁹ Edd. addunt *et habilitate* et mox pro *ex hoc non sequitur* exhibent *ex hoc tamen non sequitur.*` Second variant lemma corrected to *ex hoc non sequitur* (from the conservative reconstruction *non sequitur, quod mali sint odiendi*); `[?]` removed. |
| 6 | `d24-littera` ⁶-vs-⁸ on *octavo libro de Trinitate* (p.507) | **RESOLVED @600dpi → ACCEPT (documented edition mis-set)** (`p507-sup8.png`, `p507-quoad.png`, `p507-foot.png`). The printed superscript is unambiguously **⁶** (single closed loop — a 6, not an 8), so it is NOT an OCR slip for ⁸. But by content the clause *octavo libro de Trinitate* is glossed by NOTAE **n.8** (`Libr. VIII. de Trin. c. 4. n. 6.`), while NOTAE **n.6** (`Cap. 4. n. 6. — Pro quo ad…`) is the *quo ad eum videndum* variant — and *quo ad eum videndum* carries **no printed in-text marker** (next printed digit is ⁷ on *diligatur*). This is a genuine **Quaracchi edition-level print mis-set**. Content-correct anchoring retained ([^p507-8] = source citation on *Trinitate*; [^p507-6] = *quo-ad* variant); the ⁶/⁸ discrepancy is documented, not silently emended. |
| 7 | `d30-a1-q5` `[^19]` (p.667 n.9) *ratione[?]* | **RESOLVED @600dpi → ACCEPT (Quaracchi's own printed query)** (`p667-foot-R.png`). The `[?]` is **Quaracchi's OWN printed editorial query mark**, not our transcription ambiguity: the footer prints `…quod homo est animal **ratione [?]** amicis benefaciens et inimicis malefaciens…`, the editors themselves setting `[?]` after *ratione* (they could not certainly read Albert's source). The word IS *ratione*; the `[?]` is reproduced verbatim (re-spaced `ratione [?]` to match the print). Not a flag to clear — a faithful transcription of an editorial query. |
| 8 | `d30-a1-q6` `[^15]` (p.669 n.7) | **RESOLVED @600dpi** (`p669-foot-R.png`). Footer prints `⁷ Ille in lit. Magistri. — Mox post *potest* cod. Z inserit *sic*.` exactly; provisional *inserit sic* confirmed; `[?]` removed. |
| 9a | `d30-dubia` `[^2]` (p.670 n.4) "pag. 311" | **RESOLVED @600dpi** (`p670-foot-L.png`). Footer prints `⁴ Cfr. supra pag. **311**, nota 1. — In fine arg. multi codd. et edd. 1, 2 omittunt *amicum et.*` The cross-ref page **311** is confirmed; reading correct as printed; `[?]` removed. |
| 9b | `d30-dubia` `[^10]` (p.671 n.6) "Codd. Z aa" | **RESOLVED @600dpi** (`p671-foot-R.png`, `p671-n6b-zoom.png`). Footer prints `⁶ Codd. **Z aa** adiungunt *sibi*.` — the second siglum is clearly **aa** (the doubled-minuscule codex siglum cited elsewhere on this page), NOT "ad". Reading correct as printed; `[?]` removed. |

**Tally:** **6 RESOLVED (corrected/confirmed reading)**, **2 ACCEPT-as-printed** (flag #6 documented edition mis-set; flag #7 Quaracchi's own printed query), **1 RESOLVED-via-backfill** (flag #3, 7 new apparatus entries). All nine parked `[?]` markers cleared from the chunk bodies/apparatus; each chunk's `## Notes` carries the disposition.

---

## d27-q6 p.615 footer backfill — verification

The `d27-a2-q6` "p.615 footer backfill (2026-06-11)" restored p.615 nn.1–4 as `[^14]`–`[^17]` (q6's tail share). **VERIFIED at 600 dpi** (`/tmp/hires/p615-foot-L.png`): the p.615 footer sequence runs nn.1–17 contiguously, split by body anchor at the top-of-page q6 tail vs the DUBIA below —
- **n.1** = `…pro in quo potest cod. Z quia potest. Inferius etiam pro iustis omnibus codd. A K Z et edd. iustis hominibus.` → q6 `[^14]` ✓
- **n.2** = `Cfr. August., de Spiritu et littera, c. 36. n. 66.` → q6 `[^15]` ✓ (the d27-dubia stale note's "n.196" was wrong; correct is **n.66**)
- **n.3** = `Hic c. 6.` → q6 `[^16]` ✓
- **n.4** = `Vide scholion ad praecedentem quaest.` → q6 `[^17]` ✓
- **n.5** = `Secundum Aristot., VI. Topic. c. 3. (c. 4.). Vide supra pag. 504, nota 2.` → d27-dubia `[^p615-5]` ✓ (first Dubia note)

The backfill is **correct**. The now-stale open-flag bullet in `d27-dubia` (`[?] q6 p.615 footers nn.1–4 … appear genuinely dropped`) was updated to mark the gap RESOLVED/backfilled and verified; d27-dubia's own apparatus (nn.5–17) was NOT otherwise altered.

---

## Build + audit status

- `cd site && node scripts/build-content.mjs`: parses clean; translated count held at **1186** (resolving flags + backfilling apparatus does not change translated-chunk count).
- Three guard-rail audits `--volume 3 --min-d 21 --max-d 30` (paraphrase / headers / apparatus-count): **no NEW flags**.

**Pass 1 status: CLOSED.** No unresolved `[?]` flags remain in Vol III d.21–d.30. Passes 2 and 3 still pending — d.31+ dispatch remains blocked until all three close.

---

# PASS 2 — Style/formatting audit (full corpus)

**Date:** 2026-06-12.
**Tool:** `tools/audit-style-formatting.py` (extended this session — see below), report at `manual-review/vol3-d21-d30-pass2-style-audit.md`. Streams all Tier-2 chunks across Vol I + Vol II + Vol III (Vol I=406, Vol II=448, Vol III=309 Tier-2; 125 skeletons skipped at the start).

## Tool extensions made this session
- **`-dup2` detection added** to `find_legacy_duplicates` — flags any `<chunk>-dup2.md` whose canonical `<chunk>.md` exists (the auto-chunker class the d.21–d.30 audit surfaced).
- **Scholion-ordering check added** (`scholion_not_last`): for each `## Latin` / `## English`, if a `### Scholion` is followed by any further non-Scholion `### ` subsection, the chunk is flagged — this is the parser-emptying class (`extractLanguageBlock` reads everything after `### Scholion` as scholion).
- Report path/title moved to the Vol III d.21–d.30 convention.

## Checks run (per CLAUDE.md §2)
Required Tier-2 frontmatter (`title_la`, `title_en`, `printed_pages`, `pdf_pages`, `source`, `has_apparatus`, `transcription_status`); `## Latin`/`## English`/`## Apparatus` structure; **apparatus marker pairing** (every `[^N]:` def anchored in BOTH bodies, no orphan body anchors); `### Scholion`-last ordering; page-break `<!-- page N -->` presence; `transcription_status` prefix; legacy/`-dup2`/pars-split duplicates; `**En.**` 4-vs-5 indent mix within a chunk.

## Findings + dispositions

### `-dup2` skeletons (the headline item)
All five in-scope `-dup2` files carried `transcription_status: "auto-chunked 2026-06-02"` with a raw-OCR Latin body, `[Translation pending]` English, and **no apparatus** — i.e. vestigial auto-chunker duplicates. Their canonical siblings are all fully Tier-2 (verified status strings). **Disposition: DELETE (vestigial).** Backed up to `_backup-d21-d30-dup2-pre-delete-20260612/` first, then removed:
- `bon-sent-III-d24-a1-q1-dup2.md`, `…-q2-dup2.md`, `…-q3-dup2.md`
- `bon-sent-III-d25-a1-q1-dup2.md`, `…-q3-dup2.md`

**NOT deleted — out of scope + NOT yet superseded:** the d.34 (`d34-p1-a1-q1/q2/q3-dup2`) and d.39 (`d39-a2-q1/q2/q3-dup2`) dup2 files. For these, BOTH the dup2 AND the canonical are still `auto-chunked` skeletons (d.34/d.39 not yet translated), so they are future-work scaffolds, not vestigial duplicates. Left in place.

### `scholion_not_last` — 1 flag, Vol I, ACCEPT
- `bon-sent-I-d27-p1-a1-q2.md` (Latin + English): carries a `### Anecdota` subsection AFTER `### Scholion` in both bodies. This is the corpus-wide pass earning its keep, but on inspection it is **not a body-emptying defect**: the quaestio body (objections → Respondeo → Epilogus) all precedes the scholion; `### Anecdota` is scholion-adjacent editorial matter (two anecdota fragments + variant readings, with its own `[^25]` anchor) that the parser folds INTO the scholion render — it is displayed, not dropped. Build confirms `hasTranslation: true` for this chunk. It is a **published Vol I** chunk that already passed its own gate; per the "do not bulk-rewrite" rule it is **ACCEPTED as-is** (Anecdota renders within the scholion block). No Vol III chunk has this issue. Flagged here for the record; no edit made.

### `orphan_app_defs` — 2 flags, both ACCEPT (documented no-anchor source-refs)
- `bon-sent-III-d26-a2-q5.md` `[^9]` (in d.21–d.30 scope): the chunk `## Notes` documents this as the genuine **p.579 n.9** footer (Augustine *de Spiritu et anima* + Damascenus tail); it is a footer whose printed superscript anchors the body but whose def the audit reads as orphan because of where the anchor sits — eyes-on confirms the anchor IS present in both bodies (the audit's orphan call is a regex artifact of the very long def). Legitimate; ACCEPT.
- `bon-sent-I-d5-a2-q4.md` `[^11]` (out of scope, Vol I): explicitly documented in its `## Notes` as a **standalone scholion source-reference list** (`Alex. Hal. … Biel`) printed with a marginal Roman-numeral sigil and **carrying no body marker by design**; appended as `[^11]` with an explicit "no body marker" note. Intentional; ACCEPT.

### Everything else: CLEAN
Zero `missing_frontmatter`, zero `missing_section`, zero `status_prefix`, zero `no_page_breaks`, zero `en_indent_mix`, zero `body_anchor_no_def`, zero La↔En anchor mismatches across all 309 Vol III Tier-2 chunks (and Vol I/II). **No mechanical fixes were required** in Vol III beyond the dup2 deletion — the d.21–d.30 chunks are formatting-clean.

**Pass 2 status: CLOSED.** Mechanical action taken: 5 vestigial `-dup2` skeletons deleted (backed up). All other flags dispositioned ACCEPT-with-reason (2 documented no-anchor source-refs; 1 Vol I Anecdota-after-scholion that renders correctly). No substantive guess-fixes.

---

# PASS 3 — Cross-chunk boundary integrity sweep (d.21–d.30, 450 dpi)

**Date:** 2026-06-12.
**Tool:** `tools/seam-screen.py` (extended this session to accept `--volume 3`), `python3.11 tools/seam-screen.py 21 30 --volume 3`. Offset `pdf = printed + 22`; 450 dpi column bands via `extract-pages.py --volume vol3 --dpi 450` + `colcrop.py vol3 <printed>` where eyes-on was warranted.

## Method
The screen walks every adjacent chunk pair in canonical order (littera→divisio→a1-q1→…→dubia), detects shared-page (mid-printed-page) boundaries via `printed_pages` frontmatter, and surfaces the prior chunk's Latin tail + receiving chunk's Latin head, flagging any prior tail that does NOT end on terminal punctuation — **the cascade-merge signature** (the d9-divisio class: a grammatically broken splice in the prior chunk's tail). **88 mid-page boundaries** in d.21–d.30; **2 tail-not-terminal suspects** surfaced.

## Per-boundary verdict
All 88 mid-page seams checked via the screen (continuity of `Secundo/Tertio/… quaeritur` / `Consequenter quaeritur` openers against the prior chunk's TRACTATIO listing + tail closure). **86 CLEAN outright** (prior tail closes on a complete sentence — typically a scholion citation-list section III/IV, an `Et per hoc patent quaesita[^N]` closure, or an `[^N]`-anchored sentence — and the receiving head opens on the expected numbered-quaestio formula).

### The 2 tail-not-terminal suspects — both CLEAN (heuristic false-positive)
- **p.555** `d26-divisio → d26-a1-q1`: the screen sampled `*De spe secundum considerationem absolutam.*` because the divisio's true tail is a `### ARTICULUS` header + its italic title (the screen strips `#` lines). The actual divisio content ends on a complete TRACTATIO listing (`…Quinto quaeritur, utrum in actu suo sit certitudinalis, an dubia.`) matching q1's `…utrum spes sit virtus gratuita`. No content lost. **CLEAN.**
- **p.589** `d27-divisio → d27-a1-q1`: identical pattern — tail sampled as `*De ipsa caritate quantum ad habitum.*` (the `### ARTICULUS I.` title). Divisio's real tail is a complete prose sentence (`…ideo nunc restat determinare alia quatuor sequentia.`) + the full six-fold question listing matching q1's `…utrum caritas sit habitus…`. **CLEAN.**

Both are the expected divisio→a1-q1 artifact (divisio bodies end on an ARTICULUS title), **not** cascade-merge signatures.

### Footer-accounting spot-check at 450 dpi (representative riskier seam)
- **p.492** `d23-a2-q2 → d23-a2-q3` (prior tail ends on argument prose `…habetur sufficientius[^p492-5]`, a footnote-anchored sentence — the riskier non-scholion-list class). Read `colcrop.py vol3 492` R-column footer band: the page's footer sequence runs nn.1–9. **Split verified by body anchor:** q2 owns `[^p492-1..5]` (n.5 = `Vide scholion ad praecedentem quaest.`, matches band); q3 owns `[^p492-6..9]` (n.6 `Vers. 19. — …infra d. 34.`, n.7 `Vers. 17. — Glossa apud Petr. Lombard.`, n.8 `Vers. 24. Cfr. ibid.`, n.9 `Dist. 3. p. I. q. 4.` — all match the band). **All 9 footers fully accounted, no drop or double-count.** Latin continuous (q2 closes `…habetur sufficientius`, q3 opens fresh `Tertio quaeritur de subiecto fidei informis`). **CLEAN.**

Pass 1 had already done 600 dpi footer work on the d.24/d.26/d.27 shared pages (pp.508–517, 573–582, 589–615) and the d.27→d.27-dubia / d.30 footers; that footer discipline is corroborated by this independent p.492 read.

## Cascade-merge dropouts found
**NONE.** No grammatically broken prior-chunk tail anywhere in d.21–d.30. The 2 heuristic suspects were divisio-title artifacts. No `~170-word`-class silent dropout was found; no seam required repair.

**Pass 3 status: CLOSED.** 88/88 mid-page seams verdicted (86 CLEAN, 2 CLEAN-after-inspection); footer-split discipline confirmed at the representative p.492 shared page; zero cascade-merge dropouts.

---

# d.21–d.30 DECADE-POLISH GATE — CLOSED (all 3 passes)

- **Pass 1** (`[?]`-flag resolution): CLOSED (commit `f712e2f`) — 9 flags cleared (6 resolved, 2 accept-as-printed, 1 backfill).
- **Pass 2** (style/formatting, full corpus): CLOSED — 5 vestigial `-dup2` skeletons deleted; all other flags ACCEPT-with-reason; Vol III formatting-clean.
- **Pass 3** (seam integrity, d.21–d.30 @ 450 dpi): CLOSED — 88 mid-page seams clean; zero cascade-merge dropouts.

**Build:** `node scripts/build-content.mjs` → 3 books, **1283 questions, 1186 translated** (question count fell 1288→1283 as the 5 phantom dup2 skeletons were removed; translated count held at 1186). **Audits** `--volume 3 --min-d 21 --max-d 30`: paraphrase 0 critical/0 high; apparatus-count diffs are the standard divisio/littera undercount noise (pre-existing, triage-only); headers `d.25 A-LOSS` is the pre-existing coarse-ARTICULUS-count artifact (present before AND after dup2 deletion; deletion improved the diff −7→−2; d.25 structure a1/a2 × 3 q each is correct and Tier-2). **No NEW flags.**

**d.31 is UNBLOCKED.**
