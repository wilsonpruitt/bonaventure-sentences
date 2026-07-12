#!/usr/bin/env python3.11
"""Create Vol IV d.36 skeletons fresh (SINGLE-PARS, De impedimento conditionis servitutis et aetatis).
TWO articles x 3 questions (count verified via TRACTATIO "quaeruntur tria" + ordinal openers; two QUAESTIO
headers were OCR-garbled — Art I q3 'QU.\\ESTIO III' L85107, Art II q3 titles garbled):
 Art I De conditione servitutis: q1 cum contradictione domini / q2 cum errore / q3 cuius conditionem sequatur proles,
 Art II De aetate: q1 status aetatis / q2 defectus aetatis / q3 sponsalia post septennium dissolvi.
Scholion: a2-q1 (SCHOLIOK L85329). Art I — no scholion found; a1-q1 writer checks by content.
Recreate all 9 with raw OCR sliced into ## Latin + line_start/line_end. Deletes existing d36-* first.
Run: python3.11 tools/rechunk_d36.py
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
   "Littera Magistri (Lombard), Distinctio XXXVI",
   "The text of the Master (Lombard), Distinction XXXVI",
   84662,84799,[790,791],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   84800,84837,[791],False),
 ("a1-q1","quaestio",1,1,
   "Utrum conditio servitutis cum contradictione domini impediat matrimonium",
   "Whether the condition of servitude, with the master objecting, impedes marriage",
   84838,85013,[791,792,793],False),
 ("a1-q2","quaestio",1,2,
   "Utrum conditio servitutis cum errore impediat matrimonium",
   "Whether the condition of servitude with error impedes marriage",
   85014,85106,[793,794],False),
 ("a1-q3","quaestio",1,3,
   "Utrum conditio prolis sequatur patrem, an matrem",
   "Whether the condition of the offspring follows the father or the mother",
   85107,85225,[794,795],False),
 ("a2-q1","quaestio",2,1,
   "Utrum status aetatis impediat matrimonium",
   "Whether the state of age impedes marriage",
   85226,85353,[795,796],True),
 ("a2-q2","quaestio",2,2,
   "Utrum defectus aetatis impediat contractionem sponsalium",
   "Whether defect of age impedes the contracting of betrothal",
   85354,85425,[796,797],False),
 ("a2-q3","quaestio",2,3,
   "Utrum sponsalia contracta post septennium possint dissolvi per mutuum consensum",
   "Whether betrothals contracted after the seventh year can be dissolved by mutual consent",
   85426,85586,[797,798,799],False),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   85587,85792,[799,800],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d36-{idsuf}"', "volume: 4", "book: 4", "distinctio: 36"]
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
    y.append('transcription_status: "auto-chunked 2026-07-12 (rechunk_d36) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d36-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.36 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d36-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.36 skeletons created.")
