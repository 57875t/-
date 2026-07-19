# Security Policy

## Supported scope

Security reports are welcomed for the current public QR Desk source bundle, reconstruction tooling, and future modular releases.

Historical milestone builds are preserved for reproducibility and may contain prototype-only patterns that should not be treated as production authentication or deployment designs.

## Reporting a vulnerability

Please open a GitHub issue **without including live credentials, personal data, brokerage information, private strategy parameters, or exploitable secret values**. Describe the affected version, reproduction steps, impact, and a safe proof of concept.

For a report that cannot be disclosed safely in a public issue, contact the maintainer through the private reporting option available on the repository once enabled.

## Credential handling

- Never commit API keys, tokens, passwords, private keys, cookies, or account credentials.
- Demo strings are placeholders and must not be reused as authentication secrets.
- Public builds should keep credentials in memory where possible and must redact them from logs, exports, reports, and backups.
- Client-side access gates are not security boundaries. Real authentication, quotas, and authorization require a backend.

## Financial safety boundary

QR Desk must not execute real orders, control real funds, or access brokerage accounts. Any future integration that could create real-world financial consequences requires a separate security review, explicit human approval, and a design that defaults to simulation or dry-run behavior.
