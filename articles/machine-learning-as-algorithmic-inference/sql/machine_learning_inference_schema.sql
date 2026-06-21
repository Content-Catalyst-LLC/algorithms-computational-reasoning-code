CREATE TABLE IF NOT EXISTS ml_model_metrics (
  split TEXT,
  threshold REAL,
  n INTEGER,
  true_positive INTEGER,
  false_positive INTEGER,
  true_negative INTEGER,
  false_negative INTEGER,
  accuracy REAL,
  precision REAL,
  recall REAL,
  false_positive_rate REAL,
  false_negative_rate REAL,
  mean_log_loss REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS ml_threshold_sweep (
  threshold REAL,
  false_positive_rate REAL,
  false_negative_rate REAL,
  accuracy REAL,
  precision REAL,
  recall REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS ml_feature_label_audit (
  item TEXT PRIMARY KEY,
  status TEXT,
  risk TEXT,
  review_question TEXT
);

CREATE TABLE IF NOT EXISTS ml_inference_governance_register (
  review_area TEXT PRIMARY KEY,
  signal TEXT,
  status TEXT,
  evidence TEXT
);
