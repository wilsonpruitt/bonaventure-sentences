#!/usr/bin/env python3.11
"""Create Vol IV d.50 skeletons fresh — the LAST distinction of Book IV. TWO PARTES, 17 chunks.
Structure count-verified 2026-07-18.

⚠ WHY THIS SCRIPT EXISTS — the 2026-06-16 auto-chunk **never detected d.50 at all** (the
  bootstrap note records d.4, d.23 and d.50 as "merged into neighbours" via garbled DISTINCTIO
  headers). d.50's content was instead filed under d.49 ids as the `-dup3`/`-dup4` families
  (e.g. `d49-p2-a1-q1-dup4` = L111305–111641, which is d.50 P.II a1-q1), and
  `d49-p2-a4-q2` overran the d.50 header. `tools/rechunk_d49.py` deletes all `d49-*` files and
  rebuilds d.49 within its true bounds; this script reclaims d.50's ranges under correct ids.
  **Run rechunk_d49.py and rechunk_d50.py together** — d.50's content only exists in the corpus
  after both have run.

COUNT-CHECK (2 partes × 2 articles × 3 questions, plus one dubium):
  - P.I TRACTATIO L110272: "duo principaliter quaeruntur" → 2 articles.
    Art I (L110284, De subversione voluntatis damnatorum) q1 L110288, q2 L110495, q3 L110671.
    Art II (L110810, De excaecatione damnatorum) q1 L110826, q2 L110926, q3 L111162.
  - P.II TRACTATIO L111291: "duo quaeruntur principaliter" → 2 articles.
    Art I (L111302, De cognitione animae separatae) q1 L111305, q2 L111642, q3 L111798.
    Art II (L111914, De verme qui est in damnatis) q1 L111929, q2 L112039, q3 L112238.
  - Tail-check: the book's last question opens "Tertio **et ultimo** quaeritur" (L112241) — a
    clean terminal marker — and is followed by a single `DUBIUM CIRCA LITTERAM MAGISTRI.`
    (L112272, SINGULAR — one dubium, not a dubia block).

GARBLED HEADERS: `QUAESTIO 111.` (L111798), `QUAESTiO II.` (L112039, lowercase i — the d.46
  a2-q4 shape), `SCHOLIOK` (L110916, L111582, L112028).

SCHOLIA (one per article, in that article's q1): p1-a1-q1 L110470 (`SCHOLION.`),
  p1-a2-q1 L110916, p2-a1-q1 L111582, p2-a2-q1 L112028.

BOUNDARY — d.50 = L109979–L112356.
  ⚠ OPENING: real header `DISTINCTIO L.` at **L109979**; the `DISTINGTIO L. P. I. 1033` at
    L109974 is the p.1033 running-head bleed sitting inside d.49's last question. d.49 ends
    L109978 — verified against rechunk_d49.py, no double-claim.
  ⚠ CLOSING: the body ends at **L112356**; `INDEX QUAESTIONUM` begins L112357. The index is
    apparatus of the printed volume, NOT Bonaventure's text — do not chunk it.

LITTERA: Lombard's text splits by pars in the print — `Pars I.` L109982 (Cap. I–II),
  `Pars IL` L110086 (Cap. III onward) — so it is chunked as p1-littera / p2-littera, per the
  corpus convention of a littera per pars (cf. d.1, d.44, d.49).

PAGE TOPS from running heads (odd only; even tops INTERPOLATED as midpoints → page assignments
  are ESTIMATES, writers correct from the bands). Several heads are OCR-mangled and are
  corrected by sequence below. Printed span 1033–1054.

⚠ BANDS: gutter alternates by page parity (`manual-review/vol4-column-gutter-parity.md`).
  MEASURE each of pp.1033–1054 and regenerate before dispatching. Offset pdf = printed + 20.

★ d.50 closing this distinction TRIGGERS THE d.41–d.50 DECADE GATE — the last of Book IV, and a
  hard blocker. See the resume note.

Run: python3.11 tools/rechunk_d50.py
"""
import os, glob, bisect

RAW = "raw/bonaventure_vol4_raw.txt"
VOL = "vol4"
OFF = 20
D = 50

