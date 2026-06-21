# Bayesian Computation and Updating Beliefs

This companion folder supports the Sustainable Catalyst article **“Bayesian Computation and Updating Beliefs.”** It provides reproducible, multi-language examples for Bayesian computation, Bayes' theorem, prior distributions, likelihood functions, posterior distributions, evidence updating, sequential inference, posterior prediction, prior sensitivity, expected loss, Bayesian decision-making, validation, calibration, governance, and interpretation limits.

## Article sequence

- Previous: `probabilistic-algorithms-and-reasoning-under-uncertainty`
- Current: `bayesian-computation-and-updating-beliefs`
- Next: `causal-inference-and-computational-reasoning`

## Core workflow

```bash
python3 python/bayesian_computation_updating_beliefs_audit.py
Rscript r/bayesian_computation_updating_beliefs_summary.R
bash calculators/run_calculator_smoke_tests.sh
```

The Python workflow produces CSV and JSON outputs under `outputs/`. The R workflow creates base-R diagnostic figures when R is available. The calculator layer provides reusable Bayesian updating, beta-binomial, posterior probability, prior sensitivity, and expected-loss utilities.
