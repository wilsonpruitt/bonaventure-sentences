#!/usr/bin/env python3.11
"""Re-chunk Vol IV d.24 (De ordine / holy orders) from correct raw ranges.
The auto-chunker mislabeled ALL articles as `p2` (only p1-littera was correct) +
left dup2 artifacts, and collapsed the two-pars structure. This creates 21 fresh
skeletons (Pars I: littera, divisio, a1 q1-q4, a2 q1-q4, dubia = 11; Pars II:
divisio, a1 q1-q4, a2 q1-q4, dubia = 10) with the raw OCR sliced into ## Latin,
INCLUDING line_start/line_end so the header + apparatus audits run.
Deletes all existing d24-* skeletons first. Run: python3.11 tools/rechunk_d24.py
"""
import os, glob

RAW = "raw/bonaventure_vol4_raw.txt"
VOL = "vol4"
OFF = 20  # pdf = printed + 20

with open(RAW, encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

# (id-suffix, type, pars, art, q, title_la, title_en, l0, l1, printed_pages)
CH = [
 # ---- PARS I: De ordinis signaculo (tonsura/corona) ----
 ("p1-littera","littera",1,None,None,
   "Littera Magistri (Lombard), Distinctio XXIV",
   "The text of the Master (Lombard), Distinction XXIV",
   65708,66246,[602,603,604,605,606]),
 ("p1-divisio","divisio",1,None,None,
   "Divisio textus et tractatio quaestionum, Pars I",
   "Division of the text and treatment of the questions, Part I",
   66247,66291,[607]),
 ("p1-a1-q1","quaestio",1,1,1,
   "Utrum ordinandi debeant tonsurari sive coronari",
   "Whether those to be ordained ought to be tonsured or crowned",
   66292,66486,[607,608,609]),
 ("p1-a1-q2","quaestio",1,1,2,
   "Utrum, dato quod sic, coronari debeant in modum coronae",
   "Whether, granting they should, they ought to be crowned in the manner of a crown",
   66487,66620,[609,610]),
 ("p1-a1-q3","quaestio",1,1,3,
   "Utrum in susceptione coronae fiat abrenuntiatio temporalium",
   "Whether in receiving the crown there is a renunciation of temporal things",
   66621,66748,[610,611,612]),
 ("p1-a1-q4","quaestio",1,1,4,
   "Utrum Ecclesia talibus teneatur ad temporale subsidium",
   "Whether the Church is bound to such men for temporal support",
   66749,66848,[612,613]),
 ("p1-a2-q1","quaestio",1,2,1,
   "De ordinis Sacramento, quaestio prima",
   "On the Sacrament of order, first question",
   66849,67037,[613,614]),
 ("p1-a2-q2","quaestio",1,2,2,
   "De ordinis Sacramento, quaestio secunda",
   "On the Sacrament of order, second question",
   67038,67202,[614,615,616]),
 ("p1-a2-q3","quaestio",1,2,3,
   "De ordinis Sacramento, quaestio tertia",
   "On the Sacrament of order, third question",
   67203,67312,[617,618]),
 ("p1-a2-q4","quaestio",1,2,4,
   "De ordinis Sacramento, quaestio quarta",
   "On the Sacrament of order, fourth question",
   67313,67381,[618,619]),
 ("p1-dubia","dubia",1,None,None,
   "Dubia circa litteram Magistri, Pars I",
   "Doubts concerning the text of the Master, Part I",
   67382,67574,[619,620,621]),
 # ---- PARS II: De ordinum numero et distinctione ----
 ("p2-divisio","divisio",2,None,None,
   "Commentarius et divisio textus, Pars II",
   "Commentary and division of the text, Part II",
   67575,67644,[621,622]),
 ("p2-a1-q1","quaestio",2,1,1,
   "Utrum in omnibus ordinibus imprimatur character",
   "Whether a character is impressed in all orders",
   67645,67797,[622,623]),
 ("p2-a1-q2","quaestio",2,1,2,
   "Utrum character ordinis sit unus vel plures",
   "Whether the character of order is one or many",
   67798,67937,[623,624,625]),
 ("p2-a1-q3","quaestio",2,1,3,
   "Utrum ordines habeant ordinem ad invicem",
   "Whether the orders have an ordering to one another",
   67938,68109,[625,626,627,628]),
 ("p2-a1-q4","quaestio",2,1,4,
   "De signo exteriore quod characteri respondet",
   "On the exterior sign which corresponds to the character",
   68110,68413,[628,629,630]),
 ("p2-a2-q1","quaestio",2,2,1,
   "De numero et distinctione ordinum, quaestio prima",
   "On the number and distinction of orders, first question",
   68414,68597,[630,631]),
 ("p2-a2-q2","quaestio",2,2,2,
   "De numero et distinctione ordinum, quaestio secunda",
   "On the number and distinction of orders, second question",
   68598,68731,[631,632,633]),
 ("p2-a2-q3","quaestio",2,2,3,
   "De numero et distinctione ordinum, quaestio tertia",
   "On the number and distinction of orders, third question",
   68732,68915,[633,634]),
 ("p2-a2-q4","quaestio",2,2,4,
   "De numero et distinctione ordinum, quaestio quarta",
   "On the number and distinction of orders, fourth question",
   68916,69132,[635,636]),
 ("p2-dubia","dubia",2,None,None,
   "Dubia circa litteram Magistri, Pars II",
   "Doubts concerning the text of the Master, Part II",
   69133,69352,[637,638]),
]

def fm(idsuf, typ, pars, art, q, tla, ten, pp, l0, l1):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d24-{idsuf}"', "volume: 4", "book: 4", "distinctio: 24", f"pars: {pars}"]
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
    y.append('transcription_status: "auto-chunked 2026-07-05 (rechunk_d24) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

# delete every existing d24 skeleton (mislabeled p2 + dup2)
for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d24-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, pars, art, q, tla, ten, l0, l1, pp in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, pars, art, q, tla, ten, pp, l0, l1)
    out += f"\n# d.24 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d24-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]})")

print(f"\n{len(CH)} d.24 skeletons created.")
