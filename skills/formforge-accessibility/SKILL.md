---
name: formforge-accessibility
description: FORMFORGE accessibility auditing and remediation. Use when invoked via /formforge-accessibility to fix semantic HTML, keyboard, focus, contrast, screen-reader, and reduced-motion issues.
license: MIT
---

# /formforge-accessibility

## Purpose & Scope

Identify and resolve semantic HTML, keyboard navigation, focus management, WCAG 2.2 AA contrast, ARIA naming, screen-reader announcement, and reduced-motion accessibility issues.

## Activation Criteria & Boundaries

Use for targeted accessibility remediation or verification. Unlike read-only `/formforge-audit`, implements verified accessibility fixes unless asked for review only. Do not auto-chain or circularly invoke sibling skills; suggest optional next skills only after completing this workflow.

## Workflow

1. Audit landmarks, headings, form labels/errors, keyboard tab order, focus visibility, dialogs/menus, contrast, and reduced-motion (`accessibility-engineering.md`).
2. Replace clickable `<div>`/`<span>` patterns with native semantic controls (`<button>`, `<a>`, `<dialog>`).
3. Fix focus trapping/restoration, live regions, contrast tokens, and keyboard alternatives for pointer gestures.
4. Verify keyboard-only traversal, accessible names, contrast ratios, and reduced-motion behavior.

## Shared Reference Routing

- Core kernel: [SKILL.md](../../SKILL.md)
- [accessibility-engineering.md](../../references/accessibility-engineering.md)
- [functional-and-technical-audits.md](../../references/functional-and-technical-audits.md)
- [verification-and-refinement.md](../../references/verification-and-refinement.md)
- *Standalone install fallback*: If installed outside the repo root, resolve `SKILL.md` and `references/*.md` from the installed `formforge/` skill directory.

## Expected Output & Verification Requirements

Resolved accessibility issues with native-first semantics and verified keyboard/contrast/ARIA checks.
