# Overfitting, Underfitting, and Model Error

This companion folder supports the Sustainable Catalyst article **Overfitting, Underfitting, and Model Error**.

It provides reproducible, teaching-oriented workflows for model complexity, bias/variance intuition, underfitting, overfitting, residual error, validation curves, regularization, shifted-test performance, and responsible model-error governance.

## Article sequence

- Previous: `training-testing-and-generalization`
- Current: `overfitting-underfitting-and-model-error`
- Next: `neural-networks-and-representation-learning`

## What this repository folder demonstrates

This article folder treats model error as a computational reasoning problem, not merely a metric. The workflow generates synthetic observations, fits polynomial models of different complexity, compares training, test, and shifted-test mean squared error, records generalization gaps, identifies underfitting and overfitting patterns, compares regularized and unregularized models, produces residual diagnostics, and writes governance review artifacts.

The examples are intentionally dependency-light. They are designed to run in ordinary terminal environments while producing tables, JSON records, logs, calculator outputs, and cross-language teaching examples.

## Contents

- `python/` — reference overfitting/underfitting/model-error audit workflow
- `tests/` — smoke tests for generated outputs and audit invariants
- `r/` — base-R diagnostic plots and summary tables
- `sql/` — schema and review queries for model-error governance
- `calculators/` — self-contained calculators for generalization gap, bias/variance intuition, and regularization review
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
