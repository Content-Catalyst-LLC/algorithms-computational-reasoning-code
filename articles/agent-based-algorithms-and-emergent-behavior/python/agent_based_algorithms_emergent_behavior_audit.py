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
class Agent:
    agent_id: int
    group: str
    row: int
    col: int
    tolerance: float


@dataclass(frozen=True)
class RunConfig:
    grid_size: int
    agents_per_group: int
    tolerance: float
    empty_fraction: float
    steps: int
    seed: int


def neighbors(row: int, col: int, grid_size: int) -> list[tuple[int, int]]:
    cells: list[tuple[int, int]] = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            rr, cc = row + dr, col + dc
            if 0 <= rr < grid_size and 0 <= cc < grid_size:
                cells.append((rr, cc))
    return cells


def build_initial_agents(config: RunConfig) -> list[Agent]:
    rng = random.Random(config.seed)
    total_cells = config.grid_size * config.grid_size
    planned_agents = config.agents_per_group * 2
    max_agents = int(total_cells * (1.0 - config.empty_fraction))
    if planned_agents > max_agents:
        raise ValueError("Too many agents for requested empty fraction.")

    cells = [(r, c) for r in range(config.grid_size) for c in range(config.grid_size)]
    rng.shuffle(cells)
    agents: list[Agent] = []
    agent_id = 1
    for group in ["A", "B"]:
        for _ in range(config.agents_per_group):
            row, col = cells.pop()
            agents.append(Agent(agent_id, group, row, col, config.tolerance))
            agent_id += 1
    return agents


def occupancy_map(agents: list[Agent]) -> dict[tuple[int, int], Agent]:
    return {(a.row, a.col): a for a in agents}


def empty_cells(agents: list[Agent], grid_size: int) -> list[tuple[int, int]]:
    occupied = set(occupancy_map(agents))
    return [(r, c) for r in range(grid_size) for c in range(grid_size) if (r, c) not in occupied]


def same_group_share(agent: Agent, occupied: dict[tuple[int, int], Agent], grid_size: int) -> float:
    nearby = [occupied[cell] for cell in neighbors(agent.row, agent.col, grid_size) if cell in occupied]
    if not nearby:
        return 1.0
    return sum(1 for other in nearby if other.group == agent.group) / len(nearby)


def is_satisfied(agent: Agent, occupied: dict[tuple[int, int], Agent], grid_size: int) -> bool:
    return same_group_share(agent, occupied, grid_size) >= agent.tolerance


def satisfaction_rate(agents: list[Agent], grid_size: int) -> float:
    occupied = occupancy_map(agents)
    return sum(1 for a in agents if is_satisfied(a, occupied, grid_size)) / len(agents)


def clustering_score(agents: list[Agent], grid_size: int) -> float:
    occupied = occupancy_map(agents)
    return mean(same_group_share(a, occupied, grid_size) for a in agents)


def step_agents(agents: list[Agent], config: RunConfig, rng: random.Random) -> tuple[list[Agent], int]:
    occupied = occupancy_map(agents)
    open_cells = empty_cells(agents, config.grid_size)
    rng.shuffle(open_cells)
    updated: list[Agent] = []
    moves = 0

    for agent in rng.sample(agents, len(agents)):
        current = agent
        if not is_satisfied(agent, occupied, config.grid_size) and open_cells:
            new_row, new_col = open_cells.pop()
            open_cells.append((agent.row, agent.col))
            current = Agent(agent.agent_id, agent.group, new_row, new_col, agent.tolerance)
            occupied.pop((agent.row, agent.col), None)
            occupied[(new_row, new_col)] = current
            moves += 1
        updated.append(current)

    updated.sort(key=lambda a: a.agent_id)
    return updated, moves


def run_simulation(config: RunConfig) -> tuple[list[dict[str, object]], dict[str, object]]:
    rng = random.Random(config.seed + 10000)
    agents = build_initial_agents(config)
    rows: list[dict[str, object]] = []
    last_moves = 0

    for step in range(config.steps + 1):
        rows.append({
            "seed": config.seed,
            "step": step,
            "grid_size": config.grid_size,
            "agents": len(agents),
            "tolerance": config.tolerance,
            "satisfaction_rate": round(satisfaction_rate(agents, config.grid_size), 6),
            "clustering_score": round(clustering_score(agents, config.grid_size), 6),
            "moves": last_moves,
            "interpretation": "Local satisfaction and movement rules can generate emergent clustering over repeated steps."
        })
        if step < config.steps:
            agents, last_moves = step_agents(agents, config, rng)

    final = rows[-1]
    summary = {
        "seed": config.seed,
        "grid_size": config.grid_size,
        "agents": len(agents),
        "tolerance": config.tolerance,
        "steps": config.steps,
        "final_satisfaction_rate": final["satisfaction_rate"],
        "final_clustering_score": final["clustering_score"],
        "interpretation": "Emergent pattern depends on local rules, stochastic update order, empty space, tolerance, and initial arrangement."
    }
    return rows, summary


