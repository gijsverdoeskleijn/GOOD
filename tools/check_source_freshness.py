#!/usr/bin/env python3
"""Compare documented repository revisions with their configured refs."""

from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs" / "_data" / "sources.yml"


def remote_revision(url: str, ref: str) -> tuple[str | None, str | None]:
    environment = dict(os.environ)
    environment["GIT_TERMINAL_PROMPT"] = "0"
    result = subprocess.run(
        ["git", "ls-remote", url, f"refs/heads/{ref}"],
        text=True,
        capture_output=True,
        check=False,
        timeout=60,
        env=environment,
    )
    if result.returncode != 0:
        return None, result.stderr.strip() or "git ls-remote failed"
    fields = result.stdout.split()
    if not fields:
        return None, f"ref {ref!r} was not found"
    return fields[0], None


def inspect(source: dict[str, Any]) -> dict[str, str]:
    result = {
        "id": str(source.get("id", "unknown")),
        "status": "skipped",
        "documented": str(source.get("documented_revision") or "—"),
        "current": "—",
        "detail": "monitoring disabled",
    }
    if not source.get("enabled") or not source.get("monitor"):
        return result
    if not source.get("url"):
        result.update(status="configuration-error", detail="repository URL is missing")
        return result
    current, error = remote_revision(str(source["url"]), str(source.get("ref", "main")))
    if error:
        result.update(status="check-error", detail=error)
        return result
    result["current"] = current or "—"
    documented = source.get("documented_revision")
    if not documented:
        result.update(status="unbaselined", detail="documented revision is missing")
    elif current == documented:
        result.update(status="current", detail="registered revision matches remote ref")
    else:
        result.update(status="drift", detail="remote ref changed; documentation review required")
    return result


def report(results: list[dict[str, str]]) -> str:
    lines = [
        "# GOOD documentation source-freshness report",
        "",
        "| Source | Status | Documented revision | Current revision | Detail |",
        "|---|---|---|---|---|",
    ]
    for item in results:
        lines.append(
            f"| {item['id']} | {item['status']} | {item['documented'][:12]} | "
            f"{item['current'][:12]} | {item['detail'].replace('|', '/')} |"
        )
    lines.extend(
        [
            "",
            "A drift result is evidence for review, not permission to modify or publish content.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    results = [inspect(source) for source in registry.get("sources", [])]
    output = report(results)
    print(output)
    if args.report:
        path = args.report if args.report.is_absolute() else ROOT / args.report
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(output, encoding="utf-8")
    return int(any(item["status"] in {"drift", "unbaselined", "configuration-error", "check-error"} for item in results))


if __name__ == "__main__":
    raise SystemExit(main())

