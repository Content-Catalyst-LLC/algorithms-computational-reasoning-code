# Causal Algorithms and Intervention Modeling

This folder is a deep companion repository for the Sustainable Catalyst article **Causal Algorithms and Intervention Modeling**.

The folder translates the article into reproducible teaching workflows for causal algorithms, intervention modeling, policy comparison, do-style scenario records, adjustment review, intervention feasibility, threshold decisions, sensitivity checks, and governance documentation.

This is not a production causal-inference, policy-optimization, or automated decision system. It is an educational research companion that makes intervention reasoning inspectable, testable, and auditable.

## Article sequence

- Previous: `counterfactual-reasoning-in-algorithmic-systems`
- Current: `causal-algorithms-and-intervention-modeling`
- Next: `decision-under-uncertainty-and-computational-risk`

## What this folder contains

| Layer | Purpose |
|---|---|
| `python/` | Dependency-light intervention modeling workflow, scenario comparison, adjustment review, policy sensitivity, and smoke tests. |
| `r/` | Base-R summaries and diagnostic figures from generated CSV outputs. |
| `sql/` | Governance schema and review queries for interventions, assumptions, effects, sensitivity checks, and audit trails. |
| `calculators/` | Self-contained calculators for effect contrasts, intervention scores, thresholds, and net benefit. |
| `docs/` | Data dictionary, method notes, governance checklist, use-boundary statement, and interpretation guidance. |
| `canvas/` | Canvas-ready cards, schemas, and exports for future website/tool integration. |
| `outputs/` | Generated CSV, JSON, log, and figure outputs. |
| language folders | Compact examples showing the same intervention-modeling idea across computational traditions. |

## Fast start

From this article folder:

```bash
make run
make test
make calculators
```

Or run the Python workflow directly:

```bash
python3 python/intervention_modeling_workflow.py
python3 python/intervention_graph_review.py
python3 python/intervention_policy_sensitivity.py
```

Optional R figures, if R is installed:

```bash
Rscript r/intervention_modeling_diagnostics.R
```

## Core outputs

Running the workflow writes:

- `outputs/tables/synthetic_intervention_cases.csv`
- `outputs/tables/intervention_scenarios.csv`
- `outputs/tables/intervention_effect_estimates.csv`
- `outputs/tables/adjustment_set_review.csv`
- `outputs/tables/intervention_feasibility_review.csv`
- `outputs/tables/policy_sensitivity_grid.csv`
- `outputs/json/intervention_modeling_audit_summary.json`
- `outputs/logs/workflow_manifest.json`

## Interpretation boundary

All records are synthetic and educational. A real intervention model must be reviewed for causal identification, feasibility, ethics, distributional effects, legal constraints, population scope, measurement limits, and institutional accountability.
