# Ranking, Filtering, and Recommendation

This companion folder supports the Sustainable Catalyst article **Ranking, Filtering, and Recommendation** in the **Algorithms & Computational Reasoning** series.

It treats ranking and recommendation as accountable visibility systems. The examples are synthetic and are designed to make candidate generation, filtering, relevance scoring, similarity, personalization, diversity, exposure effects, feedback loops, fairness review, and governance visible.

## Contents

- `python/` reference workflow, calculators, CLI, and tests.
- `r/` base R summary and plotting workflow.
- `sql/` relational schema and audit queries.
- `julia/`, `haskell/`, `rust/`, `go/`, `c/`, `cpp/`, `fortran/`, `java/`, `typescript/`, `prolog/`, and `racket/` language-specific examples.
- `data/` synthetic cases, candidates, ranking signals, and governance taxonomy.
- `outputs/` generated tables, JSON, figures, logs, and reports.
- `calculators/` self-contained calculator scripts for future website reuse.
- `canvas/` Canvas-ready manifest and summary cards.

## Run

```bash
make smoke
make all
```

Or run the reference workflow directly:

```bash
python3 python/ranking_recommendation/audit.py
python3 python/ranking_recommendation/cli.py --weights text_match=0.36,quality=0.30,freshness=0.16,diversity_bonus=0.14,risk_penalty=0.20
```

All examples use synthetic teaching data only.
