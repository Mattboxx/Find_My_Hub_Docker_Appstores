#!/usr/bin/env python3
"""Validate the identity and release version of generated catalog Compose files."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


APP_ID = "io.github.mattbox03.findmyhub"
VERSIONED_SERVICES = ("web", "apple-provider", "google-provider")


def validate_compose(path: Path, expected_version: str) -> None:
    rendered = subprocess.run(
        ["docker", "compose", "-f", str(path), "config", "--format", "json"],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(rendered.stdout)
    metadata = payload.get("x-casaos", {})

    actual_id = metadata.get("id")
    if actual_id != APP_ID:
        raise ValueError(f"{path}: expected app id {APP_ID!r}, got {actual_id!r}")

    actual_version = str(metadata.get("version"))
    if actual_version != expected_version:
        raise ValueError(
            f"{path}: expected app version {expected_version!r}, got {actual_version!r}"
        )

    services = payload.get("services", {})
    for service in VERSIONED_SERVICES:
        image = services.get(service, {}).get("image", "")
        image_without_digest = image.split("@", 1)[0]
        actual_tag = image_without_digest.rsplit(":", 1)[-1]
        if actual_tag != expected_version:
            raise ValueError(
                f"{path}: expected {service} image tag {expected_version!r}, "
                f"got {image!r}"
            )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("expected_version")
    parser.add_argument("compose_files", nargs="+", type=Path)
    args = parser.parse_args()

    for compose_file in args.compose_files:
        if not compose_file.is_file() or compose_file.stat().st_size == 0:
            raise FileNotFoundError(f"missing or empty Compose file: {compose_file}")
        validate_compose(compose_file, args.expected_version)
        print(f"Validated {compose_file} at {args.expected_version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
