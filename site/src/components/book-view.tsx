import Link from "next/link";
import { tomePath, type Book } from "@/lib/content";
import { Illumination, CrossDivider } from "@/components/decorations";
import { DistinctionContent, divisionHeading } from "@/components/distinction-content";

export function BookView({ book }: { book: Book }) {
  return (
    <div>
      {/* A work inside a multi-work tome goes back to its tome, not the top
          level. */}
      <Link
        href={book.tomeTitle && book.tome !== undefined ? tomePath(book.tome) : "/browse"}
        className="back-link"
      >
        &larr; {book.tomeTitle ?? "All Books"}
      </Link>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "1rem",
          marginBottom: "1rem",
        }}
      >
        <Illumination size={50} letter={book.initial ?? `${book.id}`} />
        <h2 className="h2">{book.title}</h2>
      </div>
      <CrossDivider />
      <div className="section-title">{book.divisionLabel ?? "Distinctions"}</div>

      <div className="distinction-accordion">
        {book.distinctions.map((dist) => {
          const translated = dist.questions.filter((q) => q.hasTranslation).length;
          return (
            <details
              key={dist.id}
              id={`d-${dist.id}`}
              className="distinction-details"
            >
              <summary className="distinction-summary">
                <span className="distinction-summary-chevron" aria-hidden>
                  &rsaquo;
                </span>
                <span className="distinction-summary-heading">
                  {divisionHeading(book, dist)}
                </span>
                <span className="distinction-summary-meta">
                  {dist.questions.length} question
                  {dist.questions.length !== 1 ? "s" : ""}
                  {translated > 0 && (
                    <>
                      {" "}
                      &middot;{" "}
                      <span className="translated-badge">
                        {translated} translated
                      </span>
                    </>
                  )}
                </span>
              </summary>
              <div className="distinction-details-body">
                <DistinctionContent
                  bookId={book.id}
                  distId={dist.id}
                  questions={dist.questions}
                />
              </div>
            </details>
          );
        })}
      </div>
    </div>
  );
}
