from pathlib import Path

from crawler.orchestrator import Crawler
from crawler.publisher import InMemoryPublisher


def test_crawler_collects_and_publishes(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(
        """
        [
          {
            "name": "peer",
            "address": "192.168.0.4",
            "resources": [
              {
                "title": "Sample",
                "category": "books",
                "peer_location": "http://192.168.0.4/sample.pdf"
              }
            ]
          }
        ]
        """
    )

    publisher = InMemoryPublisher()
    crawler = Crawler(manifest_path=manifest_path, publisher=publisher)

    crawler.run()

    assert len(publisher.storage) == 1
    resource = publisher.storage[0]
    assert resource.title == "Sample"
    assert resource.category.value == "books"
