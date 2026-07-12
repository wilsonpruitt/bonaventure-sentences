#!/usr/bin/env python3.11
"""Create Vol IV d.35 skeletons fresh (SINGLE-PARS, De divortio / dimissione uxoris ex causa fornicationis).
ARTICULUS UNICUS with 4 questions:
 q1 utrum liceat uxorem dimittere ex causa fornicationis,
 q2 utrum dimittere uxorem fornicariam sit in praecepto,
 q3 utrum possit aliquis uxorem fornicantem dimittere propria auctoritate,
 q4 utrum divortio celebrato vir possit aliam uxorem ducere.
TWO scholia: L83779 (in a1-q1, covers early q's) and L84205 (in a1-q4, covers later q's) — writers confirm coverage.
+ DUBIA (raw L84485, "DIST. XXXV. DUBIA"). Recreate all 7 with raw OCR sliced into ## Latin + line_start/line_end.
Deletes existing d35-* first. Run: python3.11 tools/rechunk_d35.py
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
   "Littera Magistri (Lombard), Distinctio XXXV",
   "The text of the Master (Lombard), Distinction XXXV",
   83448,83596,[778,779,780],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   83597,83633,[780],False),
 ("a1-q1","quaestio",1,1,
   "Utrum liceat uxorem dimittere ex causa fornicationis",
   "Whether it is licit to dismiss a wife for the cause of fornication",
   83634,83811,[780,781,782],True),
 ("a1-q2","quaestio",1,2,
   "Utrum dimittere uxorem fornicariam sit in praecepto",
   "Whether to dismiss an adulterous wife is a matter of precept",
   83812,83908,[782,783],False),
 ("a1-q3","quaestio",1,3,
   "Utrum possit aliquis uxorem fornicantem dimittere propria auctoritate",
   "Whether anyone may dismiss an adulterous wife on his own authority",
   83909,84102,[783,784,785],False),
 ("a1-q4","quaestio",1,4,
   "Utrum, divortio celebrato, vir possit aliam uxorem ducere, vel uxor alium virum",
   "Whether, once a divorce has been celebrated, the man may take another wife, or the wife another husband",
   84103,84484,[785,786,787,788,789],True),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   84485,84661,[789,790],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d35-{idsuf}"', "volume: 4", "book: 4", "distinctio: 35"]
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
    y.append('transcription_status: "auto-chunked 2026-07-12 (rechunk_d35) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d35-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.35 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d35-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.35 skeletons created.")
