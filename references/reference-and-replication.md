# Visual Reference Analysis, Replication & Comparison

**Load when**: Analyzing a visual reference (`/formforge-reference`), replicating a screenshot/authorized site (`/formforge-replicate`), or comparing design concepts/implementations (`/formforge-compare`).

## 1. Reference vs. Replicate vs. Compare Separation

- **Reference (`/formforge-reference`) — STRICT READ-ONLY**: Analyzes and produces a structured, implementation-ready specification. Never automatically generates or edits frontend code.
- **Replicate (`/formforge-replicate`) — Implements**: Translates user-provided screenshots or authorized website references into the smallest complete implementation, renders, compares, and corrects meaningful visual discrepancies.
- **Compare (`/formforge-compare`) — Read-Only by Default**: Compares visual concepts, reference designs, screenshots, or before-and-after implementations using consistent conditions and evidence-based criteria. Never modifies code unless explicitly requested.

## 2. 14-Point Visual Reference Extraction Schema

When inspecting a screenshot or authorized website reference, extract concrete measurements and observable evidence—mark inferred values explicitly:
1. **Design Language**: Aesthetic category, visual tone, restraint vs. expressiveness.
2. **Typography System**: Display/body/mono families (or closest verified stack), scale ratio, weights, line-heights, tracking, alignment.
3. **Color Palette**: Primary, secondary, surface, border, and accent hex/oklch values.
4. **Semantic Colors**: Success, warning, error, info, focus ring, and disabled states.
5. **Grid Structure**: Column count, max-width container, gutters, breakpoints.
6. **Layout Proportions**: Above-the-fold composition, section cadence, hero-to-content ratios, asymmetry.
7. **Spacing System**: Base unit, section padding, card/stack gaps, rhythm consistency.
8. **Component Appearance**: Buttons, inputs, cards, navbars, badges, tables, and interactive states.
9. **Surface Treatments**: Flat, layered, glass, grain, gradients, or hairline dividers.
10. **Shadows & Borders**: Elevation tokens, border widths, radii, and contrast boundaries.
11. **Image Treatment**: Aspect ratios, framing, overlays, duotones, or focal cropping.
12. **Information Density**: Whitespace ratio, items per row, copy-to-chrome balance.
13. **Responsive Behavior**: Desktop-to-mobile stacking, nav collapse, fluid scaling.
14. **Observable Motion & Transitions**: Hover/focus micro-feedback, scroll reveals, page/drawer transitions (report "not observable from static screenshot" when inspecting a static image).

## 3. Replication Execution & Honesty Protocol

1. **Inspect & Extract**: Run the 14-point extraction on desktop and mobile views (plus accessible interaction states) and list required media/icon/font assets.
2. **Respect Permissions**: Use only user-provided assets, licensed/open alternatives, or clean geometric placeholders—never scrape restricted assets or bypass access controls.
3. **Implement Economically**: Build the smallest complete implementation following the project's stack and [implementation-economy.md](implementation-economy.md).
4. **Render & Compare**: Inspect rendered output against the original reference at matching viewports; fix meaningful layout, typography, spacing, color, and responsive discrepancies.
5. **Honesty Gate**: Never claim pixel-perfect replication without side-by-side visual comparison evidence. Explicitly report unavailable assets, substituted fonts/media, and unavoidable differences.

## 4. Structured Comparison Protocol

- Compare under **consistent conditions** (same viewport width, theme, data state, and zoom).
- Evaluate across clear criteria: hierarchy & readability, layout balance, contrast & accessibility, responsiveness, interaction clarity, and implementation complexity.
- Separate **objective observations** (alignment, contrast, overflow, element count) from **design judgment**, and state what could not be rendered or verified.
