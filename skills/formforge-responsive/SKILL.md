---
name: formforge-responsive
description: FORMFORGE responsive layout design and repair. Use when invoked via /formforge-responsive to fix overflow, clipping, poor stacking, and mobile interaction issues.
license: MIT
---

# /formforge-responsive

## Purpose & Scope

Design and repair responsive layouts across mobile, tablet, and desktop viewports, fixing root causes of horizontal overflow, clipping, awkward wrapping, and unusable touch interactions.

## Activation Criteria & Boundaries

Use when layouts break across viewports, tables/grids overflow, or mobile navigation/touch targets fail. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Inspect layouts at key viewports (e.g., 375px, 768px, 1280px+) and identify root causes of overflow, clipping, or broken stacking.
2. Apply fluid Grid/Flexbox, container queries, `clamp()` sizing, and safe overflow patterns (`html-css-responsive.md`, `layout-and-responsive.md`).
3. Ensure touch targets, mobile nav, and sticky/fixed elements behave cleanly without obscuring content.
4. Re-verify across viewports and report any viewports that could not be live-rendered.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [html-css-responsive.md](../../references/html-css-responsive.md)
- [layout-and-responsive.md](../../references/layout-and-responsive.md)
- [functional-and-technical-audits.md](../../references/functional-and-technical-audits.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Responsive layout fixes targeting root causes across viewports with verified overflow-free behavior.
