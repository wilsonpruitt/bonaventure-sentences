import type { MetadataRoute } from "next";
import { loadAllContent, tomeGroups } from "@/lib/content";
import toc from "@/data/index-scripture-toc.json";

const BASE = "https://bonaventure.wrootpress.com";

// Mirrors the generateStaticParams of every route so the sitemap and the
// exported pages cannot drift apart.
export const dynamic = "force-static";

export default function sitemap(): MetadataRoute.Sitemap {
  const urls: string[] = ["/", "/about", "/browse", "/scripture", "/search", "/rights"];

  const books = loadAllContent();

  for (const tome of tomeGroups(books)) {
    urls.push(`/browse/tome/${tome.tome}`);
  }

  for (const book of books) {
    urls.push(`/browse/${book.id}`);
    for (const dist of book.distinctions) {
      urls.push(`/browse/${book.id}/d/${dist.id}`);
      for (const q of dist.questions) {
        urls.push(`/browse/${book.id}/d/${dist.id}/q/${encodeURIComponent(q.id)}`);
      }
    }
  }

  for (const b of toc.books as { slug: string }[]) {
    urls.push(`/scripture/${b.slug}`);
  }

  return urls.map((url) => ({ url: `${BASE}${url}` }));
}
