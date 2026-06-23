from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import claude_shannon_information_theory_map as shannon


def test_entropy_examples() -> None:
    assert abs(shannon.entropy([0.5, 0.5]) - 1.0) < 1e-9
    assert abs(shannon.entropy([1.0, 0.0]) - 0.0) < 1e-9
    assert abs(shannon.entropy([0.25, 0.25, 0.25, 0.25]) - 2.0) < 1e-9


def test_core_threads_include_entropy_channel_ai() -> None:
    config = shannon.ShannonConfig()
    scored = [shannon.score_theme(row, config) for row in shannon.shannon_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_shannon_information_thread"}
    assert "information_as_uncertainty" in core
    assert "entropy_and_source_modeling" in core
    assert "noisy_channel_capacity" in core
    assert "ai_data_systems_and_governance" in core


def test_cautions_include_semantic_boundary() -> None:
    cautions = {row["caution"] for row in shannon.interpretation_cautions()}
    assert "do_not_confuse_information_with_meaning" in cautions
    assert "do_not_treat_entropy_as_wisdom" in cautions


def main() -> None:
    test_entropy_examples()
    test_core_threads_include_entropy_channel_ai()
    test_cautions_include_semantic_boundary()
    print("All Shannon information-theory tests passed.")


if __name__ == "__main__":
    main()
