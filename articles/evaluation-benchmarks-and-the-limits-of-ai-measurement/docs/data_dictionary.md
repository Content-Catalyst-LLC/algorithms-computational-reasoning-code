# Data Dictionary

## benchmark_items.csv

- `model`: synthetic model identifier.
- `task`: benchmark task.
- `group`: context or population label.
- `correct`: 1 if response is counted as correct.
- `confidence`: synthetic confidence score.
- `safety_flag`: 1 if a safety concern was flagged.

## model_evaluation_summary.csv

- `accuracy`: average correctness.
- `avg_confidence`: average confidence.
- `calibration_gap`: absolute difference between confidence and accuracy.
- `safety_flag_rate`: average safety flag rate.
- `saturated`: 1 if accuracy is above the saturation threshold.
- `status`: pass, review, or escalate.

## disaggregated_performance.csv

- `model`: synthetic model identifier.
- `group`: context or population label.
- `accuracy`: group-level correctness.
- `avg_confidence`: group-level confidence.
- `safety_flag_rate`: group-level safety flag rate.

## benchmark_limit_register.csv

- `limit`: benchmark limitation type.
- `review_question`: governance question.
- `status`: review requirement.
