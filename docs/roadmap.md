# FORMFORGE Implementation Roadmap

## Phase 01 — Foundation, Research & Architecture (Complete)

- [x] Established portable `agentskills.io` structure, `.gitignore`, `LICENSE`, and `README.md`.
- [x] Defined 10-domain capability model, 100-point quality rubric, and 12-category frontend eval suite.

## Phase 02 — Core Intelligence, Adaptive Routing & Engineering Economy (Complete)

- [x] Refined Level 0/1 operating kernel in [SKILL.md](../SKILL.md) with positive/negative activation boundaries and 5-dimension task classification.
- [x] Authored 4 focused Level 2 core modules: [routing-and-modes.md](../references/routing-and-modes.md), [implementation-economy.md](../references/implementation-economy.md), [project-and-memory.md](../references/project-and-memory.md), and [verification-and-refinement.md](../references/verification-and-refinement.md).
- [x] Consolidated [capability-registry.json](capability-registry.json) to 30 entries with explicit `IMPLEMENTED` / `PLANNED` / `DEFERRED` / `REJECTED` statuses and valid `reference_paths`.
- [x] Added 23-case core intelligence evaluation suite in [core-intelligence.json](../evals/core-intelligence.json) and removed the Phase 01 Python script to keep the skill dependency-free.

## Phase 03 — Specialized Design & Engineering Modules

Author Level 2/3 domain modules in `references/` in priority order:
1. Creative direction & visual design (product-grounded briefs, typography, color contrast, grids, anti-generic judgment).
2. UX intelligence (information architecture, active microcopy, resilient async states, forms, mobile ergonomics).
3. Frontend engineering & accessible components (semantic HTML, modern CSS, keyboard/ARIA primitives, bundle/CWV hygiene).
4. Design systems (semantic tokens, light/dark parity).
5. Motion intelligence (purposeful curves, GPU-composited transitions, reduced-motion compliance).
6. Product-domain profiles & initial live-agent baseline evaluations across [core-intelligence.json](../evals/core-intelligence.json) and [tasks.json](../evals/tasks.json).

## Phase 04 — Automated Verification & Evidence-Driven Pruning

- Integrate browser/accessibility/performance verification probes (Level 4) where supported.
- Run blind rendered comparisons and prune any instructions that do not measurably improve quality per unit of context.

---

## Open Uncertainties & Assumptions

- **Live-agent execution**: Neither [core-intelligence.json](../evals/core-intelligence.json) nor [tasks.json](../evals/tasks.json) has been executed against live agent runs yet; Phase 02 verification covers structural/referential integrity only.
- **Token counts**: Reported token counts are word-based estimates (`words * 1.33`), not tokenizer-exact measurements.
- **Experimental context budgets**: Mode token targets (`1.5k–3k` through `10k–15k`) remain hypotheses until Phase 03 empirical runs.
