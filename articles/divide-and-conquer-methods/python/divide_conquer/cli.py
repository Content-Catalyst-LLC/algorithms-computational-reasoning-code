from pathlib import Path
import json
from divide_conquer.workflow import run_workflow
from divide_conquer.examples import binary_search, merge_sort, quicksort

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "merge_sort": merge_sort([9,3,5,1,4]),
        "quicksort": quicksort([9,3,5,1,4,3]),
        "binary_search": binary_search([1,3,4,5,9], 5)
    }
    (root/"outputs"/"json"/"divide_conquer_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Divide-and-conquer workflow complete.")
