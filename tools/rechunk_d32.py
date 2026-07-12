#!/usr/bin/env python3.11
"""Create Vol IV d.32 skeletons fresh (SINGLE-PARS, De solutione debiti coniugalis / the conjugal debt).
FOUR articles: Art I De continentia (q1 post copulam / q2 ante copulam), Art II De redditione debiti (q1 leprosus),
Art III De tempore (q1 menstrua / q2 dies solemnes), Art IV De tempore nuptiarum (q1 tempus observari / q2 separari).
Scholia: a1-q1 (SCHOLIOK L78800, covers Art I q1+q2) and a3-q1 (SCHOLIOl L79341, covers Art III q1+q2);
Art II single-q + Art IV — check for scholion content per-writer. Recreate all 10 with raw OCR sliced
into ## Latin + line_start/line_end so all 3 audits run. Deletes existing d32-* first.
Run: python3.11 tools/rechunk_d32.py
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
   "Littera Magistri (Lombard), Distinctio XXXII",
   "The text of the Master (Lombard), Distinction XXXII",
   78463,78652,[728,729,730],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   78653,78712,[730],False),
 ("a1-q1","quaestio",1,1,
   "Utrum post carnalem copulam possit vir continere, uxore nolente",
   "Whether after carnal union a man may be continent, the wife being unwilling",
   78713,78831,[730,731],True),
 ("a1-q2","quaestio",1,2,
   "Utrum vir ante carnalem commixtionem possit continere, uxore nolente",
   "Whether before carnal union a man may be continent, the wife being unwilling",
   78832,78951,[731,732],False),
 ("a2-q1","quaestio",2,1,
   "Utrum oporteat coniugi debitum reddere, si alter fiat leprosus",
   "Whether one must render the debt to a spouse if the other becomes a leper",
   78952,79132,[732,733,734],False),
 ("a3-q1","quaestio",3,1,
   "Utrum tempore menstruorum possit reddi et peti debitum",
   "Whether during the menstrual period the debt may be rendered and sought",
   79133,79383,[734,735],True),
 ("a3-q2","quaestio",3,2,
   "Utrum tempore dierum solemnium possit licite peti et solvi debitum",
   "Whether during solemn days the debt may licitly be sought and paid",
   79384,79545,[735,736,737],False),
 ("a4-q1","quaestio",4,1,
   "Utrum in celebrandis nuptiis debeat tempus observari",
   "Whether in celebrating nuptials a time ought to be observed",
   79546,79706,[737,738],False),
 ("a4-q2","quaestio",4,2,
   "Utrum matrimonium contractum in tempore indebito debeat separari",
   "Whether a marriage contracted at a forbidden time ought to be separated",
   79707,79798,[738,739,740],False),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   79799,80051,[740,741,742,743,744],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d32-{idsuf}"', "volume: 4", "book: 4", "distinctio: 32"]
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
    y.append('transcription_status: "auto-chunked 2026-07-11 (rechunk_d32) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d32-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.32 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d32-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.32 skeletons created.")
