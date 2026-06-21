-- Schema for uncertainty quantification audit outputs.
CREATE TABLE IF NOT EXISTS uncertainty_inventory (
  name TEXT PRIMARY KEY,
  center REAL,
  spread REAL,
  distribution TEXT,
  source TEXT,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS uncertainty_ensemble_runs (
  run_id INTEGER PRIMARY KEY,
  seed INTEGER,
  demand REAL,
  capacity REAL,
  failure_rate REAL,
  adaptation_rate REAL,
  measurement_noise REAL,
  risk_score REAL,
  threshold REAL,
  exceeds_threshold INTEGER
);

CREATE TABLE IF NOT EXISTS uncertainty_source_influence (
  uncertainty_source TEXT PRIMARY KEY,
  correlation_with_output REAL,
  absolute_correlation REAL,
  input_min REAL,
  input_max REAL,
  input_std REAL,
  interpretation TEXT
);
