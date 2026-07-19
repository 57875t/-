# Source Bundle

Place the prepared file below in this directory:

```text
qr-desk-public-source-bundle.tar.xz
```

Verified SHA-256:

```text
db9cf432da98cfb5b7f02adbee4b8573690a5289c90edd0c1799d55b105b70c5
```

Then extract it from the repository root:

```bash
python tools/extract_bundle.py
```

The archive contains sanitized copies of the curated QR Desk milestone HTML files and a machine-readable `MANIFEST.json`.

The source bundle is intentionally compressed as a solid XZ archive because the historical self-contained HTML builds share substantial repeated code; solid compression reduces the public transfer package from more than 13 MB to roughly 341 KB.
