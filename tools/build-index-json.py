#!/usr/bin/env python3.11
"""
build-index-json.py — views over the citation ledger (INDEX-PLAN.md, Phase 1-2).

Reads `index/citations.tsv` (built by tools/build-citations.py) and emits the site's
index data. It computes NOTHING about citations itself: every judgement about what a
citation is, where it points and how confident that is was made by the extractor and
frozen in repo CLAUDE.md § "Index conventions". This file only regroups and renders.

    index/citations.tsv ──► site/src/data/index-scripture.json     (Phase 1)
                       └──► site/src/data/index-crossref.json      (Phase 2)

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
                    "url": f"/browse/{b['id']}/d/{d['id']}/q/{q['id']}",
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
            slot[src] = {
                "chunk": src, "url": su["url"], "title": su["title"],
                "work": su["book"], "division": su["division"],
                "raw": r["raw_text"], "level": level, "n": 1,
                "viaIbid": bool(r["ibid_resolved"]),
            }

    return {t: sorted(v.values(), key=lambda x: (x["work"], x["division"], x["chunk"]))
            for t, v in inbound.items()}


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
