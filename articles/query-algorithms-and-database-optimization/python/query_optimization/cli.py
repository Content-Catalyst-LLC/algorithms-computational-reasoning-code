from pathlib import Path
from query_optimization.workflow import run_workflow
if __name__ == '__main__':
    run_workflow(Path(__file__).resolve().parents[2])
    print('Query optimization workflow complete.')
