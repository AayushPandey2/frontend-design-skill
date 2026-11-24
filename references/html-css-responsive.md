# Semantic HTML, Modern CSS & Responsive Engineering

**Load when**: Writing or refactoring markup, CSS architecture, layouts, container/media queries, or responsive behavior.

## 1. Engineering Contract & Design Fidelity

- **Process**: `Inspect -> Reuse -> Select -> Implement -> Verify -> Simplify` (compress to `Inspect -> Modify -> Verify` for localized edits).
- **Design fidelity**: Preserve Phase 03 typography, semantic colors, hierarchy, spacing, and visual signature—never replace distinctive design decisions with generic component defaults.
- **Production readiness**: Check navigation, primary actions, forms, keyboard operation, responsive widths, loading/error/empty states, console errors, and build compatibility.

## 2. Semantic HTML Intelligence

- Use native landmarks (`<main>`, `<nav>`, `<header>`, `<footer>`, `<section>`, `<article>`), ordered headings, lists, `<table>` for tabular data, `<dialog>`, `<details>`, and `<progress>`.
- **Interaction rules**: `<button>` for actions, `<a href>` for navigation, explicit `<label>` associations for controls. Never use clickable `<div>`/`<span>` as controls, never add redundant ARIA where native semantics suffice, and avoid unnecessary wrapper depth.

## 3. Advanced CSS Intelligence

- **Native layout first**: Use CSS Grid, Flexbox, logical properties, `position: sticky`, container queries, media queries, `clamp()`, and CSS transitions instead of JS resize/alignment/visibility scripts.
- **Intrinsic & fluid sizing**: Combine `min-width`/`max-width`, `min-content`/`max-content`/`fit-content`, `min()`, `max()`, and `clamp()`. Prevent flex/grid child overflow with `min-width: 0` where needed.
- **Specificity & tokens**: Keep selectors flat and predictable; avoid `!important` wars and fragile DOM-coupled chains. Reuse semantic custom properties; do not invent variables for single-use values.
- **Compatibility**: Use modern CSS supported by target browsers; add fallbacks only where project targets require them.

## 4. Responsive Engineering & Verification

- Avoid fixed widths or fixed heights on dynamic text; preserve critical actions on narrow screens; use deliberate horizontal scroll wrappers only for wide tables/data grids.
- Guard against text enlargement (`200%`), long localized labels, mobile dynamic viewports (`dvh`), and device safe areas (`env(safe-area-inset-*)`) while keeping logical reading and focus order.
- **Verification**: When browser tools exist, inspect representative widths (`320px`, `375px`/`390px`, `768px`, `1024px`, `1440px`, plus component stress widths) rather than assuming utility classes guarantee responsiveness.
