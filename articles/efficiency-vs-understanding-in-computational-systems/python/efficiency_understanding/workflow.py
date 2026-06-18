from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class EfficiencyCase:
    case_name: str
    system_context: str
    efficiency_claim: str
    performance_gain: float
    memory_gain: float
    cost_gain: float
    energy_awareness: float
    readability: float
    debuggability: float
    explainability: float
    observability: float
    auditability: float
    reproducibility: float
    maintainability: float
    governance_readiness: float
    communication_clarity: float

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def efficiency_score(case: EfficiencyCase) -> float:
    return clamp(100.0 * (
        0.30 * case.performance_gain +
        0.25 * case.memory_gain +
        0.25 * case.cost_gain +
        0.20 * case.energy_awareness
    ))

def understanding_score(case: EfficiencyCase) -> float:
    return clamp(100.0 * (
        0.12 * case.readability +
        0.12 * case.debuggability +
        0.12 * case.explainability +
        0.12 * case.observability +
        0.12 * case.auditability +
        0.10 * case.reproducibility +
        0.12 * case.maintainability +
        0.10 * case.governance_readiness +
        0.08 * case.communication_clarity
    ))

def responsible_efficiency_score(case: EfficiencyCase) -> float:
    return clamp(0.50 * efficiency_score(case) + 0.50 * understanding_score(case))

def tradeoff_risk(case: EfficiencyCase) -> float:
    efficiency = efficiency_score(case)
    understanding = understanding_score(case)
    governance_gap = 100.0 - (100.0 * mean([
        case.auditability,
        case.governance_readiness,
        case.communication_clarity,
        case.reproducibility,
    ]))
    imbalance = max(efficiency - understanding, 0.0)
    return clamp(0.65 * imbalance + 0.35 * governance_gap)

def diagnose(responsible_score: float, risk: float) -> str:
    if responsible_score >= 84 and risk <= 20:
        return "strong responsible efficiency balance"
    if responsible_score >= 70 and risk <= 35:
        return "usable efficiency gain with understanding or governance review needs"
    if risk >= 55:
        return "high risk; efficiency gain may undermine understanding, auditability, or accountability"
    return "partial balance; strengthen interpretability, documentation, observability, and governance"

def load_cases(path: Path) -> list[EfficiencyCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [
            EfficiencyCase(
                r["case_name"], r["system_context"], r["efficiency_claim"],
                float(r["performance_gain"]), float(r["memory_gain"]),
                float(r["cost_gain"]), float(r["energy_awareness"]),
                float(r["readability"]), float(r["debuggability"]),
                float(r["explainability"]), float(r["observability"]),
                float(r["auditability"]), float(r["reproducibility"]),
                float(r["maintainability"]), float(r["governance_readiness"]),
                float(r["communication_clarity"])
            ) for r in rows
        ]

def efficiency_gain(baseline_cost: float, optimized_cost: float) -> dict[str, float]:
    gain=(baseline_cost-optimized_cost)/baseline_cost
    return {
        "baseline_cost": baseline_cost,
        "optimized_cost": optimized_cost,
        "absolute_savings": round(baseline_cost-optimized_cost, 6),
        "efficiency_gain": round(gain, 6),
        "efficiency_gain_percent": round(gain*100, 3)
    }

def understanding_composite(readability: float, debuggability: float, explainability: float, auditability: float, maintainability: float) -> dict[str, float]:
    score=0.20*readability + 0.20*debuggability + 0.20*explainability + 0.20*auditability + 0.20*maintainability
    return {
        "readability": readability,
        "debuggability": debuggability,
        "explainability": explainability,
        "auditability": auditability,
        "maintainability": maintainability,
        "understanding_score": round(score*100, 3)
    }

def evaluate(cases: list[EfficiencyCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        e=efficiency_score(c)
        u=understanding_score(c)
        r=responsible_efficiency_score(c)
        risk=tradeoff_risk(c)
        out.append({**asdict(c),"efficiency_score":round(e,3),"understanding_score":round(u,3),"responsible_efficiency_score":round(r,3),"tradeoff_risk":round(risk,3),"diagnostic":diagnose(r,risk)})
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
    rows=evaluate(load_cases(root/"data"/"synthetic_efficiency_understanding_cases.csv"))
    summary={
        "case_count": len(rows),
        "average_efficiency_score": round(mean(float(row["efficiency_score"]) for row in rows), 3),
        "average_understanding_score": round(mean(float(row["understanding_score"]) for row in rows), 3),
        "average_tradeoff_risk": round(mean(float(row["tradeoff_risk"]) for row in rows), 3),
        "highest_responsible_score_case": max(rows, key=lambda row: float(row["responsible_efficiency_score"]))["case_name"],
        "highest_tradeoff_risk_case": max(rows, key=lambda row: float(row["tradeoff_risk"]))["case_name"]
    }
    calc_examples=[
        efficiency_gain(100.0, 62.0),
        understanding_composite(0.82,0.78,0.74,0.80,0.84),
    ]
    write_csv(root/"outputs"/"tables"/"efficiency_understanding_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"efficiency_understanding_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"efficiency_understanding_audit.json", rows)
    write_json(root/"outputs"/"json"/"efficiency_understanding_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"efficiency_understanding_calculator_examples.json", calc_examples)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
