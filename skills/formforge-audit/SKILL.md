---
name: formforge-audit
description: FORMFORGE read-only comprehensive frontend inspection and critique. Use when invoked via /formforge-audit to review UI, accessibility, responsiveness, or functional bugs without editing files.
license: MIT
---

# /formforge-audit

## Purpose & Scope

STRICT READ-ONLY MODE: Perform a comprehensive, evidence-driven audit of visual hierarchy, functional journeys, responsiveness, accessibility, motion, performance, and code waste without modifying any files.

## Activation Criteria & Boundaries

Use for pre-launch reviews, codebase/UI diagnostics, or design-and-engineering health checks. Never edits files; hand off fixes to `/formforge-polish`, `/formforge-optimize`, or `/formforge-accessibility` only when requested. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Inspect target routes/components and render in a browser when available (or note static-only scope).
2. Audit visual craft (`visual-critique.md`) and functional, responsive, a11y, perf, and waste dimensions (`functional-and-technical-audits.md`).
3. Classify defects by severity (`Critical` -> `Major` -> `Minor`) with exact file/line or viewport evidence.
4. Present prioritized remediation recommendations without altering repository files.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [visual-critique.md](../../references/visual-critique.md)
- [functional-and-technical-audits.md](../../references/functional-and-technical-audits.md)
- [verification-and-refinement.md](../../references/verification-and-refinement.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Prioritized, evidence-backed audit report distinguishing verified observations from unverified checks—zero files modified.
