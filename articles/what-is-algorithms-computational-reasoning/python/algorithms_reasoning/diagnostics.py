from __future__ import annotations

from dataclasses import asdict, dataclass
from math import log2
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class AlgorithmScenario:
    scenario: str
    representation_quality: float
    indexing_strength: float
    decomposition_strength: float
    correctness_evidence: float
    interpretability: float
    robustness: float
    governance_readiness: float
    data_quality: float
    objective_alignment: float
    brute_force_pressure: float
    memory_efficiency: float
    monitoring_strength: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def safe_log(value: float) -> float:
    return log2(max(2.0, value))


def load_scenarios(path: Path) -> list[AlgorithmScenario]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = []
        for row in reader:
            rows.append(AlgorithmScenario(
                scenario=row["scenario"],
                representation_quality=float(row["representation_quality"]),
                indexing_strength=float(row["indexing_strength"]),
                decomposition_strength=float(row["decomposition_strength"]),
                correctness_evidence=float(row["correctness_evidence"]),
                interpretability=float(row["interpretability"]),
                robustness=float(row["robustness"]),
                governance_readiness=float(row["governance_readiness"]),
                data_quality=float(row["data_quality"]),
                objective_alignment=float(row["objective_alignment"]),
                brute_force_pressure=float(row["brute_force_pressure"]),
                memory_efficiency=float(row["memory_efficiency"]),
                monitoring_strength=float(row["monitoring_strength"]),
            ))
        return rows


def evaluate_scenario(scenario: AlgorithmScenario, max_power: int = 14) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for power in range(4, max_power + 1):
        input_size = 2 ** power

        brute_force_growth = scenario.brute_force_pressure * (input_size ** 2) / 12000.0
        indexed_growth = (1.0 - scenario.indexing_strength) * input_size / 180.0
        decomposition_gain = scenario.decomposition_strength * safe_log(input_size) * 2.4
        representation_gain = scenario.representation_quality * 18.0
        data_penalty = (1.0 - scenario.data_quality) * 22.0
        objective_penalty = (1.0 - scenario.objective_alignment) * 24.0

        runtime_pressure = clamp(
            brute_force_growth + indexed_growth - decomposition_gain - representation_gain + data_penalty
        )
        memory_pressure = clamp(
            (1.0 - scenario.memory_efficiency) * 48.0
            + scenario.brute_force_pressure * safe_log(input_size) * 3.0
            - scenario.representation_quality * 10.0
            - scenario.decomposition_strength * 8.0
        )
        correctness_risk = clamp(
            70.0
            - scenario.correctness_evidence * 42.0
            - scenario.robustness * 18.0
            + data_penalty * 0.6
            + objective_penalty * 0.4
        )
        opacity_risk = clamp(
            65.0
            - scenario.interpretability * 45.0
            - scenario.representation_quality * 12.0
            - scenario.governance_readiness * 8.0
        )
        governance_risk = clamp(
            75.0
            - scenario.governance_readiness * 36.0
            - scenario.monitoring_strength * 24.0
            - scenario.objective_alignment * 18.0
            + opacity_risk * 0.20
            + correctness_risk * 0.15
        )
        reasoning_quality_score = clamp(
            scenario.representation_quality * 18.0
            + scenario.indexing_strength * 11.0
            + scenario.decomposition_strength * 12.0
            + scenario.correctness_evidence * 16.0
            + scenario.interpretability * 11.0
            + scenario.robustness * 10.0
            + scenario.governance_readiness * 11.0
            + scenario.objective_alignment * 11.0
            - runtime_pressure * 0.20
            - memory_pressure * 0.12
            - correctness_risk * 0.18
            - opacity_risk * 0.12
            - governance_risk * 0.16
        )

        records.append({
            "scenario": scenario.scenario,
            "input_size": input_size,
            "runtime_pressure": round(runtime_pressure, 3),
            "memory_pressure": round(memory_pressure, 3),
            "correctness_risk": round(correctness_risk, 3),
            "opacity_risk": round(opacity_risk, 3),
            "governance_risk": round(governance_risk, 3),
            "reasoning_quality_score": round(reasoning_quality_score, 3),
        })

    return records


def summarize(records: list[dict[str, object]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for scenario_name in sorted({record["scenario"] for record in records}):
        subset = [record for record in records if record["scenario"] == scenario_name]
        final = subset[-1]
        avg_runtime = mean(float(record["runtime_pressure"]) for record in subset)
        avg_correctness = mean(float(record["correctness_risk"]) for record in subset)
        avg_governance = mean(float(record["governance_risk"]) for record in subset)
        avg_score = mean(float(record["reasoning_quality_score"]) for record in subset)

        if float(final["reasoning_quality_score"]) >= 70 and float(final["governance_risk"]) <= 35:
            diagnostic = "strong computational reasoning with governance support"
        elif avg_runtime >= 65:
            diagnostic = "runtime pressure dominates the design"
        elif avg_correctness >= 55:
            diagnostic = "correctness evidence is too weak"
        elif avg_governance >= 55:
            diagnostic = "governance and monitoring need improvement"
        elif avg_score >= 55:
            diagnostic = "partial reasoning strength with remaining design risk"
        else:
            diagnostic = "weak algorithmic reasoning structure"

        output.append({
            "scenario": scenario_name,
            "final_input_size": final["input_size"],
            "final_runtime_pressure": final["runtime_pressure"],
            "final_memory_pressure": final["memory_pressure"],
            "final_correctness_risk": final["correctness_risk"],
            "final_opacity_risk": final["opacity_risk"],
            "final_governance_risk": final["governance_risk"],
            "final_reasoning_quality_score": final["reasoning_quality_score"],
            "average_runtime_pressure": round(avg_runtime, 3),
            "average_correctness_risk": round(avg_correctness, 3),
            "average_governance_risk": round(avg_governance, 3),
            "average_reasoning_quality_score": round(avg_score, 3),
            "diagnostic": diagnostic,
        })

    return output


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def run_workflow(article_root: Path) -> None:
    data_path = article_root / "data" / "synthetic_algorithm_scenarios.csv"
    output_dir = article_root / "outputs"
    scenarios = load_scenarios(data_path)
    records: list[dict[str, object]] = []
    for scenario in scenarios:
        records.extend(evaluate_scenario(scenario))

    summary = summarize(records)

    write_csv(output_dir / "tables" / "algorithmic_reasoning_timeseries.csv", records)
    write_csv(output_dir / "tables" / "algorithmic_reasoning_summary.csv", summary)
    write_json(output_dir / "json" / "algorithmic_reasoning_timeseries.json", records)
    write_json(output_dir / "json" / "algorithmic_reasoning_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
