# Typography & Interface Content Intelligence

**Load when**: Selecting/pairing fonts, setting type scales, tuning readability/responsive text, or authoring UI copy.

## 1. Font Selection, Pairing & Performance

- **Select by**: product identity, audience, reading ergonomics, required weights, script support, licensing, performance, and existing project fonts. Reuse strong existing fonts; never invent availability or ban common typefaces when composition is strong.
- **Pair 1–2 families**: expressive display + restrained body; editorial serif + crisp sans; neutral sans + `tabular-nums`/monospace for data; or one versatile family differentiated by weight/scale/tracking.
- **Performance**: Load needed weights/subsets only; prefer variable fonts when multi-weight; set fallback stacks and `font-display: swap` to prevent CLS; weigh privacy/latency before adding remote fonts.

## 2. Hierarchy & Responsive Ergonomics

- **11 functional roles**: `display`, `page-title`, `section-heading`, `subheading`, `body`, `supporting`, `label`, `caption`, `metadata`, `numeric`, `interactive`. Combine size, weight, contrast, spacing, alignment, and measure—not size alone.
- **Responsive**: Scale display/headings with CSS `clamp()` (no JS); cap mobile display size so primary content/actions stay visible; guard long words/localization (`overflow-wrap`).
- **Ergonomics**: Long-form reading favors ~55–75ch measure and generous line-height; dense tables favor compact alignment and `tabular-nums`.

## 3. Interface Copy & Content Integrity

- Use plain, product-specific language and active outcome verbs on CTAs ("Publish changes", not "Submit"); match trigger and confirmation labels.
- Write helpful, non-blaming error recovery, actionable empty states, and concise loading/success copy.
- Eliminate filler hype and fake slogans. Never invent testimonials, partner logos, or metrics; label demonstration data clearly.
