# Accessibility Engineering (WCAG 2.2 AA)

**Load when**: Implementing interactive controls, dialogs, forms, keyboard navigation, contrast fixes, or dynamic status updates.

## 1. Accessible Names & Keyboard Interaction

- Provide programmatic accessible names for every control (icon buttons, inputs, search, toggles, interactive images)—never rely on `placeholder` alone.
- Support `Tab`/`Shift+Tab` in logical DOM order, `Enter`/`Space` activation, `Escape` dismissal, arrow-key navigation on composite widgets (tabs, menus, listboxes), and visible `:focus-visible` outlines.

## 2. Dialogs, Forms, Contrast & Dynamic Content

- **Dialogs/overlays**: Prefer native `<dialog>` or existing accessible primitives. Enforce accessible name (`aria-labelledby`/`aria-label`), initial focus, modal containment, `Escape`/close dismissal, background inertness, and focus restoration to the trigger.
- **Forms & contrast**: Associate visible `<label>`, link errors via `aria-describedby` and `aria-invalid`, and pair color with text/icons. Meet WCAG 2.2 AA (`4.5:1` normal text, `3:1` large text and non-text UI/focus). Never claim compliance from automated checks alone.
- **Dynamic content**: Use `aria-live="polite"`/`role="status"` or `role="alert"` sparingly for meaningful updates; support `200%` text scaling, reflow, and `prefers-reduced-motion`.
