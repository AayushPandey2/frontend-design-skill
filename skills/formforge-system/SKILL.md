---
name: formforge-system
description: FORMFORGE design system creation, extraction, and improvement. Use when invoked via /formforge-system for design tokens, typography roles, semantic colors, and component variants.
license: MIT
---

# /formforge-system

## Purpose & Scope

Create, extract, or improve reusable design systems—tokens, typography roles, semantic colors, spacing conventions, component variants, and interaction patterns.

## Activation Criteria & Boundaries

Use when standardizing UI across pages, extracting tokens from existing code, or eliminating ad-hoc styling drift. Coordinates well with `/formforge-dna`. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Inspect existing stylesheets, theme configs, and component primitives (`project-and-memory.md`).
2. Define or normalize semantic color tokens, typography scale/roles, spacing rhythm, and surface/elevation rules.
3. Implement reusable component variants and accessible state contracts (`ux-and-systems.md`, `components-and-frameworks.md`).
4. Verify token consistency, contrast compliance, and zero broken existing consumers.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [ux-and-systems.md](../../references/ux-and-systems.md)
- [color-and-surfaces.md](../../references/color-and-surfaces.md)
- [typography-and-content.md](../../references/typography-and-content.md)
- [components-and-frameworks.md](../../references/components-and-frameworks.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Cohesive, reusable design tokens and component variants aligned with the project's stack and accessibility floor.
