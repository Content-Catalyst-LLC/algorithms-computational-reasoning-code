from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from collections import defaultdict, deque
from statistics import mean
import csv, json, math

@dataclass(frozen=True)
class PipelineCase:
    case_name: str
    system_context: str
    workflow_goal: str
    source_control: float
    input_contracts: float
    validation_coverage: float
    transformation_discipline: float
    dependency_clarity: float
    orchestration_quality: float
    idempotence: float
    provenance_support: float
    monitoring_observability: float
    governance_gates: float
    reproducibility: float
    communication_clarity: float

WEIGHTS=[0.09,0.09,0.11,0.09,0.08,0.08,0.08,0.10,0.10,0.07,0.06,0.05]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def pipeline_reliability_score(case: PipelineCase) -> float:
    vals=[case.source_control,case.input_contracts,case.validation_coverage,case.transformation_discipline,case.dependency_clarity,case.orchestration_quality,case.idempotence,case.provenance_support,case.monitoring_observability,case.governance_gates,case.reproducibility,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def pipeline_risk(case: PipelineCase) -> float:
    vals=[case.source_control,case.input_contracts,case.validation_coverage,case.transformation_discipline,case.idempotence,case.provenance_support,case.monitoring_observability,case.governance_gates,case.reproducibility]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong pipeline and workflow design discipline"
    if score >= 70 and risk <= 35:
        return "usable pipeline with review needs"
    if risk >= 55:
        return "high risk; pipeline may propagate silent failures, stale data, weak validation, or poor lineage"
    return "partial discipline; strengthen contracts, validation, idempotence, provenance, monitoring, and governance"

def load_cases(path: Path) -> list[PipelineCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [
            PipelineCase(
                r["case_name"], r["system_context"], r["workflow_goal"],
                float(r["source_control"]), float(r["input_contracts"]),
                float(r["validation_coverage"]), float(r["transformation_discipline"]),
                float(r["dependency_clarity"]), float(r["orchestration_quality"]),
                float(r["idempotence"]), float(r["provenance_support"]),
                float(r["monitoring_observability"]), float(r["governance_gates"]),
                float(r["reproducibility"]), float(r["communication_clarity"])
            ) for r in rows
        ]

def freshness_score(days_since_update: int, decay: float = 0.025) -> float:
    return round(math.exp(-decay * days_since_update), 4)

def validation_pass_rate(passed_checks: int, total_checks: int) -> float:
    return round(passed_checks / total_checks, 4) if total_checks else 0.0

def pipeline_quality_calculator(validation: float, freshness: float, completeness: float, lineage: float, monitoring: float) -> dict[str, float | str]:
    score=100*(0.25*validation+0.18*freshness+0.20*completeness+0.22*lineage+0.15*monitoring)
    return {"validation":validation,"freshness":freshness,"completeness":completeness,"lineage":lineage,"monitoring":monitoring,"pipeline_quality_score":round(score,3),"diagnostic":"strong pipeline quality evidence" if score >= 84 else "review validation, freshness, completeness, lineage, and monitoring"}

def load_tasks(path: Path) -> list[dict[str,str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def topological_order(tasks: list[dict[str,str]]) -> list[str]:
    deps={t["task_id"]: [d.strip() for d in t["depends_on"].split("|") if d.strip()] for t in tasks}
    children: dict[str, list[str]] = defaultdict(list)
    indegree={tid: len(ds) for tid, ds in deps.items()}
    for tid, ds in deps.items():
        for dep in ds:
            children[dep].append(tid)
    queue=deque(sorted([tid for tid, deg in indegree.items() if deg == 0]))
    order=[]
    while queue:
        node=queue.popleft()
        order.append(node)
        for child in sorted(children.get(node, [])):
            indegree[child]-=1
            if indegree[child] == 0:
                queue.append(child)
    return order

def validation_examples(path: Path) -> list[dict[str,object]]:
    rows=[]
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rate=validation_pass_rate(int(row["passed"]), int(row["total"]))
            rows.append({**row, "pass_rate": rate, "meets_threshold": rate >= float(row["threshold"])})
    return rows

def evaluate(cases: list[PipelineCase]) -> list[dict[str,object]]:
    out=[]
    for c in cases:
        score=pipeline_reliability_score(c)
        risk=pipeline_risk(c)
        out.append({**asdict(c), "pipeline_reliability_score":round(score,3), "pipeline_risk":round(risk,3), "diagnostic":diagnose(score,risk)})
    return out

def quality_examples() -> list[dict[str,object]]:
    return [
        pipeline_quality_calculator(.92,.86,.90,.88,.82),
        pipeline_quality_calculator(.42,.38,.50,.28,.30),
        {"example":"freshness_3_days","freshness_score":freshness_score(3)},
        {"example":"freshness_60_days","freshness_score":freshness_score(60)},
        {"example":"validation_pass_rate","validation_pass_rate":validation_pass_rate(18,20)}
    ]

def write_csv(path: Path, rows: list[dict[str,object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    audit=evaluate(load_cases(root/"data"/"synthetic_pipeline_cases.csv"))
    tasks=load_tasks(root/"data"/"synthetic_pipeline_tasks.csv")
    val=validation_examples(root/"data"/"synthetic_pipeline_quality_checks.csv")
    summary={
        "case_count": len(audit),
        "average_pipeline_reliability_score": round(mean(float(r["pipeline_reliability_score"]) for r in audit),3),
        "average_pipeline_risk": round(mean(float(r["pipeline_risk"]) for r in audit),3),
        "highest_score_case": max(audit, key=lambda r: float(r["pipeline_reliability_score"]))["case_name"],
        "highest_risk_case": max(audit, key=lambda r: float(r["pipeline_risk"]))["case_name"],
    }
    topo=[{"execution_order": i+1, "task_id": tid} for i, tid in enumerate(topological_order(tasks))]
    write_csv(root/"outputs"/"tables"/"pipeline_reliability_audit.csv", audit)
    write_csv(root/"outputs"/"tables"/"pipeline_reliability_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"pipeline_quality_examples.csv", quality_examples())
    write_csv(root/"outputs"/"tables"/"pipeline_validation_examples.csv", val)
    write_csv(root/"outputs"/"tables"/"workflow_topological_order.csv", topo)
    write_json(root/"outputs"/"json"/"pipeline_reliability_audit.json", audit)
    write_json(root/"outputs"/"json"/"pipeline_reliability_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"pipeline_quality_examples.json", quality_examples())
    write_json(root/"outputs"/"json"/"pipeline_validation_examples.json", val)
    write_json(root/"outputs"/"json"/"workflow_topological_order.json", topo)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
