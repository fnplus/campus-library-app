from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List

from .models import Category, PeerRecord, ResourceRecord


class ManifestLoaderError(RuntimeError):
    pass


class ManifestLoader:
    """Loads static peer/resource declarations from a JSON manifest.

    This acts as a stand-in for real LAN discovery while prototyping the crawler.
    """

    def __init__(self, manifest_path: Path) -> None:
        self._manifest_path = manifest_path

    def load(self) -> List[PeerRecord]:
        if not self._manifest_path.exists():
            raise ManifestLoaderError(f"Manifest file not found: {self._manifest_path}")

        try:
            raw = json.loads(self._manifest_path.read_text())
        except json.JSONDecodeError as exc:
            raise ManifestLoaderError(f"Invalid JSON in manifest: {exc}") from exc

        peers: List[PeerRecord] = []
        for entry in raw:
            peers.append(self._parse_peer(entry))
        return peers

    def _parse_peer(self, data: dict) -> PeerRecord:
        if "name" not in data or "address" not in data:
            raise ManifestLoaderError("Peer entry missing required 'name' or 'address' field")

        resources_data: Iterable[dict] = data.get("resources", [])
        resources: List[ResourceRecord] = []
        for resource in resources_data:
            resources.append(self._parse_resource(resource))

        return PeerRecord(name=data["name"], address=data["address"], resources=resources)

    def _parse_resource(self, data: dict) -> ResourceRecord:
        try:
            category = Category(data["category"])
        except KeyError as exc:
            raise ManifestLoaderError("Resource entry missing 'category' field") from exc
        except ValueError as exc:
            raise ManifestLoaderError(f"Unknown category value '{data.get('category')}'") from exc

        try:
            title = data["title"]
            peer_location = data["peer_location"]
        except KeyError as exc:
            raise ManifestLoaderError("Resource entry missing 'title' or 'peer_location'") from exc

        description = data.get("description")
        tags = data.get("tags", [])
        if not isinstance(tags, list):
            raise ManifestLoaderError("Resource 'tags' field must be a list of strings")

        return ResourceRecord(
            title=title,
            description=description,
            category=category,
            peer_location=peer_location,
            tags=tags,
        )
