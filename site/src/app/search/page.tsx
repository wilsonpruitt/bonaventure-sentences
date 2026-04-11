import { loadAllContent } from "@/lib/content";
import { SearchClient } from "./search-client";

export default function SearchPage() {
  const books = loadAllContent();

  // Build a flat search index with just the text needed for client-side search
  const searchIndex = books.flatMap((book) =>
    book.distinctions.flatMap((dist) =>
      dist.questions
        .filter((q) => q.hasTranslation)
        .map((q) => ({
          id: q.id,
          title: q.title,
          bookId: book.id,
          bookTitle: book.title,
          distId: dist.id,
          distTitle: dist.title,
          // Only send first 500 chars to keep bundle small
          englishPreview: q.english.substring(0, 500),
        }))
    )
  );

  return <SearchClient searchIndex={searchIndex} />;
}
