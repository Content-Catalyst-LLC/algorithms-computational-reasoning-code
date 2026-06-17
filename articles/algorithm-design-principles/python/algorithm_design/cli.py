from pathlib import Path
import json
from algorithm_design.workflow import run_workflow
from algorithm_design.examples import binary_search, sorted_invariant, validate_nonnegative_weights, simple_complexity_estimate

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "sorted_invariant_valid": sorted_invariant([1,2,2,3]),
        "sorted_invariant_invalid": sorted_invariant([1,3,2]),
        "binary_search_found_index": binary_search([1,3,5,8], 5),
        "nonnegative_weights_valid": validate_nonnegative_weights([("a","b",1.0),("b","c",2.0)]),
        "complexity_estimates": [simple_complexity_estimate(100, s) for s in ["linear","nlogn","quadratic"]]
    }
    (root/"outputs"/"json"/"algorithm_design_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Algorithm design workflow complete.")
