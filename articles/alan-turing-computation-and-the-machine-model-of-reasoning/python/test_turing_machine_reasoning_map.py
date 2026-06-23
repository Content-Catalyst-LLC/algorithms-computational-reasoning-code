from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import alan_turing_machine_reasoning_map as turing


def test_core_threads_include_machine_universal_undecidability() -> None:
    config = turing.TuringConfig()
    scored = [turing.score_theme(row, config) for row in turing.turing_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_turing_machine_reasoning_thread"}
    assert "turing_machine_model" in core
    assert "universal_machine" in core
    assert "undecidability_and_limits" in core
    assert "halting_problem" in core


def test_scores_are_bounded() -> None:
    config = turing.TuringConfig()
    row = turing.score_theme(turing.turing_themes()[0], config)
    assert 0.0 <= row["reasoning_score"] <= 1.0


def test_cautions_include_not_laptop_and_not_all_reasoning() -> None:
    cautions = {row["caution"] for row in turing.interpretation_cautions()}
    assert "do_not_treat_turing_machine_as_physical_laptop" in cautions
    assert "do_not_claim_all_reasoning_is_computation" in cautions


def main() -> None:
    test_core_threads_include_machine_universal_undecidability()
    test_scores_are_bounded()
    test_cautions_include_not_laptop_and_not_all_reasoning()
    print("All Turing machine reasoning tests passed.")


if __name__ == "__main__":
    main()
