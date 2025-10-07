from __future__ import annotations

from datetime import datetime, timezone
from typing import Iterable, List

from .models import PeerRecord, ResourceRecord


class Indexer:
    """Transforms discovered peer listings into normalized records."""

    def collect(self, peers: Iterable[PeerRecord]) -> List[ResourceRecord]:
        collected: List[ResourceRecord] = []
        for peer in peers:
            for resource in peer.resources:
                # Stamp discovery time to help future deduplication strategies.
                resource.discovered_at = datetime.now(timezone.utc)
                collected.append(resource)
        return collected
