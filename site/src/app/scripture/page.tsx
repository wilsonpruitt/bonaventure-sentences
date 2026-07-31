import Link from "next/link";
import { Illumination, CrossDivider } from "@/components/decorations";
import toc from "@/data/index-scripture-toc.json";

export const metadata = {
  title: "Index of Scripture — Bonaventure, Opera Omnia",
  description:
    "Every scriptural citation in the translated Opera Omnia of St. Bonaventure, "
    + "in Vulgate order — derived from Quaracchi's own text and apparatus.",
};

type TocBook = {
  key: string;
  slug: string;
  nameEn: string;
  nameLa: string;
  order: number;
  testament: string;
  unnumbered: boolean;
  count: number;
  chapters: number;
};

export default function ScriptureIndexPage() {
  const books = (toc.books as TocBook[]).slice().sort((a, b) => a.order - b.order);
  const total = books.reduce((n, b) => n + b.count, 0);
  const ot = books.filter((b) => b.testament === "OT");
  const nt = books.filter((b) => b.testament === "NT");

  const section = (label: string, list: TocBook[]) => (
    <>
      <div className="section-title">{label}</div>
      <div className="question-list">
        {list.map((b) => (
          <Link
            key={b.key}
            href={`/scripture/${b.slug}`}
            className="card card-link"
          >
            <div className="card-title">
              {b.nameEn}
              {b.unnumbered && (
                <span className="card-meta"> — letter unspecified</span>
              )}
            </div>
            <div className="card-meta">
              <span style={{ fontStyle: "italic" }}>{b.nameLa}</span>
              {" · "}
              {b.count} citation{b.count !== 1 ? "s" : ""}
              {" · "}
              {b.chapters} chapter{b.chapters !== 1 ? "s" : ""}
            </div>
          </Link>
        ))}
      </div>
    </>
  );

  return (
    <div>
      <Link href="/" className="back-link">
        &larr; Home
      </Link>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "1rem",
          marginBottom: "1rem",
        }}
      >
        <Illumination size={50} letter="S" />
        <h2 className="h2">Index of Scripture</h2>
      </div>
      <CrossDivider />

      <div className="body-text" style={{ marginBottom: "2rem" }}>
        <p>
          Every scriptural citation in the translated portion of the{" "}
          <em>Opera Omnia</em> — {total.toLocaleString()} in all, across{" "}
          {books.length} books. The index is <strong>derived</strong> from the
          text and the Quaracchi apparatus rather than tagged by hand, and it
          grows with the translation.
        </p>
        <p>
          Bonaventure normally cites a chapter without a verse (
          <em>Ioannis decimo octavo</em>), and the Quaracchi editors supply the
          verse in their footnote. The index joins the two through the footnote
          anchor. Where no verse is recoverable, the citation is listed at the
          chapter and <strong>not guessed</strong> to a verse.
        </p>
        <p>
          <strong>Psalms follow Vulgate numbering</strong>, as does the edition
          itself and Quaracchi&rsquo;s own <em>index locorum</em>. Books are in
          Vulgate canonical order.
        </p>
      </div>

      {section("Old Testament", ot)}
      {nt.length > 0 && section("New Testament", nt)}
    </div>
  );
}
