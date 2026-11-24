# FORMFORGE Architecture

## 1. Design Principles

FORMFORGE is a portable, zero-dependency, Markdown-first Agent Skill (`agentskills.io`). It avoids custom CLIs, databases, knowledge graphs, and scripting runtimes, relying on standard Markdown, JSON, and the host agent's native tools.

**Single Authoritative Source**: Global constraints (priority ladder, code/tool economy, quality floor, honesty gates) live in [SKILL.md](../SKILL.md); verification/degradation rules live in [verification-and-refinement.md](../references/verification-and-refinement.md); domain modules state only specialized rules and exceptions.

---

## 2. Progressive Context Architecture (Levels 0–4)

| Level | Artifact | Loading Behavior |
| :--- | :--- | :--- |
| **Level 0 — Discovery** | `SKILL.md` YAML frontmatter | Always in agent index |
| **Level 1 — Kernel** | `SKILL.md` Markdown body | Loaded on skill activation |
| **Level 2 — Domain Modules** | 19 focused `references/*.md` files (including `planning-mode.md` & `master-prompt-spec.md`) | Loaded selectively by user intent, never by keyword alone |
| **Native Command Dispatchers** | `.claude/commands/`, `.cursor/commands/`, `.gemini/commands/`, `.windsurf/workflows/` | Thin 9-command dispatchers pointing to `SKILL.md` + `references/` |
| **Level 4 — Verification Tools** | Host browser/test/lint/a11y tools | Invoked when task risk justifies them |

### Experimental Context Targets (Kernel + Loaded References)
- `QUICK`: ~800–2,000 est. tokens
- `STANDARD`: ~2,000–4,500 est. tokens
- `PREMIUM`: ~4,000–8,000 est. tokens
- `FLAGSHIP`: ~7,000–12,000 est. tokens

Targets are hypotheses, not rigid caps—expand context whenever accessibility, security, or complex requirements demand it.

---

## 3. Package Boundaries & Portability

- **Production skill** (`SKILL.md`, `references/`, `LICENSE`): Self-contained, portable across compatible coding agents, and free of external runtime dependencies or `docs/`/`evals/` coupling.
- **Project documentation** (`docs/`) and **Evaluations** (`evals/`): Maintained for contributors and benchmarking; not required at runtime.
- **Platform-independent instructions**: Capabilities describe required outcomes (e.g., "inspect rendered output using available browser tools") rather than hard-coding a single host tool or OS.
