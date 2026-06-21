# Data Dictionary

The generated dataset is synthetic. It is designed to show how counterfactual reasoning differs from ordinary prediction.

| Field | Meaning | Counterfactual role |
|---|---|---|
| `case_id` | Synthetic decision-record identifier. | Unit of review. |
| `baseline_score` | Starting institutional or eligibility score. | Mutable only within bounded review rules. |
| `document_quality` | Quality of submitted documentation. | Potentially changeable through resubmission. |
| `timeliness` | Whether required steps were completed on time. | Partly changeable; depends on policy context. |
| `prior_flag` | Historical flag or prior record. | Usually non-actionable and should not be used for recourse. |
| `access_constraint` | Structural access constraint. | Often not individually actionable. |
| `risk_adjustment` | Model-derived adjustment. | Used to show opaque internal model contribution. |
| `decision_score` | Weighted score used by the synthetic rule. | Determines decision at threshold. |
| `decision` | Synthetic accept/review/deny label. | Outcome to test under alternatives. |
| `counterfactual_feature` | Feature changed in a candidate scenario. | Local alteration for what-if review. |
| `delta` | Amount of proposed change. | Magnitude of counterfactual intervention. |
| `flipped` | Whether the counterfactual changes the decision. | Main recourse indicator. |
| `feasibility_status` | Actionability review status. | Separates mathematical possibility from responsible explanation. |

## Important boundary

A computed counterfactual can show that a decision would have changed under different inputs. It does not automatically prove that the change is fair, realistic, legally appropriate, or causally meaningful.
