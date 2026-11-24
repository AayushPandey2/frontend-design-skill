# Rendered Inspection, Screenshot Intelligence & Visual Critique

**Load when**: Inspecting rendered interfaces, reviewing screenshots, auditing visual/design-system quality, or critiquing UI/UX craftsmanship.

## 1. Rendered Interface & Screenshot Inspection

- **Setup**: Reuse existing project startup commands or running servers; confirm the target route loads and reaches a representative state before inspecting. Never fabricate screenshots or claim browser verification without a browser.
- **Targeted capture**: Capture only viewports/states that answer concrete questions (desktop, mobile, overlays, error/loading/nav states). For before/after comparisons, hold viewport, route, data, theme, and animation/loading state constant.
- **Screenshot limits**: Screenshots reveal visual defects only—they cannot prove keyboard accessibility, screen-reader behavior, functional correctness, security, or runtime performance.

## 2. Professional Visual Critique & Design Intent

- **Multi-scale audit** (use only scales relevant to scope):
  - **Macro**: overall composition, primary nav, IA, page rhythm, product identity, first impression.
  - **Meso**: section hierarchy, grid relationships, grouping, surface consistency, spacing balance.
  - **Micro**: typography roles, button/input states, icons, borders, focus rings, alignment, target sizes.
- **Actionable criticism format**: For every meaningful finding, state (1) issue, (2) location, (3) evidence, (4) why it matters, (5) principle, (6) root cause, (7) proposed fix, and (8) necessity. Ban vague advice ("make it more premium", "improve spacing").
- **Design intent**: Separate objective defects, usability barriers, and requirement violations from subjective `PREFERENCE` alternatives; never silently overwrite the user's design direction with personal taste.

## 3. Domain Visual Audits

- **Typography**: Check rendered font availability, loading/fallbacks, hierarchy, measure, clipping, wrapping, localization overflow, and mobile heading scale; fix systemic scale issues at the token/type-role level.
- **Color & surfaces**: Check computed foreground/background contrast, semantic token usage, focus indicators, surface/shadow/radius consistency, and dark-mode parity; never infer contrast from color names alone.
- **Layout, spacing & consistency**: Detect accidental misalignment, fixed-height clipping, container bloat, and design drift (new controls diverging from existing radii/tokens/focus); fix shared tokens/rules rather than stacking local overrides.
- **Content & assets**: Flag generic promotional copy, fake testimonials/metrics, broken image paths, mismatched icon strokes, and missing alt text; never invent replacement business claims.
- **Anti-generic audit (false-positive resistant)**: Evaluate gradients, cards, shadows, asymmetry, and dense layouts against product fit—never flag valid, intentional design choices as defects.
