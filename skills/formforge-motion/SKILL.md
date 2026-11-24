---
name: formforge-motion
description: FORMFORGE advanced animations, transitions, gestures, and micro-interactions. Use when invoked via /formforge-motion for purposeful, performant, reduced-motion-safe motion engineering.
license: MIT
---

# /formforge-motion

## Purpose & Scope

Design and implement purposeful micro-interactions, transitions, choreography, scroll-driven effects, and gesture interactions using native CSS/browser capabilities first, with full interruptibility and reduced-motion parity.

## Activation Criteria & Boundaries

Use when adding or refining interactive motion, shared-element/page transitions, springs, or gestures. Never add motion as mandatory decoration. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Assess whether motion clarifies state, spatial continuity, or feedback (`motion-and-interactions.md`).
2. Author the 12-point Animation Specification Contract (trigger, initial/final states, properties, duration, delay, easing, stagger, interruption, repeat, responsive, reduced-motion).
3. Implement using native CSS / WAAPI / View Transitions first, keeping animations compositor-safe and interruptible.
4. Verify reduced-motion alternatives, keyboard parity for gestures, and smooth runtime behavior.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [motion-and-interactions.md](../../references/motion-and-interactions.md)
- [accessibility-engineering.md](../../references/accessibility-engineering.md)
- [performance-and-reliability.md](../../references/performance-and-reliability.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

12-point motion specifications and accessible, interruptible, native-first animation implementation.
