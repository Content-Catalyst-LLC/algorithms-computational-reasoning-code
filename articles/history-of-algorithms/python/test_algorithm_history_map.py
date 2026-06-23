from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import history_of_algorithms_timeline_map as history


def test_core_layers_include_islamic_logic_electronic_ai() -> None:
    config = history.AlgorithmHistoryConfig()
    scored = [history.score_layer(row, config) for row in history.history_layers()]
    core = {row["layer_id"] for row in scored if row["interpretive_status"] == "core_algorithm_history_layer"}
    assert "islamic_world_algorism_and_algebra" in core
    assert "logic_computability_and_turing_machines" in core
    assert "electronic_computing_and_software" in core


def test_scores_are_bounded() -> None:
    config = history.AlgorithmHistoryConfig()
    row = history.score_layer(history.history_layers()[0], config)
    assert 0.0 <= row["history_score"] <= 1.0


def test_cautions_include_computer_only_and_word_origin() -> None:
    cautions = {row["caution"] for row in history.interpretation_cautions()}
    assert "do_not_treat_algorithm_history_as_computer_history_only" in cautions
    assert "do_not_confuse_word_origin_with_total_origin" in cautions


def main() -> None:
    test_core_layers_include_islamic_logic_electronic_ai()
    test_scores_are_bounded()
    test_cautions_include_computer_only_and_word_origin()
    print("All algorithm history tests passed.")


if __name__ == "__main__":
    main()
