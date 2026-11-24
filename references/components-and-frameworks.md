# Component Architecture, Frameworks, State & Forms

**Load when**: Building/modifying components, managing state, fetching data, handling forms/async states, or working in React/Vue/Svelte/Astro/TS.

## 1. Component Architecture & Frameworks

- **Reuse first**: Search existing primitives/variants before creating new ones. Extract shared abstractions only for real reuse, shared a11y, or variant consistency—never single-use wrappers, generic factories, or contradictory boolean props (use explicit `variant`/`status` unions). Implement only real states.
- **Stack discipline**: Detect framework/version, router, styling, state, and tests from `package.json`/configs first; inspect installed APIs and never migrate stacks unrequested.
- **React**: Use smallest state scope (`local -> lifted -> URL -> server-data -> context/store`). Compute derived values during render—never store derived state or use `useEffect` for events or prop-to-state sync; reserve effects for external sync with cleanup. Apply `memo`/`useCallback` only for measured bottlenecks. Preserve Server Components (`"use client"` on interactive leaves only) and keep secrets off client bundles.
- **JS/TS**: Favor clear control flow, inference over ceremony, and runtime validation at trust boundaries (TS types do not validate runtime payloads).

## 2. Async Data, Forms & Resilient States

- **Data fetching**: Reuse project fetchers; run independent requests concurrently (no waterfalls); cancel/ignore stale responses (`AbortController`) to prevent race conditions. Never invent endpoints or fake backend success; label mock data.
- **Forms & states**: Use native form semantics, `type`/`autocomplete`, visible `<label>`, and `aria-describedby` errors; preserve input on recoverable errors and prevent duplicate submits. Provide localized loading feedback (no fake delays), actionable empty states, non-blaming error recovery, and clear confirmation.
- **Anti-patterns**: Eliminate redundant state/effects, unstable list keys, missing listener/timer cleanup, and duplicate requests.
