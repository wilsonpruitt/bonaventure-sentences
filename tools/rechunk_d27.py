#!/usr/bin/env python3.11
"""Create Vol IV d.27 skeletons fresh (single-pars, 3 articles x 2 questions:
De matrimonio [definitio] / De consensu / De insolubilitate). Recreate all 9 with
raw OCR sliced into ## Latin + line_start/line_end. Scholia in a1-q1 (Art I) and
a3-q1 (Art III); Art II has none. Deletes existing d27-* first.
Run: python3.11 tools/rechunk_d27.py
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
   "Littera Magistri (Lombard), Distinctio XXVII",
   "The text of the Master (Lombard), Distinction XXVII",
   72893,73070,[672,673,674]),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   73071,73131,[674]),
 ("a1-q1","quaestio",1,1,
   "Utrum matrimonium sit coniunctio maris et feminae",
   "Whether marriage is the union of male and female",
   73132,73309,[674,675,676]),
 ("a1-q2","quaestio",1,2,
   "De matrimonio secundum nomen et rationem, quaestio secunda",
   "On marriage according to its name and account, second question",
   73310,73445,[676,677]),
 ("a2-q1","quaestio",2,1,
   "De consensu matrimoniali, quaestio prima",
   "On matrimonial consent, first question",
   73446,73539,[677,678]),
 ("a2-q2","quaestio",2,2,
   "Utrum ad contrahendum matrimonium sufficiat consensus vocalis",
   "Whether vocal consent suffices to contract marriage",
   73540,73716,[678,679,680]),
 ("a3-q1","quaestio",3,1,
   "Utrum matrimonium consummatum sit insolubile",
   "Whether a consummated marriage is indissoluble",
   73717,73870,[680,681,682]),
 ("a3-q2","quaestio",3,2,
   "De insolubilitate matrimonii, quaestio secunda",
   "On the indissolubility of marriage, second question",
   73871,73994,[682,683,684]),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   73995,74278,[684,685,686]),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d27-{idsuf}"', "volume: 4", "book: 4", "distinctio: 27"]
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
    y.append('transcription_status: "auto-chunked 2026-07-05 (rechunk_d27) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d27-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1)
    out += f"\n# d.27 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d27-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]})")

print(f"\n{len(CH)} d.27 skeletons created.")
