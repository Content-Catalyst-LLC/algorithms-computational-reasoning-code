from pathlib import Path
import json
from hashing_retrieval.workflow import run_workflow
from hashing_retrieval.examples import demo_retrieval

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    demo = demo_retrieval(root)
    (root / "outputs" / "json" / "retrieval_demo.json").write_text(json.dumps(demo, indent=2), encoding="utf-8")
    print("Hashing and retrieval audit workflow complete.")
    print("Retrieval demo:", demo)
