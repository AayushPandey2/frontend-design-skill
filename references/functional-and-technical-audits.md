# Functional, Responsive, Accessibility, Motion & Economy Audits

**Load when**: Verifying interactive flows, user journeys, responsive layouts, WCAG accessibility, motion/performance quality, or auditing engineering waste.

## 1. Functional, State & User Journey Verification

- **Behavior over syntax**: Buttons, ARIA attributes, and responsive classes in source code do not prove working UI. Exercise real navigation, forms, filters, dialogs, tabs, and error recovery when browser/test tools allow.
- **States & journeys**: Verify actual transitions (`default`, `hover`, `focus`, `disabled`, `pending`, `loading`, `empty`, `error`, `success`); flag dead controls. For multi-step journeys, test start -> intermediate -> outcome -> failure recovery using safe sample data.
- **Safety & honesty**: Never trigger unauthorized real purchases or destructive actions; never present mocked frontend flows as live backend integrations.

## 2. Responsive & Accessibility Auditing

- **Responsive**: Test representative widths (`320px`, `375px`/`390px`, `768px`, `1024px`, `1440px` as needed) plus long labels and `200%` text scaling; check overflow, clipping, touch targets, and preserved primary actions.
- **Accessibility (WCAG 2.2 AA)**: Combine automated checks with manual keyboard (`Tab`, `Enter`, `Space`, `Escape`, arrow keys), dialog focus containment/restoration, computed contrast, and `prefers-reduced-motion` verification. Zero automated violations never proves full compliance.

## 3. Motion, Performance & Engineering-Waste Audits

- **Motion**: Test rapid open/close, repeated toggling, mid-flight reversal, navigation during transitions, and `prefers-reduced-motion`—never judge motion from static screenshots or claim unmeasured FPS.
- **Performance**: Distinguish lab checks from real-user field telemetry and static risk indicators from measured results. Capture baseline -> fix root cause -> re-measure -> check regressions.
- **Engineering waste**: Detect dead code, redundant state/effects, duplicate components/styles, excessive DOM depth, and unneeded dependencies—while protecting essential validation, accessibility, security, and error recovery.
