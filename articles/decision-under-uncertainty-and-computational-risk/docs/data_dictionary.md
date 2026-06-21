# Data Dictionary

The generated data are synthetic. They model a simplified institutional decision setting where several action options are evaluated under incomplete information.

| Field | Meaning | Decision role |
|---|---|---|
| `case_id` | Synthetic unit identifier. | Unit of analysis. |
| `baseline_risk` | Estimated probability of adverse outcome without intervention. | Probability input. |
| `risk_uncertainty` | Half-width around baseline risk estimate. | Uncertainty range. |
| `benefit_if_success` | Synthetic benefit if intervention succeeds. | Utility input. |
| `loss_if_failure` | Synthetic loss if adverse event occurs. | Downside input. |
| `intervention_cost` | Synthetic cost of taking action. | Cost input. |
| `confidence_score` | Approximate reliability score for the estimate. | Governance input. |
| `option_name` | Candidate action. | Decision alternative. |
| `expected_net_value` | Expected benefit minus expected loss and cost. | Decision metric. |
| `regret` | Opportunity loss relative to best option. | Robustness metric. |
| `downside_exposure` | Approximate low-tail or adverse-exposure metric. | Risk metric. |
| `decision` | Suggested action under stated threshold. | Review output. |

These fields are intentionally simplified. Real systems need richer utility, uncertainty, calibration, subgroup, legal, and ethical review.
