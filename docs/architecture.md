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
| **Level 2 — Domain Modules** | 17 focused `references/*.md` files | Loaded selectively by user intent, never by keyword alone |
| **Level 4 — Verification Tools** | Host browser/test/lint/a11y tools | Invoked when task risk justifies them |

### Experimental Context Targets (Kernel + Loaded References)
- `QUICK`: ~800–2,000 est. tokens
- `STANDARD`: ~2,000–4,500 est. tokens
- `PREMIUM`: ~4,000–8,000 est. tokens
- `FLAGSHIP`: ~7,000–12,000 est. tokens

Targets are hypotheses, not rigid caps—expand context whenever accessibility, security, or complex requirements demand it.
