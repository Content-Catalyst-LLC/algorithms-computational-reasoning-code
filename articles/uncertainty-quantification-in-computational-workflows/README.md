# Uncertainty Quantification in Computational Workflows

This companion article folder provides reproducible teaching workflows for uncertainty quantification in computational workflows. It includes uncertainty inventories, uncertainty propagation, Monte Carlo-style ensembles, output interval summaries, threshold exceedance estimates, uncertainty-source influence rankings, review checklists, governance artifacts, and multi-language examples.

## Article sequence

- Previous: `sensitivity-analysis-for-algorithms-and-models`
- Current: `uncertainty-quantification-in-computational-workflows`
- Next: `probabilistic-algorithms-and-reasoning-under-uncertainty`

## Main workflows

```bash
python3 python/uncertainty_quantification_computational_workflows_audit.py
Rscript r/uncertainty_quantification_computational_workflows_summary.R
```

The Python workflow writes CSV and JSON outputs under `outputs/`. The R workflow reads those outputs and writes simple base-R figures and summaries.

## Calculator layer

```bash
python3 calculators/python/model_calculator.py --mode ensemble --runs 1000 --threshold 0.62
Rscript calculators/r/model_calculator.R ensemble 1000 0.62
bash calculators/run_calculator_smoke_tests.sh
```

## Design principles

- Make uncertainty sources explicit.
- Preserve parameters, seeds, assumptions, and generated outputs.
- Separate uncertainty quantification from validation while linking them in review.
- Communicate uncertainty as decision-relevant evidence, not decorative caution.
- Keep computational outputs reproducible, inspectable, and accountable.
