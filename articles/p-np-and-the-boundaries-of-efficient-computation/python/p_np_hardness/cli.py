from pathlib import Path
import json
from p_np_hardness.workflow import run_workflow, verify_sat_assignment, verify_graph_coloring

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "sat_certificate_valid": verify_sat_assignment([[1,-2],[2,3]], {1: True, 2: False, 3: True}),
        "graph_coloring_certificate_valid": verify_graph_coloring([(1,2),(2,3),(1,3)], {1: 1, 2: 2, 3: 3})
    }
    (root/"outputs"/"json"/"p_np_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("P, NP, and hardness workflow complete.")
