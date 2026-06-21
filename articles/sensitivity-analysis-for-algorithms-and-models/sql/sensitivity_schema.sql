-- Sensitivity analysis schema for reproducible review and audit trails.

CREATE TABLE IF NOT EXISTS sensitivity_runs (
  run_id INTEGER PRIMARY KEY,
  sweep_type TEXT NOT NULL,
  scenario_name TEXT,
  varied_parameter TEXT,
  varied_value REAL,
  average_risk REAL,
  threshold_crossings INTEGER,
  stability_margin REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS parameter_influence (
  parameter TEXT PRIMARY KEY,
  tested_values INTEGER,
  risk_range REAL,
  max_absolute_change_from_baseline REAL,
  threshold_crossing_range REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS review_checklist (
  check_name TEXT PRIMARY KEY,
  status TEXT NOT NULL,
  review_question TEXT NOT NULL
);
