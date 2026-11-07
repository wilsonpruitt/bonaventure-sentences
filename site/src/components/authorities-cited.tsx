import Link from "next/link";
import { authoritiesInChunk, authorityToc, UNASSIGNED } from "@/lib/authorities";

/** "Authorities cited here": each author and work this text cites, linked to its
 *  page in the Index of Authorities. Server-rendered; the data never reaches the
 *  client bundle. */
export function AuthoritiesCited({ chunkId }: { chunkId: string }) {
  const items = authoritiesInChunk(chunkId);
  if (items.length === 0) return null;
  const toc = new Map(authorityToc().map((a) => [a.id, a]));

  // Group by author, keeping the per-chunk order (by English name).
  const groups: { id: string; en: string; works: { id: string; la: string; n: number }[] }[] = [];
  for (const [aid, wid, n] of items) {
    const a = toc.get(aid);
    if (!a) continue;
    let g = groups.find((x) => x.id === aid);
    if (!g) groups.push((g = { id: aid, en: a.en, works: [] }));
    const la = wid === UNASSIGNED ? "work not identified" : a.works.find((w) => w.id === wid)?.la ?? wid;
    g.works.push({ id: wid, la, n });
  }

  return (
    <section className="cite-this" aria-label="Authorities cited here">
      <div className="section-title" style={{ fontSize: "12px" }}>Authorities cited here</div>
      <p>
        {groups.map((g, gi) => (
          <span key={g.id}>
            {gi > 0 && " · "}
            <Link href={`/authorities/${g.id}`}>{g.en}</Link>
            {", "}
            {g.works.map((w, wi) => (
              <span key={w.id}>
                {wi > 0 && ", "}
                <Link href={`/authorities/${g.id}/${w.id}`}>
                  {w.id === UNASSIGNED ? w.la : <em>{w.la}</em>}
                </Link>
                {w.n > 1 && ` (${w.n})`}
              </span>
            ))}
          </span>
        ))}
      </p>
    </section>
  );
}
