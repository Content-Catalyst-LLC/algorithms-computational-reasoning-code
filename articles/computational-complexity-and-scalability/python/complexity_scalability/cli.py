from pathlib import Path
import json, math
from complexity_scalability.workflow import run_workflow, estimate_threshold, growth_cost

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "growth_at_1000":{"linear":growth_cost(1000,"linear"),"n_log_n":growth_cost(1000,"n_log_n"),"quadratic":growth_cost(1000,"quadratic")},
        "quadratic_threshold_for_one_million": estimate_threshold(1_000_000,"quadratic"),
        "multi_resource_cost_at_10000": 10000*math.log2(10000) + 0.1*10000 + 0.05*1000 + 2*math.sqrt(10000)
    }
    (root/"outputs"/"json"/"complexity_scalability_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Complexity and scalability workflow complete.")
