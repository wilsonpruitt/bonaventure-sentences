#!/usr/bin/env python3.11
"""Create Vol IV d.33 skeletons fresh (SINGLE-PARS, De pluralitate uxorum / virginitate / repudio).
THREE articles x 3 questions:
 Art I De pluralitate uxorum (q1 concubina contra legem naturae / q2 plures uxores / q3 dispensatio Dei),
 Art II De virginitate (q1 virginitas virtus / q2 praeferatur continentiae / q3 praemium aureola),
 Art III De repudio (q1 licitum repudiare / q2 debuerit permitti / q3 reconciliari post repudium).
Scholia in each article's q1: a1-q1 (SCHOLION L80561), a2-q1 (SCHOLIOK L81133), a3-q1 (SCHOLIOK L81640, "De his tribus quaestionibus").
Recreate all 12 with raw OCR sliced into ## Latin + line_start/line_end so all 3 audits run. Deletes existing d33-* first.
Run: python3.11 tools/rechunk_d33.py
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
   "Littera Magistri (Lombard), Distinctio XXXIII",
   "The text of the Master (Lombard), Distinction XXXIII",
   80052,80295,[745,746,747],False),
 ("divisio","divisio",None,None,
   "Divisio textus et tractatio quaestionum",
   "Division of the text and treatment of the questions",
   80296,80365,[747],False),
 ("a1-q1","quaestio",1,1,
   "Utrum contra legem naturae sit habere concubinam",
   "Whether it is against the law of nature to have a concubine",
   80366,80599,[747,748,749],True),
 ("a1-q2","quaestio",1,2,
   "Utrum habere plures uxores sit contra legem naturae",
   "Whether to have several wives is against the law of nature",
   80600,80734,[749,750,751],False),
 ("a1-q3","quaestio",1,3,
   "Utrum Deus debuerit dispensare de concubina habenda",
   "Whether God ought to have granted dispensation concerning the having of a concubine",
   80735,81028,[751,752,753],False),
 ("a2-q1","quaestio",2,1,
   "Utrum virginitas sit virtus",
   "Whether virginity is a virtue",
   81029,81161,[753,754],True),
 ("a2-q2","quaestio",2,2,
   "Utrum virginitas praeferatur continentiae coniugali",
   "Whether virginity is preferred to conjugal continence",
   81162,81275,[754,755],False),
 ("a2-q3","quaestio",2,3,
   "Utrum virginitatis praemium sit aureola",
   "Whether the reward of virginity is the aureole",
   81276,81546,[755,756,757,758],False),
 ("a3-q1","quaestio",3,1,
   "Utrum fuerit licitum uxorem repudiare",
   "Whether it was licit to repudiate a wife",
   81547,81688,[758,759],True),
 ("a3-q2","quaestio",3,2,
   "Utrum repudiare uxorem debuerit permitti",
   "Whether the repudiation of a wife ought to have been permitted",
   81689,81776,[759,760],False),
 ("a3-q3","quaestio",3,3,
   "Utrum uxor post repudium debeat viro reconciliari",
   "Whether a wife after repudiation ought to be reconciled to her husband",
   81777,81878,[760,761],False),
 ("dubia","dubia",None,None,
   "Dubia circa litteram Magistri",
   "Doubts concerning the text of the Master",
   81879,82110,[761,762,763,764],False),
]

def fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    lo, hi = pp[0], pp[-1]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {lo}–{hi}"
    y = [f'id: "bon-sent-IV-d33-{idsuf}"', "volume: 4", "book: 4", "distinctio: 33"]
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
    y.append('transcription_status: "auto-chunked 2026-07-12 (rechunk_d33) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, "bon-sent-IV-d33-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

for idsuf, typ, art, q, tla, ten, l0, l1, pp, schol in CH:
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.33 {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d33-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {path}  (raw L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.33 skeletons created.")