def ensemble_study() -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    all_time_rows: list[dict[str, object]] = []
    run_summaries: list[dict[str, object]] = []

    for tolerance in [0.25, 0.35, 0.45, 0.55]:
        for seed in range(1, 16):
            config = RunConfig(24, 210, tolerance, 0.20, 40, seed)
            time_rows, summary = run_simulation(config)
            all_time_rows.extend(time_rows)
            run_summaries.append(summary)

    ensemble_rows: list[dict[str, object]] = []
    for tolerance in sorted({row["tolerance"] for row in run_summaries}):
        subset = [row for row in run_summaries if row["tolerance"] == tolerance]
        sat = [float(row["final_satisfaction_rate"]) for row in subset]
        cluster = [float(row["final_clustering_score"]) for row in subset]
        ensemble_rows.append({
            "tolerance": tolerance,
            "runs": len(subset),
            "mean_final_satisfaction_rate": round(mean(sat), 6),
            "std_final_satisfaction_rate": round(pstdev(sat), 6),
            "mean_final_clustering_score": round(mean(cluster), 6),
            "std_final_clustering_score": round(pstdev(cluster), 6),
            "interpretation": "Repeated-seed ensembles show how emergent patterns vary across stochastic initial conditions."
        })
    return all_time_rows, run_summaries, ensemble_rows


def review_checklist() -> list[dict[str, object]]:
    return [
        {"check": "agent_definition_documented", "status": "complete", "question": "Are agents, attributes, and boundaries defined clearly?"},
        {"check": "behavioral_rules_justified", "status": "complete", "question": "Are agent rules tied to theory, evidence, or explicit modeling purpose?"},
        {"check": "environment_structure_documented", "status": "complete", "question": "Is the grid, network, space, or institution described?"},
        {"check": "interaction_rules_reviewed", "status": "complete", "question": "Are neighborhoods, contacts, links, or exchange rules explicit?"},
        {"check": "stochasticity_and_seeds_recorded", "status": "complete", "question": "Are random seeds, sample size, and repeated runs documented?"},
        {"check": "sensitivity_analysis_performed", "status": "complete", "question": "Are key parameters varied and compared?"},
        {"check": "validation_evidence_linked", "status": "partial", "question": "Are outputs compared with observed patterns, theory, benchmarks, or expert expectations?"},
        {"check": "representation_limits_stated", "status": "complete", "question": "Are limits of agent simplification and emergent interpretation communicated?"}
    ]


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = sorted({k for row in rows for k in row})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def main() -> None:
    time_rows, run_summaries, ensemble_rows = ensemble_study()
    checklist = review_checklist()
    best_cluster = max(run_summaries, key=lambda row: float(row["final_clustering_score"]))
    summary = {
        "simulation_runs": len(run_summaries),
        "tolerance_levels": len(ensemble_rows),
        "highest_observed_clustering_seed": best_cluster["seed"],
        "highest_observed_clustering_tolerance": best_cluster["tolerance"],
        "highest_observed_clustering_score": best_cluster["final_clustering_score"],
        "review_items_needing_attention": sum(1 for row in checklist if row["status"] != "complete"),
        "interpretation": "Agent-based emergence should be reviewed through local rules, environment structure, repeated seeds, parameter sweeps, validation evidence, and representation limits."
    }

    write_csv(TABLES / "agent_based_time_series.csv", time_rows)
    write_csv(TABLES / "agent_based_run_summaries.csv", run_summaries)
    write_csv(TABLES / "agent_based_ensemble_summary.csv", ensemble_rows)
    write_csv(TABLES / "agent_based_review_checklist.csv", checklist)
    write_csv(TABLES / "agent_based_emergence_audit_summary.csv", [summary])

    write_json(JSON_DIR / "agent_based_time_series.json", time_rows)
    write_json(JSON_DIR / "agent_based_run_summaries.json", run_summaries)
    write_json(JSON_DIR / "agent_based_ensemble_summary.json", ensemble_rows)
    write_json(JSON_DIR / "agent_based_review_checklist.json", checklist)
    write_json(JSON_DIR / "agent_based_emergence_audit_summary.json", summary)

    print("Agent-based algorithms and emergent behavior audit complete.")
    print(TABLES / "agent_based_emergence_audit_summary.csv")


if __name__ == "__main__":
    main()
