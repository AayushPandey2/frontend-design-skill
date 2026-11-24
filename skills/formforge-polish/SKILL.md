---
name: formforge-polish
description: FORMFORGE visual hierarchy, typography, spacing, and surface refinement. Use when invoked via /formforge-polish to fix visual defects without breaking working functionality.
license: MIT
---

# /formforge-polish

## Purpose & Scope

Eliminate concrete visual defects—weak hierarchy, inconsistent spacing, awkward typography, muddy surfaces, or alignment drift—while preserving working functionality.

## Activation Criteria & Boundaries

Use when an interface works functionally but looks unfinished or visually inconsistent. Unlike `/formforge-redesign`, preserves existing layout structure and product architecture. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Critique the current UI (`visual-critique.md`) to pinpoint specific visual hierarchy, spacing, type, and surface defects.
2. Cross-check existing project tokens so refinements reinforce system consistency.
3. Apply targeted typography, color/surface, and spacing fixes without breaking logic or accessibility.
4. Re-inspect rendered output across desktop and mobile viewports to confirm visual improvement.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [visual-critique.md](../../references/visual-critique.md)
- [typography-and-content.md](../../references/typography-and-content.md)
- [color-and-surfaces.md](../../references/color-and-surfaces.md)
- [layout-and-responsive.md](../../references/layout-and-responsive.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Visually refined UI with specific defects resolved, intact behavior, and before/after verification summary.
