from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json, random
from statistics import mean, pstdev

@dataclass(frozen=True)
class EvolutionarySearchCase:
    case_name: str
    problem_context: str
    evolutionary_strategy: str
    representation_clarity: float
    fitness_alignment: float
    variation_design: float
    diversity_tracking: float
    parameter_documentation: float
    benchmark_evidence: float
    robustness_testing: float
    traceability: float
    safety_review: float
    governance_readiness: float

WEIGHTS=[0.12,0.12,0.10,0.10,0.10,0.12,0.10,0.08,0.08,0.08]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def evolutionary_quality(case: EvolutionarySearchCase) -> float:
    vals=[case.representation_clarity,case.fitness_alignment,case.variation_design,case.diversity_tracking,case.parameter_documentation,case.benchmark_evidence,case.robustness_testing,case.traceability,case.safety_review,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def evolutionary_risk(case: EvolutionarySearchCase) -> float:
    vals=[case.representation_clarity,case.fitness_alignment,case.variation_design,case.diversity_tracking,case.parameter_documentation,case.benchmark_evidence,case.robustness_testing,case.traceability,case.safety_review,case.governance_readiness]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong evolutionary-search governance discipline"
    if q >= 70 and r <= 35: return "usable evolutionary search with validation and monitoring needs"
    if r >= 55: return "high evolutionary-search risk"
    return "partial evolutionary-search discipline"

def load_cases(path: Path) -> list[EvolutionarySearchCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [EvolutionarySearchCase(r["case_name"],r["problem_context"],r["evolutionary_strategy"],float(r["representation_clarity"]),float(r["fitness_alignment"]),float(r["variation_design"]),float(r["diversity_tracking"]),float(r["parameter_documentation"]),float(r["benchmark_evidence"]),float(r["robustness_testing"]),float(r["traceability"]),float(r["safety_review"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[EvolutionarySearchCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=evolutionary_quality(c),evolutionary_risk(c)
        out.append({**asdict(c),"evolutionary_search_quality":round(q,3),"evolutionary_search_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def binary_fitness(candidate: list[int]) -> int:
    return sum(candidate)

def mutate(candidate: list[int], mutation_rate: float, rng: random.Random) -> list[int]:
    return [1-bit if rng.random() < mutation_rate else bit for bit in candidate]

def crossover(a: list[int], b: list[int], rng: random.Random) -> list[int]:
    if len(a) != len(b):
        raise ValueError("Parents must have equal length.")
    point=rng.randint(1, len(a)-1)
    return a[:point] + b[point:]

def diversity(population: list[list[int]]) -> float:
    if len(population) <= 1:
        return 0.0
    distances=[]
    for i in range(len(population)):
        for j in range(i+1, len(population)):
            diff=sum(1 for a,b in zip(population[i], population[j]) if a != b)
            distances.append(diff / len(population[i]))
    return mean(distances)

def simple_genetic_algorithm(seed: int=20260617, population_size: int=20, genome_length: int=12, generations: int=30, mutation_rate: float=0.03) -> dict[str, object]:
    rng=random.Random(seed)
    population=[[rng.randint(0,1) for _ in range(genome_length)] for _ in range(population_size)]
    history=[]
    for generation in range(generations):
        population=sorted(population, key=binary_fitness, reverse=True)
        history.append({"generation":generation,"best_fitness":binary_fitness(population[0]),"average_fitness":mean(binary_fitness(c) for c in population),"diversity":diversity(population)})
        survivors=population[:population_size//2]
        offspring=list(survivors)
        while len(offspring) < population_size:
            parent_a=rng.choice(survivors)
            parent_b=rng.choice(survivors)
            child=mutate(crossover(parent_a,parent_b,rng), mutation_rate, rng)
            offspring.append(child)
        population=offspring
    population=sorted(population, key=binary_fitness, reverse=True)
    return {"seed":seed,"best_candidate":population[0],"best_fitness":binary_fitness(population[0]),"final_diversity":diversity(population),"history":history}

def multi_seed_summary() -> dict[str, object]:
    runs=[simple_genetic_algorithm(seed=s) for s in range(20260610,20260620)]
    best=[float(r["best_fitness"]) for r in runs]
    divs=[float(r["final_diversity"]) for r in runs]
    return {"runs":len(runs),"mean_best_fitness":mean(best),"stddev_best_fitness":pstdev(best),"mean_final_diversity":mean(divs),"stddev_final_diversity":pstdev(divs)}

def algorithm_demos() -> dict[str, object]:
    return {"simple_genetic_algorithm":simple_genetic_algorithm(),"multi_seed_summary":multi_seed_summary()}

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows=evaluate(load_cases(root/"data"/"synthetic_evolutionary_search_cases.csv"))
    summary={"case_count":len(rows),"average_evolutionary_search_quality":round(mean(float(r["evolutionary_search_quality"]) for r in rows),3),"average_evolutionary_search_risk":round(mean(float(r["evolutionary_search_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["evolutionary_search_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["evolutionary_search_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"evolutionary_search_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"evolutionary_search_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"evolutionary_search_audit.json", rows)
    write_json(root/"outputs"/"json"/"evolutionary_search_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"evolutionary_algorithm_demos.json", algorithm_demos())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
