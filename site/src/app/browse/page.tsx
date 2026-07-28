import Link from "next/link";
import { loadAllContent, browseEntries, divisionCountLabel } from "@/lib/content";
import { Illumination } from "@/components/decorations";

export default function BrowsePage() {
  const entries = browseEntries(loadAllContent());

  return (
    <div>
      <div className="section-title">Browse All Books</div>
      {entries.map((entry) => {
        const { href, key, letter, title, meta } =
          entry.kind === "book"
            ? {
                href: `/browse/${entry.book.id}`,
                key: `b${entry.book.id}`,
                letter: entry.book.initial ?? `${entry.book.id}`,
                title: entry.book.title,
                meta: divisionCountLabel(entry.book),
              }
            : {
                href: `/browse/tome/${entry.tome}`,
                key: `t${entry.tome}`,
                letter: entry.initial,
                title: entry.title,
                meta: `${entry.works.length} work${entry.works.length !== 1 ? "s" : ""}`,
              };

        return (
          <Link key={key} href={href} className="card-link">
            <div className="card">
              <div style={{ display: "flex", alignItems: "flex-start", gap: "1rem" }}>
                <Illumination size={44} letter={letter} />
                <div>
                  <h3 className="card-title">{title}</h3>
                  <p className="card-meta">{meta}</p>
                </div>
              </div>
            </div>
          </Link>
        );
      })}
    </div>
  );
}
