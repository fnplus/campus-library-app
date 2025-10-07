from __future__ import annotations

import logging
from pathlib import Path

from .indexer import Indexer
from .manifest_loader import ManifestLoader
from .publisher import ResourcePublisher

logger = logging.getLogger(__name__)


class Crawler:
    def __init__(
        self,
        *,
        manifest_path: Path,
        publisher: ResourcePublisher,
        indexer: Indexer | None = None,
    ) -> None:
        self._manifest_loader = ManifestLoader(manifest_path)
        self._publisher = publisher
        self._indexer = indexer or Indexer()

    def run(self) -> None:
        logger.info("Starting crawler session")
        peers = self._manifest_loader.load()
        logger.info("Loaded %d peers from manifest", len(peers))
        resources = self._indexer.collect(peers)
        logger.info("Collected %d resources", len(resources))
        self._publisher.publish(resources)
