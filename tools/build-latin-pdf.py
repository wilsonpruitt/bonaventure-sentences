#!/usr/bin/env python3
"""Build a Latin-only PDF for each completed Quaracchi tome.

Reads site/src/data/content.json (run `cd site && node scripts/build-content.mjs`
first so it is current) and writes export/pdf/bonaventure-tomus-<N>-latin.pdf.

Per chunk: the Latin body, then the Latin scholion if any. Quaracchi's own
apparatus (the `la` side of each entry) becomes page footnotes; printed page
breaks (`<!-- page N -->`) become small bracketed page numbers. Our English
editorial blockquotes (the "Quaracchi restarts its footnote numbering…" notes)
are dropped. `[?]` flags are kept as printed in the chunk.

    python3 tools/build-latin-pdf.py            # tomes 1-5
    python3 tools/build-latin-pdf.py 3          # one tome
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "site" / "src" / "data" / "content.json"
OUT_DIR = REPO / "export" / "pdf"
COMPLETED_TOMES = [1, 2, 3, 4, 5]

TOME_TITLES = {
    1: ("Commentaria in quatuor libros Sententiarum", "In primum librum Sententiarum"),
    2: ("Commentaria in quatuor libros Sententiarum", "In secundum librum Sententiarum"),
    3: ("Commentaria in quatuor libros Sententiarum", "In tertium librum Sententiarum"),
    4: ("Commentaria in quatuor libros Sententiarum", "In quartum librum Sententiarum"),
    5: ("Opuscula varia theologica", None),
}
ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

# English editorial notes inside the Latin block (blockquotes we wrote, not Quaracchi).
EDITORIAL_QUOTE = re.compile(r"Quaracchi|footnote|footer|numbering", re.I)
PAGE_COMMENT = re.compile(r"^\s*<!--\s*page\s+([0-9]+[a-z]?)\s*-->\s*$", re.I)


def roman(n):
    vals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = ""
    for v, s in vals:
        while n >= v:
            out += s
            n -= v
    return out


def division_title(title):
    m = re.fullmatch(r"Distinction (\d+)", title)
    if m:
        return f"Distinctio {roman(int(m.group(1)))}"
    return title


def drop_editorial_quotes(text):
    """Remove blockquote paragraphs that are our English apparatus notes."""
    blocks = re.split(r"(\n\s*\n)", text)
    kept = []
    for b in blocks:
        if b.lstrip().startswith(">") and EDITORIAL_QUOTE.search(b):
            continue
        kept.append(b)
    return "".join(kept)


_last_page = [None]  # last printed page marked, carried across chunks


def page_markers(text):
    """Turn `<!-- page N -->` comments into inline typst page marks.

    A page break that falls mid-sentence (next block opens lower-case) rejoins
    the two halves of the paragraph, de-hyphenating a split word, and sets the
    mark after the rejoined word. A chunk re-announcing the page the previous
    chunk ended on gets no second mark.
    """
    blocks = re.split(r"\n\s*\n", text)
    out, pending = [], None
    for block in blocks:
        m = PAGE_COMMENT.match(block)
        if m:
            pending = m.group(1)
            continue
        if not block.strip():
            continue
        if pending is not None and pending == _last_page[0]:
            pending = None
        if pending is not None:
            _last_page[0] = pending
            mark = f'`#pg("{pending}")`{{=typst}}'
            pending = None
            prev = out[-1] if out else ""
            plain_prev = prev and not prev.lstrip().startswith(("#", ">", "|", "[^"))
            if plain_prev and re.match(r"[a-zà-ÿ]", block):
                first, _, rest = block.partition(" ")
                if re.search(r"[A-Za-zà-ÿ]-$", prev):
                    out[-1] = f"{prev[:-1]}{first} {mark} {rest}".rstrip()
                else:
                    out[-1] = f"{prev} {first} {mark} {rest}".rstrip()
                continue
            if block.lstrip().startswith(("#", ">", "|", "- ", "* ")) or re.match(r"\s*\d+\.\s", block):
                out.append(mark)
            else:
                block = f"{mark} {block}"
        out.append(block)
    if pending is not None and pending != _last_page[0]:
        _last_page[0] = pending
        out.append(f'`#pg("{pending}")`{{=typst}}')
    return "\n\n".join(out)


def escape_brackets(text):
    """Quaracchi's square brackets (supplements, `[?]`) are literal, never links."""
    parts = re.split(r"(\[\^[^\]]+\])", text)
    return "".join(p if p.startswith("[^") else p.replace("[", "\\[").replace("]", "\\]")
                   for p in parts)


