# Verification, Bounded Refinement & Graceful Degradation

## 1. Risk-Based Adaptive Verification

Scale verification effort to task risk, not diff size:
- **Low-risk localized edits**: Targeted build/typecheck/lint + inspect changed behavior.
- **Interactive / state / auth / payment changes**: Verify all affected user flows, edge states, and keyboard/error handling.
- **Visual / layout / responsive changes**: Inspect actual rendered output across desktop and mobile viewports when rendering tools are available.

## 2. Bounded Refinement Loop

Trigger refinement only on concrete defects: functional failures, a11y violations, responsive breakage, weak hierarchy, design-token drift, broken interactions, perf regressions, or unmet requirements. Never redesign satisfactory output merely because another aesthetic exists.

### Defect Fix Procedure
1. Identify defect and severity (critical functional/a11y/security issues before cosmetic polish).
2. Diagnose root cause (avoid stacking patches).
3. Apply focused fix.
4. Re-verify affected behavior.

### Default Refinement Budgets
- `QUICK`: Targeted fix and verification only.
- `STANDARD`: Up to 2 refinement passes.
- `PREMIUM`: Up to 3 refinement passes.
- `FLAGSHIP`: Up to 5 refinement passes when justified.

## 3. Stopping Conditions

Stop refining when:
- Explicit requirements, functional checks, a11y/security gates, and relevant responsive/visual checks pass.
- No known critical regression remains and further passes yield diminishing returns.
- Never chase an arbitrary 100/100 score; conversely, never ship a knowingly broken critical flow just because a pass budget was reached.

## 4. Graceful Capability Degradation

| Unavailable Capability | Fallback Behavior | Reporting Requirement |
| :--- | :--- | :--- |
| Browser / screenshots | Inspect DOM/CSS/layout logic statically; run build/unit tests if available | State clearly that visual rendering was not inspected |
| Planned Level 2/3 reference | Rely on Level 1 kernel + existing project conventions | Note capability gap without inventing guidance |
| Test runner / dev server | Run typecheck/syntax checks if available; trace logic carefully | Report exact commands run and what could not execute |
| Token telemetry | Report estimated instruction tokens (e.g., word-based estimate) | Label estimates explicitly; never present as measured |

Static code inspection must never be reported as browser verification.
