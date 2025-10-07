from __future__ import annotations

import itertools
from datetime import datetime, timezone
from typing import Dict, Iterable, List, Optional

from ..schemas import Resource, ResourceCreate


class ResourceService:
    """In-memory resource catalogue suitable for prototyping and tests."""

    def __init__(self) -> None:
        self._id_counter = itertools.count(start=1)
        self._resources: Dict[int, Resource] = {}

        # Seed with a couple of useful examples so the API has data immediately.
        self._seed_defaults()

    def _seed_defaults(self) -> None:
        defaults: Iterable[ResourceCreate] = [
            ResourceCreate(
                title="Linear Algebra Lecture Notes",
                description="Professor Chen's concise summary of key theorems and proofs.",
                category="notes",
                tags=["math201", "midterms"],
                peer_location="http://192.168.1.23:9000/linear-algebra-notes.pdf",
            ),
            ResourceCreate(
                title="Operating Systems: Three Easy Pieces",
                description="Open textbook (PDF) covering OS fundamentals.",
                category="books",
                tags=["cs301"],
                peer_location="http://192.168.1.42:8080/os-tep.pdf",
            ),
        ]

        for resource in defaults:
            self.add_resource(resource)

    def list_resources(
        self,
        *,
        category: Optional[str] = None,
        search: Optional[str] = None,
    ) -> List[Resource]:
        resources = list(self._resources.values())

        if category:
            category_lower = category.lower()
            resources = [r for r in resources if r.category.value == category_lower]

        if search:
            query = search.lower()
            resources = [
                r
                for r in resources
                if query in r.title.lower()
                or (r.description and query in r.description.lower())
                or any(query in tag.lower() for tag in r.tags)
            ]

        return resources

    def add_resource(self, payload: ResourceCreate) -> Resource:
        resource_id = next(self._id_counter)
        resource = Resource(
            id=resource_id,
            created_at=datetime.now(timezone.utc),
            **payload.model_dump(),
        )
        self._resources[resource_id] = resource
        return resource

    def get_resource(self, resource_id: int) -> Optional[Resource]:
        return self._resources.get(resource_id)

    def close(self) -> None:
        """Placeholder for future cleanup when we move to a DB-backed service."""
        return None


_SERVICE_SINGLETON: ResourceService | None = None


def get_resource_service() -> ResourceService:
    global _SERVICE_SINGLETON
    if _SERVICE_SINGLETON is None:
        _SERVICE_SINGLETON = ResourceService()
    return _SERVICE_SINGLETON
