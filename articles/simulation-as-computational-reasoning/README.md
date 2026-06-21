# Simulation as Computational Reasoning

This article folder supports the Sustainable Catalyst article **Simulation as Computational Reasoning** in the **Algorithms & Computational Reasoning** series.

It includes reproducible, educational workflows for:

- running deterministic and stochastic simulations;
- comparing scenarios and counterfactuals;
- sweeping parameters and reviewing sensitivity;
- summarizing Monte Carlo uncertainty;
- documenting assumptions, states, rules, parameters, time steps, and outputs;
- reviewing validation, calibration, governance, and representation risk;
- calculator scripts for state updates, scenario comparison, sensitivity, and Monte Carlo summaries;
- multi-language examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket.

These examples are educational scaffolds, not production scientific, engineering, policy, financial, epidemiological, climate, or security simulation tools.

## Article sequence

- Previous: `security-failures-as-algorithmic-failures`
- Current: `simulation-as-computational-reasoning`
- Next: `algorithms-in-scientific-computing`

## Run core workflows

```bash
python3 python/simulation_as_computational_reasoning_audit.py
Rscript r/simulation_as_computational_reasoning_summary.R
```

## Run calculators

```bash
python3 calculators/python/simulation_calculator.py
Rscript calculators/r/simulation_calculator.R
```

## Notes

The examples intentionally use small synthetic models. They are designed for reasoning about simulation, executable models, time steps, scenarios, uncertainty, sensitivity, validation, calibration, governance, and representation risk rather than for replacing domain-specific modeling, expert review, or institutional decision processes.
