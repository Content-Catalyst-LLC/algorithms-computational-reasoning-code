#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(dependency, shared_state, synchronization, idempotence, observability, failure_isolation):
    risk=100*(0.18*(1-dependency)+0.20*(1-shared_state)+0.17*(1-synchronization)+0.15*(1-idempotence)+0.15*(1-observability)+0.15*(1-failure_isolation))
    return {"dependency_discipline":dependency,"shared_state_control":shared_state,"synchronization_design":synchronization,"idempotence":idempotence,"observability":observability,"failure_isolation":failure_isolation,"concurrency_risk_score":round(risk,3),"diagnostic":"low concurrency risk" if risk <= 25 else "review race, deadlock, idempotence, observability, and failure-isolation controls"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--dependency",type=float,default=0.84)
    p.add_argument("--shared-state",type=float,default=0.82)
    p.add_argument("--synchronization",type=float,default=0.80)
    p.add_argument("--idempotence",type=float,default=0.84)
    p.add_argument("--observability",type=float,default=0.82)
    p.add_argument("--failure-isolation",type=float,default=0.84)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.dependency,a.shared_state,a.synchronization,a.idempotence,a.observability,a.failure_isolation)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"concurrency_risk_score_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
