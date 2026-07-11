#!/usr/bin/env python3.11
"""Re-chunk Vol IV d.21 from correct raw ranges (auto-chunker mislabeled all
Pars I articles as p2 + left dup2 artifacts). Creates 16 fresh skeletons with
the raw OCR sliced into the ## Latin block; deletes the mislabeled ones.
Run: python3.11 tools/rechunk_d21.py
"""
import os, glob, re

RAW = "raw/bonaventure_vol4_raw.txt"
VOL = "vol4"
OFF = 20  # pdf = printed + 20

with open(RAW, encoding="utf-8", errors="replace") as f:
    lines = f.readlines()  # 1-indexed via lines[n-1]

# (id-suffix, type, pars, art, q, title_la, title_en, l0, l1, printed_pages)
CH = [
 ("p1-littera","littera",1,None,None,
   "Littera Magistri (Lombard), Distinctio XXI",
   "The text of the Master (Lombard), Distinction XXI",
   60021,60250,[543,544,545]),
 ("p1-divisio","divisio",1,None,None,
   "Divisio textus et tractatio quaestionum, Pars I",
   "Division of the text and treatment of the questions, Part I",
   60251,60291,[545]),
 ("p1-a1-q1","quaestio",1,1,1,
   "Utrum peccata venialia possint deleri sine gratia",
   "Whether venial sins can be destroyed without grace",
   60292,60490,[545,546,547]),
 ("p1-a1-q2","quaestio",1,1,2,
   "Utrum peccata venialia possint deleri a gratia sine contritione sive interiore poena",
   "Whether venial sins can be destroyed by grace without contrition or interior pain",
   60491,60693,[547,548,549]),
 ("p1-a2-q1","quaestio",1,2,1,
   "Utrum in purgatorio post hanc vitam fiat purgatio aliqua ab aliqua culpa, an solum a poena",
   "Whether in purgatory after this life there is any purgation from any fault, or only from pain",
   60694,60970,[549,550,551]),
 ("p1-a2-q2","quaestio",1,2,2,
   "Utrum purgatio purgatorii fiat per ignem materialem",
   "Whether the purgation of purgatory takes place through material fire",
   60971,61168,[551,552,553]),
 ("p1-a3-q1","quaestio",1,3,1,
   "Utrum in purgatorio unus liberetur ante alium",
   "Whether in purgatory one is freed before another",
   61169,61318,[553,554,555]),
 ("p1-a3-q2","quaestio",1,3,2,
   "Utrum aliquis Sanctorum evolet in caelum ante iudicium",
   "Whether any of the saints flies up into heaven before the judgment",
   61319,61436,[555,556,557]),
 ("p1-dubia","dubia",1,None,None,
   "Dubia circa litteram Magistri, Pars I",
   "Doubts concerning the text of the Master, Part I",
   61437,61584,[557,558,559]),
 ("p2-divisio","divisio",2,None,None,
   "Divisio textus et tractatio quaestionum, Pars II",
   "Division of the text and treatment of the questions, Part II",
   61585,61624,[559,561]),
 ("p2-a1-q1","quaestio",2,1,1,
   "Utrum liceat aliquod peccatum in confessione omittere",
   "Whether it is licit to omit any sin in confession",
   61625,61818,[561]),
 ("p2-a1-q2","quaestio",2,1,2,
   "Utrum liceat aliquid in confessione addere",
   "Whether it is licit to add anything in confession",
   61819,62112,[561,562,563]),
 ("p2-a2-q1","quaestio",2,2,1,
   "Utrum in aliquo casu liceat confessionem revelare",
   "Whether in any case it is licit to reveal a confession",
   62113,62284,[563,564,565]),
 ("p2-a2-q2","quaestio",2,2,2,
   "Utrum confitens possit sacerdotem licentiare, ut revelet",
   "Whether the one confessing can license the priest to reveal it",
   62285,62356,[565]),
 ("p2-a2-q3","quaestio",2,2,3,
   "Utrum sciens aliquid per confessionem et per aliam viam teneatur celare",
   "Whether one who knows something both through confession and through another way is bound to conceal it",
   62357,62582,[565,566,567]),
 ("p2-dubia","dubia",2,None,None,
   "Dubia circa litteram Magistri, Pars II",
   "Doubts concerning the text of the Master, Part II",
   62583,62760,[569,570,571]),
]

# delete all existing d21 skeleton/dup files
for p in glob.glob(f"{VOL}/bon-sent-IV-d21-*.md"):
    os.remove(p)
    print("deleted", os.path.basename(p))

for suf, typ, pars, art, q, tla, ten, l0, l1, pp in CH:
    cid = f"bon-sent-IV-d21-{suf}"
    pdfpp = [p + OFF for p in pp]
    body = "".join(lines[l0-1:l1])
    fm = [f'---',
          f'id: "{cid}"',
          f'volume: 4', f'book: 4', f'distinctio: 21']
    if pars: fm.append(f'pars: {pars}')
    if art:  fm.append(f'articulus: {art}')
    if q:    fm.append(f'quaestio: {q}')
    fm += [f'type: {typ}',
           f'title_la: "{tla}"',
           f'title_en: "{ten}"',
           f'printed_pages: {pp}',
           f'pdf_pages: {pdfpp}',
           f'source: "S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), '
           f'pp. {pp[0]}–{pp[-1]}"',
           f'has_scholion: false',
           f'has_apparatus: true',
           f'line_start: {l0}', f'line_end: {l1}',
           f'transcription_status: "auto-rechunked 2026-06-23 (raw lines {l0}–{l1})"',
           f'format_version: 1', '---', '']
    out = "\n".join(fm) + f"\n# {cid}\n\n## Latin\n\n" + body + "\n"
    with open(f"{VOL}/{cid}.md", "w", encoding="utf-8") as g:
        g.write(out)
    print("wrote", cid, f"L{l0}-{l1}", pp)

print(f"\n{len(CH)} fresh d.21 skeletons written.")
