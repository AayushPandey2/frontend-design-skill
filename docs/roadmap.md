# FORMFORGE Roadmap

## Completed Phases
- **Phase 01 — Foundation**: `agentskills.io` structure, 10-domain capability model, 100-point rubric, 12 benchmark tasks.
- **Phase 02 — Core Intelligence**: Operating kernel, 5-dimension classification, adaptive modes, economy/memory rules, 23 core evals.
- **Phase 03 — Design Intelligence**: 6 design modules (creative direction, typography/copy, color/surfaces, layout/density, UX/systems, industry patterns), 14 design evals.
- **Phase 04 — Engineering & Motion**: 5 engineering/motion/a11y/perf modules, 14 engineering evals.
- **Phase 05 — Verification & QA**: 6-level evidence hierarchy, multi-scale critique, functional/technical audits, 9 quality gates, 11 verification evals.
- **Phase 06 — Deep Optimization**: Kernel & reference compression, single-authoritative-source deduplication, intent-over-keyword routing, updated context budgets, and [optimization-intelligence.json](../evals/optimization-intelligence.json).

## Phase 07 — Comparative Benchmarking & Ablation Testing
Execute live-agent, rendered-browser, and controlled ablation runs via Git history (no feature-flag bloat) across 9 ablation groups:
1. Operating kernel compression (`c3165d1` vs. Phase 06)
2. Reference deduplication
3. Intent-based routing optimization
4. Experimental context budget tuning
5. Persistent design memory simplification
6. Code economy reinforcement
7. Verification & screenshot economy
8. Bounded refinement & stopping conditions
9. Documentation cleanup

## Phase 08 — Packaging & Release
- Finalize distributable packaging and release verification.

---

## Open Uncertainties & Limitations
- **Live-agent & browser execution**: Deterministic structural/referential checks pass, but live-agent token telemetry, tool-call counts, rendered UI quality, and ablation comparisons remain unexecuted until Phase 07.
- **Token counts**: Reported token counts are word-based estimates (`words * 1.33`), not exact tokenizer counts.
