# Method Notes

This repository uses a synthetic design with confounding. Treatment assignment depends on pre-treatment covariates. Outcomes also depend on those covariates. A naive treated-control comparison is therefore biased.

The workflow compares:

1. **Naive difference in means** — simple association, not automatically causal.
2. **Stratified adjustment** — compares treatment and control within prior-risk strata.
3. **Inverse probability weighting** — reweights observations by estimated treatment probability.
4. **Standardization / g-computation style estimate** — estimates outcomes under treatment and control using a simple transparent formula.
5. **Sensitivity analysis** — shows how conclusions shift under hypothetical unmeasured confounding.

The point is not that any one method is universal. The point is that causal reasoning requires a chain of assumptions, evidence, diagnostics, and interpretation boundaries.
