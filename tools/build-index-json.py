#!/usr/bin/env python3.11
"""
build-index-json.py — views over the citation ledger (INDEX-PLAN.md, Phase 1-2).

Reads `index/citations.tsv` (built by tools/build-citations.py) and emits the site's
index data. It computes NOTHING about citations itself: every judgement about what a
citation is, where it points and how confident that is was made by the extractor and
frozen in repo CLAUDE.md § "Index conventions". This file only regroups and renders.

    index/citations.tsv ──► site/src/data/index-scripture.json     (Phase 1)
                       └──► site/src/data/index-crossref.json      (Phase 2)
    index/authorities.tsv ─► site/src/data/authorities/*.json      (SITE-PLAN Phase 4)
                          ├► site/src/data/index-authorities-toc.json
                          └► site/src/data/authorities-by-chunk.json

Decisions frozen here, with reasons:

  * **Only `verse` and `chapter` resolutions enter the index.** A
    `chapter-out-of-range` record is a QA line (a digit-confusion candidate), not a
    citation — indexing it would publish a reading nobody has settled.
  * **Psalms carry BARE VULGATE numbers**, with a note on the book page. This is a
    Vulgate-based edition and Quaracchi's own index locorum is Vulgate. Dual
    numbering ("Psalm 24 (25)") would need a hand-built 150-row mapping whose
    split/merge points are easy to get subtly wrong; a wrong number in an index is
    worse than an unfamiliar one. Revisit only with a checked table.
  * **Anaphor-resolved citations ARE included** — an `ibid.` is a real citation — but
    carry `viaIbid`, because their reference is inherited from the printed sequence
    rather than printed at that spot. The display shows Quaracchi's `ibid.` verbatim.
  * **Unnumbered books** (`Cor*` — "ad Corinthios" with no numeral) get their own
    entry rather than being guessed into I or II.
  * **Snippets are rebuilt from the chunk files**, not stored in the ledger: it keeps
    the committed ledger lean and reuses the extractor's own section parser, so the
    two cannot drift.

Usage:
    python3.11 tools/build-index-json.py                # scripture + crossref
    python3.11 tools/build-index-json.py --scripture    # Phase 1 only
"""

from __future__ import annotations

import argparse
import csv
import glob
import importlib.util
import json
import os
import re
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "index", "citations.tsv")
AUTH_LEDGER = os.path.join(ROOT, "index", "authorities.tsv")
AUTH_TABLE = os.path.join(ROOT, "tools", "authorities.json")
BOOKS_JSON = os.path.join(ROOT, "tools", "scripture-books.json")
CONTENT = os.path.join(ROOT, "site", "src", "data", "content.json")
OUT_DIR = os.path.join(ROOT, "site", "src", "data")

SNIPPET_CHARS = 180
SPLIT_WARN_MB = 1.5  # above this, split index-scripture.json per book


