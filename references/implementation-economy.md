# Implementation & Tool Economy

## 1. Implementation Decision Ladder

Before writing new code, evaluate in order and stop at the first viable option:
1. **Existing project code**: Reuse existing components, hooks, helpers, and tokens.
2. **Native HTML & CSS**: Prefer semantic elements and modern CSS over custom JS.
3. **Browser APIs**: Use platform APIs (`Intl`, `Dialog`, `IntersectionObserver`, `Web Animations`) before packages.
4. **Installed dependencies**: Reuse what is already in `package.json`.
5. **Small custom implementation**: Write clear, shallow, readable code.
6. **Justified complexity**: Add dependencies or abstractions only when concrete benefits outweigh maintenance cost.

## 2. Frontend-Specific Simplifications

Default to the simpler platform mechanism unless accessibility, interactivity, or creative requirements demand otherwise:
- CSS `:hover`/`:focus-within`, Grid/Flexbox, media/container queries, and `position: sticky` over JS listeners.
- CSS transitions over animation libraries for simple state changes.
- Derived values computed during render over redundant state or synchronization effects.
- Event handlers over effect-driven side effects.
- Local component state over global stores unless cross-tree sharing is required.
- Semantic HTML (`<button>`, `<dialog>`, `<details>`, `<nav>`) over `<div>` wrappers.
- Existing design tokens over repeated hardcoded values.

## 3. Anti-Bloat & Editing Economy

- **Avoid**: unrequested features, speculative abstractions, single-use wrappers, unused imports/variables, dead code, redundant fallback layers, and wholesale file rewrites for localized edits.
- **Existing repos**: Modify the minimum necessary files, preserve established component APIs, avoid unrelated formatting/renaming, remove superseded dead code, and update directly affected callers/tests.
- Never sacrifice readability or root-cause correctness to artificially shrink a diff.

## 4. Tool & Execution Economy

- **Search first**: Locate symbols/files with targeted search before reading; read only needed line ranges.
- **Batch**: Group independent file reads or checks.
- **No churn**: Never re-read unchanged files, repeat identical commands without new information, or recap large edited code blocks in the final response.
- **Risk-scaled checks**: Run targeted tests/builds for low-risk edits; run broader regression checks when shared primitives or critical flows change.
