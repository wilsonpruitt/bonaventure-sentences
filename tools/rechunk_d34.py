#!/usr/bin/env python3.11
"""Create Vol IV d.34 skeletons fresh (SINGLE-PARS, De impedimentis matrimonii).
THREE articles x 2 questions:
 Art I De impedimentis in generali (q1 utrum matrimonium habeat impedimentum / q2 de numero et sufficientia),
 Art II De impotentia (q1 impotentia naturalis / q2 impotentia accidentalis per maleficium),
 Art III (q1 utrum furia impediat matrimonium / q2 utrum crimen incestus impediat).
Scholia: a1-q1 (SCHOLION L82448) and a3-q1 (SCHOLIOK L83146); Art II — check per writer.
Recreate all 9 with raw OCR sliced into ## Latin + line_start/line_end so all 3 audits run. Deletes existing d34-* first.
Run: python3.11 tools/rechunk_d34.py
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
   "Littera Magistri (Lombard), Distinctio XXXIV",
   "The text of the Master (Lombard), Distinction XXXIV",
   82111,82280,[765,766,767],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   82281,82364,[767],False),
 ("a1-q1","quaestio",1,1,
   "Utrum matrimonium habeat impedimentum",
   "Whether marriage has any impediment",
   82365,82483,[767,768],True),
 ("a1-q2","quaestio",1,2,
   "De numero et sufficientia impedimentorum matrimonii",
   "On the number and sufficiency of the impediments of marriage",
   82484,82651,[768,769,770],False),
 ("a2-q1","quaestio",2,1,
   "Utrum impotentia naturalis coeundi sit impedimentum matrimonii",
   "Whether natural impotence for intercourse is an impediment to marriage",
   82652,82790,[770,771,772],True),
 ("a2-q2","quaestio",2,2,
   "Utrum impotentia coeundi accidentalis, quae est per maleficium, impediat matrimonium",
   "Whether accidental impotence for intercourse, which is through sorcery, impedes marriage",
   82791,83049,[772,773,774],False),
 ("a3-q1","quaestio",3,1,
   "Utrum furia impediat matrimonium",
   "Whether madness impedes marriage",
   83050,83162,[774,775],True),
 ("a3-q2","quaestio",3,2,
   "Utrum crimen incestus impediat matrimonium et faciat personam illegitimam",
   "Whether the crime of incest impedes marriage and makes the person illegitimate",
   83163,83238,[775,776],False),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   83239,83447,[776,777,778],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d34-{idsuf}"', "volume: 4", "book: 4", "distinctio: 34"]
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
    y.append('transcription_status: "auto-chunked 2026-07-12 (rechunk_d34) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d34-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.34 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d34-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.34 skeletons created.")
