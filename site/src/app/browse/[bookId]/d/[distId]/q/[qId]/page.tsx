import Link from "next/link";
import { loadAllContent } from "@/lib/content";
import { CrossDivider } from "@/components/decorations";
import { TextReader } from "./text-reader";
import { CitedBy } from "@/components/cited-by";

export function generateStaticParams() {
  const books = loadAllContent();
  const params: { bookId: string; distId: string; qId: string }[] = [];
  for (const book of books) {
    for (const dist of book.distinctions) {
      for (const q of dist.questions) {
        params.push({
          bookId: String(book.id),
          distId: String(dist.id),
          qId: q.id,
        });
      }
    }
  }
  return params;
}

export default async function QuestionPage({
  params,
}: {
  params: Promise<{ bookId: string; distId: string; qId: string }>;
}) {
  const { bookId, distId, qId } = await params;
  const books = loadAllContent();
  const book = books.find((b) => b.id === parseInt(bookId));
  if (!book) return <p>Book not found.</p>;
  const dist = book.distinctions.find((d) => d.id === parseInt(distId));
  if (!dist) return <p>Distinction not found.</p>;
  const question = dist.questions.find((q) => q.id === decodeURIComponent(qId));
  if (!question) return <p>Question not found.</p>;

  // Find prev/next
  const qIdx = dist.questions.findIndex((q) => q.id === question.id);
  const prevQ = qIdx > 0 ? dist.questions[qIdx - 1] : null;
  const nextQ = qIdx < dist.questions.length - 1 ? dist.questions[qIdx + 1] : null;

  return (
    <div>
      <Link href={`/browse/${book.id}/d/${dist.id}`} className="back-link">
        &larr; Back to {dist.title}
      </Link>

      <h2 className="h2" style={{ fontSize: "22px", marginBottom: "0.25rem" }}>
        {question.title}
      </h2>
      <p
        style={{
          fontSize: "13px",
          color: "#8B6914",
          fontFamily: "var(--font-cinzel), serif",
          letterSpacing: "0.08em",
          marginBottom: "0.5rem",
        }}
      >
        {book.title} &middot; {dist.title}
      </p>

      <CrossDivider />

      <TextReader
        latin={question.latin}
        english={question.english}
        latinScholion={question.latinScholion ?? ""}
        englishScholion={question.englishScholion ?? ""}
        apparatus={question.apparatus ?? []}
        hasTranslation={question.hasTranslation}
      />

      <CitedBy chunkId={question.id} />

      {(prevQ || nextQ) && (
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            marginTop: "2rem",
            paddingTop: "1rem",
            borderTop: "1px solid rgba(139,105,20,0.2)",
          }}
        >
          {prevQ ? (
            <Link
              href={`/browse/${book.id}/d/${dist.id}/q/${encodeURIComponent(prevQ.id)}`}
              className="back-link"
            >
              &larr; {prevQ.title}
            </Link>
          ) : (
            <span />
          )}
          {nextQ && (
            <Link
              href={`/browse/${book.id}/d/${dist.id}/q/${encodeURIComponent(nextQ.id)}`}
              className="back-link"
            >
              {nextQ.title} &rarr;
            </Link>
          )}
        </div>
      )}
    </div>
  );
}
