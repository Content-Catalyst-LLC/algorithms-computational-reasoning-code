# Training, Testing, and Generalization

This companion folder supports the Sustainable Catalyst article **Training, Testing, and Generalization**.

It provides reproducible, teaching-oriented workflows for train/test splitting, validation design, cross-validation, generalization gaps, distribution shift, leakage review, uncertainty reporting, and responsible model evaluation.

## Article sequence

- Previous: `features-labels-and-the-politics-of-measurement`
- Current: `training-testing-and-generalization`
- Next: `overfitting-underfitting-and-model-error`

## What this repository folder demonstrates

This article folder treats model evaluation as a reasoning problem, not a scoreboard. The workflow generates synthetic training, test, and shifted-test datasets; fits a compact dependency-free logistic model; evaluates accuracy, log loss, Brier score, precision, recall, calibration, cross-validation stability, group-level performance, distribution shift, and governance risk.

The examples are intentionally dependency-light. They are designed to run in ordinary terminal environments while producing tables, JSON records, logs, calculator outputs, and cross-language teaching examples.

## Contents

- `python/` — reference training/testing/generalization audit workflow
- `tests/` — smoke tests for generated outputs and audit invariants
- `r/` — base-R diagnostic plots and summary tables
- `sql/` — schema and review queries for evaluation governance
- `calculators/` — self-contained calculators for split sizing, generalization gaps, confusion metrics, and cross-validation summaries
- `docs/` — method notes, data dictionary, governance checklist, and use boundaries
- `canvas/` — Canvas-ready cards, schemas, and exports
- language folders — compact examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

All data are synthetic and educational. They should not be used for operational model validation or real-world deployment decisions.

## Quick start

```bash
make run
make test
make calculators
```

Optional R diagnostics:

```bash
make r
```
