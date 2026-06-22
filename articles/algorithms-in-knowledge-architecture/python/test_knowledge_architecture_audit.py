from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithms_in_knowledge_architecture_audit as audit


def test_knowledge_architecture_detects_review_or_rebuild_case() -> None:
    config = audit.KnowledgeArchitectureConfig()
    rows = [audit.score_object(row, config) for row in audit.knowledge_objects()]
    recommendations = {row["recommendation"] for row in rows}

    assert any(row["recommendation"] != "knowledge_architecture_ready" for row in rows)
    assert {
        "editorial_governance_review_required",
        "metadata_and_linking_review_required",
        "maintenance_backlog_review_required",
        "rebuild_before_algorithmic_discovery",
    } & recommendations


def test_scores_are_bounded() -> None:
    config = audit.KnowledgeArchitectureConfig()
    row = audit.score_object(audit.knowledge_objects()[0], config)
    assert 0.0 <= row["architecture_readiness_score"] <= 1.0
    assert 0.0 <= row["maintenance_risk_score"] <= 1.0
    assert 0.0 <= row["governance_readiness_score"] <= 1.0


def test_register_has_metadata_schema() -> None:
    rows = audit.knowledge_architecture_register()
    assert any(row["control"] == "metadata_schema" for row in rows)


def main() -> None:
    test_knowledge_architecture_detects_review_or_rebuild_case()
    test_scores_are_bounded()
    test_register_has_metadata_schema()
    print("All algorithms in knowledge architecture tests passed.")


if __name__ == "__main__":
    main()
