CREATE TABLE IF NOT EXISTS split_performance_metrics (
  split TEXT PRIMARY KEY,
  n INTEGER,
  accuracy REAL,
  precision REAL,
  recall REAL,
  brier_score REAL,
  log_loss REAL,
  true_positive INTEGER,
  true_negative INTEGER,
  false_positive INTEGER,
  false_negative INTEGER,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS cross_validation_metrics (
  fold INTEGER PRIMARY KEY,
  split TEXT,
  n INTEGER,
  accuracy REAL,
  precision REAL,
  recall REAL,
  brier_score REAL,
  log_loss REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS distribution_shift_diagnostics (
  feature TEXT PRIMARY KEY,
  train_mean REAL,
  shifted_test_mean REAL,
  standardized_shift REAL,
  absolute_standardized_shift REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS generalization_risk_register (
  risk TEXT PRIMARY KEY,
  value REAL,
  status TEXT,
  review_question TEXT,
  interpretation TEXT
);
