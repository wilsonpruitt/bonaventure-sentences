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
}

export interface Distinction {
  id: number;
  title: string;
  questions: Question[];
}

export interface Book {
  id: number;
  title: string;
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

/** Address of a chunk page (pre-Phase-2 scheme). */
export function chunkHref(stop: ReadingStop): string {
  return `/browse/${stop.book.id}/d/${stop.dist.id}/q/${encodeURIComponent(stop.q.id)}`;
}
