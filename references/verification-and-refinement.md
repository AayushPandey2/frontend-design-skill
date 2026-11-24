# Verification, Severity, Self-Correction & Degradation

## 1. Verification Contract & Evidence Hierarchy

Workflow: `Understand -> Implement -> Render -> Inspect -> Critique -> Prioritize -> Correct -> Reverify -> Deliver` (compress for `QUICK`). Match every claim to its evidence level:
- **L0 — Unsupported assumption**: Never report as verified.
- **L1 — Static inspection**: Code/CSS/token review; cannot establish rendered quality.
- **L2 — Automated checks**: Build, typecheck, lint, unit/integration tests, static a11y.
- **L3 — Rendered inspection**: Live browser rendering, screenshots, DOM/computed styles.
- **L4 — Behavioral verification**: Real navigation, forms, keyboard flows, states, gestures.
- **L5 — Measured & independent**: Perf/a11y audits, regression comparisons, unanchored independent critique.

## 2. Severity, Root-Cause Remediation & Independent Critique

| Severity | Meaning | Action |
| :--- | :--- | :--- |
| **BLOCKER** | Won't start, primary flow broken, security/data-loss risk | Resolve or report explicitly before delivery |
| **MAJOR** | Mobile clipping, keyboard trap/unlabeled control, broken interaction, unmet core req | Prioritize before cosmetic fixes |
| **MODERATE** | Weak hierarchy, token drift, layout imbalance, avoidable complexity | Fix when in scope and materially beneficial |
| **MINOR** | Slight spacing/alignment/secondary type polish | Fix only if cheap; never extend loop |
| **PREFERENCE** | Subjective aesthetic alternative with no defect | Do not edit code automatically |

- **Temporary defect record**: `ID | Category | Severity | Target | Evidence | Actual vs. Expected | Root Cause | Fix | Verify | Status` (do not persist to skill files).
- **Root-cause fix**: Fix shared tokens, intrinsic sizing, semantics, or state ownership rather than stacking patches; reverify affected flows.
- **Independent critique**: Optional on `PREMIUM`/`FLAGSHIP`; withhold generator's self-assessment to prevent anchoring; never claim independence if the same agent generated and critiqued.

## 3. Gates, Stopping Conditions, Economy & Degradation

- **9 Mandatory Gates**: Requirement, Functional, Accessibility, Responsive, Design, Engineering, Security, Economy, Evidence. Failed critical gates cannot be offset by aesthetic or token-economy scores.
- **Stop when**: Required gates and rendered checks pass, no critical regressions remain, and further edits yield diminishing returns. Never ship broken critical flows just because a pass budget expired.
- **Verification economy**: Run targeted checks for local edits and broader regression checks for shared/critical changes; avoid duplicate captures of unchanged states or rerunning identical passing commands.
- **Degradation**: When browser, screenshot, test, or telemetry tools are unavailable, use the best static/build alternative, state unverified dimensions explicitly, and never fabricate evidence.
