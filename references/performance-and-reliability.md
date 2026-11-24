# Performance, Asset Optimization, Data Viz & Security

**Load when**: Optimizing Core Web Vitals, bundles, images/fonts, data visualizations, or frontend security.

## 1. Core Web Vitals & Asset Discipline

- **CWV targets** (field p75; distinguish lab from field): `LCP <= 2.5s`, `INP <= 200ms`, `CLS <= 0.1`. Protocol: `identify bottleneck -> measure -> inspect -> minimal fix -> re-measure -> regression check`. Avoid premature optimization.
- **Bundles**: Check existing packages and native APIs first; remove duplicate icon/utility/animation libs; code-split heavy offscreen modules. Never claim bundle savings without measurement.
- **Images & fonts**: Never lazy-load primary LCP hero images (`fetchpriority="high"` when helpful); reserve dimensions/`aspect-ratio`; use modern formats and `srcset`; load needed font weights only with `font-display: swap`; never reference nonexistent assets.

## 2. Data Visualization & Security

- **Data viz**: Reuse existing charting tools or native HTML/SVG for simple indicators; provide accurate labels, units, legends, tooltips, keyboard/text access, and empty/loading/error states. Label sample data; never invent datasets.
- **Security**: Prevent XSS (no unsanitized `dangerouslySetInnerHTML`/`v-html`/`{@html}`), validate external URLs (`https:`/`http:` only), use `rel="noopener noreferrer"`, keep secrets off client bundles, never treat hidden UI as authorization, and guard duplicate submits/destructive actions/race conditions.
