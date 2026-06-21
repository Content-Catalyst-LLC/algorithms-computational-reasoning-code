from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class SymbolicAuditConfig:
    article: str = "automated_reasoning_symbolic_ai_and_hybrid_systems"
    require_trace: bool = True
    require_rule_provenance: bool = True
    contradiction_review_required: bool = True


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


def facts() -> set[str]:
    return {
        "has_documentation",
        "has_human_review",
        "logs_decisions",
        "uses_statistical_model",
        "uses_symbolic_rules",
        "high_stakes_context",
    }


def rules() -> list[dict[str, object]]:
    return [
        {
            "rule_id": "R1",
            "premises": ["has_documentation", "logs_decisions"],
            "conclusion": "traceable_system",
            "provenance": "governance_policy_v1",
        },
        {
            "rule_id": "R2",
            "premises": ["has_human_review", "traceable_system"],
            "conclusion": "reviewable_system",
            "provenance": "governance_policy_v1",
        },
        {
            "rule_id": "R3",
            "premises": ["uses_statistical_model", "uses_symbolic_rules"],
            "conclusion": "hybrid_system",
            "provenance": "architecture_record_v2",
        },
        {
            "rule_id": "R4",
            "premises": ["high_stakes_context", "hybrid_system"],
            "conclusion": "requires_escalation_review",
            "provenance": "risk_policy_v3",
        },
        {
            "rule_id": "R5",
            "premises": ["requires_escalation_review", "reviewable_system"],
            "conclusion": "conditionally_approvable",
            "provenance": "risk_policy_v3",
        },
    ]


def infer(initial_facts: set[str], rule_rows: list[dict[str, object]]) -> tuple[set[str], list[dict[str, object]]]:
    known = set(initial_facts)
    trace: list[dict[str, object]] = []
    changed = True

    while changed:
        changed = False
        for rule in rule_rows:
            premises = set(rule["premises"])
            conclusion = str(rule["conclusion"])
            if premises.issubset(known) and conclusion not in known:
                known.add(conclusion)
                trace.append({
                    "rule_id": rule["rule_id"],
                    "premises": ";".join(sorted(premises)),
                    "conclusion": conclusion,
                    "provenance": rule["provenance"],
                    "trace_note": "Conclusion inferred because all premises were present.",
                })
                changed = True

    return known, trace


def contradiction_checks(known: set[str]) -> list[dict[str, object]]:
    pairs = [
        ("conditionally_approvable", "prohibited_use"),
        ("reviewable_system", "unreviewable_system"),
        ("traceable_system", "no_audit_trail"),
        ("requires_escalation_review", "fully_automated_without_review"),
    ]
    rows = []
    for left, right in pairs:
        conflict = left in known and right in known
        rows.append({
            "left_claim": left,
            "right_claim": right,
            "conflict_detected": int(conflict),
            "interpretation": "Conflicting conclusions require governance review before deployment." if conflict else "No conflict detected for this pair.",
        })
    return rows


def constraint_review(known: set[str]) -> list[dict[str, object]]:
    required = [
        "traceable_system",
        "reviewable_system",
        "hybrid_system",
        "requires_escalation_review",
        "conditionally_approvable",
    ]
    return [{
        "constraint": item,
        "satisfied": int(item in known),
        "interpretation": "Required symbolic governance condition is satisfied." if item in known else "Required symbolic governance condition is missing.",
    } for item in required]


def hybrid_interface_register() -> list[dict[str, object]]:
    return [
        {
            "interface_item": "statistical_score_to_symbolic_fact",
            "example": "risk_score >= threshold becomes high_stakes_context",
            "review_question": "Is the threshold justified and documented?",
            "risk": "A learned score may be treated as a fact without uncertainty review.",
        },
        {
            "interface_item": "retrieved_text_to_rule",
            "example": "policy excerpt becomes rule premise",
            "review_question": "Is the source authoritative and current?",
            "risk": "Bad retrieval can create invalid symbolic rules.",
        },
        {
            "interface_item": "llm_output_to_constraint",
            "example": "generated plan step becomes required action",
            "review_question": "Was the generated constraint verified?",
            "risk": "Generated procedural content can look formal before validation.",
        },
    ]


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "rule_provenance", "review_question": "Who authorized each rule?", "status": "required"},
        {"item": "knowledge_validity", "review_question": "Are facts and categories current?", "status": "required"},
        {"item": "inference_trace", "review_question": "Can conclusions be traced to premises?", "status": "required"},
        {"item": "contradiction_review", "review_question": "How are conflicting rules resolved?", "status": "required"},
        {"item": "hybrid_interface", "review_question": "How do statistical outputs become symbolic inputs?", "status": "required"},
        {"item": "appeal_process", "review_question": "Can affected people challenge facts, rules, and conclusions?", "status": "required"},
    ]


def main() -> None:
    config = SymbolicAuditConfig()
    initial = facts()
    rule_rows = rules()
    known, trace = infer(initial, rule_rows)
    contradictions = contradiction_checks(known)
    constraints = constraint_review(known)
    hybrid_interfaces = hybrid_interface_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "initial_fact_count": len(initial),
        "rule_count": len(rule_rows),
        "derived_fact_count": len(known - initial),
        "trace_steps": len(trace),
        "constraints_satisfied": sum(int(row["satisfied"]) for row in constraints),
        "constraints_required": len(constraints),
        "conflicts_detected": sum(int(row["conflict_detected"]) for row in contradictions),
        "hybrid_interface_items": len(hybrid_interfaces),
        "interpretation": "Automated reasoning systems should expose rules, premises, derived conclusions, contradictions, constraints, hybrid interfaces, and governance responsibilities.",
    }

    write_csv(TABLES / "symbolic_initial_facts.csv", [{"fact": item} for item in sorted(initial)])
    write_csv(TABLES / "symbolic_rules.csv", [{
        "rule_id": row["rule_id"],
        "premises": ";".join(row["premises"]),
        "conclusion": row["conclusion"],
        "provenance": row["provenance"],
    } for row in rule_rows])
    write_csv(TABLES / "symbolic_inference_trace.csv", trace)
    write_csv(TABLES / "symbolic_known_facts.csv", [{"fact": item} for item in sorted(known)])
    write_csv(TABLES / "symbolic_contradiction_checks.csv", contradictions)
    write_csv(TABLES / "symbolic_constraint_review.csv", constraints)
    write_csv(TABLES / "symbolic_hybrid_interface_register.csv", hybrid_interfaces)
    write_csv(TABLES / "symbolic_governance_register.csv", governance_register())
    write_csv(TABLES / "symbolic_audit_summary.csv", [summary])

    write_json(JSON_DIR / "symbolic_audit_config.json", asdict(config))
    write_json(JSON_DIR / "symbolic_inference_trace.json", trace)
    write_json(JSON_DIR / "symbolic_known_facts.json", sorted(known))
    write_json(JSON_DIR / "symbolic_hybrid_interface_register.json", hybrid_interfaces)
    write_json(JSON_DIR / "symbolic_audit_summary.json", summary)

    print("Symbolic reasoning audit complete.")
    print(TABLES / "symbolic_audit_summary.csv")


if __name__ == "__main__":
    main()
