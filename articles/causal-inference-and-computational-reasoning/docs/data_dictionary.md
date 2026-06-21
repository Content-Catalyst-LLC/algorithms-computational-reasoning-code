# Data Dictionary

The generated dataset is synthetic. It is designed to show why causal inference is different from prediction.

| Field | Meaning | Causal role |
|---|---|---|
| `unit_id` | Synthetic observation identifier. | Unit of analysis. |
| `prior_risk` | Simulated pre-treatment risk level. | Confounder. |
| `institutional_access` | Simulated access or institutional advantage. | Confounder. |
| `baseline_capacity` | Simulated baseline capacity before treatment. | Confounder. |
| `treatment_probability` | Probability of receiving treatment under the synthetic assignment process. | Propensity score. |
| `treatment` | Whether the unit received the intervention. | Treatment indicator. |
| `potential_outcome_control` | Synthetic potential outcome without intervention. | Usually unobserved in real data. |
| `potential_outcome_treated` | Synthetic potential outcome under treatment. | Usually unobserved in real data. |
| `observed_outcome` | Observed outcome under the assigned treatment condition. | Evidence available to estimator. |
| `true_effect` | Synthetic treatment effect used to generate data. | Known only because this is a teaching dataset. |

## Important boundary

Real causal inference does not usually reveal both potential outcomes for the same unit. This repository includes both only to support teaching, debugging, and estimator comparison.
