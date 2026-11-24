# Color, Contrast & Surface Intelligence

**Load when**: Creating a palette, extending theme tokens, building light/dark modes, fixing contrast, or designing elevation/materiality.

## 1. Semantic Color System

Organize colors by functional role rather than raw hex names:
- **Surfaces**: `canvas`, `surface`, `elevated-surface`, `border`
- **Ink**: `text-primary`, `text-secondary`, `text-muted`
- **Actions & focus**: `action-primary`, `action-secondary`, `accent`, `focus-ring`, `selection`
- **Status & data**: `success`, `warning`, `error`, `info`, `disabled`, `dataviz`

Reuse existing project tokens first. Do not generate full 10-step scales for colors used once.

## 2. Contextual Palette Generation

1. Identify product category and emotional tone.
2. Establish a dominant neutral environment (canvas, surfaces, ink).
3. Select 1–2 intentional brand/accent hues (no arbitrary bans on purple, blue, or gradients—only ban unmotivated defaults).
4. Map semantic roles and interactive states (hover, active, disabled, focus).
5. Verify contrast in both light and dark contexts if dual-theme applies.
6. Prune unused colors.

## 3. Color Accessibility (WCAG 2.2 AA Default)

- Enforce contrast targets for normal text (>= 4.5:1), large text and non-text UI/borders/icons (>= 3:1), interactive states, and visible focus indicators.
- Never communicate status, errors, or chart series through color alone (pair with text, icons, or patterns).
- Account for color-vision differences. Do not claim compliance without checking actual contrast values.

## 4. Light & Dark Modes

- Implement dark mode only when requested or standard for the product/repo.
- **Never invert colors blindly**: Build dark surfaces with subtle elevation stepping (higher elevation = slightly lighter surface), reduce glare, soften harsh borders, desaturate bright accents slightly to avoid vibration, and tune media/shadow contrast while preserving brand identity.

## 5. Materiality, Elevation & Surfaces

Use flat surfaces, borders, shadows, elevation, overlays, blur, gradients, textures, and corner radii with one coherent rationale:
- Use **borders** for crisp structural separation; **shadows/elevation** for overlays, popovers, and interactive depth; **blur/transparency** sparingly for layered chrome; **textures/gradients** only when they reinforce material character.
- **Failure modes**: Stacking shadows + heavy borders + blur + gradients simultaneously; inconsistent corner radii across nested elements; expensive blur/filter effects where flat surfaces communicate the same hierarchy.
