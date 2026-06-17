from pathlib import Path
import json
from representation_shape.workflow import run_workflow
from representation_shape.examples import demo_shapes

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    demo = demo_shapes()
    (root / "outputs" / "json" / "representation_shape_demo.json").write_text(json.dumps(demo, indent=2), encoding="utf-8")
    print("Representation audit workflow complete.")
    print("Representation shape demo:", demo)
