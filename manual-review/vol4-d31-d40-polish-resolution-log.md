# Vol IV — Decade polish gate d.31–d.40 (resolution log)

Date: 2026-07-13. Fires per CLAUDE.md "Polish-blocker cadence" after d.40-dubia shipped
(last unit of DISTINCTIO XL, commit `a0b746d`). Three locked passes, all closed.

Distinctions covered (all Tier 2, committed): d.31 (9 chunks) · d.32 (11) · d.33 (12) ·
d.34 (9) · d.35 (9) · d.36 (9) · d.37 (9) · d.38 (9) · d.39 (11) · d.40 (6) = **94 chunks**.
Build at gate: **1798 translated, 1924 questions, 4 books, no parse errors.**

---

## Pass 1 — `[?]` flag resolution at 600 dpi: **CLOSED**

23 printed pages re-extracted at 600 dpi (`pdftoppm -r 600`, pdf = printed + 20). Full-page
600 dpi images exceed the API's 5 MB image limit — every read was done on a PIL crop of the
footer/scholion band, enlarged. **22 flags dispositioned: 21 RESOLVED, 1 ACCEPT-ILLEGIBLE.**

### Real defects found and fixed (5)

1. **`d31-a2-q2` — a MISSING WORD in the Latin body (p.724).** The long-standing `[?]` on the
   dangling fragment `po-` in fundamentum 1's Augustine quotation (*«…utuntur invicem ultra
   necessitatem procreandi liberos, po-[?] nam in his…»*) resolves as the **column-break
   hyphenation of *ponam***: the printed line ends `…procreandi liberos, po-` and the next
   column line opens `nam in his, pro quibus quotidie dicimus: Dimitte…`. The IA djvu OCR
   dropped the wrap. Nothing else was lost; the restored text matches Augustine, *De bono
   coniugali* c.10 n.11. **Latin and English bodies corrected; both `[?]` deleted.**
   This was the only body-text (as opposed to citation) defect in the decade.

2. **`d35-a1-q1` `[^p781-2]` (p.781).** Quaracchi prints **`II. Comment. in Matth. 15, 12.`** —
   NOT `18, 12`. The "unreadable glyph" was a period. Corrected in La + En.

3. **`d35-a1-q4` scholion §I (p.786).** `Petr. a Tar., hic a.` = **5**, not 8 (the 450 dpi
   suspicion was right, the IA OCR wrong). Incidental correction found in the same line:
   the print reads **`B. Albert., hic a. 5-16`**, not `15-16`. Both corrected in La + En.
   The faint trailing numeral in `cfr. supra d. 27. a. 3. q. 1. 2.` = **2**.

4. **`d40-a1-q2` `[^p849-4]` (p.849).** Verse number **5, not 3** — Quaracchi prints
   `Vers. 5. seq. Vulgata habet Deus vester tantum in v. 4.` The promoting writer's inference
   had been inverted: Bonaventure cites Lev. 18, 5 ff., and Quaracchi's remark is a
   *correction* (the quoted *Deus vester* stands only at v. 4, not in vv. 5 ff.). Corrected.

5. **`d34-divisio` `[^2]` (p.766) — Quaracchi's own misprint, transcribed not emended.**
   The edition really does print **`infra d. 57`** (italic figure: flat top bar + single lower
   bowl = 5). Book IV has only 50 distinctions and the note concerns d. XXXVII, so 57 is the
   edition's slip. **Per house rule the Latin keeps `57`**; the "misprint for d. 37"
   observation lives in a translator's bracket in the English + `## Notes`.

### Accepted illegible (1)

- **`d36-a2-q1` `[^p796-5]` (p.796).** The footer line is legible through
  *`Secundum Aristot., I. Phys. text. 81. (c. 9.). Cfr. IV. de`* and then **runs into the
  trimmed outer margin of the scan and stops** — no wrap line below, and the IA djvu OCR
  breaks off at the identical point (raw L85370). Not recoverable at any dpi from this scan.
  Tail rendered as an explicit editorial supply — `Cfr. IV. de [Generat. animal. c. 3.]` — on
  the authority of the parallel note at p.795 fn. 3 (raw L85271).

### Confirmed correct, Notes-only disposition (16)

