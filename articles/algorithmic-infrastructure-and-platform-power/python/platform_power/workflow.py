from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv, json

@dataclass(frozen=True)
class PlatformPowerCase:
    case_name: str
    platform_context: str
    dependency_goal: str
    access_dependence: float
    visibility_dependence: float
    api_dependence: float
    data_dependence: float
    cost_dependence: float
    switching_difficulty: float
    interoperability: float
    transparency: float
    auditability: float
    appeal_mechanism: float
    governance_review: float
    communication_clarity: float

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def platform_power_risk(case: PlatformPowerCase) -> float:
    return clamp(100.0 * (
        0.11*case.access_dependence +
        0.11*case.visibility_dependence +
        0.10*case.api_dependence +
        0.10*case.data_dependence +
        0.09*case.cost_dependence +
        0.11*case.switching_difficulty +
        0.10*(1.0-case.interoperability) +
        0.09*(1.0-case.transparency) +
        0.08*(1.0-case.auditability) +
        0.06*(1.0-case.appeal_mechanism) +
        0.04*(1.0-case.governance_review) +
        0.01*(1.0-case.communication_clarity)
    ))

def platform_accountability_score(case: PlatformPowerCase) -> float:
    return clamp(100.0 * (
        0.18*case.interoperability +
        0.18*case.transparency +
        0.17*case.auditability +
        0.14*case.appeal_mechanism +
        0.17*case.governance_review +
        0.16*case.communication_clarity
    ))

def diagnose(risk: float, accountability: float) -> str:
    if risk >= 70 and accountability <= 45:
        return "high platform power risk with weak accountability"
    if risk >= 55:
        return "substantial platform dependency; strengthen portability, transparency, audit, appeals, and governance"
    if accountability >= 75:
        return "stronger accountability posture, but dependency should still be monitored"
    return "moderate platform risk; improve evidence, interoperability, and participant communication"

def dependency_score(access: float, visibility: float, cost: float, switching: float, evidence: float) -> float:
    return round(100.0 * (0.22*access + 0.22*visibility + 0.18*cost + 0.24*switching + 0.14*evidence), 3)

def switching_cost(migration: float, rebuild: float, training: float, downtime: float, lost_network: float) -> float:
    return round(migration + rebuild + training + downtime + lost_network, 3)

def api_dependency_ratio(platform_requests: float, total_requests: float) -> float:
    return round(platform_requests / total_requests, 6) if total_requests else 0.0

def visibility_share(actor_exposure: float, total_exposure: float) -> float:
    return round(actor_exposure / total_exposure, 6) if total_exposure else 0.0

def load_cases(path: Path) -> list[PlatformPowerCase]:
    fields=["access_dependence","visibility_dependence","api_dependence","data_dependence","cost_dependence","switching_difficulty","interoperability","transparency","auditability","appeal_mechanism","governance_review","communication_clarity"]
    with path.open(newline="", encoding="utf-8") as f:
        return [PlatformPowerCase(r["case_name"],r["platform_context"],r["dependency_goal"],*[float(r[k]) for k in fields]) for r in csv.DictReader(f)]

def evaluate(cases: list[PlatformPowerCase]) -> list[dict[str,object]]:
    rows=[]
    for c in cases:
        risk=platform_power_risk(c)
        accountability=platform_accountability_score(c)
        rows.append({**asdict(c),"platform_power_risk":round(risk,3),"platform_accountability_score":round(accountability,3),"diagnostic":diagnose(risk,accountability)})
    return rows

def dependency_metrics_summary(path: Path) -> list[dict[str,object]]:
    rows=[]
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append({
                **r,
                "dependency_score": dependency_score(float(r["access_dependence"]),float(r["visibility_dependence"]),float(r["cost_dependence"]),float(r["switching_difficulty"]),float(r["evidence_dependence"])),
                "switching_cost": switching_cost(float(r["migration"]),float(r["rebuild"]),float(r["training"]),float(r["downtime"]),float(r["lost_network"])),
                "api_dependency_ratio": api_dependency_ratio(float(r["platform_requests"]),float(r["total_requests"])),
                "visibility_share": visibility_share(float(r["actor_exposure"]),float(r["total_exposure"]))
            })
    return rows

def calculator_examples() -> list[dict[str,object]]:
    return [
        {"example":"platform_dependency_score","access_dependence":0.80,"visibility_dependence":0.90,"cost_dependence":0.70,"switching_difficulty":0.85,"evidence_dependence":0.65,"dependency_score":dependency_score(0.80,0.90,0.70,0.85,0.65)},
        {"example":"switching_cost","migration":45000,"rebuild":120000,"training":18000,"downtime":24000,"lost_network":75000,"switching_cost":switching_cost(45000,120000,18000,24000,75000)},
        {"example":"api_dependency_ratio","platform_requests":850000,"total_requests":1000000,"api_dependency_ratio":api_dependency_ratio(850000,1000000)},
        {"example":"visibility_share","actor_exposure":250000,"total_exposure":5000000,"visibility_share":visibility_share(250000,5000000)}
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
    audit=evaluate(load_cases(root/"data"/"synthetic_platform_power_cases.csv"))
    metrics=dependency_metrics_summary(root/"data"/"synthetic_platform_dependency_metrics.csv")
    summary={
        "case_count":len(audit),
        "average_platform_power_risk":round(mean(float(r["platform_power_risk"]) for r in audit),3),
        "average_platform_accountability_score":round(mean(float(r["platform_accountability_score"]) for r in audit),3),
        "highest_risk_case":max(audit,key=lambda r:float(r["platform_power_risk"]))["case_name"],
        "highest_accountability_case":max(audit,key=lambda r:float(r["platform_accountability_score"]))["case_name"]
    }
    for name, rows in [
        ("platform_power_audit",audit),
        ("platform_power_audit_summary",[summary]),
        ("platform_dependency_metrics_summary",metrics),
        ("platform_power_calculator_examples",calculator_examples())
    ]:
        write_csv(root/"outputs"/"tables"/f"{name}.csv", rows)
        write_json(root/"outputs"/"json"/f"{name}.json", rows)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
