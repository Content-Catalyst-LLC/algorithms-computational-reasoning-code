from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import trade_inheritance_surveying_practical_calculation_map as practical


def test_core_threads_include_trade_inheritance_surveying() -> None:
    config = practical.PracticalCalculationConfig()
    scored = [practical.score_theme(row, config) for row in practical.practical_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_practical_calculation_thread"}
    assert "trade_commercial_reckoning" in core
    assert "inheritance_allocation" in core
    assert "surveying_land_measurement" in core


def test_scores_are_bounded() -> None:
    config = practical.PracticalCalculationConfig()
    row = practical.score_theme(practical.practical_themes()[0], config)
    assert 0.0 <= row["practical_score"] <= 1.0


def test_cautions_include_not_lesser_and_not_neutral() -> None:
    cautions = {row["caution"] for row in practical.interpretation_cautions()}
    assert "do_not_treat_practical_math_as_lesser" in cautions
    assert "do_not_assume_calculation_is_neutral" in cautions


def main() -> None:
    test_core_threads_include_trade_inheritance_surveying()
    test_scores_are_bounded()
    test_cautions_include_not_lesser_and_not_neutral()
    print("All practical calculation map tests passed.")


if __name__ == "__main__":
    main()
