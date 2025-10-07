export type Category =
  | "books"
  | "notes"
  | "media"
  | "software"
  | "other";

export interface Resource {
  id: number;
  title: string;
  description?: string | null;
  category: Category;
  tags: string[];
  peer_location: string;
  created_at: string;
}
