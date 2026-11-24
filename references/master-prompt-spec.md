# Master Implementation Prompt Specification

**Load when**: Generating the final standalone implementation prompt at the end of `/formforge-plan`.

## 1. Output Structure (3 Parts, Read-Only)

Present these three parts in order without modifying repository files or starting implementation:
1. **A. Final Design Summary**: Compact human-readable overview of the approved experience.
2. **B. Master Implementation Prompt**: One self-contained, copyable code/text block usable in a fresh coding-agent conversation—with or without FORMFORGE installed (never auto-execute).
3. **C. Optional Reference & Asset Index**: Verified reference URLs, approved/rejected traits, and asset responsibilities/fallbacks when needed.

## 2. Applicable Master Prompt Sections

Include only sections relevant to the project (zero empty sections, zero repeated global prose):
- **Identity & Context**: Project identity, objective, product description, target audience, user goals.
- **Decisions & References**: Creative direction; `LOCKED`, `PREFERRED`, `REJECTED`, `FLEXIBLE`, and `UNRESOLVED` decisions; approved visual references (`ID | URL | visual description fallback | approved/rejected traits | target sections`).
- **Design System & Tokens**: Concrete values/formulas for colors (bg, surface, elevated, primary/secondary text, accent, border, focus, status), typography (families, weights, sizes/fluid `clamp()`, line-heights, letter-spacing, fallbacks), spacing, radii, shadows, container widths, and motion durations/easing—distinguishing fixed values from proposed defaults.
- **Structure & Behavior**: Layout/grid system, surface/material rules, page architecture, section-by-section specs, component specs, content/copy rules (marking immutable copy vs. demo data), asset direction/fallbacks, interactions, **Motion Specification Contracts**, responsive adaptation rules, functional flows, and data/backend scope (live APIs vs. labeled sample data).
- **Engineering & Quality**: Technical constraints (preserve existing stack), WCAG 2.2 AA accessibility, performance, implementation economy (smallest complete native-first solution), verification requirements, verifiable acceptance criteria, delegated decisions, and known limitations/assumptions.

## 3. Implementation Fidelity & Deviation Protocol

Instruct the receiving coding agent inside the prompt to:
1. Read the entire specification and inspect existing project code before editing.
2. Preserve all `LOCKED` decisions (direction, typography, semantic colors, page/section structure, component behavior, motion specs, responsive rules) without unapproved decorative reinterpretation or framework migration.
3. Implement the smallest complete solution, render the output when tools allow, compare against the specification, verify interactions, and fix discrepancies.
4. Report any unavoidable deviation (e.g., accessibility, missing assets, framework/API limits, security) using: `Original Requirement | Implemented Behavior | Reason | Evidence | User Approval Needed`. Never promise pixel-perfect reproduction from text alone, and never falsely claim attachments auto-transfer to fresh sessions.
