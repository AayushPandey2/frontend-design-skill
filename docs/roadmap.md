# FORMFORGE Implementation Roadmap

## Phase 01 — Foundation, Research & Architecture (Complete)
- [x] Portable `agentskills.io` structure, 10-domain capability model, 100-point rubric, and 12-category benchmark tasks.

## Phase 02 — Core Intelligence, Adaptive Routing & Engineering Economy (Complete)
- [x] Level 0/1 operating kernel in [SKILL.md](../SKILL.md), 4 core Level 2 modules, consolidated [capability-registry.json](capability-registry.json), and [core-intelligence.json](../evals/core-intelligence.json).

## Phase 03 — Advanced Design Intelligence & Visual Craftsmanship (Complete)
- [x] Authored 6 consolidated Level 2 design intelligence modules: [creative-direction.md](../references/creative-direction.md), [typography-and-content.md](../references/typography-and-content.md), [color-and-surfaces.md](../references/color-and-surfaces.md), [layout-and-responsive.md](../references/layout-and-responsive.md), [ux-and-systems.md](../references/ux-and-systems.md), and [industry-patterns.md](../references/industry-patterns.md).
- [x] Integrated design routing into [SKILL.md](../SKILL.md) and [routing-and-modes.md](../references/routing-and-modes.md), updated [capability-registry.json](capability-registry.json), created [design-intelligence.json](../evals/design-intelligence.json), and added `supplementary_design_rubric` to [rubric.json](../evals/rubric.json).

## Phase 04 — Frontend Engineering, Accessible Components, Motion & Performance
- Author engineering-level modules for semantic HTML/modern CSS/security, accessible interactive primitives (keyboard, focus, ARIA), spring/gesture motion engineering, and Core Web Vitals/bundle optimization.

## Phase 05 — Browser Verification, Visual Criticism & Automated Quality Gates
- Integrate live browser verification, independent visual criticism, and empirical baseline evaluations across `evals/`.
- Prune any instructions that do not measurably improve quality per unit of context.

---

## Open Uncertainties & Assumptions
- **Live-agent & rendered execution**: Structural/referential checks pass, but [core-intelligence.json](../evals/core-intelligence.json), [design-intelligence.json](../evals/design-intelligence.json), and [tasks.json](../evals/tasks.json) have not yet been executed against live agent or browser runs.
- **Token counts**: Reported token counts are word-based estimates (`words * 1.33`), not tokenizer-exact measurements.
- **Rubric hypothesis**: `supplementary_design_rubric` in [rubric.json](../evals/rubric.json) is an unvalidated evaluation hypothesis subordinate to mandatory global gates.
