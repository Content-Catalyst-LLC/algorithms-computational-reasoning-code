from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json, math
from statistics import mean

@dataclass(frozen=True)
class ScalabilityCase:
    case_name: str
    system_context: str
    dominant_growth: str
    input_definition_clarity: float
    time_complexity_clarity: float
    space_complexity_clarity: float
    benchmark_evidence: float
    bottleneck_identification: float
    threshold_reporting: float
    degradation_planning: float
    monitoring_readiness: float
    governance_readiness: float
    equity_under_scale_review: float

WEIGHTS=[0.12,0.12,0.10,0.12,0.10,0.10,0.08,0.08,0.10,0.08]

def clamp(x: float) -> float: return max(0.0, min(100.0, x))

def scalability_quality(case: ScalabilityCase) -> float:
    vals=[case.input_definition_clarity,case.time_complexity_clarity,case.space_complexity_clarity,case.benchmark_evidence,case.bottleneck_identification,case.threshold_reporting,case.degradation_planning,case.monitoring_readiness,case.governance_readiness,case.equity_under_scale_review]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def scalability_risk(case: ScalabilityCase) -> float:
    vals=[case.input_definition_clarity,case.time_complexity_clarity,case.space_complexity_clarity,case.benchmark_evidence,case.bottleneck_identification,case.threshold_reporting,case.degradation_planning,case.monitoring_readiness,case.governance_readiness,case.equity_under_scale_review]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong complexity and scalability discipline"
    if q >= 70 and r <= 35: return "usable scalability evidence with review needs"
    if r >= 55: return "high scalability risk"
    return "partial scalability discipline"

def load_cases(path: Path) -> list[ScalabilityCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [ScalabilityCase(r["case_name"],r["system_context"],r["dominant_growth"],float(r["input_definition_clarity"]),float(r["time_complexity_clarity"]),float(r["space_complexity_clarity"]),float(r["benchmark_evidence"]),float(r["bottleneck_identification"]),float(r["threshold_reporting"]),float(r["degradation_planning"]),float(r["monitoring_readiness"]),float(r["governance_readiness"]),float(r["equity_under_scale_review"])) for r in rows]

def growth_cost(n: int, growth: str) -> float:
    if growth == "constant": return 1.0
    if growth == "log": return math.log2(max(n,2))
    if growth == "linear": return float(n)
    if growth == "n_log_n": return n * math.log2(max(n,2))
    if growth == "quadratic": return float(n*n)
    if growth == "cubic": return float(n*n*n)
    if growth == "exponential": return float(2**n) if n < 64 else float("inf")
    raise ValueError(growth)

def estimate_threshold(budget: float, growth: str, max_n: int = 1_000_000) -> int:
    n=1
    while n < max_n:
        if growth_cost(n, growth) > budget: return n-1
        n += 1
    return max_n

def evaluate(cases: list[ScalabilityCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=scalability_quality(c),scalability_risk(c)
        out.append({**asdict(c),"scalability_quality":round(q,3),"scalability_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def growth_table(values: list[int]) -> list[dict[str, object]]:
    return [{"n":n,"log2_n":round(math.log2(max(n,2)),3),"n_value":n,"n_log2_n":round(n*math.log2(max(n,2)),3),"n_squared":n**2,"n_cubed":n**3,"two_to_n_capped":2**n if n <= 30 else "too_large_for_table"} for n in values]

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    audit=evaluate(load_cases(root/"data"/"synthetic_complexity_scalability_cases.csv"))
    growth=growth_table([10,20,30,50,100,1000,10000])
    thresholds=[{"growth":g,"budget":1_000_000,"largest_n_under_budget":estimate_threshold(1_000_000,g)} for g in ["linear","n_log_n","quadratic","cubic","exponential"]]
    summary={"case_count":len(audit),"average_scalability_quality":round(mean(float(r["scalability_quality"]) for r in audit),3),"average_scalability_risk":round(mean(float(r["scalability_risk"]) for r in audit),3),"highest_quality_case":max(audit,key=lambda r:float(r["scalability_quality"]))["case_name"],"highest_risk_case":max(audit,key=lambda r:float(r["scalability_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"complexity_scalability_audit.csv", audit)
    write_csv(root/"outputs"/"tables"/"complexity_scalability_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"growth_rate_table.csv", growth)
    write_csv(root/"outputs"/"tables"/"scalability_thresholds.csv", thresholds)
    write_json(root/"outputs"/"json"/"complexity_scalability_audit.json", audit)
    write_json(root/"outputs"/"json"/"complexity_scalability_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"growth_rate_table.json", growth)
    write_json(root/"outputs"/"json"/"scalability_thresholds.json", thresholds)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
