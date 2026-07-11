#!/usr/bin/env python3.11
"""Create Vol IV d.25 skeletons fresh (single-pars: De ministris ordinum + De
suscipientibus). Skeletons were incomplete (divisio + a2-q3 missing) and possibly
mislabeled; recreate all 11 with raw OCR sliced into ## Latin + line_start/line_end
so all 3 audits run. Deletes existing d25-* first. Run: python3.11 tools/rechunk_d25.py
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
   "Littera Magistri (Lombard), Distinctio XXV",
   "The text of the Master (Lombard), Distinction XXV",
   69353,69540,[638,639,640,641]),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   69541,69575,[641]),
 ("a1-q1","quaestio",1,1,
   "Utrum solus episcopus possit ordinare",
   "Whether only a bishop can ordain",
   69576,69909,[641,642,643,644]),
 ("a1-q2","quaestio",1,2,
   "Utrum episcopus haereticus possit ordinare",
   "Whether a heretical bishop can ordain",
   69910,70029,[644,645]),
 ("a1-q3","quaestio",1,3,
   "Utrum simoniacus episcopus aliquem ordinem possit vendere",
   "Whether a simoniac bishop can sell an order",
   70030,70164,[645,646,647]),
 ("a1-q4","quaestio",1,4,
   "De ministris ordinum, quaestio quarta",
   "On the ministers of orders, fourth question",
   70165,70412,[647,648,649]),
 ("a2-q1","quaestio",2,1,
   "Utrum ad susceptionem ordinis requiratur sexus virilis",
   "Whether the male sex is required for receiving an order",
   70413,70617,[649,650,651]),
 ("a2-q2","quaestio",2,2,
   "Utrum ad susceptionem ordinis necessarius sit usus rationis",
   "Whether the use of reason is necessary for receiving an order",
   70618,70859,[651,652,653]),
 ("a2-q3","quaestio",2,3,
   "Utrum ad susceptionem ordinis sit necessaria indivisio carnis",
   "Whether integrity of the flesh is necessary for receiving an order",
   70860,71065,[653,654,655]),
 ("a2-q4","quaestio",2,4,
   "Utrum ad susceptionem ordinis sit necessaria conditio libertatis",
   "Whether the condition of freedom is necessary for receiving an order",
   71066,71216,[655,656]),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   71217,71443,[656,657,658]),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d25-{idsuf}"', "volume: 4", "book: 4", "distinctio: 25"]
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
    y.append('transcription_status: "auto-chunked 2026-07-05 (rechunk_d25) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d25-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1)
    out += f"\n# d.25 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d25-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]})")

print(f"\n{len(CH)} d.25 skeletons created.")
