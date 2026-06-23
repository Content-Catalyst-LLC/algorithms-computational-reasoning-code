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
class DataStructureHistoryConfig:
    article: str = "the_history_of_data_structures_and_algorithm_analysis"
    core_threshold: float = 0.80
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


def binary_search_steps(n: int) -> int:
    if n <= 0:
        return 0
    return math.ceil(math.log2(n + 1))


def adjacency_memory_nodes_edges(nodes: int, edges: int) -> dict[str, int]:
    return {
        "nodes": nodes,
        "edges": edges,
        "adjacency_matrix_cells": nodes * nodes,
        "adjacency_list_units": nodes + edges,
    }


def structure_traditions() -> list[dict[str, object]]:
    return [
        {"tradition_id": "arrays_records_contiguous_memory", "representation_centrality": 0.96, "operation_clarity": 0.92, "memory_awareness": 0.98, "time_analysis": 0.88, "space_analysis": 0.96, "scale_sensitivity": 0.90, "abstraction_maturity": 0.82, "systems_relevance": 0.96, "historical_influence": 0.98, "governance_caution": 0.86},
        {"tradition_id": "linked_structures_pointers", "representation_centrality": 0.96, "operation_clarity": 0.88, "memory_awareness": 0.98, "time_analysis": 0.86, "space_analysis": 0.92, "scale_sensitivity": 0.88, "abstraction_maturity": 0.80, "systems_relevance": 0.96, "historical_influence": 0.94, "governance_caution": 0.96},
        {"tradition_id": "stacks_queues_access_discipline", "representation_centrality": 0.90, "operation_clarity": 0.98, "memory_awareness": 0.82, "time_analysis": 0.92, "space_analysis": 0.84, "scale_sensitivity": 0.84, "abstraction_maturity": 0.92, "systems_relevance": 0.94, "historical_influence": 0.94, "governance_caution": 0.86},
        {"tradition_id": "trees_hierarchical_search", "representation_centrality": 0.98, "operation_clarity": 0.92, "memory_awareness": 0.90, "time_analysis": 0.96, "space_analysis": 0.88, "scale_sensitivity": 0.96, "abstraction_maturity": 0.92, "systems_relevance": 0.96, "historical_influence": 0.98, "governance_caution": 0.90},
        {"tradition_id": "heaps_priority_queues", "representation_centrality": 0.92, "operation_clarity": 0.94, "memory_awareness": 0.86, "time_analysis": 0.96, "space_analysis": 0.84, "scale_sensitivity": 0.92, "abstraction_maturity": 0.90, "systems_relevance": 0.94, "historical_influence": 0.92, "governance_caution": 0.88},
        {"tradition_id": "hash_tables_expected_access", "representation_centrality": 0.96, "operation_clarity": 0.88, "memory_awareness": 0.88, "time_analysis": 0.94, "space_analysis": 0.88, "scale_sensitivity": 0.94, "abstraction_maturity": 0.92, "systems_relevance": 0.98, "historical_influence": 0.96, "governance_caution": 0.94},
        {"tradition_id": "graphs_relational_structure", "representation_centrality": 0.98, "operation_clarity": 0.90, "memory_awareness": 0.92, "time_analysis": 0.98, "space_analysis": 0.94, "scale_sensitivity": 0.98, "abstraction_maturity": 0.90, "systems_relevance": 0.98, "historical_influence": 0.98, "governance_caution": 0.96},
        {"tradition_id": "files_indexes_databases", "representation_centrality": 0.94, "operation_clarity": 0.88, "memory_awareness": 0.96, "time_analysis": 0.94, "space_analysis": 0.96, "scale_sensitivity": 0.98, "abstraction_maturity": 0.92, "systems_relevance": 0.98, "historical_influence": 0.96, "governance_caution": 0.98},
        {"tradition_id": "abstract_data_types", "representation_centrality": 0.92, "operation_clarity": 0.98, "memory_awareness": 0.82, "time_analysis": 0.90, "space_analysis": 0.84, "scale_sensitivity": 0.88, "abstraction_maturity": 0.98, "systems_relevance": 0.92, "historical_influence": 0.96, "governance_caution": 0.90},
        {"tradition_id": "asymptotic_algorithm_analysis", "representation_centrality": 0.86, "operation_clarity": 0.94, "memory_awareness": 0.88, "time_analysis": 0.98, "space_analysis": 0.94, "scale_sensitivity": 0.98, "abstraction_maturity": 0.96, "systems_relevance": 0.92, "historical_influence": 0.98, "governance_caution": 0.94},
        {"tradition_id": "amortized_average_worst_case_analysis", "representation_centrality": 0.86, "operation_clarity": 0.92, "memory_awareness": 0.86, "time_analysis": 0.98, "space_analysis": 0.88, "scale_sensitivity": 0.96, "abstraction_maturity": 0.96, "systems_relevance": 0.90, "historical_influence": 0.94, "governance_caution": 0.94},
        {"tradition_id": "ai_infrastructure_structures", "representation_centrality": 0.98, "operation_clarity": 0.82, "memory_awareness": 0.96, "time_analysis": 0.94, "space_analysis": 0.98, "scale_sensitivity": 0.98, "abstraction_maturity": 0.88, "systems_relevance": 0.98, "historical_influence": 0.88, "governance_caution": 0.98},
    ]


