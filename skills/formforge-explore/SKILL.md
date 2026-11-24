---
name: formforge-explore
description: FORMFORGE creative exploration and moodboard generator. Use when invoked via /formforge-explore to compare 2-4 genuinely distinct creative directions before planning or coding.
license: MIT
---

# /formforge-explore

## Purpose & Scope

STRICT READ-ONLY MODE: Generate 2–4 genuinely distinct creative directions and moodboards (never color-only swaps) covering identity, philosophy, references, type, palette, layout, components, assets, motion, and trade-offs. Never automatically implement code.

## Activation Criteria & Boundaries

Use when the user wants to evaluate meaningfully different creative directions before locking a design in `/formforge-plan`. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Understand product goals, domain posture, and constraints.
2. Develop 2–4 structurally and aesthetically distinct directions using the 10-part Direction Card (`inspiration-and-exploration.md`).
3. Present advantages, trade-offs, and verified reference anchors for each direction.
4. Allow the user to select, reject, or combine compatible traits for handoff to `/formforge-plan`.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [inspiration-and-exploration.md](../../references/inspiration-and-exploration.md)
- [creative-direction.md](../../references/creative-direction.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

2–4 complete, distinct creative direction moodboards ready for user selection or `/formforge-plan` integration—zero code modified.
