from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class ArchitectureCase:
    case_name: str
    problem_context: str
    architecture_choice: str
    boundary_clarity: float
    modular_cohesion: float
    dependency_control: float
    interface_discipline: float
    state_ownership: float
    failure_containment: float
    scalability_readiness: float
    security_boundaries: float
    observability: float
    governance_readiness: float

WEIGHTS=[0.12,0.12,0.12,0.10,0.10,0.10,0.08,0.10,0.08,0.08]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def architecture_quality(case: ArchitectureCase) -> float:
    vals=[case.boundary_clarity,case.modular_cohesion,case.dependency_control,case.interface_discipline,case.state_ownership,case.failure_containment,case.scalability_readiness,case.security_boundaries,case.observability,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def architecture_risk(case: ArchitectureCase) -> float:
    vals=[case.boundary_clarity,case.modular_cohesion,case.dependency_control,case.interface_discipline,case.state_ownership,case.failure_containment,case.security_boundaries,case.observability]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong architecture discipline"
    if q >= 70 and r <= 35: return "usable architecture discipline with review needs"
    if r >= 55: return "high architecture risk"
    return "partial architecture discipline"

def load_cases(path: Path) -> list[ArchitectureCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [ArchitectureCase(r["case_name"],r["problem_context"],r["architecture_choice"],float(r["boundary_clarity"]),float(r["modular_cohesion"]),float(r["dependency_control"]),float(r["interface_discipline"]),float(r["state_ownership"]),float(r["failure_containment"]),float(r["scalability_readiness"]),float(r["security_boundaries"]),float(r["observability"]),float(r["governance_readiness"])) for r in rows]

def load_edges(path: Path) -> list[tuple[str,str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return [(r["source"], r["target"]) for r in csv.DictReader(f)]

def dependency_summary(edges: list[tuple[str,str]]) -> dict[str, object]:
    nodes=sorted({n for e in edges for n in e})
    outgoing={n:0 for n in nodes}; incoming={n:0 for n in nodes}
    for s,t in edges:
        outgoing[s]+=1; incoming[t]+=1
    possible=max(1,len(nodes)*(len(nodes)-1))
    return {
        "node_count":len(nodes),
        "edge_count":len(edges),
        "dependency_density":round(len(edges)/possible,4),
        "highest_outgoing_dependency":max(outgoing.items(), key=lambda x:x[1]),
        "highest_incoming_dependency":max(incoming.items(), key=lambda x:x[1]),
        "nodes":nodes
    }

def evaluate(cases: list[ArchitectureCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=architecture_quality(c),architecture_risk(c)
        out.append({**asdict(c),"architecture_quality":round(q,3),"architecture_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows=evaluate(load_cases(root/"data"/"synthetic_software_architecture_cases.csv"))
    graph=dependency_summary(load_edges(root/"data"/"synthetic_architecture_dependency_edges.csv"))
    summary={"case_count":len(rows),"average_architecture_quality":round(mean(float(r["architecture_quality"]) for r in rows),3),"average_architecture_risk":round(mean(float(r["architecture_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["architecture_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["architecture_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"software_architecture_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"software_architecture_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"software_architecture_audit.json", rows)
    write_json(root/"outputs"/"json"/"software_architecture_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"dependency_graph_summary.json", graph)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
