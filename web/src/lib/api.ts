import "server-only";

import { Resource } from "@/types/resource";

const DEFAULT_API_BASE = "http://localhost:8080/api";

interface FetchResourcesOptions {
  search?: string;
  category?: string;
}

const apiBase =
  process.env.API_BASE_URL ??
  process.env.NEXT_PUBLIC_API_BASE_URL ??
  DEFAULT_API_BASE;

const normalizedBase = apiBase.endsWith("/") ? apiBase : `${apiBase}/`;

export async function fetchResources(
  options: FetchResourcesOptions = {},
): Promise<Resource[]> {
  const url = new URL("resources/", normalizedBase);
  if (options.search) {
    url.searchParams.set("search", options.search);
  }
  if (options.category) {
    url.searchParams.set("category", options.category);
  }

  const response = await fetch(url.toString(), {
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error(`API error: ${response.status} ${response.statusText}`);
  }

  const data = (await response.json()) as Resource[];
  return data;
}
