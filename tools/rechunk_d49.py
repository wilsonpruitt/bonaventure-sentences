#!/usr/bin/env python3.11
"""Create Vol IV d.49 skeletons fresh — TWO PARTES, and the ONLY distinction in Books I–IV with
a SECTIO level. Structure count-verified 2026-07-18. 24 chunks.

⚠ ID CONVENTION — see CLAUDE.md §5a (frozen 2026-07-18). Pars II's sections are the Quaracchi
  EDITORS' division, not Bonaventure's: their footnote on the Sectio I page says they added it
  "ad confusionem in citando vitandam", and they then cite by it (`a. 2. sect. 2. n. 49`).
  Sectio is therefore a real slug level between pars and articulus —
  `bon-sent-IV-d49-p2-s{1,2}-a{N}-q{N}` — plus a `sectio: N` frontmatter field. It is REQUIRED,
  not cosmetic: Pars II contains TWO `Articulus I`, so a flat id collides.

⚠ WHY THIS SCRIPT EXISTS — the 2026-06-16 auto-chunk was badly wrong here:
  1. It had no sectio concept, so it filed Sectio II's articles as `-dup2` of Sectio I's.
  2. Its `-dup3`/`-dup4` families carry line ranges PAST L109979 — they are **d.50's content
     filed under d.49 ids**. `tools/rechunk_d50.py` reclaims those ranges; this script deletes
     every `d49-*` file, so RUN d50 AFTER d49 (or just run both; they touch disjoint ids).
  3. `d49-p2-a4-q2` ran 109887–110248, overrunning the d.50 header at L109979.
  4. `d49-p1-littera` ran 106123–106349, spanning BOTH partes of Lombard's text — his
     `Pars II.` is at L106309. Split here into p1-littera / p2-littera, per the corpus
     convention of a littera per pars (cf. d.1, d.44). The Pars II commentary's
     "TEXTUM MAGISTRI VIDE SUPRA PAG. 999" confirms Lombard's Pars II text is printed up on
     p.999 with the rest of the littera, not beside its own commentary.

COUNT-CHECK (every leg agreeing):
  - P.I TRACTATIO L106424: "de hoc sex quaeruntur" → ARTICULUS UNICUS with 6 questions ✓
  - P.II TRACTATIO L107655: "duo principaliter quaeruntur" → 2 SECTIONES ✓
  - Sectio I L107664: "Circa primum quaeruntur principaliter tria" → 3 articles;
    Art I 2 q, Art II "circa hoc duo" 2 q, Art III "hoc duo quaeruntur" 2 q ✓
  - Sectio II L108777: "quatuor principaliter quaerunlur" (the four dotes) → 4 articles;
    Art I "Circa primum quaeruntur duo" 2 q, Art II 2 q, Art III 2 q,
    Art IV "de qua duo quaeruntur" 2 q ✓
  - ⚠ **Sectio II Art IV q2 was nearly lost**: its header is OCR-garbled `QU.\\ESTIO II.`
    (L109887) and is invisible to a `QUAESTIO` grep. It was found only because Art IV's opener
    promises two questions ("Secundo quaeritur de inclinatione corporis gloriosi per
    agilitatem"). Same failure class as d.47/d.48 a2-q3. The auto-chunker's START for it was
    right; only its line_end was wrong.

DIVISIO / OPENER FOLDING (follows the established "short opener folds into that unit's q1" rule,
  CLAUDE.md Vol II Override step 5):
  - `p1-divisio` = COMMENTARIUS (L106350) + DIVISIO TEXTUS (L106363) + TRACTATIO (L106424).
    The `ARTIGULUS UNIGUS` opener (L106437) folds into p1-a1-q1.
  - `p2-divisio` = COMMENTARIUS (L107630) + DIVISIO TEXTUS (L107643) + TRACTATIO (L107655)
    + the **Sectio I header and prologue** (L107664–107690), which are contiguous with it.
  - **Sectio II's header + prologue (L108777–108790) fold into `p2-s2-a1-q1`.** They sit ~1,100
    lines downstream of p2-divisio, so they cannot live in it without a non-contiguous range.
    This AMENDS CLAUDE.md §5a as first written (which assumed both prologues could sit in
    p2-divisio); the amendment is recorded there. Still NO `-sN-divisio` chunks.

SCHOLIA: p1-a1-q1 L106577 (`SCHOLIOK`); s1-a1-q1 L107845 (`SCHOLIOl^`); s1-a3-q1 L108560;
  s2-a1-q1 L108987; s2-a3-q1 L109644 (`SCHOLIOK`).

BOUNDARY — d.49 = L106123–L109978. Real headers: `DISTINCTIO XLIX.` L106123, `DISTINCTIO L.`
  L109979. The `DISTINCTIO XLIX. P. I. 997` at L106068 and `DISTINGTIO L. P. I. 1033` at
  L109974 are running-head bleeds. d.48's dubia end at L106122 — no double-claim.

⚠ DUBIA: **NO dubia header is greppable anywhere in d.49's range**, and none is assumed here.
  That is exactly the d.45 failure shape (9 dubia printed, only 3 greppable, six cased `DuB.`).
  **VERIFY OFF THE BANDS before accepting that d.49 has no dubia** — check the foot of p.1032
  in particular. If dubia exist, add a `d49-p2-dubia` chunk and shorten s2-a4-q2.

PAGE TOPS from running heads (odd only; even tops INTERPOLATED as midpoints → page assignments
  are ESTIMATES, writers correct from the bands). Note p.1005's head is OCR'd "1003", a
  duplicate of p.1003's — corrected below by sequence. Printed span 997–1032.

⚠ BANDS: gutter alternates by page parity (`manual-review/vol4-column-gutter-parity.md`).
  MEASURE each of pp.997–1032 and regenerate before dispatching. Offset pdf = printed + 20.

Run: python3.11 tools/rechunk_d49.py
"""
import os, glob, bisect

