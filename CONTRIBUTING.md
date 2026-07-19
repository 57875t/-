# Contributing to QR Desk

Thanks for helping improve QR Desk. The project is moving from large self-contained prototypes toward a modular, testable, and contributor-friendly codebase.

## Good first contributions

- reproduce a bug in a preserved milestone build;
- improve setup or reconstruction documentation;
- extract a self-contained component without changing behavior;
- add tests for abnormal input, missing data, API failure, recovery, or user mistakes;
- improve accessibility, keyboard navigation, or responsive behavior;
- improve secret redaction and audit-log safety;
- document architecture decisions and known limitations.

## Contribution workflow

1. Open an issue describing the problem, user impact, and proposed acceptance criteria.
2. Create a focused branch and avoid unrelated visual or architectural changes.
3. Preserve the human-in-the-loop and no-real-trading boundaries.
4. Add or update tests and documentation.
5. Run secret scanning before submitting.
6. Open a pull request describing what changed, what did not change, risks, and verification evidence.

## Pull-request checklist

- [ ] No credentials, personal data, private strategy data, or licensed datasets were added.
- [ ] Real and simulated data remain clearly separated.
- [ ] The change does not execute trades or control real funds.
- [ ] Failure states are visible rather than silently replaced with fabricated success.
- [ ] Human review remains required for consequential actions.
- [ ] Tests or reproducible verification steps are included.
- [ ] Documentation and changelog entries are updated when appropriate.

## Design principles

- **Evidence before confidence.** Do not mark a result as verified without supporting data.
- **Degrade honestly.** Missing or blocked data should produce a degraded or failed state, not synthetic success presented as truth.
- **Audit the work, not the person.** Findings should identify observable defects and remediation steps.
- **Small, reviewable changes.** Prefer focused improvements over broad rewrites.
- **User control.** AI assists; humans approve and execute real-world actions.

## Licensing

By contributing, you agree that your contribution will be licensed under the Apache License 2.0.
