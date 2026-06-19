#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def dependency_score(access, visibility, cost, switching, evidence):
    return 100.0*(0.22*access + 0.22*visibility + 0.18*cost + 0.24*switching + 0.14*evidence)

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--access",type=float,default=0.80)
    p.add_argument("--visibility",type=float,default=0.90)
    p.add_argument("--cost",type=float,default=0.70)
    p.add_argument("--switching",type=float,default=0.85)
    p.add_argument("--evidence",type=float,default=0.65)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result={"access_dependence":a.access,"visibility_dependence":a.visibility,"cost_dependence":a.cost,"switching_difficulty":a.switching,"evidence_dependence":a.evidence,"dependency_score":round(dependency_score(a.access,a.visibility,a.cost,a.switching,a.evidence),3)}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"platform_dependency_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
