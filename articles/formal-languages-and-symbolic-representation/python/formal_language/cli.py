from pathlib import Path
from formal_language.workflow import run_workflow

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
    print("Formal language audit workflow complete.")
