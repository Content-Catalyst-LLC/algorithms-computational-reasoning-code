DROP TABLE IF EXISTS platform_cases;
CREATE TABLE platform_cases (
  case_name TEXT PRIMARY KEY,
  access_dependence REAL,
  visibility_dependence REAL,
  api_dependence REAL,
  data_dependence REAL,
  cost_dependence REAL,
  switching_difficulty REAL,
  interoperability REAL,
  transparency REAL,
  auditability REAL,
  appeal_mechanism REAL,
  governance_review REAL,
  communication_clarity REAL
);

DROP TABLE IF EXISTS platform_metrics;
CREATE TABLE platform_metrics (
  case_name TEXT PRIMARY KEY,
  access_dependence REAL,
  visibility_dependence REAL,
  cost_dependence REAL,
  switching_difficulty REAL,
  evidence_dependence REAL,
  migration REAL,
  rebuild REAL,
  training REAL,
  downtime REAL,
  lost_network REAL,
  platform_requests REAL,
  total_requests REAL,
  actor_exposure REAL,
  total_exposure REAL
);

INSERT INTO platform_cases VALUES
('Search-dependent publisher',0.78,0.92,0.34,0.64,0.52,0.74,0.46,0.38,0.42,0.34,0.56,0.58),
('Cloud-native data platform',0.72,0.22,0.84,0.86,0.78,0.88,0.44,0.62,0.72,0.46,0.68,0.64),
('Marketplace seller ecosystem',0.86,0.88,0.62,0.72,0.82,0.80,0.36,0.34,0.40,0.38,0.48,0.52),
('AI model API dependency',0.82,0.30,0.90,0.70,0.78,0.76,0.50,0.48,0.62,0.40,0.66,0.60);

INSERT INTO platform_metrics VALUES
('search_dependent_publisher',0.80,0.92,0.60,0.78,0.72,20000,45000,8000,12000,85000,150000,500000,250000,5000000),
('cloud_native_data_platform',0.74,0.20,0.82,0.90,0.76,95000,180000,45000,60000,25000,850000,1000000,120000,3500000),
('marketplace_seller_ecosystem',0.88,0.90,0.84,0.82,0.62,30000,75000,14000,28000,125000,320000,550000,180000,2500000),
('ai_model_api_dependency',0.84,0.34,0.78,0.78,0.70,45000,120000,18000,24000,75000,850000,1000000,90000,1800000);
