# Causal Inference and Computational Reasoning

This folder is a reproducible companion repository for the Sustainable Catalyst article **Causal Inference and Computational Reasoning**.

The goal is not to provide a production causal-inference library. The goal is to make the article's reasoning operational: define a causal question, generate transparent synthetic data, compare naive and adjusted estimates, inspect balance, document assumptions, run sensitivity checks, preserve audit trails, and show how causal claims should be reviewed before they guide action.

## Article sequence

- Previous: `bayesian-computation-and-updating-beliefs`
- Current: `causal-inference-and-computational-reasoning`
- Next: `counterfactual-reasoning-in-algorithmic-systems`

## What this folder contains

| Layer | Purpose |
|---|---|
| `python/` | Main dependency-light causal audit workflow, DAG utilities, sensitivity analysis, and tests. |
| `r/` | Base-R diagnostic summaries and plots from the generated outputs. |
| `julia/` | Numerical treatment-effect and overlap checks. |
| `sql/` | Governance-oriented schema and review queries for causal evidence records. |
| `calculators/` | Self-contained calculators for treatment contrasts, difference-in-differences, IPW, and sensitivity checks. |
| `docs/` | Data dictionary, causal review checklist, governance notes, and use-boundary documentation. |
| `canvas/` | Canvas-ready cards and schema files for later website/tool integration. |
| `data/` | Synthetic design notes, DAG edges, and input assumptions. |
| `outputs/` | Reproducible generated CSV, JSON, figure, and log outputs. |
| language folders | Compact examples showing the same causal reasoning idea across multiple computational traditions. |

## Fast start

From this article folder:

```bash
make run
make test
make calculators
```

Or run the Python workflow directly:

```bash
python3 python/causal_inference_audit_workflow.py
```

Optional R figures, if R is installed:

```bash
Rscript r/causal_inference_diagnostics.R
```

## Core outputs

Running the workflow writes:

- `outputs/tables/synthetic_causal_observations.csv`
- `outputs/tables/causal_effect_estimates.csv`
- `outputs/tables/covariate_balance_diagnostics.csv`
- `outputs/tables/causal_assumption_register.csv`
- `outputs/tables/sensitivity_analysis.csv`
- `outputs/json/causal_audit_summary.json`
- `outputs/logs/workflow_manifest.json`

## Interpretation boundary

All data are synthetic and educational. The scripts demonstrate causal reasoning structure, not operational decision-making. A real causal claim would require domain evidence, data provenance review, stakeholder review, sensitivity analysis, ethical review, and institutional accountability.
