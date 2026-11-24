# Visual Hierarchy, Layout, Spacing, Responsive & Asset Direction

**Load when**: Structuring page composition, grids, spacing, density, responsive layouts, or visual asset direction.

## 1. Visual Hierarchy

Order attention deliberately before composing:
1. Primary user objective -> 2. Primary action -> 3. Primary content -> 4. Secondary actions -> 5. Supporting context -> 6. Metadata.
- Control prominence via position, scale, contrast, weight, spacing, grouping, and color—never give every element equal weight or create competing primary actions.
- In operational tools, optimize for rapid scanning and repeat use rather than marketing-style hero attention.

## 2. Layout & Composition Strategy

Choose structure from content relationships, density, and reading flow:
- **Patterns**: editorial/asymmetric grids, split views, modular bands, full-bleed moments, focused single-column flows, or dense multi-column workspaces.
- **Symmetry vs. asymmetry**: Symmetry conveys stability and clarity; intentional asymmetry adds editorial energy—never use arbitrary offsets.
- **Earn containers**: Do not wrap every item in a card. Use containers only when they define clear grouping, interaction boundaries, or surface contrast.
- **Rhythm**: Vary scale, width, alignment, and density across marketing sections; keep transactional/enterprise layouts predictable.

## 3. Spacing, Proportion & Visual Density

- Use existing spacing tokens; when new, choose a coherent scale distinguishing intra-group, inter-group, section, and region spacing via proximity.
- **Calibrate density** (spacious, balanced, compact, dense) to user expertise, task frequency, and viewport: high-craft dashboards can be dense and crisp; editorial/luxury sites benefit from generous breathing room. Preserve legibility and target sizes at every density.

## 4. Responsive Design Strategy

Responsive design is content-driven recomposition, not shrinking desktop views:
- Adapt reading order, navigation, column counts, data tables, and spacing via CSS Grid/Flexbox and content-driven breakpoints (no JS resize listeners).
- Preserve critical actions and information on narrow screens—never hide essential controls just to fit.
- Test against narrow viewports (320px–375px), enlarged text, long strings, and realistic data.

## 5. Asset Direction

- Decide first whether imagery, diagrams, or icons actually add clarity or atmosphere.
- Define subject, art direction, aspect ratio, cropping, placement, alt text, and consistent icon stroke/family.
- **Integrity**: Never use icons as decorative clutter, invent asset availability, reference nonexistent image files, or claim an image was generated when no generation tool ran.
