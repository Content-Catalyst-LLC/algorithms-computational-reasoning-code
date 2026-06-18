#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def score(problem_form, certificate, verifier, reduction, class_evidence, communication):
    vals=[problem_form, certificate, verifier, reduction, class_evidence, communication]
    quality=100*sum(vals)/len(vals)
    risk=100*(1-sum(vals)/len(vals))
    return round(quality,3), round(risk,3)

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--problem-form",type=float,default=0.9)
    p.add_argument("--certificate",type=float,default=0.9)
    p.add_argument("--verifier",type=float,default=0.9)
    p.add_argument("--reduction",type=float,default=0.8)
    p.add_argument("--class-evidence",type=float,default=0.85)
    p.add_argument("--communication",type=float,default=0.8)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    quality,risk=score(a.problem_form,a.certificate,a.verifier,a.reduction,a.class_evidence,a.communication)
    result={"complexity_class_claim_quality":quality,"complexity_class_claim_risk":risk,"interpretation":"Higher quality requires precise problem form, certificate, verifier, reduction evidence, class evidence, and communication."}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"complexity_class_claim_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
