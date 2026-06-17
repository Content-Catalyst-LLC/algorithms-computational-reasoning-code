from pathlib import Path
import json
from graph_relationships.workflow import run_workflow
from graph_relationships.examples import demo_graph

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    demo = demo_graph()
    (root / "outputs" / "json" / "graph_traversal_demo.json").write_text(json.dumps(demo, indent=2), encoding="utf-8")
    print("Graph relationship audit workflow complete.")
    print("Graph traversal demo:", demo)
