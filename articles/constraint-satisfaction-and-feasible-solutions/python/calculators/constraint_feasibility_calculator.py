#!/usr/bin/env python3
import argparse, itertools, json
from pathlib import Path

def parse_constraints(text):
    rules=[]
    for item in text.split('|'):
        parts=item.split(':')
        if len(parts)==3:
            rules.append({'kind':parts[0], 'left':parts[1], 'right':parts[2]})
    return rules

def parse_assignment(text):
    out={}
    for item in text.split(';'):
        if '=' in item:
            k,v=item.split('=',1); out[k.strip()]=v.strip()
    return out

def violation_count(assignment, constraints):
    total=0
    for rule in constraints:
        left,right=rule['left'],rule['right']
        if left not in assignment or right not in assignment: continue
        if rule['kind']=='not_equal' and assignment[left]==assignment[right]: total += 1
        if rule['kind']=='equal' and assignment[left]!=assignment[right]: total += 1
    return total

def feasible_assignments(variables, domain_values, constraints):
    count=0
    for values in itertools.product(domain_values, repeat=len(variables)):
        assignment=dict(zip(variables, values))
        if violation_count(assignment, constraints)==0: count += 1
    return count

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--variables', default='A,B,C')
    p.add_argument('--domain-values', default='red,blue')
    p.add_argument('--constraints', default='not_equal:A:B|not_equal:B:C')
    p.add_argument('--candidate-assignment', default='A=red;B=blue;C=red')
    p.add_argument('--output-dir', type=Path, default=Path('outputs/json'))
    a=p.parse_args()
    variables=[x.strip() for x in a.variables.split(',') if x.strip()]
    domain_values=[x.strip() for x in a.domain_values.split(',') if x.strip()]
    constraints=parse_constraints(a.constraints)
    candidate=parse_assignment(a.candidate_assignment)
    result={'variables':variables,'domain_values':domain_values,'constraint_count':len(constraints),'feasible_assignment_count':feasible_assignments(variables,domain_values,constraints),'candidate_assignment':candidate,'candidate_violation_count':violation_count(candidate,constraints),'candidate_is_feasible':violation_count(candidate,constraints)==0}
    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir/'constraint_feasibility_calculator.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
