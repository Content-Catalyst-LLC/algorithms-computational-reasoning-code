from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import json
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class NeuralLogicConfig:
    article: str = "warren_mcculloch_walter_pitts_and_neural_logic"
    core_threshold: float = 0.78
    high_influence_threshold: float = 0.86


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


def threshold_unit(inputs: list[int], weights: list[int], threshold: int) -> int:
    if len(inputs) != len(weights):
        raise ValueError("inputs and weights must have the same length")
    total = sum(x * w for x, w in zip(inputs, weights))
    return 1 if total >= threshold else 0


def concept_rows() -> list[dict[str, object]]:
    return [
        {"concept_id": "threshold_unit", "logical_clarity": 0.96, "neural_abstraction": 0.94, "computational_relevance": 0.96, "cybernetic_connection": 0.86, "ai_lineage": 0.96, "biological_caution": 0.94, "historical_influence": 0.98, "interpretability": 0.94, "formal_tractability": 0.98, "responsible_use_relevance": 0.90},
        {"concept_id": "logical_network", "logical_clarity": 0.94, "neural_abstraction": 0.92, "computational_relevance": 0.98, "cybernetic_connection": 0.88, "ai_lineage": 0.98, "biological_caution": 0.92, "historical_influence": 0.98, "interpretability": 0.90, "formal_tractability": 0.94, "responsible_use_relevance": 0.88},
        {"concept_id": "activation_pattern", "logical_clarity": 0.86, "neural_abstraction": 0.90, "computational_relevance": 0.92, "cybernetic_connection": 0.90, "ai_lineage": 0.94, "biological_caution": 0.90, "historical_influence": 0.92, "interpretability": 0.82, "formal_tractability": 0.86, "responsible_use_relevance": 0.86},
        {"concept_id": "inhibition", "logical_clarity": 0.90, "neural_abstraction": 0.90, "computational_relevance": 0.88, "cybernetic_connection": 0.88, "ai_lineage": 0.86, "biological_caution": 0.92, "historical_influence": 0.90, "interpretability": 0.86, "formal_tractability": 0.88, "responsible_use_relevance": 0.86},
        {"concept_id": "temporal_sequence", "logical_clarity": 0.84, "neural_abstraction": 0.86, "computational_relevance": 0.90, "cybernetic_connection": 0.90, "ai_lineage": 0.88, "biological_caution": 0.88, "historical_influence": 0.88, "interpretability": 0.80, "formal_tractability": 0.84, "responsible_use_relevance": 0.84},
        {"concept_id": "automata_connection", "logical_clarity": 0.92, "neural_abstraction": 0.84, "computational_relevance": 0.96, "cybernetic_connection": 0.88, "ai_lineage": 0.92, "biological_caution": 0.86, "historical_influence": 0.92, "interpretability": 0.88, "formal_tractability": 0.94, "responsible_use_relevance": 0.86},
        {"concept_id": "cybernetic_bridge", "logical_clarity": 0.84, "neural_abstraction": 0.88, "computational_relevance": 0.88, "cybernetic_connection": 0.98, "ai_lineage": 0.90, "biological_caution": 0.88, "historical_influence": 0.94, "interpretability": 0.82, "formal_tractability": 0.82, "responsible_use_relevance": 0.90},
        {"concept_id": "modern_ai_boundary", "logical_clarity": 0.78, "neural_abstraction": 0.82, "computational_relevance": 0.90, "cybernetic_connection": 0.80, "ai_lineage": 0.94, "biological_caution": 0.98, "historical_influence": 0.86, "interpretability": 0.78, "formal_tractability": 0.76, "responsible_use_relevance": 0.98},
    ]


def score_concept(row: dict[str, object], config: NeuralLogicConfig) -> dict[str, object]:
    keys = [
        "logical_clarity", "neural_abstraction", "computational_relevance",
        "cybernetic_connection", "ai_lineage", "biological_caution",
        "historical_influence", "interpretability", "formal_tractability",
        "responsible_use_relevance",
    ]
    score = mean(float(row[key]) for key in keys)
    if score >= config.core_threshold and float(row["historical_influence"]) >= config.high_influence_threshold:
        status = "core_neural_logic_thread"
    elif score >= config.core_threshold:
        status = "major_neural_logic_thread"
    else:
        status = "supporting_neural_logic_thread"

    scored = {key: round(float(row[key]), 6) for key in keys}
    scored.update({
        "concept_id": row["concept_id"],
        "neural_logic_score": round(score, 6),
        "interpretive_status": status,
    })
    return scored


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_confuse_simplified_neuron_with_biology", "meaning": "The McCulloch-Pitts neuron is a formal abstraction, not a full biological neuron."},
        {"caution": "do_not_call_it_modern_deep_learning", "meaning": "The model is foundational to neural-network history but lacks modern learning, gradients, large data, and deep architectures."},
        {"caution": "do_not_separate_neural_from_symbolic_too_cleanly", "meaning": "The model was both neural and logical."},
        {"caution": "do_not_treat_model_output_as_understanding", "meaning": "A formal network output does not imply cognition or meaning by itself."},
        {"caution": "do_not_ignore_responsibility_in_ai_lineage", "meaning": "Historical neural abstractions should be interpreted with clear limits and responsible use boundaries."},
    ]


def main() -> None:
    config = NeuralLogicConfig()
    concepts = concept_rows()
    scored = [score_concept(row, config) for row in concepts]
    cautions = interpretation_cautions()

    logic_examples = [
        {"gate": "AND", "x1": 0, "x2": 0, "threshold": 2, "output": threshold_unit([0, 0], [1, 1], 2)},
        {"gate": "AND", "x1": 1, "x2": 1, "threshold": 2, "output": threshold_unit([1, 1], [1, 1], 2)},
        {"gate": "OR", "x1": 1, "x2": 0, "threshold": 1, "output": threshold_unit([1, 0], [1, 1], 1)},
        {"gate": "OR", "x1": 0, "x2": 0, "threshold": 1, "output": threshold_unit([0, 0], [1, 1], 1)},
    ]

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "concepts_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_neural_logic_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_neural_logic_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_neural_logic_thread"),
        "mean_neural_logic_score": round(mean(float(row["neural_logic_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "McCulloch-Pitts neural logic should be studied as a bridge among threshold units, symbolic logic, neural abstraction, cybernetics, automata, AI history, and responsible model interpretation.",
    }

    write_csv(TABLES / "neural_logic_concepts.csv", concepts)
    write_csv(TABLES / "mcculloch_pitts_neural_logic_map.csv", scored)
    write_csv(TABLES / "threshold_logic_examples.csv", logic_examples)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "neural_logic_summary.csv", [summary])

    write_json(JSON_DIR / "neural_logic_config.json", asdict(config))
    write_json(JSON_DIR / "mcculloch_pitts_neural_logic_map.json", scored)
    write_json(JSON_DIR / "threshold_logic_examples.json", logic_examples)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "neural_logic_summary.json", summary)

    print("McCulloch-Pitts neural logic map complete.")
    print(TABLES / "neural_logic_summary.csv")


if __name__ == "__main__":
    main()
