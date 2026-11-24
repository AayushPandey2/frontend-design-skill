# FORMFORGE Comparative Benchmark & Ablation Protocol

## 1. Lifecycle & Baselines
Lifecycle: `Define -> Control -> Execute -> Observe -> Measure -> Compare -> Diagnose -> Improve -> Reverify`.
- **`B0` (No-skill)**: Same coding agent and prompt with FORMFORGE inactive.
- **`B1` (Foundational)**: Commit `5338b45` (`formforge/phase-01-foundation`).
- **`B2` (Pre-optimization)**: Commit `c3165d1` (`formforge/phase-05-verification-intelligence`).
- **`B3` (Current)**: Commit `9368df9` (`formforge/phase-06-optimization`) / current `HEAD`.
- **`B4` (Anonymous comparisons)**: External configurations labeled `Comparison A`, `Comparison B`, `Comparison C` (keep exact mappings private).
- **`B5` (Ablations `A01`–`A10`)**: Isolated Git worktrees or temporary skill copies with one capability group removed; never add feature flags to production skill files.

## 2. Controlled Experiment Rules
Hold constant across compared runs: model & version, reasoning config, prompt, starting project/deps, tools, browser/viewports, test data, rubric, and resource budget.
- Run in isolated sessions (no inherited outputs, design memory, or hidden defect lists/answers).
- When resources allow, execute `>= 3` independent trials per task/configuration; report attempted, completed, and successful runs, mean, median, min, max, variability, and failure rate (never drop failed runs).

## 3. Scoring, Quality Gates & Blind Visual Evaluation
- **Global rubric (`100` pts)**: Anchor each applicable dimension (`Poor`, `Below expectations`, `Acceptable`, `Strong`, `Exceptional`) with observed evidence; mark genuinely N/A dimensions and normalize transparently; never convert `UNVERIFIED` to passing.
- **7 Mandatory Gates** (`PASS`, `FAIL`, `UNVERIFIED`, `NOT APPLICABLE`): Required functionality, critical accessibility, security, required responsiveness, explicit user requirements, verification integrity, regression prevention. A failed gate disqualifies superiority regardless of visual score or token savings.
- **Blind visual evaluation**: Strip configuration IDs, randomize order, withhold generator self-assessment, collect independent ratings on rendered desktop/mobile/state captures, and reveal IDs only afterward.

## 4. Measurement & Evidence Integrity
- **Tokens**: Track instruction, loaded reference, source, tool-result, input, output, cached, and reasoning tokens without double-counting; include planning, inspection, verification, and refinement. Distinguish provider-reported, tokenizer-derived, estimated, and unavailable counts.
- **Code & tools**: Measure added/removed/net source lines (excluding `node_modules`/lockfiles/binaries), changed files, new abstractions, added deps, dead code/redundant state, total tool calls, unnecessary tool calls, and elapsed time.
- **Defect detection**: Record `TP`, `FP`, `FN`, `precision = TP/(TP+FP)`, `recall = TP/(TP+FN)`, `F1`, `correction_rate = verified_resolved/confirmed_detected`, `end_to_end_resolution = verified_resolved/total_seeded`, `regression_count`.
- **Comparative deltas**: `((Baseline - FORMFORGE) / Baseline) * 100` for tokens/code/time/cost; `FORMFORGE_score - Baseline_score` in points for quality. Never hide negative outcomes.
- **Evidence labels**: `MEASURED`, `ESTIMATED`, `STRUCTURAL CHECK`, `SIMULATED`, `SELF-ASSESSED`, `INDEPENDENTLY REVIEWED`, `NOT EXECUTED`, `UNVERIFIED`, `NOT APPLICABLE`.

## 5. Staged Execution, Holdouts & Readiness
Execute in order: `Stage A` (Structural validation) -> `Stage B` (Pilot) -> `Stage C` (Targeted) -> `Stage D` (Ablation) -> `Stage E` (Regression) -> `Stage F` (Reserved holdouts `H01`–`H03`) -> `Stage G` (Final report).
- **Readiness**: `NOT READY` | `EXPERIMENTAL` (operational, real-world execution unverified) | `BETA READY` (representative tasks & gates verified) | `RELEASE READY` (comprehensive evidence, zero critical blockers).
