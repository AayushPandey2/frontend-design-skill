---
name: formforge-dna
description: FORMFORGE persistent project Design DNA management. Use when invoked via /formforge-dna to extract, create, update, apply, or detect drift in project design identity.
license: MIT
---

# /formforge-dna

## Purpose & Scope

Extract, create, update, and apply persistent project-specific design identity (`DESIGN.md` when justified) while keeping code and design tokens as the authoritative source for implementation values.

## Activation Criteria & Boundaries

Use to capture an existing project's visual identity, establish Design DNA for a new project, apply conventions to new pages, or detect design drift across sessions. Never persist secrets or PII. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Inspect existing code, tokens, components, and any existing `DESIGN.md` (`design-dna.md`, `project-and-memory.md`).
2. Extract or update the 11-point Design DNA schema without duplicating exact code token tables.
3. When applying DNA or checking drift, compare new UI against `DESIGN.md` and authoritative tokens to flag off-scale or unapproved patterns.
4. Verify no sensitive credentials, internal URLs, or PII are stored in `DESIGN.md`.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [design-dna.md](../../references/design-dna.md)
- [project-and-memory.md](../../references/project-and-memory.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Extracted/updated `DESIGN.md` (when justified) or drift report grounded in authoritative project tokens.
