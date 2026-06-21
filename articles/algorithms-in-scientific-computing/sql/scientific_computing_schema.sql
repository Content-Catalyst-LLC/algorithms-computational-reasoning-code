-- Scientific computing workflow metadata schema.
CREATE TABLE IF NOT EXISTS computational_run (
  run_id TEXT PRIMARY KEY,
  article_slug TEXT NOT NULL,
  method TEXT NOT NULL,
  parameter_json TEXT NOT NULL,
  output_path TEXT NOT NULL,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS numerical_diagnostic (
  diagnostic_id INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id TEXT NOT NULL,
  metric TEXT NOT NULL,
  value REAL NOT NULL,
  interpretation TEXT,
  FOREIGN KEY (run_id) REFERENCES computational_run(run_id)
);
