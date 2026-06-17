#!/usr/bin/env python3
import argparse, json
from pathlib import Path
def compute(mutable_sites, logged_mutations, shared_references, guarded_shared_references, side_effects, bounded_side_effects):
    ml=min(1,logged_mutations/max(1,mutable_sites))
    ac=min(1,guarded_shared_references/max(1,shared_references))
    ec=min(1,bounded_side_effects/max(1,side_effects))
    safety=round(100*(0.4*ml+0.3*ac+0.3*ec),2)
    return {"mutation_safety_score":safety,"mutation_risk_score":round(100-safety,2),"interpretation":"Mutation risk falls when mutations are logged, shared references are controlled, and side effects are bounded."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--mutable-sites",type=int,default=10); p.add_argument("--logged-mutations",type=int,default=8)
    p.add_argument("--shared-references",type=int,default=6); p.add_argument("--guarded-shared-references",type=int,default=5)
    p.add_argument("--side-effects",type=int,default=7); p.add_argument("--bounded-side-effects",type=int,default=6)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args(); result=compute(a.mutable_sites,a.logged_mutations,a.shared_references,a.guarded_shared_references,a.side_effects,a.bounded_side_effects)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"mutation_risk_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
