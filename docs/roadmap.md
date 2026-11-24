# FORMFORGE Roadmap

## Completed Phases
- **Phase 01 — Foundation**: `agentskills.io` structure, 10-domain capability model, 100-point rubric, 12 benchmark tasks.
- **Phase 02 — Core Intelligence**: Operating kernel, 5-dimension classification, adaptive modes, economy/memory rules, 23 core evals.
- **Phase 03 — Design Intelligence**: 6 design modules, 14 design evals.
- **Phase 04 — Engineering & Motion**: 5 engineering/motion/a11y/perf modules, 14 engineering evals.
- **Phase 05 — Verification & QA**: 6-level evidence hierarchy, multi-scale critique, functional/technical audits, 9 quality gates, 11 verification evals.
- **Phase 06 — Deep Optimization**: Kernel & reference compression (`-31.7%` total instruction words), single-authoritative-source deduplication, 10 optimization evals.

## Phase 07 — Comparative Benchmarking & Ablation Testing (Partially Complete)
- [x] Authored [protocol.md](../evals/protocol.md), [benchmarks.json](../evals/benchmarks.json) (32 tasks, 3 holdouts, 10 ablations, 6 interaction pairs), and Stage A structural/context-simulation [results.json](../evals/results.json).
- [ ] Execute Stage B–F live-agent, rendered-browser, and ablation trials when authorized execution budget and browser/model telemetry are available.

## Phase 08 — Final Integration, Production Hardening & Installation (Complete)
- [x] Decoupled production skill (`SKILL.md` + `references/` + `LICENSE`) from `docs/`, added untrusted-content security hardening, removed leftover development-phase phrasing, finalized [README.md](../README.md), and verified clean isolated installation packaging.

---

## Release Readiness & Open Limitations
- **Current Readiness**: **`EXPERIMENTAL`** — All structural, link, schema, security, licensing, and clean-install checks pass, and `B1`/`B2`/`B3` corpus & simulated context deltas are measured/estimated, while live-agent, rendered-browser, cost, and ablation executions (`Stages B–F`) remain `NOT EXECUTED`.
