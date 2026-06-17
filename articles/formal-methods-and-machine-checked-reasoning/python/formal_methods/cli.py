from pathlib import Path
import json
from formal_methods.workflow import run_workflow
from formal_methods.proof_obligation_examples import verified_sort_demo

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    demo = verified_sort_demo([3, 1, 2])
    (root / "outputs" / "json" / "proof_obligation_demo.json").write_text(json.dumps(demo, indent=2), encoding="utf-8")
    print("Formal methods audit workflow complete.")
    print("Proof obligation demo:", demo)
