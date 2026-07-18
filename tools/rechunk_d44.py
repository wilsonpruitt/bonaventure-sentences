#!/usr/bin/env python3.11
"""Create Vol IV d.44 skeletons fresh (TWO-PARS, De resurrectione quantum ad modum / De poena
damnatorum). Structure count-verified:
  - Pars I TRACTATIO (L96455): "tria principaliter quaeruntur" -> 3 articles; each "Circa primum
    quaeruntur duo" -> 2 questions per article. ARTICULUS I "Quid resurgat in corpore humano",
    II "Quid in quo resurgat", III "Qualia futura sint corpora resurgentium".
  - Pars II TRACTATIO (L97847): "tria quaeruntur" -> 3 articles; 2 q each. ART I "De existentia
    et loco inferni", II "De quidditate poenae infernalis", III "De actione ignis".
  - Ordinal openers + QUAESTIO headers + scholion "SCHOLIOK/SCHOLION" all cross-checked.
GARBLED HEADERS: Pars I Art II "ARTIGULUS 11" (L96776) + "QUAESTIO -I" (L96787); Pars I Art III
"ARTIGULUS"; Pars II Art I header garbled ("ARTlCUtUS..l." ~L97869) + Art III "ARTIGULUS III".
SCHOLIA (one per article, in that article's q1, covers q1+q2): Pars I a1-q1 L96630, a2-q1 L97063,
a3-q1 L97374; Pars II a1-q1 L98224, a2-q1 L98662, a3-q1 L99008.
DUBIA both pars cascade-merged (count off the 450dpi bands): Pars I greppable DUB I/II/III;
Pars II only DUB II greppable.
LITTERA opens at TOP of p.904 (Cap. I De aetate et statura resurgentium), Master's own Pars I
(Caps I-IV) + Pars II (Caps V-VII). The p.904 NOTAE AD LIBR. SENTENTIARUM footer (Eph 4:13/Haymo,
De Civ. Dei XXII c.15...) is d44-LITTERA's apparatus; the numbered footers [^p904-1..7] above it
were already claimed by d43-dubia (De resurrectione dubia tail). No double-claim.
Offset pdf = printed + 20. Page tops from running heads: 907=L96434, 909=L96626, 911=L96853,
913=L97128, 915=L97312, [P.I DUBIA]=L97545; 919=L97733, 921=L97989, 923=L98204, 925=L98407,
927=L98648, 929=L98830, 931=L99003, 933=L99182, [P.II DUBIA]=L99451.
d.44 = raw L96182 -> DISTINCTIO XLV at L99733.
Run: python3.11 tools/rechunk_d44.py
"""
import os, glob

RAW = "raw/bonaventure_vol4_raw.txt"
VOL = "vol4"
OFF = 20

with open(RAW, encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

# (id-suffix, pars, type, art, q, title_la, title_en, l0, l1, printed_pages, has_scholion)
CH = [
 # ---- PARS I: De aetate et statura resurgentium ----
 ("p1-littera",1,"littera",None,None,
   "Littera Magistri (Lombard), Distinctio XLIV — De aetate et statura resurgentium",
   "The text of the Master (Lombard), Distinction XLIV — On the age and stature of those who rise",
   96182,96400,[904,905,906],False),
 ("p1-divisio",1,"divisio",None,None,
   "Divisio textus et tractatio quaestionum (Pars I)",
   "Division of the text and treatment of the questions (Part I)",
   96401,96463,[906,907],False),
 ("p1-a1-q1",1,"quaestio",1,1,
   "Utrum humores resurgant",
   "Whether the humors rise again",
   96464,96653,[907,908],True),
 ("p1-a1-q2",1,"quaestio",1,2,
   "Utrum resurgant quae spectant ad superfluitatem, ut sunt intestina, capilli et ungues",
   "Whether those things rise again which pertain to superfluity, such as the intestines, hair, and nails",
   96654,96775,[909,910],False),
 ("p1-a2-q1",1,"quaestio",2,1,
   "Utrum caro, quae est in duobus hominibus caro, resurgat caro in primo, vel in secundo",
   "Whether flesh which is flesh in two men rises again as flesh in the first or in the second",
   96776,97140,[911,912],True),
 ("p1-a2-q2",1,"quaestio",2,2,
   "Utrum materia uniuscuiusque membri resurgat in suo, an indifferenter in quolibet",
   "Whether the matter of each member rises again in its own [member], or indifferently in any",
   97141,97252,[913],False),
 ("p1-a3-q1",1,"quaestio",3,1,
   "Utrum corpora electorum resurgant cum deformitatibus",
   "Whether the bodies of the elect rise again with deformities",
   97253,97388,[913,914],True),
 ("p1-a3-q2",1,"quaestio",3,2,
   "Utrum deformitates resurgant in corporibus damnatorum",
   "Whether deformities rise again in the bodies of the damned",
   97389,97559,[915,916],False),
 ("p1-dubia",1,"dubia",None,None,
   "Dubia circa litteram Magistri (Pars I)",
   "Doubts concerning the text of the Master (Part I)",
   97560,97732,[917,918],False),
 # ---- PARS II: De poena damnatorum / infernus ----
 ("p2-divisio",2,"divisio",None,None,
   "Divisio textus et tractatio quaestionum (Pars II)",
   "Division of the text and treatment of the questions (Part II)",
   97733,97868,[919,920],False),
 ("p2-a1-q1",2,"quaestio",1,1,
   "Utrum sit infernus",
   "Whether there is a hell",
   97869,98248,[920,921,922],True),
 ("p2-a1-q2",2,"quaestio",1,2,
   "Ubi sit infernus",
   "Where hell is",
   98249,98417,[923,924],False),
 ("p2-a2-q1",2,"quaestio",2,1,
   "Utrum ignis inferni sit verus ignis",
   "Whether the fire of hell is a true fire",
   98418,98676,[925,926],True),
 ("p2-a2-q2",2,"quaestio",2,2,
   "Utrum puniens in inferno sit solus ignis",
   "Whether that which punishes in hell is fire alone",
   98677,98787,[927],False),
 ("p2-a3-q1",2,"quaestio",3,1,
   "Utrum ignis inferni consumat corpora damnatorum",
   "Whether the fire of hell consumes the bodies of the damned",
   98788,99058,[927,928,929,930],True),
 ("p2-a3-q2",2,"quaestio",3,2,
   "Utrum ignis inferni affligat spiritum",
   "Whether the fire of hell afflicts the spirit",
   99059,99450,[931,932,933,934],False),
 ("p2-dubia",2,"dubia",None,None,
   "Dubia circa litteram Magistri (Pars II)",
   "Doubts concerning the text of the Master (Part II)",
   99451,99732,[935,936],False),
]

def fm(idsuf, pars, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d44-{idsuf}"', "volume: 4", "book: 4", "distinctio: 44",
         f"pars: {pars}"]
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
    y.append('transcription_status: "auto-chunked 2026-07-18 (rechunk_d44) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d44-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, pars, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, pars, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.44 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d44-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.44 skeletons created.")
