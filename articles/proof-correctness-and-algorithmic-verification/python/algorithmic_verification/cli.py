from pathlib import Path
from algorithmic_verification.workflow import run_workflow

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
    print("Algorithmic verification audit workflow complete.")
