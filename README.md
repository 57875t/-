# QR Desk

**An auditable, human-in-the-loop AI workspace for quantitative research and multi-agent engineering workflows.**

QR Desk is an independent open-source project exploring how AI agents can support market-data research, simulation, calibration, code review, quality assurance, and structured delivery without taking control of real accounts or real funds.

> **Core boundary:** AI may analyze, simulate, calibrate, test, explain, and recommend review steps. A human remains responsible for every real-world decision and action.

## Why QR Desk exists

General-purpose AI chat tools are flexible but often lack reproducible workflows, explicit evidence, failure handling, and audit trails. Traditional quantitative platforms can be difficult to inspect or extend. QR Desk explores the space between them through:

- multi-agent routing and orchestration;
- real-versus-simulated data separation;
- evidence and provenance tracking;
- preview, execution, review, nitpick, and acceptance stages;
- boundary checks and secret redaction;
- report-quality evaluation;
- human approval before consequential actions.

## Current public baseline

The public bundle contains curated milestone builds from **v1.0 through v1.9**, an evidence-production **v2.0** build, and the current **v2.4** rollback/candidate builds.

The historical sequence intentionally skips **v1.4** because no distinct accepted v1.4 artifact exists in the preserved project files. The repository does not invent a missing release.

Because the original prototypes are large self-contained HTML applications, the preserved source bundle is stored as split Base64 parts under `bundles/`. Reconstruct it with:

```bash
python tools/reconstruct_bundle.py
```

The command creates `dist/qr-desk-public-source-bundle.zip`. Extract the archive and open any HTML milestone locally in a browser.

## Repository layout

```text
.
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── MANIFEST.md
├── bundles/
│   ├── README.md
│   └── qr-desk-public-source.zip.b64.part01 ...
├── docs/
│   ├── ARCHITECTURE.md
│   └── OPEN_SOURCE_SCOPE.md
└── tools/
    └── reconstruct_bundle.py
```

## Safety and scope

QR Desk is **not** an autonomous trading bot and does not provide guaranteed investment outcomes. The public project must not contain:

- brokerage credentials or real account access;
- API keys, tokens, passwords, or private keys;
- private trading strategies or production parameters;
- licensed datasets that cannot legally be redistributed;
- automatic order execution or real-fund control.

The preserved public bundle has been scanned and sanitized for obvious personal identifiers and credential-like demo strings. Placeholder credentials are not authentication mechanisms.

## Development priorities

1. Convert the self-contained prototype into maintainable modules.
2. Add reproducible tests for abnormal input, missing data, API failure, recovery, boundary values, and user mistakes.
3. Evaluate report accuracy, completeness, consistency, explainability, and actionability.
4. Improve contributor documentation and public issue-driven development.
5. Keep AI assistance transparent and subject to human review.

## Status

QR Desk is an early-stage engineering project transitioning from rapid private prototyping to a documented public codebase. Historical builds are preserved for reproducibility; they are not all production-ready.

## License

Licensed under the Apache License 2.0. See [`LICENSE`](LICENSE).
