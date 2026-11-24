---
name: formforge-assets
description: FORMFORGE visual asset discovery and planning. Use when invoked via /formforge-assets to plan photography, illustrations, icons, textures, videos, and asset performance constraints.
license: MIT
---

# /formforge-assets

## Purpose & Scope

Discover and specify suitable photography, illustrations, icons, textures, videos, and product imagery with clear art direction, licensing, cropping, accessibility, and performance constraints.

## Activation Criteria & Boundaries

Use when planning or sourcing visual media slots for a page or component. Never fabricate asset availability or invent unverified URLs. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Audit every visual slot in the UI and define its communication role (`inspiration-and-exploration.md`, `layout-and-responsive.md`).
2. Specify subject, lighting, framing, aspect ratio, focal point, and verified source/licensing requirements.
3. Set accessibility (`alt` rules) and performance constraints (`AVIF`/`WebP`, explicit dimensions, LCP eager vs. lazy loading, SVG optimization).
4. Report any missing or unavailable assets honestly with safe placeholder specs.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [inspiration-and-exploration.md](../../references/inspiration-and-exploration.md)
- [layout-and-responsive.md](../../references/layout-and-responsive.md)
- [performance-and-reliability.md](../../references/performance-and-reliability.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Actionable asset plan covering art direction, licensing, placement/cropping, accessibility, and performance—with zero fabricated URLs.
