#!/usr/bin/env python3
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from crawler.orchestrator import Crawler
from crawler.publisher import HttpPublisher


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="CampusLibrary LAN crawler")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("crawler/sample_peers.json"),
        help="Path to JSON manifest representing peer shares.",
    )
    parser.add_argument(
        "--api-base",
        default="http://localhost:8080/api",
        help="CampusLibrary API base URL.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not send data to the API, just log the discoveries.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Python logging level (DEBUG, INFO, WARNING, ...).",
    )
    return parser.parse_args(argv)


def configure_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(levelname)s %(name)s - %(message)s",
    )


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    configure_logging(args.log_level)

    publisher = HttpPublisher(args.api_base, dry_run=args.dry_run)
    crawler = Crawler(manifest_path=args.manifest, publisher=publisher)

    try:
        crawler.run()
    except Exception:  # pragma: no cover - convenience catch
        logging.exception("Crawler run failed")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