def load_extractor():
    """Reuse the extractor's Chunk/section parser so snippets cannot drift from it."""
    spec = importlib.util.spec_from_file_location(
        "bc", os.path.join(ROOT, "tools", "build-citations.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def chunk_urls():
    """chunk id -> (url, book title, division title) from content.json.

    content.json is the site's own view of the corpus, so a URL built from it is a
    URL the site actually serves — safer than reconstructing one from frontmatter.
    """
    with open(CONTENT, encoding="utf-8") as fh:
        books = json.load(fh)
    out = {}
    for b in books:
        for d in b["distinctions"]:
            for q in d["questions"]:
                out[q["id"]] = {
                    "url": q["path"],  # readable address, derived in site/scripts/lib/addresses.mjs
                    "book": b["title"],
                    "division": d["title"],
                    "title": q.get("titleEn") or q.get("title") or q["id"],
                }
    return out


def section_texts(bc, chunk):
    out = {"latin_body": chunk.latin_body, "scholion": chunk.scholion}
    for lab, txt in chunk.apparatus.items():
        out[f"apparatus:{lab}"] = txt
    return out


def build_snippets(bc, rows):
    """Locate each citation's raw text in its own section and slice context around it."""
    wanted = defaultdict(set)
    for r in rows:
        wanted[r["chunk_id"]].add(r["section"])

    cache = {}
    for v in range(1, 6):
        for p in sorted(glob.glob(os.path.join(ROOT, f"vol{v}", "*.md"))):
            c = bc.Chunk(p)
            if c.cid in wanted:
                cache[c.cid] = section_texts(bc, c)

    snippets = {}
    for r in rows:
        secs = cache.get(r["chunk_id"])
        if not secs:
            continue
        text = secs.get(r["section"], "")
        raw = r["raw_text"]
        i = text.find(raw[:40]) if raw else -1
        if i < 0:
            i = 0
        lo = max(0, i - SNIPPET_CHARS // 2)
        frag = re.sub(r"\s+", " ", text[lo: lo + SNIPPET_CHARS]).strip()
        frag = re.sub(r"\[\^[A-Za-z0-9-]+\]", "", frag)  # drop footnote anchors
        frag = frag.replace("*", "")
        if lo > 0:
            frag = "…" + frag
        snippets[(r["chunk_id"], r["section"], r["raw_text"])] = frag + "…"
    return snippets


def section_label(section):
    if section == "latin_body":
        return "text"
    if section == "scholion":
        return "scholion"
    return "apparatus"


def build_scripture(rows, cfg, urls, snippets):
    meta = {b["key"]: b for b in cfg["books"]}
    grouped = defaultdict(lambda: defaultdict(list))  # book -> chapter -> [locus]

    for r in rows:
        if r["class"] != "scripture":
            continue
        if r["resolution"] not in ("verse", "chapter"):
            continue
        tgt = r["normalized_target"]
        m = re.match(r"^(\S+)\s+(\d+)(?::(\d+)(?:-(\d+))?)?$", tgt)
        if not m:
            continue
        key, chap = m.group(1), int(m.group(2))
        verse = int(m.group(3)) if m.group(3) else None
        verse_end = int(m.group(4)) if m.group(4) else None
        u = urls.get(r["chunk_id"])
        if not u:
            continue
        grouped[key][chap].append({
            "chunk": r["chunk_id"],
            "url": u["url"],
            "work": u["book"],
            "division": u["division"],
            "title": u["title"],
            "verse": verse,
            "verseEnd": verse_end,
            "tier": r["confidence"],
            "where": section_label(r["section"]),
            "raw": r["raw_text"],
            "viaIbid": bool(r["ibid_resolved"]),
            "snippet": snippets.get((r["chunk_id"], r["section"], r["raw_text"]), ""),
        })

    books = []
    for key, chapters in grouped.items():
        b = meta.get(key)
        if not b:
            continue
        chapter_list = []
        for n in sorted(chapters):
            loci = sorted(chapters[n], key=lambda l: (l["verse"] or 0, l["chunk"]))
            chapter_list.append({"chapter": n, "loci": loci})
        books.append({
            "key": key,
            "nameEn": b["name_en"],
            "nameLa": b["name_la"],
            "order": b["order"],
            "testament": b.get("testament", ""),
            "unnumbered": bool(b.get("unnumbered_of")),
            "count": sum(len(c["loci"]) for c in chapter_list),
            "chapters": chapter_list,
        })
    books.sort(key=lambda b: (b["order"], b["key"]))
    return books


def build_crossref(rows, urls):
    """Inbound backlinks per chunk: "who cites this?".

    Levels, kept distinct because they are claims of different precision:
      * `chunk`  — the citation names this exact unit
      * `page`   — it names a printed page this chunk shares (page-multi); precise
                   to the page, not to the unit
      * `unit`   — it addresses the whole distinction / article / work this chunk
                   belongs to (`d. 2. per totam`), not this chunk in particular

    Excluded: authority citations (another doctor's numbering), and a chunk citing
    itself. Repeat citations from one chunk collapse to a single row with a count.
    """
    inbound = defaultdict(dict)
    for r in rows:
        if r["class"] != "crossref":
            continue
        res = r["resolution"]
        if res == "chunk":
            level, targets = "chunk", [r["normalized_target"]]
        elif res == "page-multi":
            level, targets = "page", r["normalized_target"].split("+")
        elif res in ("articulus", "ambiguous"):
            level, targets = "unit", r["normalized_target"].split("+")
        else:
            continue  # distinctio/work targets are not chunk ids; forward/dangling skip

        src = r["chunk_id"]
        su = urls.get(src)
        if not su:
            continue
        for t in targets:
            if not t or t == src or t not in urls:
                continue
            slot = inbound[t]
            if src in slot:
                slot[src]["n"] += 1
                # a precise level wins over a vaguer one for the same pair
                if level == "chunk":
                    slot[src]["level"] = "chunk"
                continue
            # Land on the NOTE that cites, not the top of the citing chunk.
            note = r["section"].split(":", 1)[1] if r["section"].startswith("apparatus:") else ""
            slot[src] = {
                "chunk": src, "url": su["url"] + (f"#fn-{note}" if note else ""),
                "title": su["title"],
                "work": su["book"], "division": su["division"],
                "raw": r["raw_text"], "level": level, "n": 1,
                "viaIbid": bool(r["ibid_resolved"]),
                "anchor": r.get("anchor", ""),
            }

    return {t: sorted(v.values(), key=lambda x: (x["work"], x["division"], x["chunk"]))
            for t, v in inbound.items()}


GOTO_OUT = os.path.join(ROOT, "site", "public", "goto.json")

# Abbreviations a reader may type for each work, beyond the ledger's own table
# (tools/scripture-books.json `works`). Matching is case- and point-insensitive.
GOTO_EXTRA_ABBREV = {
    "breviloquium": ["Breviloquium", "Brev."],
    "itinerarium": ["Itinerarium", "Itin."],
    "de-reductione": ["de Reductione", "Red.", "De reductione artium"],
    "hexaemeron": ["Collat. in Hexaem.", "in Hexaem.", "Hexaemeron", "Hex."],
    "septem-donis": ["de Donis", "de septem donis", "Collat. de donis", "de donis Spiritus S."],
    "decem-praeceptis": ["de decem praeceptis", "de Praeceptis", "Collat. de decem praec.", "Praec."],
    "scientia-christi": ["de Scientia Christi", "Scient. Chr.", "QD de sc. Chr."],
    "mysterio-trinitatis": ["de Mysterio Trinitatis", "Myst. Trin.", "de Myst. Trin."],
    "perfectione-evangelica": ["de Perfectione evangelica", "Perf. ev.", "de Perf. evang."],
    "sermones-selecti": ["Sermones selecti", "Serm. sel."],
    "ecclesiasten": ["Comment. in Eccl.", "in Eccl.", "Ecclesiasten", "Eccl."],
    "sapientiam": ["Comment. in Sap.", "in Sap.", "in librum Sapientiae", "Sap."],
    "ioannem": ["Comment. in Ioan.", "Comment. in Ioannem", "in Ioan.", "in Ioannem"],
    "collationes-ioannem": ["Collat. in Ioan.", "Collationes in Ioannem", "Collat. in Ioannem", "Coll. in Ioan."],
}
ID_TOKEN_RE = re.compile(r"^([a-z]+?)(\d+)(?:-(\d+))?$")


def build_goto(bc, cfg):
    """site/public/goto.json — everything the go-to box needs, fetched on first use.

    Every chunk is listed with its COORDINATES, read from the frozen id and the
    frontmatter, never typed by hand: Sentences (book, distinction, pars, sectio,
    articulus, quaestio | type) exactly as build-citations.py's `by_locus` keys
    them; a work chunk by its id tokens (`bon-brev-p5-c6` -> p=5 c=6;
    `bon-ioan-c7-v40-53` -> c=7, verses 40-53) plus its paragraph range and
    Collationes units. The client resolves with the ledger's own rule: an
    unstated coordinate is a wildcard, and only a UNIQUE survivor resolves.
    Printed pages come from `by_page`, the same index the ledger resolves on."""
    with open(CONTENT, encoding="utf-8") as fh:
        books = json.load(fh)
    path_of, slug_of = {}, {}
    for b in books:
        for d in b["distinctions"]:
            for q in d["questions"]:
                path_of[q["id"]] = q["path"]
                slug_of[q["id"]] = b["slug"]

    paths = [p for v in sorted(bc.VOLUME_COMPLETE)
             for p in sorted(glob.glob(os.path.join(ROOT, f"vol{v}", "*.md")))]
    corpus = [c for c in (bc.Chunk(p) for p in paths) if c.cid in path_of]
    _, _, by_page, _ = bc.build_indexes(corpus)

    chunks = []
    for c in corpus:
        e = {"id": c.cid, "path": path_of[c.cid], "w": slug_of[c.cid]}
        if c.book and c.dist is not None and slug_of[c.cid] == "sentences":
            e["t"] = {k: v for k, v in (("b", c.book), ("d", c.dist), ("p", c.pars),
                                        ("s", c.sectio), ("a", c.art),
                                        ("q", c.quaestio)) if v is not None}
            if not c.quaestio:
                e["type"] = c.ctype
        else:
            t = {}
            prefix = re.match(r"^bon-[a-z]+-?", c.cid).group(0)
            # Tokens like p5 / c6 / q1 / a2 / v40 (+ range tail) / s1 / coll4.
            rest = c.cid[len(prefix):] if c.cid.startswith(prefix) else ""
            parts = rest.split("-") if rest else []
            i = 0
            while i < len(parts):
                m = re.match(r"^([a-z]+)(\d+)$", parts[i])
                if m:
                    key, num = m.group(1), int(m.group(2))
                    if key == "v":
                        end = num
                        if i + 1 < len(parts) and parts[i + 1].isdigit():
                            end = int(parts[i + 1]); i += 1
                        e["v"] = [num, end]
                    else:
                        t[key] = num
                elif parts[i]:
                    e["type"] = parts[i] if "type" not in e else e["type"] + "-" + parts[i]
                i += 1
            if t:
                e["t"] = t
            if c.paragraphs:
                e["n"] = list(c.paragraphs)
            units = {k: v for k, v in c.units.items() if v}
            if units:
                e["u"] = units
        chunks.append(e)

    works = {}
    for entry in cfg["works"]["entries"]:
        works.setdefault(entry["slug"], []).extend(entry["abbrev"])
    for slug, abbrevs in GOTO_EXTRA_ABBREV.items():
        works.setdefault(slug, []).extend(a for a in abbrevs if a not in works.get(slug, []))

    pages = {f"{v}:{p}": [path_of[cid] for cid in ids if cid in path_of]
             for (v, p), ids in by_page.items() if v is not None}
    out = {
        "_about": "Generated by tools/build-index-json.py. Do not hand-edit; regenerate.",
        "works": works,
        "chunks": chunks,
        "pages": {k: v for k, v in pages.items() if v},
    }
    with open(GOTO_OUT, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, separators=(",", ":"))
    print(f"goto            : {len(chunks)} chunks, {len(out['pages'])} printed pages, "
          f"{os.path.getsize(GOTO_OUT)/1e3:.0f} KB")


def build_authorities(urls):
    """The index of authorities (repo CLAUDE.md § "Authorities conventions"):
    author -> work -> loci, the two roles kept apart (R1), the locus as printed with
    its sort key (R3). One file per author, read from disk at build time by the
    pages (Augustine alone is ~1 MB); a small table of contents; and a per-chunk map
    for the panel on each text page."""
    if not os.path.exists(AUTH_LEDGER):
        raise SystemExit("index/authorities.tsv is missing: run tools/build-authorities.py first")
    with open(AUTH_TABLE, encoding="utf-8") as fh:
        table = json.load(fh)
    authors = {a["id"]: a for a in table["authors"]}
    works = {(a["id"], w["id"]): w for a in table["authors"] for w in a["works"]}
    with open(AUTH_LEDGER, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))

    order = {cid: i for i, cid in enumerate(urls)}  # reading order of the corpus

    def key(l):
        nums = [int(x) for x in l["key"].split(".") if x.isdigit()] if l["key"] else []
        return (nums or [10 ** 6], order.get(l["chunk"], 10 ** 6))

    per = defaultdict(lambda: defaultdict(list))
    by_chunk = defaultdict(lambda: defaultdict(int))
    for r in rows:
        u = urls.get(r["chunk_id"])
        if not u or r["author"] not in authors:
            continue
        wid = r["work"] or "unassigned"
        per[r["author"]][wid].append({
            "chunk": r["chunk_id"], "url": u["url"] + f"#fn-{r['note']}", "title": u["title"],
            "work": u["book"], "division": u["division"], "book": r["book"], "locus": r["locus"],
            "key": r["locus_key"], "role": r["role"], "pseudo": r["pseudo"] == "true",
            "named": r["via"].startswith("body-join"), "inherited": r["via"] == "anaphor",
            "raw": r["raw"],
        })
        by_chunk[r["chunk_id"]][(r["author"], wid)] += 1

    out_dir = os.path.join(OUT_DIR, "authorities")
    os.makedirs(out_dir, exist_ok=True)
    for stale in glob.glob(os.path.join(out_dir, "*.json")):
        os.remove(stale)
    about = ("Generated by tools/build-index-json.py from index/authorities.tsv. "
             "Do not hand-edit; regenerate.")
    toc, biggest = [], 0.0
    for aid, wmap in per.items():
        a = authors[aid]
        wl = []
        for wid, loci in wmap.items():
            w = works.get((aid, wid), {})
            loci.sort(key=key)
            wl.append({"id": wid, "la": w.get("la", ""), "en": w.get("en", ""),
                       "pseudo": bool(w.get("pseudo")), "count": len(loci),
                       "cited": sum(1 for l in loci if l["role"] == "cited"),
                       "samePassage": sum(1 for l in loci if l["role"] == "same-passage"),
                       "loci": loci})
        wl.sort(key=lambda w: (w["id"] == "unassigned", -w["count"], w["la"]))
        data = {"_about": about, "id": aid, "la": a["la"], "en": a.get("en", a["la"]),
                "count": sum(w["count"] for w in wl), "works": wl}
        path = os.path.join(out_dir, f"{aid}.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))
        biggest = max(biggest, os.path.getsize(path) / 1e6)
        toc.append({"id": aid, "la": a["la"], "en": a.get("en", a["la"]), "count": data["count"],
                    "cited": sum(w["cited"] for w in wl), "samePassage": sum(w["samePassage"] for w in wl),
                    "works": [{"id": w["id"], "la": w["la"], "count": w["count"]} for w in wl]})
    toc.sort(key=lambda a: a["en"])
    tpath = os.path.join(OUT_DIR, "index-authorities-toc.json")
    with open(tpath, "w", encoding="utf-8") as fh:
        json.dump({"_about": about, "authors": toc}, fh, ensure_ascii=False, separators=(",", ":"))
    chunks = {}
    for cid, d in by_chunk.items():
        chunks[cid] = sorted(([aid, wid, n] for (aid, wid), n in d.items()),
                             key=lambda x: (authors[x[0]].get("en", ""), x[1]))
    cpath = os.path.join(OUT_DIR, "authorities-by-chunk.json")
    with open(cpath, "w", encoding="utf-8") as fh:
        json.dump({"_about": about, "chunks": chunks}, fh, ensure_ascii=False, separators=(",", ":"))
    n = sum(a["count"] for a in toc)
    print(f"authorities     : {len(toc)} authors, {sum(len(a['works']) for a in toc)} works, {n} citations")
    print(f"  per author    : {out_dir}/  (largest {biggest:.2f} MB) · toc {os.path.getsize(tpath)/1e3:.0f} KB"
          f" · by-chunk {os.path.getsize(cpath)/1e3:.0f} KB ({len(chunks)} chunks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default=LEDGER)
    ap.add_argument("--scripture", action="store_true", help="Phase 1 only")
    args = ap.parse_args()

    bc = load_extractor()
    cfg = bc.load_books()
    with open(args.ledger, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))

    urls = chunk_urls()
    scripture_rows = [r for r in rows if r["class"] == "scripture"]
    snippets = build_snippets(bc, scripture_rows)
    books = build_scripture(rows, cfg, urls, snippets)

    # SPLIT PER BOOK. A single file is 3.8 MB, and on a static export every page
    # that imports it inlines it into that page's payload. The table of contents is
    # tiny; each book page loads only its own book.
    per_book_dir = os.path.join(OUT_DIR, "scripture")
    os.makedirs(per_book_dir, exist_ok=True)
    for stale in glob.glob(os.path.join(per_book_dir, "*.json")):
        os.remove(stale)

    ABOUT = ("Generated by tools/build-index-json.py from index/citations.tsv. "
             "Do not hand-edit; regenerate. Psalms use Vulgate numbering.")

    toc = {"_about": ABOUT, "books": []}
    biggest = 0.0
    for b in books:
        # `*` is legal in a book key (the unnumbered bucket) but not in a URL.
        slug = b["key"].replace("*", "-any").lower()
        b["slug"] = slug
        path = os.path.join(per_book_dir, f"{slug}.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({"_about": ABOUT, **b}, fh, ensure_ascii=False,
                      separators=(",", ":"))
        biggest = max(biggest, os.path.getsize(path) / 1e6)
        toc["books"].append({k: b[k] for k in
                             ("key", "slug", "nameEn", "nameLa", "order",
                              "testament", "unnumbered", "count")}
                            | {"chapters": len(b["chapters"])})

    toc_path = os.path.join(OUT_DIR, "index-scripture-toc.json")
    with open(toc_path, "w", encoding="utf-8") as fh:
        json.dump(toc, fh, ensure_ascii=False, separators=(",", ":"))

    total = sum(b["count"] for b in books)
    print(f"scripture index : {len(books)} books, {total} citations")
    print(f"  toc           : {os.path.getsize(toc_path)/1e3:.1f} KB")
    print(f"  per book      : {per_book_dir}/  (largest {biggest:.2f} MB)")
    if biggest > SPLIT_WARN_MB:
        print(f"  ⚠ a single book still exceeds {SPLIT_WARN_MB} MB")
    top = sorted(books, key=lambda b: -b["count"])[:6]
    print("  most cited    : " + " · ".join(f"{b['nameEn']} {b['count']}" for b in top))

    if args.scripture:
        return 0

    build_goto(bc, cfg)
    build_authorities(urls)

    inbound = build_crossref(rows, urls)
    xpath = os.path.join(OUT_DIR, "index-crossref.json")
    with open(xpath, "w", encoding="utf-8") as fh:
        json.dump({"_about": ABOUT, "inbound": inbound}, fh,
                  ensure_ascii=False, separators=(",", ":"))
    links = sum(len(v) for v in inbound.values())
    busiest = sorted(inbound.items(), key=lambda kv: -len(kv[1]))[:3]
    print(f"crossref index  : {len(inbound)} chunks cited, {links} backlinks, "
          f"{os.path.getsize(xpath)/1e6:.2f} MB")
    print("  most cited    : " + " · ".join(f"{k} ({len(v)})" for k, v in busiest))


if __name__ == "__main__":
    raise SystemExit(main())
