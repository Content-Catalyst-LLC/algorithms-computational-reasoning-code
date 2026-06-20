from pathlib import Path
import json
from constraint_satisfaction.workflow import run_workflow, feasible_assignments, assignment_feasible, violation_count

if __name__ == '__main__':
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    constraints=[{'kind':'not_equal','left':'A','right':'B'},{'kind':'not_equal','left':'B','right':'C'}]
    demos={
        'feasible_assignment_count':len(feasible_assignments(['A','B','C'],['red','blue'],constraints)),
        'candidate_is_feasible':assignment_feasible({'A':'red','B':'blue','C':'red'},constraints),
        'candidate_violation_count':violation_count({'A':'red','B':'red','C':'blue'},constraints)
    }
    (root/'outputs'/'json'/'constraint_satisfaction_example_demos.json').write_text(json.dumps(demos,indent=2),encoding='utf-8')
    print('Constraint satisfaction workflow complete.')
