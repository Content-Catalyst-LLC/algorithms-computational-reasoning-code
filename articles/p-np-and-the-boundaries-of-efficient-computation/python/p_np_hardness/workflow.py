from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class ComplexityClassCase:
    case_name: str
    problem_context: str
    claimed_class: str
    problem_form_clarity: float
    input_definition_clarity: float
    certificate_clarity: float
    verifier_clarity: float
    reduction_evidence: float
    class_claim_evidence: float
    exact_method_feasibility: float
    approximation_readiness: float
    benchmark_support: float
    governance_readiness: float
    communication_clarity: float

WEIGHTS=[0.09,0.09,0.10,0.10,0.10,0.12,0.10,0.08,0.08,0.07,0.07]

def clamp(x: float) -> float: return max(0.0, min(100.0, x))

def claim_quality(case: ComplexityClassCase) -> float:
    vals=[case.problem_form_clarity,case.input_definition_clarity,case.certificate_clarity,case.verifier_clarity,case.reduction_evidence,case.class_claim_evidence,case.exact_method_feasibility,case.approximation_readiness,case.benchmark_support,case.governance_readiness,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def claim_risk(case: ComplexityClassCase) -> float:
    vals=[case.problem_form_clarity,case.input_definition_clarity,case.certificate_clarity,case.verifier_clarity,case.reduction_evidence,case.class_claim_evidence,case.exact_method_feasibility,case.approximation_readiness,case.benchmark_support,case.governance_readiness,case.communication_clarity]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong complexity-class claim discipline"
    if q >= 70 and r <= 35: return "usable class claim with review needs"
    if r >= 55: return "high risk; P/NP/hardness claim may be unclear or unsupported"
    return "partial claim discipline"

def load_cases(path: Path) -> list[ComplexityClassCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [ComplexityClassCase(r["case_name"],r["problem_context"],r["claimed_class"],float(r["problem_form_clarity"]),float(r["input_definition_clarity"]),float(r["certificate_clarity"]),float(r["verifier_clarity"]),float(r["reduction_evidence"]),float(r["class_claim_evidence"]),float(r["exact_method_feasibility"]),float(r["approximation_readiness"]),float(r["benchmark_support"]),float(r["governance_readiness"]),float(r["communication_clarity"])) for r in rows]

def verify_sat_assignment(clauses: list[list[int]], assignment: dict[int, bool]) -> bool:
    for clause in clauses:
        if not any((lit > 0 and assignment.get(abs(lit), False)) or (lit < 0 and not assignment.get(abs(lit), False)) for lit in clause):
            return False
    return True

def verify_graph_coloring(edges: list[tuple[int, int]], coloring: dict[int, int]) -> bool:
    return all(coloring.get(u) != coloring.get(v) for u, v in edges)

def evaluate(cases: list[ComplexityClassCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=claim_quality(c),claim_risk(c)
        out.append({**asdict(c),"complexity_class_claim_quality":round(q,3),"complexity_class_claim_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def class_reference_table() -> list[dict[str, object]]:
    return [
        {"class_or_label":"P","meaning":"Decision problems solvable in polynomial time.","practical_note":"Often treated as efficiently solvable in theory."},
        {"class_or_label":"NP","meaning":"Decision problems whose yes answers have polynomial-time verifiers.","practical_note":"Verification can be easier than discovery."},
        {"class_or_label":"NP-hard","meaning":"At least as hard as every problem in NP.","practical_note":"May not itself be in NP or even be a decision problem."},
        {"class_or_label":"NP-complete","meaning":"Both in NP and NP-hard.","practical_note":"Efficient solution to one NP-complete problem would imply P = NP."},
    ]

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    audit=evaluate(load_cases(root/"data"/"synthetic_p_np_hardness_cases.csv"))
    reference=class_reference_table()
    summary={"case_count":len(audit),"average_complexity_class_claim_quality":round(mean(float(r["complexity_class_claim_quality"]) for r in audit),3),"average_complexity_class_claim_risk":round(mean(float(r["complexity_class_claim_risk"]) for r in audit),3),"highest_quality_case":max(audit,key=lambda r:float(r["complexity_class_claim_quality"]))["case_name"],"highest_risk_case":max(audit,key=lambda r:float(r["complexity_class_claim_risk"]))["case_name"]}
    verification_demo={"sat_assignment_valid":verify_sat_assignment([[1,-2],[2,3]],{1:True,2:False,3:True}),"coloring_valid":verify_graph_coloring([(1,2),(2,3)],{1:1,2:2,3:1})}
    write_csv(root/"outputs"/"tables"/"p_np_hardness_audit.csv", audit)
    write_csv(root/"outputs"/"tables"/"p_np_hardness_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"complexity_class_reference.csv", reference)
    write_json(root/"outputs"/"json"/"p_np_hardness_audit.json", audit)
    write_json(root/"outputs"/"json"/"p_np_hardness_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"complexity_class_reference.json", reference)
    write_json(root/"outputs"/"json"/"verification_demo.json", verification_demo)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
