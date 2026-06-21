CREATE TABLE IF NOT EXISTS monte_carlo_run (
  run_id TEXT PRIMARY KEY,
  experiment TEXT NOT NULL,
  samples INTEGER NOT NULL,
  seed INTEGER NOT NULL,
  quantity_of_interest TEXT NOT NULL,
  interpretation TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS monte_carlo_summary (
  run_id TEXT NOT NULL,
  metric TEXT NOT NULL,
  value REAL NOT NULL,
  unit TEXT,
  FOREIGN KEY (run_id) REFERENCES monte_carlo_run(run_id)
);

INSERT OR REPLACE INTO monte_carlo_run VALUES
('pi-42-10000', 'pi_area_ratio', 10000, 42, 'pi estimate', 'Area-ratio demonstration of Monte Carlo estimation'),
('cost-1001-20000', 'project_cost_risk', 20000, 1001, 'threshold probability', 'Synthetic threshold-risk estimation workflow');
