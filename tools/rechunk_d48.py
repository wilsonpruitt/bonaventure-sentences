#!/usr/bin/env python3.11
"""Create Vol IV d.48 skeletons fresh (SINGLE-PARS, De iudicis apparitione et de innovatione
corporum superiorum). Structure count-verified 2026-07-18.

⚠ WHY THIS SCRIPT EXISTS — the 2026-06-16 auto-chunk produced only 10 chunks; the real
  structure is 11. **`a2-q3` was MISSING** (exactly the d.47 defect, one distinction later):
  its header is OCR-garbled `QUAESTIO lU.` (L105611), invisible to a `QUAESTIO` grep, so the
  chunker never saw it and `a2-q2` ran 105475–105766, SWALLOWING q3's whole range.
  Recovered via Art II's question-listing ("Tertio, utrum innovabuntur elementa") and the
  ordinal opener "Tertio quaeritur, uirum innovabuntur elementa" (L105614).

COUNT-CHECK (2 articles × 4 questions, all legs agreeing):
  - TRACTATIO L104663: "duo principaliter quaeruntur" → 2 articles; "Circa primum quaeruntur
    quatuor" → Art I has 4.
  - Art II opener L105280: "circa hoc quaeruntur quatuor" → remuneratio / quies / elementa /
    plantae-et-animalia — naming q3 explicitly.
  - All eight ordinal openers located.
  - Last-question tail-check: a2-q4 runs to the DUBIA header, no orphan.

GARBLED HEADERS: `DISTmCTIO XLVIII.` (L104392, IN→m — the defect class that truncated d28/d37
  litterae; here the header is correctly identified), `C0MMENTARIU8 IN DI8T1NCTI0NEM XLVIII.`
  (L104642), `ARTIGULUS I.` (L104696), `ARTIGULUS 11.` (L105280), `QUAESTIO lU.` (L105611),
  `SCHOLIOK` (L104867, L105417), `DUBfA CIRCA UTTERAM MAGISTRI.` (L105902).

SCHOLIA (one per article, in that article's q1): a1-q1 L104867, a2-q1 L105417.

BOUNDARY — d.48 = L104392–L106122.
  ⚠ The real opening header is **L104392** (`DISTmCTIO XLVIII.`); the `DISTINCTIO XLVIII. 981`
    at L104305 is the p.981 running-head bleed sitting inside d.47's dubia. d.47's dubia end at
    L104391 — verified, no double-claim.
  ⚠ The real closing boundary is L106122; `DISTINCTIO XLIX.` is L106123. The
    `DISTINCTIO XLIX. P. I. 997` at L106068 is the p.997 running-head bleed.
  ⚠ The DUBIA chunk starts at the real header **L105902**, NOT L105868 — that line is the
    `DIST. XLV[n. DUBIA. 99r` running head (the d.46–d.50 setup file names L105868; it is wrong).

DUBIA: three greppable — DUB. I (L105905), DUB. If (L105908, column interleave), DUB. III
  (L105973). ⚠ COUNT THEM OFF THE 450 dpi BANDS — the d.45 lesson (9 printed, 3 greppable,
  six cased `DuB.`) applies to exactly this shape.

PAGE TOPS from running heads (odd only; even-page heads are OCR-dropped, so even-page tops are
  INTERPOLATED as the midpoint of the surrounding odd tops — page assignments are ESTIMATES,
  writers correct them from the bands):
  981=L104305, 983=L104605, 985=L104835, 987=L105056, 989=L105255, 991=L105458, 993=L105672,
  995=L105868, 997=L106068. Printed span 981–996.

⚠ BANDS: per `manual-review/vol4-column-gutter-parity.md` the vol4 gutter alternates by page
  parity. MEASURE each of pp.981–996 and regenerate at the measured value before dispatching.
  Offset pdf = printed + 20 (pp.1001–1016).

Run: python3.11 tools/rechunk_d48.py
"""
import os, glob, bisect

RAW = "raw/bonaventure_vol4_raw.txt"
VOL = "vol4"
OFF = 20
D = 48

