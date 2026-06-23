from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from collections import Counter
import csv
import json
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class CryptanalysisConfig:
    article: str = "al_kindi_frequency_analysis_and_the_birth_of_cryptanalysis"
    core_threshold: float = 0.80
    high_inference_threshold: float = 0.86


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def frequency_table(text: str) -> list[dict[str, object]]:
    symbols = [ch.lower() for ch in text if ch.isalpha()]
    total = len(symbols)
    counts = Counter(symbols)
    rows = []
    for symbol, count in counts.most_common():
        rows.append({
            "symbol": symbol,
            "count": count,
            "relative_frequency": round(count / total, 6) if total else 0.0,
            "rank": len(rows) + 1,
        })
    return rows


def cryptanalysis_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "letter_counting_as_feature_extraction", "linguistic_evidence": 0.96, "counting_procedure": 0.98, "inferential_structure": 0.90, "cryptanalytic_relevance": 0.94, "historical_significance": 0.94, "ethical_caution": 0.82, "modern_resonance": 0.94},
        {"theme_id": "frequency_ranking_and_comparison", "linguistic_evidence": 0.98, "counting_procedure": 0.96, "inferential_structure": 0.94, "cryptanalytic_relevance": 0.96, "historical_significance": 0.94, "ethical_caution": 0.82, "modern_resonance": 0.96},
        {"theme_id": "substitution_mapping_hypothesis", "linguistic_evidence": 0.90, "counting_procedure": 0.86, "inferential_structure": 0.96, "cryptanalytic_relevance": 0.98, "historical_significance": 0.92, "ethical_caution": 0.84, "modern_resonance": 0.94},
        {"theme_id": "testing_and_revision", "linguistic_evidence": 0.88, "counting_procedure": 0.84, "inferential_structure": 0.98, "cryptanalytic_relevance": 0.94, "historical_significance": 0.90, "ethical_caution": 0.86, "modern_resonance": 0.96},
        {"theme_id": "arabic_textual_culture", "linguistic_evidence": 0.94, "counting_procedure": 0.86, "inferential_structure": 0.88, "cryptanalytic_relevance": 0.88, "historical_significance": 0.96, "ethical_caution": 0.82, "modern_resonance": 0.88},
        {"theme_id": "limits_and_countermeasures", "linguistic_evidence": 0.86, "counting_procedure": 0.88, "inferential_structure": 0.92, "cryptanalytic_relevance": 0.94, "historical_significance": 0.88, "ethical_caution": 0.94, "modern_resonance": 0.96},
        {"theme_id": "early_statistical_inference", "linguistic_evidence": 0.94, "counting_procedure": 0.96, "inferential_structure": 0.96, "cryptanalytic_relevance": 0.92, "historical_significance": 0.96, "ethical_caution": 0.84, "modern_resonance": 0.98},
    ]


def score_theme(row: dict[str, object], config: CryptanalysisConfig) -> dict[str, object]:
    cryptanalysis_score = mean([
        float(row["linguistic_evidence"]),
        float(row["counting_procedure"]),
        float(row["inferential_structure"]),
        float(row["cryptanalytic_relevance"]),
        float(row["historical_significance"]),
        float(row["ethical_caution"]),
        float(row["modern_resonance"]),
    ])

    if cryptanalysis_score >= config.core_threshold and float(row["inferential_structure"]) >= config.high_inference_threshold:
        interpretive_status = "core_cryptanalysis_thread"
    elif cryptanalysis_score >= config.core_threshold:
        interpretive_status = "major_cryptanalysis_thread"
    else:
        interpretive_status = "supporting_cryptanalysis_thread"

    return {
        "theme_id": row["theme_id"],
        "linguistic_evidence": round(float(row["linguistic_evidence"]), 6),
        "counting_procedure": round(float(row["counting_procedure"]), 6),
        "inferential_structure": round(float(row["inferential_structure"]), 6),
        "cryptanalytic_relevance": round(float(row["cryptanalytic_relevance"]), 6),
        "historical_significance": round(float(row["historical_significance"]), 6),
        "ethical_caution": round(float(row["ethical_caution"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "cryptanalysis_score": round(cryptanalysis_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_claim_al_kindi_invented_all_cryptography", "meaning": "Al-Kindī is central to surviving systematic frequency-analysis cryptanalysis, not all secrecy or ciphering."},
        {"caution": "do_not_treat_frequency_analysis_as_magic", "meaning": "The method depends on counting, comparison, hypothesis testing, and revision."},
        {"caution": "do_not_project_modern_statistics_backward", "meaning": "The method anticipates statistical inference without being modern formal statistics."},
        {"caution": "do_not_ignore_language_context", "meaning": "Cryptanalysis depends on linguistic regularity, genre, spelling, and textual knowledge."},
        {"caution": "do_not_turn_attack_methods_into_unbounded_security_advice", "meaning": "Use examples for historical and educational analysis, not unauthorized access."},
    ]


def main() -> None:
    config = CryptanalysisConfig()
    sample_ciphertext = "XLMW MW E WLSVX IHYGERXMSREP WEQTPI JSV JVIUYIRGC EREP]WMW"
    freq_rows = frequency_table(sample_ciphertext)
    themes = cryptanalysis_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "sample_symbols_reviewed": sum(int(row["count"]) for row in freq_rows),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_cryptanalysis_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_cryptanalysis_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_cryptanalysis_thread"),
        "mean_cryptanalysis_score": round(mean(float(row["cryptanalysis_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Al-Kindī’s frequency-analysis method should be studied as early algorithmic inference over language: count, rank, compare, hypothesize, test, revise, and interpret.",
    }

    write_csv(TABLES / "sample_frequency_table.csv", freq_rows)
    write_csv(TABLES / "cryptanalysis_themes.csv", themes)
    write_csv(TABLES / "cryptanalysis_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "cryptanalysis_summary.csv", [summary])

    write_json(JSON_DIR / "cryptanalysis_config.json", asdict(config))
    write_json(JSON_DIR / "sample_frequency_table.json", freq_rows)
    write_json(JSON_DIR / "cryptanalysis_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "cryptanalysis_summary.json", summary)

    print("Al-Kindī, frequency analysis, and cryptanalysis map complete.")
    print(TABLES / "cryptanalysis_summary.csv")


if __name__ == "__main__":
    main()
