from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json, random
from statistics import mean, pstdev

@dataclass(frozen=True)
class RandomizedAlgorithmCase:
    case_name: str
    problem_context: str
    randomized_procedure: str
    randomness_clarity: float
    distribution_validity: float
    seed_control: float
    error_bound_clarity: float
    sample_adequacy: float
    repeatability: float
    edge_case_coverage: float
    variance_analysis: float
    traceability: float
    governance_readiness: float

WEIGHTS=[0.12,0.12,0.10,0.10,0.10,0.10,0.10,0.10,0.08,0.08]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def randomized_quality(case: RandomizedAlgorithmCase) -> float:
    vals=[case.randomness_clarity,case.distribution_validity,case.seed_control,case.error_bound_clarity,case.sample_adequacy,case.repeatability,case.edge_case_coverage,case.variance_analysis,case.traceability,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def randomized_risk(case: RandomizedAlgorithmCase) -> float:
    vals=[case.randomness_clarity,case.distribution_validity,case.seed_control,case.error_bound_clarity,case.sample_adequacy,case.repeatability,case.edge_case_coverage,case.variance_analysis,case.traceability,case.governance_readiness]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong randomized-algorithm discipline"
    if q >= 70 and r <= 35: return "usable probabilistic procedure with review needs"
    if r >= 55: return "high randomized-procedure risk"
    return "partial randomized-algorithm discipline"

def load_cases(path: Path) -> list[RandomizedAlgorithmCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [RandomizedAlgorithmCase(r["case_name"],r["problem_context"],r["randomized_procedure"],float(r["randomness_clarity"]),float(r["distribution_validity"]),float(r["seed_control"]),float(r["error_bound_clarity"]),float(r["sample_adequacy"]),float(r["repeatability"]),float(r["edge_case_coverage"]),float(r["variance_analysis"]),float(r["traceability"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[RandomizedAlgorithmCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=randomized_quality(c),randomized_risk(c)
        out.append({**asdict(c),"randomized_algorithm_quality":round(q,3),"randomized_algorithm_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def randomized_quicksort(values: list[int], rng: random.Random) -> list[int]:
    if len(values) <= 1:
        return list(values)
    pivot=rng.choice(values)
    less=[x for x in values if x < pivot]
    equal=[x for x in values if x == pivot]
    greater=[x for x in values if x > pivot]
    return randomized_quicksort(less,rng)+equal+randomized_quicksort(greater,rng)

def monte_carlo_pi(trials: int, seed: int) -> dict[str, float]:
    rng=random.Random(seed)
    inside=0
    for _ in range(trials):
        x=rng.random(); y=rng.random()
        if x*x + y*y <= 1.0:
            inside += 1
    estimate=4.0*inside/trials
    return {"trials":trials,"seed":seed,"pi_estimate":estimate,"absolute_error_against_reference":abs(estimate-3.141592653589793)}

def repeated_sample_means(population: list[float], sample_size: int, trials: int, seed: int) -> dict[str, float]:
    rng=random.Random(seed)
    means=[]
    for _ in range(trials):
        sample=[rng.choice(population) for _ in range(sample_size)]
        means.append(mean(sample))
    return {"sample_size":sample_size,"trials":trials,"seed":seed,"average_sample_mean":mean(means),"sample_mean_stddev":pstdev(means),"population_mean":mean(population)}

def algorithm_demos() -> dict[str, object]:
    seed=20260617
    rng=random.Random(seed)
    return {
        "randomized_quicksort":{"seed":seed,"sorted_values":randomized_quicksort([9,3,7,1,4,8], rng)},
        "monte_carlo_pi":monte_carlo_pi(5000, seed),
        "repeated_sample_means":repeated_sample_means([1,2,3,4,5,6,7,8,9],4,1000,seed)
    }

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows=evaluate(load_cases(root/"data"/"synthetic_randomized_algorithm_cases.csv"))
    summary={"case_count":len(rows),"average_randomized_algorithm_quality":round(mean(float(r["randomized_algorithm_quality"]) for r in rows),3),"average_randomized_algorithm_risk":round(mean(float(r["randomized_algorithm_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["randomized_algorithm_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["randomized_algorithm_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"randomized_algorithm_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"randomized_algorithm_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"randomized_algorithm_audit.json", rows)
    write_json(root/"outputs"/"json"/"randomized_algorithm_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"randomized_algorithm_demos.json", algorithm_demos())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