with open(RAW, encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

# Known odd-page tops from running heads.
ODD_TOPS = {981:104305, 983:104605, 985:104835, 987:105056, 989:105255,
            991:105458, 993:105672, 995:105868, 997:106068}

def build_tops(odd):
    """Interpolate the OCR-dropped even-page tops as the midpoint of their neighbours."""
    tops = dict(odd)
    ks = sorted(odd)
    for a, b in zip(ks, ks[1:]):
        tops[a + 1] = (odd[a] + odd[b]) // 2
    return tops

TOPS = build_tops(ODD_TOPS)
PAGES = sorted(TOPS)
STARTS = [TOPS[p] for p in PAGES]

def pages_for(l0, l1):
    """Every page whose [top, next_top) window intersects [l0, l1]."""
    out = []
    for i, p in enumerate(PAGES):
        s = STARTS[i]
        e = STARTS[i + 1] - 1 if i + 1 < len(STARTS) else 10**9
        if s <= l1 and e >= l0:
            out.append(p)
    return out or [PAGES[max(0, bisect.bisect_right(STARTS, l0) - 1)]]

# (id-suffix, type, art, q, title_la, title_en, l0, l1, has_scholion)
CH = [
 ("littera","littera",None,None,
   "Littera Magistri (Lombard), Distinctio XLVIII — De adventu iudicis et de forma in qua apparebit",
   "The text of the Master (Lombard), Distinction XLVIII — On the coming of the judge and the form in which he will appear",
   104392,104641,False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   104642,104695,False),
 ("a1-q1","quaestio",1,1,
   "Utrum potestas iudiciaria sit Christi secundum humanitatem an secundum Divinitatem",
   "Whether the judiciary power belongs to Christ according to his humanity or according to his divinity",
   104696,104902,True),
 ("a1-q2","quaestio",1,2,
   "Utrum Christus in forma Divinitatis apparebit malis",
   "Whether Christ will appear to the wicked in the form of his divinity",
   104903,105060,False),
 ("a1-q3","quaestio",1,3,
   "Utrum Christus apparebit reprobis in forma humanitatis gloriosa",
   "Whether Christ will appear to the reprobate in the glorious form of his humanity",
   105061,105150,False),
 ("a1-q4","quaestio",1,4,
   "Utrum hora iudicii sit nota alicui creaturae",
   "Whether the hour of the judgement is known to any creature",
   105151,105279,False),
 ("a2-q1","quaestio",2,1,
   "Utrum corpora supercaelestia remunerabuntur",
   "Whether the supercelestial bodies will be rewarded",
   105280,105474,True),
 ("a2-q2","quaestio",2,2,
   "Utrum corpora supercaelestia quietabuntur",
   "Whether the supercelestial bodies will come to rest",
   105475,105610,False),
 # ⚠ THE RECOVERED CHUNK — header `QUAESTIO lU.` L105611, opener `Tertio quaeritur` L105614.
 ("a2-q3","quaestio",2,3,
   "Utrum elementa innovabuntur",
   "Whether the elements will be renewed",
   105611,105766,False),
 ("a2-q4","quaestio",2,4,
   "Utrum innovabuntur plantae et animalia bruta",
   "Whether plants and brute animals will be renewed",
   105767,105901,False),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   105902,106122,False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {pp[0]}–{pp[-1]}"
    y = [f'id: "bon-sent-IV-d{D}-{idsuf}"', "volume: 4", "book: 4", f"distinctio: {D}"]
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
    y.append(f'transcription_status: "auto-chunked 2026-07-18 (rechunk_d{D}) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, f"bon-sent-IV-d{D}-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

prev_end = None
for idsuf, typ, art, q, tla, ten, l0, l1, schol in CH:
    assert prev_end is None or l0 == prev_end + 1, f"gap/overlap at {idsuf}: {prev_end} -> {l0}"
    prev_end = l1
    pp = pages_for(l0, l1)
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.{D} {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d{D}-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {os.path.basename(path)}  (L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.{D} skeletons created, contiguous L{CH[0][6]}-{CH[-1][7]}.")
