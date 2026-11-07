import Link from "next/link";
import { loadAllContent, tomeSequence, chunkHref, type ReadingStop } from "@/lib/content";
import { CrossDivider } from "@/components/decorations";
import { TextReader } from "@/components/text-reader";
import { CitedBy } from "@/components/cited-by";

const SITE_URL = "https://bonaventure.wrootpress.com";

/** Metadata for a chunk page, at its readable address. */
export function chunkMetadata(stop: ReadingStop | undefined) {
  if (!stop) return {};
  return {
    title: stop.q.title,
    alternates: { canonical: `${SITE_URL}${stop.q.path}` },
  };
}

export function ChunkView({ stop }: { stop: ReadingStop }) {
  const { book, dist, q: question } = stop;
  const books = loadAllContent();

  // Prev/next run across divisions and works, within the tome.
  const seq = tomeSequence(books, book);
  const pos = seq.findIndex((st) => st.q.id === question.id && st.book.id === book.id);
  const prevStop = pos > 0 ? seq[pos - 1] : null;
  const nextStop = pos >= 0 && pos < seq.length - 1 ? seq[pos + 1] : null;
  // When a step leaves this division (or work), say where it goes.
  const context = (st: ReadingStop) =>
    st.book.id !== book.id ? st.book.title : st.dist.id !== dist.id ? st.dist.title : null;

  const canonicalUrl = `${SITE_URL}${question.path}`;
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "CreativeWork",
    "@id": canonicalUrl,
    url: canonicalUrl,
    name: question.title,
    author: { "@type": "Person", name: "St. Bonaventure" },
    translator: { "@type": "Organization", name: "Wroot Press" },
    publisher: {
      "@type": "Organization",
      name: "Wroot Press",
      url: "https://bonaventure.wrootpress.com",
    },
    inLanguage: ["en", "la"],
    isBasedOn: {
      "@type": "Book",
      name: "Opera Omnia (Quaracchi critical edition)",
      volumeNumber: book.tome ?? book.id,
    },
    isPartOf: { "@type": "Collection", "@id": `${SITE_URL}${book.path}` },
    license: "https://creativecommons.org/licenses/by-nc/4.0/",
    dateModified: new Date().toISOString().slice(0, 10),
  };

  const tomeLabel = `Tome ${["I","II","III","IV","V","VI","VII","VIII","IX","X"][(book.tome ?? book.id) - 1]}`;
  return (
    // Pagefind indexes chunk pages only (data-pagefind-body), with work and
    // tome as filters; navigation and cited-by panels are excluded.
    <div data-pagefind-body>
      <span data-pagefind-filter="work" data-pagefind-ignore hidden>{book.title}</span>
      <span data-pagefind-filter="tome" data-pagefind-ignore hidden>{tomeLabel}</span>
      <span data-pagefind-meta="context" data-pagefind-ignore hidden>{`${book.title} · ${dist.title}`}</span>
      <script
        type="application/ld+json"
        // eslint-disable-next-line react/no-danger
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />
      <Link href={dist.path} className="back-link" data-pagefind-ignore>
        &larr; Back to {dist.title}
      </Link>

      <h2 className="h2" style={{ fontSize: "22px", marginBottom: "0.25rem" }} data-pagefind-meta="title">
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

      <div data-pagefind-ignore>
        <CitedBy chunkId={question.id} />
      </div>

      {(prevStop || nextStop) && (
        <nav
          data-pagefind-ignore
          aria-label="Reading order"
          style={{
            display: "flex",
            justifyContent: "space-between",
            gap: "1.5rem",
            marginTop: "2rem",
            paddingTop: "1rem",
            borderTop: "1px solid rgba(139,105,20,0.2)",
          }}
        >
          {prevStop ? (
            <Link href={chunkHref(prevStop)} className="back-link" rel="prev">
              {context(prevStop) && <span className="seq-context">{context(prevStop)}</span>}
              &larr; {prevStop.q.title}
            </Link>
          ) : (
            <span />
          )}
          {nextStop && (
            <Link
              href={chunkHref(nextStop)}
              className="back-link"
              rel="next"
              style={{ textAlign: "right" }}
            >
              {context(nextStop) && <span className="seq-context">{context(nextStop)}</span>}
              {nextStop.q.title} &rarr;
            </Link>
          )}
        </nav>
      )}
    </div>
  );
}
