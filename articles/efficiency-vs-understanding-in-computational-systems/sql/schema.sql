DROP TABLE IF EXISTS efficiency_cases;
CREATE TABLE efficiency_cases (
  case_name TEXT PRIMARY KEY,
  system_context TEXT,
  efficiency_claim TEXT,
  performance_gain REAL,
  memory_gain REAL,
  cost_gain REAL,
  energy_awareness REAL,
  readability REAL,
  debuggability REAL,
  explainability REAL,
  observability REAL,
  auditability REAL,
  reproducibility REAL,
  maintainability REAL,
  governance_readiness REAL,
  communication_clarity REAL
);
INSERT INTO efficiency_cases VALUES
('Readable optimization with tests','Algorithm improved with clearer data structures benchmark evidence and regression tests','faster and more maintainable implementation',0.78,0.68,0.70,0.66,0.86,0.84,0.82,0.78,0.82,0.84,0.88,0.80,0.84),
('Opaque model compression','Large model compressed for faster inference with limited behavior analysis','smaller and faster model',0.86,0.90,0.82,0.78,0.36,0.42,0.38,0.54,0.44,0.58,0.50,0.46,0.42),
('Approximate retrieval index','Search system uses approximate indexing to improve latency over a large vector store','faster retrieval at scale',0.88,0.72,0.76,0.70,0.62,0.60,0.52,0.72,0.66,0.70,0.68,0.64,0.60),
('Automation without recourse','Decision workflow automated to reduce manual workload but provides little explanation or appeal','lower labor cost and faster decisions',0.82,0.60,0.88,0.54,0.38,0.40,0.30,0.46,0.34,0.52,0.44,0.28,0.32);
