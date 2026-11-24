---
name: formforge-verify
description: FORMFORGE functional and technical implementation verification. Use when invoked via /formforge-verify to test user journeys, responsiveness, accessibility, and build health.
license: MIT
---

# /formforge-verify

## Purpose & Scope

Verify required functionality, interactive states, responsiveness, accessibility, build health, and technical acceptance criteria—strictly distinguishing verified behavior from assumptions.

## Activation Criteria & Boundaries

Use after implementation to validate technical correctness and QA gates. Unlike `/formforge-fidelity` (creative/design-contract agreement), Verify focuses on functional and technical acceptance. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Review technical acceptance criteria, user journeys, and edge/error/empty states (`functional-and-technical-audits.md`).
2. Run available build, typecheck, lint, test, and browser verification tools (`verification-and-refinement.md`).
3. Check console/runtime errors, keyboard/focus flows, responsive viewports, and security/XSS hygiene.
4. Report pass/fail evidence per check, explicitly listing anything unverified due to missing tools; fix only if authorized.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [functional-and-technical-audits.md](../../references/functional-and-technical-audits.md)
- [verification-and-refinement.md](../../references/verification-and-refinement.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Evidence-backed technical verification report separating observed results from unverified checks.
