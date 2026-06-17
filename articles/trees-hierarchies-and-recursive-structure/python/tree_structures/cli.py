from pathlib import Path
import json
from tree_structures.workflow import run_workflow
from tree_structures.examples import demo_tree

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    demo = demo_tree()
    (root / "outputs" / "json" / "tree_traversal_demo.json").write_text(json.dumps(demo, indent=2), encoding="utf-8")
    print("Tree structure audit workflow complete.")
    print("Tree traversal demo:", demo)
