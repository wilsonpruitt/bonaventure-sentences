# d.41–d.44 — VOL II decade polish-blocker resolution log

> **This is the VOLUME II log.** It records the Vol II (`book: 2`, `bon-sent-II-…`) decade polish dispositions for the final segment d.41–d.44 (Vol II ends at d.44). Distinct from any Volume I decade log.

Decade segment: **Vol II d.41 → d.44** (Vol II's last distinction is d.44). Polish performed **2026-06-01**.

Vol II offset: `pdf_page = printed_page + 22`. Raw OCR: `raw/bonaventure_vol2_raw.txt`. 600 dpi reads via `tools/extract-pages.py --volume vol2 --pages N --dpi 600` + `tools/colcrop.py` (full-page bottom-corner crops via PIL for the column-foot footnote tails that overflow the colcrop bands).

---

## Pass 1 — `[?]` flag resolution + apparatus-gap fixes (600 dpi eyes-on)

Five genuine open items adjudicated. Three were FIX (real apparatus gaps / mis-attributions corrected), one ACCEPT-ILLEGIBLE, one confirmed-already-clean (no change). All five carried PDF eyes-on at 600 dpi.

### 1. d43-littera vs d43-divisio — p.981 orphaned littera markers (CONFLICT adjudicated) — **RESOLVE / FIX**

**The conflict.** `d43-littera` carried a `[?]` saying the three p.981 littera-tail superscripts (¹ after *de Spiritu sancto*, ² after *qui peccat in Spiritum sanctum*, ³ after *superius … dictum est*) were unannotated (speculating an Ambrose *de Spir. sancto* note). `d43-divisio` claimed those same three markers as the left-column `NOTAE AD COMMENTARIUM` it rendered as `[^4]`–`[^6]` (*definitivam / peccant / superius*).

**600 dpi p.981 (PDF 1003), L/R footer bands.** The page foot holds a **single** footer block headed `NOTAE AD COMMENTARIUM`, split across the two columns — there is **no** separate `Notae ad Libr. Sententiarum` block on p.981. The **left** column of that block annotates exactly the three littera-tail superscripts:
- ¹ `Libr. I. c. 3. n. 54. … — Pro definitam Bonav. legit definitivam.` (Ambrose, *De Spiritu Sancto* Lib. I c. 3 n. 54 — the *de Spiritu sancto* source; the *definitam→definitivam* is a secondary editorial remark on the commentary lemma)
- ² `Codd., excepto D, peccant.` (on *qui peccat in Spiritum sanctum*)
- ³ `Libr. I. d. XXXIV. c. 4.` (the *superius dictum est* cross-reference)

So **d43-divisio was correct** and **d43-littera's `[?]` was wrong** (the markers ARE annotated, by what divisio renders as `[^4]`–`[^6]`; Quaracchi grouped the littera-tail notes into the commentary's single NOTAE block on the shared page).

**Fix.** (a) d43-littera: replaced the stale `[?]` block with a RESOLVED cross-reference note (3 markers ↔ d43-divisio `[^4]`–`[^6]`; markers stay plain text in the littera body to avoid orphans, since the defs live in divisio); removed the `[?]` clause from its `transcription_status`. (b) d43-divisio: corrected its apparatus-intro prose, which had mislabeled the first left-column anchor as *definitivam* — its true anchor is *de Spiritu sancto* (Ambrose), with *definitivam* a secondary remark; added the 600 dpi confirmation that there is no stray littera-note block. The two chunks now agree.

### 2. d44-a3-q2 `[^2]` (Luc. 10:16) illegible tail — **ACCEPT-ILLEGIBLE**

**600 dpi p.1012 (PDF 1034), L-col footer band + full-page bottom-left crop.** Footer ⁵ reads `Luc. 10, 16. — In fine arg. non pauci codd. cum edd.` and is the **last line of the left-column footer block**, with blank space below it. The continuation does **not** appear at the top of the right-column footer block (which begins directly with the *praelatis a Deo institutis* variant = footer 6) nor anywhere on the plate. The IA djvu OCR (raw line 70312) truncates at the identical point (`cum edd.`). The variant reading the note introduces is therefore unrecoverable from any available source.

**Disposition.** Formally ACCEPT-ILLEGIBLE. Removed the `[?]` token from the apparatus body; the entry now reproduces the legible portion with an explanatory ellipsis (no fabricated continuation). Marker anchor confirmed at *alibi* in both bodies. The chunk's `## Notes` flag block updated to record the resolution.

### 3. d44-a3-q1 — missing p.1012 reply-5 footnote definitions — **FIX** (added 3 apparatus entries `[^28]`–`[^30]`)

**600 dpi p.1012 (PDF 1034), L-0 (body) + L-2/L-3 (footer band).** a3-q1's reply 4 tail + reply 5 print at the **top of p.1012 L-col** (the page break falls inside reply 4 at *ad Timotheum se-/cundo*). The p.1012 L-col footers **1–3** anchor in a3-q1's body, not a3-q2's:
- footer 1 = `Vers. 2` → reply 4 *ad Timotheum secundo* (1 Tim 2:2) → **`[^28]`**
- footer 2 = `Rom. 8, 21. 22: Quia et ipsa creatura…usque adhuc.` → reply 5 *filiorum Dei* → **`[^29]`**
- footer 3 = `Vers. 24` → reply 5 *Matthaei sexto: Non potestis duobus dominis servire* (Matt 6:24) → **`[^30]`**

