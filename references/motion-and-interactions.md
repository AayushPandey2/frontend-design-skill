# Motion, Micro-Interactions & Gesture Engineering

**Load when**: Implementing UI transitions, choreography, micro-interactions, drag/swipe gestures, layout transitions, or scroll effects.

## 1. Motion Ladder, Timing, Easing & Springs

Check what changes, why it moves, frequency, interruptibility, reduced-motion behavior, and cost first. Pick the simplest mechanism:
1. No motion -> 2. CSS transitions -> 3. CSS keyframes -> 4. WAAPI -> 5. Existing utils/libs -> 6. Justified dependency (never install an animation library for hover/fades).
- **Timing heuristics** (keep frequent interactions fast): feedback `80–150ms`, small states `120–220ms`, menus/popovers `150–250ms`, dialogs/drawers `180–350ms`, spatial `250–500ms`.
- **Easing & springs**: `ease-out` (enter/response), `ease-in` (exit), `ease-in-out` (move), `linear` (continuous). Use springs (stiffness/damping/velocity) for drag, sliders, and reversible spatial transitions—not opacity fades or bouncy overshoot.

## 2. Interruptibility, Choreography, Micro-Interactions & Gestures

- **Interruptibility & choreography**: Support mid-flight reversal and rapid toggling without stale state; never gate critical logic solely on `animationend`/`transitionend`. Focus choreography on one focal sequence without blocking primary tasks.
- **Micro-interactions & gestures**: Keep press/toggle/copy/tab feedback CSS-first; never hover-lock essential actions. For drag/swipe/reorder/sliders, manage pointer capture, thresholds, cancellation, native scroll conflicts, and provide keyboard alternatives.

## 3. Performance & Reduced Motion

- Animate `transform`/`opacity` rather than `width`/`height`/`top`/`left` or large blurs; use `will-change` sparingly; prefer native scroll and CSS/observer reveals without scroll hijacking; clean up timers/RAF/observers. Never claim unmeasured FPS.
- Under `prefers-reduced-motion: reduce`, replace large spatial/parallax/zoom motion with instant updates, subtle opacity shifts, or non-motion cues.
