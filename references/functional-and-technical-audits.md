# Functional, Responsive, Accessibility, Motion & Economy Audits

**Load when**: Verifying interactive flows, user journeys, responsive widths, WCAG a11y, motion/perf quality, or auditing engineering waste.

## 1. Functional, Journey, Responsive & A11y Audits

- **Functional & journeys**: Exercise real controls, links, forms, filters, dialogs, tabs, and state transitions (`default`..`error`/`success`); flag dead controls. Test critical multi-step flows with safe sample data; never trigger unauthorized real purchases/destructive actions or present mock flows as live backends.
- **Responsive**: Test representative widths (`320px`, `375px`/`390px`, `768px`, `1024px`, `1440px`) + long labels and `200%` text scaling for overflow, clipping, touch targets, and preserved primary actions.
- **Accessibility**: Combine automated checks with manual keyboard (`Tab`, `Enter`, `Space`, `Escape`, arrows), dialog focus containment/restoration, computed contrast, and `prefers-reduced-motion` checks (zero automated violations != full WCAG compliance).

## 2. Motion, Performance & Engineering-Waste Audits

- **Motion**: Test rapid toggling, mid-flight reversal, and reduced motion—never judge motion from static screenshots or claim unmeasured FPS.
- **Performance**: Distinguish lab vs. field telemetry and baseline -> fix -> re-measure -> check regressions.
- **Engineering waste**: Flag dead code, redundant state/effects, duplicate components/styles, excessive DOM depth, and unneeded deps while protecting validation, a11y, security, and error recovery.
