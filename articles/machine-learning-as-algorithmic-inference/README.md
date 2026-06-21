# Machine Learning as Algorithmic Inference

This companion folder supports the Sustainable Catalyst article **Machine Learning as Algorithmic Inference**.

It treats machine learning as a form of algorithmic inference: a disciplined process for learning patterns from data, representing uncertainty, producing classifications or predictions, and deciding how much trust to place in model outputs. The folder is intentionally teaching-oriented and dependency-light. It is designed to make assumptions, data construction, features, labels, train/test separation, evaluation, thresholds, calibration, subgroup error, governance documentation, and interpretation limits visible.

## Article sequence

- Previous: `decision-under-uncertainty-and-computational-risk`
- Current: `machine-learning-as-algorithmic-inference`
- Next: `supervised-unsupervised-and-reinforcement-learning`

## What this folder includes

- `python/` — synthetic data generation, logistic inference workflow, threshold review, calibration checks, subgroup diagnostics, and smoke tests
- `r/` — diagnostic summaries and optional base-R visual outputs
- `sql/` — schema and review queries for model records, metrics, features, thresholds, and governance artifacts
- `calculators/` — self-contained calculators for thresholds, expected prediction value, train/test error gaps, and calibration gaps
- `docs/` — model card, data dictionary, method notes, governance checklist, use-boundary notes, and responsible interpretation guidance
- `canvas/` — Canvas-ready cards, schema, and export manifest
- language folders — compact examples across Julia, Haskell, Rust, Go, C, C++, Fortran, Java, TypeScript, Prolog, and Racket

All data are synthetic and educational. Nothing in this folder should be used for operational decisions without independent validation, domain review, and governance approval.

## Quick start

```bash
make all
```

or run the main workflow directly:

```bash
python3 python/machine_learning_algorithmic_inference_audit.py
python3 python/test_machine_learning_workflow.py
bash calculators/run_calculator_smoke_tests.sh
```

If R is installed, the Makefile will also generate optional diagnostic plots.

## Key outputs

- `outputs/tables/ml_synthetic_observations.csv`
- `outputs/tables/ml_model_metrics.csv`
- `outputs/tables/ml_threshold_sweep.csv`
- `outputs/tables/ml_group_error_diagnostics.csv`
- `outputs/tables/ml_feature_label_audit.csv`
- `outputs/tables/ml_inference_governance_register.csv`
- `outputs/json/ml_inference_audit_summary.json`

## Interpretation stance

The workflow separates four ideas that are often collapsed:

1. pattern detection,
2. predictive inference,
3. decision thresholding,
4. responsible institutional use.

A machine-learning model can rank, classify, predict, or score cases, but those outputs do not automatically justify action. The article and companion code emphasize evaluation, calibration, threshold review, subgroup diagnostics, documentation, and use boundaries.
