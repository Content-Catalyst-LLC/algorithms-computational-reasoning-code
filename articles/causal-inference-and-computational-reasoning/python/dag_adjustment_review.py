from __future__ import annotations

from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
EDGES = ROOT / "data" / "causal_graph_edges.csv"
OUT_TABLE = ROOT / "outputs" / "tables" / "dag_adjustment_review.csv"
OUT_JSON = ROOT / "outputs" / "json" / "dag_adjustment_review.json"


def read_edges() -> list[dict[str, str]]:
    with EDGES.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def review_adjustment_set(edges: list[dict[str, str]]) -> list[dict[str, object]]:
    treatment = "treatment"
    outcome = "observed_outcome"
    parents_of_treatment = {edge["source"] for edge in edges if edge["target"] == treatment}
    parents_of_outcome = {edge["source"] for edge in edges if edge["target"] == outcome}
    candidate_confounders = sorted((parents_of_treatment & parents_of_outcome) - {treatment})
    mediators_or_post_treatment = sorted({edge["target"] for edge in edges if edge["source"] == treatment and edge["target"] != outcome})
    rows = []
    for variable in candidate_confounders:
        rows.append({
            "variable": variable,
            "role": "candidate_confounder",
            "include_in_adjustment_set": True,
            "reason": "Variable is represented as a common cause of treatment and outcome in the teaching DAG.",
        })
    for variable in mediators_or_post_treatment:
        rows.append({
            "variable": variable,
            "role": "post_treatment_or_mediator",
            "include_in_adjustment_set": False,
            "reason": "Post-treatment variables should not be controlled for when estimating total treatment effect.",
        })
    return rows


def write_outputs(rows: list[dict[str, object]]) -> None:
    OUT_TABLE.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUT_TABLE.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = ["variable", "role", "include_in_adjustment_set", "reason"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    OUT_JSON.write_text(json.dumps(rows, indent=2, sort_keys=True), encoding="utf-8")


def main() -> None:
    rows = review_adjustment_set(read_edges())
    write_outputs(rows)
    print("DAG adjustment review complete.")
    print(OUT_TABLE)


if __name__ == "__main__":
    main()
