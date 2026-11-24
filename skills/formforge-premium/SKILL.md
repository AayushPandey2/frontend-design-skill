---
name: formforge-premium
description: FORMFORGE PREMIUM mode for high-craft UI/UX and product interfaces. Use when invoked via /formforge-premium for landing pages, dashboards, or bespoke product design.
license: MIT
---

# /formforge-premium

## Purpose & Scope

Deliver high-craft, distinctive product UI, marketing pages, and dashboards with strong creative direction, visual hierarchy, and bounded critique-refine loops.

## Activation Criteria & Boundaries

Use when brand expression, visual polish, and cohesive UX matter as much as clean engineering. Distinct from `/formforge-flagship` by keeping motion/interaction complexity disciplined (<= 3 passes). Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Inspect project stack/tokens and establish a coherent creative direction (`creative-direction.md`).
2. Define typography, surface/color hierarchy, and responsive composition tailored to the product domain.
3. Implement clean, modular UI with purposeful micro-interactions and accessible semantics.
4. Render, run visual + functional critique (`visual-critique.md`), and refine up to 3 bounded passes.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [creative-direction.md](../../references/creative-direction.md)
- [typography-and-content.md](../../references/typography-and-content.md)
- [color-and-surfaces.md](../../references/color-and-surfaces.md)
- [layout-and-responsive.md](../../references/layout-and-responsive.md)
- [visual-critique.md](../../references/visual-critique.md)
- [verification-and-refinement.md](../../references/verification-and-refinement.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Cohesive, high-craft interface with verified visual/responsive/a11y quality and explicit reporting of any unrendered checks.
