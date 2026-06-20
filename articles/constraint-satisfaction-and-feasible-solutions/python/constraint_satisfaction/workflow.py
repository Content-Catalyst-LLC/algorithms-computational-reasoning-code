from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv, itertools, json

@dataclass(frozen=True)
class ConstraintCase:
    case_name: str
    problem_context: str
    feasibility_goal: str
    variable_clarity: float
    domain_clarity: float
    constraint_documentation: float
    feasibility_logic: float
    inconsistency_handling: float
    pruning_transparency: float
    propagation_transparency: float
    traceability: float
    exception_handling: float
    governance_review: float
    fairness_review: float
    communication_clarity: float

WEIGHTS=[0.10,0.10,0.12,0.11,0.09,0.08,0.08,0.09,0.07,0.06,0.07,0.03]

def constraint_system_score(case: ConstraintCase) -> float:
    vals=[case.variable_clarity,case.domain_clarity,case.constraint_documentation,case.feasibility_logic,case.inconsistency_handling,case.pruning_transparency,case.propagation_transparency,case.traceability,case.exception_handling,case.governance_review,case.fairness_review,case.communication_clarity]
    return max(0.0, min(100.0, 100.0*sum(v*w for v,w in zip(vals,WEIGHTS))))

def constraint_system_risk(case: ConstraintCase) -> float:
    vals=[case.variable_clarity,case.domain_clarity,case.constraint_documentation,case.feasibility_logic,case.inconsistency_handling,case.pruning_transparency,case.propagation_transparency,case.traceability,case.exception_handling,case.governance_review,case.fairness_review]
    return max(0.0, min(100.0, 100.0*mean(1.0-v for v in vals)))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong constraint-satisfaction discipline"
    if score >= 70 and risk <= 35:
        return "usable constraint system with review needs"
    if risk >= 55:
        return "high risk; variables, domains, constraints, feasibility logic, inconsistency handling, traceability, or governance may be underdefined"
    return "partial discipline; strengthen variables, domains, constraints, feasibility checks, propagation, traces, exceptions, fairness, and governance"

def parse_constraints(text: str) -> list[dict[str,str]]:
    rules=[]
    for item in (text or '').split('|'):
        parts=item.split(':')
        if len(parts)==3:
            rules.append({'kind':parts[0], 'left':parts[1], 'right':parts[2]})
    return rules

def parse_assignment(text: str) -> dict[str,str]:
    out={}
    for item in (text or '').split(';'):
        if '=' in item:
            k,v=item.split('=',1)
            out[k.strip()]=v.strip()
    return out

def violation_count(assignment: dict[str,str], constraints: list[dict[str,str]]) -> int:
    violations=0
    for rule in constraints:
        left,right=rule['left'],rule['right']
        if left not in assignment or right not in assignment:
            continue
        if rule['kind']=='not_equal' and assignment[left] == assignment[right]:
            violations += 1
        elif rule['kind']=='equal' and assignment[left] != assignment[right]:
            violations += 1
    return violations

def assignment_feasible(assignment: dict[str,str], constraints: list[dict[str,str]]) -> bool:
    return violation_count(assignment, constraints) == 0

def feasible_assignments(variables: list[str], domain_values: list[str], constraints: list[dict[str,str]]) -> list[dict[str,str]]:
    results=[]
    for values in itertools.product(domain_values, repeat=len(variables)):
        assignment=dict(zip(variables, values))
        if assignment_feasible(assignment, constraints):
            results.append(assignment)
    return results

def load_cases(path: Path) -> list[ConstraintCase]:
    fields=['variable_clarity','domain_clarity','constraint_documentation','feasibility_logic','inconsistency_handling','pruning_transparency','propagation_transparency','traceability','exception_handling','governance_review','fairness_review','communication_clarity']
    with path.open(newline='', encoding='utf-8') as f:
        return [ConstraintCase(r['case_name'],r['problem_context'],r['feasibility_goal'],*[float(r[k]) for k in fields]) for r in csv.DictReader(f)]

def evaluate(cases: list[ConstraintCase]) -> list[dict[str,object]]:
    rows=[]
    for c in cases:
        score=constraint_system_score(c)
        risk=constraint_system_risk(c)
        rows.append({**asdict(c),'constraint_system_score':round(score,3),'constraint_system_risk':round(risk,3),'diagnostic':diagnose(score,risk)})
    return rows

def calculator_input_summary(path: Path) -> list[dict[str,object]]:
    rows=[]
    with path.open(newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            variables=[x.strip() for x in r['variables'].split(';') if x.strip()]
            domain_values=[x.strip() for x in r['domain_values'].split(';') if x.strip()]
            constraints=parse_constraints(r['constraints'])
            assignment=parse_assignment(r['candidate_assignment'])
            feasible=feasible_assignments(variables, domain_values, constraints)
            rows.append({**r,'variable_count':len(variables),'domain_size':len(domain_values),'constraint_count':len(constraints),'feasible_assignment_count':len(feasible),'candidate_is_feasible':assignment_feasible(assignment,constraints),'candidate_violation_count':violation_count(assignment,constraints)})
    return rows

def write_csv(path: Path, rows: list[dict[str,object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding='utf-8')

def run_workflow(root: Path) -> None:
    audit=evaluate(load_cases(root/'data'/'synthetic_constraint_cases.csv'))
    calc_summary=calculator_input_summary(root/'data'/'synthetic_constraint_calculator_inputs.csv')
    summary={'case_count':len(audit),'average_constraint_system_score':round(mean(float(r['constraint_system_score']) for r in audit),3),'average_constraint_system_risk':round(mean(float(r['constraint_system_risk']) for r in audit),3),'highest_score_case':max(audit,key=lambda r:float(r['constraint_system_score']))['case_name'],'highest_risk_case':max(audit,key=lambda r:float(r['constraint_system_risk']))['case_name']}
    for name, rows in [('constraint_satisfaction_audit',audit),('constraint_satisfaction_audit_summary',[summary]),('constraint_satisfaction_calculator_input_summary',calc_summary)]:
        write_csv(root/'outputs'/'tables'/f'{name}.csv', rows)
        write_json(root/'outputs'/'json'/f'{name}.json', rows)

if __name__ == '__main__':
    run_workflow(Path(__file__).resolve().parents[2])
