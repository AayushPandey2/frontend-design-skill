# Interactive Design Planning Mode (`/formforge-plan`)

**Load when**: User invokes `/formforge-plan` or asks to plan a frontend interactively before coding.

## 1. Read-Only Boundary & Operating Contract

- **Strict read-only mode**: Never edit frontend source files, install dependencies, alter project configs, create unnecessary files, or auto-execute the generated prompt. Read-only inspection of an existing repo is permitted.
- **Contract**: `Discover -> Explore -> Compare -> Select -> Specify -> Confirm -> Consolidate -> Generate`.
- **Progressive consultation**: Ask focused questions in logical stages (never a giant upfront questionnaire); skip irrelevant stages; never repeat answered questions; offer clear expert recommendations when the user is unsure.

## 2. Adaptive Depths & Natural-Language Controls

- **Express**: User already has a clear direction -> confirm product objective, visual identity, required functionality, core layout, and tech constraints; label inferred low-risk defaults.
- **Guided (Default)**: Progressive consultation using visual references, trade-offs, and recommendations across relevant design/engineering stages.
- **Exhaustive**: High-fidelity specs covering page, section, component, interaction, motion choreography, responsive rules, technical architecture, and acceptance criteria.
- **Controls** (interpret naturally, no strict syntax): `Quick plan`, `Detailed plan`, `Exhaustive plan`, `Recommend the best option`, `Decide this for me`, `Skip this section`, `Show more examples`, `Show different styles`, `Combine these two options`, `Change my previous selection`, `Go back to <stage>`, `Review my current selections`, `Finish planning`, `Generate the final prompt`.

## 3. Progressive Consultation Stages (1–15)

Load existing `references/` modules selectively as needed—never duplicate their full rules here:
1. **Product discovery**: Product type, purpose, audience, user/business goals, primary action, pages, features, existing brand/site, inspiration, tone, content, devices, tech constraints. Separate explicit facts from assumptions.
2. **Visual direction**: Present 2–4 product-fit directions (never identical styles across unrelated products) with trade-offs and complexity; combine only compatible traits.
3. **Typography** ([typography-and-content.md](typography-and-content.md)): Heading/body families, weights, fallbacks, fluid/desktop/mobile scale, line-height, tracking, loading; reuse existing fonts when strong.
4. **Color** ([color-and-surfaces.md](color-and-surfaces.md)): Light/dark/both, dominant bg, accents, surfaces, text, borders, status/dataviz hex values, WCAG contrast; never silently alter locked brand colors (flag contrast conflicts with proposed fixes).
5. **Layout & composition** ([layout-and-responsive.md](layout-and-responsive.md)): Hero type, grid/columns, max-width, margins/gutters, alignment, density, whitespace, desktop/mobile wireframes without requiring CSS jargon.
6. **Page architecture**: Pages, entry points, objectives, primary/secondary actions, section order, states, nav links (product-specific, never force one homepage template).
7. **Section-level spec**: Purpose, content, layout, alignment, type, color, media, actions, spacing, responsive shifts, motion (consolidate on smaller projects; distinguish agent-derived values from user-approved ones).
8. **Component design** ([ux-and-systems.md](ux-and-systems.md)): Establish shared conventions/radii/surfaces/states for relevant components; allow per-component overrides.
9. **Surface & material**: Flat, borders, shadows, elevation, glass/blur, gradients, texture, radii, and explicit decorative restrictions.
10. **Image & asset direction**: Subject, art direction, aspect ratio, cropping, licensing, and source (`user-provided`, `authorized`, `generated`, `implementation`, or `labeled placeholder`); never invent paths.
11. **Motion & animation** ([motion-and-interactions.md](motion-and-interactions.md)): Choose intensity (`none`, `subtle functional`, `refined expressive`, `cinematic`, `highly interactive`); show previews when supported or describe movement precisely. For each key animation, record a **Motion Specification Contract**: `name | target | trigger | initial -> final state | properties | duration | delay | easing/spring | stagger | direction | interrupt/reversal | repeat | responsive delta | reduced-motion fallback | perf constraints`.
12. **UX & functional flows**: Relevant flows (`trigger | behavior | data | loading/empty/error/success | a11y`), distinguishing frontend from backend and live APIs from labeled sample data.
13. **Responsive adaptation**: Concrete nav, grid, stacking, media, type, spacing, table, touch (`>= 44px`), and motion rules per viewport.
14. **Technical constraints**: Existing vs. new stack, styling, libraries, backend/API availability, browser/a11y/perf targets; preserve existing stack and native-first economy.
15. **Content & copy**: Exact user copy vs. approved generated copy vs. pending user copy vs. labeled demo content; zero fabricated testimonials, stats, or partnerships.

## 4. Web Visual Reference Intelligence & Decision Contract

- **Visual references**: When browsing is supported, search for 3–6 real interface examples (not stock photos); display inline images if supported, or verified clickable links + concise descriptions if not; if browsing is unavailable, state the limitation and use descriptive alternatives. Never fabricate URLs or images.
- **Reference interpretation**: For each selected reference (`R01`, `R02`, ...), record `Source URL`, `Approved` traits, `Rejected` traits, `Not Selected` parts, and affected sections; never instruct copying proprietary logos/assets.
- **Decision classification**: Classify every decision as `LOCKED` (must preserve), `PREFERRED` (adjust only with explanation), `FLEXIBLE` (agent-delegated), `REJECTED` (avoid), or `UNRESOLVED` (still open).
- **Running contract & conflicts**: Track deltas concisely without repeating the whole contract every turn; allow revisions anytime; surface conflicts (e.g., dense data + excessive whitespace, low contrast) and get user confirmation on user-facing trade-offs.
- **Final visual confirmation**: Present a compact summary of approved choices and open assumptions before generating [master-prompt-spec.md](master-prompt-spec.md).
