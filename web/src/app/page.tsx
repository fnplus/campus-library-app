import { ResourceGrid } from "@/components/resource-grid";
import { fetchResources } from "@/lib/api";
import type { Resource } from "@/types/resource";

const categories = [
  { value: "", label: "All categories" },
  { value: "books", label: "Books" },
  { value: "notes", label: "Notes" },
  { value: "media", label: "Media" },
  { value: "software", label: "Software" },
  { value: "other", label: "Other" },
];

interface PageProps {
  searchParams?: {
    q?: string;
    category?: string;
  };
}

export default async function Home({ searchParams }: PageProps) {
  const search = searchParams?.q ?? "";
  const category = searchParams?.category ?? "";

  let resources: Resource[] = [];
  let error: string | null = null;

  try {
    resources = await fetchResources({
      search: search || undefined,
      category: category || undefined,
    });
  } catch (err) {
    error =
      err instanceof Error
        ? err.message
        : "Unable to reach the CampusLibrary API.";
  }

  return (
    <div className="space-y-10">
      <section className="flex flex-col gap-4">
        <h1 className="text-3xl font-semibold text-slate-900">
          Browse shared campus resources
        </h1>
        <p className="max-w-3xl text-sm text-slate-600">
          Explore study material, media, and software shared by peers on your
          local network. Filters update via query parameters, so you can share
          search URLs with classmates.
        </p>
        <form className="flex flex-col gap-3 rounded-xl border border-slate-200 bg-white p-4 shadow-sm sm:flex-row sm:items-center sm:gap-4">
          <label className="flex-1 text-sm">
            <span className="block text-xs font-medium uppercase tracking-wide text-slate-400">
              Search keywords
            </span>
            <input
              className="mt-1 w-full rounded-lg border border-slate-200 px-3 py-2 text-sm shadow-inner focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-200"
              type="search"
              name="q"
              defaultValue={search}
              placeholder="Try 'operating systems' or 'math201'"
            />
          </label>
          <label className="text-sm">
            <span className="block text-xs font-medium uppercase tracking-wide text-slate-400">
              Category
            </span>
            <select
              className="mt-1 w-full rounded-lg border border-slate-200 px-3 py-2 text-sm shadow-inner focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-200"
              name="category"
              defaultValue={category}
            >
              {categories.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          </label>
          <button
            className="mt-2 rounded-lg bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-200 sm:mt-6"
            type="submit"
          >
            Apply
          </button>
        </form>
        <p className="text-xs text-slate-400">
          Tip: Run the crawler (`python crawl.py`) to ingest fresh peer
          manifests into the backend.
        </p>
      </section>

      {error ? (
        <div className="rounded-xl border border-rose-200 bg-rose-50 p-6 text-rose-600">
          {error}
        </div>
      ) : (
        <ResourceGrid resources={resources} />
      )}
    </div>
  );
}
