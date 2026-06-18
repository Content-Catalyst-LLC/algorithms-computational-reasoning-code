#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from statistics import mean

def compute(metadata_quality: float, provenance_lineage: float, access_control: float, correction_workflow: float, retention_policy: float):
    risk=100*mean([1-metadata_quality,1-provenance_lineage,1-access_control,1-correction_workflow,1-retention_policy])
    return {"database_governance_risk": round(risk,3), "diagnostic": "manageable governance risk" if risk < 30 else "elevated governance risk; strengthen metadata, provenance, access, correction, and retention"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--metadata-quality",type=float,default=0.80)
    p.add_argument("--provenance-lineage",type=float,default=0.84)
    p.add_argument("--access-control",type=float,default=0.78)
    p.add_argument("--correction-workflow",type=float,default=0.76)
    p.add_argument("--retention-policy",type=float,default=0.82)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.metadata_quality,a.provenance_lineage,a.access_control,a.correction_workflow,a.retention_policy)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"database_governance_risk_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
