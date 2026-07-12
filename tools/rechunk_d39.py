#!/usr/bin/env python3.11
"""Create Vol IV d.39 skeletons fresh (SINGLE-PARS, De dispari cultu / solutione matrimonii propter infidelitatem).
TWO articles x 4 questions (count verified; NO dubia section):
 Art I De matrimonio inter fidelem et infidelem: q1 contrahi inter fidelem et infidelem / q2 Sacramentum inter infideles /
   q3 matrimonium infidelium excuset coitum / q4 matrimonium ante baptismum ponat in numerum Sacramentorum,
 Art II De solutione matrimonii propter infidelitatem: q1 solvatur quoad fidelem / q2 altero veniente ad fidem /
   q3 si alter fit infidelis / q4 in infidelibus venientibus ad fidem.
Scholia: a1-q1 (SCHOLIOK L88980), a2-q1 (SCHOLIOK L89586). NO dubia (verified — none between a2-q4 and DISTINCTIO XL L90113).
Recreate all 10 with raw OCR sliced into ## Latin + line_start/line_end. Deletes existing d39-* first.
Run: python3.11 tools/rechunk_d39.py
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
   "Littera Magistri (Lombard), Distinctio XXXIX",
   "The text of the Master (Lombard), Distinction XXXIX",
   88541,88791,[830,831],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   88792,88851,[831],False),
 ("a1-q1","quaestio",1,1,
   "Utrum matrimonium possit contrahi inter fidelem et infidelem",
   "Whether marriage can be contracted between a believer and an infidel",
   88852,89018,[831,832,833],True),
 ("a1-q2","quaestio",1,2,
   "Utrum Sacramentum matrimonii possit contrahi inter infideles",
   "Whether the sacrament of marriage can be contracted between infidels",
   89019,89121,[833,834],False),
 ("a1-q3","quaestio",1,3,
   "Utrum matrimonium infidelium excuset coitum, ut non sit ibi peccatum",
   "Whether the marriage of infidels excuses intercourse, so that there is no sin in it",
   89122,89299,[834,835,836],False),
 ("a1-q4","quaestio",1,4,
   "Utrum matrimonium contractum ante baptismum ponat in numerum Sacramentorum",
   "Whether marriage contracted before baptism places one among the sacraments",
   89300,89451,[836,837],False),
 ("a2-q1","quaestio",2,1,
   "Utrum per infidelitatem solvatur matrimonium quoad fidelem coniugem",
   "Whether through infidelity the marriage is dissolved with respect to the believing spouse",
   89452,89604,[837,838,839],True),
 ("a2-q2","quaestio",2,2,
   "Utrum, altero tantum infidelium veniente ad fidem, matrimonium solvatur",
   "Whether, when only one of the infidels comes to the faith, the marriage is dissolved",
   89605,89692,[839,840],False),
 ("a2-q3","quaestio",2,3,
   "Utrum matrimonium solvatur, si alter coniugum fit infidelis",
   "Whether the marriage is dissolved if one of the spouses becomes an infidel",
   89693,89776,[840,841],False),
 ("a2-q4","quaestio",2,4,
   "Utrum in infidelibus venientibus ad fidem solvatur matrimonium",
   "Whether among infidels coming to the faith the marriage is dissolved",
   89777,90112,[841,842,843,844],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d39-{idsuf}"', "volume: 4", "book: 4", "distinctio: 39"]
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
    y.append('transcription_status: "auto-chunked 2026-07-12 (rechunk_d39) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d39-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.39 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d39-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.39 skeletons created.")
