#!/usr/bin/env python3.11
"""Create Vol IV d.37 skeletons fresh (SINGLE-PARS, De impedimento ordinis et uxoricidii).
TWO articles x 3 questions (count verified via TRACTATIO "Circa primum quaeruntur tria" + ordinal openers;
BOTH q2 QUAESTIO headers were OCR-garbled — Art I q2 opener L86033, Art II q2 opener L86529):
 Art I De impedimento ordinis: q1 ordines minores / q2 sacer ordo / q3 Ecclesia debuerit instituere,
 Art II De uxoricidio: q1 liceat uxorem adulteram interficere / q2 gravius occidere uxorem quam matrem / q3 uxoricidium impediat.
Scholia: a1-q1 (SCHOLION L85997), a2-q1 (SCHOLIOK L86505).
Recreate all 9 with raw OCR sliced into ## Latin + line_start/line_end. Deletes existing d37-* first.
Run: python3.11 tools/rechunk_d37.py
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
   "Littera Magistri (Lombard), Distinctio XXXVII",
   "The text of the Master (Lombard), Distinction XXXVII",
   85793,85831,[801],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   85832,85888,[801],False),
 ("a1-q1","quaestio",1,1,
   "Utrum ordines minores impediant matrimonium",
   "Whether minor orders impede marriage",
   85889,86032,[801,802,803],True),
 ("a1-q2","quaestio",1,2,
   "Utrum sacer ordo matrimonium impediat",
   "Whether sacred order impedes marriage",
   86033,86149,[803,804],False),
 ("a1-q3","quaestio",1,3,
   "Utrum Ecclesia debuerit instituere ut sacer ordo impediret matrimonium",
   "Whether the Church ought to have instituted that sacred order should impede marriage",
   86150,86405,[804,805,806],False),
 ("a2-q1","quaestio",2,1,
   "Utrum liceat uxorem adulteram interficere",
   "Whether it is licit to kill an adulterous wife",
   86406,86528,[806,807],True),
 ("a2-q2","quaestio",2,2,
   "Utrum gravius sit peccatum occidere uxorem quam matrem",
   "Whether it is a graver sin to kill one's wife than one's mother",
   86529,86675,[807,808,809],False),
 ("a2-q3","quaestio",2,3,
   "Utrum uxoricidium impediat matrimonium",
   "Whether uxoricide impedes marriage",
   86676,86788,[809,810],False),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   86789,86936,[810,811],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d37-{idsuf}"', "volume: 4", "book: 4", "distinctio: 37"]
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
    y.append('transcription_status: "auto-chunked 2026-07-12 (rechunk_d37) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d37-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.37 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d37-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.37 skeletons created.")
