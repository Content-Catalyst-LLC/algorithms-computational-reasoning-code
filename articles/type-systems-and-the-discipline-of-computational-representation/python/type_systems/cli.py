from pathlib import Path
import json
from type_systems.workflow import run_workflow
from type_systems.examples import demo_type_validation

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    demo = demo_type_validation(root)
    (root / "outputs" / "json" / "type_validation_demo.json").write_text(json.dumps(demo, indent=2), encoding="utf-8")
    print("Type representation audit workflow complete.")
    print("Validation demo:", demo)
