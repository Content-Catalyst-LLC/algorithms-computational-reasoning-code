# Monte Carlo Methods and Computational Uncertainty

This companion folder supports the Sustainable Catalyst article **“Monte Carlo Methods and Computational Uncertainty.”** It treats Monte Carlo methods as computational uncertainty reasoning: random sampling, repeated trials, probability estimation, uncertainty propagation, convergence diagnostics, threshold risk, confidence intervals, reproducibility, and responsible interpretation.

## Article sequence

- Previous: Numerical Methods and Algorithmic Approximation
- Current: Monte Carlo Methods and Computational Uncertainty
- Next: Computational Experiments and Reproducible Workflows

## What this folder contains

- `python/` dependency-light Monte Carlo uncertainty audit workflow
- `r/` base R summary workflow for Monte Carlo outputs and diagnostics
- `calculators/` self-contained Python and R calculators for pi estimation, threshold risk, uncertainty propagation, and confidence intervals
- `data/` synthetic distribution and scenario metadata
- `outputs/` generated CSV, JSON, and figure outputs
- `docs/` article metadata, navigation, workflow notes, and review checklist
- language folders with compact, runnable or inspectable examples across Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

## Run the main workflows

```bash
python3 python/monte_carlo_methods_computational_uncertainty_audit.py
Rscript r/monte_carlo_methods_computational_uncertainty_summary.R
```

## Run calculator smoke tests

```bash
bash calculators/run_calculator_smoke_tests.sh
```

The examples use synthetic teaching data and are designed for reproducibility, transparent assumptions, and auditable computational reasoning.
