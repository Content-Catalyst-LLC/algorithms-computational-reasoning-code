-- SQLite schema and sample queries for model validation, testing, and computational evidence.
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS validation_run (
  run_id TEXT PRIMARY KEY,
  model_name TEXT NOT NULL,
  intended_use TEXT NOT NULL,
  data_version TEXT NOT NULL,
  code_version TEXT NOT NULL,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS validation_metric (
  metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id TEXT NOT NULL,
  metric_name TEXT NOT NULL,
  metric_value REAL NOT NULL,
  interpretation TEXT,
  FOREIGN KEY (run_id) REFERENCES validation_run(run_id)
);

CREATE TABLE IF NOT EXISTS validation_check (
  check_id INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id TEXT NOT NULL,
  check_name TEXT NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('pass','partial','fail','review')),
  evidence_path TEXT,
  FOREIGN KEY (run_id) REFERENCES validation_run(run_id)
);

INSERT OR REPLACE INTO validation_run VALUES
('demo-run-001', 'candidate_model', 'teaching example for validation evidence', 'synthetic-v1', 'article-script-v1', datetime('now'));

INSERT INTO validation_metric (run_id, metric_name, metric_value, interpretation) VALUES
('demo-run-001', 'rmse', 8.72, 'lower than baseline in synthetic validation run'),
('demo-run-001', 'mae', 6.41, 'typical absolute error'),
('demo-run-001', 'calibration_slope', 0.91, 'moderate calibration under synthetic data');

INSERT INTO validation_check (run_id, check_name, status, evidence_path) VALUES
('demo-run-001', 'intended_use_defined', 'pass', 'docs/validation_review_checklist.md'),
('demo-run-001', 'subgroup_diagnostics_reviewed', 'partial', 'outputs/tables/candidate_subgroup_diagnostics.csv'),
('demo-run-001', 'sensitivity_analysis_reviewed', 'review', 'future sensitivity article');

SELECT run_id, model_name, intended_use FROM validation_run;
SELECT metric_name, metric_value, interpretation FROM validation_metric WHERE run_id = 'demo-run-001';
SELECT status, COUNT(*) AS checks FROM validation_check GROUP BY status;
