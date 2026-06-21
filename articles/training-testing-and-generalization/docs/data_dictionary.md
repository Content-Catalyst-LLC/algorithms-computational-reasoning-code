# Data Dictionary

| Field | Meaning |
|---|---|
| `row_id` | Synthetic observation identifier. |
| `split` | Training, test, or shifted-test membership. |
| `group` | Synthetic group marker used for group-level generalization review. |
| `feature_signal` | Feature aligned with the synthetic target-generating process. |
| `feature_context` | Contextual feature with predictive signal. |
| `feature_noise_proxy` | Noisy proxy feature that is more spuriously useful in training than testing. |
| `true_probability` | Synthetic latent probability used to generate the target. |
| `target` | Binary outcome generated from the synthetic probability. |
