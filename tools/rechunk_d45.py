#!/usr/bin/env python3.11
"""Create Vol IV d.45 skeletons fresh (SINGLE-PARS, De receptaculis animarum post mortem et de
suffragiis). Structure count-verified:
  - TRACTATIO (L99935): "principaliter tria quaeruntur" -> 3 articles; "Circa primum quaeruntur
    tria" -> 3 questions in Art I. Art II + Art III openers each list 3 questions.
  - Ordinal openers cross-checked (L99941, 100212, 100304, 100481, 100776, 101027, 101105).
  - QUAESTIO headers all located; titles taken from the line AFTER each header.
GARBLED HEADERS: "ARTIGULUS I." (L99948), "QUAESTfO I." (L99952), "ARTICULUS 111." (L100772),
"SOHOLIOK" (L100414), "SCHOLIOK" (L100994).
SCHOLIA (one per article, in that article's q1, covering all 3 of its questions):
  a1-q1 L100042, a2-q1 L100414, a3-q1 L100994.
BOUNDARY — BOTH ENDS WERE INITIALLY WRONG; the corrected range is d.45 = L99598–L101427.
  ⚠ OPENING: the real `DISTINCTIO XLV.` header is at raw **L99598**, OCR-garbled as `DISTmCTIO XLV.`
  (the IN->m ligature garble already documented for Vol II's `DISTmCTIO 11.`). The L99733
  occurrence is the printed-p.937 RUNNING-HEAD BLEED. A first pass started the littera at L99733
  and thereby DROPPED Lombard's Cap. I + the opening of Cap. II (printed p.936, raw L99598-99732)
  out of the corpus entirely — `d44-p2-dubia` nominally covered those lines (line_end 99732) but
  its body never rendered them. Fixed here: littera starts at L99598, and d44-p2-dubia's line_end
  was corrected 99732 -> 99597. **Always grep distinction headers case-insensitively and
  ligature-tolerantly: `d[i1l]st[inml1]{1,2}[cg]t[il1]o`.**
  ⚠ CLOSING: the real `DISTINCTIO XLVI.` header is raw L101428 (followed by `Gap. I.`). BOTH
  L101372 (`DISTINGTIO XLVI. 983`) and L101572 (`DISTINCTIO XLVl. 955`) are running-head bleeds;
  next-session-resume had L101572 as the real header. It is not.
SEAM: the `DIST. XLV. DUBIA.` running head bleeds in at L101189, ~18 lines BEFORE the real
  `DUBIA CIRCA LITTERAM MAGISTRI.` header at L101207. a3-q3's tail continues through L101206.
DUBIA: DUB. I / II / III greppable (L101210, 101247, 101228 — printed out of reading order, the
  usual two-column artifact). COUNT THEM OFF THE 450dpi BANDS — more may be cascade-hidden.
Page tops from running heads: 937=L99733, 939=L99925, 940=L100007, 941=L100107, 942=L100194,
943=L100282, 944=L100370, 945=L100471, 946=L100561, 947=L100709, 948=L100817, 949=L100983,
951=L101189, 952=L101265, 953=L101372. (938 and 950 running heads are OCR-dropped.)
Offset pdf = printed + 20.
Run: python3.11 tools/rechunk_d45.py
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
   "Littera Magistri (Lombard), Distinctio XLV — De receptaculis animarum et de suffragiis pro defunctis",
   "The text of the Master (Lombard), Distinction XLV — On the abodes of souls and on suffrages for the dead",
   99598,99877,[936,937,938],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   99878,99947,[938,939],False),
 ("a1-q1","quaestio",1,1,
   "De receptaculis animarum ante adventum Christi",
   "On the abodes of souls before the coming of Christ",
   99948,100065,[939,940],True),
 ("a1-q2","quaestio",1,2,
   "Utrum animae post adventum Christi habeant receptacula sive loca determinata",
   "Whether after the coming of Christ souls have determinate abodes or places",
   100066,100205,[941,942],False),
 ("a1-q3","quaestio",1,3,
   "Utrum animae aliquando exeant a suis receptaculis",
   "Whether souls ever go forth from their abodes",
   100206,100293,[942,943],False),
 ("a2-q1","quaestio",2,1,
   "Utrum suffragia prosint defunctis mediocriter bonis",
   "Whether suffrages profit the dead who are moderately good",
   100294,100475,[943,944,945],True),
 ("a2-q2","quaestio",2,2,
   "Utrum defunctis prosint suffragia facta per malos",
   "Whether suffrages made by the wicked profit the dead",
   100476,100564,[945,946],False),
 ("a2-q3","quaestio",2,3,
   "Utrum suffragia magis prosint ei qui magis meruit, an ei pro quo specialiter fiunt",
   "Whether suffrages profit more the one who merited more, or the one for whom they are specially made",
   100565,100771,[946,947],False),
 ("a3-q1","quaestio",3,1,
   "Utrum Sancti orent pro nobis",
   "Whether the Saints pray for us",
   100772,101022,[947,948,949],True),
 ("a3-q2","quaestio",3,2,
   "Utrum Sancti nobis aliqua impetrent suis orationibus",
   "Whether the Saints obtain anything for us by their prayers",
   101023,101100,[949,950],False),
 ("a3-q3","quaestio",3,3,
   "Utrum utile sit nobis rogare Sanctos",
   "Whether it is useful for us to entreat the Saints",
   101101,101206,[950,951],False),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   101207,101427,[951,952,953],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d45-{idsuf}"', "volume: 4", "book: 4", "distinctio: 45"]
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
    y.append('transcription_status: "auto-chunked 2026-07-18 (rechunk_d45) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d45-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.45 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d45-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.45 skeletons created.")
