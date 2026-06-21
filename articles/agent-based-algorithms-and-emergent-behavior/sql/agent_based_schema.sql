CREATE TABLE IF NOT EXISTS simulation_runs (
  run_id INTEGER PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  seed INTEGER NOT NULL,
  grid_size INTEGER NOT NULL,
  tolerance REAL NOT NULL,
  steps INTEGER NOT NULL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS run_metrics (
  metric_id INTEGER PRIMARY KEY,
  run_id INTEGER NOT NULL,
  step INTEGER NOT NULL,
  satisfaction_rate REAL,
  clustering_score REAL,
  moves INTEGER,
  FOREIGN KEY (run_id) REFERENCES simulation_runs(run_id)
);

CREATE TABLE IF NOT EXISTS review_checks (
  check_id INTEGER PRIMARY KEY,
  check_name TEXT NOT NULL,
  status TEXT NOT NULL,
  review_question TEXT NOT NULL
);
