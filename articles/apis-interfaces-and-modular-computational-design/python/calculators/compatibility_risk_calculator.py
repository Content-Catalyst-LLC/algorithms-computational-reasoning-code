#!/usr/bin/env python3
import argparse, json
from pathlib import Path
def compute(removed_fields, changed_types, added_required_fields, undocumented_errors, consumers_known, migration_plan):
    risk = 20*removed_fields + 20*changed_types + 20*added_required_fields + 10*undocumented_errors
    mitigation = 15*consumers_known + 15*migration_plan
    score = max(0, min(100, risk - mitigation))
    return {"compatibility_risk_score":score,"interpretation":"Compatibility risk rises with breaking changes and falls when consumers are known and migrations are planned."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--removed-fields",type=int,default=0)
    p.add_argument("--changed-types",type=int,default=0)
    p.add_argument("--added-required-fields",type=int,default=0)
    p.add_argument("--undocumented-errors",type=int,default=1)
    p.add_argument("--consumers-known",type=int,default=1)
    p.add_argument("--migration-plan",type=int,default=1)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args(); result=compute(a.removed_fields,a.changed_types,a.added_required_fields,a.undocumented_errors,a.consumers_known,a.migration_plan)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"compatibility_risk_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
