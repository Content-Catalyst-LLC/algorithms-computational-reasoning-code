from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class OnlineDecisionCase:
    case_name: str
    system_context: str
    online_decision: str
    information_at_decision_clarity: float
    arrival_model_clarity: float
    commitment_awareness: float
    threshold_transparency: float
    prediction_error_handling: float
    competitive_or_regret_evidence: float
    queue_and_capacity_awareness: float
    fairness_under_arrival_review: float
    fallback_readiness: float
    governance_readiness: float
    communication_clarity: float

WEIGHTS=[0.11,0.10,0.10,0.09,0.10,0.10,0.10,0.09,0.08,0.07,0.06]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def online_decision_quality(case: OnlineDecisionCase) -> float:
    vals=[
        case.information_at_decision_clarity, case.arrival_model_clarity,
        case.commitment_awareness, case.threshold_transparency,
        case.prediction_error_handling, case.competitive_or_regret_evidence,
        case.queue_and_capacity_awareness, case.fairness_under_arrival_review,
        case.fallback_readiness, case.governance_readiness, case.communication_clarity
    ]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def online_decision_risk(case: OnlineDecisionCase) -> float:
    vals=[
        case.information_at_decision_clarity, case.arrival_model_clarity,
        case.commitment_awareness, case.threshold_transparency,
        case.prediction_error_handling, case.competitive_or_regret_evidence,
        case.queue_and_capacity_awareness, case.fairness_under_arrival_review,
        case.fallback_readiness, case.governance_readiness, case.communication_clarity
    ]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20:
        return "strong online decision discipline"
    if q >= 70 and r <= 35:
        return "usable online decision process with review needs"
    if r >= 55:
        return "high risk; arrival decision may hide uncertainty, commitment, or fairness effects"
    return "partial online decision discipline"

def load_cases(path: Path) -> list[OnlineDecisionCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [
            OnlineDecisionCase(
                r["case_name"], r["system_context"], r["online_decision"],
                float(r["information_at_decision_clarity"]), float(r["arrival_model_clarity"]),
                float(r["commitment_awareness"]), float(r["threshold_transparency"]),
                float(r["prediction_error_handling"]), float(r["competitive_or_regret_evidence"]),
                float(r["queue_and_capacity_awareness"]), float(r["fairness_under_arrival_review"]),
                float(r["fallback_readiness"]), float(r["governance_readiness"]),
                float(r["communication_clarity"])
            ) for r in rows
        ]

def ski_rental_table(rent_cost: float, buy_cost: float, max_days: int) -> list[dict[str, object]]:
    rows=[]
    break_even_day=int(buy_cost // rent_cost)
    for days in range(1, max_days+1):
        rent_only=days*rent_cost
        buy_now=buy_cost
        threshold=min(days, break_even_day)*rent_cost
        if days > break_even_day:
            threshold += buy_cost
        offline=min(rent_only, buy_now)
        rows.append({
            "days":days,
            "rent_only_cost":round(rent_only,3),
            "buy_now_cost":round(buy_now,3),
            "threshold_strategy_cost":round(threshold,3),
            "offline_optimum_cost":round(offline,3),
            "threshold_to_offline_ratio":round(threshold/max(offline,1e-9),3)
        })
    return rows

def queue_pressure_table(arrival_rates: list[float], service_rate: float) -> list[dict[str, object]]:
    rows=[]
    for arrival_rate in arrival_rates:
        utilization=arrival_rate/service_rate
        rows.append({
            "arrival_rate": arrival_rate,
            "service_rate": service_rate,
            "utilization": round(utilization,3),
            "stable_under_simple_model": arrival_rate < service_rate,
            "interpretation": "stable" if arrival_rate < service_rate else "backlog risk"
        })
    return rows

def lru_cache_simulation(requests: list[str], capacity: int) -> dict[str, object]:
    cache=[]
    hits=0
    misses=0
    trace=[]
    for item in requests:
        if item in cache:
            hits += 1
            cache.remove(item)
            cache.append(item)
            outcome="hit"
        else:
            misses += 1
            if len(cache) >= capacity:
                cache.pop(0)
            cache.append(item)
            outcome="miss"
        trace.append({"request": item, "outcome": outcome, "cache": list(cache)})
    return {"capacity":capacity,"hits":hits,"misses":misses,"hit_rate":round(hits/max(len(requests),1),3),"trace":trace}

def evaluate(cases: list[OnlineDecisionCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=online_decision_quality(c),online_decision_risk(c)
        out.append({**asdict(c),"online_decision_quality":round(q,3),"online_decision_risk":round(r,3),"diagnostic":diagnose(q,r)})
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
    audit=evaluate(load_cases(root/"data"/"synthetic_online_decision_cases.csv"))
    ski=ski_rental_table(10.0, 50.0, 12)
    queue=queue_pressure_table([40,60,80,95,100,110], 100.0)
    cache=lru_cache_simulation(["A","B","C","A","D","B","E","A","B","C"], 3)
    summary={
        "case_count": len(audit),
        "average_online_decision_quality": round(mean(float(r["online_decision_quality"]) for r in audit), 3),
        "average_online_decision_risk": round(mean(float(r["online_decision_risk"]) for r in audit), 3),
        "highest_quality_case": max(audit, key=lambda r: float(r["online_decision_quality"]))["case_name"],
        "highest_risk_case": max(audit, key=lambda r: float(r["online_decision_risk"]))["case_name"]
    }
    write_csv(root/"outputs"/"tables"/"online_decision_audit.csv", audit)
    write_csv(root/"outputs"/"tables"/"online_decision_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"ski_rental_threshold_table.csv", ski)
    write_csv(root/"outputs"/"tables"/"queue_pressure_table.csv", queue)
    write_json(root/"outputs"/"json"/"online_decision_audit.json", audit)
    write_json(root/"outputs"/"json"/"online_decision_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"ski_rental_threshold_table.json", ski)
    write_json(root/"outputs"/"json"/"queue_pressure_table.json", queue)
    write_json(root/"outputs"/"json"/"lru_cache_demo.json", cache)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
