# Features, Labels, and the Politics of Measurement

This companion folder supports the Sustainable Catalyst article **Features, Labels, and the Politics of Measurement**.

It provides reproducible, teaching-oriented workflows for examining how features, labels, proxies, measurement choices, construct definitions, missingness, label noise, threshold choices, and institutional categories shape machine-learning systems.

## Article sequence

- Previous: `supervised-unsupervised-and-reinforcement-learning`
- Current: `features-labels-and-the-politics-of-measurement`
- Next: `training-testing-and-generalization`

## What this repository folder demonstrates

This article folder treats machine learning measurement as a computational and institutional problem. The workflow generates synthetic records, creates imperfect features and labels, compares labels against a latent teaching construct, audits measurement reliability, evaluates group-level label noise, records feature provenance, and exports review artifacts for governance.

The examples are intentionally dependency-light. They are designed to run in ordinary terminal environments while producing tables, JSON records, logs, calculator outputs, and cross-language teaching examples.

## Contents

- `python/` — reference measurement audit workflow
- `tests/` — smoke tests for generated outputs and audit invariants
- `r/` — base-R diagnostic plots and summary tables
- `sql/` — schema and review queries for feature/label governance
- `calculators/` — self-contained calculators for measurement error, confusion tables, proxy risk, and label-noise impact
- `docs/` — method notes, data dictionary, governance checklist, and use boundaries
- `canvas/` — Canvas-ready cards, schemas, and exports
- language folders — compact examples across Python, R, Julia, SQL, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

All data are synthetic and educational. They should not be used for operational scoring, eligibility decisions, or real-world group comparison.

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
