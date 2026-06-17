from pathlib import Path
from debugging_reasoning.workflow import run_workflow

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
    print("Debugging reasoning audit workflow complete.")
