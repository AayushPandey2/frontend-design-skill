"""Phase 01 structural and consistency validator for FORMFORGE."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    ".gitignore",
    "docs/architecture.md",
    "docs/capability-registry.json",
    "docs/roadmap.md",
    "evals/tasks.json",
    "evals/rubric.json",
    "scripts/validate_foundation.py",
]

REQUIRED_DOMAINS = {
    "FF-CR", "FF-VD", "FF-UX", "FF-DS", "FF-CP",
    "FF-MO", "FF-EN", "FF-SP", "FF-VF", "FF-OP",
}

ALLOWED_DECISIONS = {"RETAIN", "ADOPT", "MERGE", "REPLACE", "REWRITE", "REJECT", "DEFER"}

REQUIRED_CAP_FIELDS = {
    "id", "name", "domain", "decision", "purpose", "activation_conditions",
    "unified_behavior", "unique_value", "dependencies", "context_requirements",
    "implementation_complexity", "conflicts", "acceptance_criteria", "verification_status",
}

REQUIRED_EVAL_CATEGORIES = {
    "landing-page", "saas-dashboard", "ecommerce-interface", "creative-portfolio",
    "ai-application", "mobile-interface", "existing-component-mod",
    "responsive-layout-repair", "animation-implementation",
    "accessibility-remediation", "design-system-maintenance", "performance-optimization",
}

REQUIRED_GATES = {"functional_correctness", "accessibility", "security"}

REQUIRED_EFFICIENCY_METRICS = {
    "input_tokens", "output_tokens", "total_tokens", "context_loaded_bytes",
    "generated_code_size", "changed_files", "added_dependencies", "tool_calls",
    "execution_time_seconds", "cost_usd", "functional_test_results", "regression_failures",
}


def check_required_files(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"Missing required file: {rel}")
        elif path.stat().st_size == 0:
            errors.append(f"Empty required file: {rel}")


def check_skill_md(errors: list[str]) -> dict[str, int]:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, re.DOTALL)
    if not match:
        errors.append("SKILL.md: missing or malformed YAML frontmatter")
        return {}

    fm_raw, body = match.group(1), match.group(2)
    name_m = re.search(r"^name:\s*(.+)$", fm_raw, re.MULTILINE)
    desc_m = re.search(r"^description:\s*(.+)$", fm_raw, re.MULTILINE)
    lic_m = re.search(r"^license:\s*(.+)$", fm_raw, re.MULTILINE)

    if not name_m or name_m.group(1).strip() != "formforge":
        errors.append("SKILL.md: frontmatter 'name' must be 'formforge'")
    if not desc_m:
        errors.append("SKILL.md: frontmatter 'description' missing")
    else:
        desc = desc_m.group(1).strip()
        if not desc or len(desc) > 1024:
            errors.append(f"SKILL.md: 'description' length ({len(desc)}) must be 1..1024")
    if not lic_m or lic_m.group(1).strip() != "MIT":
        errors.append("SKILL.md: frontmatter 'license' must be 'MIT'")

    body_lines = body.strip().splitlines()
    if len(body_lines) > 250:
        errors.append(f"SKILL.md: body has {len(body_lines)} lines (limit 250)")

    words = len(text.split())
    return {
        "total_lines": len(text.splitlines()),
        "body_lines": len(body_lines),
        "words": words,
        "approx_tokens": int(words * 1.33),
    }


def check_markdown_links(errors: list[str]) -> int:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    checked = 0
    for rel in ["SKILL.md", "README.md", "docs/architecture.md", "docs/roadmap.md"]:
        md_path = ROOT / rel
        if not md_path.is_file():
            continue
        content = md_path.read_text(encoding="utf-8")
        for target in link_re.findall(content):
            if target.startswith(("http://", "https://", "#")):
                continue
            target_clean = target.split("#", 1)[0]
            resolved = (md_path.parent / target_clean).resolve()
            checked += 1
            if not resolved.exists():
                errors.append(f"{rel}: broken relative link '{target}'")
    return checked


def check_registry(errors: list[str]) -> set[str]:
    data = json.loads((ROOT / "docs/capability-registry.json").read_text(encoding="utf-8"))
    domains = {d["id"] for d in data.get("domains", [])}
    if domains != REQUIRED_DOMAINS:
        errors.append(f"capability-registry.json: domain mismatch {domains ^ REQUIRED_DOMAINS}")

    caps = data.get("capabilities", [])
    cap_ids = {c.get("id") for c in caps}
    if len(cap_ids) != len(caps):
        errors.append("capability-registry.json: duplicate capability IDs found")

    for cap in caps:
        cid = cap.get("id", "<unknown>")
        missing = REQUIRED_CAP_FIELDS - set(cap.keys())
        if missing:
            errors.append(f"{cid}: missing fields {sorted(missing)}")
        if cap.get("domain") not in REQUIRED_DOMAINS:
            errors.append(f"{cid}: invalid domain '{cap.get('domain')}'")
        if cap.get("decision") not in ALLOWED_DECISIONS:
            errors.append(f"{cid}: invalid decision '{cap.get('decision')}'")
        for dep in cap.get("dependencies", []):
            if dep not in cap_ids:
                errors.append(f"{cid}: unknown dependency '{dep}'")
    return cap_ids


def check_evals(errors: list[str], cap_ids: set[str]) -> tuple[int, int]:
    tasks_data = json.loads((ROOT / "evals/tasks.json").read_text(encoding="utf-8"))
    tasks = tasks_data.get("tasks", [])
    cats = {t.get("category") for t in tasks}
    if cats != REQUIRED_EVAL_CATEGORIES:
        errors.append(f"tasks.json: category mismatch {cats ^ REQUIRED_EVAL_CATEGORIES}")

    for task in tasks:
        tid = task.get("id", "<unknown>")
        for cid in task.get("required_capabilities", []):
            if cid not in cap_ids:
                errors.append(f"{tid}: unknown required capability '{cid}'")

    rubric = json.loads((ROOT / "evals/rubric.json").read_text(encoding="utf-8"))
    total_pts = sum(c.get("max_points", 0) for c in rubric.get("quality_categories", []))
    if total_pts != 100:
        errors.append(f"rubric.json: quality categories sum to {total_pts}, expected 100")

    gates = {g.get("id") for g in rubric.get("mandatory_gates", [])}
    if gates != REQUIRED_GATES:
        errors.append(f"rubric.json: gate mismatch {gates ^ REQUIRED_GATES}")

    eff = set(rubric.get("efficiency_metrics", []))
    if eff != REQUIRED_EFFICIENCY_METRICS:
        errors.append(f"rubric.json: efficiency metric mismatch {eff ^ REQUIRED_EFFICIENCY_METRICS}")

    return len(tasks), total_pts


def check_hygiene(errors: list[str]) -> None:
    placeholder_re = re.compile(r"\b(TODO|TBD|FIXME)\b")
    for rel in REQUIRED_FILES:
        if rel == "scripts/validate_foundation.py":
            continue
        path = ROOT / rel
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            if placeholder_re.search(text):
                errors.append(f"{rel}: contains unresolved placeholder (TODO/TBD/FIXME)")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    skill_stats = check_skill_md(errors)
    links_checked = check_markdown_links(errors)
    cap_ids = check_registry(errors)
    task_count, rubric_pts = check_evals(errors, cap_ids)
    check_hygiene(errors)

    if errors:
        print("VALIDATION FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("FORMFORGE Phase 01 Validation: PASSED")
    print(f"  SKILL.md: {skill_stats.get('total_lines')} total lines, "
          f"{skill_stats.get('body_lines')} body lines, "
          f"{skill_stats.get('words')} words (~{skill_stats.get('approx_tokens')} tokens)")
    print(f"  Relative links verified: {links_checked}")
    print(f"  Capabilities registered: {len(cap_ids)} across {len(REQUIRED_DOMAINS)} domains")
    print(f"  Eval tasks: {task_count} | Rubric total: {rubric_pts} pts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
