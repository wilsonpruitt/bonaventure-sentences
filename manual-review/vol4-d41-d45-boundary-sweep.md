# Vol IV — d.41–d.45 cross-chunk boundary integrity sweep

**Pass 3 of the d.41–d.50 decade gate.** Run 2026-07-21. Scope: `vol4/bon-sent-IV-d4{1,2,3,4,5}-*.md`
(62 chunks). d.46–d.50 covered by a separate agent.

Method: reconstructed every chunk's raw line range (for d.41/d.42 the range lives in the
`transcription_status` string, not in `line_start`/`line_end` frontmatter) and its `printed_pages`,
put the chunks in reading order, and enumerated every seam where the last printed page of chunk A
equals the first printed page of chunk B. For each such seam: (a) parsed the prior chunk's closing
sentence and the receiving chunk's opening; (b) built a per-printed-page apparatus ledger across all
chunks and looked for gaps and double-claims; (c) scanned every apparatus entry in the range for a
note that breaks off without terminal punctuation (tail runover) or opens mid-sentence (inbound
fragment). Page images were pulled only where the ledger showed a hole.

## Headline

- **55 mid-page seams** checked.
- **52 CLEAN.**
- **3 defects** found: two dropped footnotes (both repaired), one double-claimed footnote (logged,
  not touched — spans two chunks).
- **1 further finding** on check (c): a truncated footer note whose runover appears to have been
  mis-filed into the body. Logged, not touched — it sits on an open `[?]` another agent is working.

## (a) Grammatical continuity / cascade-merge signature

**No cascade-merge splice anywhere in d.41–d.45.** All 55 prior-chunk tails parse as complete Latin
sentences; every receiving chunk opens on a structural heading (`ARTICULUS`, `QUAESTIO`,
`DISTINCTIO`, `DUBIA CIRCA LITTERAM MAGISTRI`, `COMMENTARIUS`), which is the expected shape at these
boundaries. The raw line ranges are fully contiguous from L91127 (`d41-littera`) through L101427
(`d45-dubia`) with no gap and no overlap, so nothing fell between two chunks either.

One tail initially looked truncated — `d45-a2-q3` ends on a bracketed editorial label with no text
after it — but that is an artifact of my scan stripping blockquote lines; the labelled block is
present and complete in the file. See the check-(c) finding below for the real question about it.

### The d.45 littera repair held

