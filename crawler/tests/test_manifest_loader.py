import json
from pathlib import Path

import pytest

from crawler.manifest_loader import ManifestLoader, ManifestLoaderError


def test_manifest_loader_parses_manifest(tmp_path: Path) -> None:
    manifest_path = tmp_path / "peers.json"
    manifest_path.write_text(
        json.dumps(
            [
                {
                    "name": "peer-1",
                    "address": "192.168.0.2",
                    "resources": [
                        {
                            "title": "Example",
                            "description": "Sample file",
                            "category": "notes",
                            "peer_location": "http://192.168.0.2:9000/example.pdf",
                            "tags": ["tag1"],
                        }
                    ],
                }
            ]
        )
    )

    loader = ManifestLoader(manifest_path)
    peers = loader.load()
    assert len(peers) == 1
    peer = peers[0]
    assert peer.name == "peer-1"
    resources = list(peer.resources)
    assert len(resources) == 1
    resource = resources[0]
    assert resource.title == "Example"
    assert resource.category.value == "notes"


def test_manifest_loader_errors_for_missing_file(tmp_path: Path) -> None:
    manifest_path = tmp_path / "missing.json"
    loader = ManifestLoader(manifest_path)
    with pytest.raises(ManifestLoaderError):
        loader.load()
