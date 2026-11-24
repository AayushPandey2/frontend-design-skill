---
name: formforge-plan
description: FORMFORGE interactive read-only design consultation producing a standalone master implementation prompt. Use when invoked via /formforge-plan or when planning a frontend before coding.
license: MIT
---

# /formforge-plan

## Purpose & Scope

STRICT READ-ONLY CONSULTATION MODE: Guide users from incomplete ideas or references to a complete, locked, implementation-ready specification and standalone copyable master prompt. Never modify frontend source files, install dependencies, or auto-execute the final prompt.

## Activation Criteria & Boundaries

Use before coding when requirements, aesthetic direction, or UX structure need interactive alignment. Never edits repository code; may consume approved decisions from `/formforge-explore` or `/formforge-inspire`. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Inspect existing workspace context read-only if a project exists.
2. Run progressive consultation (`planning-mode.md`): clarify product, audience, functional scope, visual references, and design terminology.
3. Lock typography, color system, layout, page/component structure, motion, responsive rules, and technical constraints, resolving contradictions.
4. Compile and deliver the complete standalone master implementation prompt (`master-prompt-spec.md`) for the user to copy.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [planning-mode.md](../../references/planning-mode.md)
- [master-prompt-spec.md](../../references/master-prompt-spec.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Approved design specification summary and a standalone, copyable master implementation prompt—zero source files modified.
