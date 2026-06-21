from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import json
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class AgentAuditConfig:
    article: str = "ai_agents_tool_use_and_procedural_autonomy"
    max_steps_without_review: int = 3
    escalation_threshold: float = 0.65
    require_approval_for_write_actions: bool = True


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def tool_registry() -> list[dict[str, object]]:
    return [
        {"tool": "document_search", "action_type": "read", "risk": 0.20, "approval_required": 0, "permission_scope": "selected_documents"},
        {"tool": "calculator", "action_type": "compute", "risk": 0.10, "approval_required": 0, "permission_scope": "local_calculation"},
        {"tool": "code_runner", "action_type": "execute", "risk": 0.55, "approval_required": 1, "permission_scope": "sandbox_only"},
        {"tool": "email_draft", "action_type": "draft", "risk": 0.35, "approval_required": 0, "permission_scope": "draft_only"},
        {"tool": "email_send", "action_type": "external_write", "risk": 0.85, "approval_required": 1, "permission_scope": "external_communication"},
        {"tool": "database_update", "action_type": "write", "risk": 0.90, "approval_required": 1, "permission_scope": "restricted_records"},
        {"tool": "shell_command", "action_type": "execute", "risk": 0.95, "approval_required": 1, "permission_scope": "blocked_by_default"},
    ]


def planned_actions() -> list[dict[str, object]]:
    return [
        {"step": 1, "task": "research brief", "tool": "document_search", "approved": 1, "observation_quality": 0.90, "instruction_source": "user"},
        {"step": 2, "task": "research brief", "tool": "calculator", "approved": 1, "observation_quality": 0.95, "instruction_source": "system"},
        {"step": 3, "task": "research brief", "tool": "email_draft", "approved": 1, "observation_quality": 0.80, "instruction_source": "user"},
        {"step": 4, "task": "send brief", "tool": "email_send", "approved": 0, "observation_quality": 0.70, "instruction_source": "model_plan"},
        {"step": 5, "task": "update record", "tool": "database_update", "approved": 0, "observation_quality": 0.60, "instruction_source": "retrieved_document"},
        {"step": 6, "task": "debug script", "tool": "shell_command", "approved": 0, "observation_quality": 0.45, "instruction_source": "untrusted_tool_output"},
    ]


def registry_lookup() -> dict[str, dict[str, object]]:
    return {str(row["tool"]): row for row in tool_registry()}


def audit_actions(config: AgentAuditConfig) -> list[dict[str, object]]:
    lookup = registry_lookup()
    audited = []
    for action in planned_actions():
        tool = str(action["tool"])
        metadata = lookup[tool]
        risk = float(metadata["risk"])
        approval_required = int(metadata["approval_required"])
        approved = int(action["approved"])
        approval_violation = int(approval_required == 1 and approved == 0)
        step_limit_violation = int(int(action["step"]) > config.max_steps_without_review)
        untrusted_instruction = int(str(action["instruction_source"]) in {"retrieved_document", "untrusted_tool_output"})
        escalation_required = int(
            risk >= config.escalation_threshold
            or approval_violation == 1
            or step_limit_violation == 1
            or untrusted_instruction == 1
        )
        status = "pass"
        if approval_violation:
            status = "blocked"
        elif escalation_required:
            status = "escalate"

        audited.append({
            "step": action["step"],
            "task": action["task"],
            "tool": tool,
            "action_type": metadata["action_type"],
            "permission_scope": metadata["permission_scope"],
            "tool_risk": round(risk, 6),
            "approved": approved,
            "approval_required": approval_required,
            "approval_violation": approval_violation,
            "step_limit_violation": step_limit_violation,
            "instruction_source": action["instruction_source"],
            "untrusted_instruction": untrusted_instruction,
            "observation_quality": action["observation_quality"],
            "escalation_required": escalation_required,
            "status": status,
            "interpretation": "Agent tool use should remain within permission, step, risk, instruction-source, and approval boundaries.",
        })
    return audited


