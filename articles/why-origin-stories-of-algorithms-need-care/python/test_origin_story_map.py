from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import why_origin_stories_of_algorithms_need_care_map as origins


def test_core_threads_include_word_history_al_khwarizmi_procedures() -> None:
    config = origins.OriginStoryConfig()
    scored = [origins.score_theme(row, config) for row in origins.origin_story_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_origin_story_care_thread"}
    assert "word_history_not_concept_history" in core
    assert "al_khwarizmi_without_myth" in core
    assert "procedures_before_algorithm_word" in core


def test_scores_are_bounded() -> None:
    config = origins.OriginStoryConfig()
    row = origins.score_theme(origins.origin_story_themes()[0], config)
    assert 0.0 <= row["origin_care_score"] <= 1.0


def test_cautions_include_word_origin_and_modern_projection() -> None:
    cautions = {row["caution"] for row in origins.interpretation_cautions()}
    assert "do_not_confuse_word_origin_with_invention" in cautions
    assert "do_not_project_modern_computing_backward" in cautions


def main() -> None:
    test_core_threads_include_word_history_al_khwarizmi_procedures()
    test_scores_are_bounded()
    test_cautions_include_word_origin_and_modern_projection()
    print("All algorithm origin-story care tests passed.")


if __name__ == "__main__":
    main()
