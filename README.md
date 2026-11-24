# FORMFORGE

**Maximum taste. Minimum waste.**

FORMFORGE is a portable, zero-dependency AI agent skill ecosystem (25 individually discoverable `/formforge*` skills) for frontend design, interactive consultation, visual replication, Design DNA, motion, accessibility, engineering, and quality assurance.

## Why FORMFORGE

AI-generated frontends frequently suffer from generic card-kit layouts, weak typographic hierarchy, redundant state/effects, unnecessary dependencies, incomplete interaction states, and unverified visual or accessibility claims. FORMFORGE addresses these through:
- **25 focused skills over one monolith**: Invoke `/formforge` for auto-selected execution or target a specialized skill (`/formforge-plan`, `/formforge-reference`, `/formforge-replicate`, `/formforge-dna`, `/formforge-motion`, `/formforge-fidelity`, etc.).
- **Single authoritative intelligence**: All 25 skills route into one shared core kernel ([SKILL.md](SKILL.md)) and 23 modular `references/*.md` files—zero duplicated instructions.
- **Native-first implementation economy**: Reuses existing project code, HTML/CSS, and browser APIs before introducing abstractions or packages.
- **Evidence-gated verification**: Separates static inspection from rendered/behavioral proof and design-contract fidelity (`/formforge-verify` vs. `/formforge-fidelity`).

## Command Directory (25 Skills)

Type `/` in supported editors or use natural-language equivalents where native slash commands are unsupported:

| Command | Responsibility | Edits Code? |
| :--- | :--- | :---: |
| `/formforge` | Automatic capability and execution mode selection (`QUICK`–`FLAGSHIP`) | Yes |
| `/formforge-quick` | Small, targeted, low-risk frontend modifications | Yes |
| `/formforge-standard` | Ordinary frontend feature and component development | Yes |
| `/formforge-premium` | High-end professional UI/UX development | Yes |
| `/formforge-flagship` | Ambitious, sophisticated interactive experiences | Yes |
| `/formforge-plan` | Interactive design consultation and standalone master prompt generation | **No (Read-only)** |
| `/formforge-audit` | Comprehensive visual, functional, a11y, and waste inspection | **No (Read-only)** |
| `/formforge-polish` | Visual hierarchy, typography, spacing, and surface refinement | Yes |
| `/formforge-optimize` | Code, bundle, token, rendering, and Core Web Vitals optimization | Yes |
| `/formforge-replicate` | Recreate an interface from a screenshot or authorized reference | Yes |
| `/formforge-inspire` | Discover relevant real-world visual inspiration from the web | **No (Read-only)** |
| `/formforge-explore` | Explore 2–4 genuinely distinct creative directions and moodboards | **No (Read-only)** |
| `/formforge-redesign` | Completely rethink an existing interface while preserving core flows | Yes |
| `/formforge-motion` | Advanced native-first animations, transitions, gestures & micro-interactions | Yes |
| `/formforge-system` | Create, extract, or improve reusable design systems and tokens | Yes |
| `/formforge-responsive` | Design and repair responsive layouts across viewports | Yes |
| `/formforge-accessibility` | Identify and resolve semantic, keyboard, focus, contrast & a11y issues | Yes |
| `/formforge-deslop` | Detect and eliminate generic AI-generated design patterns and clutter | Yes |
| `/formforge-compare` | Compare design alternatives and before-and-after implementations | **No (Default)** |
| `/formforge-assets` | Discover and plan images, icons, illustrations, licensing & media perf | Plan / Config |
| `/formforge-verify` | Verify functional, responsive, a11y, and technical build requirements | Verify-first |
| `/formforge-reference` | Extract a 14-point design specification from screenshots/sites | **No (Read-only)** |
| `/formforge-dna` | Extract, maintain (`DESIGN.md`), and apply persistent project Design DNA | `DESIGN.md` |
| `/formforge-fidelity` | Verify implementation against approved design specs/contracts | Verify-first |
| `/formforge-help` | Display all 25 commands, workflows, and usage examples | **No (Read-only)** |

## Skill Collaboration Workflows

Skills cooperate cleanly without auto-chaining or circular invocation:
- **Concept to Contract to Build**: `/formforge-inspire` -> `/formforge-explore` -> `/formforge-plan` -> `/formforge-premium` -> `/formforge-fidelity`
- **Reference to Replication**: `/formforge-reference` -> `/formforge-replicate` -> `/formforge-compare` -> `/formforge-fidelity`
- **System Consistency**: `/formforge-dna` -> `/formforge-system` -> `/formforge-standard` -> `/formforge-verify`
- **Quality Recovery**: `/formforge-audit` -> `/formforge-deslop` -> `/formforge-polish` -> `/formforge-verify`
- **Interaction & Perf**: `/formforge-motion` -> `/formforge-accessibility` -> `/formforge-optimize`
- **Flagship Launch**: `/formforge-plan` -> `/formforge-flagship` -> `/formforge-fidelity`

