from pathlib import Path
import json
from search_spaces.workflow import run_workflow, branching_state_count, path_cost, heuristic_score, coverage_ratio, pruning_ratio
if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={"branching_state_count":branching_state_count(3,5),"path_cost":path_cost([2.5,3.0,1.25,4.75]),"heuristic_score":heuristic_score(8.0,5.5),"coverage_ratio":coverage_ratio(850,5000),"pruning_ratio":pruning_ratio(1200,4200)}
    (root/"outputs"/"json"/"search_space_example_demos.json").write_text(json.dumps(demos,indent=2),encoding="utf-8")
    print("Search spaces and computational exploration workflow complete.")
