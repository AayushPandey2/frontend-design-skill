---
name: formforge-help
description: FORMFORGE command directory, capabilities overview, and usage examples. Use when invoked via /formforge-help to see all 25 commands and collaboration workflows.
license: MIT
---

# /formforge-help

## Purpose & Scope

STRICT READ-ONLY MODE: Display all 25 FORMFORGE commands, their purposes, example invocations, collaboration workflows, and platform/verification limitations without loading unrelated reference modules.

## Activation Criteria & Boundaries

Use whenever the user asks for `/formforge-help`, available commands, or how to combine FORMFORGE skills. Never load external reference files or modify files.

## Workflow

1. Respond directly from this skill's built-in command directory without loading external reference modules.
2. Present the grouped command table, relevant usage examples, and suggested collaboration workflows.
3. Note read-only boundaries and platform-specific invocation fallbacks.

## Command Directory (25 Skills)

### Execution Modes
- `/formforge` — Auto-select the lightest sufficient mode (`QUICK`–`FLAGSHIP`)
- `/formforge-quick` — Small, targeted, low-risk edits
- `/formforge-standard` — Ordinary components and pages reusing existing systems
- `/formforge-premium` — High-craft UI/UX, landing pages, and dashboards
- `/formforge-flagship` — Ambitious, motion-rich interactive experiences

### Planning, Inspiration & Reference (Read-Only)
- `/formforge-plan` — Interactive read-only design consultation -> standalone master prompt
- `/formforge-inspire` — Discover real-world web design inspiration & transferable techniques
- `/formforge-explore` — Compare 2–4 genuinely distinct creative directions & moodboards
- `/formforge-reference` — Extract a 14-point design specification from screenshots/sites (no code)
- `/formforge-compare` — Side-by-side comparison of concepts, references, or before/after UI

### Creation, Replication, Systems & Motion
- `/formforge-replicate` — Recreate a screenshot or authorized website reference in code + compare
- `/formforge-redesign` — Rethink an existing interface's creative direction while keeping core flows
- `/formforge-system` — Create, extract, or improve reusable design tokens and components
- `/formforge-dna` — Extract, maintain (`DESIGN.md`), and apply persistent project Design DNA
- `/formforge-motion` — Purposeful, native-first animations, transitions, and gestures
- `/formforge-assets` — Plan photography, illustrations, icons, licensing, cropping, and media perf

### Quality, Refinement & Verification
- `/formforge-audit` — Read-only comprehensive visual, functional, a11y, and waste inspection
- `/formforge-polish` — Refine typography, hierarchy, spacing, and surfaces without breaking logic
- `/formforge-deslop` — Detect and remove generic AI-generated patterns and decorative clutter
- `/formforge-responsive` — Design and repair responsive layouts across viewports
- `/formforge-accessibility` — Fix semantic, keyboard, focus, contrast, ARIA, and reduced-motion issues
- `/formforge-optimize` — Eliminate code, bundle, rendering, and Core Web Vitals waste
- `/formforge-verify` — Verify functional journeys, responsiveness, a11y, and build health
- `/formforge-fidelity` — Verify implementation agreement against approved design specs/contracts
- `/formforge-help` — Show this command directory and usage guide

## Example Invocations & Collaboration Workflows
- `/formforge-inspire Minimalist fintech dashboard` -> `/formforge-explore` -> `/formforge-plan` -> `/formforge-premium` -> `/formforge-fidelity`
- `/formforge-reference [screenshot]` -> `/formforge-replicate` -> `/formforge-compare` -> `/formforge-fidelity`
- `/formforge-dna` -> `/formforge-system` -> `/formforge-standard` -> `/formforge-verify`
- `/formforge-audit` -> `/formforge-deslop` -> `/formforge-polish` -> `/formforge-verify`

## Notes & Fallbacks
- Read-only skills (`plan`, `audit`, `reference`, `inspire`, `explore`, `compare`, `help`) never edit code.
- Where a host does not support native `/` slash commands, invoke any command by name in natural language (e.g., *"Use formforge-audit on src/Checkout.tsx"*).