Verified directly in the raw text. L99598 is the true `DISTmCTIO XLV.` header; the earlier
`d44-p2-dubia` `line_end` of 99732 was the p.937 running-head bleed (`DISTINCTIO XLV. 937` sits at
~L99732, well inside Lombard's Cap. II). With `d44-p2-dubia` now closing at 99597 and `d45-littera`
opening at 99598, Lombard's Cap. I and the opening of Cap. II are back in the corpus:
`bon-sent-IV-d45-littera.md` carries `Cap. I` through `Cap. VI`. Nothing is orphaned between the two
chunks — the ranges abut exactly.

### Other d.45 spot-checks from the brief

- **9 dubia present** in `d45-dubia` (`Dub. I`–`Dub. IX`), including the six lowercase-cased ones.
- **p.953 footers correctly split, not double-claimed.** `d45-dubia` renders p.953 notes 1–10 (the
  commentary series). `d46-littera` renders only the page's *second* footer block — the
  `NOTAE AD LIBR. SENTENTIARUM` series — as a single entry keyed with a deliberate `-lit` infix
  precisely so it cannot collide with d.45's p.953 keys. Correct on both sides.

## (b) Shared-page footer accounting

Per-page ledger across all d.41–d.45 chunks. Every printed page from 855 to 953 reconciles once the
sequentially-labelled chunks (`d41-divisio`, `d41-dubia`, `d42-divisio`, `d42-a1-q2`, `d42-a1-q3`,
`d42-a2-q1`, `d42-a2-q3`, `d42-a3-q1`, `d42-a3-q3` — these renumber 1..N per file rather than
page-keying) are credited with the page ranges their own `## Notes` declare. Those Notes blocks are
unusually good and each states its split explicitly; I took them as the claim and checked the
arithmetic closes.

Residual ledger "gaps" at pp. 858, 874, 877 are all of that kind — the missing low-numbered notes
are held by the sequentially-labelled predecessor chunk (`d41-divisio` holds p.858 nn.1–6;
`d42-a2-q1` holds p.874 nn.1–5; `d42-a3-q1` holds p.877 nn.1–4). No loss.

Residual ledger "duplicates" at pp. 864, 880, 882, 906, 936 are **not** duplicates: those pages each
print **two independent footer series** (Quaracchi's `NOTAE AD COMMENTARIUM` and its
`NOTAE AD LIBRUM SENTENTIARUM`, the latter serving Lombard's text where a new distinction's littera
opens on the page). I compared the note texts pairwise in each case — they are entirely different
entries that merely collide on a `pNNN-1` style label. This is a labelling-hygiene item, not a
content defect, and it must **not** be "fixed" by renumbering. `d45-divisio` already models the right
answer with its `p938c-1` key; a corpus-wide convention (a `-c` / `-lit` infix on two-series pages)
would remove the collision without touching any number.

### DEFECT 1 — `bon-sent-IV-d44-p2-a1-q1` — p.923 footer note 1 dropped. **Severity: medium. FIXED.**

Nobody owned it. `d44-p2-a1-q1` spans pp. 920–923 but held no p.923 entry; its own Notes recorded
that the OCR line for *Deus duo tempora sibi distinxit* "carries a possible footnote marker
(apostrophe artifact)" but that no footer text was available, so none was written. The sibling
`d44-p2-a1-q2` independently recorded that p.923 note 1 belongs to q1 and declined it, opening its
own claim at p.923 note 2 — and added "if a.1 q.1 was promoted without its p923 note 1, it should be
added there." It had not been.

Pulled p.923 at 450 dpi, measured the gutter at **1495** (odd page, consistent with the parity table),
cropped, and read the left footer band. p.923 note 1 reads:

    Codd. F bb constituit, edd. distinxit vel constituit.

A variant on *distinxit* — which confirms the apostrophe artifact was a real marker and fixes the
anchor exactly. **Fixed:** added the entry as `p923-1`, anchored on *distinxit* in reply 6 of the
Latin and mirrored at the matching point in the English ("has distinguished two times for himself").
Disposition written into the chunk's `## Notes` under the existing open item. Apparatus count for
that chunk is now 31.

### DEFECT 2 — `bon-sent-IV-d44-p2-a1-q2` — p.925 footer notes 1 and 2 dropped. **Severity: medium. FIXED.**

Same shape, two notes. `d44-p2-a1-q2`'s page span was corrected to 923–925 during its build, but its
p.925 tail was set from OCR because no p.925 band was ever generated, so the page's footers were
never read and never claimed. The following chunk, `d44-p2-a2-q1`, correctly declined them —
recording that p.925 nn. 1–2 anchor in a.1 q.2 at *quodlibet* and *in extremo*, and opening its own
claim at p.925 note 3. Both notes were therefore unowned.

Pulled p.925 at 450 dpi, measured the gutter at **1581**, cropped, read the footer band:

    1  Vat. pro eo quod. Mox substituimus ex cod. F (E a secunda manu) superioris pro inferioris.
       Inferius pro medietas multi codd. et edd. mediocritas.
    2  Vide scholion ad praecedentem quaest.

Note 1's lemmas (*superioris*, *medietas*) both fall inside this chunk's p.925 sentence, which fixes
its marker at *quodlibet*; note 2 cross-refers to the preceding question's scholion (this chunk
carries none of its own), fixing its marker at the closing *in extremo*. Both agree with the anchors
the a.2 q.1 writer reported from the same band. **Fixed:** both entries added, anchored in the Latin
and mirrored in the English; the apparatus header note and the chunk's split map updated from 13 to
15 entries. Nothing retranslated, nothing renumbered.

### DEFECT 3 — p.920 note 1 claimed by two chunks. **Severity: low. LOGGED, NOT TOUCHED (spans two chunks).**

`bon-sent-IV-d44-p2-divisio` and `bon-sent-IV-d44-p2-a1-q1` both carry a `p920-1` entry with
**identical** text — *Codd. Quando.* Unlike pp. 864/880/882/906/936, this is not a two-series page:
it is one note claimed twice.

