from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import heapq
import json
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class DijkstraConfig:
    article: str = "edsger_dijkstra_and_the_discipline_of_structured_programming"
    core_threshold: float = 0.80
    high_structure_threshold: float = 0.86


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


def dijkstra_shortest_paths(graph: dict[str, list[tuple[str, float]]], source: str) -> dict[str, float]:
    distances = {node: float("inf") for node in graph}
    distances[source] = 0.0
    heap: list[tuple[float, str]] = [(0.0, source)]
    settled: set[str] = set()

    while heap:
        distance, node = heapq.heappop(heap)
        if node in settled:
            continue
        settled.add(node)
        for neighbor, weight in graph[node]:
            if weight < 0:
                raise ValueError("Dijkstra's algorithm requires nonnegative weights.")
            if distance + weight < distances[neighbor]:
                distances[neighbor] = distance + weight
                heapq.heappush(heap, (distances[neighbor], neighbor))

    return distances


def dijkstra_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "structured_control_flow", "structured_control": 0.98, "correctness": 0.94, "invariants": 0.90, "proof_relevance": 0.92, "formal_methods": 0.88, "readability": 0.98, "maintainability": 0.96, "algorithmic_relevance": 0.90, "system_design": 0.88, "governance_caution": 0.92},
        {"theme_id": "goto_considered_harmful", "structured_control": 0.98, "correctness": 0.90, "invariants": 0.82, "proof_relevance": 0.88, "formal_methods": 0.84, "readability": 0.98, "maintainability": 0.98, "algorithmic_relevance": 0.84, "system_design": 0.82, "governance_caution": 0.90},
        {"theme_id": "program_correctness", "structured_control": 0.92, "correctness": 0.98, "invariants": 0.94, "proof_relevance": 0.98, "formal_methods": 0.98, "readability": 0.90, "maintainability": 0.94, "algorithmic_relevance": 0.90, "system_design": 0.88, "governance_caution": 0.96},
        {"theme_id": "loop_invariants", "structured_control": 0.94, "correctness": 0.98, "invariants": 0.98, "proof_relevance": 0.96, "formal_methods": 0.94, "readability": 0.88, "maintainability": 0.92, "algorithmic_relevance": 0.94, "system_design": 0.84, "governance_caution": 0.92},
        {"theme_id": "weakest_preconditions", "structured_control": 0.90, "correctness": 0.98, "invariants": 0.92, "proof_relevance": 0.98, "formal_methods": 0.98, "readability": 0.84, "maintainability": 0.88, "algorithmic_relevance": 0.90, "system_design": 0.86, "governance_caution": 0.94},
        {"theme_id": "guarded_commands", "structured_control": 0.94, "correctness": 0.96, "invariants": 0.92, "proof_relevance": 0.98, "formal_methods": 0.98, "readability": 0.86, "maintainability": 0.88, "algorithmic_relevance": 0.88, "system_design": 0.84, "governance_caution": 0.92},
        {"theme_id": "dijkstra_shortest_path_algorithm", "structured_control": 0.86, "correctness": 0.96, "invariants": 0.96, "proof_relevance": 0.94, "formal_methods": 0.90, "readability": 0.86, "maintainability": 0.86, "algorithmic_relevance": 0.98, "system_design": 0.88, "governance_caution": 0.88},
        {"theme_id": "layered_systems_and_concurrency", "structured_control": 0.88, "correctness": 0.94, "invariants": 0.92, "proof_relevance": 0.92, "formal_methods": 0.94, "readability": 0.88, "maintainability": 0.96, "algorithmic_relevance": 0.88, "system_design": 0.98, "governance_caution": 0.96},
        {"theme_id": "ai_generated_code_review", "structured_control": 0.92, "correctness": 0.98, "invariants": 0.90, "proof_relevance": 0.94, "formal_methods": 0.90, "readability": 0.94, "maintainability": 0.96, "algorithmic_relevance": 0.90, "system_design": 0.92, "governance_caution": 0.98},
    ]


def score_theme(row: dict[str, object], config: DijkstraConfig) -> dict[str, object]:
    discipline_score = mean([
        float(row["structured_control"]),
        float(row["correctness"]),
        float(row["invariants"]),
        float(row["proof_relevance"]),
        float(row["formal_methods"]),
        float(row["readability"]),
        float(row["maintainability"]),
        float(row["algorithmic_relevance"]),
        float(row["system_design"]),
        float(row["governance_caution"]),
    ])

    if discipline_score >= config.core_threshold and float(row["structured_control"]) >= config.high_structure_threshold:
        interpretive_status = "core_dijkstra_structured_programming_thread"
    elif discipline_score >= config.core_threshold:
        interpretive_status = "major_dijkstra_structured_programming_thread"
    else:
        interpretive_status = "supporting_dijkstra_structured_programming_thread"

    scored = {key: round(float(row[key]), 6) for key in [
        "structured_control", "correctness", "invariants", "proof_relevance",
        "formal_methods", "readability", "maintainability", "algorithmic_relevance",
        "system_design", "governance_caution"
    ]}
    scored.update({
        "theme_id": row["theme_id"],
        "discipline_score": round(discipline_score, 6),
        "interpretive_status": interpretive_status,
    })
    return scored


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_reduce_dijkstra_to_goto", "meaning": "The go to debate was part of a broader discipline of structured reasoning and correctness."},
        {"caution": "do_not_confuse_testing_with_proof", "meaning": "Testing is essential but does not usually prove absence of errors."},
        {"caution": "do_not_treat_structure_as_style_only", "meaning": "Program structure affects the ability to reason about correctness."},
        {"caution": "do_not_ignore_assumptions", "meaning": "Algorithms and proofs depend on preconditions such as nonnegative edge weights."},
        {"caution": "do_not_accept_ai_generated_code_without_reasoning", "meaning": "Generated code still requires specification, review, tests, invariants, and accountability."},
    ]


def main() -> None:
    config = DijkstraConfig()
    themes = dijkstra_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", 1), ("D", 5)],
        "C": [("B", 1), ("D", 8), ("E", 10)],
        "D": [("E", 2)],
        "E": [],
    }
    shortest_paths = [
        {"source": "A", "node": node, "distance": dist}
        for node, dist in sorted(dijkstra_shortest_paths(graph, "A").items())
    ]

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_dijkstra_structured_programming_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_dijkstra_structured_programming_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_dijkstra_structured_programming_thread"),
        "mean_discipline_score": round(mean(float(row["discipline_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Dijkstra should be studied as a theorist of structured programming, correctness, invariants, weakest preconditions, guarded commands, and disciplined software reasoning.",
    }

    write_csv(TABLES / "dijkstra_themes.csv", themes)
    write_csv(TABLES / "dijkstra_structured_programming_map.csv", scored)
    write_csv(TABLES / "dijkstra_shortest_path_example.csv", shortest_paths)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "dijkstra_structured_programming_summary.csv", [summary])

    write_json(JSON_DIR / "dijkstra_config.json", asdict(config))
    write_json(JSON_DIR / "dijkstra_structured_programming_map.json", scored)
    write_json(JSON_DIR / "dijkstra_shortest_path_example.json", shortest_paths)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "dijkstra_structured_programming_summary.json", summary)

    print("Dijkstra structured programming map complete.")
    print(TABLES / "dijkstra_structured_programming_summary.csv")


if __name__ == "__main__":
    main()
