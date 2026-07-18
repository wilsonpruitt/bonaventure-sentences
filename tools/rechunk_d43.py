#!/usr/bin/env python3.11
"""Create Vol IV d.43 skeletons fresh (SINGLE-PARS, De resurrectione et iudicii conditione —
the pivot into De novissimis / last things). Structure count-verified three ways:
  - TRACTATIO: "duo principaliter" (Part 1 De resurrectione, Part 2 De librorum apertione);
    "Quantum ad primum quaeruntur sex" -> ARTICULUS I has SIX questions.
  - Ordinal openers Primo..Sexto quaeritur all found (q5 opener L94836, header GARBLED).
  - Second-part sub-divisio L95341 ("Consequenter quantum ad secundam partem... Et duo
    quaeruntur: primo de libro vitae, secundo de libris conscientiae") -> Art II + Art III.
ARTICULUS I "De resurrectione" 6q; ARTICULUS II "De libro vitae" 3q; ARTICULUS III
"De libris conscientiae" 3q. Matches the 15 skeletons on disk.
GARBLED HEADERS caught by count-check: Art I QUAESTIO V header garbled (title
"Utrum resurrectio sit naturalis, an miraculosa" L94833, opener L94836);
Art III QUAESTIO II garbled as "QUAESTiO II" (lowercase i, L95815).
SCHOLIA (all OCR "SCHOLIOK"): Art I has TWO blocks — block1 L94125 in a1-q1 (covers Art I
q1-q3), block2 L94719 in a1-q4 (covers Art I q4-q6); Art II block L95475 in a2-q1 (covers
Art II q1-q3); Art III block L95806 ("De 3. quaestione: S. Thom.") in a3-q1 (covers Art III q1-q3).
LITTERA opens at the FOOT of printed p.880 (Cap. I De resurrectione), running head "881" is the
NEXT page; the p.880 NOTAE AD LIBR. SENTENTIARUM footer (L93755, glossing the Master's littera)
is d43-littera's apparatus — d.42-a3-q3 deliberately left it unclaimed.
Offset pdf = printed + 20. Page tops from running heads: 883=L93959, 885=L94187, 887=L94364,
889=L94559, 893=L95011, 895=L95212, 897=L95426, 901=L95854, 903(DUBIA)=L96041.
d.43 = raw L93703 -> DISTINCTIO XLIV at L96182.
Run: python3.11 tools/rechunk_d43.py
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
   "Littera Magistri (Lombard), Distinctio XLIII — De resurrectione et iudicii conditione",
   "The text of the Master (Lombard), Distinction XLIII — On the resurrection and the condition of judgment",
   93703,93884,[880,881,882],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   93885,93965,[882,883],False),
 ("a1-q1","quaestio",1,1,
   "Utrum resurrectio sit futura",
   "Whether the resurrection will be",
   93966,94190,[883,884],True),
 ("a1-q2","quaestio",1,2,
   "Utrum resurrectio sit omnium",
   "Whether the resurrection will be of all",
   94191,94296,[885,886],False),
 ("a1-q3","quaestio",1,3,
   "Utrum resurrectio sit omnium simul, an successive",
   "Whether the resurrection of all will be simultaneous or successive",
   94297,94416,[886,887],False),
 ("a1-q4","quaestio",1,4,
   "Utrum resurrectio sit eorundem secundum numerum",
   "Whether the resurrection will be of the same bodies according to number",
   94417,94830,[887,888,889,890,891,892],True),
 ("a1-q5","quaestio",1,5,
   "Utrum resurrectio sit naturalis, an miraculosa",
   "Whether the resurrection is natural or miraculous",
   94831,95146,[892,893,894],False),
 ("a1-q6","quaestio",1,6,
   "Quae sit causa nostrae resurrectionis",
   "What is the cause of our resurrection",
   95147,95340,[895,896],False),
 ("a2-q1","quaestio",2,1,
   "De quidditate libri vitae",
   "On the quiddity of the book of life",
   95341,95490,[896,897],True),
 ("a2-q2","quaestio",2,2,
   "Utrum in libro vitae omnia scribantur",
   "Whether all things are written in the book of life",
   95491,95585,[897,898],False),
 ("a2-q3","quaestio",2,3,
   "Utrum liber vitae necessario aperietur",
   "Whether the book of life will necessarily be opened",
   95586,95669,[898,899],False),
 ("a3-q1","quaestio",3,1,
   "Utrum in conscientia legantur omnia merita",
   "Whether all merits are read in the conscience",
   95670,95814,[899,900,901],True),
 ("a3-q2","quaestio",3,2,
   "Utrum quilibet legat omnia in conscientia alterius",
   "Whether each one reads all things in the conscience of another",
   95815,95938,[901,902],False),
 ("a3-q3","quaestio",3,3,
   "Utrum omnia videantur simul ab omnibus",
   "Whether all things are seen at once by all",
   95939,96010,[902,903],False),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   96011,96181,[903,904],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d43-{idsuf}"', "volume: 4", "book: 4", "distinctio: 43"]
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
    y.append('transcription_status: "auto-chunked 2026-07-17 (rechunk_d43) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d43-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.43 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d43-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.43 skeletons created.")
