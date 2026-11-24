---
name: formforge-optimize
description: FORMFORGE code, bundle, rendering, and Core Web Vitals optimization. Use when invoked via /formforge-optimize to eliminate UI waste and performance bottlenecks.
license: MIT
---

# /formforge-optimize

## Purpose & Scope

Eliminate unnecessary frontend code, redundant state/effects, oversized dependencies, rendering bottlenecks, and Core Web Vitals regressions without degrading UX or accessibility.

## Activation Criteria & Boundaries

Use for slow renders, bloated bundles, unnecessary re-renders, image/font bottlenecks, or over-engineered UI code. Never sacrifice accessibility, validation, or correctness. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Profile or inspect bundle, dependency weight, rendering paths, state/effects, and asset loading.
2. Identify dead code, derived-state effects, unoptimized media/fonts, and heavy library usage replaceable by native browser/CSS features.
3. Apply minimal, high-leverage optimizations (`implementation-economy.md`, `performance-and-reliability.md`).
4. Re-verify build, runtime behavior, and measurable performance metrics (never fabricate timings).

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [implementation-economy.md](../../references/implementation-economy.md)
- [components-and-frameworks.md](../../references/components-and-frameworks.md)
- [performance-and-reliability.md](../../references/performance-and-reliability.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Leaner, faster frontend code with measured or structurally verified improvements and intact functionality.
