# Model Validation, Testing, and Computational Evidence

This companion folder supports the Sustainable Catalyst article **Model Validation, Testing, and Computational Evidence** in the **Algorithms & Computational Reasoning** series.

The article examines how computational models become credible evidence through validation, verification, testing, benchmark comparison, diagnostics, calibration, subgroup review, threshold analysis, sensitivity review, audit trails, and governance.

## Article sequence

- Previous: `computational-experiments-and-reproducible-workflows`
- Current: `model-validation-testing-and-computational-evidence`
- Next: `sensitivity-analysis-for-algorithms-and-models`

## Core workflow

Run the Python reference workflow:

```bash
python3 python/model_validation_evidence_audit.py
```

Then summarize with R when available:

```bash
Rscript r/model_validation_summary.R
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

Validation is not proof that a model is true. It is evidence that a model is credible for a defined use, under defined assumptions, with known limitations and review records.
