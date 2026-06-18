from pathlib import Path
import json
from tractability_hardness.workflow import run_workflow, subset_count, permutation_count, feasibility_table

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={"subsets_30":subset_count(30),"permutations_12":permutation_count(12),"feasibility_budget_table":feasibility_table()}
    (root/"outputs"/"json"/"tractability_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Tractability workflow complete.")
