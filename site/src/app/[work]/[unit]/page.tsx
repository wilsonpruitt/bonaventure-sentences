import { notFound } from "next/navigation";
import { loadAllContent, findChunk, allChunks } from "@/lib/content";
import { ChunkView, chunkMetadata } from "@/components/chunk-view";

// /{slug}/{unit}: a chunk of a work (Tome V onward).
export const dynamicParams = false;

export function generateStaticParams() {
  return allChunks(loadAllContent())
    .filter((st) => st.book.slug !== "sentences")
    .map((st) => {
      const [, work, unit] = st.q.path.split("/");
      return { work, unit };
    });
}

type P = { params: Promise<{ work: string; unit: string }> };

export async function generateMetadata({ params }: P) {
  const { work, unit } = await params;
  return chunkMetadata(findChunk(loadAllContent(), `/${work}/${unit}`));
}

export default async function Page({ params }: P) {
  const { work, unit } = await params;
  const stop = findChunk(loadAllContent(), `/${work}/${unit}`);
  if (!stop) notFound();
  return <ChunkView stop={stop} />;
}
