from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import al_kindi_frequency_analysis_cryptanalysis_map as crypto


def test_core_threads_include_frequency_mapping_inference() -> None:
    config = crypto.CryptanalysisConfig()
    scored = [crypto.score_theme(row, config) for row in crypto.cryptanalysis_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_cryptanalysis_thread"}
    assert "letter_counting_as_feature_extraction" in core
    assert "frequency_ranking_and_comparison" in core
    assert "substitution_mapping_hypothesis" in core


def test_frequency_table_counts_symbols() -> None:
    rows = crypto.frequency_table("AAB CCC")
    counts = {row["symbol"]: row["count"] for row in rows}
    assert counts["a"] == 2
    assert counts["b"] == 1
    assert counts["c"] == 3


def test_cautions_include_not_all_cryptography_and_not_magic() -> None:
    cautions = {row["caution"] for row in crypto.interpretation_cautions()}
    assert "do_not_claim_al_kindi_invented_all_cryptography" in cautions
    assert "do_not_treat_frequency_analysis_as_magic" in cautions


def main() -> None:
    test_core_threads_include_frequency_mapping_inference()
    test_frequency_table_counts_symbols()
    test_cautions_include_not_all_cryptography_and_not_magic()
    print("All cryptanalysis map tests passed.")


if __name__ == "__main__":
    main()
