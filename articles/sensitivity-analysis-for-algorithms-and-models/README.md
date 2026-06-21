# Sensitivity Analysis for Algorithms and Models

This companion folder supports the Sustainable Catalyst article **Sensitivity Analysis for Algorithms and Models** in the **Algorithms & Computational Reasoning** series.

The article examines how computational outputs change when assumptions, inputs, parameters, thresholds, rules, data, random seeds, or model structures shift. The goal is to make algorithmic conclusions more inspectable, reproducible, testable, and accountable.

## Article sequence

- Previous: `model-validation-testing-and-computational-evidence`
- Current: `sensitivity-analysis-for-algorithms-and-models`
- Next: `uncertainty-quantification-in-computational-workflows`

## Core workflow

Run the Python reference workflow:

```bash
python3 python/sensitivity_analysis_audit.py
```

Then summarize with R when available:

```bash
Rscript r/sensitivity_summary.R
```

Run the calculator layer smoke test:

```bash
bash calculators/run_calculator_smoke_tests.sh
```

Run all available checks:

```bash
bash run_all_available.sh
```

## Outputs

Generated outputs are written to:

- `outputs/tables/`
- `outputs/json/`
- `outputs/figures/`
- `outputs/logs/`
- `calculators/outputs/`

## Governance note

Sensitivity analysis should expose dependence, not create false confidence. Every sweep should document what varied, what stayed fixed, why ranges were selected, and how findings affect validation, monitoring, and decision use.
