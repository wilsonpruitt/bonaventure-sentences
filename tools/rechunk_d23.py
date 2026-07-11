#!/usr/bin/env python3.11
"""Create Vol IV d.23 (De extrema unctione) skeletons from raw ranges.
The auto-chunker MERGED d.23 into neighbors (no d23 skeletons existed), so all
11 chunks are created fresh with the raw OCR sliced into the ## Latin block.
Single-pars: littera, divisio, Art I q1-q4, Art II q1-q4, dubia.
Titles are provisional (writers finalize from bands). Run: python3.11 tools/rechunk_d23.py
"""
import os

RAW = "raw/bonaventure_vol4_raw.txt"
VOL = "vol4"
OFF = 20  # pdf = printed + 20

with open(RAW, encoding="utf-8", errors="replace") as f:
    lines = f.readlines()  # 1-indexed via lines[n-1]

# (id-suffix, type, art, q, title_la, title_en, l0, l1, printed_pages)
CH = [
 ("littera","littera",None,None,
   "Littera Magistri (Lombard), Distinctio XXIII",
   "The text of the Master (Lombard), Distinction XXIII",
   64093,64206,[586,587]),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   64207,64260,[587]),
 ("a1-q1","quaestio",1,1,
   "Utrum Sacramentum extremae unctionis principaliter sit ordinatum ad remedium",
   "Whether the Sacrament of extreme unction is principally ordained as a remedy",
   64261,64501,[587,588,589,590]),
 ("a1-q2","quaestio",1,2,
   "Utrum hoc Sacramentum fuerit institutum a Christo, an ab aliquo eius discipulo",
   "Whether this Sacrament was instituted by Christ, or by one of his disciples",
   64502,64679,[590,591,592]),
 ("a1-q3","quaestio",1,3,
   "Utrum materia huius Sacramenti sit oleum",
   "Whether the matter of this Sacrament is oil",
   64680,64881,[592,593,594]),
 ("a1-q4","quaestio",1,4,
   "Utrum forma verbi sit de essentia Sacramenti",
   "Whether the form of the word belongs to the essence of the Sacrament",
   64882,65058,[594,595,596]),
 ("a2-q1","quaestio",2,1,
   "Utrum hoc Sacramentum debeat conferri per solum sacerdotem",
   "Whether this Sacrament ought to be conferred by a priest alone",
   65059,65270,[596,597,598,599]),
 ("a2-q2","quaestio",2,2,
   "Utrum cui debeat hoc Sacramentum conferri",
   "To whom this Sacrament ought to be conferred",
   65271,65374,[599,600]),
 ("a2-q3","quaestio",2,3,
   "Utrum in quibus partibus corporis debeat fieri unctio",
   "On which parts of the body the unction ought to be made",
   65375,65499,[600,601,602]),
 ("a2-q4","quaestio",2,4,
   "Utrum hoc Sacramentum debeat iterari",
   "Whether this Sacrament ought to be repeated",
   65500,65557,[602,603]),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   65558,65707,[603,604,605,606]),
]

def fm(idsuf, typ, art, q, tla, ten, pp):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d23-{idsuf}"', "volume: 4", "book: 4", "distinctio: 23"]
    if art is not None: y.append(f"articulus: {art}")
    if q is not None: y.append(f"quaestio: {q}")
    y.append(f"type: {typ}")
    y.append(f'title_la: "{tla}"')
    y.append(f'title_en: "{ten}"')
    y.append(f"printed_pages: {pp}")
    y.append(f"pdf_pages: {pdf}")
    y.append(f'source: "{src}"')
    y.append("has_scholion: false")
    y.append("has_apparatus: true")
    y.append('transcription_status: "auto-chunked 2026-07-04 (rechunk_d23) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for idsuf, typ, art, q, tla, ten, l0, l1, pp in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp)
    out += f"\n# d.23 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d23-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]})")

print(f"\n{len(CH)} d.23 skeletons created.")
