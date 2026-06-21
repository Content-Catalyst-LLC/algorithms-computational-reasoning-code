# Decision Under Uncertainty and Computational Risk

This folder is a deep companion repository for the Sustainable Catalyst article **Decision Under Uncertainty and Computational Risk**.

It translates the article into reproducible teaching workflows for probability, expected value, risk thresholds, sensitivity analysis, regret, uncertainty ranges, risk registers, decision logs, governance review, and responsible computational interpretation.

This is not a production risk engine, credit model, clinical triage tool, insurance model, investment model, or automated decision system. It is an educational research companion that makes decision logic inspectable, auditable, and contestable.

## Article sequence

- Previous: `causal-algorithms-and-intervention-modeling`
- Current: `decision-under-uncertainty-and-computational-risk`
- Next: `machine-learning-as-algorithmic-inference`

## What this folder contains

| Layer | Purpose |
|---|---|
| `python/` | Dependency-light decision-under-uncertainty workflow, threshold review, risk sensitivity, and smoke tests. |
| `r/` | Base-R summaries and diagnostic figures from generated CSV outputs. |
| `sql/` | Governance schema and review queries for options, thresholds, assumptions, risks, and audit trails. |
| `calculators/` | Self-contained calculators for expected value, threshold action, regret, and risk scores. |
| `docs/` | Data dictionary, method notes, governance checklist, uncertainty register, and use-boundary statement. |
| `canvas/` | Canvas-ready cards, schemas, and exports for future website/tool integration. |
| `outputs/` | Generated CSV, JSON, log, and figure outputs. |
| language folders | Compact examples showing the same uncertainty reasoning across computational traditions. |

## Fast start

From this article folder:

```bash
make run
make test
make calculators
```

Or run the Python workflow directly:

```bash
python3 python/decision_uncertainty_risk_workflow.py
python3 python/risk_threshold_review.py
python3 python/uncertainty_sensitivity_analysis.py
```

Optional R figures, if R is installed:

```bash
Rscript r/decision_risk_diagnostics.R
```

## Core outputs

Running the workflow writes:

- `outputs/tables/synthetic_decision_cases.csv`
- `outputs/tables/decision_options.csv`
- `outputs/tables/decision_metrics.csv`
- `outputs/tables/threshold_review.csv`
- `outputs/tables/risk_register.csv`
- `outputs/tables/uncertainty_sensitivity_grid.csv`
- `outputs/json/decision_risk_audit_summary.json`
- `outputs/logs/workflow_manifest.json`

## Interpretation boundary

All records are synthetic and educational. A real decision-under-uncertainty workflow must be reviewed for data provenance, probability calibration, utility assumptions, uncertainty structure, distributional effects, legal constraints, ethical limits, stakeholder impact, and escalation requirements.
