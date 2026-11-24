# Project Design DNA & Persistent Identity

**Load when**: Extracting, creating, updating, applying, or checking drift against persistent project-specific design identity (`/formforge-dna`).

## 1. Core Principle: Code Is Authoritative

- Existing code, CSS variables, theme files, and design tokens are the **authoritative source** for exact implementation values.
- Maintain a lightweight `DESIGN.md` at the project root **only when justified** (multi-page/multi-session projects needing stable creative and architectural decisions). Never duplicate token tables or component props already cleanly expressed in code.
- **Security & Privacy Gate**: Never persist API keys, credentials, tokens, internal URLs, PII, or confidential business data in `DESIGN.md`.

## 2. 11-Point Design DNA Schema

Extract or define concise, durable conventions:
1. **Product Identity**: Product purpose, audience, and domain posture.
2. **Brand Personality**: 3–5 concrete tonal attributes (e.g., *editorial, technical, calm*—not vague buzzwords).
3. **Typography Conventions**: Font roles, hierarchy rules, numeric styling, line-length limits.
4. **Color Conventions**: Surface/ink hierarchy, semantic usage rules, light/dark polarity.
5. **Layout Principles**: Container widths, grid discipline, section cadence, density target.
6. **Spacing Conventions**: Scale rhythm and component-to-section proportion rules.
7. **Component Patterns**: Canonical primitives, button/input hierarchy, state conventions.
8. **Surface Treatments**: Border-vs-shadow philosophy, radius system, elevation limits.
9. **Motion Conventions**: Timing tier, easing character, reduced-motion contract.
10. **Design Restrictions**: Explicit non-goals and banned patterns for this project.
11. **User-Approved Preferences**: Locked choices from `/formforge-plan`, `/formforge-explore`, or reviews.

## 3. Supported Workflows

- **Extract**: Inspect existing styles, tokens, layouts, and components to document the implicit Design DNA without inventing unverified conventions.
- **Create**: Establish initial Design DNA for a new project and write a concise `DESIGN.md` when authorized.
- **Update**: Record newly approved design decisions while preserving non-conflicting conventions.
- **Apply**: Inject existing `DESIGN.md` + token constraints into new pages/features before coding.
- **Drift Detection**: Compare new or modified UI against `DESIGN.md` and authoritative tokens; report ad-hoc colors, off-scale spacing, mismatched typography, or unapproved patterns.
