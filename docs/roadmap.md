# FORMFORGE Implementation Roadmap

## Phase 01 — Foundation, Research & Architecture (Current)

- [x] Initialize `formforge/phase-01-foundation` branch and repository hygiene (`.gitignore`, `LICENSE`).
- [x] Author portable Level 0/1 operating kernel in [SKILL.md](../SKILL.md).
- [x] Define progressive context, adaptive modes, conflict resolution, and economy rules in [architecture.md](architecture.md).
- [x] Establish the 10-domain unified capability registry in [capability-registry.json](capability-registry.json).
- [x] Define 12 benchmark tasks and the 100-point quality + 12-metric efficiency rubric in [tasks.json](../evals/tasks.json) and [rubric.json](../evals/rubric.json).
- [x] Add zero-dependency structural validator in [validate_foundation.py](../scripts/validate_foundation.py).

---

## Phase 02 — Core Level 2 Capability Modules

Build focused, non-overlapping `references/*.md` modules loaded selectively by task route, ordered by impact:

1. **Creative Direction & Visual Design (`references/creative-direction.md`, `references/visual-design.md`)**
   - Product-grounded brief template, contextual anti-generic review, unified typography engine, semantic color contrast rules, grid/density guidance.
2. **UX Intelligence (`references/ux-intelligence.md`)**
   - Task-based navigation, active microcopy rules, resilient async states (loading/empty/error/success), form ergonomics, mobile-first touch standards.
3. **Frontend Engineering & Components (`references/engineering.md`, `references/components.md`)**
   - Stack detection, reuse-first component discovery, accessible interactive primitives, state derivation, bundle/Core Web Vitals discipline, client security.
4. **Design Systems (`references/design-systems.md`)**
   - Semantic token architecture, light/dark parity, minimal token budgets.
5. **Motion Intelligence (`references/motion.md`)**
   - Purposeful motion hierarchy, timing/easing curves, GPU-composited transitions, interruptibility, `prefers-reduced-motion` compliance.
6. **Verification Intelligence (`references/verification.md`)**
   - Rendered visual critique checklist, keyboard/a11y gate protocol, bounded refinement stopping rules.

---

## Phase 03 — Specialized Intelligence, Design Memory & Baseline Evals

- Author compact Level 3 product-domain profiles (SaaS, fintech, e-commerce, AI-native apps, portfolios, mobile-first).
- Define a lightweight persistent project design memory convention for multi-session continuity.
- Execute initial baseline runs across `evals/tasks.json` against real rendered outputs to establish empirical quality and token baselines.

---

## Phase 04 — Automated Verification & Evidence-Driven Optimization

- Add Level 4 executable browser/a11y/layout verification scripts (`scripts/`) that run out-of-context.
- Compare FORMFORGE against unassisted and baseline runs using blind rendered scoring and efficiency metrics.
- Prune or compress any instruction modules that do not measurably improve quality per unit of context.

---

## Open Uncertainties & Assumptions

- **Triggering recall across agents**: `SKILL.md` frontmatter description has not yet been tested across multiple agent runtimes for under-triggering or false-positive triggering.
- **Optimal Level 2 module size**: Target budgets (~1.5–3KB per reference file) are architectural hypotheses pending Phase 03 token-efficiency measurements.
- **Empirical quality/token lift**: No benchmark runs have been executed yet in Phase 01; all capability effectiveness claims remain hypotheses until Phase 03/04 rendered evaluations complete.
