# Implementation, Repo Inspection & Tool Economy

## 1. Repository Inspection & File-Reading Intelligence

Inspect in order, stopping as soon as the scope is clear:
1. Structure -> 2. Stack (`package.json`/configs) -> 3. Affected files -> 4. Existing symbols/primitives -> 5. Targeted line ranges -> 6. Expand only if shared callers/constraints require it.
- **Avoid**: Reading entire repos, `node_modules`, build outputs, or unchanged files; broad audits for localized fixes.
- **Full-file reads**: Justified only for complex state, shared dependencies, security boundaries, or intricate control flow.

## 2. Frontend Simplifications & Editing Economy

Prefer native platform capabilities unless accessibility, interactivity, or creative requirements justify more:
- CSS `:hover`/`:focus-within`, Grid/Flexbox, container/media queries, `position: sticky`, and CSS transitions over JS listeners or animation libraries.
- Derived values during render over redundant state or synchronization effects; event handlers over effect-driven side effects.
- Local state over global stores; semantic HTML (`<button>`, `<dialog>`, `<details>`) over `<div>` wrappers; existing primitives and tokens over duplicates.
- **Existing repos**: Modify minimum necessary files, preserve component APIs, skip unrelated formatting/renaming, delete superseded dead code, and update directly affected callers/tests. Never sacrifice readability or root-cause correctness to shrink line count.

## 3. Tool-Call & Response Economy

- Batch independent reads/searches; run targeted builds/tests for low-risk edits and regression checks when shared primitives or critical flows change.
- Never repeat identical passing commands or echo large edited code blocks in final replies.
