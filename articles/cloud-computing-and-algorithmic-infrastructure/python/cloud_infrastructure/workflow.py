from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv, json

@dataclass(frozen=True)
class CloudInfrastructureCase:
    case_name: str
    system_context: str
    infrastructure_goal: str
    compute_design: float
    storage_governance: float
    network_design: float
    deployment_reproducibility: float
    observability: float
    identity_access_control: float
    cost_visibility: float
    scaling_policy: float
    resilience_design: float
    data_governance: float
    dependency_mapping: float
    communication_clarity: float

WEIGHTS=[0.09,0.09,0.08,0.10,0.11,0.11,0.08,0.08,0.10,0.08,0.05,0.03]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def cloud_infrastructure_score(case: CloudInfrastructureCase) -> float:
    vals=[case.compute_design,case.storage_governance,case.network_design,case.deployment_reproducibility,case.observability,case.identity_access_control,case.cost_visibility,case.scaling_policy,case.resilience_design,case.data_governance,case.dependency_mapping,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def cloud_infrastructure_risk(case: CloudInfrastructureCase) -> float:
    vals=[case.storage_governance,case.deployment_reproducibility,case.observability,case.identity_access_control,case.cost_visibility,case.scaling_policy,case.resilience_design,case.data_governance,case.dependency_mapping]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong cloud infrastructure discipline"
    if score >= 70 and risk <= 35:
        return "usable cloud infrastructure design with review needs"
    if risk >= 55:
        return "high risk; weak deployment, observability, identity, cost, resilience, data governance, or dependency mapping may undermine algorithmic infrastructure"
    return "partial discipline; strengthen reproducibility, observability, access control, cost governance, resilience, data governance, and dependency mapping"

def load_cases(path: Path) -> list[CloudInfrastructureCase]:
    fields=["compute_design","storage_governance","network_design","deployment_reproducibility","observability","identity_access_control","cost_visibility","scaling_policy","resilience_design","data_governance","dependency_mapping","communication_clarity"]
    with path.open(newline="", encoding="utf-8") as f:
        return [CloudInfrastructureCase(r["case_name"],r["system_context"],r["infrastructure_goal"],*[float(r[k]) for k in fields]) for r in csv.DictReader(f)]

def total_latency(compute_ms: float, storage_ms: float, network_ms: float, queue_ms: float, coordination_ms: float) -> float:
    return round(compute_ms + storage_ms + network_ms + queue_ms + coordination_ms, 3)

def nominal_capacity(node_count: int, capacity_per_node: float) -> float:
    return round(node_count * capacity_per_node, 3)

def unit_cost(compute_cost: float, storage_cost: float, network_cost: float, managed_service_cost: float, observability_cost: float, completed_work: float) -> float:
    total = compute_cost + storage_cost + network_cost + managed_service_cost + observability_cost
    return round(total / completed_work, 6) if completed_work else 0.0

def redundant_availability(availabilities: list[float]) -> float:
    failure_product=1.0
    for availability in availabilities:
        failure_product *= (1.0 - availability)
    return round(1.0 - failure_product, 8)

def infrastructure_risk_score(security_gap: float, cost_gap: float, observability_gap: float, governance_gap: float, dependency_gap: float) -> float:
    return round(100.0*(0.25*security_gap + 0.18*cost_gap + 0.22*observability_gap + 0.20*governance_gap + 0.15*dependency_gap), 3)

def evaluate(cases: list[CloudInfrastructureCase]) -> list[dict[str,object]]:
    rows=[]
    for c in cases:
        score=cloud_infrastructure_score(c)
        risk=cloud_infrastructure_risk(c)
        rows.append({**asdict(c),"cloud_infrastructure_score":round(score,3),"cloud_infrastructure_risk":round(risk,3),"diagnostic":diagnose(score,risk)})
    return rows

def cloud_cost_latency_summary(path: Path) -> list[dict[str,object]]:
    rows=[]
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            compute=float(r["compute_ms"])
            storage=float(r["storage_ms"])
            network=float(r["network_ms"])
            queue=float(r["queue_ms"])
            coordination=float(r["coordination_ms"])
            rows.append({
                **r,
                "total_latency_ms": total_latency(compute,storage,network,queue,coordination),
                "unit_cost": unit_cost(float(r["compute_cost"]),float(r["storage_cost"]),float(r["network_cost"]),float(r["managed_service_cost"]),float(r["observability_cost"]),float(r["completed_work"]))
            })
    return rows

def resource_summary(path: Path) -> list[dict[str,object]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def calculator_examples() -> list[dict[str,object]]:
    return [
        {"example":"cloud_response_latency_ms","compute_ms":80,"storage_ms":45,"network_ms":60,"queue_ms":25,"coordination_ms":15,"total_latency_ms":total_latency(80,45,60,25,15)},
        {"example":"nominal_capacity","node_count":12,"capacity_per_node":250,"total_nominal_capacity":nominal_capacity(12,250)},
        {"example":"unit_cost","compute_cost":120,"storage_cost":35,"network_cost":25,"managed_service_cost":90,"observability_cost":18,"completed_work":144000,"unit_cost":unit_cost(120,35,25,90,18,144000)},
        {"example":"redundant_availability","availability_a":0.99,"availability_b":0.985,"redundant_availability":redundant_availability([0.99,0.985])},
        {"example":"infrastructure_risk","security_gap":0.18,"cost_gap":0.24,"observability_gap":0.16,"governance_gap":0.22,"dependency_gap":0.20,"infrastructure_risk_score":infrastructure_risk_score(0.18,0.24,0.16,0.22,0.20)}
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
    audit=evaluate(load_cases(root/"data"/"synthetic_cloud_infrastructure_cases.csv"))
    cloud_cost=cloud_cost_latency_summary(root/"data"/"synthetic_cloud_latency_cost.csv")
    resources=resource_summary(root/"data"/"synthetic_cloud_resources.csv")
    summary={
        "case_count":len(audit),
        "average_cloud_infrastructure_score":round(mean(float(r["cloud_infrastructure_score"]) for r in audit),3),
        "average_cloud_infrastructure_risk":round(mean(float(r["cloud_infrastructure_risk"]) for r in audit),3),
        "highest_score_case":max(audit,key=lambda r:float(r["cloud_infrastructure_score"]))["case_name"],
        "highest_risk_case":max(audit,key=lambda r:float(r["cloud_infrastructure_risk"]))["case_name"]
    }
    for name, rows in [
        ("cloud_infrastructure_audit",audit),
        ("cloud_infrastructure_audit_summary",[summary]),
        ("cloud_latency_cost_summary",cloud_cost),
        ("cloud_resource_summary",resources),
        ("cloud_infrastructure_calculator_examples",calculator_examples())
    ]:
        write_csv(root/"outputs"/"tables"/f"{name}.csv", rows)
        write_json(root/"outputs"/"json"/f"{name}.json", rows)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
