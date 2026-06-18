from pathlib import Path
import json
from dynamic_programming.workflow import run_workflow
from dynamic_programming.examples import edit_distance, fibonacci_memo, knapsack_01, state_space_size

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "fibonacci_memo_12": fibonacci_memo(12),
        "edit_distance_algorithm_algorithms": edit_distance("algorithm","algorithms"),
        "knapsack_value": knapsack_01([6,10,12],[1,2,3],5),
        "state_space_size": state_space_size([50,100,20])
    }
    (root/"outputs"/"json"/"dynamic_programming_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Dynamic programming workflow complete.")