The evidence favours the divisio. It anchors the note on *Cum* in
*Cum autem constet, animas* — and *Quando* is precisely the codical variant of *Cum*. `p2-a1-q1`
anchors the same note on *Primo* and its own Notes concede the position: "the superscript is not
legible in the p920 band; anchored provisionally... Position uncertain — resolve at the d.40/d.50
600 dpi pass." So the likely correct disposition is: keep it in `d44-p2-divisio`, drop it from
`d44-p2-a1-q1`, and renumber nothing.

Not acted on here: it spans two chunks, and the a.1 q.1 side is an open flag another agent is
working. Recommend a 600 dpi read of the p.920 right column to confirm which word carries the
superscript, then a one-line deletion.

## (c) Cross-page footer runover

Scanned every apparatus entry in d.41–d.45 for a `La.` text ending without terminal punctuation
(the tail-runover signature) and for a note-1 opening lowercase or on an ellipsis (the inbound-
fragment signature). **One hit, no inbound fragments anywhere.**

### FINDING — `bon-sent-IV-d45-a2-q3` — p.946 note 6 truncated; its runover may be mis-filed as body. **Severity: medium. LOGGED, NOT TOUCHED.**

`p946-6` quotes Praepositivus and stops dead, without a stop, at:

> …quod speciales orationes, quae fiunt pro divite, prosunt etiam pauperi, ad similitudinem
> candelae, quae accenditur pro divite

The chunk's writer parked a `[?]` on exactly this, having found nothing beyond *pro divite* in the
column. But the same chunk renders, at the very end of both language blocks, an unnumbered petit-type
block labelled *[Continuatio altera, minoribus litteris ad calcem pag. 946 impressa:]* which begins:

> …in domo et illuminat omnes circumstantes, alios plus, alios minus secundum vim acuminis visus
> eorum; ita eleemosyna oblata pro uno, qui est in purgatorio, omnibus prodest…

Joined to note 6 that is grammatically seamless — *candela quae accenditur pro divite* **in domo et
illuminat omnes circumstantes** — and the block's whole content (the candle simile worked out, then
the Jerome citation, then an objection and reply) reads as a continuous report of Praepositivus's
opinion, i.e. as the rest of the note. The writer instead read it as a second, mutually exclusive
petit-type recension of the body, reasoning that the main body runs continuously across the page
break without it. Both readings are defensible from the text alone.

If the block is note 6's runover, then the chunk has apparatus text sitting in its body, and note 6
is truncated. If the writer is right, both are fine as they stand. **Do not guess** — this needs the
p.946 right-column footer band read at 600 dpi to see whether the petit block sits above or below the
footnote rule and whether it is set at note-size or body-petit-size. That single observation settles
it. Flagged to the `[?]`-resolution agent, whose queue already contains this flag.

## Also observed (not boundary defects, no action taken)

- **`d45-dubia`, p.953 notes 6 and 7** — the d.46 writer read the p.953 bands and reports two
  citation disagreements with what `d45-dubia` transcribed: note 6 has *tom. II. pag. 177, nota 3*
  where the band reads **nota 5**, and note 7 has *III. Sent. d. 33. q. 1. ad 2* where the band reads
  **d. 35. q. 4. ad 2**. That is an apparatus-accuracy item inside one chunk, not a seam loss;
  carrying it here so it is not lost.
- **`d41-a1-q3` frontmatter `line_end` disagrees with its own status string** — frontmatter says
  91898, the status string says the range ends at 91892, and `d41-dubia` starts at 91893. The status
  string is right and the content is correctly split; the frontmatter field is a stale 6-line
  overhang. Cosmetic, but it is the kind of drift that makes the next ledger harder to build.
- **Apparatus-intro blockquote placement is inconsistent** across the decade: some chunks put it at
  the top of `## Latin`, some at the bottom of `## Latin`, some under `## Apparatus`. Style-pass
  territory (Pass 2), noted only because it makes programmatic body extraction unreliable.

## Files changed

- `vol4/bon-sent-IV-d44-p2-a1-q1.md` — added `p923-1` apparatus entry + Latin and English anchors;
  Notes updated.
- `vol4/bon-sent-IV-d44-p2-a1-q2.md` — added `p925-1` and `p925-2` apparatus entries + Latin and
  English anchors; apparatus header note and split map updated; Notes updated.

No build run, no commit.
