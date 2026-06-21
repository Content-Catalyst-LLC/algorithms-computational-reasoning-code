# Counterfactual Reasoning in Algorithmic Systems

This folder is a reproducible companion repository for the Sustainable Catalyst article **Counterfactual Reasoning in Algorithmic Systems**.

The folder turns the article's conceptual argument into concrete, inspectable workflows: generate synthetic decision records, compute counterfactual alternatives, identify minimal changes that would flip a decision, distinguish possible changes from feasible changes, document recourse boundaries, and preserve governance records for counterfactual explanations.

This is not a production fairness, recourse, or causal-inference library. It is an educational research companion designed to make counterfactual reasoning visible, auditable, and reusable.

## Article sequence

- Previous: `causal-inference-and-computational-reasoning`
- Current: `counterfactual-reasoning-in-algorithmic-systems`
- Next: `causal-algorithms-and-intervention-modeling`

## What this folder contains

| Layer | Purpose |
|---|---|
| `python/` | Main dependency-light counterfactual audit workflow, recourse search, threshold review, sensitivity checks, and tests. |
| `r/` | Base-R summary tables and diagnostic figures from generated outputs. |
| `julia/` | Numerical counterfactual distance and threshold examples. |
| `sql/` | Governance schema and queries for storing decisions, counterfactuals, feasibility reviews, and audit trails. |
| `calculators/` | Self-contained calculators for threshold flips, recourse distance, counterfactual contrasts, and feasibility scoring. |
| `docs/` | Data dictionary, counterfactual review checklist, governance notes, and use-boundary documentation. |
| `canvas/` | Canvas-ready cards and schemas for later website/tool integration. |
| `data/` | Synthetic design notes, allowed-change rules, and threshold policy examples. |
| `outputs/` | Reproducible generated CSV, JSON, figure, and log outputs. |
| language folders | Compact examples showing the same counterfactual reasoning idea across multiple computational traditions. |

## Fast start

From this article folder:

```bash
make run
make test
make calculators
```

Or run the Python workflow directly:

```bash
python3 python/counterfactual_reasoning_audit_workflow.py
```

Optional R figures, if R is installed:

```bash
Rscript r/counterfactual_reasoning_diagnostics.R
```

## Core outputs

Running the workflow writes:

- `outputs/tables/synthetic_algorithmic_decisions.csv`
- `outputs/tables/counterfactual_candidates.csv`
- `outputs/tables/minimal_recourse_actions.csv`
- `outputs/tables/threshold_sensitivity.csv`
- `outputs/tables/feasibility_review.csv`
- `outputs/json/counterfactual_audit_summary.json`
- `outputs/logs/workflow_manifest.json`

## Interpretation boundary

All records are synthetic and educational. A real counterfactual explanation must be checked for causal validity, feasibility, legality, contestability, and institutional accountability. A mathematical counterfactual is not automatically a fair, ethical, or actionable explanation.
