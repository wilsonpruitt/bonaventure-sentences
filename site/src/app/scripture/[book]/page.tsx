import fs from "node:fs";
import path from "node:path";
import Link from "next/link";
import { CrossDivider } from "@/components/decorations";
import toc from "@/data/index-scripture-toc.json";

type TocBook = {
  key: string;
  slug: string;
  nameEn: string;
  nameLa: string;
  testament: string;
  unnumbered: boolean;
  count: number;
  chapters: number;
};

type Locus = {
  chunk: string;
  url: string;
  work: string;
  division: string;
  title: string;
  verse: number | null;
  verseEnd: number | null;
  tier: string;
  where: string;
  raw: string;
  viaIbid: boolean;
  snippet: string;
};

type BookIndex = {
  key: string;
  slug: string;
  nameEn: string;
  nameLa: string;
  unnumbered: boolean;
  count: number;
  chapters: { chapter: number; loci: Locus[] }[];
};

// The per-book files are read from disk at BUILD time rather than imported, so a
// page's payload carries only its own book. The whole index is 3.8 MB; the largest
// single book is 0.41 MB.
function loadBook(slug: string): BookIndex | null {
  const file = path.join(process.cwd(), "src", "data", "scripture", `${slug}.json`);
  if (!fs.existsSync(file)) return null;
  return JSON.parse(fs.readFileSync(file, "utf-8")) as BookIndex;
}

export function generateStaticParams() {
  return (toc.books as TocBook[]).map((b) => ({ book: b.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ book: string }>;
}) {
  const { book } = await params;
  const meta = (toc.books as TocBook[]).find((b) => b.slug === book);
  return {
    title: meta
      ? `${meta.nameEn} — Index of Scripture — Bonaventure`
      : "Index of Scripture — Bonaventure",
  };
}

function verseLabel(l: Locus) {
  if (l.verse === null) return "chapter";
  return l.verseEnd ? `${l.verse}–${l.verseEnd}` : String(l.verse);
}

export default async function ScriptureBookPage({
  params,
}: {
  params: Promise<{ book: string }>;
}) {
  const { book } = await params;
  const data = loadBook(book);
  if (!data) return <p>Book not found.</p>;

  return (
    <div>
      <Link href="/scripture" className="back-link">
        &larr; Index of Scripture
      </Link>
      <h2 className="h2">{data.nameEn}</h2>
      <p className="card-meta" style={{ marginTop: "-0.5rem" }}>
        <span style={{ fontStyle: "italic" }}>{data.nameLa}</span> ·{" "}
        {data.count} citation{data.count !== 1 ? "s" : ""}
      </p>
      <CrossDivider />

      {data.unnumbered && (
        <p className="body-text">
          Citations here name the book <strong>without its numeral</strong> (for
          example <em>ad Corinthios</em> with no <em>prima</em> or{" "}
          <em>secunda</em>). They are listed separately rather than assigned to
          one letter or the other.
        </p>
      )}
      {data.key === "Ps" && (
        <p className="body-text">
          Psalms are numbered as in the <strong>Vulgate</strong>, which runs one
          behind the Hebrew numbering through most of the psalter.
        </p>
      )}

      {data.chapters.map((ch) => (
        <div key={ch.chapter} className="dist-section">
          <div className="section-title">
            {data.nameEn} {ch.chapter}
          </div>
          <div className="question-list">
            {ch.loci.map((l, i) => (
              <Link key={`${l.chunk}-${i}`} href={l.url} className="card card-link">
                <div className="card-title">
                  <span className="apparatus-num">{verseLabel(l)}</span>{" "}
                  {l.title}
                </div>
                <div className="card-meta">
                  {l.work} · {l.division} · in the {l.where}
                  {l.viaIbid && (
                    <>
                      {" · "}
                      <span title="Quaracchi prints ibid. here; the reference is inherited from the preceding citation.">
                        via <em>ibid.</em>
                      </span>
                    </>
                  )}
                  {l.tier === "C" && (
                    <>
                      {" · "}
                      <span title="Chapter only — no verse is recoverable, and none is guessed.">
                        chapter only
                      </span>
                    </>
                  )}
                </div>
                {l.snippet && (
                  <div className="card-meta" style={{ fontStyle: "italic" }}>
                    {l.snippet}
                  </div>
                )}
              </Link>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
