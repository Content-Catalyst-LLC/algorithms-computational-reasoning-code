from pathlib import Path
import json
from execution_models.workflow import run_workflow
from execution_models.examples import demo_interpreter

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    demo = demo_interpreter(root)
    (root / "outputs" / "json" / "tiny_interpreter_demo.json").write_text(json.dumps(demo, indent=2), encoding="utf-8")
    print("Execution model audit workflow complete.")
    print("Tiny interpreter demo:", demo)
