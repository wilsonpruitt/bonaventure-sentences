import Link from "next/link";
import { loadAllContent } from "@/lib/content";
import { Illumination } from "@/components/decorations";

export default function BrowsePage() {
  const books = loadAllContent();

  return (
    <div>
      <div className="section-title">Browse All Books</div>
      {books.map((book) => (
        <Link key={book.id} href={`/browse/${book.id}`} className="card-link">
          <div className="card">
            <div style={{ display: "flex", alignItems: "flex-start", gap: "1rem" }}>
              <Illumination size={44} letter={book.initial ?? `${book.id}`} />
              <div>
                <h3 className="card-title">{book.title}</h3>
                <p className="card-meta">
                  {book.distinctions.length}{" "}
                  {book.divisionLabel
                    ? (book.distinctions.length === 1
                        ? book.divisionLabel.replace(/s$/, "")
                        : book.divisionLabel
                      ).toLowerCase()
                    : `distinction${book.distinctions.length !== 1 ? "s" : ""}`}
                </p>
              </div>
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
}
