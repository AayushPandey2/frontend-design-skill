# Project Awareness & Persistent Design Memory

## 1. Proportional Stack & Dependency Discipline

Inspect only what the task requires (`package.json`, framework/TS config, styling/tokens, component primitives, routing, state, test tools, project instructions).
- **Preserve the stack**: Write idiomatic code for the project's framework, styling engine, and router; never migrate stacks unrequested. For greenfield work, pick the lightest suitable stack and note key assumptions.
- **Before adding any dependency**: Confirm (1) not already installed, (2) no installed package covers it, (3) native HTML/CSS/Browser APIs cannot solve it, and (4) bundle, a11y, and maintenance cost are justified.

## 2. Lightweight Persistent Design Memory

- **Scope**: Read existing tokens/themes/design notes first. Create or update a concise design-decisions note only for multi-page/multi-session continuity—never for `QUICK` or trivial edits.
- **Authority & economy**: Code/CSS tokens remain authoritative. Store only non-obvious decisions not easily recovered from code (product identity, audience, direction, type/color rationale, density/motion/a11y conventions). Never store secrets, API keys, transcripts, code snippets, or stale notes.
- **Conflicts**: When design memory conflicts with code, inspect the discrepancy; explicit user intent wins, followed by authoritative project code, then prune/update stale memory to keep one source of truth.
