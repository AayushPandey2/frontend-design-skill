---
name: formforge-compare
description: FORMFORGE structured comparison of design alternatives and before-and-after implementations. Use when invoked via /formforge-compare for evidence-based evaluation.
license: MIT
---

# /formforge-compare

## Purpose & Scope

STRICT READ-ONLY MODE: Compare visual concepts, reference designs, screenshots, or before-and-after implementations under consistent conditions and evidence-based criteria. Never automatically modify code unless explicitly requested.

## Activation Criteria & Boundaries

Use when choosing between UI variants, evaluating a redesign against the original, or comparing implementation against reference. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Establish consistent comparison conditions (matching viewport, theme, data state, and criteria).
2. Inspect both candidates across hierarchy, layout balance, contrast/a11y, responsiveness, interaction clarity, and code/visual economy (`reference-and-replication.md`, `visual-critique.md`).
3. Separate objective observations from subjective trade-offs and note any unrendered dimensions.
4. Deliver a clear recommendation without modifying code unless the user explicitly asks to apply changes.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [reference-and-replication.md](../../references/reference-and-replication.md)
- [visual-critique.md](../../references/visual-critique.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Structured side-by-side comparison matrix with objective findings, trade-offs, and recommendation—zero code edits by default.
