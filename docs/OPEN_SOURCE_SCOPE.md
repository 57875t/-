# Open-Source Scope

## Included

The public QR Desk project may include:

- user-interface and workspace code;
- multi-agent routing and orchestration patterns;
- preview, calibration, execution, nitpick, review, and acceptance workflows;
- data-provider adapter interfaces;
- simulation and dry-run logic;
- evidence, provenance, audit, and observability structures;
- secret-redaction and boundary-checking logic;
- reproducible test fixtures and synthetic sample data;
- documentation, issue templates, and contributor workflows.

## Excluded

The public repository must not include:

- real API keys, tokens, cookies, passwords, or private keys;
- brokerage credentials, account identifiers, or real-fund access;
- private or commercially sensitive trading strategies and parameters;
- paid or licensed datasets without redistribution rights;
- personal identity information and private server details;
- automatic order execution or code designed to bypass human approval;
- fabricated metrics, users, downloads, stars, dependencies, or project impact.

## Human-in-the-loop rule

AI systems may analyze, simulate, calibrate, test, explain, and generate reviewable code or reports. They must not independently execute real financial actions. A human remains responsible for approving and carrying out any real-world decision.

## Historical artifacts

Historical builds are included to show engineering progression. Their presence does not mean every prototype pattern is recommended. Candidate and rollback labels must remain visible. Client-side access gates are demonstrations, not security controls.

## Public claims

Project descriptions and applications should use verifiable facts only. QR Desk is currently an early-stage project transitioning from private prototyping to public maintenance; it should not claim large download numbers, external dependencies, or contributor counts until those exist.
