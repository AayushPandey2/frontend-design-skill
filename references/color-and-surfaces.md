# Color, Contrast & Surface Intelligence

**Load when**: Creating a palette, extending theme tokens, building dark mode, or designing elevation/surfaces.

## 1. Semantic Color System & Palette Workflow

Map colors by functional role rather than raw hex names (`canvas`, `surface`, `elevated-surface`, `border`, `text-primary`/`secondary`/`muted`, `action-primary`/`secondary`, `accent`, `focus-ring`, `selection`, `success`/`warning`/`error`/`info`, `disabled`, `dataviz`). Reuse existing tokens; skip 10-step scales for single-use colors.

**Palette steps**: 1. Product tone -> 2. Dominant neutral base -> 3. 1–2 intentional accents (no arbitrary color bans) -> 4. Semantic roles & interactive states -> 5. Contrast check (see [accessibility-engineering.md](accessibility-engineering.md)) -> 6. Prune unused colors. Never communicate status or chart series by color alone.

## 2. Light & Dark Modes

Build dark mode only when requested or standard for the repo. **Never invert blindly**: step dark surfaces by elevation (higher = slightly lighter), reduce glare, soften harsh borders, desaturate bright accents slightly, and tune media/shadow contrast while preserving brand identity.

## 3. Materiality, Elevation & Surfaces

Apply flat surfaces, borders, shadows, overlays, blur, gradients, textures, and corner radii under one coherent rationale:
- **Borders** for crisp separation; **shadows/elevation** for overlays/popovers; **blur/transparency** sparingly for layered chrome; **textures/gradients** only when reinforcing material character.
- **Avoid**: stacking shadows + heavy borders + blur + gradients together, mismatched nested radii, or expensive blur filters where flat surfaces work.
