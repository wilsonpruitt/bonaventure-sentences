// Readable addresses (SITE-PLAN Phase 2). ONE place derives every address on
// the site, from the frozen chunk ids, so an address is as permanent as the id
// it comes from. build-content.mjs stamps the results into content.json; every
// page, the indices (tools/build-index-json.py), the reading-layer siblings
// and the redirect rules (build-redirects.mjs) read them from there or from here.
//
//   Sentences  /sentences/{book}                    book (Tomes I–IV)
//              /sentences/{book}/d{N}               distinction N
//              /sentences/{book}/d{N}/{unit}        chunk bon-sent-{R}-d{N}-{unit}
//              /sentences/{book}/{unit}             division-0 chunk bon-sent-{R}-{unit}
//   Works      /{slug}                              work landing page (registry slug)
//              /{slug}#d-{N}                        a division (anchor on the landing page)
//              /{slug}/{unit}                       chunk bon-{abbr}-{unit}
//              /{slug}/text                         a work that is ONE chunk with a bare id (bon-red)
//   Tomes      /tome/{n}
//
// The build FAILS on any id that does not fit, rather than inventing an address.

export const ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"];

/** App routes a work slug must never shadow. */
export const RESERVED_TOP = new Set([
  "about", "browse", "export", "progress", "rights", "scripture", "search", "sitemap",
  "sentences", "tome", "authorities", "pagefind", "_next", "api",
]);

const UNIT_RE = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

/** The id prefix every chunk of a work shares: `bon-{abbr}-`, or the bare id
 *  for a one-chunk work. Sentences books return `bon-sent-{R}-`. */
export function idPrefix(book) {
  if (book.tome === undefined) return `bon-sent-${ROMAN[book.id - 1]}-`;
  const first = book.distinctions[0].questions[0].id;
  const m = first.match(/^(bon-[a-z]+)(-|$)/);
  if (!m) throw new Error(`addresses: cannot read an id prefix from ${first}`);
  return m[2] ? `${m[1]}-` : m[1];
}

export function assignAddresses(books, slugForBook) {
  const seen = new Map();
  const claim = (p, who) => {
    if (seen.has(p)) throw new Error(`addresses: ${p} claimed by both ${seen.get(p)} and ${who}`);
    seen.set(p, who);
  };
  for (const book of books) {
    const sentences = book.tome === undefined;
    const slug = sentences ? "sentences" : slugForBook(book.id);
    if (!slug) throw new Error(`addresses: book ${book.id} has no registry slug`);
    if (!sentences && RESERVED_TOP.has(slug)) throw new Error(`addresses: slug ${slug} shadows an app route`);
    book.slug = slug;
    book.path = sentences ? `/sentences/${book.id}` : `/${slug}`;
    claim(book.path, `book ${book.id}`);
    const prefix = idPrefix(book);

    for (const dist of book.distinctions) {
      dist.path = sentences && dist.id !== 0 ? `${book.path}/d${dist.id}` : `${book.path}#d-${dist.id}`;
      if (!dist.path.includes("#")) claim(dist.path, `book ${book.id} d.${dist.id}`);

      for (const q of dist.questions) {
        let unit;
        if (q.id === prefix) unit = "text"; // one-chunk work, bare id
        else if (q.id.startsWith(prefix)) unit = q.id.slice(prefix.length);
        else throw new Error(`addresses: ${q.id} does not start with its work's prefix ${prefix}`);

        if (sentences && dist.id !== 0) {
          const m = unit.match(/^d(\d+)-(.+)$/);
          if (!m || Number(m[1]) !== dist.id)
            throw new Error(`addresses: ${q.id} is filed under d.${dist.id} but its id says otherwise`);
          unit = m[2];
        } else if (sentences && /^d\d+(-|$)/.test(unit)) {
          throw new Error(`addresses: division-0 chunk ${q.id} looks like a distinction address`);
        }
        if (!UNIT_RE.test(unit)) throw new Error(`addresses: ${q.id} gives an unsafe unit "${unit}"`);
        q.path = `${sentences && dist.id !== 0 ? dist.path : book.path}/${unit}`;
        claim(q.path, q.id);
      }
    }
  }
  return books;
}
