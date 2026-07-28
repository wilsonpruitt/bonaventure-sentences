import Link from "next/link";
import { notFound } from "next/navigation";
import { loadAllContent, tomeGroups, divisionCountLabel } from "@/lib/content";
import { Illumination, CrossDivider } from "@/components/decorations";

export function generateStaticParams() {
  return tomeGroups(loadAllContent()).map((t) => ({ tomeId: `${t.tome}` }));
}

export default async function TomePage({
  params,
}: {
  params: Promise<{ tomeId: string }>;
}) {
  const { tomeId } = await params;
  const tome = tomeGroups(loadAllContent()).find((t) => `${t.tome}` === tomeId);
  if (!tome) notFound();

  return (
    <div>
      <Link href="/browse" className="back-link">
        &larr; All Books
      </Link>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "1rem",
          marginBottom: "1rem",
        }}
      >
        <Illumination size={50} letter={tome.initial} />
        <h2 className="h2">{tome.title}</h2>
      </div>
      <CrossDivider />
      <div className="section-title">Works</div>
      {tome.works.map((work) => (
        <Link key={work.id} href={`/browse/${work.id}`} className="card-link">
          <div className="card">
            <div style={{ display: "flex", alignItems: "flex-start", gap: "1rem" }}>
              <Illumination size={44} letter={work.initial ?? `${work.id}`} />
              <div>
                <h3 className="card-title">{work.title}</h3>
                <p className="card-meta">{divisionCountLabel(work)}</p>
              </div>
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
}
