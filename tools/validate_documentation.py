#!/usr/bin/env python3
"""Validate page metadata and its references to registered sources."""

from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
DATA_DIR = DOCS_DIR / "_data"
REQUIRED = {
    "owner",
    "status",
    "access",
    "last_reviewed",
    "review_interval_days",
    "sources",
}
STATUSES = {"draft", "in-review", "approved", "deprecated"}
ACCESS_LEVELS = {"internal", "restricted", "public"}


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = yaml.safe_load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return value


def page_metadata(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML front matter")
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        raise ValueError("unterminated YAML front matter")
    metadata = yaml.safe_load(parts[1])
    if not isinstance(metadata, dict):
        raise ValueError("front matter must be a mapping")
    return metadata


def registered_source_ids() -> set[str]:
    ids: set[str] = set()
    for filename in ("sources.yml", "pdf-sources.yml"):
        registry = load_yaml(DATA_DIR / filename)
        for source in registry.get("sources", []):
            source_id = source.get("id")
            if source_id:
                if source_id in ids:
                    raise ValueError(f"duplicate source id: {source_id}")
                ids.add(source_id)
    return ids


def parse_date(value: Any) -> dt.date:
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    return dt.date.fromisoformat(str(value))


def validate_page(path: Path, source_ids: set[str]) -> list[str]:
    errors: list[str] = []
    try:
        metadata = page_metadata(path)
    except (ValueError, yaml.YAMLError) as exc:
        return [f"{path.relative_to(ROOT)}: {exc}"]

    missing = REQUIRED - metadata.keys()
    if missing:
        errors.append(f"missing metadata: {', '.join(sorted(missing))}")
    if metadata.get("status") not in STATUSES:
        errors.append(f"invalid status: {metadata.get('status')!r}")
    if metadata.get("access") not in ACCESS_LEVELS:
        errors.append(f"invalid access: {metadata.get('access')!r}")

    sources = metadata.get("sources")
    if not isinstance(sources, list):
        errors.append("sources must be a list")
    else:
        unknown = set(sources) - source_ids
        if unknown:
            errors.append(f"unknown source ids: {', '.join(sorted(unknown))}")

    try:
        last_reviewed = parse_date(metadata.get("last_reviewed"))
        interval = int(metadata.get("review_interval_days"))
        if interval < 1:
            raise ValueError("review interval must be positive")
        if dt.date.today() > last_reviewed + dt.timedelta(days=interval):
            errors.append(
                f"review overdue since {last_reviewed + dt.timedelta(days=interval)}"
            )
    except (TypeError, ValueError) as exc:
        errors.append(f"invalid review date or interval: {exc}")

    prefix = str(path.relative_to(ROOT))
    return [f"{prefix}: {error}" for error in errors]


def main() -> int:
    try:
        source_ids = registered_source_ids()
    except (ValueError, yaml.YAMLError) as exc:
        print(f"Registry error: {exc}")
        return 1

    pages = sorted(
        path
        for path in DOCS_DIR.rglob("*.md")
        if "_content" not in path.parts
    )
    errors = [error for page in pages for error in validate_page(page, source_ids)]
    if errors:
        print("Documentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(pages)} documentation pages and {len(source_ids)} sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

