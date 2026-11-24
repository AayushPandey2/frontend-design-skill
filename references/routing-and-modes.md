# Routing & Adaptive Execution Modes

## 1. Task Classification Matrix

Evaluate all five dimensions before selecting a mode or loading references:

- **Task type**: new interface, redesign, page/component creation, component modification, visual/layout/responsive fix, design system generation/maintenance, motion, accessibility remediation, performance optimization, debugging, UI/UX critique, or design reproduction.
- **Scope**: single property -> single element -> single component -> section -> page -> multi-page -> design system -> full app.
- **Complexity**: count interacting components, user journeys, state/data dependencies, and technical uncertainty—never raw line count.
- **Risk**: interaction breakage, auth/payment/data-loss impact, a11y/responsive regression, security, or design-system drift. High risk upgrades verification even for small edits.
- **User intent**: implement code, advise/critique only, debug, reproduce, or scoped edit. Never edit files on review-only requests; never redesign on targeted fixes.

## 2. Mode Workflows & Guardrails

### `QUICK`
- **Workflow**: Inspect affected files -> preserve existing conventions -> minimal complete change -> targeted verification -> concise report.
- **Restrictions**: No design brief, no design system generation, no repo-wide audit, no new dependencies, no unrelated refactoring, no repeated verification without cause.

### `STANDARD`
- **Workflow**: Understand requirements -> inspect project & conventions -> load matched capabilities -> preserve/set direction -> implement -> verify behavior -> render/inspect if practical -> refine defects -> deliver.

### `PREMIUM`
- **Workflow**: Product & audience brief -> inspect architecture -> explore creative directions (skip if brand/reference already pins direction) -> select visual identity -> tokens -> plan journeys/states -> implement -> render -> visual/technical critique -> refine -> verify gates.

### `FLAGSHIP`
- **Workflow**: Deep product/audience analysis -> creative direction -> design system -> complex interactions -> purposeful motion -> comprehensive responsive, a11y & perf verification -> independent critique -> bounded refinement.
- **Guardrail**: Never load every capability automatically; activate only what the experience actually requires.

### Escalation & De-escalation
- **Escalate** when hidden coupling, higher risk, broader regressions, or missing design foundations surface.
- **De-escalate** when an existing component/token already solves most of the task.

## 3. Capability Routing Procedure

1. Interpret request and classify 5 dimensions.
2. Inspect existing project constraints first.
3. Select the lightest sufficient mode.
4. Load mandatory core references only; exclude unrelated capabilities.
5. Expand context only if a concrete gap or verification failure emerges. Never recurse indefinitely or reload already-read references.

## 4. Routing Examples

- **Change button border radius**: `QUICK` -> inspect button + tokens -> preserve design language -> apply edit. Exclude creative direction, motion, and industry modules.
- **Build a premium financial dashboard**: `PREMIUM` -> load design systems, fintech/data density, hierarchy, typography, responsive, a11y, perf. Exclude decorative motion unless justified.
- **Build a cinematic creative portfolio**: `PREMIUM`/`FLAGSHIP` -> load creative direction, typography, composition, asset direction, motion, responsive, perf, a11y.
- **Fix keyboard navigation in a modal**: `STANDARD` -> load accessibility + component focus/Escape/dismissal rules -> preserve visual design -> verify keyboard flow.
- **Make an existing page load faster**: `STANDARD` -> load perf + framework guidance -> profile/identify bottlenecks -> targeted fix -> measure if supported.
- **Build a luxury product landing page**: `PREMIUM` -> load `creative-direction`, `typography-and-content`, `color-and-surfaces`, `layout-and-responsive`, `industry-patterns` (skip dense dashboard/tool rules).
- **Improve an existing dashboard table**: `STANDARD` -> load `layout-and-responsive` (hierarchy/density), `ux-and-systems` (table patterns), `project-and-memory` (existing tokens/a11y) -> skip creative exploration.
- **Change the primary accent color**: `QUICK` -> load `color-and-surfaces` (semantic color + contrast), `implementation-economy` -> skip full design intelligence.
- **Improve a confusing checkout flow**: `STANDARD`/`PREMIUM` -> load `ux-and-systems` (journeys, IA, forms, states), `industry-patterns` (e-commerce), `typography-and-content` (microcopy).

## 5. Context Budgets & Compression

- Experimental targets (kernel + loaded references): `QUICK` ~1.5k–3k, `STANDARD` ~3k–6k, `PREMIUM` ~6k–10k, `FLAGSHIP` ~10k–15k tokens.
- Expand above target only when essential requirements demand it. Do not build token-counting machinery to enforce budgets.
