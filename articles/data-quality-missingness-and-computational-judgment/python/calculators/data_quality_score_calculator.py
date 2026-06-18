#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(completeness: float, validity: float, timeliness: float, provenance: float, validation: float):
    score=100*(0.25*completeness+0.20*validity+0.15*timeliness+0.22*provenance+0.18*validation)
    return {"completeness":completeness,"validity":validity,"timeliness":timeliness,"provenance":provenance,"validation":validation,"data_quality_score":round(score,3),"diagnostic":"strong data-quality evidence" if score >= 84 else "review completeness, validity, timeliness, provenance, and validation"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--completeness",type=float,default=0.92)
    p.add_argument("--validity",type=float,default=0.88)
    p.add_argument("--timeliness",type=float,default=0.86)
    p.add_argument("--provenance",type=float,default=0.90)
    p.add_argument("--validation",type=float,default=0.89)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.completeness,a.validity,a.timeliness,a.provenance,a.validation)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"data_quality_score_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
