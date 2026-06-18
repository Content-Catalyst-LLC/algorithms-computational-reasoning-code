from pathlib import Path
import json
from search_sorting.workflow import run_workflow
from search_sorting.examples import bfs_reachable, binary_search, linear_search, merge_sort

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "linear_search": linear_search([4,8,15,16], 15),
        "binary_search": binary_search([4,8,15,16], 8),
        "merge_sort": merge_sort([9,3,5,1,4]),
        "bfs_reachable": bfs_reachable({"api":["domain","auth"],"domain":["storage"],"auth":[],"storage":[]}, "api")
    }
    (root/"outputs"/"json"/"search_sorting_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Search and sorting workflow complete.")
