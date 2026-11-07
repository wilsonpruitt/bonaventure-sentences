import Link from "next/link";
import { CrossDivider } from "@/components/decorations";
import { authorityToc, loadAuthor, locusLabel, UNASSIGNED, type AuthLocus } from "@/lib/authorities";

export function generateStaticParams() {
  return authorityToc().flatMap((a) => a.works.map((w) => ({ author: a.id, work: w.id })));
}

export async function generateMetadata({ params }: { params: Promise<{ author: string; work: string }> }) {
  const { author, work } = await params;
  const a = loadAuthor(author);
  const w = a?.works.find((x) => x.id === work);
  const name = w && w.id !== UNASSIGNED ? w.la : "Unidentified work";
  return { title: a ? `${a.en}, ${name} — Index of Authorities — Bonaventure` : "Index of Authorities" };
}

function LocusCard({ l }: { l: AuthLocus }) {
  return (
    <Link href={l.url} className="card card-link">
      <div className="card-title">
        <span className="apparatus-num">{locusLabel(l)}</span> {l.title}
      </div>
      <div className="card-meta">
        {l.work} · {l.division}
        {l.named && (
          <>
            {" · "}
            <span title="Bonaventure names the author in his text; the footnote gives the locus.">
              named in the text
            </span>
          </>
        )}
        {l.inherited && (
          <>
            {" · "}
            <span title="Quaracchi prints loc. cit. here; the work is inherited from the preceding citation.">
              via <em>loc. cit.</em>
            </span>
          </>
        )}
        {l.pseudo && (
          <>
            {" · "}
            <span title="Attributed: the editors treat the work as not by this author.">attributed</span>
          </>
        )}
      </div>
    </Link>
  );
}

export default async function AuthorityWorkPage({
  params,
}: {
  params: Promise<{ author: string; work: string }>;
}) {
  const { author, work } = await params;
  const a = loadAuthor(author);
  const w = a?.works.find((x) => x.id === work);
  if (!a || !w) return <p>Work not found.</p>;

  const cited = w.loci.filter((l) => l.role === "cited");
  const same = w.loci.filter((l) => l.role === "same-passage");
  const title = w.id === UNASSIGNED ? "Unidentified work" : w.la;

  return (
    <div>
      <Link href={`/authorities/${a.id}`} className="back-link">
        &larr; {a.en}
      </Link>
      <h2 className="h2">
        {w.id === UNASSIGNED ? title : <em>{title}</em>}
      </h2>
      <p className="card-meta" style={{ marginTop: "-0.5rem" }}>
        {a.en} · {w.count} reference{w.count !== 1 ? "s" : ""}
        {w.pseudo && " · attributed"}
      </p>
      <CrossDivider />

      <p className="body-text">
        Loci are given as Quaracchi prints them, in the order of the work cited. Each entry opens
        the passage of Bonaventure at the footnote.
      </p>

      {cited.length > 0 && (
        <div className="dist-section">
          {same.length > 0 && <div className="section-title">Cited</div>}
          <div className="question-list">
            {cited.map((l, i) => (
              <LocusCard key={`${l.chunk}-${i}`} l={l} />
            ))}
          </div>
        </div>
      )}
      {same.length > 0 && (
        <div className="dist-section">
          <div className="section-title">On the same passage</div>
          <div className="question-list">
            {same.map((l, i) => (
              <LocusCard key={`s-${l.chunk}-${i}`} l={l} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
