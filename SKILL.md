---
name: formforge
description: Unified frontend design and engineering intelligence for building, redesigning, auditing, and optimizing web and mobile interfaces. Combines creative direction, visual design, UX, design systems, components, purposeful motion, frontend engineering, verification, and strict code/context economy. Use whenever creating, modifying, reviewing, or debugging UI, pages, components, layouts, styles, animations, accessibility, or design systems.
license: MIT
metadata:
  version: "0.1.0"
  tagline: "Maximum taste. Minimum waste."
---

# FORMFORGE — Core Operating Kernel

> **Maximum taste. Minimum waste.**
> Maximize visual craft, usability, functional correctness, and design consistency while minimizing unnecessary code, tokens, dependencies, tool calls, and abstractions. Optimize waste, never value.

## 1. Instruction Priority Ladder

Resolve any conflict using this strict order (contextual exceptions beat rigid universal bans):

1. Safety, security, and mandatory platform constraints.
2. Explicit user requirements and brief constraints.
3. Functional correctness and data integrity.
4. Accessibility (keyboard, contrast, semantics, reduced motion) and usability.
5. Existing project architecture, tech stack, and design system.
6. Product-specific creative direction and visual identity.
7. Runtime performance and long-term maintainability.
8. Code, context, and tool-call economy.
9. Creative experimentation.
10. Decorative preferences.

## 2. Adaptive Execution Modes

Select the lightest mode that satisfies task scope, risk, and quality bar. Honor explicit user overrides.

| Mode | Trigger Scope | Workflow Depth | Verification |
| :--- | :--- | :--- | :--- |
| **QUICK** | Single-component tweak, CSS/layout fix, copy update, low-risk edit | Inspect affected files -> minimal edit -> targeted check | Targeted build/lint/render check |
| **STANDARD** | Ordinary page, new component, feature UI, a11y/perf remediation | Inspect project -> establish/preserve direction -> implement -> verify | Render + responsive + a11y + functional check |
| **PREMIUM** | Landing page, product interface, multi-view flow, design system setup | Product brief -> creative direction -> token system -> build -> render & critique -> refine | Full rubric check + rendered visual critique |
| **FLAGSHIP** | High-craft portfolio, flagship brand experience, complex interactive UI | Deep direction exploration -> bespoke typography/motion -> build -> independent critique -> refine | Comprehensive visual, motion, a11y & perf audit |

## 3. Execution Loop

Scale each stage to the active mode:

`Understand -> Route -> Design -> Implement -> Render -> Critique -> Refine -> Verify -> Deliver`

- **Bounded refinement**: Every refinement pass must target an identified weakness. Stop once acceptance criteria are met and additional passes yield no meaningful improvement.
- **No gratuitous redesigns**: Never alter working visual direction or architecture without a concrete requirement or defect.

## 4. Global Economy Protocol

### Code Economy Decision Ladder
Before writing new code, evaluate in order and stop at the first viable option:
1. **Existing project code**: Reuse existing components, tokens, helpers, and patterns.
2. **Native HTML & CSS**: Prefer semantic elements, CSS Grid/Flexbox, `:has()`, `clamp()`, and CSS transitions over JS.
3. **Browser APIs**: Use native platform capabilities before reaching for libraries.
4. **Existing dependencies**: Use what is already installed; never add a package for trivial logic.
5. **Small custom implementation**: Write clear, minimal, readable code with shallow nesting.
6. **Justified complexity**: Add abstractions or dependencies only when concrete benefits outweigh maintenance cost.

**Enforce strictly**: No speculative features, premature abstractions, unnecessary component wrappers, redundant state, effects for derived values, file rewrites for minor edits, or dead code. Never sacrifice readability for line-count golfing.

### Context & Tool Economy
- Inspect directory structure and search symbols before reading files; read only necessary line ranges.
- Never reload unchanged files or unrelated reference modules.
- Batch independent tool calls; keep reasoning and final reports concise and actionable.

### Quality Protection Floor
Economy rules never override functional correctness, accessibility, security, responsiveness, essential error handling, readability, or visual quality.

## 5. Contextual Anti-Generic Design Check

Before writing UI code in `STANDARD`, `PREMIUM`, or `FLAGSHIP` mode, verify that visual choices are earned by the product rather than pulled from generic defaults:
- **Earned structure**: Use cards, borders, badges, numbered markers, gradients, or glass effects only when they clarify hierarchy or serve the brand—never as filler.
- **Typography & copy**: Pick intentional typefaces, clear scale, readable line lengths, and active, user-centric copy. Avoid filler labels, fake metrics, and decorative micro-badges.
- **Purposeful motion**: Animate to communicate state change, spatial continuity, or focal hierarchy. Respect `prefers-reduced-motion`; skip unmotivated entrance choreography.
- **User authority**: When a brief explicitly requests a specific aesthetic, honor it cleanly.

## 6. Capability Routing (Progressive Context)

Load only the capability domains needed for the current task. Full capability contracts live in [docs/capability-registry.json](docs/capability-registry.json), and system rules live in [docs/architecture.md](docs/architecture.md).

| Domain ID | Domain | Activate When |
| :--- | :--- | :--- |
| `FF-CR` | Creative Intelligence | Defining visual direction, brand adaptation, hero concepts, or originality |
| `FF-VD` | Visual Design | Choosing typography, color systems, layout grids, spacing, contrast, or density |
| `FF-UX` | UX Intelligence | Structuring navigation, forms, states (loading/empty/error/success), or mobile flows |
| `FF-DS` | Design Systems | Creating or maintaining tokens, themes, light/dark modes, or design memory |
| `FF-CP` | Component Intelligence | Discovering, reusing, composing, or architecting accessible UI components |
| `FF-MO` | Motion Intelligence | Designing transitions, micro-interactions, choreography, or reduced-motion rules |
| `FF-EN` | Frontend Engineering | Implementing semantic HTML/CSS/TS/framework code, state, perf, or security |
| `FF-SP` | Specialized Product | Adapting density and patterns for SaaS, fintech, e-commerce, AI, or mobile |
| `FF-VF` | Verification Intelligence | Inspecting rendered UI, responsive breakpoints, a11y, perf, and regressions |
| `FF-OP` | Optimization Intelligence | Enforcing token budgets, minimal diffs, dependency hygiene, and bounded loops |

## 7. Verification & Honesty Gates

- **Mandatory gates**: Functional correctness, accessibility, and security must pass before delivery.
- **Evidence rule**: Never claim an interface is visually verified unless the actual rendered output has been inspected.
- **Honest reporting**: Report only observed tool outputs, executed checks, and real unresolved issues.
