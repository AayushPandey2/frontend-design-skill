# Verification, Severity, Self-Correction & Degradation

**Load when**: Classifying defects, running bounded self-correction, enforcing quality gates, deciding when to stop, or handling unavailable tools.

## 1. Verification Contract & Evidence Hierarchy

Workflow: `Understand -> Implement -> Render -> Inspect -> Critique -> Prioritize -> Correct -> Reverify -> Deliver` (compress for localized `QUICK` edits).

Match every claim to its evidence level—never present lower-level checks as higher-level proof:
- **Level 0 — Unsupported assumption**: No evidence; never report as verified.
- **Level 1 — Static inspection**: Source/CSS/token review; cannot establish rendered quality.
- **Level 2 — Automated project checks**: Build, typecheck, lint, unit/integration tests, static a11y checks.
- **Level 3 — Rendered inspection**: Live browser rendering, screenshots, DOM/computed styles.
- **Level 4 — Behavioral verification**: Executing real navigation, forms, keyboard flows, states, and gestures.
- **Level 5 — Measured & independent evaluation**: Performance/a11y audits, regression comparisons, unanchored independent criticism.

## 2. Severity Classification & Root-Cause Remediation

| Severity | Meaning | Action |
| :--- | :--- | :--- |
| **BLOCKER** | App fails to start, primary flow broken, security/data-loss risk | Must resolve or report explicitly before delivery |
| **MAJOR** | Mobile clipping, keyboard trap/unlabeled control, broken interaction, unmet core req | Prioritize before cosmetic fixes |
| **MODERATE** | Weak hierarchy, token drift, layout imbalance, avoidable complexity | Fix when in scope and materially beneficial |
| **MINOR** | Slight spacing/alignment/secondary type polish | Fix only if cheap; never extend loop endlessly |
| **PREFERENCE** | Subjective aesthetic alternative with no defect | Do not modify code automatically |

- **Structured defect record** (temporary working note, not persisted to skill files): `ID | Category | Severity | Target | Evidence | Actual vs. Expected | Root Cause | Fix | Verify | Status`.
- **Root-cause fix**: Fix shared tokens, intrinsic sizing, semantics, or state ownership rather than stacking compensating patches. Verify regressions on affected flows/components without rerunning unrelated expensive suites.
- **Independent criticism** (optional on `PREMIUM`/`FLAGSHIP` when supported): Withhold the generator's self-assessment to avoid anchoring; never claim independent review when the same agent generated and critiqued.

## 3. Mandatory Quality Gates, Budgets & Stopping Conditions

- **9 Gates**: Requirement, Functional, Accessibility, Responsive, Design, Engineering, Security, Economy, Evidence. Failed critical gates cannot be offset by aesthetic or token-economy scores; unverified gates must be marked unverified.
- **Default refinement budgets**: `QUICK`: targeted fix/verify only; `STANDARD`: <=2 passes; `PREMIUM`: <=3 passes; `FLAGSHIP`: <=5 passes.
- **Stop when**: Requirements, functional/a11y/security gates, and needed rendered checks pass; no critical regressions remain; and further edits yield diminishing returns. Never ship knowingly broken critical behavior just because a budget expired.

## 4. Verification Economy & Graceful Degradation

- **Economy**: Avoid duplicate screenshots of unchanged states, re-reading unchanged files, or repeating identical passing commands.
- **Degradation**: When browser tools, screenshots, test runners, or telemetry are unavailable, use the best static/build alternative, state unverified dimensions explicitly, and never fabricate screenshots, FPS, or test passes.
