# CampusLibrary Crawler

Prototype crawler that ingests peer manifests and publishes resources to the CampusLibrary API.

## Running the Crawler

```bash
python crawl.py --dry-run
```

- `--manifest`: path to a JSON manifest describing peers (defaults to `crawler/sample_peers.json`).
- `--api-base`: API base URL (defaults to `http://localhost:8080/api`).
- `--dry-run`: log discovered resources without sending them to the API.

With the backend running locally:

```bash
python crawl.py --api-base http://localhost:8080/api
```

## Manifest Format

```json
[
  {
    "name": "peer-id",
    "address": "192.168.0.10",
    "resources": [
      {
        "title": "Example resource",
        "description": "Optional summary",
        "category": "books",
        "tags": ["tag1", "tag2"],
        "peer_location": "http://192.168.0.10:9000/example.pdf"
      }
    ]
  }
]
```

This file stands in for real LAN discovery while the crawler is under development.

## Tests

```bash
pytest crawler/tests
```
