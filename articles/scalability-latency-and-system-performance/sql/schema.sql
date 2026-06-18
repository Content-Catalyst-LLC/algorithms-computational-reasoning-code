DROP TABLE IF EXISTS performance_cases;
CREATE TABLE performance_cases (
  case_name TEXT PRIMARY KEY,
  throughput_headroom REAL,
  latency_decomposition REAL,
  tail_latency_visibility REAL,
  bottleneck_clarity REAL,
  queue_discipline REAL,
  observability REAL,
  failure_behavior REAL,
  cost_awareness REAL,
  governance_review REAL
);

DROP TABLE IF EXISTS latency_samples;
CREATE TABLE latency_samples (
  request_id TEXT PRIMARY KEY,
  system_path TEXT,
  network_ms REAL,
  queue_ms REAL,
  compute_ms REAL,
  storage_ms REAL,
  coordination_ms REAL,
  status TEXT
);

INSERT INTO performance_cases VALUES
('Distributed search fanout',0.82,0.86,0.84,0.82,0.78,0.86,0.78,0.72,0.74),
('AI retrieval and generation path',0.72,0.82,0.76,0.78,0.70,0.80,0.72,0.76,0.78),
('Data pipeline validation backlog',0.76,0.78,0.72,0.84,0.82,0.82,0.80,0.72,0.80),
('Opaque fast dashboard',0.62,0.34,0.22,0.30,0.38,0.24,0.28,0.50,0.24);

INSERT INTO latency_samples VALUES
('r001','search_fanout',35,12,48,28,8,'ok'),
('r002','search_fanout',42,18,51,31,9,'ok'),
('r003','search_fanout',58,45,92,44,18,'tail_slow'),
('r004','ai_retrieval',55,22,380,65,20,'ok'),
('r005','ai_retrieval',70,88,620,96,40,'tail_slow'),
('r006','data_pipeline',20,140,210,70,35,'queued'),
('r007','data_pipeline',22,250,240,85,45,'queued'),
('r008','dashboard_cache',15,4,12,8,2,'stale_cache');
