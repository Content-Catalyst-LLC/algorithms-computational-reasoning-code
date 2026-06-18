from pathlib import Path
import json
from randomized_algorithms.workflow import run_workflow
from randomized_algorithms.examples import amplification_failure_probability, monte_carlo_pi, randomized_quicksort, sample_mean_summary

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "randomized_quicksort": randomized_quicksort([9,3,7,1,4,8]),
        "monte_carlo_pi": monte_carlo_pi(5000),
        "amplification_failure_probability": amplification_failure_probability(0.1,5),
        "sample_mean_summary": sample_mean_summary([1,2,3,4,5,6,7,8,9],4,1000)
    }
    (root/"outputs"/"json"/"randomized_algorithm_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Randomized algorithm workflow complete.")
