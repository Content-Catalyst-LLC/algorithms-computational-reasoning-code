CREATE TABLE IF NOT EXISTS numerical_method_runs (
  run_id INTEGER PRIMARY KEY,
  method TEXT NOT NULL,
  problem TEXT NOT NULL,
  resolution REAL NOT NULL,
  estimate REAL,
  reference REAL,
  absolute_error REAL,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO numerical_method_runs (method, problem, resolution, estimate, reference, absolute_error)
VALUES ('central_difference', 'derivative', 0.01, 1.04028, 1.04030, 0.00002);
