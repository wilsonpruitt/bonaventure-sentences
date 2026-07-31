import fs from "node:fs";
import path from "node:path";
import Link from "next/link";

export type Backlink = {
  chunk: string;
  url: string;
  title: string;
  work: string;
  division: string;
  raw: string;
  level: "chunk" | "page" | "unit";
  n: number;
  viaIbid: boolean;
};

// The crossref index is 2.65 MB and every one of ~1,990 question pages consults it,
// so it is read from disk ONCE at build time and cached — not imported, which would
// inline the whole thing into every page's payload.
let cache: Record<string, Backlink[]> | null = null;

function inboundFor(chunkId: string): Backlink[] {
  if (cache === null) {
    const file = path.join(process.cwd(), "src", "data", "index-crossref.json");
    if (!fs.existsSync(file)) {
      // FAIL LOUDLY. Falling back to an empty index would drop the panel from every
      // one of ~1,990 pages and the build would still report success — the exact
      // silent-omission failure this project keeps getting bitten by.
      throw new Error(
        "index-crossref.json is missing. Run `python3.11 tools/build-index-json.py` "
        + "before building (see CLAUDE.md § Build and deploy)."
      );
    }
    cache = JSON.parse(fs.readFileSync(file, "utf-8")).inbound as Record<string, Backlink[]>;
  }
  return cache[chunkId] ?? [];
}

const MAX_SHOWN = 25;

/** "Cited by" — the inbound half of the self-cross-reference index.
 *
 *  Rendered server-side from the derived index; it adds nothing to the client
 *  bundle and does not touch the reader or content.json.
 */
export function CitedBy({ chunkId }: { chunkId: string }) {
  const all = inboundFor(chunkId);
  if (all.length === 0) return null;

  // A citation naming this exact unit is a stronger claim than one naming a printed
  // page it shares, or the whole article it sits in. They are shown apart rather
  // than blended into one count.
  const exact = all.filter((b) => b.level === "chunk");
  const nearby = all.filter((b) => b.level !== "chunk");
  const shown = exact.slice(0, MAX_SHOWN);
  const hidden = exact.length - shown.length;

  return (
    <div className="notes-section" style={{ marginTop: "2.5rem" }}>
      <div className="section-title">Cited by</div>

      {exact.length > 0 ? (
        <>
          <p className="card-meta" style={{ marginBottom: "0.75rem" }}>
            {exact.length} place{exact.length !== 1 ? "s" : ""} in the{" "}
            <em>Opera Omnia</em> cite{exact.length === 1 ? "s" : ""} this question.
            Derived from Quaracchi&rsquo;s own apparatus, never tagged by hand.
          </p>
          <div className="question-list">
            {shown.map((b) => (
              <Link key={b.chunk} href={b.url} className="card card-link">
                <div className="card-title">{b.title}</div>
                <div className="card-meta">
                  {b.work} &middot; {b.division}
                  {b.n > 1 && <> &middot; {b.n}&times;</>}
                  {b.viaIbid && (
                    <>
                      {" "}
                      &middot;{" "}
                      <span title="Quaracchi prints ibid. here; the reference is inherited from the preceding citation.">
                        via <em>ibid.</em>
                      </span>
                    </>
                  )}
                </div>
                <div className="card-meta" style={{ fontStyle: "italic" }}>
                  {b.raw}
                </div>
              </Link>
            ))}
          </div>
          {hidden > 0 && (
            <p className="card-meta">and {hidden} more.</p>
          )}
        </>
      ) : null}

      {nearby.length > 0 && (
        <p className="card-meta" style={{ marginTop: exact.length ? "1rem" : 0 }}>
          {nearby.length} further reference{nearby.length !== 1 ? "s" : ""} address
          {nearby.length === 1 ? "es" : ""} the article or printed page this question
          belongs to, rather than the question itself.
        </p>
      )}
    </div>
  );
}
