#!/usr/bin/env python3
import argparse, json
from pathlib import Path
def compute(component_count, dependency_count, shared_state_count, undocumented_dependency_count, ownerless_component_count):
    possible=max(1, component_count*(component_count-1))
    density=dependency_count/possible
    risk=min(100, round(100*(0.35*density + 0.25*shared_state_count/max(1,component_count) + 0.25*undocumented_dependency_count/max(1,dependency_count) + 0.15*ownerless_component_count/max(1,component_count)),2))
    return {"dependency_density":round(density,4),"dependency_risk_score":risk,"interpretation":"Dependency risk rises with dense dependency graphs, shared state, undocumented dependencies, and ownerless components."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--component-count",type=int,default=10)
    p.add_argument("--dependency-count",type=int,default=14)
    p.add_argument("--shared-state-count",type=int,default=2)
    p.add_argument("--undocumented-dependency-count",type=int,default=3)
    p.add_argument("--ownerless-component-count",type=int,default=1)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args(); result=compute(a.component_count,a.dependency_count,a.shared_state_count,a.undocumented_dependency_count,a.ownerless_component_count)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"dependency_risk_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
