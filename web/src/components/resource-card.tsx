import { Resource } from "@/types/resource";

interface ResourceCardProps {
  resource: Resource;
}

const categoryColors: Record<Resource["category"], string> = {
  books: "bg-emerald-100 text-emerald-800",
  media: "bg-indigo-100 text-indigo-800",
  notes: "bg-amber-100 text-amber-800",
  other: "bg-slate-100 text-slate-700",
  software: "bg-cyan-100 text-cyan-800",
};

export function ResourceCard({ resource }: ResourceCardProps) {
  const createdAt = new Date(resource.created_at).toLocaleString();

  return (
    <article className="flex h-full flex-col rounded-xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md">
      <header className="mb-4 flex items-start justify-between gap-3">
        <h3 className="text-lg font-semibold text-slate-900">
          {resource.title}
        </h3>
        <span
          className={`rounded-full px-3 py-1 text-xs font-medium uppercase tracking-wide ${categoryColors[resource.category]}`}
        >
          {resource.category}
        </span>
      </header>
      {resource.description ? (
        <p className="mb-4 flex-1 text-sm text-slate-600">
          {resource.description}
        </p>
      ) : (
        <p className="mb-4 flex-1 text-sm text-slate-400 italic">
          No description provided.
        </p>
      )}
      <dl className="mt-auto space-y-3 text-sm text-slate-500">
        <div>
          <dt className="font-medium text-slate-600">Access</dt>
          <dd>
            <a
              className="break-all text-indigo-600 hover:text-indigo-500"
              href={resource.peer_location}
              target="_blank"
              rel="noopener noreferrer"
            >
              {resource.peer_location}
            </a>
          </dd>
        </div>
        <div>
          <dt className="font-medium text-slate-600">Tags</dt>
          <dd className="flex flex-wrap gap-2">
            {resource.tags.length ? (
              resource.tags.map((tag) => (
                <span
                  key={tag}
                  className="rounded-full bg-slate-100 px-3 py-1 text-xs font-medium text-slate-600"
                >
                  {tag}
                </span>
              ))
            ) : (
              <span className="text-slate-400">No tags</span>
            )}
          </dd>
        </div>
        <div>
          <dt className="font-medium text-slate-600">Discovered</dt>
          <dd>{createdAt}</dd>
        </div>
      </dl>
    </article>
  );
}
