from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import evaluation_benchmarks_ai_measurement_audit as audit


def test_model_summaries_include_calibration_and_safety() -> None:
    config = audit.EvaluationAuditConfig()
    rows = audit.benchmark_rows()
    summaries = audit.summarize_model_performance(rows, config)
    assert len(summaries) == 3
    assert all("calibration_gap" in row for row in summaries)
    assert all("safety_flag_rate" in row for row in summaries)


def test_disaggregated_performance_is_not_empty() -> None:
    rows = audit.benchmark_rows()
    disagg = audit.disaggregated_performance(rows)
    assert disagg
    assert any(row["group"] == "underrepresented_language" for row in disagg)


def test_saturated_model_is_detected() -> None:
    config = audit.EvaluationAuditConfig()
    summaries = audit.summarize_model_performance(audit.benchmark_rows(), config)
    assert any(int(row["saturated"]) == 1 for row in summaries)


def main() -> None:
    test_model_summaries_include_calibration_and_safety()
    test_disaggregated_performance_is_not_empty()
    test_saturated_model_is_detected()
    print("All evaluation benchmark tests passed.")


if __name__ == "__main__":
    main()
