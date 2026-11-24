# Routing, Modes, Planning & Delegation Economy

## 1. Mode Guardrails & Escalation

- **`QUICK`**: Inspect affected files -> preserve conventions -> minimal change -> targeted check. No design brief, design memory, repo-wide audit, new deps, or unrelated refactoring.
- **`STANDARD`**: Understand -> inspect stack -> load matched refs -> set/preserve direction -> implement -> verify/render -> refine defects (<=2 passes).
- **`PREMIUM`**: Product brief -> inspect architecture -> 2–3 distinct directions (skip if brand/ref pins it) -> tokens -> states -> implement -> render & critique -> refine (<=3 passes).
- **`FLAGSHIP`**: Deep analysis -> creative direction -> design system -> complex interactions/motion -> comprehensive responsive/a11y/perf checks -> unanchored critique -> refine (<=5 passes). Never load every capability blindly.
- **Escalate** on hidden coupling, auth/payment risk, or missing foundations; **de-escalate** when existing primitives/tokens already solve the task.

## 2. Intent-First Routing & Stopping Rules

Route by **user intent**, not keyword matching (e.g., "remove button animation" uses `QUICK` + `implementation-economy`, not `motion-and-interactions`).
- **Expand context** only when a required capability is missing, new complexity/constraints appear, or verification uncovers a defect.
- **Stop expanding** once decisions are reliable and existing conventions resolve remaining questions. Never recursively load references merely because another module is mentioned.

| Task Example | Mode | Load | Exclude |
| :--- | :--- | :--- | :--- |
| Change button radius / remove hover | `QUICK` | `implementation-economy` | `creative-direction`, `motion-and-interactions`, `industry-patterns` |
| Fix dropdown keyboard nav | `STANDARD` | `accessibility-engineering`, `components-and-frameworks` | `creative-direction`, `project-and-memory` |
| Improve dashboard table | `STANDARD` | `layout-and-responsive`, `ux-and-systems`, `project-and-memory` | `creative-direction`, `motion-and-interactions` |
| Luxury landing page / portfolio | `PREMIUM`/`FLAGSHIP` | `creative-direction`, `typography-and-content`, `color-and-surfaces`, `layout-and-responsive`, `industry-patterns` | Dense tool patterns |
| Drag-and-drop board | `PREMIUM` | `components-and-frameworks`, `motion-and-interactions`, `accessibility-engineering`, `performance-and-reliability` | Unrelated domain profiles |

## 3. Planning & Delegation Economy

- **Planning**: Small tasks -> compact mental diff (no plans/briefs). Standard -> requirements, constraints, approach, verify. Complex -> detailed plan only when it prevents rework.
- **Delegation**: Delegate only for unanchored independent visual critique, genuinely parallel independent tasks, or specialized audits. Never delegate CSS tweaks, routine file reads, or tasks the main agent handles faster—parallel agents increase total tokens.
