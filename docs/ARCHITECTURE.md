# QR Desk Architecture

## System intent

QR Desk is a human-in-the-loop research and engineering workspace. It coordinates specialized AI-assisted stages while preserving evidence, exposing failures, and requiring human approval for consequential actions.

## Conceptual pipeline

```text
User request
  ↓
Intent and boundary classification
  ↓
Preview / planning
  ↓
Calibration and evidence collection
  ↓
Execution or simulation
  ↓
Nitpick / adversarial review
  ↓
Acceptance and human approval
  ↓
Report, patch, or non-consequential deliverable
```

## Agent responsibilities

- **Router / Controller:** classifies intent and selects the appropriate workflow.
- **Preview Agent:** restates the target, constraints, acceptance criteria, and missing information.
- **Calibration Agent:** compares evidence, reference data, and simulated output.
- **Execution Agent:** performs bounded analysis or produces reviewable artifacts.
- **Nitpick Agent:** actively searches for defects, contradictions, unsupported claims, and boundary violations.
- **Market/Data Agent:** handles market-data acquisition and labels provenance and degradation states.
- **Review / Acceptance:** verifies that the deliverable meets explicit criteria before release.

The preserved milestones use different combinations and names. This document describes the stable architectural direction rather than asserting that every historical prototype implements every component completely.

## Data truth model

QR Desk should distinguish at least four states:

1. **Verified real/reference data** — retrieved from an identified source and validated.
2. **Degraded reference data** — incomplete, delayed, blocked, or otherwise limited.
3. **Simulated data** — intentionally generated for testing, forecasting, or dry-run use.
4. **Unknown/failed** — insufficient evidence; the system must not invent a successful state.

Real and simulated data must never be silently merged or presented as equivalent.

## Safety boundary

The architecture excludes autonomous real trading, brokerage-account access, real-fund control, guaranteed returns, and hidden production changes. Consequential actions remain outside the agent runtime and require explicit human execution.

## Current technical state

The preserved project is primarily a sequence of large self-contained HTML prototypes. The next engineering phase is to extract modules for UI, state, runtime adapters, evidence records, audit events, redaction, tests, and provider interfaces while preserving observable behavior.
