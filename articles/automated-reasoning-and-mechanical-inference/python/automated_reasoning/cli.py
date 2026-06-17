from pathlib import Path
from automated_reasoning.workflow import run_workflow

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
    print("Automated reasoning audit workflow complete.")
