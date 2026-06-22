# Data Dictionary

## bias_history_group_records.csv

- `group_id`: synthetic group label.
- `data_share`: share of the group in available data.
- `deployment_share`: share of the group in deployment population.
- `selection_rate`: rate receiving positive outcome or prediction.
- `label_positive_rate`: rate of positive institutional labels.
- `verified_positive_rate`: later verified or alternative positive-outcome rate.
- `provenance_risk`: risk that data origin encodes institutional history.
- `measurement_weakness`: weakness in feature/label construct validity.
- `proxy_risk`: risk that features carry historical inequality indirectly.
- `remediation`: capacity to correct outcomes and source conditions.

## bias_history_group_metrics.csv

- `representation_gap`: absolute data/deployment share difference.
- `label_gap`: absolute institutional label/verified-outcome difference.
- `historical_risk_score`: average of provenance risk, measurement weakness, proxy risk, and weak remediation.

## bias_history_audit_summary.csv

- `selection_gap`: max minus min group selection rate.
- `total_representation_gap`: sum of group representation gaps.
- `max_label_gap`: maximum label gap across groups.
- `mean_historical_risk_score`: average historical risk.
- `max_historical_risk_score`: highest group historical risk.
- `status`: pass, review, or escalate.
