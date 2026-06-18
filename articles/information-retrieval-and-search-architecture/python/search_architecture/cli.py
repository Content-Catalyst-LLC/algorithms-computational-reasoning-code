from pathlib import Path
import json
from search_architecture.workflow import run_workflow, precision_recall, search_architecture_calculator

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "precision_recall_sample": precision_recall({"doc_1","doc_4"}, ["doc_4","doc_2","doc_1"]),
        "search_architecture_core_sample": search_architecture_calculator(.88,.90,.84,.76,.74,.86)
    }
    (root/"outputs"/"json"/"search_architecture_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Search architecture workflow complete.")
