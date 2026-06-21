# simulation_as_computational_reasoning_audit.py
# Dependency-light workflow for scenario simulation, uncertainty review, and sensitivity audit.

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean, pstdev
import csv
import json
import random

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class SimulationScenario:
    scenario_name: str
    initial_stock: float
    growth_rate: float
    loss_rate: float
    intervention_strength: float
    shock_probability: float
    shock_size: float
    time_steps: int


def clamp(value: float, low: float = 0.0) -> float:
    return max(low, value)


def run_stock_flow_simulation(scenario: SimulationScenario, stochastic: bool = False, seed: int | None = None) -> list[dict[str, object]]:
    rng = random.Random(seed)
    stock = scenario.initial_stock
    rows: list[dict[str, object]] = []
    for t in range(scenario.time_steps + 1):
        rows.append({
            "scenario_name": scenario.scenario_name,
            "time_step": t,
            "stock": round(stock, 6),
            "stochastic": stochastic,
        })
        growth = scenario.growth_rate * stock
        loss = scenario.loss_rate * stock
        intervention = scenario.intervention_strength * stock
        shock = scenario.shock_size * stock if stochastic and rng.random() < scenario.shock_probability else 0.0
        stock = clamp(stock + growth - loss - intervention - shock)
    return rows


def scenario_summary(rows: list[dict[str, object]]) -> dict[str, object]:
    stocks = [float(row["stock"]) for row in rows]
    return {
        "scenario_name": rows[0]["scenario_name"],
        "stochastic": rows[0]["stochastic"],
        "initial_stock": stocks[0],
        "final_stock": stocks[-1],
        "peak_stock": max(stocks),
        "minimum_stock": min(stocks),
        "total_stock_over_time": round(sum(stocks), 6),
        "average_stock": round(mean(stocks), 6),
        "interpretation": "Scenario trajectory summarizes how model rules transform initial conditions over time.",
    }


def build_scenarios() -> list[SimulationScenario]:
    return [
        SimulationScenario("baseline_growth", 100.0, 0.08, 0.03, 0.00, 0.00, 0.00, 30),
        SimulationScenario("moderate_intervention", 100.0, 0.08, 0.03, 0.04, 0.00, 0.00, 30),
        SimulationScenario("strong_intervention", 100.0, 0.08, 0.03, 0.08, 0.00, 0.00, 30),
        SimulationScenario("stochastic_shocks", 100.0, 0.08, 0.03, 0.04, 0.18, 0.12, 30),
    ]


def run_all_deterministic() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    all_rows: list[dict[str, object]] = []
    summaries: list[dict[str, object]] = []
    for scenario in build_scenarios()[:3]:
        rows = run_stock_flow_simulation(scenario, stochastic=False)
        all_rows.extend(rows)
        summaries.append(scenario_summary(rows))
    return all_rows, summaries


def run_monte_carlo(scenario: SimulationScenario, runs: int = 250) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for run_id in range(1, runs + 1):
        trajectory = run_stock_flow_simulation(scenario, stochastic=True, seed=run_id)
        stocks = [float(row["stock"]) for row in trajectory]
        rows.append({
            "run_id": run_id,
            "scenario_name": scenario.scenario_name,
            "final_stock": round(stocks[-1], 6),
            "peak_stock": round(max(stocks), 6),
            "minimum_stock": round(min(stocks), 6),
            "total_stock_over_time": round(sum(stocks), 6),
        })
    return rows


def quantile(values: list[float], q: float) -> float:
    values = sorted(values)
    idx = int(round((len(values) - 1) * q))
    return values[idx]


def monte_carlo_summary(rows: list[dict[str, object]]) -> dict[str, object]:
    final_values = [float(row["final_stock"]) for row in rows]
    total_values = [float(row["total_stock_over_time"]) for row in rows]
    return {
        "scenario_name": rows[0]["scenario_name"],
        "runs": len(rows),
        "mean_final_stock": round(mean(final_values), 6),
        "std_final_stock": round(pstdev(final_values), 6),
        "p05_final_stock": round(quantile(final_values, 0.05), 6),
        "p50_final_stock": round(quantile(final_values, 0.50), 6),
        "p95_final_stock": round(quantile(final_values, 0.95), 6),
        "mean_total_stock_over_time": round(mean(total_values), 6),
        "interpretation": "Monte Carlo results summarize uncertainty across repeated stochastic simulation runs.",
    }