RAW = "raw/bonaventure_vol4_raw.txt"
VOL = "vol4"
OFF = 20
D = 49

with open(RAW, encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

ODD_TOPS = {997:106068, 999:106272, 1001:106529, 1003:106737,
            1005:106953,  # running head OCR'd "1003"; corrected by sequence
            1007:107160, 1009:107348, 1011:107602, 1013:107792, 1015:108060,
            1017:108292, 1019:108501, 1021:108754, 1023:108964,
            1025:109151,  # head OCR'd "102i5"
            1027:109371, 1029:109601, 1031:109783, 1033:109974}

def build_tops(odd):
    tops = dict(odd)
    ks = sorted(odd)
    for a, b in zip(ks, ks[1:]):
        tops[a + 1] = (odd[a] + odd[b]) // 2
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

# (id-suffix, type, pars, sectio, art, q, title_la, title_en, l0, l1, has_scholion)
CH = [
 ("p1-littera","littera",1,None,None,None,
   "Littera Magistri (Lombard), Distinctio XLIX, Pars I — De beatitudine Sanctorum",
   "The text of the Master (Lombard), Distinction XLIX, Part I — On the beatitude of the Saints",
   106123,106308,False),
 # Lombard's Pars II text is printed here, on p.999, not beside its own commentary.
 ("p2-littera","littera",2,None,None,None,
   "Littera Magistri (Lombard), Distinctio XLIX, Pars II — De gloria corporis sive de stola secunda",
   "The text of the Master (Lombard), Distinction XLIX, Part II — On the glory of the body, or the second robe",
   106309,106349,False),
 ("p1-divisio","divisio",1,None,None,None,
   "Divisio textus et tractatio quaestionum (Pars I)",
   "Division of the text and treatment of the questions (Part I)",
   106350,106436,False),
 ("p1-a1-q1","quaestio",1,None,1,1,
   "Quid sit beatitudo",
   "What beatitude is",
   106437,106712,True),
 ("p1-a1-q2","quaestio",1,None,1,2,
   "Qualiter beatitudo sit appetibilis",
   "In what way beatitude is desirable",
   106713,106833,False),
 ("p1-a1-q3","quaestio",1,None,1,3,
   "In quo subiecto sit beatitudo",
   "In what subject beatitude resides",
   106834,107077,False),
 ("p1-a1-q4","quaestio",1,None,1,4,
   "Secundum quid beatitudo insit in anima",
   "According to what beatitude is present in the soul",
   107078,107274,False),
 ("p1-a1-q5","quaestio",1,None,1,5,
   "Quibus potentiis insit actus sive operatio gloriae",
   "In which powers the act or operation of glory resides",
   107275,107472,False),
 ("p1-a1-q6","quaestio",1,None,1,6,
   "De differenti participatione beatitudinis, utrum scilicet omnes habeant aequalem beatitudinem",
   "On the differing participation in beatitude, namely whether all have equal beatitude",
   107473,107629,False),
 # Includes the SECTIO I header + prologue (L107664–107690), contiguous with the pars divisio.
 ("p2-divisio","divisio",2,None,None,None,
   "Divisio textus et tractatio quaestionum (Pars II), cum principio Sectionis I",
   "Division of the text and treatment of the questions (Part II), with the opening of Section I",
   107630,107690,False),
 # ---- SECTIO I — De gloria corporis in generali ----
 ("p2-s1-a1-q1","quaestio",2,1,1,1,
   "Utrum gloria corporis sit de substantia beatitudinis",
   "Whether the glory of the body belongs to the substance of beatitude",
   107691,107896,True),
 ("p2-s1-a1-q2","quaestio",2,1,1,2,
   "Utrum gloria corporis sit a gloria animae originaliter",
   "Whether the glory of the body derives originally from the glory of the soul",
   107897,108069,False),
 ("p2-s1-a2-q1","quaestio",2,1,2,1,
   "De numero et sufficientia dotium",
   "On the number and sufficiency of the dowries",
   108070,108295,False),
 ("p2-s1-a2-q2","quaestio",2,1,2,2,
   "Utrum dotes corporis aequaliter sint in omnibus",
   "Whether the dowries of the body are equally in all",
   108296,108358,False),
 ("p2-s1-a3-q1","quaestio",2,1,3,1,
   "Utrum in patria omnes sensus habeant suos actus",
   "Whether in the fatherland all the senses have their acts",
   108359,108610,True),
 ("p2-s1-a3-q2","quaestio",2,1,3,2,
   "Utrum sensus illi, qui sunt in suo actu, cognoscant per receptionem speciei",
   "Whether those senses which are in their act know through the reception of a species",
   108611,108776,False),
 # ---- SECTIO II — De gloria corporis in speciali (the four dotes) ----
 # Folds the SECTIO II header + prologue (L108777–108790) and the Articulus I opener.
 ("p2-s2-a1-q1","quaestio",2,2,1,1,
   "Utrum corpus gloriosum sit passibile ab intrinseco",
   "Whether the glorified body is passible from within",
   108777,109014,True),
 ("p2-s2-a1-q2","quaestio",2,2,1,2,
   "Utrum corpus gloriosum sit passibile passione veniente ab extrinseco",
   "Whether the glorified body is passible by a passion coming from without",
   109015,109110,False),
 ("p2-s2-a2-q1","quaestio",2,2,2,1,
   "Utrum corpora gloriosa sint pervia, an colorata, an luminosa",
   "Whether glorified bodies are transparent, or coloured, or luminous",
   109111,109282,False),
 ("p2-s2-a2-q2","quaestio",2,2,2,2,
   "Utrum corpora gloriosa possint claritatem suam secundum imperium animae oculis nostris occultare",
   "Whether glorified bodies can hide their brightness from our eyes at the command of the soul",
   109283,109391,False),
 ("p2-s2-a3-q1","quaestio",2,2,3,1,
   "Utrum corpus gloriosum possit penetrare omne aliud corpus",
   "Whether the glorified body can penetrate every other body",
   109392,109697,True),
 ("p2-s2-a3-q2","quaestio",2,2,3,2,
   "Utrum corpus glorificatum sit palpabile a tactu non glorificato",
   "Whether the glorified body is palpable to a touch that is not glorified",
   109698,109754,False),
 ("p2-s2-a4-q1","quaestio",2,2,4,1,
   "Utrum agilitas sit in omnibus corporibus gloriosis",
   "Whether agility is in all glorified bodies",
   109755,109886,False),
 # ⚠ RECOVERED — header `QU.\ESTIO II.` L109887, promised by Art IV's opener.
 ("p2-s2-a4-q2","quaestio",2,2,4,2,
   "Utrum agilitas inclinet corpus gloriosum ad omnem differentiam positionis, an ad aliquem locum determinatum",
   "Whether agility inclines the glorified body to every difference of position, or to some determinate place",
   109887,109978,False),
]

def fm(idsuf, typ, pars, sect, art, q, tla, ten, pp, l0, l1, schol):
    pdf = [p + OFF for p in pp]
    src = f"S. Bonaventurae, Opera Omnia, Tomus IV (Quaracchi, 1889), pp. {pp[0]}–{pp[-1]}"
    y = [f'id: "bon-sent-IV-d{D}-{idsuf}"', "volume: 4", "book: 4", f"distinctio: {D}"]
    if pars is not None: y.append(f"pars: {pars}")
    if sect is not None: y.append(f"sectio: {sect}")
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
print(f"deleted {len(glob.glob(os.path.join(VOL, f'bon-sent-IV-d{D}-*.md')))} residual (all d.{D} files removed)")

prev_end = None
for idsuf, typ, pars, sect, art, q, tla, ten, l0, l1, schol in CH:
    assert prev_end is None or l0 == prev_end + 1, f"gap/overlap at {idsuf}: {prev_end} -> {l0}"
    prev_end = l1
    pp = pages_for(l0, l1)
    body = "".join(lines[l0-1:l1])
    out = fm(idsuf, typ, pars, sect, art, q, tla, ten, pp, l0, l1, schol)
    out += f"\n# d.{D} {idsuf}\n## *{tla}*\n\n---\n\n## Latin\n<!-- raw OCR L{l0}–L{l1}; re-set from bands -->\n\n```\n{body}\n```\n\n---\n\n## English\n\n(skeleton)\n\n---\n\n## Apparatus\n\n(skeleton)\n"
    path = os.path.join(VOL, f"bon-sent-IV-d{D}-{idsuf}.md")
    with open(path, "w", encoding="utf-8") as fo:
        fo.write(out)
    print(f"wrote {os.path.basename(path)}  (L{l0}-{l1}, pp.{pp[0]}-{pp[-1]}, scholion={schol})")

print(f"\n{len(CH)} d.{D} skeletons created, contiguous L{CH[0][8]}-{CH[-1][9]}.")
