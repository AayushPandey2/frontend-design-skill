# Design-Contract Fidelity Verification

**Load when**: Verifying an implementation against an approved design contract, locked decisions, or selected visual references (`/formforge-fidelity`).

## 1. Fidelity vs. Verify Distinction

- **Verify (`/formforge-verify`)**: Tests functional journeys, interactive states, responsiveness, accessibility, build health, and technical acceptance criteria.
- **Fidelity (`/formforge-fidelity`)**: Measures **agreement with approved creative and design intent**—comparing the actual implementation against approved design specs, locked decisions, `DESIGN.md`, or selected visual references.

## 2. 10-Dimension Contract Audit

Inspect rendered browser output (or static code/styles when browser rendering is unavailable, stating that limitation clearly) across:
1. **Approved Design Specifications**: Master prompt / design brief requirements and section structure.
2. **Locked Design Decisions**: Explicit user choices (palette polarity, nav pattern, density, CTA hierarchy).
3. **Selected Visual References**: Structural, typographic, and compositional alignment with chosen references.
4. **Typography Requirements**: Font families, weights, scale ratios, line heights, tracking, and truncation.
5. **Color Specifications**: Exact surface, ink, border, accent, and semantic state tokens.
6. **Layout Specifications**: Grid columns, container widths, alignment, proportions, and whitespace cadence.
7. **Component Appearance**: Radii, borders, elevation, iconography, and interactive state styling.
8. **Motion Specifications**: Trigger, duration, easing, choreography, and `prefers-reduced-motion` adherence.
9. **Responsive Requirements**: Breakpoint stacking, mobile navigation, and overflow-free scaling.
10. **Functional Requirements**: Core interactive behaviors specified in the design contract.

## 3. Deviation Classification & Remediation

- Classify every finding cleanly:
  - **Missing Requirement**: Specified element, state, or behavior absent.
  - **Incorrect Implementation**: Present but violates spec (wrong token, layout, timing, or behavior).
  - **Unapproved Visual Change / Design Drift**: Substituted style, generic card/gradient creep, or off-contract component.
  - **Responsive / Motion Discrepancy**: Breakpoint or animation mismatch against contract.
- Rank by severity (`Critical` -> `Major` -> `Minor`).
- **Read-Only Default**: Report findings first. Apply targeted corrections **only when authorized** by the user, reverify corrected behavior, and **never introduce subjective redesigns** that override approved decisions.
