from pathlib import Path
import json
from control_flow.workflow import run_workflow
from control_flow.examples import bounded_retry_outcomes, iterative_sum, nondecreasing, recursive_factorial

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "iterative_sum":[iterative_sum([1,2,3]), iterative_sum([])],
        "recursive_factorial_5":recursive_factorial(5),
        "nondecreasing_valid":nondecreasing([1,2,2,4]),
        "nondecreasing_invalid":nondecreasing([1,4,2]),
        "bounded_retry_success":bounded_retry_outcomes(5,3),
        "bounded_retry_exhausted":bounded_retry_outcomes(3,None)
    }
    (root/"outputs"/"json"/"control_flow_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Iteration, recursion, and control-flow workflow complete.")
