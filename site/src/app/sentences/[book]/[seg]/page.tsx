import { notFound } from "next/navigation";
import { loadAllContent, findChunk, allChunks } from "@/lib/content";
import { DivisionView } from "@/components/division-view";
import { ChunkView, chunkMetadata } from "@/components/chunk-view";

// /sentences/{book}/{seg}: either a distinction (`d3`) or a division-0 chunk
// (`proem`, `littera`, `capitula`…). The address module guarantees the two
// never collide: a division-0 unit may not look like `dN`.
export const dynamicParams = false;

export function generateStaticParams() {
  const books = loadAllContent().filter((b) => b.slug === "sentences");
  const dists = books.flatMap((b) =>
    b.distinctions.filter((d) => d.id !== 0).map((d) => ({ book: String(b.id), seg: `d${d.id}` }))
  );
  const front = allChunks(books)
    .filter((st) => st.dist.id === 0)
    .map((st) => ({ book: String(st.book.id), seg: st.q.path.split("/")[3] }));
  return [...dists, ...front];
}

function resolve(book: string, seg: string) {
  const books = loadAllContent();
  const path = `/sentences/${book}/${seg}`;
  const b = books.find((x) => x.path === `/sentences/${book}`);
  const dist = b?.distinctions.find((d) => d.path === path);
  if (b && dist) return { kind: "division" as const, book: b, dist };
  const stop = findChunk(books, path);
  return stop ? { kind: "chunk" as const, stop } : null;
}

export async function generateMetadata({ params }: { params: Promise<{ book: string; seg: string }> }) {
  const { book, seg } = await params;
  const r = resolve(book, seg);
  if (!r) return {};
  if (r.kind === "chunk") return chunkMetadata(r.stop);
  return {
    title: `${r.book.title} · ${r.dist.title}`,
    alternates: { canonical: `https://bonaventure.wrootpress.com${r.dist.path}` },
  };
}

export default async function Page({ params }: { params: Promise<{ book: string; seg: string }> }) {
  const { book, seg } = await params;
  const r = resolve(book, seg);
  if (!r) notFound();
  return r.kind === "chunk" ? <ChunkView stop={r.stop} /> : <DivisionView book={r.book} dist={r.dist} />;
}
