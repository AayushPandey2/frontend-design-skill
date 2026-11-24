# FORMFORGE Architecture Specification

## 1. Design Goals & Architectural Economy

FORMFORGE is a portable, file-based Agent Skill compliant with the `agentskills.io` specification. Every architectural choice adheres to **architectural economy**:

- **Zero runtime dependencies**: No custom CLI, database, knowledge graph, or scripting runtime is required.
- **Zero speculative infrastructure**: Modules and evaluations exist only when a concrete capability or measurement need justifies their maintenance and context cost.
- **Portable knowledge**: Standard Markdown and JSON ensure consistent execution across compatible coding agents.

---

## 2. Progressive Context Architecture (Levels 0–4)

| Level | Artifact / Scope | Context Behavior | Status |
| :--- | :--- | :--- | :--- |
| **Level 0 — Discovery** | `SKILL.md` YAML frontmatter (`name`, `description`) | Always in agent index | Operational (Phase 01–02) |
| **Level 1 — Core Kernel** | `SKILL.md` Markdown body | Loaded on skill activation (target ~1k–2k est. tokens) | Operational (Phase 02) |
| **Level 2 — Core Intelligence** | `references/routing-and-modes.md`, `implementation-economy.md`, `project-and-memory.md`, `verification-and-refinement.md` | Loaded selectively by task route | Operational (Phase 02) |
| **Level 2 — Design Intelligence** | `references/creative-direction.md`, `typography-and-content.md`, `color-and-surfaces.md`, `layout-and-responsive.md`, `ux-and-systems.md`, `industry-patterns.md` | Loaded selectively by design route | Operational (Phase 03) |
| **Level 2 — Engineering & Motion** | `references/html-css-responsive.md`, `components-and-frameworks.md`, `motion-and-interactions.md`, `accessibility-engineering.md`, `performance-and-reliability.md` | Loaded selectively by engineering route | Operational (Phase 04) |
| **Level 2 — Verification & QA** | `references/visual-critique.md`, `functional-and-technical-audits.md`, `verification-and-refinement.md` | Loaded selectively by risk & audit scope | Operational (Phase 05) |
| **Level 4 — Executable Probes** | Existing browser/a11y/perf tools | Invoked via agent tools when supported | Integrated via instructions (Phase 05) |

### Experimental Context Targets (Kernel + Loaded References)
- `QUICK`: ~1,500–3,000 estimated tokens
- `STANDARD`: ~3,000–6,000 estimated tokens
- `PREMIUM`: ~6,000–10,000 estimated tokens
- `FLAGSHIP`: ~10,000–15,000 estimated tokens

These are experimental optimization targets, not rigid limits; expand context when essential requirements demand it.

---

## 3. Adaptive Execution & Refinement Budgets

FORMFORGE classifies tasks across **5 dimensions** (task type, scope, complexity, risk, user intent) and selects the lightest sufficient mode (`QUICK`, `STANDARD`, `PREMIUM`, `FLAGSHIP`):

- **`QUICK`**: Targeted fix + verification only; no design brief, no design memory, no unrelated refactoring.
- **`STANDARD`**: Up to 2 bounded refinement passes; preserves or sets design direction and verifies affected flows.
- **`PREMIUM`**: Up to 3 bounded refinement passes; includes product brief, tokens, and rendered visual critique when supported.
- **`FLAGSHIP`**: Up to 5 bounded refinement passes when justified; activates only capabilities the experience actually requires.

Modes escalate when hidden complexity or risk appears and de-escalate when existing components/tokens already solve the task.

---

## 4. Conflict Resolution & Graceful Degradation

Conflicts follow the 10-level priority ladder in [SKILL.md](../SKILL.md):
- Existing design systems and authoritative code override new creative preferences unless a redesign is explicitly requested.
- Accessibility, functional correctness, and security always override code/token economy.
- Explicit user aesthetic requests override anti-generic heuristics.
- When browser tools, tests, references, or token telemetry are unavailable, FORMFORGE degrades gracefully, uses the best static/build alternative, and reports unverified dimensions honestly without fabricating evidence.
