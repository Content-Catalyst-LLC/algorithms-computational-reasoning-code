# Numerical Methods and Algorithmic Approximation

This companion folder supports the Sustainable Catalyst article **“Numerical Methods and Algorithmic Approximation.”** It treats numerical methods as disciplined algorithmic approximation: finite differences, quadrature, root finding, iterative solvers, time stepping, error analysis, convergence, tolerances, reproducibility, and responsible interpretation.

## Article sequence

- Previous: Algorithms in Scientific Computing
- Current: Numerical Methods and Algorithmic Approximation
- Next: Monte Carlo Methods and Computational Uncertainty

## What this folder contains

- `python/` dependency-light numerical approximation audit workflow
- `r/` base R summary workflow for approximation error and convergence outputs
- `calculators/` self-contained Python and R calculators for finite differences, quadrature, roots, and ODE time stepping
- `data/` synthetic parameters and method metadata
- `outputs/` generated CSV, JSON, and figure outputs
- `docs/` article metadata, navigation, and workflow notes
- language folders with compact, runnable or inspectable examples across Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

## Run the main workflows

```bash
python3 python/numerical_methods_algorithmic_approximation_audit.py
Rscript r/numerical_methods_algorithmic_approximation_summary.R
```

## Run calculator smoke tests

```bash
bash calculators/run_calculator_smoke_tests.sh
```

The examples use synthetic teaching data and are designed for reproducibility, transparent assumptions, and auditable computational reasoning.
