#!/usr/bin/env python3.11
"""Create Vol IV d.40 skeletons fresh (SINGLE-PARS, De cognatione carnali / consanguinitate et gradibus).
ARTICULUS UNICUS x 3 questions (count verified three ways: QUAESTIO headers L90351/L90578/L90754;
"Tertio quaeritur" opener L90759; scholion doctor-lists "De 1. et 2. quaestione" + "De 3. quaestione").
Scholion: ONE block at L90557 (OCR "SCHOLIOK"), sits in q1's tail -> a1-q1 OWNS it and renders BOTH
sections (§I covers q1+q2, §II covers q3); q2 and q3 render none.
COMMENTARIUS header OCR'd "C0MMENTARIU8 IN DI8TINCTI0NEM XL." (L90204) -> divisio chunk.
TRACTATIO QUAESTIONUM here opens with a long PRAENOTATA (definitions of consanguinitas / linea / gradus
+ three notulae) -> belongs to the divisio chunk.
DUBIA: L90956 (DUBIA CIRCA LITTERAM MAGISTRI) -> at least Dub I-V; the section is two-column OCR-merged
and DUB. III/IV headers are NOT greppable -> the dubia writer MUST count them off the PDF bands.
The L91100 "DISTINCTIO XLI. 85b" is a running-head BLEED (d.40 dubia continue past it: DuB. V at L91119);
the real d.41 header is L91127.
Recreate all 6 with raw OCR sliced into ## Latin + line_start/line_end (so all 3 audits run).
Deletes existing d40-* first.
Run: python3.11 tools/rechunk_d40.py
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
   "Littera Magistri (Lombard), Distinctio XL",
   "The text of the Master (Lombard), Distinction XL",
   90113,90203,[844,845],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum (cum praenotatis)",
   "Division of the text and treatment of the questions (with the preliminary notes)",
   90204,90350,[845,846,847],False),
 ("a1-q1","quaestio",1,1,
   "Utrum consanguinitas sit aliquod vinculum",
   "Whether consanguinity is some bond",
   90351,90577,[847,848,849],True),
 ("a1-q2","quaestio",1,2,
   "Utrum consanguinitas matrimonio praestet impedimentum",
   "Whether consanguinity poses an impediment to marriage",
   90578,90753,[849,850,851],False),
 ("a1-q3","quaestio",1,3,
   "Usque ad quem gradum se extendat impedimentum consanguinitatis",
   "To what degree the impediment of consanguinity extends",
   90754,90955,[851,852,853],False),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   90956,91126,[853,854,855,856],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d40-{idsuf}"', "volume: 4", "book: 4", "distinctio: 40"]
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
    y.append('transcription_status: "auto-chunked 2026-07-13 (rechunk_d40) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d40-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.40 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d40-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.40 skeletons created.")
