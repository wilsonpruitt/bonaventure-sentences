#!/usr/bin/env python3.11
"""Create Vol IV d.47 skeletons fresh (SINGLE-PARS, De iudicio universali et de igne
conflagrationis). Structure count-verified 2026-07-18.

⚠ WHY THIS SCRIPT EXISTS — the 2026-06-16 auto-chunk produced only 10 chunks; the real
  structure is 11. **`a2-q3` was MISSING**: its header is OCR-garbled `QUAESTIO ni.` (L104051),
  invisible to a `QUAESTIO` grep, so the chunker never saw it and `a2-q2`'s skeleton ran
  103926–104152, SWALLOWING q3's entire range. Same failure mode as d.42 a3-q3 and d.46 a2-q4.
  Found via the mandatory ordinal-opener cross-check (`Tertio quaeritur de illius ignis
  exlensione`, L104054) and Art II's own question-listing.

COUNT-CHECK (all four legs agree on 2 articles × 4 questions):
  - TRACTATIO L103133: "duo principaliter quaeruntur" → 2 articles. Art I's listing gives
    2 (iudicantes: Apostoli, Angeli) + 2 (iudicandi: omnes, Angeli) = 4.
  - Art II opener L103680: "Et circa hoc quaeruntur quatuor" → quidditas / virtus / extensio /
    ordo — which names q3 (*de extensione*) explicitly.
  - Ordinal openers all located: L103180, 103342, 103437, 103577 (Art I);
    L103693, 103929, 104054, 104156 (Art II).
  - Last-question tail-check: a2-q4 runs to the DUBIA header, no orphan.

GARBLED HEADERS in this range: `C0MMENTARIU8 IN MSTINOTIONEM XLVIL` (L103093),
  `ARTICULUS 11.` (L103677), `QUAESTIO 11.` (L103339), `QUAESTIO ni.` (L104051 — the one that
  cost us the chunk), `SCHOLIOK` (L103303), `DUBIA CIRGA LITTERAM MAGISTRI.` (L104264).

SCHOLIA (one per article, in that article's q1): a1-q1 L103303 (`SCHOLIOK`),
  a2-q1 L103885 (`SCHOLION.`).

BOUNDARY — d.47 = L102921–L104391.
  ⚠ OPENING: `DISTINCTIO XLVII.` at L102921 is the real header (the L102981 hit is the p.969
    running head). d.46's dubia end at L102920 — verified, no double-claim.
  ⚠ CLOSING: the real `DISTmCTIO XLVIII.` header is **L104392** (IN→m garble); the
    `DISTINCTIO XLVIII. 981` at L104305 is the p.981 running-head BLEED, sitting inside d.47's
    dubia. Do not cut there.

⚠⚠ INHERITED HAZARD — SHARED FOOTER BLOCK AT L102941–102963. This is a two-column interleave:
  the LEFT column is printed p.968's footer, which belongs to **d.46's dubia and is ALREADY
  RENDERED in `bon-sent-IV-d46-dubia.md`** (tells: "De hoc dub. cfr. Petr. a Tar.", "Hic in lit.
  Magistri, c. 3", "Vide I. Sent. d. 30"). The RIGHT column, under the `NOTAE AD LIBR.
  SENTENTIARUM.` header (L102961), is **d.47's littera apparatus** (tells: "Matth. 23, 34",
  "Sap. 3, 8 ... Matth. 19, 28", "Hic et duo seqq. loci sunt ex Beda"). The d.47 littera writer
  must claim ONLY the NOTAE entries and must NOT re-claim p.968's footers. Diff against
  d46-dubia before writing.

DUBIA: four greppable — DUB. I (L104267), DUB. II + DuB. IV both on L104332 (column
  interleave), DUB. III (L104379). ⚠ COUNT THEM OFF THE 450 dpi BANDS ANYWAY — the d.45 lesson
  (9 printed, 3 greppable, six cased `DuB.`) applies directly to this range.

PAGE TOPS from running heads (odd pages only; even-page heads are OCR-dropped):
  969=L102981, 971=L103169, 973=L103394, 975=L103637, 977=L103880, 979=L104109, 981=L104305.
  Printed span 968–981. Page assignments below are ESTIMATES derived from those tops —
  writers correct them from the bands.

⚠ BANDS: do NOT use colcrop's default split. Per `manual-review/vol4-column-gutter-parity.md`
  the vol4 gutter alternates by page parity; MEASURE each of pp.968–981 and regenerate at the
  measured value before dispatching. Offset pdf = printed + 20 (pp.988–1001).

Run: python3.11 tools/rechunk_d47.py
"""
import os, glob

RAW = "raw/bonaventure_vol4_raw.txt"
VOL = "vol4"
OFF = 20

with open(RAW, encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

# (id-suffix, type, art, q, title_la, title_en, l0, l1, printed_pages, has_scholion)
CH = [
 ("littera","littera",None,None,
   "Littera Magistri (Lombard), Distinctio XLVII — De iudicio universali",
   "The text of the Master (Lombard), Distinction XLVII — On the universal judgement",
   102921,103092,[968,969,970],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   103093,103173,[970,971],False),
 ("a1-q1","quaestio",1,1,
   "Utrum Apostoli iudicent",
   "Whether the Apostles will judge",
   103174,103338,[971,972],True),
 ("a1-q2","quaestio",1,2,
   "Utrum Angeli in die iudicii iudicabunt",
   "Whether the Angels will judge on the day of judgement",
   103339,103434,[972,973],False),
 ("a1-q3","quaestio",1,3,
   "Utrum omnes iudicabuntur, tam boni quam mali",
   "Whether all will be judged, both the good and the evil",
   103435,103573,[973,974],False),
 ("a1-q4","quaestio",1,4,
   "Utrum Angeli iudicabuntur",
   "Whether the Angels will be judged",
   103574,103676,[974,975],False),
 ("a2-q1","quaestio",2,1,
   "De quidditate ignis conflagratorii",
   "On the quiddity of the fire of the conflagration",
   103677,103925,[975,976,977],True),
 ("a2-q2","quaestio",2,2,
   "De virtute huius ignis, utrum sit naturalis, an supra naturam",
   "On the power of this fire, whether it is natural or above nature",
   103926,104050,[977,978],False),
 # ⚠ THE RECOVERED CHUNK — header `QUAESTIO ni.` L104051, opener `Tertio quaeritur` L104054.
 ("a2-q3","quaestio",2,3,
   "De extensione illius ignis",
   "On the extent of that fire",
   104051,104152,[978,979],False),
 ("a2-q4","quaestio",2,4,
   "De ordine huius ignis ad ea quae fient in iudicio",
   "On the order of this fire in relation to the things that will take place at the judgement",
   104153,104263,[979,980],False),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   104264,104391,[980,981],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d47-{idsuf}"', "volume: 4", "book: 4", "distinctio: 47"]
    if art is not None: y.append(f"articulus: {art}")
    if q is not None: y.append(f"quaestio: {q}")
    y.append(f"type: {typ}")
    y.append(f'title_la: "{tla}"')
    y.append(f'title_en: "{ten}"')
    y.append(f"printed_pages: {pp}")
    y.append(f"pdf_pages: {pdf}")
    y.append(f"line_start: {l0}")
    y.append(f"line_end: {l1}")
    y.append(f'source: "{src}"')
    y.append(f"has_scholion: {'true' if schol else 'false'}")
    y.append("has_apparatus: true")
    y.append('transcription_status: "auto-chunked 2026-07-18 (rechunk_d47) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d47-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.47 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d47-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.47 skeletons created.")
