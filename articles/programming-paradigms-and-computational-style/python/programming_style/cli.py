from pathlib import Path
import json
from programming_style.workflow import run_workflow
from programming_style.examples import demo_styles

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    demo = demo_styles(root)
    (root / "outputs" / "json" / "programming_style_demo.json").write_text(json.dumps(demo, indent=2), encoding="utf-8")
    print("Programming paradigm and computational style audit workflow complete.")
    print("Style demo:", demo)
