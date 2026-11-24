---
name: formforge-standard
description: FORMFORGE STANDARD mode for ordinary frontend components and pages. Use when invoked via /formforge-standard for routine feature UI reusing existing design systems.
license: MIT
---

# /formforge-standard

## Purpose & Scope

Build or update ordinary frontend components, forms, tables, and pages while reusing the project's existing architecture and design system.

## Activation Criteria & Boundaries

Use for multi-file feature UI, interactive forms, data views, or routine component composition. Hand off to `/formforge-premium` only if bespoke brand direction is requested. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Inspect existing components, design tokens, and framework patterns (`project-and-memory.md`).
2. Load only task-relevant design, component, and accessibility references.
3. Implement reusing existing primitives, native HTML/CSS first, and clean state boundaries.
4. Verify functionality, responsive behavior, accessibility, and build health (<= 2 refinement passes).

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [routing-and-modes.md](../../references/routing-and-modes.md)
- [implementation-economy.md](../../references/implementation-economy.md)
- [components-and-frameworks.md](../../references/components-and-frameworks.md)
- [verification-and-refinement.md](../../references/verification-and-refinement.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Production-ready feature or component aligned with project conventions, plus verified functional/build/a11y checks.