def shift_headings(text):
    """Chunk headings (printed Quaracchi headings) sit below our levels 1-2."""
    def repl(m):
        n = len(m.group(1))
        return "#" * min(6, max(3, n + 1)) + " "
    return re.sub(r"^(#{1,6}) ", repl, text, flags=re.M)


def chunk_markdown(q, key):
    app = {e["id"]: e["la"] for e in q.get("apparatus", []) if e.get("la")}
    used = set()

    def fn(m):
        fid = m.group(1)
        if fid in app:
            used.add(fid)
            return f"[^{key}-{fid}]"
        return ""

    parts = []
    for field, label in (("latin", None), ("latinScholion", "Scholion")):
        t = q.get(field) or ""
        if not t.strip():
            continue
        t = drop_editorial_quotes(t)
        t = re.sub(r"^\s*-{3,}\s*$", "", t, flags=re.M)  # our section rules, not Quaracchi's
        t = re.sub(r"\[\^([^\]]+)\]", fn, t)
        t = escape_brackets(t)
        t = page_markers(t)
        t = shift_headings(t)
        if label:
            t = f"#### {label}\n\n{t}"
        parts.append(t.strip())
    if not parts:
        return ""
    defs = []
    for fid in app:
        if fid in used:
            note = escape_brackets(re.sub(r"\s+", " ", app[fid]).strip())
            defs.append(f"[^{key}-{fid}]: {note}")
    return "\n\n".join(parts) + "\n\n" + "\n".join(defs) + "\n"


def tome_markdown(books, tome):
    md = []
    multi_work = len(books) > 1
    n = 0
    for b in books:
        if multi_work:
            md.append(f"# {b['title']}\n")
        for dv in b["distinctions"]:
            md.append(f"{'##' if multi_work else '#'} {division_title(dv['title'])}\n")
            for q in dv["questions"]:
                n += 1
                body = chunk_markdown(q, f"c{n}")
                if body:
                    md.append(body)
    return "\n\n".join(md), n


