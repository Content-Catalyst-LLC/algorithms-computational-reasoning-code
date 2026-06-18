DROP TABLE IF EXISTS cloud_cases;
CREATE TABLE cloud_cases (
  case_name TEXT PRIMARY KEY,
  compute_design REAL,
  storage_governance REAL,
  network_design REAL,
  deployment_reproducibility REAL,
  observability REAL,
  identity_access_control REAL,
  cost_visibility REAL,
  scaling_policy REAL,
  resilience_design REAL,
  data_governance REAL,
  dependency_mapping REAL
);

DROP TABLE IF EXISTS cloud_resources;
CREATE TABLE cloud_resources (
  resource_id TEXT PRIMARY KEY,
  resource_type TEXT,
  service_layer TEXT,
  monthly_cost REAL,
  criticality TEXT,
  owner TEXT,
  observability_level TEXT,
  access_risk TEXT
);

INSERT INTO cloud_cases VALUES
('AI retrieval infrastructure',0.78,0.82,0.76,0.78,0.84,0.80,0.76,0.72,0.74,0.84,0.78),
('Search indexing platform',0.82,0.80,0.78,0.82,0.86,0.76,0.72,0.80,0.78,0.78,0.80),
('Scientific simulation cluster',0.86,0.78,0.72,0.80,0.76,0.74,0.82,0.78,0.72,0.80,0.74),
('Unreviewed serverless automation',0.58,0.36,0.44,0.28,0.26,0.22,0.30,0.34,0.30,0.32,0.24);

INSERT INTO cloud_resources VALUES
('res001','container_cluster','compute',460.00,'high','platform_team','high','medium'),
('res002','object_storage','storage',95.00,'high','data_team','medium','medium'),
('res003','vector_database','data',720.00,'high','ai_team','medium','medium'),
('res004','managed_queue','coordination',120.00,'medium','platform_team','high','low'),
('res005','serverless_function','compute',60.00,'medium','data_team','low','high'),
('res006','monitoring_workspace','observability',180.00,'high','sre_team','high','low'),
('res007','api_gateway','network',140.00,'high','platform_team','high','medium'),
('res008','secrets_manager','security',45.00,'high','security_team','high','low');
