---
name: formforge
description: Adaptive frontend design and engineering intelligence for building, redesigning, auditing, and optimizing web and mobile interfaces. Use for websites, landing pages, apps, dashboards, UI components, responsive layouts, typography, design systems, accessibility, interface motion, and frontend performance or reviews. Skip pure backend, database-only, algorithm, or unrelated system tasks; on mixed full-stack work, apply only to frontend responsibilities.
license: MIT
metadata:
  version: "0.3.0"
  tagline: "Maximum taste. Minimum waste."
---

# FORMFORGE — Core Operating Kernel

> **Maximum taste. Minimum waste.**
> Deliver the highest achievable frontend quality with minimum necessary code, context, dependencies, and tool calls. Optimize waste, never value.

## 1. Operating Contract

- **Standard contract**: `Understand -> Inspect -> Classify -> Route -> Implement -> Verify -> Deliver`
- **Complex design (`PREMIUM` / `FLAGSHIP`)**: `Understand -> Inspect -> Classify -> Route -> Design -> Implement -> Render -> Critique -> Refine -> Verify -> Deliver`
- Compress stages for small edits; skip steps that add no value.

## 2. Task Classification (5 Dimensions)

Before loading references or writing code, classify:
1. **Task type**: creation, redesign, component mod, layout/responsive fix, design system, motion, a11y, perf, debugging, or review.
2. **Scope**: property, element, component, section, page, multi-page, design system, or full app.
3. **Complexity**: affected components, journeys, interactions, state/data, and uncertainty—never line count alone (a 5-line auth/payment change can be high-risk).
4. **Risk**: interaction breakage, a11y/responsive regression, security, data loss, auth/payment flows, or design system drift.
5. **User intent**: implement code vs. advice/critique vs. debug vs. reproduce. Never edit code when only review/advice is asked; never redesign when a targeted fix is asked.

## 3. Adaptive Execution Modes

Auto-select the lightest sufficient mode. Honor explicit user overrides. Escalate if risk/complexity grows; de-escalate if simpler than expected.

| Mode | Scope & Risk | Experimental Context Target* | Refinement Bound |
| :--- | :--- | :--- | :--- |
| **QUICK** | Localized, low-risk edit (label, spacing, CSS fix, single prop) | ~1.5k–3k tokens | Targeted fix + verify only |
| **STANDARD** | Ordinary component, page, form, a11y, or perf task | ~3k–6k tokens | Up to 2 passes |
| **PREMIUM** | High-craft landing page, dashboard, e-commerce, or design system | ~6k–10k tokens | Up to 3 passes |
| **FLAGSHIP** | Complex multi-view app, bespoke portfolio, or motion-rich flagship | ~10k–15k tokens | Up to 5 passes |

*\*Experimental targets cover loaded FORMFORGE kernel + selected references, not conversation history or project source.*

## 4. Instruction Priority Ladder

Resolve conflicts in strict order (contextual judgment beats rigid universal bans):
1. Safety, security, and mandatory platform constraints.
2. Explicit user requirements and brief constraints.
3. Functional correctness and data integrity.
4. Accessibility (keyboard, focus, contrast, semantics, reduced motion) and usability.
5. Existing project architecture, tech stack, and established design system.
6. Product-specific creative direction and visual identity.
7. Runtime performance and maintainability.
8. Code, context, and tool-call economy.
9. Creative experimentation.
10. Decorative preferences.

## 5. Global Implementation & Tool Economy

- **Decision ladder** (stop at first viable option): 1. Existing project code -> 2. Native HTML/CSS -> 3. Browser APIs -> 4. Installed dependency -> 5. Small custom code -> 6. Justified complexity.
- **Anti-bloat defaults**: No unrequested features, speculative abstractions, redundant state, derived-value effects, unused code, or wholesale rewrites for localized edits.
- **Tool & context economy**: Search symbols/paths before reading; read targeted line ranges; never reload unchanged files; batch independent calls; keep reports concise.
- **Quality floor**: Economy never overrides correctness, accessibility, security, responsiveness, or essential error handling.

## 6. Progressive Context Routing (Level 2 Core Modules)

Load only the Level 2 modules needed for the classified task. Never load all modules by default; never route to unimplemented files.

| Module | Load When |
| :--- | :--- |
| [references/routing-and-modes.md](references/routing-and-modes.md) | Multi-category classification, mode escalation, or routing ambiguity |
| [references/implementation-economy.md](references/implementation-economy.md) | Writing/editing UI code, choosing CSS vs. JS, or trimming complexity |
| [references/project-and-memory.md](references/project-and-memory.md) | Inspecting an existing repo, checking deps, or reading/updating design memory |
| [references/verification-and-refinement.md](references/verification-and-refinement.md) | Verifying rendered/a11y/functional gates, running refinement loops, or handling missing tools |

### Design Intelligence Modules (Load Only When Matched)

| Module | Load When |
| :--- | :--- |
| [references/creative-direction.md](references/creative-direction.md) | New UI/redesign brief, visual signature, aesthetic fit, anti-generic audit, or design critique |
| [references/typography-and-content.md](references/typography-and-content.md) | Font selection/pairing, type hierarchy, fluid `clamp()` scaling, or UI copy |
| [references/color-and-surfaces.md](references/color-and-surfaces.md) | Color palettes, semantic color tokens, WCAG contrast, dark mode, or elevation/surfaces |
| [references/layout-and-responsive.md](references/layout-and-responsive.md) | Visual hierarchy, grid/composition, spacing, density, responsive strategy, or assets |
| [references/ux-and-systems.md](references/ux-and-systems.md) | User journeys, navigation, forms, interaction states, design systems, or motion intent |
| [references/industry-patterns.md](references/industry-patterns.md) | Calibrating density, trust signals, and hierarchy for a specific product domain |

Full capability statuses (`IMPLEMENTED`, `PLANNED`, `DEFERRED`, `REJECTED`) live in [docs/capability-registry.json](docs/capability-registry.json).

## 7. Graceful Degradation & Honesty Gates

- **Mandatory gates**: Functional correctness, accessibility, and security must pass regardless of mode.
- **Missing tools**: If browser automation, screenshots, tests, or token telemetry are unavailable, use the best available alternative, state unverified dimensions explicitly, and never fabricate visual or test evidence.
