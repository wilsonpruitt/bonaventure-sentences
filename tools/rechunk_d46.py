#!/usr/bin/env python3.11
"""Create Vol IV d.46 skeletons fresh (SINGLE-PARS, De mitigatione poenae damnatorum et de
misericordia et veritate in operibus Dei). Structure count-verified 2026-07-18:
  - TRACTATIO (L101688): "duo principaliter quaeruntur" -> 2 articles; "Circa primum quaeruntur
    quatuor" -> Art I has 4 questions; Art II's opener (L102270) lists 4.
  - Ordinal openers cross-checked (L101694, 101696, 102029, 102150, 102270, 102405, 102598).
  - QUAESTIO headers all located; titles taken from the line AFTER each header.
GARBLED HEADERS: "DISTINCTIO XLYI." (L101428), "Gap. I." (L101431), "ARTIGULUS I." (L101703),
  "ARTICULUS 11." (L102262), "QUAESTiO IV." (L102594 — lowercase i, INVISIBLE to a `QUAESTIO`
  grep; found only via the ordinal-opener cross-check `Quarto quaeritur` at L102598),
  "SCHOLIOK" (L101867).
SCHOLIA (one per article, in that article's q1, covering all 4 of its questions):
  a1-q1 L101867 (`SCHOLIOK`), a2-q1 L102368 (`SCHOLION.`). The hits at L102221/102325/102527/
  102621 are apparatus cross-references ("Vide scholion ad ..."), NOT scholion headers.
BOUNDARY — d.46 = L101428–L102920.
  ⚠ OPENING: the real `DISTINCTIO XLVI.` header is raw **L101428** (followed by `Gap. I.`).
  BOTH L101372 (`DISTINGTIO XLVI. 983`) and L101572 (`DISTINCTIO XLVl. 955`) are running-head
  bleeds. The 2026-06-16 auto-chunk had littera starting at L101372 — i.e. DOUBLE-CLAIMING
  L101372–101427, which belong to `bon-sent-IV-d45-dubia` (line_end 101427). Corrected here.
  ⚠ CLOSING: the real `DISTINCTIO XLVII.` header is L102921; the auto-chunk ran dubia to
  L102980, overrunning into d.47. Corrected to L102920.
  ⚠ Other auto-chunk corrections: a1-q1 now folds the `ARTIGULUS I.` opener (101703, was 101707);
  a2-q1 now folds the `ARTICULUS 11.` opener + its question-listing (102262, was 102277); dubia
  now starts at the real `DUBIA CIRCA LITTERAM MAGISTRI.` header L102793 (was 102796).
⚠ INHERITED HAZARD — d.45's apparatus is printed INSIDE d.46's raw range. Raw L101441–101462 is
  printed p.953's footer block and is ALREADY CLAIMED by `bon-sent-IV-d45-dubia.md` (10 entries).
  d.46's littera must NOT claim it. Verify against that file before writing.
DUBIA: only `DUB. I.` (L102795) is greppable, but the body carries further run-in "Item quaeritur
  de hoc quod dicit ..." openers and the apparatus at L102861-102875 references multiple dubia
  ("hoc dubio", "eodem dubio"). ⚠ COUNT THEM OFF THE 450dpi BANDS — the d.45 lesson (9 dubia
  printed, 3 greppable, six cased `DuB.`) applies directly.
Page tops from running heads: 955=L101572, 957=L101743, 959=L101930, 961=L102130, 963=L102342,
  967=L102788. Even-page heads are OCR-dropped; page assignments below are ESTIMATES — writers
  correct them from the bands.
Offset pdf = printed + 20.
Run: python3.11 tools/rechunk_d46.py
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
   "Littera Magistri (Lombard), Distinctio XLVI — De mitigatione poenae damnatorum et de misericordia et veritate in omnibus viis Dei",
   "The text of the Master (Lombard), Distinction XLVI — On the mitigation of the punishment of the damned, and on mercy and truth in all the ways of God",
   101428,101659,[953,954,955,956],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   101660,101702,[956],False),
 ("a1-q1","quaestio",1,1,
   "Utrum per suffragia Ecclesiae aliqua mitigatio fiat damnatis",
   "Whether through the suffrages of the Church any mitigation is granted to the damned",
   101703,101934,[956,957,958,959],True),
 ("a1-q2","quaestio",1,2,
   "Utrum fiat mitigatio damnatis propter misericordiae pietatem",
   "Whether mitigation is granted to the damned on account of the tenderness of mercy",
   101935,102023,[959,960],False),
 ("a1-q3","quaestio",1,3,
   "Utrum Deus misericordius agat cum uno quam cum alio",
   "Whether God acts more mercifully with one than with another",
   102024,102144,[960,961],False),
 ("a1-q4","quaestio",1,4,
   "Utrum Deus agat iustius cum uno quam cum altero",
   "Whether God acts more justly with one than with another",
   102145,102261,[961,962],False),
 ("a2-q1","quaestio",2,1,
   "Utrum in aliquo opere Domini sit misericordia et veritas",
   "Whether in any work of the Lord there are mercy and truth",
   102262,102399,[962,963],True),
 ("a2-q2","quaestio",2,2,
   "Utrum in eodem opere Domini sit misericordia et veritas",
   "Whether in the same work of the Lord there are mercy and truth",
   102400,102498,[963,964],False),
 ("a2-q3","quaestio",2,3,
   "Utrum in omni opere Domini sit misericordia et veritas, secundum quod proprie accipiuntur, an aliquando separentur",
   "Whether in every work of the Lord there are mercy and truth, according as they are properly taken, or whether they are sometimes separated",
   102499,102593,[964,965],False),
 ("a2-q4","quaestio",2,4,
   "Utrum Deus possit aliquem pure remunerare ex iustitia, vel pure ex misericordia",
   "Whether God can reward anyone purely out of justice, or purely out of mercy",
   102594,102792,[965,966,967],False),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   102793,102920,[967,968],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d46-{idsuf}"', "volume: 4", "book: 4", "distinctio: 46"]
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
    y.append('transcription_status: "auto-chunked 2026-07-18 (rechunk_d46) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d46-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.46 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d46-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.46 skeletons created.")
