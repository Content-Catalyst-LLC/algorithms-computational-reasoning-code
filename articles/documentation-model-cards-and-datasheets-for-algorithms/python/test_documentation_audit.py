from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import documentation_model_cards_datasheets_audit as audit


def test_documentation_audit_detects_review_or_escalation() -> None:
    config = audit.DocumentationConfig()
    rows = [audit.score_record(row, config) for row in audit.documentation_records()]
    assert any(row["status"] in {"review", "escalate"} for row in rows)


def test_scores_are_bounded() -> None:
    config = audit.DocumentationConfig()
    row = audit.score_record(audit.documentation_records()[0], config)
    assert 0.0 <= row["documentation_completeness_score"] <= 1.0
    assert 0.0 <= row["artifact_coverage_score"] <= 1.0
    assert 0.0 <= row["documentation_quality_score"] <= 1.0
    assert row["documentation_risk_score"] >= 0.0


def test_documentation_register_has_model_card_and_datasheet() -> None:
    rows = audit.documentation_register()
    artifacts = {row["artifact"] for row in rows}
    assert "model_card" in artifacts
    assert "datasheet" in artifacts


def main() -> None:
    test_documentation_audit_detects_review_or_escalation()
    test_scores_are_bounded()
    test_documentation_register_has_model_card_and_datasheet()
    print("All documentation, model-card, and datasheet tests passed.")


if __name__ == "__main__":
    main()
