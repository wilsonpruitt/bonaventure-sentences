import { notFound } from "next/navigation";
import { loadAllContent, findChunk, allChunks } from "@/lib/content";
import { ChunkView, chunkMetadata } from "@/components/chunk-view";

// /sentences/{book}/d{N}/{unit}: a chunk of a distinction.
export const dynamicParams = false;

export function generateStaticParams() {
  return allChunks(loadAllContent())
    .filter((st) => st.book.slug === "sentences" && st.dist.id !== 0)
    .map((st) => {
      const [, , book, seg, unit] = st.q.path.split("/");
      return { book, seg, unit };
    });
}

type P = { params: Promise<{ book: string; seg: string; unit: string }> };

export async function generateMetadata({ params }: P) {
  const { book, seg, unit } = await params;
  return chunkMetadata(findChunk(loadAllContent(), `/sentences/${book}/${seg}/${unit}`));
}

export default async function Page({ params }: P) {
  const { book, seg, unit } = await params;
  const stop = findChunk(loadAllContent(), `/sentences/${book}/${seg}/${unit}`);
  if (!stop) notFound();
  return <ChunkView stop={stop} />;
}
