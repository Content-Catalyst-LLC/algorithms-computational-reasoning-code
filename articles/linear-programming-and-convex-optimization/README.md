# Linear Programming and Convex Optimization

This companion folder supports the Sustainable Catalyst article **Linear Programming and Convex Optimization** in the **Algorithms & Computational Reasoning** series.

The folder contains reproducible workflows, calculators, synthetic teaching data, governance checklists, and multi-language examples for decision variables, objectives, constraints, feasible regions, linear programming, convex functions, slack, shadow prices, sensitivity, robustness, fairness review, and traceability.

## Article sequence

- Previous: `decision-rules-thresholds-and-classification`
- Current: `linear-programming-and-convex-optimization`
- Next: `gradient-descent-and-optimization-in-machine-learning`

## Run the main workflows

```bash
make smoke
make all
```

Or run the Python audit directly:

```bash
python3 python/lp_convex/audit.py
python3 python/lp_convex/cli.py
```

## Calculator examples

```bash
python3 calculators/python/linear_programming_calculator.py
Rscript calculators/r/convex_quadratic_calculator.R
```

## Governance framing

Optimization outputs should be interpreted relative to the model that defines variables, objectives, constraints, data, and feasible sets. A mathematically optimal solution is not automatically an institutionally legitimate solution.
