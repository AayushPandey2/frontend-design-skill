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

## 4. Advanced Motion Patterns (Native-First)

Apply sophisticated motion **only when justified by product clarity or storytelling**, never as mandatory decoration. Prefer CSS (`@starting-style`, `view-transition-name`, `animation-timeline: view()`, `scroll-snap-type`), WAAPI, and IntersectionObserver before adding animation libraries:
- **Micro-Interactions & Hover/Press Feedback**: Instantaneous scale/translate/border-color response (`80–150ms`), tactile press compression, and focus-visible continuity.
- **Entrance/Exit & Staggered Animations**: Coordinated focal sequence with short stagger (`30–60ms` per item, capped total delay so content never feels sluggish).
- **Page & Shared-Element Transitions**: Native View Transitions API (`document.startViewTransition` / CSS cross-document transitions) for continuous spatial context across views.
- **Layout Animations**: Smooth reordering, expand/collapse, and tab-indicator glides using FLIP or CSS Grid/View Transitions without layout thrash.
- **Scroll-Driven Animations & Scroll Storytelling**: Native CSS `scroll()` / `view()` timelines or passive observer reveals; preserve natural user scroll velocity (no scroll hijacking).
- **Image/Text Reveals & Interactive Typography**: Masked clip-path/opacity reveals, subtle variable-font weight/width response, and readable contrast throughout.
- **Magnetic Interactions & Parallax**: Subtle pointer-tracking or depth offset strictly on pointer-fine devices, clamped to small bounds, disabled under reduced motion and touch.
- **Gesture Interactions, Dragging & Reordering**: Pointer-capture drag, velocity-aware spring release, clear drop indicators, cancel on `Escape`, and full keyboard reordering alternatives.

## 5. 12-Point Animation Specification Contract

For every significant animation or interactive transition, specify:
1. **Trigger**: Hover, press, focus, mount, scroll threshold, drag, or route change.
2. **Initial State**: Exact starting `transform`, `opacity`, clip, or layout values.
3. **Final State**: Exact resting values.
4. **Animated Properties**: Compositor-safe properties (`transform`, `opacity`, `clip-path`, `filter` sparingly).
5. **Duration**: Exact ms or spring physics parameters.
6. **Delay**: Exact ms (or `0ms`).
7. **Easing**: CSS `cubic-bezier(...)` or spring stiffness/damping/mass.
8. **Stagger**: Per-item offset and maximum cap.
9. **Interruption Behavior**: Mid-flight reversal, cancel, or retargeting rule.
10. **Repeat Behavior**: Once, on-reenter, or bounded loop.
11. **Responsive Behavior**: Touch/small-viewport adaptation or simplification.
12. **Reduced-Motion Alternative**: Exact `prefers-reduced-motion: reduce` fallback.
