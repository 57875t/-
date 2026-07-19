#!/usr/bin/env python3
"""Extract the curated QR Desk public source bundle.

Expected input:
    bundles/qr-desk-public-source-bundle.tar.xz

Output:
    dist/qr-desk-public-source/
"""
from __future__ import annotations

import hashlib
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "bundles" / "qr-desk-public-source-bundle.tar.xz"
OUTPUT = ROOT / "dist" / "qr-desk-public-source"
EXPECTED_SHA256 = "db9cf432da98cfb5b7f02adbee4b8573690a5289c90edd0c1799d55b105b70c5"


def main() -> None:
    if not BUNDLE.exists():
        raise SystemExit(
            "Missing source bundle: " + str(BUNDLE) + "\n"
            "Place the prepared .tar.xz file in the bundles directory first."
        )

    digest = hashlib.sha256(BUNDLE.read_bytes()).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"SHA-256 mismatch. Expected {EXPECTED_SHA256}, got {digest}."
        )

    OUTPUT.mkdir(parents=True, exist_ok=True)
    with tarfile.open(BUNDLE, mode="r:xz") as archive:
        archive.extractall(OUTPUT, filter="data")

    print(f"Extracted QR Desk source to: {OUTPUT}")


if __name__ == "__main__":
    main()
