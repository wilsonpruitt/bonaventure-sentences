#!/usr/bin/env python3.11
"""Create Vol IV d.38 skeletons fresh (SINGLE-PARS, De voto — the vow as impediment to marriage).
TWO articles x 3 questions (count verified via TRACTATIO "duo principaliter quaeruntur" + ordinal openers):
 Art I De voto in se: q1 quid sit votum secundum essentiam / q2 de quo sit votum / q3 de materia in qua,
 Art II De obligatione voti: q1 votum continentiae impediat/dirimat matrimonium / q2 votum possit permutari / q3 Summus Pontifex dispensare in voto.
Scholia: a1-q1 (SCHOLIOK L87279), a2-q1 (SCHOLIOK L87778).
Recreate all 9 with raw OCR sliced into ## Latin + line_start/line_end. Deletes existing d38-* first.
Run: python3.11 tools/rechunk_d38.py
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
   "Littera Magistri (Lombard), Distinctio XXXVIII",
   "The text of the Master (Lombard), Distinction XXXVIII",
   86937,87111,[813,814],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   87112,87149,[814],False),
 ("a1-q1","quaestio",1,1,
   "Quid sit votum secundum essentiam",
   "What a vow is according to its essence",
   87150,87290,[814,815,816],True),
 ("a1-q2","quaestio",1,2,
   "De quo sit votum",
   "On what a vow is concerned with",
   87291,87461,[816,817],False),
 ("a1-q3","quaestio",1,3,
   "De materia in qua est votum",
   "On the matter in which a vow consists",
   87462,87593,[817,818,819],False),
 ("a2-q1","quaestio",2,1,
   "Utrum votum continentiae impediat, vel dirimat matrimonium",
   "Whether a vow of continence impedes or dissolves marriage",
   87594,87800,[819,820,821],True),
 ("a2-q2","quaestio",2,2,
   "Utrum votum possit permutari",
   "Whether a vow can be commuted",
   87801,87884,[821,822],False),
 ("a2-q3","quaestio",2,3,
   "Utrum Summus Pontifex possit dispensare in voto",
   "Whether the Supreme Pontiff can dispense in a matter of a vow",
   87885,88094,[822,823,824,825],False),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   88095,88540,[825,826,827,828,829,830],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d38-{idsuf}"', "volume: 4", "book: 4", "distinctio: 38"]
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
    y.append('transcription_status: "auto-chunked 2026-07-12 (rechunk_d38) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d38-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.38 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d38-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.38 skeletons created.")
