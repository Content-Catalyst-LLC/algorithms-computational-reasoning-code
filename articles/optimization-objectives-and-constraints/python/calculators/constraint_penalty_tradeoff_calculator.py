#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def constraint_margin(limit, observed_value):
    return limit - observed_value

def penalty_objective(base_objective, penalty, penalty_weight):
    return base_objective + penalty_weight * penalty

def normalized_tradeoff_score(cost_score, quality_score, risk_score):
    return (0.35*(1.0-cost_score)) + (0.40*quality_score) + (0.25*(1.0-risk_score))

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--limit",type=float,default=100.0)
    p.add_argument("--observed-value",type=float,default=86.5)
    p.add_argument("--base-objective",type=float,default=42.0)
    p.add_argument("--penalty",type=float,default=8.0)
    p.add_argument("--penalty-weight",type=float,default=2.5)
    p.add_argument("--cost-score",type=float,default=0.30)
    p.add_argument("--quality-score",type=float,default=0.82)
    p.add_argument("--risk-score",type=float,default=0.25)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result={
        "constraint_margin":round(constraint_margin(a.limit,a.observed_value),6),
        "penalty_objective":round(penalty_objective(a.base_objective,a.penalty,a.penalty_weight),6),
        "normalized_tradeoff_score":round(normalized_tradeoff_score(a.cost_score,a.quality_score,a.risk_score),6)
    }
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"constraint_penalty_tradeoff_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
