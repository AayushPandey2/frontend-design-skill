# FORMFORGE Architecture Specification

## 1. Design Goals & Architectural Economy

FORMFORGE is built as a portable, file-based Agent Skill compliant with the `agentskills.io` specification. Every architectural choice adheres to **architectural economy**:

- **Zero runtime dependencies**: The core skill requires no custom daemon, database, knowledge graph, or proprietary CLI to function across coding agents.
- **Zero speculative infrastructure**: Modules, schemas, and verification scripts are introduced only when a concrete capability or measurement requirement justifies their maintenance and context cost.
- **Portable knowledge**: All instructions use standard Markdown and JSON so any compatible agent can discover, route, and apply them consistently.

---

## 2. Progressive Context Architecture (Levels 0–4)

FORMFORGE minimizes input token overhead by loading knowledge strictly on demand:

| Level | Artifact / Scope | Context Behavior | Phase Status |
| :--- | :--- | :--- | :--- |
| **Level 0 — Discovery** | `SKILL.md` YAML frontmatter (`name`, `description`) | Always in agent index (~100 tokens) | Implemented (Phase 01) |
| **Level 1 — Core Kernel** | `SKILL.md` Markdown body | Loaded on skill activation (<= 250 lines) | Implemented (Phase 01) |
| **Level 2 — Capability Modules** | Focused domain guides (`references/*.md`) | Loaded selectively by task route | Planned (Phase 02) |
| **Level 3 — Specialized Knowledge** | Product-domain profiles, compact pattern tables, project design memory | Retrieved only when product/pattern matches | Planned (Phase 03) |
| **Level 4 — Executable Tools** | Validation and verification scripts (`scripts/*.py`, browser probes) | Executed as black-box tools; source stays out of context | Foundation validator in Phase 01; browser/a11y probes in Phase 04 |

---

## 3. Adaptive Execution Modes & Workflow Scaling

FORMFORGE scales process ceremony to task scope and risk. The agent auto-selects the lightest sufficient mode unless the user explicitly overrides it.

### `QUICK`
- **Entry criteria**: Single-component adjustment, localized CSS/responsive fix, copy edit, or low-risk bug fix.
- **Workflow**: Inspect affected files -> minimal edit -> targeted verification -> concise report.
- **Refinement bound**: Max 1 verification pass after fix.

### `STANDARD`
- **Entry criteria**: Ordinary feature page, new reusable component, accessibility remediation, performance tuning, or design system update.
- **Workflow**: Understand -> Inspect stack & existing tokens -> Route relevant domains -> Implement -> Render & verify -> Refine identified defects -> Deliver.
- **Refinement bound**: Up to 2 targeted refinement passes.

### `PREMIUM`
- **Entry criteria**: High-impact landing page, multi-screen product interface, e-commerce flow, or full design system creation.
- **Workflow**: Product brief -> Creative direction -> Token & layout plan -> Implement -> Render -> Visual & UX critique -> Refine -> Verify all gates -> Deliver.
- **Refinement bound**: Up to 3 bounded refinement passes, stopping early when acceptance criteria pass.

### `FLAGSHIP`
- **Entry criteria**: Bespoke brand flagship, creative portfolio, or complex interactive experience with custom motion/choreography.
- **Workflow**: Deep direction exploration (2–3 distinct concepts, select strongest) -> Bespoke typography/motion/system -> Implement -> Independent visual, motion, a11y & perf audit -> Refine -> Deliver.
- **Refinement bound**: Up to 3 comprehensive passes; never equate flagship quality with gratuitous animation or code bloat.

---

## 4. Capability Routing Strategy

Routing maps incoming task signals to **mode** + **active capability domains** (`FF-CR` through `FF-OP`) without loading unrelated guidance:

1. **Detect stack & existing system first**: Inspect `package.json`, directory layout, and existing tokens/components before choosing any implementation pattern.
2. **Classify scope & risk**: Pick `QUICK`, `STANDARD`, `PREMIUM`, or `FLAGSHIP`.
3. **Select active domains**:
   - Bugfix / CSS tweak -> `FF-EN`, `FF-OP`, `FF-VF`
   - New dashboard / SaaS feature -> `FF-UX`, `FF-CP`, `FF-DS`, `FF-EN`, `FF-SP`, `FF-VF`, `FF-OP`
   - Brand landing page / portfolio -> `FF-CR`, `FF-VD`, `FF-UX`, `FF-DS`, `FF-MO`, `FF-EN`, `FF-VF`, `FF-OP`
   - Accessibility / perf audit -> `FF-VF`, `FF-EN`, `FF-UX`, `FF-OP`
4. **Load only matched Level 2/3 knowledge** (once Phase 02+ modules exist).

---

## 5. Conflict Resolution Policy

When two instructions or design goals collide, apply the **10-level priority ladder** in [SKILL.md](../SKILL.md):

1. Safety, security, and mandatory platform constraints.
2. Explicit user requirements and brief constraints.
3. Functional correctness and data integrity.
4. Accessibility and usability.
5. Existing project architecture and design system.
6. Product-specific creative direction and visual identity.
7. Runtime performance and maintainability.
8. Code, context, and tool-call economy.
9. Creative experimentation.
10. Decorative preferences.

### Concrete Resolution Rules
- **Creative direction vs. Existing design system**: Preserve existing tokens and component contracts by default (Priority 5 > 6). Introduce new visual direction only for greenfield work or when the user explicitly requests a redesign (Priority 2).
- **Economy vs. Accessibility / Security**: Accessibility and security always win (Priority 1, 4 > 8). Never omit focus management, keyboard navigation, contrast checks, or input validation to save lines or tokens.
- **Anti-generic heuristics vs. Explicit user requests**: Explicit user aesthetic choices override anti-generic heuristics (Priority 2 > 6/10). Evaluate every technique contextually rather than applying universal bans.
- **Verification thoroughness vs. Tool-call economy**: Scale verification to risk. Small edits use targeted checks; UI/layout changes require rendered inspection. Never skip mandatory gates to save tool calls.
- **Deep domain knowledge vs. Context budget**: Load only the active domain guidance for the current task; defer specialized references until a concrete task requires them.

---

## 6. Global Economy Protocol

1. **Code economy**: Follow the 6-step decision ladder (existing project code -> native HTML/CSS -> browser API -> installed dependency -> small custom code -> justified complexity). Eliminate dead code, redundant state, derived-value effects, and premature wrappers.
2. **Context economy**: Search before reading; read targeted line ranges; avoid re-reading unchanged files; keep design briefs and final reports compact.
3. **Architectural economy**: Every file and abstraction must solve a present, concrete problem.
4. **Verification economy**: Run risk-appropriate checks; fix root causes rather than stacking patches; stop refining once acceptance criteria are met.

---

## 7. Evidence-Driven Refinement & Verification Model

FORMFORGE follows a closed feedback loop:

`Understand -> Route -> Design -> Implement -> Render -> Critique -> Refine -> Verify -> Deliver`

- **Evidence requirement**: Visual, responsive, and motion claims require inspecting actual rendered output (browser/screenshot/DOM metrics), not just reading source code.
- **Stopping condition**: Stop refining when mandatory gates pass, rubric targets for the active mode are met, and further edits yield diminishing returns.
- **Honesty**: Unchecked criteria, missing runtime environments, or unresolved defects must be reported explicitly.
