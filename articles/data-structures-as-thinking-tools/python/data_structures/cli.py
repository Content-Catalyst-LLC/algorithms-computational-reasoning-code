from pathlib import Path
import json
from data_structures.workflow import run_workflow
from data_structures.examples import demo_structures

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    demo = demo_structures()
    (root / "outputs" / "json" / "data_structure_demo.json").write_text(json.dumps(demo, indent=2), encoding="utf-8")
    print("Data structure reasoning audit workflow complete.")
    print("Data structure demo:", demo)
