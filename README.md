# FORMFORGE

**Maximum taste. Minimum waste.**

FORMFORGE is a portable, modular AI agent skill for frontend design and engineering. It pairs product-grounded creative direction, visual craft, UX rigor, and purposeful motion with strict code, context, and verification economy.

## Core Principles

- **Taste over templates**: Visual and structural choices derive from the product's actual domain, audience, and job—never generic card-kit defaults or rigid aesthetic bans.
- **Economy without compromise**: Follow a strict code decision ladder (existing project code -> native HTML/CSS -> browser APIs -> installed packages -> minimal custom code) while protecting correctness, accessibility, and security as non-negotiable gates.
- **Progressive context loading**: Keep the core kernel (`SKILL.md`) concise and load domain guidance only when a task route requires it.
- **Adaptive execution modes**: Scale ceremony to risk (`QUICK`, `STANDARD`, `PREMIUM`, `FLAGSHIP`).
- **Evidence-driven verification**: Never claim visual or functional quality without inspecting actual rendered output and running targeted checks.

## Repository Layout

```text
FORMFORGE/
├── SKILL.md                      # Level 0 discovery + Level 1 core operating kernel
├── README.md                     # Project overview
├── LICENSE                       # MIT License
├── docs/
│   ├── architecture.md           # Progressive context, modes, routing, conflict & economy policies
│   ├── capability-registry.json  # Unified 10-domain capability registry (40 evaluated entries)
│   └── roadmap.md                # Phased implementation plan & open assumptions
├── evals/
│   ├── tasks.json                # 12 benchmark tasks across core frontend categories
│   └── rubric.json               # 100-point quality rubric, 3 mandatory gates, 12 efficiency metrics
└── scripts/
    └── validate_foundation.py    # Zero-dependency Phase 01 structural & consistency validator
```

## Validation

Run the Phase 01 foundation validator with Python 3.10+:

```bash
python scripts/validate_foundation.py
```

## Roadmap

- **Phase 01 (Current)**: Core kernel, architecture, capability registry, evaluation suite, and structural validator.
- **Phase 02**: Focused Level 2 `references/` modules for creative direction, visual design, UX, components, engineering, design systems, motion, and verification.
- **Phase 03**: Product-domain profiles, persistent project design memory, and initial rendered baseline evaluations.
- **Phase 04**: Automated Level 4 browser/accessibility verification scripts and evidence-driven instruction pruning.

See [docs/roadmap.md](docs/roadmap.md) for details.
