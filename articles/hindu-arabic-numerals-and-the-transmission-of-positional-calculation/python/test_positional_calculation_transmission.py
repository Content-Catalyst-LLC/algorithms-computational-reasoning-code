from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import hindu_arabic_numerals_positional_calculation_map as position


def test_core_threads_include_place_value_zero_and_algorism() -> None:
    config = position.PositionalCalculationConfig()
    scored = [position.score_theme(row, config) for row in position.positional_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_positional_calculation_thread"}
    assert "decimal_place_value" in core
    assert "zero_placeholder" in core
    assert "written_algorism" in core


def test_scores_are_bounded() -> None:
    config = position.PositionalCalculationConfig()
    row = position.score_theme(position.positional_themes()[0], config)
    assert 0.0 <= row["positional_score"] <= 1.0


def test_cautions_include_indian_origins_and_arabic_transmission() -> None:
    cautions = {row["caution"] for row in position.interpretation_cautions()}
    assert "do_not_erase_indian_origins" in cautions
    assert "do_not_erase_arabic_transmission" in cautions


def main() -> None:
    test_core_threads_include_place_value_zero_and_algorism()
    test_scores_are_bounded()
    test_cautions_include_indian_origins_and_arabic_transmission()
    print("All positional calculation transmission tests passed.")


if __name__ == "__main__":
    main()
