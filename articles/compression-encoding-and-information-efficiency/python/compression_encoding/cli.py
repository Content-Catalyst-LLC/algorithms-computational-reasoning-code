from pathlib import Path
import json
from compression_encoding.workflow import run_workflow
from compression_encoding.examples import demo_compression_encoding

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    demo = demo_compression_encoding(root)
    (root / "outputs" / "json" / "compression_encoding_demo.json").write_text(json.dumps(demo, indent=2), encoding="utf-8")
    print("Compression and encoding audit workflow complete.")
    print("Compression demo:", demo)
