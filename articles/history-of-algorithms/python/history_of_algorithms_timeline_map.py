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
class AlgorithmHistoryConfig:
    article: str = "history_of_algorithms"
    core_threshold: float = 0.80
    high_procedure_threshold: float = 0.86


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


def history_layers() -> list[dict[str, object]]:
    return [
        {"layer_id": "ancient_worked_procedures", "procedural_explicitness": 0.92, "representation": 0.84, "proof_correctness": 0.80, "portability": 0.82, "mechanization": 0.30, "formalization": 0.54, "programmability": 0.20, "institutional_adoption": 0.78, "governance_relevance": 0.62, "modern_resonance": 0.90},
        {"layer_id": "greek_demonstrated_procedure", "procedural_explicitness": 0.90, "representation": 0.88, "proof_correctness": 0.98, "portability": 0.86, "mechanization": 0.28, "formalization": 0.76, "programmability": 0.22, "institutional_adoption": 0.82, "governance_relevance": 0.60, "modern_resonance": 0.92},
        {"layer_id": "indian_numeration_and_calculation", "procedural_explicitness": 0.94, "representation": 0.98, "proof_correctness": 0.84, "portability": 0.96, "mechanization": 0.34, "formalization": 0.76, "programmability": 0.32, "institutional_adoption": 0.88, "governance_relevance": 0.66, "modern_resonance": 0.98},
        {"layer_id": "chinese_procedural_mathematics", "procedural_explicitness": 0.92, "representation": 0.92, "proof_correctness": 0.82, "portability": 0.88, "mechanization": 0.34, "formalization": 0.74, "programmability": 0.30, "institutional_adoption": 0.86, "governance_relevance": 0.70, "modern_resonance": 0.92},
        {"layer_id": "islamic_world_algorism_and_algebra", "procedural_explicitness": 0.98, "representation": 0.94, "proof_correctness": 0.92, "portability": 0.98, "mechanization": 0.54, "formalization": 0.84, "programmability": 0.42, "institutional_adoption": 0.94, "governance_relevance": 0.72, "modern_resonance": 0.98},
        {"layer_id": "latin_reception_and_commercial_arithmetic", "procedural_explicitness": 0.94, "representation": 0.94, "proof_correctness": 0.84, "portability": 0.96, "mechanization": 0.44, "formalization": 0.78, "programmability": 0.36, "institutional_adoption": 0.96, "governance_relevance": 0.76, "modern_resonance": 0.94},
        {"layer_id": "early_modern_symbolism_and_tables", "procedural_explicitness": 0.92, "representation": 0.98, "proof_correctness": 0.92, "portability": 0.96, "mechanization": 0.62, "formalization": 0.92, "programmability": 0.54, "institutional_adoption": 0.96, "governance_relevance": 0.74, "modern_resonance": 0.96},
        {"layer_id": "mechanical_and_programmable_machines", "procedural_explicitness": 0.96, "representation": 0.94, "proof_correctness": 0.86, "portability": 0.90, "mechanization": 0.98, "formalization": 0.88, "programmability": 0.90, "institutional_adoption": 0.92, "governance_relevance": 0.76, "modern_resonance": 0.98},
        {"layer_id": "logic_computability_and_turing_machines", "procedural_explicitness": 0.98, "representation": 0.96, "proof_correctness": 0.98, "portability": 0.96, "mechanization": 0.86, "formalization": 0.98, "programmability": 0.92, "institutional_adoption": 0.92, "governance_relevance": 0.80, "modern_resonance": 0.98},
        {"layer_id": "electronic_computing_and_software", "procedural_explicitness": 0.98, "representation": 0.98, "proof_correctness": 0.92, "portability": 0.94, "mechanization": 0.98, "formalization": 0.94, "programmability": 0.98, "institutional_adoption": 0.98, "governance_relevance": 0.88, "modern_resonance": 0.98},
        {"layer_id": "ai_platforms_and_governance", "procedural_explicitness": 0.90, "representation": 0.94, "proof_correctness": 0.78, "portability": 0.92, "mechanization": 0.98, "formalization": 0.88, "programmability": 0.96, "institutional_adoption": 0.98, "governance_relevance": 0.98, "modern_resonance": 0.98},
    ]


def score_layer(row: dict[str, object], config: AlgorithmHistoryConfig) -> dict[str, object]:
    history_score = mean([
        float(row["procedural_explicitness"]),
        float(row["representation"]),
        float(row["proof_correctness"]),
        float(row["portability"]),
        float(row["mechanization"]),
        float(row["formalization"]),
        float(row["programmability"]),
        float(row["institutional_adoption"]),
        float(row["governance_relevance"]),
        float(row["modern_resonance"]),
    ])

    if history_score >= config.core_threshold and float(row["procedural_explicitness"]) >= config.high_procedure_threshold:
        interpretive_status = "core_algorithm_history_layer"
    elif history_score >= config.core_threshold:
        interpretive_status = "major_algorithm_history_layer"
    else:
        interpretive_status = "supporting_algorithm_history_layer"

    return {
        "layer_id": row["layer_id"],
        "procedural_explicitness": round(float(row["procedural_explicitness"]), 6),
        "representation": round(float(row["representation"]), 6),
        "proof_correctness": round(float(row["proof_correctness"]), 6),
        "portability": round(float(row["portability"]), 6),
        "mechanization": round(float(row["mechanization"]), 6),
        "formalization": round(float(row["formalization"]), 6),
        "programmability": round(float(row["programmability"]), 6),
        "institutional_adoption": round(float(row["institutional_adoption"]), 6),
        "governance_relevance": round(float(row["governance_relevance"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "history_score": round(history_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_treat_algorithm_history_as_computer_history_only", "meaning": "Algorithms have procedural ancestors long before electronic computers."},
        {"caution": "do_not_confuse_word_origin_with_total_origin", "meaning": "The word algorithm matters, but procedure history is broader."},
        {"caution": "do_not_project_modern_code_backward", "meaning": "Historical procedures can be algorithm-like without being programs."},
        {"caution": "do_not_ignore_institutions", "meaning": "Teaching, translation, copying, commerce, machines, and governance make algorithms durable."},
        {"caution": "do_not_reduce_history_to_efficiency", "meaning": "Correctness, proof, trust, responsibility, and public consequence also matter."},
    ]


def main() -> None:
    config = AlgorithmHistoryConfig()
    layers = history_layers()
    scored = [score_layer(row, config) for row in layers]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "layers_reviewed": len(scored),
        "core_layers": sum(1 for row in scored if row["interpretive_status"] == "core_algorithm_history_layer"),
        "major_layers": sum(1 for row in scored if row["interpretive_status"] == "major_algorithm_history_layer"),
        "supporting_layers": sum(1 for row in scored if row["interpretive_status"] == "supporting_algorithm_history_layer"),
        "mean_history_score": round(mean(float(row["history_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Algorithm history is a layered movement from procedure to computation: examples, rules, notation, proof, tables, machines, programs, analysis, platforms, and governance.",
    }

    write_csv(TABLES / "algorithm_history_layers.csv", layers)
    write_csv(TABLES / "algorithm_history_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "algorithm_history_summary.csv", [summary])

    write_json(JSON_DIR / "algorithm_history_config.json", asdict(config))
    write_json(JSON_DIR / "algorithm_history_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "algorithm_history_summary.json", summary)

    print("Algorithm history timeline map complete.")
    print(TABLES / "algorithm_history_summary.csv")


if __name__ == "__main__":
    main()
