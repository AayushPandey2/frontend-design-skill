# FORMFORGE

**Maximum taste. Minimum waste.**

FORMFORGE is a portable, zero-dependency AI agent skill for frontend design and engineering. It combines adaptive task classification, progressive context loading, strict implementation economy, project/design-memory awareness, and bounded evidence-driven verification.

## Core Capabilities (Phase 02)

- **Lightweight Operating Kernel** ([SKILL.md](SKILL.md)): Clear activation boundaries, 5-dimension task classification, 10-level conflict priority ladder, and 6-step code economy ladder.
- **Adaptive Modes & Routing** ([references/routing-and-modes.md](references/routing-and-modes.md)): Auto-selects `QUICK`, `STANDARD`, `PREMIUM`, or `FLAGSHIP` based on scope and risk, loading only task-relevant guidance.
- **Implementation & Tool Economy** ([references/implementation-economy.md](references/implementation-economy.md)): Prefers existing project code and native HTML/CSS/Browser APIs over unnecessary JS, wrappers, or dependencies.
- **Project Awareness & Design Memory** ([references/project-and-memory.md](references/project-and-memory.md)): Preserves existing frameworks and tokens while maintaining concise, non-duplicative cross-session design decisions.
- **Verification & Graceful Degradation** ([references/verification-and-refinement.md](references/verification-and-refinement.md)): Risk-scaled checks, bounded refinement loops, and honest fallback reporting when browser or test tools are unavailable.

## Repository Layout

```text
FORMFORGE/
├── SKILL.md                           # Level 0 discovery + Level 1 core operating kernel
├── README.md                          # Project overview
├── LICENSE                            # MIT License
├── references/
│   ├── routing-and-modes.md           # 5-dimension classification, modes, routing examples
│   ├── implementation-economy.md      # Code/CSS/editing/tool economy rules
│   ├── project-and-memory.md          # Stack detection, dependency checks, design memory
│   └── verification-and-refinement.md # Risk-based checks, bounded loops, degradation
├── docs/
│   ├── architecture.md                # Progressive context, budgets, conflict & degradation model
│   ├── capability-registry.json       # Unified 10-domain registry (30 entries)
│   └── roadmap.md                     # Phased plan & open uncertainties
└── evals/
    ├── core-intelligence.json         # 23 core intelligence test cases (9 categories)
    ├── tasks.json                     # 12 frontend benchmark tasks
    └── rubric.json                    # 100-point rubric, 3 mandatory gates, 12 efficiency metrics
```

See [docs/roadmap.md](docs/roadmap.md) for Phase 03–04 plans and open uncertainties.
