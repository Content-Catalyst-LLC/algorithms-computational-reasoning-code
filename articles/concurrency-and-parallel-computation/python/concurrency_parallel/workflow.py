from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from collections import defaultdict, deque
import csv, json

@dataclass(frozen=True)
class ConcurrencyCase:
    case_name: str
    system_context: str
    computational_goal: str
    decomposition_clarity: float
    dependency_discipline: float
    shared_state_control: float
    synchronization_design: float
    idempotence: float
    deadlock_avoidance: float
    load_balancing: float
    observability: float
    failure_isolation: float
    reproducibility: float
    governance_review: float
    communication_clarity: float

WEIGHTS=[0.09,0.10,0.11,0.09,0.09,0.08,0.08,0.10,0.09,0.07,0.06,0.04]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def concurrency_reliability_score(case: ConcurrencyCase) -> float:
    vals=[case.decomposition_clarity,case.dependency_discipline,case.shared_state_control,case.synchronization_design,case.idempotence,case.deadlock_avoidance,case.load_balancing,case.observability,case.failure_isolation,case.reproducibility,case.governance_review,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def concurrency_risk(case: ConcurrencyCase) -> float:
    vals=[case.dependency_discipline,case.shared_state_control,case.synchronization_design,case.idempotence,case.deadlock_avoidance,case.observability,case.failure_isolation,case.reproducibility,case.governance_review]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong concurrency and parallel-computation discipline"
    if score >= 70 and risk <= 35:
        return "usable concurrent design with review needs"
    if risk >= 55:
        return "high risk; race conditions, deadlocks, weak state control, or poor observability may distort computation"
    return "partial discipline; strengthen dependencies, shared-state control, synchronization, idempotence, observability, and failure isolation"

def load_cases(path: Path) -> list[ConcurrencyCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [ConcurrencyCase(r["case_name"], r["system_context"], r["computational_goal"], float(r["decomposition_clarity"]), float(r["dependency_discipline"]), float(r["shared_state_control"]), float(r["synchronization_design"]), float(r["idempotence"]), float(r["deadlock_avoidance"]), float(r["load_balancing"]), float(r["observability"]), float(r["failure_isolation"]), float(r["reproducibility"]), float(r["governance_review"]), float(r["communication_clarity"])) for r in rows]

def speedup(sequential_time: float, parallel_time: float) -> float:
    return round(sequential_time / parallel_time, 4) if parallel_time else 0.0

def amdahl_speedup(processors: int, sequential_fraction: float) -> float:
    return round(1.0 / (sequential_fraction + ((1.0 - sequential_fraction) / processors)), 4) if processors else 0.0

def parallel_efficiency(processors: int, observed_speedup: float) -> float:
    return round(observed_speedup / processors, 4) if processors else 0.0

def concurrency_risk_score(dependency: float, shared_state: float, synchronization: float, idempotence: float, observability: float, failure_isolation: float) -> dict[str, float | str]:
    risk=100*(0.18*(1-dependency)+0.20*(1-shared_state)+0.17*(1-synchronization)+0.15*(1-idempotence)+0.15*(1-observability)+0.15*(1-failure_isolation))
    return {"dependency_discipline":dependency,"shared_state_control":shared_state,"synchronization_design":synchronization,"idempotence":idempotence,"observability":observability,"failure_isolation":failure_isolation,"concurrency_risk_score":round(risk,3),"diagnostic":"low concurrency risk" if risk <= 25 else "review race, deadlock, idempotence, observability, and failure-isolation controls"}

def load_task_graph(path: Path) -> list[dict[str,str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def topological_order(tasks: list[dict[str,str]]) -> list[str]:
    deps={t["task_id"]:[d.strip() for d in t["depends_on"].split("|") if d.strip()] for t in tasks}
    children: dict[str, list[str]] = defaultdict(list)
    indegree={tid:len(ds) for tid, ds in deps.items()}
    for tid, ds in deps.items():
        for d in ds:
            children[d].append(tid)
    queue=deque(sorted([tid for tid, deg in indegree.items() if deg == 0]))
    order=[]
    while queue:
        n=queue.popleft(); order.append(n)
        for child in sorted(children.get(n, [])):
            indegree[child]-=1
            if indegree[child] == 0:
                queue.append(child)
    return order

def performance_examples(path: Path) -> list[dict[str, object]]:
    out=[]
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            p=int(row["processors"]); s=float(row["sequential_fraction"]); t1=float(row["sequential_time"]); tp=float(row["parallel_time"])
            obs=speedup(t1,tp); amd=amdahl_speedup(p,s)
            out.append({**row,"observed_speedup":obs,"observed_efficiency":parallel_efficiency(p,obs),"amdahl_speedup":amd,"amdahl_efficiency":parallel_efficiency(p,amd)})
    return out

def evaluate(cases: list[ConcurrencyCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        score=concurrency_reliability_score(c); risk=concurrency_risk(c)
        out.append({**asdict(c), "concurrency_reliability_score":round(score,3), "concurrency_risk":round(risk,3), "diagnostic":diagnose(score,risk)})
    return out

def calculator_examples() -> list[dict[str, object]]:
    return [
        {"example":"observed_speedup_120_to_28","speedup":speedup(120,28),"parallel_efficiency_8_workers":parallel_efficiency(8,speedup(120,28))},
        {"example":"amdahl_8_workers_s_0_12","amdahl_speedup":amdahl_speedup(8,.12),"parallel_efficiency":parallel_efficiency(8,amdahl_speedup(8,.12))},
        concurrency_risk_score(.84,.82,.80,.84,.82,.84),
        concurrency_risk_score(.42,.24,.22,.26,.28,.30),
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
    audit=evaluate(load_cases(root/"data"/"synthetic_concurrency_cases.csv"))
    tasks=load_task_graph(root/"data"/"synthetic_task_graph.csv")
    task_order=[{"execution_order":i+1,"task_id":tid} for i,tid in enumerate(topological_order(tasks))]
    perf=performance_examples(root/"data"/"synthetic_parallel_performance.csv")
    summary={"case_count": len(audit), "average_concurrency_reliability_score": round(mean(float(r["concurrency_reliability_score"]) for r in audit),3), "average_concurrency_risk": round(mean(float(r["concurrency_risk"]) for r in audit),3), "highest_score_case": max(audit, key=lambda r: float(r["concurrency_reliability_score"]))["case_name"], "highest_risk_case": max(audit, key=lambda r: float(r["concurrency_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"concurrency_parallelism_audit.csv", audit)
    write_csv(root/"outputs"/"tables"/"concurrency_parallelism_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"parallel_performance_examples.csv", perf)
    write_csv(root/"outputs"/"tables"/"task_graph_topological_order.csv", task_order)
    write_csv(root/"outputs"/"tables"/"concurrency_calculator_examples.csv", calculator_examples())
    write_json(root/"outputs"/"json"/"concurrency_parallelism_audit.json", audit)
    write_json(root/"outputs"/"json"/"concurrency_parallelism_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"parallel_performance_examples.json", perf)
    write_json(root/"outputs"/"json"/"task_graph_topological_order.json", task_order)
    write_json(root/"outputs"/"json"/"concurrency_calculator_examples.json", calculator_examples())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
