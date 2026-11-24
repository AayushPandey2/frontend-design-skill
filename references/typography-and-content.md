# Typography & Interface Content Intelligence

**Load when**: Selecting/pairing fonts, setting type scales, tuning readability/responsive text, or authoring UI copy.

## 1. Font Selection & Pairing

- **Selection criteria**: Product identity, audience, reading ergonomics, required weights, language/script support, licensing, performance, and existing project fonts. Reuse strong existing fonts; never invent font availability or ban widely used typefaces when composition is strong.
- **Pairing rules**: Default to 1–2 families:
  - Expressive display + restrained functional body.
  - Editorial serif + crisp sans-serif.
  - Neutral sans-serif + `tabular-nums` / monospace for financial or technical data.
  - Single versatile family differentiated by weight, size, and tracking.

## 2. Typographic Hierarchy

Assign clear functional roles: `display`, `page-title`, `section-heading`, `subheading`, `body`, `supporting`, `label`, `caption`, `metadata`, `numeric`, `interactive`.
- Combine **size, weight, contrast, position, spacing, alignment, and measure**—never rely on size alone or make everything bold.
- Preserve readable contrast on supporting/muted text.

## 3. Responsive Typography & Ergonomics

- Use CSS `clamp()` for fluid display/heading scales (never JS resize listeners).
- Cap mobile display sizes so headings do not push primary content and actions below the fold.
- Guard against long words, localization expansion, and narrow viewports (`overflow-wrap`, intentional wrapping).
- **Context-adapted ergonomics**: Long-form reading favors comfortable measure (~55–75ch) and generous line-height; dense dashboard tables favor compact, crisp alignment and tabular figures. Treat numeric guidelines as defaults, not rigid laws.

## 4. Typography Performance

- Load only needed weights/subsets; prefer variable fonts when multiple weights are used; define clean system fallback stacks; prevent layout shift (`font-display: swap` / metric-matched fallbacks).
- Never add remote font dependencies without considering availability, privacy, licensing, and latency.

## 5. Interface Copy & Content Intelligence

Copy is structural UI, not filler:
- **Clarity & voice**: Use plain, product-specific language and active outcome verbs on CTAs (e.g., "Publish changes", not "Submit"); match trigger labels to confirmation feedback.
- **State copy**: Write helpful, non-blaming error recovery ("Card declined—check expiry or try another card"), actionable empty states, and concise loading/success messages.
- **Anti-slop & honesty**: Eliminate generic hype, unnecessary adjectives, and placeholder-heavy slogans. Never invent customer testimonials, partner logos, certifications, or fake statistics; clearly label demonstration data when used.
