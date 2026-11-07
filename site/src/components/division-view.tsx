import Link from "next/link";
import type { Book, Distinction } from "@/lib/content";
import { DistinctionContent, divisionHeading } from "@/components/distinction-content";

export function DivisionView({ book, dist }: { book: Book; dist: Distinction }) {
  return (
    <div>
      <Link href={book.path} className="back-link">
        &larr; Back to {book.title}
      </Link>

      <header className="dist-header">
        <h1 className="dist-page-title">
          {divisionHeading(book, dist)}
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
