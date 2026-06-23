from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import translation_movements_computational_knowledge_transfer_map as transfer


def test_core_threads_include_procedural_vocabulary_diagrams() -> None:
    config = transfer.TranslationTransferConfig()
    scored = [transfer.score_theme(row, config) for row in transfer.transfer_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_computational_knowledge_transfer_thread"}
    assert "procedural_fidelity" in core
    assert "technical_vocabulary_mapping" in core
    assert "diagrams_tables_nonverbal_knowledge" in core


def test_scores_are_bounded() -> None:
    config = transfer.TranslationTransferConfig()
    row = transfer.score_theme(transfer.transfer_themes()[0], config)
    assert 0.0 <= row["transfer_score"] <= 1.0


def test_cautions_include_not_preservation_only_and_not_single_institution() -> None:
    cautions = {row["caution"] for row in transfer.interpretation_cautions()}
    assert "do_not_reduce_translation_to_preservation" in cautions
    assert "do_not_center_everything_on_one_institution" in cautions


def main() -> None:
    test_core_threads_include_procedural_vocabulary_diagrams()
    test_scores_are_bounded()
    test_cautions_include_not_preservation_only_and_not_single_institution()
    print("All translation transfer tests passed.")


if __name__ == "__main__":
    main()
