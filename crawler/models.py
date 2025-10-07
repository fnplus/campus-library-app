from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Iterable, List


class Category(str, Enum):
    books = "books"
    notes = "notes"
    media = "media"
    software = "software"
    other = "other"


@dataclass(slots=True)
class ResourceRecord:
    title: str
    description: str | None
    category: Category
    peer_location: str
    tags: List[str] = field(default_factory=list)
    discovered_at: datetime | None = None

    def to_payload(self) -> dict:
        """Transform into the API payload shape."""
        return {
            "title": self.title,
            "description": self.description,
            "category": self.category.value,
            "peer_location": self.peer_location,
            "tags": self.tags,
        }


@dataclass(slots=True)
class PeerRecord:
    name: str
    address: str
    resources: Iterable[ResourceRecord]

