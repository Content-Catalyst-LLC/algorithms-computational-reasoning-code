from pathlib import Path
import json
from sequence_structures.workflow import run_workflow
from sequence_structures.examples import demo_sequence_structures

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    demo = demo_sequence_structures()
    (root / "outputs" / "json" / "sequence_structure_demo.json").write_text(json.dumps(demo, indent=2), encoding="utf-8")
    print("Sequence structure audit workflow complete.")
    print("Sequence structure demo:", demo)