## Shared Intelligence Architecture

- **Core Kernel**: [SKILL.md](SKILL.md) (5-dimension classification, mode bounds, priority ladder, quality/honesty gates).
- **Shared Domain Modules**: `references/` (23 focused Markdown modules, including `reference-and-replication.md`, `inspiration-and-exploration.md`, `design-dna.md`, and `design-fidelity.md`).
- **25 Specialized Skill Entry Points**: `skills/<command>/SKILL.md` (each with distinct purpose, boundaries, workflow, reference routing, and verification requirements).
- **8 Platform Command Directories**: `.agents/skills/`, `.codex/prompts/`, `.claude/commands/`, `.cursor/commands/`, `.gemini/commands/`, `.windsurf/workflows/`, `.github/prompts/`, and `.opencode/commands/` — 25 thin dispatchers per platform.
- **Docs & Evals**: `docs/` ([architecture.md](docs/architecture.md), [capability-registry.json](docs/capability-registry.json)) and `evals/` (including [planning-mode.json](evals/planning-mode.json) and [ecosystem-skills.json](evals/ecosystem-skills.json)).

## Installation

```bash
git clone https://github.com/AayushPandey2/frontend-design-skill.git
```

- **Complete ecosystem installation (Recommended)**: Copy `SKILL.md`, `references/`, `LICENSE`, and `skills/` into your workspace or global skills directory (or copy the platform-specific command directory: `.agents/skills/`, `.codex/prompts/`, `.claude/commands/`, `.cursor/commands/`, `.gemini/commands/`, `.windsurf/workflows/`, `.github/prompts/`, or `.opencode/commands/`).
- **Individual skill installation**: Install `SKILL.md` + `references/` + `LICENSE` into `<skills-dir>/formforge/`, and install any individual `skills/<command>/SKILL.md` alongside it (updating relative links to `../formforge/SKILL.md` and `../formforge/references/*.md` if moved out of `skills/`).
- **Remove**: Delete the installed `formforge*` skill folders and command files.

## Usage Examples

- *"/formforge-inspire Minimalist architectural studio portfolio with strong editorial typography."*
- *"/formforge-explore B2B climate analytics dashboard — show 3 distinct creative directions."*
- *"/formforge-plan Create a premium website for a luxury watch brand."*
- *"/formforge-reference Extract the typography, spacing, and surface system from this screenshot."*
- *"/formforge-replicate Recreate this pricing section cleanly in React + Tailwind."*
- *"/formforge-dna Extract our project Design DNA into DESIGN.md without duplicating CSS tokens."*
- *"/formforge-motion Add interruptible, reduced-motion-safe drawer and tab transitions."*
- *"/formforge-fidelity Verify our landing page against the locked master prompt."*
- *"/formforge-help"*

## Evaluation & Limitations

- **Current Readiness**: **`EXPERIMENTAL`**. Deterministic structural, metadata, link, JSON schema, and read-only guard checks pass (`0` Python files, `0` runtime dependencies). Corpus and simulated context comparisons are recorded in [evals/results.json](evals/results.json).
- **Limitations**: Live-agent execution, rendered browser scoring, and third-party host slash-command auto-discovery remain **host-untested** outside structural file verification.

## Compatibility

| Target | Status | Integration Mechanism & Fallback |
| :--- | :--- | :--- |
| **`agentskills.io` Specification** | Structurally Verified | Valid `SKILL.md` frontmatter + progressive `references/` + 25 `skills/*/SKILL.md` |
| **Antigravity & OpenAI Codex** | Structurally Verified / Host Untested | `.agents/skills/<cmd>/SKILL.md` & `.codex/prompts/<cmd>.md` + natural-language fallback |
| **Claude Code** | Structurally Verified / Host Untested | `.claude/commands/<cmd>.md` + natural-language fallback |
| **Cursor** | Structurally Verified / Host Untested | `.cursor/commands/<cmd>.md` + natural-language fallback |
| **Gemini CLI** | Structurally Verified / Host Untested | `.gemini/commands/<cmd>.toml` + natural-language fallback |
| **Windsurf** | Structurally Verified / Host Untested | `.windsurf/workflows/<cmd>.md` + natural-language fallback |
| **GitHub Copilot** | Structurally Verified / Host Untested | `.github/prompts/<cmd>.prompt.md` + natural-language fallback |
| **OpenCode** | Structurally Verified / Host Untested | `.opencode/commands/<cmd>.md` + natural-language fallback |

## License

MIT License — see [LICENSE](LICENSE).
