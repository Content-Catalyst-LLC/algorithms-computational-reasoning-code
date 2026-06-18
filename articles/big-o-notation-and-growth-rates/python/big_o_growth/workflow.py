from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json, math
from statistics import mean

@dataclass(frozen=True)
class BigOClaim:
    claim_name: str
    system_context: str
    claimed_growth: str
    input_definition_clarity: float
    resource_scope_clarity: float
    case_assumption_clarity: float
    derivation_quality: float
    tightness_clarity: float
    benchmark_support: float
    threshold_reporting: float
    hidden_cost_review: float
    governance_readiness: float
    communication_clarity: float

WEIGHTS=[0.12,0.10,0.10,0.12,0.10,0.12,0.10,0.08,0.08,0.08]

def clamp(x: float) -> float: return max(0.0, min(100.0, x))

def claim_quality(claim: BigOClaim) -> float:
    vals=[claim.input_definition_clarity,claim.resource_scope_clarity,claim.case_assumption_clarity,claim.derivation_quality,claim.tightness_clarity,claim.benchmark_support,claim.threshold_reporting,claim.hidden_cost_review,claim.governance_readiness,claim.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def claim_risk(claim: BigOClaim) -> float:
    vals=[claim.input_definition_clarity,claim.resource_scope_clarity,claim.case_assumption_clarity,claim.derivation_quality,claim.tightness_clarity,claim.benchmark_support,claim.threshold_reporting,claim.hidden_cost_review,claim.governance_readiness,claim.communication_clarity]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong Big-O claim discipline"
    if q >= 70 and r <= 35: return "usable Big-O claim with documentation or benchmark needs"
    if r >= 55: return "high risk; Big-O claim may be unclear or unsupported"
    return "partial Big-O discipline"

def load_claims(path: Path) -> list[BigOClaim]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [BigOClaim(r["claim_name"],r["system_context"],r["claimed_growth"],float(r["input_definition_clarity"]),float(r["resource_scope_clarity"]),float(r["case_assumption_clarity"]),float(r["derivation_quality"]),float(r["tightness_clarity"]),float(r["benchmark_support"]),float(r["threshold_reporting"]),float(r["hidden_cost_review"]),float(r["governance_readiness"]),float(r["communication_clarity"])) for r in rows]

def cost(n: int, growth: str):
    if growth == "constant": return 1.0
    if growth == "log": return math.log2(max(n,2))
    if growth == "linear": return float(n)
    if growth == "n_log_n": return n*math.log2(max(n,2))
    if growth == "quadratic": return float(n*n)
    if growth == "cubic": return float(n*n*n)
    if growth == "exponential": return float(2**n) if n <= 30 else "too_large"
    if growth == "factorial": return float(math.factorial(n)) if n <= 12 else "too_large"
    raise ValueError(growth)

def growth_table(values: list[int]) -> list[dict[str, object]]:
    return [{"n":n,"constant":cost(n,"constant"),"log2_n":round(float(cost(n,"log")),3),"linear":cost(n,"linear"),"n_log2_n":round(float(cost(n,"n_log_n")),3),"quadratic":cost(n,"quadratic"),"cubic":cost(n,"cubic"),"exponential":cost(n,"exponential"),"factorial":cost(n,"factorial")} for n in values]

def estimate_threshold(budget: float, growth: str, max_n: int = 1_000_000) -> int:
    n=1
    while n < max_n:
        value=cost(n,growth)
        if value == "too_large" or float(value) > budget:
            return n-1
        n += 1
    return max_n

def evaluate(claims: list[BigOClaim]) -> list[dict[str, object]]:
    out=[]
    for c in claims:
        q,r=claim_quality(c),claim_risk(c)
        out.append({**asdict(c),"big_o_claim_quality":round(q,3),"big_o_claim_risk":round(r,3),"diagnostic":diagnose(q,r)})
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
    audit=evaluate(load_claims(root/"data"/"synthetic_big_o_claims.csv"))
    growth=growth_table([5,10,20,30,50,100,1000])
    thresholds=[{"growth":g,"budget":1_000_000,"largest_n_under_budget":estimate_threshold(1_000_000,g)} for g in ["linear","n_log_n","quadratic","cubic","exponential","factorial"]]
    summary={"case_count":len(audit),"average_big_o_claim_quality":round(mean(float(r["big_o_claim_quality"]) for r in audit),3),"average_big_o_claim_risk":round(mean(float(r["big_o_claim_risk"]) for r in audit),3),"highest_quality_claim":max(audit,key=lambda r:float(r["big_o_claim_quality"]))["claim_name"],"highest_risk_claim":max(audit,key=lambda r:float(r["big_o_claim_risk"]))["claim_name"]}
    write_csv(root/"outputs"/"tables"/"big_o_claim_audit.csv", audit)
    write_csv(root/"outputs"/"tables"/"big_o_claim_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"growth_rate_table.csv", growth)
    write_csv(root/"outputs"/"tables"/"growth_rate_thresholds.csv", thresholds)
    write_json(root/"outputs"/"json"/"big_o_claim_audit.json", audit)
    write_json(root/"outputs"/"json"/"big_o_claim_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"growth_rate_table.json", growth)
    write_json(root/"outputs"/"json"/"growth_rate_thresholds.json", thresholds)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
