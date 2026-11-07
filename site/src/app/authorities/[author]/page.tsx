import Link from "next/link";
import { CrossDivider } from "@/components/decorations";
import { authorityToc, loadAuthor, UNASSIGNED } from "@/lib/authorities";

export function generateStaticParams() {
  return authorityToc().map((a) => ({ author: a.id }));
}

export async function generateMetadata({ params }: { params: Promise<{ author: string }> }) {
  const { author } = await params;
  const a = authorityToc().find((x) => x.id === author);
  return { title: a ? `${a.en} — Index of Authorities — Bonaventure` : "Index of Authorities — Bonaventure" };
}

export default async function AuthorPage({ params }: { params: Promise<{ author: string }> }) {
  const { author } = await params;
  const a = loadAuthor(author);
  if (!a) return <p>Author not found.</p>;

  const works = a.works.filter((w) => w.id !== UNASSIGNED);
  const cited = works.filter((w) => w.cited > 0);
  const same = works.filter((w) => w.samePassage > 0);
  const unassigned = a.works.find((w) => w.id === UNASSIGNED);

  const card = (w: (typeof works)[number], n: number) => (
    <Link key={w.id} href={`/authorities/${a.id}/${w.id}`} className="card card-link">
      <div className="card-title">
        <em>{w.la}</em>
        {w.pseudo && <span className="card-meta"> — attributed</span>}
      </div>
      <div className="card-meta">
        {n} reference{n !== 1 ? "s" : ""}
      </div>
    </Link>
  );

  return (
    <div>
      <Link href="/authorities" className="back-link">
        &larr; Index of Authorities
      </Link>
      <h2 className="h2">{a.en}</h2>
      <p className="card-meta" style={{ marginTop: "-0.5rem" }}>
        <span style={{ fontStyle: "italic" }}>{a.la}</span> · {a.count.toLocaleString()} reference
        {a.count !== 1 ? "s" : ""}
      </p>
      <CrossDivider />

      {cited.length > 0 && (
        <>
          <div className="section-title">Works cited</div>
          <div className="question-list">{cited.map((w) => card(w, w.cited))}</div>
        </>
      )}

      {same.length > 0 && (
        <>
          <div className="section-title">On the same passage</div>
          <p className="body-text">
            Places where the editors cite {a.en} on the same text Bonaventure is treating.
          </p>
          <div className="question-list">{same.map((w) => card(w, w.samePassage))}</div>
        </>
      )}

      {unassigned && (
        <>
          <div className="section-title">Work not identified</div>
          <p className="body-text">
            References that name {a.en} but no work the index can identify. They are listed, not
            guessed.
          </p>
          <div className="question-list">
            <Link href={`/authorities/${a.id}/${UNASSIGNED}`} className="card card-link">
              <div className="card-title">Unidentified work</div>
              <div className="card-meta">
                {unassigned.count} reference{unassigned.count !== 1 ? "s" : ""}
              </div>
            </Link>
          </div>
        </>
      )}
    </div>
  );
}
