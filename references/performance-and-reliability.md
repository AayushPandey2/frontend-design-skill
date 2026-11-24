# Performance, Asset Optimization, Data Viz & Security

**Load when**: Optimizing Core Web Vitals, bundles, images/fonts, charts/data visualizations, or frontend reliability and security.

## 1. Core Web Vitals & Performance Protocol

- **Targets** (field 75th percentile; distinguish lab checks from real-user field telemetry): `LCP <= 2.5s`, `INP <= 200ms`, `CLS <= 0.1`.
- **Protocol**: 1. Identify suspected bottleneck -> 2. Measure where supported -> 3. Inspect implementation -> 4. Apply smallest root-cause fix -> 5. Re-measure -> 6. Check regressions. Avoid premature optimization.

## 2. Bundle, Asset & Font Optimization

- **Dependencies**: Check existing packages and native browser APIs first. Eliminate duplicate icon/utility/state libraries and unnecessary animation packages; code-split heavy offscreen modules. Never claim bundle savings without measurement.
- **Images & media**: Never lazy-load the primary above-the-fold LCP hero image (`fetchpriority="high"` where helpful); set explicit width/height or `aspect-ratio` to prevent CLS; use modern compressed formats and responsive `srcset`; never reference nonexistent asset paths.
- **Fonts**: Load only required families/weights/subsets; use clean fallback stacks and `font-display: swap`; avoid unnecessary preloads that starve critical assets.

## 3. Data Visualization Engineering

- Reuse existing charting tools or native HTML/SVG for simple progress/sparklines before adding chart libraries.
- Include accurate axis labels, units, legends, tooltips, keyboard/text value access, and explicit empty/loading/error states. Never invent datasets; clearly label sample data.

## 4. Frontend Reliability & Security

- **Safe rendering**: Prevent XSS—avoid `dangerouslySetInnerHTML`/`v-html`/`{@html}` with untrusted input, validate external URLs (`https:`/`http:` only), and use `rel="noopener noreferrer"` where needed.
- **Trust boundaries**: Never expose secrets in client bundles, never treat hidden UI elements as authorization, and preserve server-side validation for security-sensitive operations. Guard against duplicate submissions, accidental destructive actions, and async race conditions.