with open(RAW, encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

ODD_TOPS = {1033:109974,
            1035:110229,  # head OCR'd "103i"
            1037:110453, 1039:110647, 1041:110867, 1043:111157,
            1045:111344,  # head OCR'd "1043", a duplicate; corrected by sequence
            1047:111568,
            1049:111794,  # head lost its page number
            1051:111986,  # head OCR'd "lOSl"
            1053:112224}  # head OCR'd "1033", a duplicate; corrected by sequence

def build_tops(odd):
    tops = dict(odd)
    ks = sorted(odd)
    for a, b in zip(ks, ks[1:]):
        tops[a + 1] = (odd[a] + odd[b]) // 2
    tops[max(ks) + 1] = (odd[max(ks)] + 112357) // 2
    return tops

TOPS = build_tops(ODD_TOPS)
PAGES = sorted(TOPS)
STARTS = [TOPS[p] for p in PAGES]

def pages_for(l0, l1):
    out = []
    for i, p in enumerate(PAGES):
        s = STARTS[i]
        e = STARTS[i + 1] - 1 if i + 1 < len(STARTS) else 10**9
        if s <= l1 and e >= l0:
            out.append(p)
    return out or [PAGES[max(0, bisect.bisect_right(STARTS, l0) - 1)]]

# (id-suffix, type, pars, art, q, title_la, title_en, l0, l1, has_scholion)
CH = [
 ("p1-littera","littera",1,None,None,
   "Littera Magistri (Lombard), Distinctio L, Pars I — De statu damnatorum post iudicium",
   "The text of the Master (Lombard), Distinction L, Part I — On the state of the damned after the judgement",
   109979,110085,False),
 ("p2-littera","littera",2,None,None,
   "Littera Magistri (Lombard), Distinctio L, Pars II — De statu animarum ante iudicium",
   "The text of the Master (Lombard), Distinction L, Part II — On the state of souls before the judgement",
   110086,110248,False),
 ("p1-divisio","divisio",1,None,None,
   "Divisio textus et tractatio quaestionum (Pars I)",
   "Division of the text and treatment of the questions (Part I)",
   110249,110283,False),
 ("p1-a1-q1","quaestio",1,1,1,
   "Utrum damnati velint, se peccasse",
   "Whether the damned will that they had sinned",
   110284,110494,True),
 ("p1-a1-q2","quaestio",1,1,2,
   "Utrum voluntate deliberativa damnati malint non esse quam sic esse",
   "Whether by deliberative will the damned would rather not be than be thus",
   110495,110670,False),
 ("p1-a1-q3","quaestio",1,1,3,
   "Utrum damnati mallent, omnes esse damnatos, quam quosdam damnatos, quosdam beatos",
   "Whether the damned would rather that all were damned than that some be damned and some blessed",
   110671,110809,False),
 ("p1-a2-q1","quaestio",1,2,1,
   "Utrum in inferno sint tenebrae corporales",
   "Whether in hell there are bodily darknesses",
   110810,110925,True),
 ("p1-a2-q2","quaestio",1,2,2,
   "Utrum in damnatis erunt tenebrae spirituales quoad actum cognoscendi",
   "Whether in the damned there will be spiritual darknesses as to the act of knowing",
   110926,111161,False),
 ("p1-a2-q3","quaestio",1,2,3,
   "Utrum in damnatis sint tenebrae spirituales quoad actum memorandi",
   "Whether in the damned there are spiritual darknesses as to the act of remembering",
   111162,111261,False),
 ("p2-divisio","divisio",2,None,None,
   "Divisio textus et tractatio quaestionum (Pars II)",
   "Division of the text and treatment of the questions (Part II)",
   111262,111301,False),
 ("p2-a1-q1","quaestio",2,1,1,
   "Utrum anima separata habeat usum potentiae sensitivae",
   "Whether the separated soul has the use of the sensitive power",
   111302,111641,True),
 ("p2-a1-q2","quaestio",2,1,2,
   "Utrum anima separata cognoscat ea quae circa nos geruntur",
   "Whether the separated soul knows the things that are done about us",
   111642,111797,False),
 ("p2-a1-q3","quaestio",2,1,3,
   "Utrum Beati et damnati mutuo se cognoscant",
   "Whether the blessed and the damned know one another",
   111798,111913,False),
 ("p2-a2-q1","quaestio",2,2,1,
   "Utrum damnati habeant vermem materialem",
   "Whether the damned have a material worm",
   111914,112038,True),
 ("p2-a2-q2","quaestio",2,2,2,
   "Utrum et qua ratione in damnatis sit vermis spiritualis",
   "Whether, and for what reason, there is a spiritual worm in the damned",
   112039,112237,False),
 # The last question of Book IV — opener "Tertio et ultimo quaeritur" (L112241).
 ("p2-a2-q3","quaestio",2,2,3,
   "Utrum vermis ille sit invariabilis",
   "Whether that worm is unchangeable",
   112238,112271,False),
 ("p2-dubium","dubia",2,None,None,
   "Dubium circa litteram Magistri",
   "A doubt concerning the text of the Master",
   112272,112356,False),
]

def fm(idsuf, typ, pars, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {pp[0]}–{pp[-1]}"
    y = [f'id: "bon-sent-IV-d{D}-{idsuf}"', "volume: 4", "book: 4", f"distinctio: {D}"]
    if pars is not None: y.append(f"pars: {pars}")
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
    y.append(f'transcription_status: "auto-chunked 2026-07-18 (rechunk_d{D}) — SKELETON, needs Tier 2"')
    y.append("format_version: 1")
    return "---\n" + "\n".join(y) + "\n---\n"

for old in glob.glob(os.path.join(VOL, f"bon-sent-IV-d{D}-*.md")):
    os.remove(old)
    print(f"deleted {os.path.basename(old)}")

prev_end = None
for idsuf, typ, pars, art, q, tla, ten, l0, l1, schol in CH:
    assert prev_end is None or l0 == prev_end + 1, f"gap/overlap at {idsuf}: {prev_end} -> {l0}"
    prev_end = l1
    pp = pages_for(l0, l1)
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, pars, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.{D} {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d{D}-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {os.path.basename(path)}  (L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.{D} skeletons created, contiguous L{CH[0][7]}-{CH[-1][8]}.")