def prompt_injection_checks() -> list[dict[str, object]]:
    return [
        {
            "scenario": "retrieved_document_contains_instruction",
            "risk": "Untrusted document tells agent to ignore system instructions.",
            "control": "Treat retrieved content as data, not instruction.",
            "status": "required",
        },
        {
            "scenario": "tool_output_contains_command",
            "risk": "External tool output asks agent to execute a hidden command.",
            "control": "Validate tool outputs and block command execution without approval.",
            "status": "required",
        },
        {
            "scenario": "credential_exfiltration_request",
            "risk": "Prompt attempts to reveal secrets or private data.",
            "control": "Deny access and log incident.",
            "status": "required",
        },
    ]


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "intended_use", "review_question": "What workflow may the agent support?", "status": "required"},
        {"item": "tool_permissions", "review_question": "Which tools are allowed for this task?", "status": "required"},
        {"item": "approval_gates", "review_question": "Which actions require human confirmation?", "status": "required"},
        {"item": "state_logging", "review_question": "Can steps and observations be reconstructed?", "status": "required"},
        {"item": "security_controls", "review_question": "How are prompt injection and unsafe tool calls handled?", "status": "required"},
        {"item": "rollback", "review_question": "Can harmful or mistaken actions be reversed?", "status": "required"},
        {"item": "contestability", "review_question": "Can affected people challenge outputs or actions?", "status": "required"},
    ]


def autonomy_profile(audits: list[dict[str, object]]) -> dict[str, object]:
    total = len(audits)
    blocked = sum(1 for row in audits if row["status"] == "blocked")
    escalated = sum(1 for row in audits if row["status"] == "escalate")
    passed = sum(1 for row in audits if row["status"] == "pass")
    mean_risk = mean(float(row["tool_risk"]) for row in audits)
    approval_violations = sum(int(row["approval_violation"]) for row in audits)
    untrusted_instruction_events = sum(int(row["untrusted_instruction"]) for row in audits)
    if blocked:
        recommendation = "supervised_action_only"
    elif escalated:
        recommendation = "bounded_automation_with_escalation"
    else:
        recommendation = "bounded_automation"
    return {
        "total_actions": total,
        "passed_actions": passed,
        "escalated_actions": escalated,
        "blocked_actions": blocked,
        "approval_violations": approval_violations,
        "untrusted_instruction_events": untrusted_instruction_events,
        "mean_tool_risk": round(mean_risk, 6),
        "autonomy_recommendation": recommendation,
        "interpretation": "Autonomy level should be reduced or gated when actions require approval, exceed step limits, originate from untrusted instruction sources, or carry high tool risk.",
    }


def main() -> None:
    config = AgentAuditConfig()
    registry = tool_registry()
    audits = audit_actions(config)
    profile = autonomy_profile(audits)
    security = prompt_injection_checks()
    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "tools_registered": len(registry),
        "actions_reviewed": len(audits),
        "actions_passed": profile["passed_actions"],
        "actions_escalated": profile["escalated_actions"],
        "actions_blocked": profile["blocked_actions"],
        "approval_violations": profile["approval_violations"],
        "untrusted_instruction_events": profile["untrusted_instruction_events"],
        "mean_tool_risk": profile["mean_tool_risk"],
        "recommended_autonomy_level": profile["autonomy_recommendation"],
        "security_checks": len(security),
        "interpretation": "Agentic systems should be audited as procedural workflows with permissions, approvals, observations, escalation, security controls, and accountability records.",
    }

    write_csv(TABLES / "agent_tool_registry.csv", registry)
    write_csv(TABLES / "agent_planned_actions.csv", planned_actions())
    write_csv(TABLES / "agent_tool_use_audit.csv", audits)
    write_csv(TABLES / "agent_autonomy_profile.csv", [profile])
    write_csv(TABLES / "agent_prompt_injection_checks.csv", security)
    write_csv(TABLES / "agent_governance_register.csv", governance_register())
    write_csv(TABLES / "agent_audit_summary.csv", [summary])

    write_json(JSON_DIR / "agent_audit_config.json", asdict(config))
    write_json(JSON_DIR / "agent_tool_use_audit.json", audits)
    write_json(JSON_DIR / "agent_autonomy_profile.json", profile)
    write_json(JSON_DIR / "agent_prompt_injection_checks.json", security)
    write_json(JSON_DIR / "agent_audit_summary.json", summary)

    print("Agent tool-use audit complete.")
    print(TABLES / "agent_audit_summary.csv")


if __name__ == "__main__":
    main()
