CREATE TABLE IF NOT EXISTS experiments (
  experiment_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  purpose TEXT NOT NULL,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS experiment_runs (
  run_id TEXT PRIMARY KEY,
  experiment_id TEXT NOT NULL,
  scenario TEXT NOT NULL,
  seed INTEGER,
  code_version TEXT,
  environment_version TEXT,
  status TEXT NOT NULL,
  FOREIGN KEY (experiment_id) REFERENCES experiments(experiment_id)
);

CREATE TABLE IF NOT EXISTS run_parameters (
  run_id TEXT NOT NULL,
  parameter_name TEXT NOT NULL,
  parameter_value TEXT NOT NULL,
  PRIMARY KEY (run_id, parameter_name),
  FOREIGN KEY (run_id) REFERENCES experiment_runs(run_id)
);

CREATE TABLE IF NOT EXISTS artifacts (
  artifact_id TEXT PRIMARY KEY,
  run_id TEXT NOT NULL,
  relative_path TEXT NOT NULL,
  artifact_type TEXT NOT NULL,
  sha256 TEXT,
  size_bytes INTEGER,
  FOREIGN KEY (run_id) REFERENCES experiment_runs(run_id)
);

CREATE TABLE IF NOT EXISTS review_checks (
  check_id TEXT PRIMARY KEY,
  run_id TEXT NOT NULL,
  check_name TEXT NOT NULL,
  status TEXT NOT NULL,
  notes TEXT,
  FOREIGN KEY (run_id) REFERENCES experiment_runs(run_id)
);
