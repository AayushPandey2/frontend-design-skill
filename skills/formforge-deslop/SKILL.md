---
name: formforge-deslop
description: FORMFORGE AI-slop detection and cleanup. Use when invoked via /formforge-deslop to eliminate generic compositions, repetitive cards, meaningless decoration, and generic copy.
license: MIT
---

# /formforge-deslop

## Purpose & Scope

Detect and eliminate generic AI-generated UI patterns—weak hierarchy, monotonous card grids, gratuitous gradients/glows, cliché copy, and decorative noise—without enforcing a rigid universal style blacklist.

## Activation Criteria & Boundaries

Use when an interface feels templated, repetitive, or over-decorated. Replaces generic clutter with purposeful typography, hierarchy, and authentic product framing. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Run an anti-generic critique (`visual-critique.md`) against the product's actual domain and hierarchy.
2. Identify repetitive card wrappers, filler badges, decorative blurs/gradients, and generic placeholder copy.
3. Replace clutter with intentional layout rhythm, restrained surfaces, and domain-authentic copy (`creative-direction.md`, `typography-and-content.md`).
4. Verify improved visual clarity and preserved functionality.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [visual-critique.md](../../references/visual-critique.md)
- [creative-direction.md](../../references/creative-direction.md)
- [typography-and-content.md](../../references/typography-and-content.md)
- [layout-and-responsive.md](../../references/layout-and-responsive.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Cleaner, more distinctive UI with generic slop removed and functional/visual quality verified.
