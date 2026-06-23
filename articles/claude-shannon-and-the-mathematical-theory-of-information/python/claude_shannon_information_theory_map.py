from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import json
import math
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class ShannonConfig:
    article: str = "claude_shannon_and_the_mathematical_theory_of_information"
    core_threshold: float = 0.80
    high_entropy_threshold: float = 0.86


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


def entropy(probabilities: list[float]) -> float:
    total = sum(probabilities)
    if not math.isclose(total, 1.0, rel_tol=1e-9, abs_tol=1e-9):
        probabilities = [p / total for p in probabilities if p >= 0]
    return -sum(p * math.log2(p) for p in probabilities if p > 0)


def shannon_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "information_as_uncertainty", "entropy_centrality": 0.98, "coding_relevance": 0.88, "channel_capacity": 0.84, "noise_awareness": 0.86, "redundancy_design": 0.90, "computation_relevance": 0.96, "cryptography_relevance": 0.86, "ai_relevance": 0.92, "semantic_boundary": 0.98, "governance_caution": 0.94},
        {"theme_id": "entropy_and_source_modeling", "entropy_centrality": 0.98, "coding_relevance": 0.96, "channel_capacity": 0.82, "noise_awareness": 0.84, "redundancy_design": 0.96, "computation_relevance": 0.96, "cryptography_relevance": 0.82, "ai_relevance": 0.96, "semantic_boundary": 0.92, "governance_caution": 0.90},
        {"theme_id": "source_coding_and_compression", "entropy_centrality": 0.94, "coding_relevance": 0.98, "channel_capacity": 0.80, "noise_awareness": 0.78, "redundancy_design": 0.98, "computation_relevance": 0.98, "cryptography_relevance": 0.78, "ai_relevance": 0.90, "semantic_boundary": 0.88, "governance_caution": 0.88},
        {"theme_id": "noisy_channel_capacity", "entropy_centrality": 0.92, "coding_relevance": 0.98, "channel_capacity": 0.98, "noise_awareness": 0.98, "redundancy_design": 0.96, "computation_relevance": 0.96, "cryptography_relevance": 0.82, "ai_relevance": 0.88, "semantic_boundary": 0.86, "governance_caution": 0.92},
        {"theme_id": "error_correction_reliability", "entropy_centrality": 0.86, "coding_relevance": 0.98, "channel_capacity": 0.94, "noise_awareness": 0.98, "redundancy_design": 0.98, "computation_relevance": 0.96, "cryptography_relevance": 0.80, "ai_relevance": 0.88, "semantic_boundary": 0.82, "governance_caution": 0.92},
        {"theme_id": "cryptography_and_secrecy", "entropy_centrality": 0.88, "coding_relevance": 0.84, "channel_capacity": 0.76, "noise_awareness": 0.82, "redundancy_design": 0.90, "computation_relevance": 0.92, "cryptography_relevance": 0.98, "ai_relevance": 0.84, "semantic_boundary": 0.88, "governance_caution": 0.96},
        {"theme_id": "digital_logic_and_bits", "entropy_centrality": 0.88, "coding_relevance": 0.90, "channel_capacity": 0.76, "noise_awareness": 0.78, "redundancy_design": 0.82, "computation_relevance": 0.98, "cryptography_relevance": 0.82, "ai_relevance": 0.86, "semantic_boundary": 0.86, "governance_caution": 0.86},
        {"theme_id": "ai_data_systems_and_governance", "entropy_centrality": 0.90, "coding_relevance": 0.92, "channel_capacity": 0.84, "noise_awareness": 0.94, "redundancy_design": 0.92, "computation_relevance": 0.98, "cryptography_relevance": 0.88, "ai_relevance": 0.98, "semantic_boundary": 0.98, "governance_caution": 0.98},
    ]


def score_theme(row: dict[str, object], config: ShannonConfig) -> dict[str, object]:
    information_score = mean([
        float(row["entropy_centrality"]),
        float(row["coding_relevance"]),
        float(row["channel_capacity"]),
        float(row["noise_awareness"]),
        float(row["redundancy_design"]),
        float(row["computation_relevance"]),
        float(row["cryptography_relevance"]),
        float(row["ai_relevance"]),
        float(row["semantic_boundary"]),
        float(row["governance_caution"]),
    ])

    if information_score >= config.core_threshold and float(row["entropy_centrality"]) >= config.high_entropy_threshold:
        interpretive_status = "core_shannon_information_thread"
    elif information_score >= config.core_threshold:
        interpretive_status = "major_shannon_information_thread"
    else:
        interpretive_status = "supporting_shannon_information_thread"

    scored = {key: round(float(row[key]), 6) for key in [
        "entropy_centrality", "coding_relevance", "channel_capacity", "noise_awareness",
        "redundancy_design", "computation_relevance", "cryptography_relevance",
        "ai_relevance", "semantic_boundary", "governance_caution"
    ]}
    scored.update({
        "theme_id": row["theme_id"],
        "information_score": round(information_score, 6),
        "interpretive_status": interpretive_status,
    })
    return scored


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_confuse_information_with_meaning", "meaning": "Shannon information measures uncertainty, not semantic truth or importance."},
        {"caution": "do_not_treat_entropy_as_wisdom", "meaning": "High entropy can describe randomness as well as useful surprise."},
        {"caution": "do_not_ignore_channel_assumptions", "meaning": "Capacity depends on the channel model and noise assumptions."},
        {"caution": "do_not_treat_redundancy_as_only_waste", "meaning": "Redundancy can support reliability and error correction."},
        {"caution": "do_not_apply_information_theory_as_total_governance", "meaning": "Information-theoretic measures must be paired with ethics, context, and accountability."},
    ]


def main() -> None:
    config = ShannonConfig()
    themes = shannon_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    entropy_examples = [
        {"source": "fair_binary", "probabilities": "0.5,0.5", "entropy_bits": round(entropy([0.5, 0.5]), 6)},
        {"source": "biased_binary", "probabilities": "0.9,0.1", "entropy_bits": round(entropy([0.9, 0.1]), 6)},
        {"source": "four_equal_symbols", "probabilities": "0.25,0.25,0.25,0.25", "entropy_bits": round(entropy([0.25, 0.25, 0.25, 0.25]), 6)},
        {"source": "certain_symbol", "probabilities": "1.0,0.0", "entropy_bits": round(entropy([1.0, 0.0]), 6)},
    ]

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_shannon_information_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_shannon_information_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_shannon_information_thread"),
        "mean_information_score": round(mean(float(row["information_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Shannon should be studied as the architect of mathematical information theory: entropy, coding, capacity, noise, redundancy, reliability, and semantic boundaries.",
    }

    write_csv(TABLES / "shannon_themes.csv", themes)
    write_csv(TABLES / "shannon_information_map.csv", scored)
    write_csv(TABLES / "entropy_examples.csv", entropy_examples)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "shannon_information_summary.csv", [summary])

    write_json(JSON_DIR / "shannon_config.json", asdict(config))
    write_json(JSON_DIR / "shannon_information_map.json", scored)
    write_json(JSON_DIR / "entropy_examples.json", entropy_examples)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "shannon_information_summary.json", summary)

    print("Shannon information theory map complete.")
    print(TABLES / "shannon_information_summary.csv")


if __name__ == "__main__":
    main()
