#!/usr/bin/env python3
import argparse, json, random
from pathlib import Path
from statistics import mean
def diversity(population):
    if len(population) <= 1:
        return 0.0
    distances=[]
    for i in range(len(population)):
        for j in range(i+1, len(population)):
            distances.append(sum(1 for a,b in zip(population[i],population[j]) if a!=b)/len(population[i]))
    return mean(distances)
def compute(population_size, genome_length, seed):
    rng=random.Random(seed)
    population=[[rng.randint(0,1) for _ in range(genome_length)] for _ in range(population_size)]
    return {"population_size":population_size,"genome_length":genome_length,"seed":seed,"average_pairwise_hamming_diversity":round(diversity(population),6),"interpretation":"Higher diversity means candidates are more different; low diversity can indicate premature convergence."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--population-size",type=int,default=20)
    p.add_argument("--genome-length",type=int,default=12)
    p.add_argument("--seed",type=int,default=20260617)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.population_size,a.genome_length,a.seed)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"population_diversity_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
