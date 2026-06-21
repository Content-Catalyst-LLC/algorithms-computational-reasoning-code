CREATE TABLE IF NOT EXISTS model_complexity_metrics (
  model_name TEXT PRIMARY KEY,
  degree INTEGER,
  ridge_penalty REAL,
  train_mse REAL,
  test_mse REAL,
  shifted_test_mse REAL,
  generalization_gap_mse REAL,
  shift_penalty_mse REAL,
  pattern_classification TEXT,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS model_error_governance_review (
  review_item TEXT PRIMARY KEY,
  status TEXT,
  evidence TEXT,
  review_question TEXT
);

CREATE TABLE IF NOT EXISTS model_error_residual_diagnostics (
  split TEXT,
  group_name TEXT,
  count INTEGER,
  mean_residual REAL,
  mean_absolute_residual REAL,
  residual_sd REAL,
  interpretation TEXT
);
