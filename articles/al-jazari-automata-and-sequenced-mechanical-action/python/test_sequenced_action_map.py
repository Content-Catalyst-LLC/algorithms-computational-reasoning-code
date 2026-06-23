from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import al_jazari_automata_sequenced_action_map as action


def test_core_threads_include_clocks_elephant_cams() -> None:
    config = action.SequencedActionConfig()
    scored = [action.score_theme(row, config) for row in action.sequenced_action_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_sequenced_mechanical_action_thread"}
    assert "clocks_as_timed_state_change" in core
    assert "elephant_clock_layered_sequence" in core
    assert "cams_levers_control" in core


def test_scores_are_bounded() -> None:
    config = action.SequencedActionConfig()
    row = action.score_theme(action.sequenced_action_themes()[0], config)
    assert 0.0 <= row["sequenced_action_score"] <= 1.0


def test_cautions_include_not_robots_and_not_source_code() -> None:
    cautions = {row["caution"] for row in action.interpretation_cautions()}
    assert "do_not_call_al_jazari_devices_modern_robots" in cautions
    assert "do_not_call_the_book_source_code" in cautions


def main() -> None:
    test_core_threads_include_clocks_elephant_cams()
    test_scores_are_bounded()
    test_cautions_include_not_robots_and_not_source_code()
    print("All sequenced mechanical action tests passed.")


if __name__ == "__main__":
    main()
