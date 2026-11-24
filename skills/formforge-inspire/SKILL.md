---
name: formforge-inspire
description: FORMFORGE web-based visual inspiration discovery. Use when invoked via /formforge-inspire to find real-world design references and explain effective techniques without coding.
license: MIT
---

# /formforge-inspire

## Purpose & Scope

STRICT READ-ONLY MODE: Discover relevant, real-world web design inspiration tailored to the product and aesthetic, display screenshots when supported or verified links otherwise, and explain transferable techniques. Never automatically begin frontend implementation.

## Activation Criteria & Boundaries

Use at the start of ideation when the user wants concrete real-world visual references. Avoid irrelevant stock galleries and fabricated URLs. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Clarify product domain, audience, mood, and aesthetic constraints.
2. Search for real-world, live web design examples with verified URLs (`inspiration-and-exploration.md`).
3. Present inline images when supported (or descriptive + verified link fallbacks) and explain why each reference's typography, layout, color, and interaction work.
4. Invite the user to pick preferred traits or continue into `/formforge-explore` or `/formforge-plan`.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [inspiration-and-exploration.md](../../references/inspiration-and-exploration.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Curated list of verified real-world web references with visual breakdowns and selectable traits—zero code generated.
