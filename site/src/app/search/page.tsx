import { SearchClient } from "./search-client";

// Full-text search runs on Pagefind's index (built over out/ after `next
// build`; see the "build" script). Nothing is inlined into this page: the
// index is split and fetched on demand, so it scales to the whole corpus.
export default function SearchPage() {
  return <SearchClient />;
}