These three were never defined in a3-q1 (its apparatus stopped at `[^27]` / p.1011). **Fix.** Added defs `[^28]`–`[^30]` (La + En) and placed the three body markers in both the Latin and English bodies at the positions above. No collision with a3-q2 (whose apparatus correctly begins at p.1012 footer 4 = its `[^1]`). Updated a3-q1's `transcription_status` (27 → 30 entries), its Apparatus page-split map, and corrected the stale hand-off note that had wrongly claimed "the whole p.1012 footer block is a3-q2's" and "a3-q2 has no scholion" (a3-q2 does have its own scholion; that chunk carries `has_scholion: true`).

### 4. d44-a3-q1 `[^1]` (August. *de Civ. Dei* XIX c.15) body anchor — **CONFIRMED CLEAN (no structural change; provenance documented)**

The brief's premise (no matching body marker) was **stale**: `[^1]` already has paired anchors at *potentiae* / *the power* (ARTICULUS III opener) in both bodies.

**600 dpi p.1009 (PDF 1031), R-0 (body) + R-2 (footer band).** Footer **⁴** (= a3-q1's `[^1]`, de Civ. Dei XIX c.15 `Nullus autem natura… — Vide scholion ad praecedentem quaest.`) prints its superscript on the word ***conservari***, the LAST word of **a2-q2**'s Ad-4 reply (`…ubi ordo habet perturbari et potest per dominium conservari⁴.`), immediately before the `ARTICULUS III` header. So the footer's true textual home is a2-q2's tail; a2-q2 explicitly **forwarded** it (its Notes: "p.1009 R-col footers 4–9 belong to ARTICULUS III / a3-q1 — forwarded, NOT claimed here"), and a3-q1 picked it up as the lead `[^1]` of the inherited R-col block, anchored to the opener's *potentiae*.

**Disposition.** No structural change — the marker is present and paired in exactly one chunk (a3-q1), with a matching def; a2-q2 does not also carry it (no duplicate). The cross-chunk provenance (true anchor = a2-q2's *conservari*) is now documented on the a3-q1 side with the 600 dpi citation. Marker pairing clean.

### 5. d44-littera `[^1]` vs d43-dubia `[^16]` duplicate (the *Cfr. infra d.44 … infirmus esse* footer), p.998 — **FIX** (removed the duplicate from d44-littera; renumbered)

**600 dpi p.998 (PDF 1020), L-1/L-2 (body+footer bands), R-0/R-2 (body+footer band).** The brief speculated the footer's true home was the d44-littera CAP. I anchor; **the 600 dpi read shows the opposite.** Findings:
- The footer's variant lemma ***infirmus esse*** appears **only in DUB. IV** (`…potest deficere et infirmus esse`, d43-dubia) — it is **nowhere in the CAP. I littera** (whose quoted block ends at *facultate*).
- The footer sits in the p.998 **L-col** footnote block (the DUB. III/IV column: ¹ Alex. Hal., ² *Cfr. infra d.44 … infirmus esse*, ³ Aristot. III Ethic., ⁴ Art. 2 q.1) — **not** in the R-col `NOTAE AD LIBR. SENTENTIARUM` block.
- The CAP. I littera's own footers are the THREE R-col `NOTAE AD LIBR. SENTENTIARUM` entries: ¹ Fulgentius *de Fide ad Petrum* c.3 n.34 (*parari et tribui* variant, anchoring the Fulgentius quote at *facultate*); ² Rom 13:1 + Ioan 19:11 + Glossa (at *Apostolus*); ³ Enarr. in Ps. 32 / Job 1:11 (at *Augustinus*).

So **d44-littera had the wrong note as its `[^1]`** (a duplicate of d43-dubia's `[^16]`), anchored at *facultate*, AND a spurious marker on *monstratur* (which has no footer). d43-dubia's `[^16]` is correct (anchored at *potentia* in the DUB. IV body, its true home).

**Fix (d44-littera only — d43-dubia needed no change):**
- Removed the bogus `[^1]` (DUB. IV note) entirely.
- Deleted the body marker that had sat on *monstratur* (no footer annotates it).
- Re-pointed `facultate` to the Fulgentius note (now `[^1]`); *Apostolus* → Rom 13:1 (`[^2]`); *Augustinus* → Enarr. Ps. 32 (`[^3]`).
- Renumbered all subsequent markers + defs down by one (old `[^2]`–`[^9]` → `[^1]`–`[^8]`); total 9 → 8 entries.
- Updated `transcription_status`, page-split map, and apparatus-split notes. Added a confirming note to d43-dubia's `## Notes` that `[^16]` is correctly its own and that the d44-littera duplicate was removed.

No duplicate remains; both chunks agree the note lives in d43-dubia.

---

## Final verification

- **Marker pairing** (edited body chunks): `d44-littera` defs 1–8 — La==En==defs, 0 orphans; `d44-a3-q1` defs 1–30 — La==En==defs, 0 orphans; `d44-a3-q2` defs 1–20 — La==En==defs, 0 orphans. (`d43-littera`, `d43-divisio`, `d43-dubia`: Notes-only / prose edits, body markers unchanged and previously paired.)
- **Smoke build** `node site/scripts/build-content.mjs`: `2 book(s), 875 questions, 875 translated` — parses cleanly.
- **`audit-paraphrase.py --volume 2 --min-d 43 --max-d 44`:** 18 chunks, 0 critical / 0 high.
- **`audit-apparatus-count.py --volume 2 --min-d 43 --max-d 44`:** 0 flagged.
- **`audit-headers.py --volume 2 --min-d 43 --max-d 44`:** no LOSS flags (per-distinction rows empty for this range — the known-coarse Vol II header audit; not a regression).

**Chunks edited this pass:** `d43-littera`, `d43-divisio`, `d43-dubia`, `d44-littera`, `d44-a3-q1`, `d44-a3-q2` (+ `content.json`).

**New `[?]` left:** none. (Item 2's `[^2]` Luc. 10:16 tail is formally ACCEPT-ILLEGIBLE — the `[?]` token was removed and replaced with an explanatory ellipsis + Notes disposition.)

**Note:** d.44 is the last distinction of Vol II; there is no d.50 polish gate beyond this. When Vol II ships, update landing/About copy per MEMORY.md `update-about-copy-after-vol2`.

---

## Pass 2 — full-corpus style/formatting audit (2026-06-01)

Programmatic scan over **every Tier-2 chunk** (`transcription_status` starts with `Phase C Tier 2 complete —`) in both `vol1/` and `vol2/`. This is the corpus-wide drift check (not last-decade-only): its purpose is to keep formatting drift from compounding as new chunks are added. Script: `/tmp/pass2_audit.py`.

**Scanned: 874 Tier-2 chunks (vol1 = 410, vol2 = 464).**

### Per-check results

| Check | Result |
|---|---|
| 1. Required frontmatter (`title_la`/`title_en`/`printed_pages`/`pdf_pages`/`source`/`has_apparatus`/`transcription_status`/`id`/`type`) | **0 violations** |
| 2. Structure (`## Latin`, `## English`, `## Apparatus` when `has_apparatus`) | **0 violations** |
| 3. Apparatus marker pairing | 14 entries flagged — all FALSE POSITIVE (per-page footnote-number restart; see below) |
| 4. Page-break presence (`<!-- page N -->` in Latin) | **0 violations** |
| 5. `transcription_status` exact prefix `Phase C Tier 2 complete —` | **0 violations** |
| 6. `title_en` not bloated (no `I/II Sent.,` / `d. N` breadcrumb prefix) | **0 violations** |
| 7. `**En.**` 4-vs-5(vs-6)-space intra-file indent mixing | 1 violation — **FIXED** |
| 8. Legacy auto-chunked `dN-divisio` superseded by `dN-p1/p2-divisio` | **0 violations** |

### FIXED

- **`d9-littera` (vol2) — check 7, mixed `**En.**` continuation indents.** Apparatus entries `[^1]`–`[^9]` used a 5-space continuation indent; `[^10]`–`[^18]` used 6 spaces. Per CLAUDE.md the corpus convention is 5 spaces (4 also accepted; 6 is non-standard). Normalized the 18→ the nine 6-space lines down to 5 spaces (mechanical, `perl -i -pe`), so the whole file is uniform 5-space. The `[^N]:` defs themselves were already at column 0; only the `**En.**` line indents changed. Build re-parses cleanly (parser is indent-tolerant; this is hygiene, not a parse fix).

### FLAGGED / ACCEPTED (no change)

- **Check 3 — 14 "duplicate def" flags across `d38-a1-q1` (`[^1]`–`[^7]` ×2) and `d42-a2-q1` (`[^2]`–`[^8]` ×2): ACCEPTED, false positive.** Quaracchi restarts footnote numbering on each printed page, so a multi-page chunk legitimately carries two `[^1]…[^N]` sequences. Both chunks span 3 printed pages (`d38-a1-q1` = pp.881–883; `d42-a2-q1` = pp.964–966) and the build parser maps the repeated markers positionally. This is the documented per-page-restart convention, not drift. No change.
- **No marker-pairing orphans found** — every `[^N]:` definition has a matching anchor in BOTH the Latin and English bodies, and every body anchor has a definition, across all 874 chunks. (The initial audit run reported a large spurious count from a regex bug: body anchors that legitimately precede a `:` introducing a quotation, e.g. `*de Trinitate*[^3]: «Uti…»`, were mis-excluded by a `(?!:)` lookahead. Corrected to distinguish line-start `^\s*[\^N]:` definitions from in-text anchors; re-run gave the clean result above.)

**Build after fix:** `node site/scripts/build-content.mjs` → `2 book(s), 875 questions, 875 translated` — clean.

**Files changed this pass:** `vol2/bon-sent-II-d9-littera.md`, `site/src/data/content.json`, this log.
