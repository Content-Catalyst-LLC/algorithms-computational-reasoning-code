# Supervised, Unsupervised, and Reinforcement Learning

This companion folder supports the Sustainable Catalyst article **Supervised, Unsupervised, and Reinforcement Learning**.

It treats the three major learning paradigms as different forms of algorithmic inference: learning from labeled examples, finding structure without labels, and improving action through feedback. The folder is intentionally teaching-oriented and dependency-light. It makes training data, labels, features, clusters, reward signals, policies, validation metrics, uncertainty, and governance assumptions inspectable.

## Article sequence

- Previous: `machine-learning-as-algorithmic-inference`
- Current: `supervised-unsupervised-and-reinforcement-learning`
- Next: `features-labels-and-the-politics-of-measurement`

## What this folder includes

- `python/` — synthetic supervised, unsupervised, and reinforcement-learning audit workflow with smoke tests
- `r/` — optional base-R diagnostic summaries and plots
- `sql/` — schema and review queries for paradigm records, metrics, clusters, rewards, thresholds, and governance artifacts
- `calculators/` — self-contained calculators for classification metrics, cluster assignment, generalization gaps, and expected reward
- `docs/` — data dictionary, method notes, governance checklist, model-card notes, and use-boundary documentation
- `canvas/` — Canvas-ready cards, schema, and export manifest
- language folders — compact examples across Julia, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

All data are synthetic and educational. Nothing in this folder should be used for operational decisions without independent validation, domain review, and governance approval.

## Quick start

```bash
make all
```

or run the main workflow directly:

```bash
python3 python/supervised_unsupervised_rl_audit.py
python3 python/test_learning_paradigms_workflow.py
bash calculators/run_calculator_smoke_tests.sh
```

If R is installed, the Makefile will also generate optional diagnostic plots.

## Key outputs

- `outputs/tables/supervised_observations.csv`
- `outputs/tables/supervised_metrics.csv`
- `outputs/tables/unsupervised_cluster_assignments.csv`
- `outputs/tables/unsupervised_cluster_summary.csv`
- `outputs/tables/reinforcement_learning_trace.csv`
- `outputs/tables/reinforcement_learning_summary.csv`
- `outputs/tables/learning_paradigm_governance_register.csv`
- `outputs/json/learning_paradigms_audit_summary.json`
