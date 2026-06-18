#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from statistics import mean

def compute(key_quality: float, cardinality_documented: float, duplicate_checks: float, missingness_policy: float, provenance_linked: float):
    risk=100*mean([1-key_quality,1-cardinality_documented,1-duplicate_checks,1-missingness_policy,1-provenance_linked])
    return {"join_risk": round(risk,3), "diagnostic": "manageable join risk" if risk < 30 else "elevated join risk; review keys, cardinality, duplicates, missingness, and provenance"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--key-quality",type=float,default=0.84)
    p.add_argument("--cardinality-documented",type=float,default=0.80)
    p.add_argument("--duplicate-checks",type=float,default=0.78)
    p.add_argument("--missingness-policy",type=float,default=0.82)
    p.add_argument("--provenance-linked",type=float,default=0.84)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.key_quality,a.cardinality_documented,a.duplicate_checks,a.missingness_policy,a.provenance_linked)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"join_risk_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