def score_tradition(row: dict[str, object], config: DataStructureHistoryConfig) -> dict[str, object]:
    history_score = mean([
        float(row["representation_centrality"]),
        float(row["operation_clarity"]),
        float(row["memory_awareness"]),
        float(row["time_analysis"]),
        float(row["space_analysis"]),
        float(row["scale_sensitivity"]),
        float(row["abstraction_maturity"]),
        float(row["systems_relevance"]),
        float(row["historical_influence"]),
        float(row["governance_caution"]),
    ])

    if history_score >= config.core_threshold and float(row["historical_influence"]) >= config.high_influence_threshold:
        interpretive_status = "core_data_structure_analysis_history_thread"
    elif history_score >= config.core_threshold:
        interpretive_status = "major_data_structure_analysis_history_thread"
    else:
        interpretive_status = "supporting_data_structure_analysis_history_thread"

    scored = {key: round(float(row[key]), 6) for key in [
        "representation_centrality", "operation_clarity", "memory_awareness",
        "time_analysis", "space_analysis", "scale_sensitivity", "abstraction_maturity",
        "systems_relevance", "historical_influence", "governance_caution"
    ]}
    scored.update({
        "tradition_id": row["tradition_id"],
        "history_score": round(history_score, 6),
        "interpretive_status": interpretive_status,
    })
    return scored


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_separate_algorithm_from_representation", "meaning": "Algorithmic cost depends on how data are structured."},
        {"caution": "do_not_treat_big_o_as_the_only_truth", "meaning": "Asymptotic analysis must be complemented by constants, memory, locality, I/O, and measurement."},
        {"caution": "do_not_ignore_space_cost", "meaning": "Memory and storage can dominate runtime and feasibility."},
        {"caution": "do_not_assume_average_case_without_assumptions", "meaning": "Expected cost depends on distributions, hash behavior, and adversarial inputs."},
        {"caution": "do_not_build_ai_systems_without_data_structure_audits", "meaning": "AI infrastructure depends on indexes, tensors, queues, embeddings, logs, and provenance structures."},
    ]


def main() -> None:
    config = DataStructureHistoryConfig()
    traditions = structure_traditions()
    scored = [score_tradition(row, config) for row in traditions]
    cautions = interpretation_cautions()

    growth_rows = [
        {"n": n, "constant": 1, "log2_n": round(math.log2(n), 6), "linear": n, "n_log2_n": round(n * math.log2(n), 6), "quadratic": n * n}
        for n in [10, 100, 1000, 10000]
    ]
    binary_rows = [
        {"n": n, "binary_search_steps": binary_search_steps(n)}
        for n in [1, 2, 4, 8, 16, 32, 64, 100, 1000]
    ]
    graph_rows = [
        adjacency_memory_nodes_edges(nodes, edges)
        for nodes, edges in [(10, 20), (100, 300), (1000, 4000), (10000, 50000)]
    ]

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "traditions_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_data_structure_analysis_history_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_data_structure_analysis_history_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_data_structure_analysis_history_thread"),
        "mean_history_score": round(mean(float(row["history_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Data-structure and algorithm-analysis history should be studied as a joined history of representation, operation cost, memory, scale, abstraction, systems infrastructure, and governance.",
    }

    write_csv(TABLES / "data_structure_traditions.csv", traditions)
    write_csv(TABLES / "data_structure_algorithm_analysis_history_map.csv", scored)
    write_csv(TABLES / "growth_rate_examples.csv", growth_rows)
    write_csv(TABLES / "binary_search_steps.csv", binary_rows)
    write_csv(TABLES / "graph_representation_memory.csv", graph_rows)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "data_structure_algorithm_analysis_summary.csv", [summary])

    write_json(JSON_DIR / "data_structure_history_config.json", asdict(config))
    write_json(JSON_DIR / "data_structure_algorithm_analysis_history_map.json", scored)
    write_json(JSON_DIR / "growth_rate_examples.json", growth_rows)
    write_json(JSON_DIR / "binary_search_steps.json", binary_rows)
    write_json(JSON_DIR / "graph_representation_memory.json", graph_rows)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "data_structure_algorithm_analysis_summary.json", summary)

    print("Data-structure and algorithm-analysis history map complete.")
    print(TABLES / "data_structure_algorithm_analysis_summary.csv")


if __name__ == "__main__":
    main()
