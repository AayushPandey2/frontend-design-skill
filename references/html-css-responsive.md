# Semantic HTML, Modern CSS & Responsive Engineering

**Load when**: Writing or refactoring markup, CSS architecture, layouts, container/media queries, or responsive widths.

## 1. Semantic HTML & Design Fidelity

- Preserve established typography, semantic colors, hierarchy, spacing, and visual signature.
- Use native landmarks (`<main>`, `<nav>`, `<header>`, `<footer>`, `<section>`, `<article>`), ordered headings, lists, `<table>` for tabular data, `<dialog>`, `<details>`, and `<progress>`.
- Use `<button>` for actions, `<a href>` for navigation, and explicit `<label>` associations. Never use clickable `<div>`/`<span>` as controls, add redundant ARIA where native semantics suffice, or add unnecessary wrapper depth.

## 2. Advanced CSS & Responsive Engineering

- **Native layout first**: Use CSS Grid, Flexbox, logical properties, `position: sticky`, container/media queries, `clamp()`, and CSS transitions over JS resize/alignment/visibility scripts.
- **Sizing & specificity**: Combine `min-width`/`max-width`, `min-content`/`max-content`/`fit-content`, `min()`, `max()`, and `clamp()`; set `min-width: 0` on flex/grid children to prevent overflow. Keep selectors flat (no `!important` wars) and reuse semantic tokens.
- **Responsive rules**: Avoid fixed widths/heights on dynamic text; preserve critical actions on narrow screens; use scroll wrappers only for wide tables. Support `200%` text scaling, long localized strings, `dvh`, and `env(safe-area-inset-*)` while keeping logical reading/focus order.
- **Verification**: Inspect representative widths (`320px`, `375px`/`390px`, `768px`, `1024px`, `1440px`, plus stress widths) when browser tools exist.
