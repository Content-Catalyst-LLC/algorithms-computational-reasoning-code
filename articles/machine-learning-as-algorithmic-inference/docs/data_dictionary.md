# Data Dictionary

| Field | Meaning | Review concern |
|---|---|---|
| `unit_id` | Synthetic observation identifier. | Not a real person or institution. |
| `prior_signal` | Input feature representing an earlier observable signal. | May become a proxy in real systems. |
| `measurement_quality` | Feature representing how well the case is measured. | Uneven measurement can distort inference. |
| `context_pressure` | Feature representing environmental or institutional pressure. | Contextual variables can be misused as individual blame. |
| `historical_access` | Feature representing prior access to resources or supports. | May encode institutional history. |
| `label` | Synthetic binary target. | Real labels require construct-validity review. |
| `model_score` | Predicted probability-like score. | Requires calibration before probability interpretation. |
| `predicted_label_0_50` | Classification at threshold 0.50. | Thresholds encode trade-offs and should be governed. |
