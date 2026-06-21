# Algorithms in Scientific Computing

This article folder supports the Sustainable Catalyst article **Algorithms in Scientific Computing** in the **Algorithms & Computational Reasoning** series.

It includes reproducible, educational workflows for:

- finite-difference derivative approximation;
- numerical integration and quadrature;
- Euler and Runge-Kutta ODE solver comparisons;
- convergence and error checks;
- floating-point and approximation-risk review;
- Monte Carlo estimation and uncertainty summaries;
- reproducible scientific workflow checklists;
- calculator scripts for derivative, integral, ODE, and Monte Carlo examples;
- multi-language examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket.

These examples are educational scaffolds, not production scientific, engineering, environmental, health, policy, financial, or infrastructure analysis tools.

## Article sequence

- Previous: `simulation-as-computational-reasoning`
- Current: `algorithms-in-scientific-computing`
- Next: `numerical-methods-and-algorithmic-approximation`

## Run core workflows

```bash
python3 python/algorithms_in_scientific_computing_audit.py
Rscript r/algorithms_in_scientific_computing_summary.R
```

## Run calculators

```bash
python3 calculators/python/scientific_computing_calculator.py
Rscript calculators/r/scientific_computing_calculator.R
```

## Notes

The examples intentionally use small synthetic mathematical models. They are designed for reasoning about approximation, discretization, convergence, finite precision, uncertainty, reproducibility, validation, governance, and representation risk rather than for replacing domain-specific scientific computing practice.
