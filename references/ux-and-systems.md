# UX Psychology, Design Systems, Component Design & Motion Foundations

**Load when**: Designing user journeys, navigation, forms, interaction states, design systems, component specs, or motion intent.

## 1. UX Psychology & Ethical Usability

- Reduce cognitive load via clear grouping, recognition over recall, familiar patterns, and progressive disclosure.
- **Zero dark patterns**: Optimize conversion through clarity and trust—never use fake urgency, hidden costs, misleading copy, or obstructive cancellation flows.

## 2. Information Architecture & Interaction States

- **Navigation**: Organize around user tasks (primary/secondary/local nav, search, filters, sorting, breadcrumbs, tabs, mobile drawers, multi-step flows). Keep location, destinations, active state, and return paths unmistakable.
- **Journeys & states**: Plan entry -> action -> intermediate -> completion/failure/recovery. Implement real `default`, `hover`, `focus`, `active`, `selected`, `disabled`, `loading`, `empty`, `error`, `success`, `expanded`, and `collapsed` states only where behavior exists.
- **Honesty**: Never add non-functional buttons or simulate backend success; label mock/demo data clearly.

## 3. Design System & Component Design Intelligence

- **Existing systems**: Reuse CSS variables, theme configs, and component variants; never introduce a parallel system or redesign unrelated components.
- **New systems**: Define only needed semantic tokens and integrate non-obvious decisions with persistent design memory without duplicating code.
- **Component patterns** (design-level; code engineering deepens in Phase 04):
  - **Buttons / Actions**: Clear hierarchy (one primary per region), active labels, visible focus, disabled vs. loading clarity.
  - **Inputs / Forms**: Visible labels, logical grouping, inline non-blaming validation, helpful input types/autocomplete, >= 44px touch targets.
  - **Cards / Lists / Tables**: Scannable alignment, clear sort/filter affordances, horizontal scroll or stacked adaptation on mobile tables.
  - **Dialogs / Drawers / Dropdowns / Tabs**: Clear dismissal (`Escape`, close trigger), focus containment/restoration, unambiguous active state.
  - **Feedback (Tooltips, Toasts, Empty/Loading/Error)**: Non-blocking, concise, actionable recovery.

## 4. Design-Level Motion Intent

Animate only for interaction feedback, state clarity, spatial continuity, or brand character; keep frequent tasks fast and respect `prefers-reduced-motion`. For implementation mechanics, timing, springs, gestures, and GPU performance, load [motion-and-interactions.md](motion-and-interactions.md).
