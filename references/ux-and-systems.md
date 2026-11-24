# UX Psychology, Design Systems & Component Patterns

**Load when**: Designing user journeys, navigation, forms, interaction states, design systems, or component specs.

## 1. UX Psychology, IA & Interaction States

- Reduce cognitive load via grouping, recognition over recall, and progressive disclosure. **Zero dark patterns**: never use fake urgency, hidden costs, misleading copy, or obstructive cancellation.
- **Navigation**: Organize around user tasks (`nav`, search, filters, sort, breadcrumbs, tabs, mobile drawers, multi-step flows) with unmistakable location, active state, and return paths.
- **Journeys & states**: Plan `entry -> action -> intermediate -> completion/failure/recovery`. Implement real states (`default`, `hover`, `focus`, `active`, `selected`, `disabled`, `loading`, `empty`, `error`, `success`, `expanded`, `collapsed`) only where behavior exists. Never add dead controls or simulate backend success; label mock data.

## 2. Design Systems & Component Patterns

- Reuse existing CSS variables, themes, and variants; build only needed semantic tokens for new projects and sync non-obvious decisions with [project-and-memory.md](project-and-memory.md).
- **Buttons**: Clear hierarchy (one primary/region), active labels, visible focus, pending vs. disabled clarity.
- **Inputs/Forms**: Visible labels, logical grouping, inline non-blaming validation, `>= 44px` touch targets.
- **Lists/Tables**: Scannable alignment, clear sort/filter affordances, horizontal scroll or stacked mobile adaptation.
- **Dialogs/Drawers/Tabs/Menus**: `Escape`/close triggers, focus containment/restoration, clear active state.
- **Motion intent**: Animate only for feedback, state clarity, or spatial continuity; see [motion-and-interactions.md](motion-and-interactions.md) for implementation.
