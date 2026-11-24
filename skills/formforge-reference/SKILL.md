---
name: formforge-reference
description: FORMFORGE read-only visual reference analysis. Use when invoked via /formforge-reference to extract a 14-point design specification from screenshots or websites without coding.
license: MIT
---

# /formforge-reference

## Purpose & Scope

STRICT READ-ONLY MODE: Analyze screenshots or authorized websites and produce a structured, 14-point implementation-ready design specification. Never automatically generate or modify frontend code.

## Activation Criteria & Boundaries

Use when the user wants to understand or document a visual reference's design system before deciding whether to implement. Unlike `/formforge-replicate`, Reference never writes UI code. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Inspect provided desktop/mobile screenshots or authorized reference URLs.
2. Extract all 14 dimensions in `reference-and-replication.md` (design language, typography, palette, semantic colors, grid, proportions, spacing, components, surfaces, shadows/borders, imagery, density, responsive behavior, observable motion).
3. Mark inferred values explicitly and note anything unobservable from static images (such as hover/motion).
4. Deliver the structured specification ready for `/formforge-plan` or `/formforge-replicate`.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [reference-and-replication.md](../../references/reference-and-replication.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Structured 14-point design specification with measured/inferred markers—zero code generated.
