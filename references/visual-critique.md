# Rendered Inspection, Screenshot Economy & Visual Critique

**Load when**: Inspecting rendered UI, capturing screenshots, auditing visual/design-system quality, or critiquing craftsmanship.

## 1. Rendered Inspection & Screenshot Economy

- Reuse existing startup commands/running servers; verify target routes reach a representative state.
- **Screenshot economy**: Capture only viewports/states answering concrete questions (desktop, mobile, overlays, errors)—never capture unchanged states, redundant viewports, or nonvisual edits. Hold viewport, route, data, theme, and animation/loading state constant for before/after comparisons.
- **Limits**: Screenshots reveal visual defects only; pair them with behavioral/technical checks for keyboard a11y, security, and functionality.

## 2. Multi-Scale Critique & Domain Audits

- **Scales** (use only relevant scales): **Macro** (composition, nav, IA, rhythm, identity) -> **Meso** (section hierarchy, grids, grouping, spacing) -> **Micro** (type roles, states, icons, focus rings, alignment, targets).
- **8-field finding format**: `issue | location | evidence | why it matters | principle | root cause | proposed fix | necessity`. Ban vague feedback ("make it more premium"); separate objective defects from `PREFERENCE` alternatives.
- **Domain checks**: Verify rendered font loading/measure/clipping, computed contrast, semantic token drift (fix shared tokens over local overrides), honest copy/assets, and contextual anti-generic fit (never flag valid, brief-earned gradients, cards, asymmetry, or dense layouts).
