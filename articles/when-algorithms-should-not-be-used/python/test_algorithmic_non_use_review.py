from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithmic_non_use_review as review


def test_non_use_review_detects_refusal() -> None:
    config = review.NonUseConfig()
    rows = [review.score_use_case(row, config) for row in review.candidate_use_cases()]
    assert any(row["status"] == "refuse" for row in rows)


def test_scores_are_bounded() -> None:
    config = review.NonUseConfig()
    row = review.score_use_case(review.candidate_use_cases()[0], config)
    assert 0.0 <= row["responsible_use_readiness_score"] <= 1.0
    assert 0.0 <= row["non_use_pressure_score"] <= 1.0


def test_non_use_register_has_inappropriate_target() -> None:
    rows = review.non_use_register()
    assert any(row["criterion"] == "inappropriate_target" for row in rows)


def main() -> None:
    test_non_use_review_detects_refusal()
    test_scores_are_bounded()
    test_non_use_register_has_inappropriate_target()
    print("All algorithmic non-use review tests passed.")


if __name__ == "__main__":
    main()
