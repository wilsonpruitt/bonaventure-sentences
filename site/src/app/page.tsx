import Link from "next/link";
import { loadAllContent, browseEntries, divisionCountLabel, tomePath } from "@/lib/content";
import progress from "@/data/progress.json";
import { HomeIntro } from "@/components/site-copy";
import { Illumination, CrossDivider, FleuronDivider } from "@/components/decorations";

// The scope table is DERIVED: titles, years, glosses and status come from
// progress.json (scripts/build-progress.mjs), never hand-written rows, so it
// cannot go stale as volumes close. Vol X is not transcribed: the site's
// generated indices replace it (SITE-PLAN decision 3).
type ScopeStatus = "complete" | "in-progress" | "planned" | "indices";
const SCOPE_LABEL: Record<ScopeStatus, string> = {
  complete: "Complete",
  "in-progress": "In progress",
  planned: "Planned",
  indices: "Generated indices",
};
interface ProgressVolume {
  n: number;
  tome: string;
  year: number;
  title: string;
  gloss: string;
  state: "complete" | "in-progress" | "planned";
  counted?: boolean;
  works?: { slug: string; title: string; complete: boolean }[];
}
function scopeRows(published: Map<number, string>, tomesWithWorks: Set<number>) {
  return (progress.volumes as ProgressVolume[]).map((v) => {
    const isIndexVolume = v.counted === false;
    const status: ScopeStatus = isIndexVolume ? "indices" : v.state;
    const href = isIndexVolume
      ? "/scripture"
      : tomesWithWorks.has(v.n)
        ? tomePath(v.n)
        : published.get(v.n);
    const pending =
      v.state === "in-progress" && v.works ? v.works.filter((w) => !w.complete) : [];
    return { ...v, status, href, pending };
  });
}

export default function HomePage() {
  const books = loadAllContent();
  const totalTranslated = books.reduce(
    (sum, b) =>
      sum + b.distinctions.reduce((s, d) => s + d.questions.filter((q) => q.hasTranslation).length, 0),
    0
  );
  const totalQuestions = books.reduce(
    (sum, b) => sum + b.distinctions.reduce((s, d) => s + d.questions.length, 0),
    0
  );

  return (
    <div>
      <div style={{ textAlign: "center", margin: "2rem 0 3rem" }}>
        <Illumination size={80} letter="B" />
        <h2
          style={{
            fontFamily: "var(--font-cinzel-decorative), serif",
            fontSize: "28px",
            color: "#3D1308",
            margin: "1.5rem 0 0.5rem",
            fontWeight: 400,
          }}
        >
          The Bonaventure Opera Omnia
        </h2>
        <p
          style={{
            fontFamily: "var(--font-cinzel), serif",
            fontSize: "14px",
            letterSpacing: "0.15em",
            color: "#8B6914",
            textTransform: "uppercase",
          }}
        >
          A New English Translation
        </p>
        <CrossDivider />
        {/* Prose slot: placeholder until the commissioned text arrives (site-copy.tsx). */}
        <HomeIntro />
      </div>

      <FleuronDivider />

      <div className="section-title">Published Volumes</div>
      {browseEntries(books).map((entry) => {
        // A multi-work tome is one row; its counts are the sum of its works.
        const group = entry.kind === "tome" ? entry.works : [entry.book];
        const translated = group.reduce(
          (sum, b) =>
            sum +
            b.distinctions.reduce(
              (s, d) => s + d.questions.filter((q) => q.hasTranslation).length,
              0
            ),
          0
        );
        const total = group.reduce(
          (sum, b) => sum + b.distinctions.reduce((s, d) => s + d.questions.length, 0),
          0
        );
        const { href, key, letter, title, count } =
          entry.kind === "book"
            ? {
                href: entry.book.path,
                key: `b${entry.book.id}`,
                letter: entry.book.initial ?? `${entry.book.id}`,
                title: entry.book.title,
                count: divisionCountLabel(entry.book),
              }
            : {
                href: tomePath(entry.tome),
                key: `t${entry.tome}`,
                letter: entry.initial,
                title: entry.title,
                count: `${entry.works.length} work${entry.works.length !== 1 ? "s" : ""}`,
              };

        return (
          <Link key={key} href={href} className="card-link">
            <div className="card">
              <div style={{ display: "flex", alignItems: "flex-start", gap: "1rem" }}>
                <Illumination size={44} letter={letter} />
                <div>
                  <h3 className="card-title">{title}</h3>
                  <p className="card-meta">
                    {count} &middot; {translated} of {total} questions translated
                  </p>
                </div>
              </div>
            </div>
          </Link>
        );
      })}

      <FleuronDivider />

      <div className="section-title">The Full Opera Omnia &mdash; Project Scope</div>
      <p className="body-text" style={{ marginBottom: "1.5rem" }}>
        The Quaracchi <em>Opera Omnia</em>&thinsp; runs to ten volumes (1882&ndash;1902). Volumes I
        through IX hold the texts; Volume X is the edition&rsquo;s index volume, and its place is
        taken here by indices generated from the translation itself. See{" "}
        <Link href="/progress">Progress</Link> for page counts.
      </p>
      {scopeRows(
        new Map(books.filter((b) => b.tome === undefined).map((b) => [b.id, b.path])),
        new Set(books.filter((b) => b.tome !== undefined).map((b) => b.tome as number))
      ).map((t) => {
        const row = (
          <div className={`scope-row scope-${t.status}`}>
            <span className="scope-num">{t.tome}</span>
            <div className="scope-body">
              <span className="scope-title">
                {t.title} <span className="scope-year">&middot; {t.year}</span>
              </span>
              <span className="scope-gloss">{t.gloss}</span>
              {t.pending.length > 0 && (
                <span className="scope-gloss">
                  Still in progress:{" "}
                  {t.pending.map((w, i) => (
                    <span key={w.slug}>
                      {i > 0 ? ", " : ""}
                      <em>{w.title}</em>
                    </span>
                  ))}
                </span>
              )}
            </div>
            <span className="scope-status">{SCOPE_LABEL[t.status]}</span>
          </div>
        );
        return t.href ? (
          <Link key={t.tome} href={t.href} className="card-link scope-link">
            {row}
          </Link>
        ) : (
          <div key={t.tome}>{row}</div>
        );
      })}

      <FleuronDivider />

      <div className="card" style={{ cursor: "default", background: "rgba(61,19,8,0.04)" }}>
        <div className="section-title">About this Project</div>
        <p className="body-text">
          Bonaventure of Bagnoregio (1221&ndash;1274), the Seraphic Doctor, composed his{" "}
          <em>Commentary on the Sentences</em>&thinsp; while teaching at the University of Paris. It remains
          one of the most important works of medieval theology, yet no complete English translation
          has ever been published. This project seeks to remedy that gap.
        </p>
        <Link href="/about" className="back-link" style={{ marginTop: "1rem", display: "inline-block" }}>
          Read More &rarr;
        </Link>
      </div>
    </div>
  );
}
