from pathlib import Path
from pseudocode_translation.workflow import run_workflow

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
    print("Pseudocode translation audit workflow complete.")
