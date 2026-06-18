from pathlib import Path
import json
from knowledge_graphs.workflow import run_workflow, graph_path_score, hybrid_score

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "graph_path_score": graph_path_score(3, .90, .92, .95),
        "hybrid_retrieval_score": hybrid_score(.82,.78,.88,.90)
    }
    (root/"outputs"/"json"/"knowledge_graph_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Knowledge graphs and semantic retrieval workflow complete.")
