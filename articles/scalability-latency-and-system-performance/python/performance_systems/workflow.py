from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv, json

@dataclass(frozen=True)
class PerformanceCase:
    case_name: str
    system_context: str
    performance_goal: str
    throughput_headroom: float
    latency_decomposition: float
    tail_latency_visibility: float
    bottleneck_clarity: float
    queue_discipline: float
    caching_policy: float
    resource_efficiency: float
    observability: float
    failure_behavior: float
    cost_awareness: float
    governance_review: float
    communication_clarity: float

WEIGHTS=[0.09,0.10,0.11,0.10,0.09,0.07,0.08,0.11,0.09,0.06,0.06,0.04]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def performance_reliability_score(case: PerformanceCase) -> float:
    vals=[case.throughput_headroom,case.latency_decomposition,case.tail_latency_visibility,case.bottleneck_clarity,case.queue_discipline,case.caching_policy,case.resource_efficiency,case.observability,case.failure_behavior,case.cost_awareness,case.governance_review,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def performance_risk(case: PerformanceCase) -> float:
    vals=[case.throughput_headroom,case.latency_decomposition,case.tail_latency_visibility,case.bottleneck_clarity,case.queue_discipline,case.observability,case.failure_behavior,case.cost_awareness,case.governance_review]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong performance discipline"
    if score >= 70 and risk <= 35:
        return "usable performance design with review needs"
    if risk >= 55:
        return "high risk; latency, tail behavior, bottlenecks, queues, observability, or overload behavior may distort system claims"
    return "partial discipline; strengthen latency decomposition, tail metrics, bottleneck analysis, queue controls, observability, failure behavior, and governance"

def load_cases(path: Path) -> list[PerformanceCase]:
    fields=["throughput_headroom","latency_decomposition","tail_latency_visibility","bottleneck_clarity","queue_discipline","caching_policy","resource_efficiency","observability","failure_behavior","cost_awareness","governance_review","communication_clarity"]
    with path.open(newline="", encoding="utf-8") as f:
        return [PerformanceCase(r["case_name"],r["system_context"],r["performance_goal"],*[float(r[k]) for k in fields]) for r in csv.DictReader(f)]

def response_time(network_ms: float, queue_ms: float, compute_ms: float, storage_ms: float, coordination_ms: float) -> float:
    return round(network_ms + queue_ms + compute_ms + storage_ms + coordination_ms, 3)

def throughput(completed_work: float, time_seconds: float) -> float:
    return round(completed_work / time_seconds, 6) if time_seconds else 0.0

def utilization(arrival_rate: float, service_rate: float) -> float:
    return round(arrival_rate / service_rate, 6) if service_rate else 0.0

def little_law(arrival_rate: float, average_time_in_system: float) -> float:
    return round(arrival_rate * average_time_in_system, 6)

def amdahl_speedup(processors: int, serial_fraction: float) -> float:
    return round(1.0 / (serial_fraction + ((1.0 - serial_fraction) / processors)), 6) if processors else 0.0

def unit_cost(total_cost: float, completed_work: float) -> float:
    return round(total_cost / completed_work, 6) if completed_work else 0.0

def evaluate(cases: list[PerformanceCase]) -> list[dict[str,object]]:
    rows=[]
    for c in cases:
        score=performance_reliability_score(c)
        risk=performance_risk(c)
        rows.append({**asdict(c),"performance_reliability_score":round(score,3),"performance_risk":round(risk,3),"diagnostic":diagnose(score,risk)})
    return rows

def latency_summary(path: Path) -> list[dict[str,object]]:
    rows=[]
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            total=response_time(float(r["network_ms"]),float(r["queue_ms"]),float(r["compute_ms"]),float(r["storage_ms"]),float(r["coordination_ms"]))
            rows.append({**r,"response_time_ms":total})
    return rows

def throughput_summary(path: Path) -> list[dict[str,object]]:
    rows=[]
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            completed=float(r["completed_work"])
            seconds=float(r["time_seconds"])
            arrival=float(r["arrival_rate"])
            service=float(r["service_rate"])
            cost=float(r["total_cost"])
            rows.append({**r,"throughput":throughput(completed,seconds),"utilization":utilization(arrival,service),"unit_cost":unit_cost(cost,completed)})
    return rows

def calculator_examples() -> list[dict[str,object]]:
    return [
        {"example":"end_to_end_response_time_ms","network_ms":45,"queue_ms":20,"compute_ms":85,"storage_ms":35,"coordination_ms":15,"response_time_ms":response_time(45,20,85,35,15)},
        {"example":"throughput_requests_per_second","completed_work":12000,"time_seconds":60,"throughput":throughput(12000,60)},
        {"example":"utilization_queue_warning","arrival_rate":180,"service_rate":200,"utilization":utilization(180,200)},
        {"example":"little_law_queue_estimate","arrival_rate":180,"average_time_in_system":0.45,"average_items_in_system":little_law(180,0.45)},
        {"example":"amdahl_parallel_speedup","processors":8,"serial_fraction":0.12,"speedup":amdahl_speedup(8,0.12)},
        {"example":"unit_cost_per_request","total_cost":240,"completed_work":120000,"unit_cost":unit_cost(240,120000)}
    ]

def write_csv(path: Path, rows: list[dict[str,object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    audit=evaluate(load_cases(root/"data"/"synthetic_performance_cases.csv"))
    latency=latency_summary(root/"data"/"synthetic_latency_samples.csv")
    capacity=throughput_summary(root/"data"/"synthetic_throughput_capacity.csv")
    summary={
        "case_count":len(audit),
        "average_performance_reliability_score":round(mean(float(r["performance_reliability_score"]) for r in audit),3),
        "average_performance_risk":round(mean(float(r["performance_risk"]) for r in audit),3),
        "highest_score_case":max(audit,key=lambda r:float(r["performance_reliability_score"]))["case_name"],
        "highest_risk_case":max(audit,key=lambda r:float(r["performance_risk"]))["case_name"]
    }
    for name, rows in [
        ("scalability_latency_performance_audit",audit),
        ("scalability_latency_performance_audit_summary",[summary]),
        ("latency_response_time_summary",latency),
        ("throughput_capacity_summary",capacity),
        ("performance_calculator_examples",calculator_examples())
    ]:
        write_csv(root/"outputs"/"tables"/f"{name}.csv", rows)
        write_json(root/"outputs"/"json"/f"{name}.json", rows)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