def parameter_sweep() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for intervention in [0.00, 0.02, 0.04, 0.06, 0.08, 0.10]:
        scenario = SimulationScenario(f"intervention_{intervention:.2f}", 100.0, 0.08, 0.03, intervention, 0.00, 0.00, 30)
        trajectory = run_stock_flow_simulation(scenario, stochastic=False)
        stocks = [float(row["stock"]) for row in trajectory]
        rows.append({
            "intervention_strength": intervention,
            "final_stock": round(stocks[-1], 6),
            "peak_stock": round(max(stocks), 6),
            "total_stock_over_time": round(sum(stocks), 6),
            "threshold_crossed": max(stocks) >= 300.0,
        })
    return rows


def simulation_review_checklist() -> list[dict[str, object]]:
    return [
        {"check": "purpose_defined", "question": "Is the simulation purpose explicitly stated?", "status": "complete"},
        {"check": "assumptions_documented", "question": "Are model assumptions and boundaries documented?", "status": "complete"},
        {"check": "parameters_reviewed", "question": "Are parameter meanings, sources, and ranges documented?", "status": "partial"},
        {"check": "sensitivity_tested", "question": "Have important parameters been varied?", "status": "complete"},
        {"check": "uncertainty_reported", "question": "Are stochastic outcomes summarized as ranges rather than single values?", "status": "complete"},
        {"check": "validation_evidence_linked", "question": "Is there evidence that the model is fit for intended use?", "status": "partial"},
        {"check": "limitations_communicated", "question": "Are omitted mechanisms and interpretation limits stated?", "status": "complete"},
        {"check": "decision_use_governed", "question": "Is use of simulation output in decisions documented?", "status": "needs_review"},
    ]


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


def main() -> None:
    deterministic_rows, deterministic_summary = run_all_deterministic()
    stochastic_scenario = build_scenarios()[3]
    mc_rows = run_monte_carlo(stochastic_scenario, runs=250)
    mc_summary = monte_carlo_summary(mc_rows)
    sweep_rows = parameter_sweep()
    checklist_rows = simulation_review_checklist()
    all_summary = {
        "deterministic_scenarios": len(deterministic_summary),
        "monte_carlo_runs": len(mc_rows),
        "lowest_final_stock_in_sweep": min(row["final_stock"] for row in sweep_rows),
        "highest_final_stock_in_sweep": max(row["final_stock"] for row in sweep_rows),
        "review_items_needing_attention": sum(1 for row in checklist_rows if row["status"] in {"partial", "needs_review"}),
        "interpretation": "Simulation as computational reasoning compares scenarios, explores uncertainty, tests sensitivity, and documents assumptions so modeled consequences can be interpreted responsibly.",
    }

    write_csv(TABLES / "deterministic_simulation_trajectories.csv", deterministic_rows)
    write_csv(TABLES / "deterministic_simulation_summary.csv", deterministic_summary)
    write_csv(TABLES / "monte_carlo_simulation_runs.csv", mc_rows)
    write_csv(TABLES / "monte_carlo_simulation_summary.csv", [mc_summary])
    write_csv(TABLES / "parameter_sweep.csv", sweep_rows)
    write_csv(TABLES / "simulation_review_checklist.csv", checklist_rows)
    write_csv(TABLES / "simulation_audit_summary.csv", [all_summary])

    write_json(JSON_DIR / "deterministic_simulation_trajectories.json", deterministic_rows)
    write_json(JSON_DIR / "deterministic_simulation_summary.json", deterministic_summary)
    write_json(JSON_DIR / "monte_carlo_simulation_runs.json", mc_rows)
    write_json(JSON_DIR / "monte_carlo_simulation_summary.json", mc_summary)
    write_json(JSON_DIR / "parameter_sweep.json", sweep_rows)
    write_json(JSON_DIR / "simulation_review_checklist.json", checklist_rows)
    write_json(JSON_DIR / "simulation_audit_summary.json", all_summary)

    print("Simulation as computational reasoning audit complete.")
    print(TABLES / "simulation_audit_summary.csv")


if __name__ == "__main__":
    main()
