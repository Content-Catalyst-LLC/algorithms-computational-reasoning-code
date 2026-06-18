from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class ScaleCase:
    case_name: str
    system_context: str
    scale_claim: str
    decomposability: float
    partitioning_clarity: float
    communication_awareness: float
    synchronization_control: float
    load_balance_evidence: float
    data_locality_awareness: float
    fault_tolerance: float
    consistency_clarity: float
    benchmark_support: float
    cost_awareness: float
    governance_readiness: float
    communication_clarity: float

WEIGHTS=[0.10,0.09,0.10,0.08,0.09,0.08,0.10,0.08,0.10,0.07,0.06,0.05]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def scale_claim_quality(case: ScaleCase) -> float:
    vals=[
        case.decomposability, case.partitioning_clarity, case.communication_awareness,
        case.synchronization_control, case.load_balance_evidence, case.data_locality_awareness,
        case.fault_tolerance, case.consistency_clarity, case.benchmark_support,
        case.cost_awareness, case.governance_readiness, case.communication_clarity
    ]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def scale_claim_risk(case: ScaleCase) -> float:
    vals=[
        case.decomposability, case.partitioning_clarity, case.communication_awareness,
        case.synchronization_control, case.load_balance_evidence, case.data_locality_awareness,
        case.fault_tolerance, case.consistency_clarity, case.benchmark_support,
        case.cost_awareness, case.governance_readiness, case.communication_clarity
    ]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20:
        return "strong parallel and distributed scale discipline"
    if q >= 70 and r <= 35:
        return "usable scale claim with benchmark or resilience review needs"
    if r >= 55:
        return "high risk; scale claim may ignore overhead, failure, or governance"
    return "partial scale discipline"

def load_cases(path: Path) -> list[ScaleCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [
            ScaleCase(
                r["case_name"], r["system_context"], r["scale_claim"],
                float(r["decomposability"]), float(r["partitioning_clarity"]),
                float(r["communication_awareness"]), float(r["synchronization_control"]),
                float(r["load_balance_evidence"]), float(r["data_locality_awareness"]),
                float(r["fault_tolerance"]), float(r["consistency_clarity"]),
                float(r["benchmark_support"]), float(r["cost_awareness"]),
                float(r["governance_readiness"]), float(r["communication_clarity"])
            ) for r in rows
        ]

def speedup(serial_fraction: float, processors: int) -> float:
    return 1.0 / (serial_fraction + ((1.0 - serial_fraction) / processors))

def speedup_table(serial_fraction: float, processors: list[int]) -> list[dict[str, float]]:
    rows=[]
    for p in processors:
        s=speedup(serial_fraction, p)
        rows.append({"processors":p,"serial_fraction":serial_fraction,"amdahl_speedup_bound":round(s,4),"parallel_efficiency":round(s/p,4)})
    return rows

def capacity_table(service_rate_per_worker: float, workers: list[int], overhead_rate: float = 0.05) -> list[dict[str, float]]:
    rows=[]
    for p in workers:
        ideal=service_rate_per_worker*p
        overhead=ideal*overhead_rate*max(p-1,0)
        effective=max(ideal-overhead,0.0)
        rows.append({"workers":p,"ideal_capacity":round(ideal,3),"estimated_overhead":round(overhead,3),"effective_capacity":round(effective,3)})
    return rows

def evaluate(cases: list[ScaleCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=scale_claim_quality(c),scale_claim_risk(c)
        out.append({**asdict(c),"scale_claim_quality":round(q,3),"scale_claim_risk":round(r,3),"diagnostic":diagnose(q,r)})
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
    audit=evaluate(load_cases(root/"data"/"synthetic_parallelism_scale_cases.csv"))
    speedups=speedup_table(0.10, [1,2,4,8,16,32,64])
    capacity=capacity_table(100.0, [1,2,4,8,16,32])
    summary={
        "case_count": len(audit),
        "average_scale_claim_quality": round(mean(float(r["scale_claim_quality"]) for r in audit), 3),
        "average_scale_claim_risk": round(mean(float(r["scale_claim_risk"]) for r in audit), 3),
        "highest_quality_case": max(audit, key=lambda r: float(r["scale_claim_quality"]))["case_name"],
        "highest_risk_case": max(audit, key=lambda r: float(r["scale_claim_risk"]))["case_name"]
    }
    write_csv(root/"outputs"/"tables"/"parallelism_scale_audit.csv", audit)
    write_csv(root/"outputs"/"tables"/"parallelism_scale_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"amdahl_speedup_table.csv", speedups)
    write_csv(root/"outputs"/"tables"/"distributed_capacity_table.csv", capacity)
    write_json(root/"outputs"/"json"/"parallelism_scale_audit.json", audit)
    write_json(root/"outputs"/"json"/"parallelism_scale_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"amdahl_speedup_table.json", speedups)
    write_json(root/"outputs"/"json"/"distributed_capacity_table.json", capacity)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
