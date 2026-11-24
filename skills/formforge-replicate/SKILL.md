---
name: formforge-replicate
description: FORMFORGE screenshot-to-code and authorized website-reference-to-code implementation. Use when invoked via /formforge-replicate to faithfully recreate a visual reference.
license: MIT
---

# /formforge-replicate

## Purpose & Scope

Recreate a user-provided screenshot or authorized website reference using the smallest complete implementation, then render, compare, and fix visual discrepancies.

## Activation Criteria & Boundaries

Use when the user wants working code matching a provided screenshot or authorized reference URL. Unlike `/formforge-reference` (read-only spec only), Replicate implements code. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Analyze desktop/mobile screenshots or authorized reference using the 14-point extraction schema (`reference-and-replication.md`).
2. Identify required fonts, icons, and media assets; respect licensing/permissions and use authorized or clean fallback assets.
3. Implement the interface with minimal, clean code matching the target stack.
4. Render the implementation, compare side-by-side against the original reference, fix meaningful discrepancies, and report unavailable assets or unavoidable differences honestly.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [reference-and-replication.md](../../references/reference-and-replication.md)
- [implementation-economy.md](../../references/implementation-economy.md)
- [layout-and-responsive.md](../../references/layout-and-responsive.md)
- [verification-and-refinement.md](../../references/verification-and-refinement.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Implemented interface plus side-by-side comparison notes, missing-asset disclosures, and honest fidelity status (never claiming pixel-perfection without evidence).
