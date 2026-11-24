# Visual Inspiration, Creative Exploration & Asset Direction

**Load when**: Discovering real-world web inspiration (`/formforge-inspire`), generating distinct creative directions/moodboards (`/formforge-explore`), or planning visual assets (`/formforge-assets`).

## 1. Inspiration Discovery (`/formforge-inspire`) — STRICT READ-ONLY

- **Never automatically implement code** during inspiration discovery.
- **Workflow**:
  1. Clarify the product domain, target audience, emotional tone, and requested aesthetic.
  2. Search for real-world, live web design examples relevant to the domain (avoid generic stock galleries and fabricated URLs/screenshots).
  3. Present verified clickable reference links; display inline screenshots/images only when supported by the host environment, otherwise provide concise visual descriptions and verified links.
  4. Explain *why* each reference works: specific typography choices, layout composition, color/surface restraint, and interaction patterns worth borrowing—plus what to avoid.
  5. Invite the user to select preferred traits or feed them into `/formforge-explore` or `/formforge-plan`.

## 2. Creative Exploration & Moodboards (`/formforge-explore`) — STRICT READ-ONLY

- **Never automatically implement code** during exploration.
- Generate **2–4 genuinely distinct creative directions** tailored to the product. Never produce superficial variants that differ only in accent color.
- **Required 10-Part Direction Card**:
  1. **Visual Identity**: Name, mood, and one-line positioning.
  2. **Design Philosophy**: Core tension, restraint, and user-experience thesis.
  3. **Representative Web References**: Verified real-world sites or authentic aesthetic anchors.
  4. **Typography**: Display + body + mono pairing, scale character, and tone.
  5. **Color Palette**: Surface, ink, border, and accent roles with contrast rationale.
  6. **Layout Direction**: Grid, density, rhythm, and focal composition.
  7. **Component Character**: Radii, borders, elevation, and control density.
  8. **Asset Direction**: Photography/illustration/iconography style and framing.
  9. **Motion Character**: Pacing, easing personality, and restraint level.
  10. **Advantages & Trade-Offs**: Strengths, engineering cost, and maintenance risks.
- Allow users to select one direction, reject options, or combine compatible traits, then optionally hand off approved decisions to `/formforge-plan`.

## 3. Visual Asset Discovery & Planning (`/formforge-assets`)

- Cover photography, illustrations, icon systems, textures/patterns, videos, and product imagery.
- **For every asset slot, specify**:
  - **Direction & Subject**: Concrete visual content, lighting, composition, and mood matching the product.
  - **Source & Licensing**: Verified open/licensed source, user-supplied asset, or bespoke asset brief—**never fabricate asset URLs or claim unverified availability**.
  - **Placement & Cropping**: Aspect ratio, focal point (`object-position`), responsive `srcset`/`sizes`, and safe-area margins.
  - **Accessibility & Performance**: Meaningful `alt` text (or `alt=""` for decorative), format (`AVIF`/`WebP`/inline SVG), lazy vs. eager LCP priority, explicit dimensions to prevent CLS.
