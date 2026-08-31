#!/usr/bin/env python3
"""Write a reproducibility manifest for a documentation build."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import subprocess
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_value(*arguments: str) -> str | None:
    result = subprocess.run(
        ["git", *arguments], cwd=ROOT, text=True, capture_output=True, check=False
    )
    return result.stdout.strip() if result.returncode == 0 else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    registry_path = ROOT / "docs" / "_data" / "sources.yml"
    registry = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    documentation_files = sorted((ROOT / "docs").rglob("*.md"))
    combined = hashlib.sha256()
    for path in documentation_files:
        combined.update(path.relative_to(ROOT).as_posix().encode())
        combined.update(path.read_bytes())

    manifest = {
        "schema_version": 1,
        "built_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "profile": "developer",
        "repository_revision": git_value("rev-parse", "HEAD"),
        "repository_branch": git_value("branch", "--show-current"),
        "repository_dirty": bool(git_value("status", "--porcelain")),
        "documentation_sha256": combined.hexdigest(),
        "source_registry_sha256": digest(registry_path),
        "sources": [
            {
                "id": source.get("id"),
                "ref": source.get("ref"),
                "documented_revision": source.get("documented_revision"),
                "enabled": source.get("enabled"),
            }
            for source in registry.get("sources", [])
        ],
    }
    output = args.output if args.output.is_absolute() else ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

