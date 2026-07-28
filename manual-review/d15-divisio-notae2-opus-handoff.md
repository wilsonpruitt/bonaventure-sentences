> # ✅ RETIRED — CLOSED 2026-07-28 (Opus, commit `c9f0708`). DO NOT RE-RUN.
>
> `[^notae-2]` **was placed**, and this file's central premise was wrong. It argued the note
> had "no locator" and could only be content-matched. In fact printed p.329 carries **two
> independent footnote series** — the main body-footers 1–4 (Lombard's *littera*) and a
> separate `NOTAE AD COMMENTARIUM` block 1–2 (the commentary) — and **both *Notae*
> superscripts are printed**, contrary to §2's claim (a) that the 2026-07-13 pass had
> established there were none.
>
> - `[^notae-2]` → the `²` on `Ad intelligentiam autem huius partis incidit ² quaestio circa
>   duo` (TRACTATIO QUAESTIONUM). Codd. U V W Z read *incidit **hic** quaestio*. The note
>   names no lemma because the superscript already fixes the insertion point.
> - `[^notae-1]` → the `¹` on `in speciali, ibi ¹:` (DIVISIO TEXTUS) — **not** the TRACTATIO's
>   later *in speciali*, where §0 reported it as correctly resolved.
> - §5's "do not touch anything else" could not be honoured: `[^p329-1]`/`[^p329-2]` were
>   sitting on the two *Notae* positions and `[^p329-3]` on an unmarked lemma line. All three
>   were returned to `d15-littera`, which had dropped its own anchors (19 → 22 entries).
> - The littera's two standalone *hic* occurrences that §2 flagged as the lead were a **red
>   herring** — both are Augustine-quotation prose, neither is the variant.
>
> Kept for the record only. Full disposition: `next-session-resume.md` and both chunks' `## Notes`.

# `III-d15-divisio` `[^notae-2]` — single-chunk Opus decision. SESSION HANDOFF (written 2026-07-28)

**Read this whole file before touching anything.** This is a **single unresolved apparatus
entry in one published chunk** — not a batch job. It needs Opus because it's a philological
delete-vs-anchor judgment call on live text, not because of volume.

## 0. Correcting the prior framing

`NEXT-SESSION-QUEUE.md`'s "Class C" item describes this chunk as "5 apparatus defs, ZERO
body anchors." **That description is stale/inaccurate for the file as it stands now.** A
2026-07-13 apparatus-anchor pass already resolved 4 of the 5:
- `[^p329-1]`, `[^p329-2]`, `[^p329-3]` — the three numbered p.329 footers — are correctly
  anchored in both languages (confirmed by content match).
- `[^notae-1]` — anchored by content match (its text names its own topic — "*Intellige cum
  edd. 1, 2 infra dist. 16*" — which the DIVISIO TEXTUS and TRACTATIO QUAESTIONUM both
  independently name as "the passion of grief in particular" / "certain defects in
  particular").
- **Only `[^notae-2]` remains unplaced.** Read the chunk's own `## Notes` in full
  (`vol3/bon-sent-III-d15-divisio.md`) before doing anything else — it already documents the
  2026-07-13 investigation in detail and explains exactly why it was left unanchored rather
  than force-placed.

**The actual open question is narrow: where, if anywhere, does `[^notae-2]` belong?**

## 1. What `[^notae-2]` says

```
[^notae-2]: **La.** Codd. U V W Z adiiciunt hic.
    **En.** Codices U V W Z add *here*.
```

This is a textual-variant note: codices U, V, W, Z add the word *hic* ("here") at some point
in the text. Unlike `[^notae-1]` and unlike the accepted corpus precedent (e.g. `d1-p1-divisio`'s
`[^1n]`–`[^3n]`, each of which quotes a specific phrase from its host sentence), this note names
only the single word being added — a common function word — with no "*ante X*" / "*post Y*"
locator and no unique surrounding co-text to match against a body.

## 2. What the 2026-07-13 pass checked, and what it did NOT check

The prior pass confirmed: (a) no printed superscript exists anywhere on p.329 for the NOTAE
AD COMMENTARIUM block (both notes are genuinely unmarked in print — placement, if any, must
be by content, not position); (b) the word "*hic*" does **not** appear as a standalone word
anywhere in `III-d15-divisio`'s own Latin body (confirmed by grep at the time).

**What it did NOT check: the sibling `III-d15-littera` chunk.** This matters because:
- The heading is **"NOTAE AD COMMENTARIUM"** — literally "notes to the COMMENTARY" — which by
  its own name should mean these are Bonaventure's-commentary notes, not Lombard's-littera
  notes. That argues against this being a J3-style "filed under the wrong chunk" case.
- **But** a fresh grep (2026-07-28) of `III-d15-littera.md` found the word "*hic*" occurring
  standalone **twice** in its running prose, both on printed p.329 (the littera spans
  pp.327–329; `pdf_pages: [349, 350, 351]`):
  - `"— Ecce evidenter dicit **hic** Augustinus, ignorantiam..."` (line 32 of the littera file)
  - `"— Ecce **hic** videtur tristitiam et timorem a Christo removere."` (line 50 of the
    littera file)
  Both are already transcribed *with* "hic" present — so if one of these is actually the
  variant reading (i.e., the base/other editions read the sentence *without* "hic" and only
  codd. U V W Z add it), the littera's transcription may currently be silently following the
  variant reading without documenting it, or the note may genuinely belong there rather than
  in the divisio.
- The littera's own `[^p329-4]` (its sole p.329 apparatus claim) is a different note entirely
  (`"haec distinctio continuatur usque ad c. 3. sequentis dist.: Hic oritur"` — a citation of
  the *next* distinction's opening words, coincidentally also containing "Hic" but as part of
  a quoted incipit, not the same variant). Don't confuse this with `[^notae-2]`.

## 3. What to actually do

1. Re-pull the 450 dpi (or 600 dpi if ambiguous) column bands for **printed p.329** — both the
   littera's tail (top of both columns) and the COMMENTARIUS/DIVISIO/TRACTATIO region (lower
   ~two-thirds), per the existing Notes' provenance section. `pdf_pages: [349, 350, 351]` for
   the littera (p.329 = pdf 351); same for the divisio.
2. Check specifically: is there a printed superscript numeral anywhere on p.329 near either of
   the littera's two "hic" occurrences, or anywhere else on the page, that could bind to
   `[^notae-2]`? The 2026-07-13 pass already established there's no marked anchor in the
   divisio/commentary region — extend that same check to the littera region, which was not
   checked.
3. If a genuine, evidence-backed location is found (in either chunk): move `[^notae-2]` there,
   following the corpus convention (page-suffixed slug, content-matched, never by position).
   If it belongs in the littera, delete it from the divisio and add it to the littera's own
   apparatus (mirroring how footers were split between the two chunks originally, per the
   littera's own hand-off note).
4. If no textual evidence turns up in either chunk (as `[^notae-1]`'s investigation genuinely
   found none, then found evidence anyway — don't assume the same negative result before
   checking): **leave it as a documented, deliberate refusal**, exactly as the current file
   already does, and just add a note confirming the littera was checked too. A refusal with
   evidence is a fine outcome — do not force a placement you're not confident in.
5. **Do not touch anything else in either chunk.** Both are Tier 2, published, and everything
   else in both files' apparatus is already correctly dispositioned.

## 4. Verify

```bash
cd site && node scripts/build-content.mjs   # must stay at 1949 translated / 1949 questions
python3.11 tools/polish-style-scan.py --volume 3   # III-d15-divisio's [PAIR] flag should
                                                     # either clear (if placed) or remain
                                                     # exactly as before (if refused again)
```

**Do NOT `git push`, do NOT deploy.** Both need Wilson's explicit per-action OK. Commit
locally with a clear message, report the disposition, and ask about push + deploy for the
whole accumulated session (this item plus everything else from 2026-07-28).
