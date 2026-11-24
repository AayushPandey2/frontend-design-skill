# FORMFORGE Implementation Roadmap

## Phase 01 — Foundation, Research & Architecture (Complete)
- [x] Portable `agentskills.io` structure, 10-domain capability model, 100-point rubric, and 12-category benchmark tasks.

## Phase 02 — Core Intelligence, Adaptive Routing & Engineering Economy (Complete)
- [x] Level 0/1 operating kernel in [SKILL.md](../SKILL.md), 4 core Level 2 modules, consolidated [capability-registry.json](capability-registry.json), and [core-intelligence.json](../evals/core-intelligence.json).

## Phase 03 — Advanced Design Intelligence & Visual Craftsmanship (Complete)
- [x] 6 Level 2 design modules, design routing integration, [design-intelligence.json](../evals/design-intelligence.json), and `supplementary_design_rubric`.

## Phase 04 — Advanced Frontend Engineering, Motion & Interaction Intelligence (Complete)
- [x] Authored 5 consolidated Level 2 engineering modules: [html-css-responsive.md](../references/html-css-responsive.md), [components-and-frameworks.md](../references/components-and-frameworks.md), [motion-and-interactions.md](../references/motion-and-interactions.md), [accessibility-engineering.md](../references/accessibility-engineering.md), and [performance-and-reliability.md](../references/performance-and-reliability.md).
- [x] Integrated engineering routing in [SKILL.md](../SKILL.md) and [routing-and-modes.md](../references/routing-and-modes.md), updated [capability-registry.json](capability-registry.json), created [engineering-intelligence.json](../evals/engineering-intelligence.json), and added `supplementary_engineering_rubric` to [rubric.json](../evals/rubric.json).

## Phase 05 — Browser Verification, Visual Criticism & Automated Quality Gates
- Integrate live browser verification, independent visual criticism, and automated quality gates (`FF-VF-01`).

## Phase 06 — Context & Architectural Optimization
- Profile and refine token budgets, context retrieval density, and routing precision.

## Phase 07 — Comparative Benchmarking & Ablation Testing
- Execute empirical blind comparisons and ablation runs across `evals/`.

---

## Open Uncertainties & Assumptions
- **Live-agent & browser execution**: Structural/referential checks pass, but [core-intelligence.json](../evals/core-intelligence.json), [design-intelligence.json](../evals/design-intelligence.json), [engineering-intelligence.json](../evals/engineering-intelligence.json), and [tasks.json](../evals/tasks.json) have not yet been executed against live agent, browser, or Lighthouse runs.
- **Token counts**: Reported token counts are word-based estimates (`words * 1.33`), not tokenizer-exact measurements.
- **Rubric hypotheses**: Supplementary design and engineering rubrics in [rubric.json](../evals/rubric.json) are unvalidated hypotheses subordinate to mandatory global gates.
