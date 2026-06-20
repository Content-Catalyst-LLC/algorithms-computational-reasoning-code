-- SQL schema for gradient descent and machine learning optimization governance.

CREATE TABLE IF NOT EXISTS training_runs (
  run_id TEXT PRIMARY KEY,
  article_slug TEXT NOT NULL,
  model_context TEXT NOT NULL,
  loss_function TEXT NOT NULL,
  optimizer_name TEXT NOT NULL,
  learning_rate REAL NOT NULL,
  batch_size INTEGER NOT NULL,
  random_seed INTEGER NOT NULL,
  training_loss REAL,
  validation_loss REAL,
  fairness_review_completed INTEGER NOT NULL DEFAULT 0,
  robustness_review_completed INTEGER NOT NULL DEFAULT 0,
  traceability_notes TEXT
);

CREATE TABLE IF NOT EXISTS training_metrics (
  metric_id INTEGER PRIMARY KEY,
  run_id TEXT NOT NULL,
  step INTEGER NOT NULL,
  metric_name TEXT NOT NULL,
  metric_value REAL NOT NULL,
  FOREIGN KEY (run_id) REFERENCES training_runs(run_id)
);

INSERT INTO training_runs (
  run_id,
  article_slug,
  model_context,
  loss_function,
  optimizer_name,
  learning_rate,
  batch_size,
  random_seed,
  training_loss,
  validation_loss,
  fairness_review_completed,
  robustness_review_completed,
  traceability_notes
) VALUES (
  'demo-gradient-descent-run',
  'gradient-descent-and-optimization-in-machine-learning',
  'synthetic regression teaching example',
  'mean squared error',
  'gradient descent',
  0.08,
  40,
  42,
  0.075,
  0.091,
  1,
  1,
  'Synthetic teaching run with documented objective, optimizer, learning rate, and training trace.'
);
