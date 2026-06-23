from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import john_von_neumann_architecture_map as arch


def test_core_threads_include_stored_program_memory_bottleneck() -> None:
    config = arch.ArchitectureConfig()
    scored = [arch.score_theme(row, config) for row in arch.architecture_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_von_neumann_architecture_thread"}
    assert "stored_program_concept" in core
    assert "memory_instructions_data" in core
    assert "von_neumann_bottleneck" in core


def test_scores_are_bounded() -> None:
    config = arch.ArchitectureConfig()
    row = arch.score_theme(arch.architecture_themes()[0], config)
    assert 0.0 <= row["architecture_score"] <= 1.0


def test_cautions_include_lone_inventor_and_bottleneck() -> None:
    cautions = {row["caution"] for row in arch.interpretation_cautions()}
    assert "do_not_tell_a_lone_inventor_story" in cautions
    assert "do_not_ignore_the_bottleneck" in cautions


def main() -> None:
    test_core_threads_include_stored_program_memory_bottleneck()
    test_scores_are_bounded()
    test_cautions_include_lone_inventor_and_bottleneck()
    print("All von Neumann architecture tests passed.")


if __name__ == "__main__":
    main()
