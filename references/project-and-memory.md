# Project Awareness & Persistent Design Memory

## 1. Proportional Project Inspection

Inspect only what the task scope requires (skip repo-wide audits for a 1-file CSS fix):
- **Stack & tooling**: `package.json`, framework config, TypeScript config, package manager, build/test scripts.
- **Styling & tokens**: CSS custom properties, Tailwind config, theme files, existing spacing/color/type conventions.
- **UI architecture**: component directories, shared primitives, icon/animation libraries, routing, state, and project-level agent instructions.

## 2. Framework & Dependency Discipline

- **Preserve the stack**: Write idiomatic code for the project's existing framework, styling system, and router. Never migrate frameworks, styling engines, or state libraries unless explicitly asked.
- **Greenfield selection**: If no project exists, choose the lightest stack that fits the requirements and note key assumptions concisely.
- **Before adding any dependency**: Verify (1) it isn't already installed, (2) no installed package covers it, (3) native HTML/CSS/Browser APIs cannot solve it, and (4) bundle size, accessibility, and maintenance cost are justified.

## 3. Lightweight Persistent Design Memory

Preserve high-value design decisions across pages and sessions without duplicating code.

### When to Use
- **Read first** when a project already has design tokens, theme files, or a concise design-decisions note.
- **Create or update** only when establishing a design system, multi-page product identity, or stable cross-session conventions—never for `QUICK` or trivial edits.

### Memory Economy
- **Code is authoritative**: Existing CSS variables, theme configs, and components remain the primary source of truth.
- **Store only non-obvious decisions**: product identity, audience, creative direction, typography pairing rationale, semantic role rules, layout/density rules, motion principles, and a11y conventions.
- **Never store**: secrets, API keys, conversation transcripts, duplicate code snippets, temporary debug notes, or stale decisions.

### Conflict Resolution
When stored design memory conflicts with current project code:
1. Inspect the discrepancy.
2. Treat explicit user requirements as highest priority, followed by current authoritative project code.
3. Update or prune stale memory so there is never a second contradictory source of truth.
