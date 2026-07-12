#!/usr/bin/env python3.11
"""Create Vol IV d.31 skeletons fresh (SINGLE-PARS, De bonis coniugii, 2 articles x 3 questions).
Art I (De bonis coniugii): q1 tria bona / q2 numerus et sufficientia / q3 de necessitate.
Art II (De actu coniugali): q1 coitus propter prolem / q2 causa fornicationis vitandae / q3 ratione concupiscentiae.
Scholia: a1-q1 (SCHOLION L77372) and a2-q1 (SCHOLIOK L77905). Recreate all 9 with raw OCR
sliced into ## Latin + line_start/line_end so all 3 audits run. Deletes existing d31-* first.
Run: python3.11 tools/rechunk_d31.py
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
   "Littera Magistri (Lombard), Distinctio XXXI",
   "The text of the Master (Lombard), Distinction XXXI",
   76939,77222,[713,714,715,716],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   77223,77277,[716,717],False),
 ("a1-q1","quaestio",1,1,
   "Utrum tria sint matrimonii bona",
   "Whether there are three goods of marriage",
   77278,77448,[717,718],True),
 ("a1-q2","quaestio",1,2,
   "De numero et sufficientia bonorum matrimonii",
   "On the number and sufficiency of the goods of marriage",
   77449,77563,[718,719,720],False),
 ("a1-q3","quaestio",1,3,
   "Utrum haec tria bona sint de necessitate matrimonii",
   "Whether these three goods are of the necessity of marriage",
   77564,77694,[720,721],False),
 ("a2-q1","quaestio",2,1,
   "Utrum coitus propter prolem possit esse sine omni culpa",
   "Whether intercourse for the sake of offspring can be without all fault",
   77695,78000,[721,722,723],True),
 ("a2-q2","quaestio",2,2,
   "Utrum coitus coniugalis causa fornicationis vitandae possit esse sine omni peccato veniali",
   "Whether conjugal intercourse for the sake of avoiding fornication can be without all venial sin",
   78001,78086,[723,724,725],False),
 ("a2-q3","quaestio",2,3,
   "Utrum coire cum uxore ratione concupiscentiae satiandae sit semper peccatum mortale",
   "Whether to have intercourse with one's wife for the sake of satisfying concupiscence is always a mortal sin",
   78087,78228,[725,726],False),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   78229,78462,[726,727],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d31-{idsuf}"', "volume: 4", "book: 4", "distinctio: 31"]
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
    y.append('transcription_status: "auto-chunked 2026-07-11 (rechunk_d31) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d31-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.31 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d31-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.31 skeletons created.")
