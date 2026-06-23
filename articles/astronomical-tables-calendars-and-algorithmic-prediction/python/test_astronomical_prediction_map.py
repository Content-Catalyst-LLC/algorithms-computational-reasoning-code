from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import astronomical_tables_calendars_prediction_map as astro


def test_core_threads_include_tables_calendars_zij() -> None:
    config = astro.AstronomicalPredictionConfig()
    scored = [astro.score_theme(row, config) for row in astro.astronomical_prediction_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_astronomical_prediction_thread"}
    assert "tables_as_stored_computation" in core
    assert "calendars_as_rule_systems" in core
    assert "zij_tabular_astronomy" in core


def test_scores_are_bounded() -> None:
    config = astro.AstronomicalPredictionConfig()
    row = astro.score_theme(astro.astronomical_prediction_themes()[0], config)
    assert 0.0 <= row["prediction_score"] <= 1.0


def test_cautions_include_tables_not_passive_and_prediction_not_certainty() -> None:
    cautions = {row["caution"] for row in astro.interpretation_cautions()}
    assert "do_not_treat_tables_as_passive_lists" in cautions
    assert "do_not_equate_prediction_with_certainty" in cautions


def main() -> None:
    test_core_threads_include_tables_calendars_zij()
    test_scores_are_bounded()
    test_cautions_include_tables_not_passive_and_prediction_not_certainty()
    print("All astronomical prediction map tests passed.")


if __name__ == "__main__":
    main()
