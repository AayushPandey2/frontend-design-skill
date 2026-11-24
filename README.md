# FORMFORGE

**Maximum taste. Minimum waste.**

FORMFORGE is a portable, zero-dependency AI agent skill for frontend design, engineering, and quality assurance. It combines product-grounded design intelligence, modern frontend engineering, purposeful motion, and evidence-gated verification with strict code, context, and tool-call economy.

## Why FORMFORGE

AI-generated frontends frequently suffer from generic card-kit layouts, weak typographic hierarchy, redundant state/effects, unnecessary dependencies, incomplete interaction states, and unverified visual or accessibility claims. FORMFORGE addresses these through:
- **Intentional design judgment** grounded in product subject, audience, and density—without rigid aesthetic blacklists.
- **Native-first implementation economy** that reuses existing project code, HTML/CSS, and browser APIs before introducing abstractions or packages.
- **Selective context loading** so trivial fixes load minimal guidance while complex builds retrieve specialized modules on demand.
- **Evidence-gated verification** that separates static inspection from rendered/behavioral proof and stops once quality gates pass.

## Core Capabilities

- **Core & Routing** ([SKILL.md](SKILL.md)): 5-dimension task classification, adaptive modes (`QUICK`, `STANDARD`, `PREMIUM`, `FLAGSHIP`), 10-level conflict ladder, and progressive Level 2 routing.
- **Design Intelligence**: Product-grounded creative direction, anti-generic judgment, typography & active microcopy, semantic color & non-inverted dark mode, layout/density, UX journeys/states, and 10 product-domain profiles.
- **Engineering & Motion**: Semantic HTML, modern CSS & responsive sizing, component reuse, React/framework state discipline, CWV/asset/security hygiene, WCAG 2.2 AA engineering, and interruptible GPU-composited motion.
- **Verification & QA**: 6-level evidence hierarchy, multi-scale visual critique, functional/responsive/a11y/waste audits, 5-level defect severity, root-cause remediation, and graceful degradation.

## Package Boundaries

- **Production Skill (Installable)**: [SKILL.md](SKILL.md), `references/` (17 modules), and [LICENSE](LICENSE). Self-contained with zero runtime dependencies and no Python/Node scripts required.
- **Project Documentation**: `docs/` ([architecture.md](docs/architecture.md), [capability-registry.json](docs/capability-registry.json)).
- **Evaluation Suite**: `evals/` ([protocol.md](evals/protocol.md), [benchmarks.json](evals/benchmarks.json), [results.json](evals/results.json), [rubric.json](evals/rubric.json), and 6 task/intelligence fixtures).

## Installation

Clone the repository and copy only the **production skill** (`SKILL.md`, `references/`, and `LICENSE`) into a directory named `formforge/` inside your coding agent's skills folder:

```bash
git clone https://github.com/AayushPandey2/frontend-design-skill.git
```

- **Project-level or user-level placement**: Place `SKILL.md`, `references/`, and `LICENSE` under `<your-agent-skills-dir>/formforge/` (for example, `.agents/skills/formforge/` or `~/.gemini/config/skills/formforge/` depending on your host agent's documented skills path).
- **Activate**: Use natural-language frontend prompts; no custom CLI or configuration file is required.
- **Verify installation**: Confirm `formforge/SKILL.md` is discovered by your agent and that relative links to `references/*.md` exist in the same `formforge/` folder.
- **Remove**: Delete the `formforge/` skill folder.

*Note: Isolated clean-directory packaging and relative link resolution have been verified locally; host-specific auto-discovery across individual third-party agent CLIs has not been live-tested.*

## Usage Examples

- *"Build a premium editorial landing page for an architectural lighting brand."* (`PREMIUM`)
- *"Create a financial analytics dashboard with tabular numerals, filtering, and responsive charts."* (`PREMIUM`)
- *"Redesign this existing SaaS settings page while preserving our design tokens and components."* (`STANDARD`)
- *"Create a distinctive interactive portfolio with purposeful, reduced-motion-safe transitions."* (`FLAGSHIP`)
- *"Fix the keyboard navigation and Escape dismissal in this modal without changing its visual style."* (`STANDARD`)
- *"Fix horizontal mobile overflow in this pricing grid at 320px and 375px."* (`QUICK`)
- *"Remove unnecessary React state and useEffect synchronization while preserving behavior."* (`QUICK`)
- *"Audit this frontend for visual hierarchy, accessibility, and engineering-waste defects—don't edit yet."* (Review-only)
- *"Change the primary button label and padding without modifying unrelated files."* (`QUICK`)

## How It Works

1. **Classify**: Evaluate task type, scope, complexity, risk, and user intent.
2. **Route**: Select the lightest sufficient mode (`QUICK`–`FLAGSHIP`) and load only intent-matched `references/*.md` modules.
3. **Implement**: Follow the 6-step code economy ladder while preserving correctness, accessibility, and security.
4. **Verify & Refine**: Check rendered/behavioral outcomes where tools allow, fix root causes within mode budgets, and report unverified items honestly.

## Evaluation & Limitations

- **Current Readiness**: **`EXPERIMENTAL`**.
- **Verified**: Deterministic structural, metadata, link, JSON schema, and clean-install checks pass across all 34 files (`0` Python files, `0` runtime dependencies). Corpus word-count and simulated per-task context comparisons (`B1` -> `B2` -> `B3`) are recorded in [evals/results.json](evals/results.json).
- **Limitations**: Live-agent execution, rendered browser/screenshot scoring, provider token/cost telemetry, and ablation trials (`Stages B–F` in [evals/protocol.md](evals/protocol.md)) have **not yet been executed**.

## Compatibility

| Target | Status | Basis |
| :--- | :--- | :--- |
| **`agentskills.io` Specification** | Structurally Verified | Valid `SKILL.md` frontmatter + progressive `references/` layout |
| **Claude Code, OpenAI Codex, Cursor, Gemini CLI, GitHub Copilot, Windsurf, OpenCode** | Documented / Untested | Portable Markdown + JSON skill format; live host discovery not executed in this session |

## License

MIT License — see [LICENSE](LICENSE).
