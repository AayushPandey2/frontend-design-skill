---
name: formforge-fidelity
description: FORMFORGE design-contract fidelity verification. Use when invoked via /formforge-fidelity to verify implementation against approved design specs, locked decisions, and visual references.
license: MIT
---

# /formforge-fidelity

## Purpose & Scope

Verify actual implementation against approved design specifications, locked decisions, `DESIGN.md`, and selected visual references using rendered browser evidence where available.

## Activation Criteria & Boundaries

Use after building from a `/formforge-plan` prompt, `/formforge-reference` spec, or locked creative direction. Unlike `/formforge-verify` (technical/functional QA), Fidelity measures agreement with creative and design intent. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Load the approved design contract (master prompt, `DESIGN.md`, locked choices, or reference spec) and inspect rendered UI (`design-fidelity.md`).
2. Audit all 10 contract dimensions (specs, locked decisions, references, typography, color, layout, components, motion, responsive, functional contract).
3. Classify deviations by severity (missing requirement, incorrect implementation, unapproved visual change/drift, responsive/motion discrepancy).
4. Report findings first; apply targeted corrections only when authorized, then reverify without introducing subjective redesigns.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [design-fidelity.md](../../references/design-fidelity.md)
- [visual-critique.md](../../references/visual-critique.md)
- [verification-and-refinement.md](../../references/verification-and-refinement.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Severity-ranked design-contract fidelity report (plus verified targeted fixes only if authorized).
