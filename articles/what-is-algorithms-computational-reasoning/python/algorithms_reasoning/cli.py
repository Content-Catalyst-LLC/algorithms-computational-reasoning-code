from pathlib import Path
from algorithms_reasoning.diagnostics import run_workflow

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
    print("Algorithmic reasoning diagnostics complete.")
