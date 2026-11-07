import Link from "next/link";
import { tomePath, unitCount, chunkCount, pageSpan, divisionCountLabel, type Book } from "@/lib/content";
import progress from "@/data/progress.json";

type Vol = {
  n: number; tome: string; year: number; state: string;
  works?: { slug: string; complete: boolean }[];
};

// Factual header (SITE-PLAN Phase 1; Wilson 2026-11-06: no editorial intro).
function workStatus(book: Book, vol?: Vol): string {
  const w = vol?.works?.find((x) => x.slug === book.slug);
  if (w) return w.complete ? "Complete" : "In progress";
  if (vol?.state === "complete") return "Complete";
  return vol?.state === "in-progress" ? "In progress" : "Planned";
}
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
        <div>
          <h2 className="h2" style={{ marginBottom: "0.15rem" }}>
            {book.slug === "sentences" ? book.titleEn : book.titleLa}
          </h2>
          <p className="card-meta" style={{ fontStyle: "italic" }}>
            {book.slug === "sentences" ? book.titleLa : book.titleEn}
          </p>
        </div>
      </div>
      {(() => {
        const tomeN = book.tome ?? book.id;
        const vol = (progress.volumes as Vol[]).find((v) => v.n === tomeN);
        return (
          <dl className="work-facts">
            <dt>Genre</dt>
            <dd>{book.genre}</dd>
            <dt>Edition</dt>
            <dd>
              Quaracchi <em>Opera Omnia</em>, tom. {vol?.tome ?? tomeN}
              {vol ? ` (${vol.year})` : ""}
              {book.pages ? `, ${pageSpan(book.pages)}` : ""}
            </dd>
            {book.distinctions.length > 1 && (
              <>
                <dt>Structure</dt>
                <dd>{divisionCountLabel(book)}</dd>
              </>
            )}
            <dt>On this site</dt>
            <dd>
              {chunkCount(book)} page{chunkCount(book) !== 1 ? "s" : ""} of text, Latin and English
            </dd>
            <dt>Status</dt>
            <dd>{workStatus(book, vol)}</dd>
            <dt>Citation</dt>
            <dd>
              By Quaracchi tome and page. Each page of the text gives its own citation under
              &ldquo;Cite this.&rdquo;
            </dd>
          </dl>
        );
      })()}
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
                  {dist.questions.length > 1 &&
                    (dist.id === 0 && book.slug !== "sentences"
                      ? `${dist.questions.length} sections`
                      : unitCount(book, dist.questions.length))}
                  {translated > 0 && translated < dist.questions.length && (
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
                  unitPlural={book.slug === "sentences" ? "Questions" : ""}
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
