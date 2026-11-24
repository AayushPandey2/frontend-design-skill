# FORMFORGE

**Maximum taste. Minimum waste.**

FORMFORGE is a portable, zero-dependency AI agent skill for frontend design, interactive consultation, engineering, and quality assurance. It pairs product-grounded design judgment, modern frontend engineering, purposeful motion, and evidence-gated verification with strict code, context, and tool-call economy.

## Why FORMFORGE

AI-generated frontends frequently suffer from generic card-kit layouts, weak typographic hierarchy, redundant state/effects, unnecessary dependencies, incomplete interaction states, and unverified visual or accessibility claims. FORMFORGE addresses these through:
- **Intentional design judgment** grounded in product subject, audience, and density—without rigid aesthetic blacklists.
- **Interactive pre-code consultation** (`/formforge-plan`) that turns vague ideas and visual references into a standalone, copyable master implementation prompt.
- **Native-first implementation economy** that reuses existing project code, HTML/CSS, and browser APIs before introducing abstractions or packages.
- **Selective context loading** so trivial fixes load minimal guidance while complex builds retrieve specialized modules on demand.
- **Evidence-gated verification** that separates static inspection from rendered/behavioral proof and stops once quality gates pass.

## Standalone Slash Commands

Type `/` in supported editors or use natural-language equivalents where native slash commands are unsupported:

| Command | Mode / Role | Edits Code? | Natural-Language Fallback |
| :--- | :--- | :---: | :--- |
| `/formforge` | Auto-select mode (`QUICK`–`FLAGSHIP`) | Yes | *"Use FORMFORGE to build..."* |
| `/formforge-quick` | Targeted, low-risk edits (`QUICK`) | Yes | *"FORMFORGE quick fix..."* |
| `/formforge-standard` | Ordinary frontend development (`STANDARD`) | Yes | *"FORMFORGE standard build..."* |
| `/formforge-premium` | High-craft UI/UX development (`PREMIUM`) | Yes | *"FORMFORGE premium design..."* |
| `/formforge-flagship` | Ambitious interactive experiences (`FLAGSHIP`) | Yes | *"FORMFORGE flagship experience..."* |
| `/formforge-audit` | Comprehensive visual, functional, a11y & waste audit | **No (Read-only)** | *"FORMFORGE, audit this frontend"* |
| `/formforge-polish` | Visual hierarchy, typography, spacing & surface refinement | Yes | *"FORMFORGE, polish this UI"* |
| `/formforge-optimize` | Code, bundle, rendering & CWV optimization | Yes | *"FORMFORGE, optimize this frontend"* |
| `/formforge-plan` | Interactive design consultation -> master prompt | **No (Read-only)** | *"FORMFORGE, plan my website"* |

## Interactive Design Planning Mode (`/formforge-plan`)

`/formforge-plan` enters a strict **read-only design consultation studio** (`Discover -> Explore -> Compare -> Select -> Specify -> Confirm -> Consolidate -> Generate`). It adapts across `Express`, `Guided`, and `Exhaustive` depths, retrieves real web visual references when browsing is available, records `LOCKED`/`PREFERRED`/`FLEXIBLE`/`REJECTED`/`UNRESOLVED` decisions, defines measurable Motion Specification Contracts, and outputs:
1. A compact **Final Design Summary**
2. A **Standalone Copyable Master Implementation Prompt** (usable in a fresh agent session with or without FORMFORGE)
3. An optional **Reference & Asset Index**

## Package Boundaries

- **Production Skill (Installable)**: [SKILL.md](SKILL.md), `references/` (19 modules), and [LICENSE](LICENSE).
- **Native Slash Command Dispatchers**: `.claude/commands/` (`.md`), `.cursor/commands/` (`.md`), `.gemini/commands/` (`.toml`), and `.windsurf/workflows/` (`.md`) — 9 thin dispatchers per platform.
- **Project Documentation & Evals**: `docs/` ([architecture.md](docs/architecture.md), [capability-registry.json](docs/capability-registry.json)) and `evals/` (including [planning-mode.json](evals/planning-mode.json)).

## Installation

```bash
git clone https://github.com/AayushPandey2/frontend-design-skill.git
```

- **Skill installation**: Copy `SKILL.md`, `references/`, and `LICENSE` into `<your-agent-skills-dir>/formforge/` (e.g., `.agents/skills/formforge/` or `~/.gemini/config/skills/formforge/`).
- **Native slash commands**: Copy the matching command directory into your project or user config (`.claude/commands/`, `.cursor/commands/`, `.gemini/commands/`, or `.windsurf/workflows/`). Where native slash commands are unsupported, invoke FORMFORGE via natural language.
- **Remove**: Delete the `formforge/` skill folder and the `formforge*` command files.

*Note: Clean-directory skill packaging, TOML/YAML command syntax, and internal links are structurally verified; third-party host CLI auto-discovery has not been live-tested.*

## Usage Examples

- *"/formforge-plan Create a premium website for a luxury watch brand."* (`PLAN`, read-only)
- *"/formforge-premium Build an editorial landing page for an architectural lighting studio."* (`PREMIUM`)
- *"/formforge-standard Add a filterable billing table reusing our existing Table and Button."* (`STANDARD`)
- *"/formforge-flagship Build an interactive portfolio with purposeful, reduced-motion-safe transitions."* (`FLAGSHIP`)
- *"/formforge-audit Review our checkout flow for accessibility, responsive overflow, and dead controls."* (`AUDIT`, read-only)
- *"/formforge-polish Fix the competing nav hierarchy and inconsistent card spacing."* (`POLISH`)
- *"/formforge-optimize Remove redundant React state/effects and oversized icon imports."* (`OPTIMIZE`)
- *"/formforge-quick Update the Save button label without modifying unrelated files."* (`QUICK`)

## Evaluation & Limitations

- **Current Readiness**: **`EXPERIMENTAL`**. Deterministic structural, metadata, link, JSON schema, and clean-install checks pass (`0` Python files, `0` runtime dependencies). Corpus and simulated context comparisons are recorded in [evals/results.json](evals/results.json).
- **Limitations**: Live-agent execution, rendered browser scoring, fresh-session prompt reconstruction tests, and third-party host slash-command auto-discovery remain **unexecuted**.

## Compatibility

| Target | Status | Basis |
| :--- | :--- | :--- |
| **`agentskills.io` Specification** | Structurally Verified | Valid `SKILL.md` frontmatter + progressive `references/` layout |
| **Claude Code, Cursor, Gemini CLI, Windsurf** | Structurally Verified / Host Untested | Native `.claude/commands/`, `.cursor/commands/`, `.gemini/commands/`, `.windsurf/workflows/` files provided; host discovery untested |
| **OpenAI Codex, GitHub Copilot, OpenCode** | Documented / Untested | Portable `SKILL.md` + natural-language command fallbacks |

## License

MIT License — see [LICENSE](LICENSE).
