import Link from "next/link";
import { loadAllContent } from "@/lib/content";
import { DistinctionContent, romanize } from "@/components/distinction-content";

export function generateStaticParams() {
  const books = loadAllContent();
  const params: { bookId: string; distId: string }[] = [];
  for (const book of books) {
    for (const dist of book.distinctions) {
      params.push({ bookId: String(book.id), distId: String(dist.id) });
    }
  }
  return params;
}

export default async function DistinctionPage({
  params,
}: {
  params: Promise<{ bookId: string; distId: string }>;
}) {
  const { bookId, distId } = await params;
  const books = loadAllContent();
  const book = books.find((b) => b.id === parseInt(bookId));
  if (!book) return <p>Book not found.</p>;
  const dist = book.distinctions.find((d) => d.id === parseInt(distId));
  if (!dist) return <p>Distinction not found.</p>;

  return (
    <div>
      <Link href={`/browse/${book.id}`} className="back-link">
        &larr; Back to {book.title}
      </Link>

      <header className="dist-header">
        <h1 className="dist-page-title">
          {book.divisionLabel ? dist.title : `Distinction ${romanize(dist.id)}`}
        </h1>
      </header>

      <DistinctionContent
        bookId={book.id}
        distId={dist.id}
        questions={dist.questions}
      />
    </div>
  );
}
