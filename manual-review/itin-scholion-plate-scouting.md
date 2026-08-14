# `bon-itin-scholion` — plate scouting (2026-08-14)

Everything below is **measured or read off the 450 dpi plates** and is banked so the
writing session does not have to re-derive it. Nothing here is a guess. The chunk itself
is **not yet written**; this file is scouting only, on the precedent of
`itin-c2-plate-scouting.md`.

## Span — SETTLED, and it settles an open question in the resume note too

- **The scholion runs pp. 313–316.** It opens on **p. 313** beneath a **full-width centred
  `SCHOLION` display heading** at ~48 % down, and closes on **p. 316** at ~62 % down the
  right column, at *…vel saltem conferat locos a nobis in notis allegatos.*
- **✅ p. 317 IS *De reductione*'s HALF-TITLE** — verified on the plate (`SERAPHICI DOCTORIS
  / SANCTI BONAVENTURAE / OPUSCULUM / DE / REDUCTIONE ARTIUM AD THEOLOGIAM`). **The
  standing "p. 317/319, span to be verified" uncertainty is closed at 317.** p. 318 not yet
  checked; expect blank.
- The index's claim of 313–316 turned out right and was used for nothing.

## Structure — three facts that change how the chunk is built

1. **★★ THE SCHOLION CARRIES NO APPARATUS AT ALL.** pp. 314, 315 and 316 have **no footer
   register whatsoever** — the two-column scholion text runs to the foot of the page and
   stops. p. 313's six footer notes are **Cap. VII's**, already owned by `bon-itin-c7`.
   **So this chunk has `has_apparatus: false` and zero `[^N]` anchors** — the first Vol V
   chunk of which that is true. The scholion cites its authorities **inline** instead
   (`(Prolog. n. 4.)`, `(III. Sent. d. 24. dub. 4.)`, `(II. Sent. d. 18. a. 1. q. 3.)`,
   `S. Thom. (S. I. II. q. 94. a. 2. corp.)`, and so on, in parentheses in the body).
2. **The scholion carries no marginalia** on any of its four leaves.
3. **It is numbered internally** — `1.`, `2.`, `a.`/`b.`/`c.`, `3.`, `4.`, `Tertio`,
   `Quarto`, `In toto autem Itinerario suo…` — a lettered/numbered editorial argument, not
   continuous prose. Preserve the numbering verbatim as with Quaracchi's paragraph numbers.

## Gutters — measured per leaf, and p. 314/315 needed the escalation

| Page | Adopted | Zero band | Rule inside it | colcrop default | Verdict |
|---|---|---|---|---|---|
| 313 (Scholion region) | **1161** | 1129–1194 (66 px) | 1160–1162 | 1161 page-wide | region value — see below |
| 314 | **1375** | 1352–1398 (**47 px**) | 1363–1386 (**24 px**) | 1371 / 55 px | skewed leaf; band midpoint adopted |
| 315 | **1189** | 1163–1215 (**53 px**) | 1183–1195 (**13 px**) | 1187 / 57 px | skewed leaf; band midpoint adopted |
| 316 | **1385** | 1355–1416 (62 px) | 1384–1388 (5 px) | 1385 / 64 px | clean leaf, default confirmed |

Thresholds 90/110/140/170 all agree on every band above, so **none of this is ink-threshold
sensitivity.**

### ★★★ A FOURTH MECHANISM BEHIND A NARROW RUN: SCAN SKEW SMEARS THE CENTRE RULE

The frozen rule says a sub-60 px run usually means **the centre rule inked heavily** on that
leaf. pp. 314 and 315 are neither heavily inked nor genuinely narrow — **the leaf is
rotated**, so the full-height vertical rule sweeps horizontally down the page, and the union
of its positions is subtracted from the apparent blank band.

**The diagnostic is cheap and decisive: profile the rule's peak x per vertical band and look
for MONOTONIC drift.**

```
p. 314  rows  382– 898 → x=1384      p. 315  rows  382– 898 → x=1193
        rows  898–1414 → x=1379              rows  898–1414 → x=1193
        rows 1414–1930 → x=1376              rows 1414–1930 → x=1190
        rows 1930–2446 → x=1374              rows 1930–2446 → x=1190
        rows 2446–2962 → x=1370              rows 2446–2962 → x=1186
        rows 2962–3478 → x=1368              rows 2962–3478 → x=1184
        drift 16 px, monotonic               drift 9 px, monotonic
```

A heavily-inked rule sits **still** and just darkens; a skewed one **walks**. p. 316 is the
control — its rule is 5 px wide and its band is a healthy 62 px.

**Consequence for the split value:** the band midpoint is still the right single number
(it lands on the rule's mid-height position), and `colcrop`'s ±60 px column overlap absorbs
the sweep. **What is wrong is the inference** — do not read 47 px as "heavily inked" and go
looking for an obstruction that is not there. Add skew to the list before concluding.

⚠ **This is now the fourth member of the bad-run family**, after (a) the display heading
crossing the gutter, (b) an in-column `Cap. N.` heading flooding one side, and (c) the
region-mismatch found at c7 on p. 313. Only (c) fails to move the run width at all.

### The region rule from c7 holds here and was used

p. 313 has **two** gutters — Cap. VII's body at 1166 and the Scholion's at 1161. This chunk
takes **1161**. pp. 314–316 are single-region (scholion only), so page = region there.

⚠ **A trap worth recording:** a hand-rolled scan window of x∈[1050,1320] finds p. 315's
gutter and **completely misses pp. 314's and 316's**, which sit near 1375–1385 — the even
leaves. It returns a minimum ink of 278 with no zero column and looks like a failed page.
It is not; the window was wrong. **`colcrop`'s own 0.42–0.60 fraction window spans both
clusters and is correct — do not hand-roll a narrower one.** (The parity model stays retired:
these four leaves happen to alternate, and that is worth nothing as a predictor.)

## Digits already settled at the plate

- **p. 313, Scholion §: *Quaestionem disputatam supra pag. 47*** — the raw agrees, but the
  glyph is squarely in the 1/4 confusion class and a first read of the band gave "17".
  **Settled as 4** by comparing against a known `1` and a known `4` **in the same size on the
  same page**: the line *Dissertationem (ibid. pag. 1-47)* three lines below supplies both.
  The `1` is a narrow flagged upright with no crossbar; the disputed glyph is wide and
  carries the `4`'s horizontal crossbar. ★ **This is the frozen siglum/digit rule working in
  reverse — the risk was reading a true `4` as `1`, not the usual direction. Find both
  numerals on the same leaf before deciding either.**

## Raw range

`raw/doctorisseraphic05bona_djvu.txt`, the p. 313 preamble at **L55511–55603**
(*Aurei huius opusculi doctrina…*) and the numbered body from **L55604** (*1. Quoad indolem
opusculi peculiarem notamus…*) to **~L56040** (*…conferat locos a nobis in notis allegatos.*).
**~4,300 words of Latin** — roughly double a capitulum, and the largest single chunk in the
work by a wide margin. The raw is usable for the running prose but garbles heavily in the
citation clusters; grade it per region as always.

## What is NOT yet done

- The chunk is **not written**. No `vol5/bon-itin-scholion.md` exists.
- pp. 314–316 have been **rendered whole and structurally read**, but their text has **not**
  been transcribed column-band by column-band.
- `KNOWN_TOTALS` needs **no** entry for 314–316 (no footer register). p. 313 is already fed
  with 6, all of them c7's.
- The ledger will take a **negative** line for this chunk (no runovers possible — no footers).
