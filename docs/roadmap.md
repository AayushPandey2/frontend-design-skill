# FORMFORGE Implementation Roadmap

## Phase 01 — Foundation, Research & Architecture (Complete)
- [x] Portable `agentskills.io` structure, 10-domain capability model, 100-point rubric, and 12-category benchmark tasks.

## Phase 02 — Core Intelligence, Adaptive Routing & Engineering Economy (Complete)
- [x] Level 0/1 operating kernel in [SKILL.md](../SKILL.md), 4 core Level 2 modules, consolidated [capability-registry.json](capability-registry.json), and [core-intelligence.json](../evals/core-intelligence.json).

## Phase 03 — Advanced Design Intelligence & Visual Craftsmanship (Complete)
- [x] 6 Level 2 design modules, design routing integration, [design-intelligence.json](../evals/design-intelligence.json), and `supplementary_design_rubric`.

## Phase 04 — Advanced Frontend Engineering, Motion & Interaction Intelligence (Complete)
- [x] 5 Level 2 engineering/motion/a11y/perf modules, engineering routing integration, [engineering-intelligence.json](../evals/engineering-intelligence.json), and `supplementary_engineering_rubric`.

## Phase 05 — Critique, Verification, Quality Assurance & Self-Correction (Complete)
- [x] Authored [visual-critique.md](../references/visual-critique.md) and [functional-and-technical-audits.md](../references/functional-and-technical-audits.md), upgraded [verification-and-refinement.md](../references/verification-and-refinement.md) with the 6-level evidence hierarchy, 5 severity levels, and 9 mandatory quality gates.
- [x] Upgraded `FF-VF-01` in [capability-registry.json](capability-registry.json), created [verification-intelligence.json](../evals/verification-intelligence.json), and extended [rubric.json](../evals/rubric.json).

## Phase 06 — Deep Skill & Context Optimization
- Audit and compress token budgets, eliminate redundant cross-module prose, and refine routing precision.

## Phase 07 — Comparative Benchmarking, Ablation & Regression Evaluation
- Execute live-agent, rendered-browser, and ablation evaluations across all `evals/` suites.

## Phase 08 — Packaging & Release
- Finalize distributable skill packaging, release verification, and documentation.

---

## Open Uncertainties & Assumptions
- **Live-agent & browser execution**: Structural/referential checks pass, but [core-intelligence.json](../evals/core-intelligence.json), [design-intelligence.json](../evals/design-intelligence.json), [engineering-intelligence.json](../evals/engineering-intelligence.json), [verification-intelligence.json](../evals/verification-intelligence.json), and [tasks.json](../evals/tasks.json) have not yet been executed against live agent or browser runs.
- **Token counts**: Reported token counts are word-based estimates (`words * 1.33`), not tokenizer-exact measurements.
