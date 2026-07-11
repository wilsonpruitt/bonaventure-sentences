#!/usr/bin/env python3.11
"""Create Vol IV d.26 skeletons fresh (single-pars: De Sacramento coniugii —
institution + essence of marriage). Skeletons were incomplete (missing a1-q2) /
mislabeled; recreate all 9 with raw OCR sliced into ## Latin + line_start/line_end.
Art I (De institutione) q1-q3; Art II (De essentia/quid sit) q1-q3.
Deletes existing d26-* first. Run: python3.11 tools/rechunk_d26.py
"""
import os, glob

RAW = "raw/bonaventure_vol4_raw.txt"
VOL = "vol4"
OFF = 20

with open(RAW, encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

# (id-suffix, type, art, q, title_la, title_en, l0, l1, printed_pages)
CH = [
 ("littera","littera",None,None,
   "Littera Magistri (Lombard), Distinctio XXVI",
   "The text of the Master (Lombard), Distinction XXVI",
   71468,71629,[659,660,661]),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   71630,71684,[661]),
 ("a1-q1","quaestio",1,1,
   "Quando matrimonium fuerit institutum",
   "When marriage was instituted",
   71685,71922,[661,662,663,664]),
 ("a1-q2","quaestio",1,2,
   "A quo fuerit matrimonium institutum",
   "By whom marriage was instituted",
   71923,72062,[664,665]),
 ("a1-q3","quaestio",1,3,
   "Utrum institutio matrimonii fuerit sub praecepto",
   "Whether the institution of marriage was under a precept",
   72063,72172,[665,666]),
 ("a2-q1","quaestio",2,1,
   "Quid sit matrimonium",
   "What marriage is",
   72173,72382,[666,667,668]),
 ("a2-q2","quaestio",2,2,
   "De essentia matrimonii, quaestio secunda",
   "On the essence of marriage, second question",
   72383,72555,[668,669,670]),
 ("a2-q3","quaestio",2,3,
   "De essentia matrimonii, quaestio tertia",
   "On the essence of marriage, third question",
   72556,72681,[670,671]),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   72682,72892,[671,672,673]),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d26-{idsuf}"', "volume: 4", "book: 4", "distinctio: 26"]
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
    y.append("has_scholion: false")
    y.append("has_apparatus: true")
    y.append('transcription_status: "auto-chunked 2026-07-05 (rechunk_d26) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d26-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1)
    out += f"\n# d.26 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d26-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]})")

print(f"\n{len(CH)} d.26 skeletons created.")
