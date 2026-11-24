---
name: formforge
description: FORMFORGE auto-mode frontend design, engineering, and QA. Use when invoked via /formforge or for general frontend tasks needing auto-selected QUICK-FLAGSHIP rigor.
license: MIT
---

# /formforge

## Purpose & Scope

Automatically classify frontend requests across Type, Scope, Complexity, Risk, and Intent, then execute in the lightest sufficient mode (`QUICK`–`FLAGSHIP`).

## Activation Criteria & Boundaries

Default entry point for general frontend creation, modification, or review when no narrower `/formforge-*` command is specified. Never auto-chain sibling skills unless requested. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Classify the request across the 5 dimensions in `SKILL.md` before loading domain modules.
2. Auto-select `QUICK`, `STANDARD`, `PREMIUM`, or `FLAGSHIP` mode (respecting user overrides and escalating on discovered risk).
3. Load only intent-matched `references/*.md` modules and inspect existing project files/tokens first.
4. Implement with minimum necessary code/dependencies, verify proportionally, and run bounded refinement.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [routing-and-modes.md](../../references/routing-and-modes.md)
- [implementation-economy.md](../../references/implementation-economy.md)
- [verification-and-refinement.md](../../references/verification-and-refinement.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Implemented or reviewed frontend changes with a concise summary of mode used, key decisions, verified checks, and any unverified limitations.
