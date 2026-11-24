# Component Architecture, Frameworks, State & Forms

**Load when**: Building or modifying components, managing state, fetching data, handling forms/async states, or working in React/Next/Vue/Svelte/Astro/TS.

## 1. Component Architecture & Reuse

- **Pre-creation check**: Search existing project -> inspect primitives & variants -> verify a11y needs -> compose existing parts before writing new primitives.
- **Abstraction discipline**: Extract shared components only for genuine reuse, shared a11y, or variant consistency. Avoid single-use wrappers, excessive prop forwarding, generic factories, and contradictory boolean props (prefer explicit `variant`/`status` unions). Implement only real states (`default`, `hover`, `focus-visible`, `active`, `selected`, `disabled`, `pending`/`loading`, `empty`, `error`, `success`, `expanded`/`collapsed`).

## 2. Framework Detection & React Intelligence

- **Respect the stack**: Detect framework, version, language, router, styling, state, and test tools from `package.json`/configs first. Never migrate frameworks unrequested; check installed APIs before assuming behavior.
- **React state & effects**: Use the smallest state scope (local -> lifted -> URL -> server-data -> context/store). Compute derived values during render—never store derived state or use `useEffect` for event handling or prop-to-state syncing. Reserve effects for external synchronization with proper cleanup.
- **Rendering & server boundaries**: Apply `memo`/`useCallback` only for measured bottlenecks. Preserve Server Components where supported (`"use client"` only on interactive leaves) and keep server secrets out of client bundles.

## 3. JavaScript & TypeScript Discipline

- Favor clear control flow, inference over ceremony, and pure helpers where useful. Validate untrusted runtime data at trust boundaries (TS types do not validate runtime payloads). Eliminate dead code, unused imports, and speculative fallbacks.

## 4. Async Data, Forms & Resilient States

- **Data fetching**: Reuse project fetchers; run independent requests concurrently (avoid waterfalls); cancel or ignore stale responses to prevent race conditions. Never invent endpoints or fake backend success; label mock data clearly.
- **Forms**: Prefer native form semantics, appropriate `type`/`autocomplete`, visible labels, and `aria-describedby` errors. Preserve user input on recoverable errors, prevent duplicate submits while pending, and never rely solely on client validation for security.
- **States**: Provide localized loading feedback (no artificial delays), actionable empty states, non-blaming error recovery without exposing stack/secrets, and clear confirmation when changes aren't self-evident.
- **Anti-pattern check**: Watch for redundant state/effects, unstable list keys, missing listener/timer cleanup, and duplicate requests.
