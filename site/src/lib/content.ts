import contentData from "@/data/content.json";

export interface ApparatusEntry {
  id: string;
  la: string;
  en: string;
}

export interface Question {
  id: string;
  title: string;
  titleLa?: string;
  titleEn?: string;
  type: string;
  latin: string;
  english: string;
  latinScholion: string;
  englishScholion: string;
  apparatus: ApparatusEntry[];
  notes: string;
  hasTranslation: boolean;
  pars?: number;
  articulus?: number;
  quaestio?: number;
  capitulum?: number;
  section?: number;
  /** Readable address, derived from the id (scripts/lib/addresses.mjs). */
  path: string;
  /** Printed span [first, last] from the chunk's `printed_pages`. */
  pages?: [number, number];
  /** Quaracchi paragraph range [first, last] (John commentary, ruling 73). */
  paragraphs?: [number, number];
}

export interface Distinction {
  id: number;
  title: string;
  questions: Question[];
  /** `/sentences/1/d3` for a Sentences distinction; `/{slug}#d-N` (an anchor
   *  on the landing page) for a work's division and for any division 0. */
  path: string;
}

export interface Book {
  id: number;
  title: string;
  slug: string; // "sentences" for Tomes I–IV, else the WORKS registry slug
  path: string; // `/sentences/1` or `/{slug}`
  titleLa: string;
  titleEn: string;
  genre: string;
  unitLabel: [string, string]; // singular, plural: "collation", "collations"
  pages?: [number, number]; // printed span of the whole work in its tome
  distinctions: Distinction[];
  // Vol V+ works only (Tome V onward holds multiple independent works;
  // each work is a Book whose divisions replace the Sentences' distinctions):
  tome?: number;
  initial?: string; // Illumination glyph, e.g. "B" for Breviloquium
  divisionLabel?: string; // e.g. "Parts" — UI label replacing "Distinctions"
  tomeTitle?: string; // e.g. "Book V: Opuscula Theologica" — container entry
  tomeInitial?: string; // Illumination glyph for that container, e.g. "5"
}

export function loadAllContent(): Book[] {
  return contentData as Book[];
}

/** A row in the top-level browse/home listing: either a standalone book
 *  (Tomes I–IV, one work each) or a tome that contains several works. */
export type BrowseEntry =
  | { kind: "book"; book: Book }
  | { kind: "tome"; tome: number; title: string; initial: string; works: Book[] };

/** Collapse multi-work tomes into a single container row, preserving order.
 *  Shared by the home page and the browse page so the two cannot drift. */
export function browseEntries(books: Book[]): BrowseEntry[] {
  const entries: BrowseEntry[] = [];
  const seen = new Map<number, Extract<BrowseEntry, { kind: "tome" }>>();

  for (const book of books) {
    if (!book.tomeTitle || book.tome === undefined) {
      entries.push({ kind: "book", book });
      continue;
    }
    const existing = seen.get(book.tome);
    if (existing) {
      existing.works.push(book);
      continue;
    }
    const group: Extract<BrowseEntry, { kind: "tome" }> = {
      kind: "tome",
      tome: book.tome,
      title: book.tomeTitle,
      initial: book.tomeInitial ?? `${book.tome}`,
      works: [book],
    };
    seen.set(book.tome, group);
    entries.push(group);
  }
  return entries;
}

export function tomeGroups(books: Book[]) {
  return browseEntries(books).filter(
    (e): e is Extract<BrowseEntry, { kind: "tome" }> => e.kind === "tome"
  );
}

/** "40 distinctions" / "2 parts" — divisionLabel overrides the default.
 *  Division 0 is a prologue, not a numbered division, so it is excluded from
 *  the count: the Breviloquium's prologue is not one of its seven partes. */
export function divisionCountLabel(book: Book): string {
  const n = book.distinctions.filter((d) => d.id !== 0).length;
  if (!book.divisionLabel) return `${n} distinction${n !== 1 ? "s" : ""}`;
  const label = n === 1 ? book.divisionLabel.replace(/s$/, "") : book.divisionLabel;
  return `${n} ${label.toLowerCase()}`;
}

/** One chunk's place in reading order. */
export interface ReadingStop {
  book: Book;
  dist: Distinction;
  q: Question;
}

let _sequence: Map<number, ReadingStop[]> | null = null;

/** Reading order within a tome: every chunk of every division of every work,
 *  in content order. Previous/next run across divisions and on into the next
 *  work of the same tome, and stop at the tome's edge. Tomes I–IV hold one
 *  work each, so there a book is a tome. */
export function tomeSequence(books: Book[], book: Book): ReadingStop[] {
  if (!_sequence) {
    _sequence = new Map();
    for (const b of books) {
      const key = b.tome ?? b.id;
      if (!_sequence.has(key)) _sequence.set(key, []);
      const seq = _sequence.get(key)!;
      for (const d of b.distinctions) for (const q of d.questions) seq.push({ book: b, dist: d, q });
    }
  }
  return _sequence.get(book.tome ?? book.id) ?? [];
}

/** Address of a chunk page. */
export function chunkHref(stop: ReadingStop): string {
  return stop.q.path;
}

let _byPath: Map<string, ReadingStop> | null = null;

/** Look a chunk up by its readable address. */
export function findChunk(books: Book[], path: string): ReadingStop | undefined {
  if (!_byPath) {
    _byPath = new Map();
    for (const book of books)
      for (const dist of book.distinctions)
        for (const q of dist.questions) _byPath.set(q.path, { book, dist, q });
  }
  return _byPath.get(path);
}

/** Every chunk, for generateStaticParams. */
export function allChunks(books: Book[]): ReadingStop[] {
  return books.flatMap((book) =>
    book.distinctions.flatMap((dist) => dist.questions.map((q) => ({ book, dist, q })))
  );
}

/** Where a tome's page lives. */
export const tomePath = (tome: number) => `/tome/${tome}`;

/** "1 collation" / "24 collations": the work's own noun for one chunk. */
export function unitCount(book: Book, n: number): string {
  return `${n} ${n === 1 ? book.unitLabel[0] : book.unitLabel[1]}`;
}

export const chunkCount = (book: Book) =>
  book.distinctions.reduce((s, d) => s + d.questions.length, 0);

export const pageSpan = (p?: [number, number]) =>
  !p ? "" : p[0] === p[1] ? `p. ${p[0]}` : `pp. ${p[0]}\u2013${p[1]}`;
