#!/usr/bin/env python3
"""Render the human-readable source registry from the machine-readable files."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "docs" / "_data"
OUTPUT = ROOT / "docs" / "reference" / "source-registry.md"


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        data = yaml.safe_load(stream)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return data


def cell(value: Any) -> str:
    if value is None or value == "":
        return "—"
    if isinstance(value, bool):
        return "yes" if value else "no"
    return str(value).replace("|", "\\|").replace("\n", " ")


def link(label: str, url: str | None) -> str:
    return f"[{label}]({url})" if url else label


def main() -> None:
    repositories = load_yaml(DATA_DIR / "sources.yml")
    pdfs = load_yaml(DATA_DIR / "pdf-sources.yml")

    lines = [
        "---",
        "owner: GOOD documentation owner",
        "status: draft",
        "access: internal",
        "last_reviewed: '2026-08-31'",
        "review_interval_days: 90",
        "sources:",
        "  - good-docs",
        "---",
        "",
        "# Source registry",
        "",
        "This page is generated from `docs/_data/sources.yml` and "
        "`docs/_data/pdf-sources.yml`. Edit those files and run `make registry`.",
        "",
        "## Code and service repositories",
        "",
        "| Source | Provider | Ref | Documented revision | Access | Active | Owner |",
        "|---|---|---|---|---|---|---|",
    ]

    for source in repositories.get("sources", []):
        source_name = link(cell(source.get("name")), source.get("url"))
        revision = source.get("documented_revision")
        if revision:
            revision = str(revision)[:12]
        lines.append(
            "| "
            + " | ".join(
                [
                    source_name,
                    cell(source.get("provider")),
                    cell(source.get("ref")),
                    cell(revision),
                    cell(source.get("access")),
                    cell(source.get("enabled")),
                    cell(source.get("owner")),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Controlled PDF sources",
            "",
            f"Approved folder: {pdfs.get('drive_folder', 'not configured')}",
            "",
            "| Source | Revision | Access | Registration | Owner |",
            "|---|---|---|---|---|",
        ]
    )
    for source in pdfs.get("sources", []):
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(source.get("title")),
                    cell(source.get("revision")),
                    cell(source.get("access")),
                    cell(source.get("review_status")),
                    cell(source.get("owner")),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "```{note}",
            "A source is not eligible for automated ingestion until its owner, access "
            "classification, stable identifier, and baseline revision are present.",
            "```",
            "",
        ]
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()

