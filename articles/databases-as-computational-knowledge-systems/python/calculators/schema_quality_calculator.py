#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(fields_defined: float, keys_defined: float, constraints_defined: float, metadata_complete: float, lineage_documented: float):
    score=100*(0.22*fields_defined+0.20*keys_defined+0.20*constraints_defined+0.20*metadata_complete+0.18*lineage_documented)
    return {"schema_quality_score": round(score,3), "diagnostic": "strong schema quality" if score >= 84 else "review schema, keys, constraints, metadata, and lineage"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--fields-defined",type=float,default=0.90)
    p.add_argument("--keys-defined",type=float,default=0.85)
    p.add_argument("--constraints-defined",type=float,default=0.80)
    p.add_argument("--metadata-complete",type=float,default=0.88)
    p.add_argument("--lineage-documented",type=float,default=0.82)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.fields_defined,a.keys_defined,a.constraints_defined,a.metadata_complete,a.lineage_documented)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"schema_quality_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
