---
name: formforge-quick
description: FORMFORGE QUICK mode for targeted, low-risk frontend edits. Use when invoked via /formforge-quick or for localized UI copy, style, or small component fixes.
license: MIT
---

# /formforge-quick

## Purpose & Scope

Execute small, localized, low-risk frontend modifications (copy tweaks, spacing, CSS fixes, single-prop adjustments) with minimal context and zero unrelated redesign.

## Activation Criteria & Boundaries

Use for isolated edits on 1–2 files with low regression risk. Escalate to `STANDARD` only if hidden coupling, a11y breakage, or broken flows are discovered. Do not invoke sibling skills. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Locate the exact target file(s) and read only the relevant range.
2. Verify existing design tokens or utility classes so the edit matches surrounding UI.
3. Apply the smallest targeted change without refactoring unrelated code or styles.
4. Run targeted verification (build/typecheck/lint or quick visual check) on the changed area.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [implementation-economy.md](../../references/implementation-economy.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Minimal, clean edit with targeted verification results and no unrequested changes.