TEMPLATE = r"""
#set document(title: "$doctitle$", author: "S. Bonaventura")
#set text(font: ("EB Garamond 12", "EB Garamond 08", "Libertinus Serif"), size: 11pt, lang: "la", hyphenate: true, features: (locl: 0))
#set page(paper: "a4", margin: (x: 2.4cm, top: 2.4cm, bottom: 2.6cm),
  header: context {
    if counter(page).get().first() > 2 {
      set text(size: 8.5pt, fill: luma(90))
      let hs = query(selector(heading.where(level: 1)).before(here()))
      smallcaps[$runhead$]
      h(1fr)
      if hs.len() > 0 { smallcaps(hs.last().body) }
    }
  },
  numbering: "1")
#set par(justify: true, leading: 0.62em, spacing: 0.9em)
#show footnote.entry: set text(size: 8.5pt)
#set footnote.entry(separator: line(length: 25%, stroke: 0.4pt), gap: 0.35em)
#let pg(n) = text(size: 7.5pt, fill: luma(110), baseline: -0.15em)[\[#n\]]
#show quote.where(block: true): set pad(x: 1.5em)
#show heading: set text(weight: "regular")
#show heading.where(level: 1): it => { pagebreak(weak: true); v(2.5em); align(center, text(size: 17pt, smallcaps(it.body))); v(1.4em) }
#show heading.where(level: 2): it => { v(1.4em); align(center, text(size: 13.5pt, smallcaps(it.body))); v(0.8em) }
#show heading.where(level: 3): it => { v(0.9em); align(center, text(size: 12pt, it.body)); v(0.4em) }
#show heading.where(level: 4): it => { v(0.6em); align(center, text(size: 11pt, it.body)); v(0.3em) }
#show heading.where(level: 5): it => { v(0.4em); align(center, text(size: 10.5pt, it.body)); v(0.2em) }
#show heading.where(level: 6): it => { v(0.3em); align(center, text(size: 10.5pt, it.body)); v(0.2em) }
#set heading(outlined: false)
#show heading.where(level: 1): set heading(outlined: true)
$if(outline2)$#show heading.where(level: 2): set heading(outlined: true)$endif$

#page(numbering: none, header: none)[
  #v(5cm)
  #align(center)[
    #text(size: 13pt, smallcaps[Doctoris Seraphici])\
    #v(0.3em)
    #text(size: 26pt)[S. Bonaventurae]\
    #v(0.3em)
    #text(size: 14pt, smallcaps[Opera Omnia])
    #v(2.2em)
    #text(size: 18pt)[Tomus $tome$]
    #v(1em)
    #text(size: 14pt, style: "italic")[$subtitle$]
    $if(subtitle2)$#v(0.4em)
    #text(size: 12.5pt)[$subtitle2$]$endif$
    #v(1fr)
    #text(size: 9.5pt)[Textus Latinus editionis Quaracchiensis (Ad Claras Aquas, 1882–1902),\ cum apparatu editorum. Transcriptio: bonaventure.wrootpress.com]
    #v(0.6em)
    #text(size: 8.5pt, fill: luma(90))[The Quaracchi Latin text and apparatus are in the public domain. Numbers in brackets mark the printed pages\ of the Quaracchi tome; footnotes are the editors' apparatus, renumbered continuously. Built $date$.]
  ]
  #v(2cm)
]
#page(numbering: none, header: none)[
  #align(center, text(size: 17pt, smallcaps[Index]))
  #v(1.2em)
  #outline(title: none, depth: 2, indent: 1.2em)
]
#counter(page).update(1)

$body$
"""


def first_printed_page(book):
    for dv in book["distinctions"]:
        for q in dv["questions"]:
            m = re.search(r"<!--\s*page\s+(\d+)", q.get("latin") or "")
            if m:
                return int(m.group(1))
    return 10**6


def build(tome, data):
    books = [b for b in data if b.get("tome", b["id"]) == tome]
    books.sort(key=first_printed_page)
    md, n = tome_markdown(books, tome)
    work = OUT_DIR / f"tomus-{tome}"
    work.mkdir(parents=True, exist_ok=True)
    (work / "latin.md").write_text(md)
    sub, sub2 = TOME_TITLES[tome]
    from datetime import date
    tpl = work / "template.typ"
    tpl.write_text(TEMPLATE)
    typ = work / "latin.typ"
    args = [
        "pandoc", str(work / "latin.md"), "-f", "markdown-implicit_figures-auto_identifiers",
        "-t", "typst", "--template", str(tpl), "-o", str(typ),
        "-V", f"tome={ROMAN[tome]}", "-V", f"subtitle={sub}",
        "-V", f"doctitle=S. Bonaventurae Opera Omnia, Tomus {ROMAN[tome]} (Latin)",
        "-V", f"runhead=S. Bonaventurae Opera, Tom. {ROMAN[tome]}",
        "-V", f"date={date.today().isoformat()}",
    ]
    if sub2:
        args += ["-V", f"subtitle2={sub2}"]
    if tome == 5:
        args += ["-V", "outline2=true"]
    subprocess.run(args, check=True)
    pdf = OUT_DIR / f"bonaventure-tomus-{tome}-latin.pdf"
    subprocess.run(["typst", "compile", str(typ), str(pdf)], check=True)
    print(f"Tomus {ROMAN[tome]}: {n} chunks -> {pdf}")


def main():
    tomes = [int(a) for a in sys.argv[1:]] or COMPLETED_TOMES
    data = json.loads(CONTENT.read_text())
    for t in tomes:
        build(t, data)


if __name__ == "__main__":
    main()
