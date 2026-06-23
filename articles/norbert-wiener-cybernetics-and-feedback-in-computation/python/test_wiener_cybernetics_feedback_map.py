from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import norbert_wiener_cybernetics_feedback_map as wiener


def test_core_threads_include_feedback_platform_ai() -> None:
    config = wiener.WienerConfig()
    scored = [wiener.score_theme(row, config) for row in wiener.wiener_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_wiener_cybernetic_feedback_thread"}
    assert "feedback_as_computational_structure" in core
    assert "software_and_platform_feedback" in core
    assert "ai_governance_feedback_loops" in core


def test_scores_are_bounded() -> None:
    config = wiener.WienerConfig()
    row = wiener.score_theme(wiener.wiener_themes()[0], config)
    assert 0.0 <= row["cybernetic_score"] <= 1.0


def test_cautions_include_feedback_and_loops() -> None:
    cautions = {row["caution"] for row in wiener.interpretation_cautions()}
    assert "do_not_treat_feedback_as_inherently_good" in cautions
    assert "do_not_govern_models_without_governing_loops" in cautions


def main() -> None:
    test_core_threads_include_feedback_platform_ai()
    test_scores_are_bounded()
    test_cautions_include_feedback_and_loops()
    print("All Wiener cybernetic feedback tests passed.")


if __name__ == "__main__":
    main()
