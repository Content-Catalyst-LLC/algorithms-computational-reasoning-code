from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import islamic_world_roots_of_algorithmic_reasoning_map as roots


def test_core_threads_include_algorism_algebra_and_positional_calculation() -> None:
    config = roots.HistoricalReasoningConfig()
    scored = [roots.score_theme(row, config) for row in roots.historical_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_algorithmic_reasoning_thread"}
    assert "al_khwarizmi_algorism" in core
    assert "algebraic_transformation" in core
    assert "hindu_arabic_positional_calculation" in core


def test_scores_are_bounded() -> None:
    config = roots.HistoricalReasoningConfig()
    row = roots.score_theme(roots.historical_themes()[0], config)
    assert 0.0 <= row["significance_score"] <= 1.0


def test_cautions_include_single_origin_and_modern_projection() -> None:
    cautions = {row["caution"] for row in roots.historical_cautions()}
    assert "avoid_single_origin_story" in cautions
    assert "avoid_modern_projection" in cautions


def main() -> None:
    test_core_threads_include_algorism_algebra_and_positional_calculation()
    test_scores_are_bounded()
    test_cautions_include_single_origin_and_modern_projection()
    print("All Islamic-world roots map tests passed.")


if __name__ == "__main__":
    main()
