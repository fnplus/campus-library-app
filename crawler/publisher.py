from __future__ import annotations

import logging
from typing import Iterable, List, Sequence

import httpx

from .models import ResourceRecord

logger = logging.getLogger(__name__)


class ResourcePublisher:
    def publish(self, resources: Sequence[ResourceRecord]) -> None:  # pragma: no cover - interface
        raise NotImplementedError


class HttpPublisher(ResourcePublisher):
    """Posts discovered resources to the CampusLibrary API."""

    def __init__(self, api_base: str, *, dry_run: bool = False, timeout: float = 5.0) -> None:
        self._api_base = api_base.rstrip("/")
        self._dry_run = dry_run
        self._timeout = timeout

    def publish(self, resources: Sequence[ResourceRecord]) -> None:
        if not resources:
            logger.info("No resources to publish")
            return

        if self._dry_run:
            logger.info("Dry-run mode: would publish %d resources", len(resources))
            for resource in resources:
                logger.info("Resource: %s (%s)", resource.title, resource.peer_location)
            return

        with httpx.Client(timeout=self._timeout) as client:
            for resource in resources:
                payload = resource.to_payload()
                response = client.post(f"{self._api_base}/resources/", json=payload)
                try:
                    response.raise_for_status()
                except httpx.HTTPStatusError as exc:  # pragma: no cover - network edge
                    logger.error("Failed to publish %s: %s", resource.title, exc)
                else:
                    logger.info("Published resource '%s'", resource.title)


class InMemoryPublisher(ResourcePublisher):
    """Collects resources for tests and offline debugging."""

    def __init__(self) -> None:
        self._storage: List[ResourceRecord] = []

    @property
    def storage(self) -> List[ResourceRecord]:
        return self._storage

    def publish(self, resources: Sequence[ResourceRecord]) -> None:
        self._storage.extend(resources)
