from pathlib import Path
import json
from space_complexity.workflow import run_workflow, graph_storage, memory_budget_table

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "graph_storage_1000_5000": graph_storage(1000,5000),
        "memory_budget_table": memory_budget_table()
    }
    (root/"outputs"/"json"/"space_complexity_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Space complexity workflow complete.")
