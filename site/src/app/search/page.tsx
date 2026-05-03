import { loadAllContent } from "@/lib/content";
import { SearchClient } from "./search-client";

export default function SearchPage() {
  const books = loadAllContent();

  // Build a flat search index. Include BOTH latin and english previews so
  // the client can search either language. Chunks without an English
  // translation are still Latin-searchable.
  const searchIndex = books.flatMap((book) =>
    book.distinctions.flatMap((dist) =>
      dist.questions.map((q) => ({
        id: q.id,
        title: q.title,
        bookId: book.id,
        bookTitle: book.title,
        distId: dist.id,
        distTitle: dist.title,
        hasTranslation: q.hasTranslation,
        // First 500 chars of each — keeps the index compact.
        latinPreview: q.latin.substring(0, 500),
        englishPreview: q.english.substring(0, 500),
      }))
    )
  );

  return <SearchClient searchIndex={searchIndex} />;
}
