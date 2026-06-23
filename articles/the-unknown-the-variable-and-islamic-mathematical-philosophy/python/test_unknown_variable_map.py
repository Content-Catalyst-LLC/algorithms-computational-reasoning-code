from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import unknown_variable_islamic_mathematical_philosophy_map as unknown


def test_core_threads_include_unknown_shay_variable() -> None:
    config = unknown.UnknownVariableConfig()
    scored = [unknown.score_theme(row, config) for row in unknown.unknown_variable_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_unknown_variable_philosophy_thread"}
    assert "unknown_as_named_object" in core
    assert "shay_root_square_number" in core
    assert "from_unknown_to_variable" in core


def test_scores_are_bounded() -> None:
    config = unknown.UnknownVariableConfig()
    row = unknown.score_theme(unknown.unknown_variable_themes()[0], config)
    assert 0.0 <= row["unknown_variable_score"] <= 1.0


def test_cautions_include_no_modern_symbolism_projection() -> None:
    cautions = {row["caution"] for row in unknown.interpretation_cautions()}
    assert "do_not_project_modern_symbolism_backward" in cautions
    assert "do_not_equate_unknown_and_variable_too_quickly" in cautions


def main() -> None:
    test_core_threads_include_unknown_shay_variable()
    test_scores_are_bounded()
    test_cautions_include_no_modern_symbolism_projection()
    print("All unknown-variable philosophy tests passed.")


if __name__ == "__main__":
    main()
