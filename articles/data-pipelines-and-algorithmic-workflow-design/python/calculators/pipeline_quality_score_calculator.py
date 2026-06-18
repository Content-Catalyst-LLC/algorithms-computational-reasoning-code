#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(validation: float, freshness: float, completeness: float, lineage: float, monitoring: float):
    score=100*(0.25*validation+0.18*freshness+0.20*completeness+0.22*lineage+0.15*monitoring)
    return {"validation":validation,"freshness":freshness,"completeness":completeness,"lineage":lineage,"monitoring":monitoring,"pipeline_quality_score":round(score,3),"diagnostic":"strong pipeline quality evidence" if score >= 84 else "review validation, freshness, completeness, lineage, and monitoring"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--validation",type=float,default=0.92)
    p.add_argument("--freshness",type=float,default=0.86)
    p.add_argument("--completeness",type=float,default=0.90)
    p.add_argument("--lineage",type=float,default=0.88)
    p.add_argument("--monitoring",type=float,default=0.82)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.validation,a.freshness,a.completeness,a.lineage,a.monitoring)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"pipeline_quality_score_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
