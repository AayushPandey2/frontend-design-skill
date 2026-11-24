# Motion, Micro-Interactions & Gesture Engineering

**Load when**: Implementing UI transitions, choreography, micro-interactions, drag/swipe gestures, layout transitions, or scroll effects.

## 1. Motion Decision Ladder & Timing

Before animating, verify what changes, why it moves, frequency, interruptibility, reduced-motion behavior, and cost. Choose the simplest sufficient mechanism:
1. No motion -> 2. CSS transitions -> 3. CSS keyframes -> 4. Web Animations API -> 5. Existing project utils/libs -> 6. Justified dependency (never install an animation library for hover/simple fades).

- **Timing heuristics** (adjust for distance, size, and frequency; keep frequent tasks fast): immediate feedback `80–150ms`, small state changes `120–220ms`, menus/popovers `150–250ms`, dialogs/drawers `180–350ms`, larger spatial transitions `250–500ms`.
- **Easing**: `ease-out` for entering/immediate responses, `ease-in` for exits, `ease-in-out` for state-to-state moves, `linear` for continuous progress. Avoid dramatic overshoot on routine UI.
- **Springs**: Use stiffness/damping/velocity physics for drag, sliders, and reversible spatial transitions—not simple opacity fades. Avoid bouncy overshoot or building a custom spring engine.

## 2. Interruptibility, Choreography & Layout/Scroll Motion

- **Interruptibility**: Allow mid-flight reversal and rapid toggling without stale state; never gate critical app logic solely on `animationend`/`transitionend`.
- **Choreography**: Anchor attention on one focal sequence; avoid cascading staggers that delay content or hide essential UI if JS fails.
- **Layout & scroll**: Use transform-based continuity or native view transitions without layout thrashing. Prefer native scroll and CSS/observer reveals—never hijack wheel/touch scrolling or attach heavy synchronous scroll listeners.

## 3. Micro-Interactions & Gestures

- Keep press, toggle, copy, tab, and expand feedback crisp and CSS-first; never lock essential actions behind hover.
- For drag, swipe, reorder, or sliders: manage pointer capture, movement thresholds, cancellation, and scroll conflicts—and always provide accessible keyboard alternatives.

## 4. Performance & Reduced Motion

- Animate `transform` and `opacity` rather than `width`/`height`/`top`/`left` or large blurs; use `will-change` sparingly; clean up timers, `requestAnimationFrame`, and observers. Never claim a frame rate without measurement.
- Under `prefers-reduced-motion: reduce`, replace large spatial/parallax/zoom motion with instant updates, subtle opacity shifts, or non-motion state cues.