All were band-vs-OCR digit disagreements where the **450 dpi column band had already been
right and the IA djvu OCR wrong**: `d31-a2-q1` (`d. 26` ✓) · `d32-littera` (`C. 33. q. 4.` ✓) ·
`d32-a1-q1` (`pag. 655` ✓) · `d32-a3-q1` (**`Lev. 15, 2. et 19.`** ✓ — an OCR mangle, NOT an
edition misprint, so no restoration of "13" was needed) · `d32-a4-q2` (`(tit. 17.)` ✓ retained
as printed; the lex *Non dubium est* is really C. 1.14.5 — Quaracchi's slip, noted not emended) ·
`d33-a1-q1` (canon `Liberi dicti (15.)` ✓) · `d33-a3-q1` (`Dist. 35. q. 1. seqq.` ✓) ·
`d35-divisio` (`[^1]` anchor placement confirmed on *de adul-|terio¹*; the COMMENTARIUS subtitle
carries no superscript — no marker moved) · `d35-a1-q1` `[^p781-9]` (the glyph after *seu lucem*
is a comma) · `d37-dubia` (`Si quis vivente (5.)` ✓) · `d38-a2-q1` (p.821 running head
`DIST. XXXVIII. ART. II. QUAEST. II.` ✓, printed_pages confirmed) · `d39-a2-q4` (`q. 4.` ✓) ·
`d40-a1-q2` `[^p849-5]` (codex siglum **A** ✓) · `d40-a1-q3` `[^p851-3]` (`Hic c. 1.` ✓) ·
`d40-a1-q3` `[^p851-4]` (**`supra d. 35. q. 5. arg. 1.`** ✓ — the feared d.35/d.33 citation
error does NOT exist) · `d32-divisio` structural flag (**false alarm** — `d32-littera` contains
no COMMENTARIUS heading and no *Sciendum est etiam* lemma; nothing duplicated, nothing deleted).

### Calibration note for d.41+

16 of 22 flags needed no text change: the 450 dpi band read was correct every time and the IA
OCR wrong every time. Band-vs-OCR **digit** disagreements are being parked as `[?]` more
conservatively than the evidence warrants — when the band is legible, resolve at band time and
record the disagreement in `## Notes` rather than raising a gate flag. The flags that *did*
matter were of a different kind: a column-break word loss (`ponam`) and a misread footer
*structure*, not a contested digit.

**Marker integrity: verified after all edits — 94/94 chunks pair 1:1:1
(Latin anchors = English anchors = apparatus defs). No marker counts changed.**

---

## Pass 2 — Style/formatting audit (full corpus): **CLEAN for d.31–d.40; a corpus-wide backlog surfaced**

`tools/polish-style-scan.py` across all Tier-2 chunks. **d.31–d.40: 0 issues across all 94 chunks.**

### ⚠ The scan had never covered Vol III or Vol IV

`polish-style-scan.py` was hardcoded `DIRS = ["vol1", "vol2"]` and was never extended when
Vol III (2026-06-02) or Vol IV (2026-06-16) opened. **Every "Pass 2 CLEAN" recorded in the
vol3 and vol4 gate logs was therefore reporting on `audit-paraphrase.py`, not on this scan.**
Extended to `["vol1","vol2","vol3","vol4"]` at this gate (committed).

With the full corpus in scope it reports **61 chunks with real apparatus defects** — **none in
d.31–d.40**; all pre-existing, in Vol II (2), Vol III (27), and Vol IV d.1–d.28 (32):

- **25 chunks with DUPLICATE apparatus defs.** Quaracchi restarts footnote numbering on every
  printed page; these chunks rendered that with bare `[^1]`, `[^2]`… so a multi-page chunk ends
  up with two `[^1]:` definitions. **At render time a body marker binds only one of them, so
  apparatus entries are silently dropped on the published page.** Worst: `d3-p2-a3-q2` (19 dup),
  `d27-a1-q4` (16), `d29-a1-q1` (16), `d20-p2-dubia` (15), `d6-p1-littera` (15).
  The `[^pNNN-M]` page-qualified convention adopted at d.31 exists precisely to prevent this —
  the older chunks predate it.
- **7 chunks whose ENGLISH body carries ZERO apparatus markers** (footnotes render in the Latin
  and nowhere in the translation): `IV-d9-a1-q1`, `IV-d12-p1-divisio`, `IV-d14-p1-divisio`,
  `IV-d15-p1-divisio`, `IV-d20-p2-divisio`, `IV-d21-p2-divisio`, `IV-d28-a1-q6`.
- The remainder: partial missing anchors (a def with no body anchor in one or both languages).

**Vol III is LIVE on bonaventure.wrootpress.com**, so part of this is reader-visible today.

**NOT repaired at this gate** — it is out of scope for a d.31–d.40 blocker, it touches published
volumes, and it is a ~61-chunk job. **Owner decision required** (see `next-session-resume.md`).
This gate does not pass or fail on it; d.41 is not blocked by it.

---

## Pass 3 — Cross-chunk boundary integrity (d.31–d.40): **CLEAN**

- `audit-headers.py --volume 4 --min-d 31 --max-d 40`: **no LOSS flags**; all diffs non-negative
  (the expected Vol II/IV heuristic-undercount pattern). d.40's `DUB raw 1 / chunk 5` diff is the
  audit independently confirming the four OCR-hidden dubia headers the d.40 writer read off print.
- `audit-paraphrase.py --volume 4 --min-d 31 --max-d 40`: **0 critical, 0 high** (94 chunks).
- `audit-apparatus-count.py --volume 4 --min-d 31 --max-d 40`: **0 flagged** (94 chunks).
- **Footer double-claim sweep (programmatic, all 113 page-qualified pages in the decade):**
  no apparatus entry is claimed by two chunks. Three same-text hits were investigated and all
  three are the stock Quaracchi redirect *«Vide scholion ad … praecedentis articuli quaest.»*
  legitimately repeated on **different** pages/questions — not double-claims.
- **Dropped-footer sweep (per-page footnote contiguity):** six pages initially showed gaps
  (735, 739, 761, 770, 791, 814). **All six are artifacts of mixed labeling** — the sibling
  chunk sharing each page uses bare `[^N]` numbering, invisible to a page-qualified scan. Union
  coverage is contiguous 1..N on every page. **No footer is dropped.**
- **Seam-page "double-claims" (778, 812, 829, 844) investigated and cleared:** at a
  distinction seam the shared page carries **two independent footer blocks** — Bonaventure's
  commentary footers (outgoing dubia) and the `NOTAE AD LIBR. SENTENTIARUM` block (the incoming
  distinction's littera apparatus). Both restart at 1, so `[^p844-1]` legitimately denotes two
  different footers in two different files. Separate files = separate footnote namespaces, so
  there is **no render collision**. Texts verified different in all four cases.
  *Known cosmetic ambiguity — documented so a future gate does not re-flag it.*

---

## Gate disposition: **PASSED.** d.41 unblocked.

Disk: 450 dpi page images + colcrop bands + the 23 600 dpi hi-res pages deleted per CLAUDE.md
gate step 4 (all regenerable from the gitignored PDF via `extract-pages.py` / `colcrop.py`).
