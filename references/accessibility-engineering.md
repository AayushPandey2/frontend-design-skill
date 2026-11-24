# Accessibility Engineering (WCAG 2.2 AA)

**Load when**: Implementing interactive controls, dialogs, forms, keyboard navigation, contrast fixes, or dynamic status updates.

## 1. Accessible Names & Keyboard Interaction

- **Accessible names**: Every interactive control (especially icon-only buttons, inputs, search fields, toggles, and interactive images) must have a clear programmatic name. Never rely solely on `placeholder` as a label.
- **Keyboard flow**: Support `Tab`/`Shift+Tab` in logical DOM order, `Enter`/`Space` activation, `Escape` dismissal on overlays, and arrow-key navigation on composite widgets (tabs, menus, listboxes) following established patterns.
- **Focus visibility**: Preserve clear `:focus-visible` outlines on all interactive elements.

## 2. Dialogs, Overlays & Focus Management

- Prefer native `<dialog>` or existing accessible dialog primitives before custom implementations.
- Enforce: accessible name (`aria-labelledby`/`aria-label`), initial focus inside the dialog, modal focus containment (`inert`/trap), `Escape` and backdrop/close dismissal, background scroll lock where appropriate, and focus restoration to the triggering control on close.

## 3. Forms, Contrast & Dynamic Announcements

- **Forms**: Associate visible `<label>` elements, link validation errors via `aria-describedby` and `aria-invalid`, and pair color with text/icons.
- **Contrast**: Meet WCAG 2.2 AA thresholds (`4.5:1` normal text, `3:1` large text and non-text UI components/borders/focus indicators). Never claim compliance from automated checks alone.
- **Dynamic content**: Use `aria-live="polite"`/`role="status"` or `role="alert"` sparingly for meaningful async updates without announcing trivial UI noise. Support `200%` text scaling, responsive reflow, and `prefers-reduced-motion`.
