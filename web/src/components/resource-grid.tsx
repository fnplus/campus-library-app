import { Resource } from "@/types/resource";
import { ResourceCard } from "./resource-card";

interface ResourceGridProps {
  resources: Resource[];
}

export function ResourceGrid({ resources }: ResourceGridProps) {
  if (!resources.length) {
    return (
      <div className="rounded-xl border border-dashed border-slate-300 bg-slate-100/70 p-12 text-center text-slate-500">
        No resources discovered yet. Run the crawler or add shares on the LAN.
      </div>
    );
  }

  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
      {resources.map((resource) => (
        <ResourceCard key={resource.id} resource={resource} />
      ))}
    </div>
  );
}
