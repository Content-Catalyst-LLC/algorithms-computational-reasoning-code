# Data Dictionary

## supervised_observations.csv

- `unit_id` — synthetic observation identifier.
- `feature_access` — synthetic feature representing access, support, or observed opportunity.
- `feature_risk` — synthetic feature representing risk or burden.
- `latent_group` — synthetic unobserved group used to generate structure for teaching.
- `true_probability` — synthetic data-generating probability.
- `label` — supervised learning target.
- `split` — train or test partition.
- `predicted_probability` — simple model score.

## unsupervised_cluster_summary.csv

- `cluster` — learned cluster identifier.
- `centroid_access`, `centroid_risk` — centroid coordinates.
- `mean_distance_to_centroid` — simple cohesion measure.

## reinforcement_learning_summary.csv

- `arm` — action option.
- `true_reward_probability` — synthetic reward probability.
- `times_selected` — number of times the action was chosen.
- `observed_mean_reward` — empirical reward rate.
