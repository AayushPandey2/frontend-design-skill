# FORMFORGE

**Maximum taste. Minimum waste.**

FORMFORGE is a portable, zero-dependency AI agent skill for frontend design, engineering, and quality assurance. It pairs product-grounded design judgment, modern frontend engineering, purposeful motion, and evidence-gated verification with strict code, context, and tool-call economy.

## Structure

```text
FORMFORGE/
├── SKILL.md                           # Level 0 discovery + Level 1 kernel & routing index
├── README.md                          # Project overview
├── LICENSE                            # MIT License
├── references/                        # 17 selective Level 2 core, design, engineering & QA modules
├── docs/
│   ├── architecture.md                # Progressive context, single-source rules & budgets
│   ├── capability-registry.json       # Unified 10-domain registry (30 entries)
│   └── roadmap.md                     # Phases 01–08 & release readiness
└── evals/
    ├── protocol.md                    # Controlled benchmark, blind eval & ablation protocol
    ├── benchmarks.json                # 32 tasks, 3 holdouts, 10 ablations, 6 interactions
    ├── results.json                   # Stage A structural & B1/B2/B3 context-simulation results
    ├── core-intelligence.json         # 23 core intelligence cases
    ├── design-intelligence.json       # 14 design intelligence cases
    ├── engineering-intelligence.json  # 14 engineering intelligence cases
    ├── verification-intelligence.json # 11 verification intelligence cases
    ├── optimization-intelligence.json # 10 optimization & anti-over-optimization cases
    ├── tasks.json                     # 12 end-to-end frontend benchmark tasks
    └── rubric.json                    # 100-pt global + supplementary rubrics & severity taxonomy
```

## Readiness & Limitations

Current release readiness: **`EXPERIMENTAL`**. Deterministic structural checks and `B1`/`B2`/`B3` instruction/context-simulation comparisons pass in [evals/results.json](evals/results.json); live-agent, rendered-browser, cost, and ablation trials remain unexecuted (see [docs/roadmap.md](docs/roadmap.md)).
