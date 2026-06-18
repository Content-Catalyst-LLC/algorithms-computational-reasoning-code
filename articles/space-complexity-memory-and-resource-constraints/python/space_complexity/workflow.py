from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class SpaceComplexityCase:
    case_name: str
    system_context: str
    claimed_space: str
    input_space_clarity: float
    auxiliary_space_clarity: float
    output_space_clarity: float
    peak_memory_evidence: float
    data_structure_fit: float
    time_space_tradeoff_clarity: float
    io_and_data_movement_awareness: float
    streaming_or_external_memory_readiness: float
    failure_handling: float
    governance_readiness: float
    communication_clarity: float

WEIGHTS=[0.09,0.11,0.08,0.12,0.11,0.10,0.10,0.09,0.08,0.07,0.05]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def space_claim_quality(case: SpaceComplexityCase) -> float:
    vals=[
        case.input_space_clarity, case.auxiliary_space_clarity, case.output_space_clarity,
        case.peak_memory_evidence, case.data_structure_fit, case.time_space_tradeoff_clarity,
        case.io_and_data_movement_awareness, case.streaming_or_external_memory_readiness,
        case.failure_handling, case.governance_readiness, case.communication_clarity
    ]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def space_claim_risk(case: SpaceComplexityCase) -> float:
    vals=[
        case.input_space_clarity, case.auxiliary_space_clarity, case.output_space_clarity,
        case.peak_memory_evidence, case.data_structure_fit, case.time_space_tradeoff_clarity,
        case.io_and_data_movement_awareness, case.streaming_or_external_memory_readiness,
        case.failure_handling, case.governance_readiness, case.communication_clarity
    ]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20:
        return "strong space-complexity discipline"
    if q >= 70 and r <= 35:
        return "usable memory claim with documentation or benchmark needs"
    if r >= 55:
        return "high risk; memory or resource claim may be incomplete"
    return "partial space-complexity discipline"

def load_cases(path: Path) -> list[SpaceComplexityCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [
            SpaceComplexityCase(
                r["case_name"], r["system_context"], r["claimed_space"],
                float(r["input_space_clarity"]), float(r["auxiliary_space_clarity"]),
                float(r["output_space_clarity"]), float(r["peak_memory_evidence"]),
                float(r["data_structure_fit"]), float(r["time_space_tradeoff_clarity"]),
                float(r["io_and_data_movement_awareness"]),
                float(r["streaming_or_external_memory_readiness"]),
                float(r["failure_handling"]), float(r["governance_readiness"]),
                float(r["communication_clarity"])
            ) for r in rows
        ]

def graph_storage(vertices: int, edges: int) -> dict[str, object]:
    matrix=vertices*vertices
    adj_list=vertices+edges
    return {
        "vertices": vertices,
        "edges": edges,
        "adjacency_matrix_units": matrix,
        "adjacency_list_units": adj_list,
        "matrix_to_list_ratio": round(matrix/max(adj_list,1), 3)
    }

def graph_storage_table(values: list[tuple[int,int]]) -> list[dict[str, object]]:
    return [graph_storage(v,e) for v,e in values]

def memory_budget_table() -> list[dict[str, object]]:
    rows=[]
    for n in [100,1_000,10_000]:
        linear=n
        quadratic=n*n
        rows.append({
            "n": n,
            "linear_units": linear,
            "quadratic_units": quadratic,
            "fits_budget_1k_linear": linear <= 1_000,
            "fits_budget_10k_linear": linear <= 10_000,
            "fits_budget_1m_linear": linear <= 1_000_000,
            "fits_budget_1k_quadratic": quadratic <= 1_000,
            "fits_budget_10k_quadratic": quadratic <= 10_000,
            "fits_budget_1m_quadratic": quadratic <= 1_000_000,
        })
    return rows

def evaluate(cases: list[SpaceComplexityCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=space_claim_quality(c),space_claim_risk(c)
        out.append({**asdict(c),"space_claim_quality":round(q,3),"space_claim_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    audit=evaluate(load_cases(root/"data"/"synthetic_space_complexity_cases.csv"))
    graph=graph_storage_table([(100,300),(1000,5000),(10000,30000),(50000,200000)])
    budget=memory_budget_table()
    summary={
        "case_count": len(audit),
        "average_space_claim_quality": round(mean(float(r["space_claim_quality"]) for r in audit), 3),
        "average_space_claim_risk": round(mean(float(r["space_claim_risk"]) for r in audit), 3),
        "highest_quality_case": max(audit, key=lambda r: float(r["space_claim_quality"]))["case_name"],
        "highest_risk_case": max(audit, key=lambda r: float(r["space_claim_risk"]))["case_name"]
    }
    write_csv(root/"outputs"/"tables"/"space_complexity_audit.csv", audit)
    write_csv(root/"outputs"/"tables"/"space_complexity_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"graph_storage_comparison.csv", graph)
    write_csv(root/"outputs"/"tables"/"memory_budget_table.csv", budget)
    write_json(root/"outputs"/"json"/"space_complexity_audit.json", audit)
    write_json(root/"outputs"/"json"/"space_complexity_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"graph_storage_comparison.json", graph)
    write_json(root/"outputs"/"json"/"memory_budget_table.json", budget)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
