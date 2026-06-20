from pathlib import Path
import json
from optimization_audit.workflow import run_workflow, linear_objective, constraint_margin, penalty_objective, normalized_tradeoff_score

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "linear_objective":linear_objective([4.0,2.0,1.5],[10.0,20.0,5.0]),
        "constraint_margin":constraint_margin(100.0,86.5),
        "penalty_objective":penalty_objective(42.0,8.0,2.5),
        "normalized_tradeoff_score":normalized_tradeoff_score(0.30,0.82,0.25)
    }
    (root/"outputs"/"json"/"optimization_example_demos.json").write_text(json.dumps(demos,indent=2),encoding="utf-8")
    print("Optimization, objectives, and constraints workflow complete.")
