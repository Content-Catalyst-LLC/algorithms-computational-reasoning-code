DROP TABLE IF EXISTS runtime_context_cases;
CREATE TABLE runtime_context_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, runtime_design_choice TEXT,
  runtime_documentation REAL, dependency_control REAL, configuration_validation REAL, resource_visibility REAL,
  portability_support REAL, reproducibility_support REAL, security_boundaries REAL, observability REAL, external_service_discipline REAL, governance_readiness REAL
);
INSERT INTO runtime_context_cases VALUES
('Reproducible scientific notebook','A research workflow must produce comparable results across machines and future runs','Pinned package manifest container image explicit random seed data snapshot executed notebook log and environment manifest',0.90,0.90,0.84,0.82,0.86,0.92,0.78,0.86,0.82,0.88),
('Cloud function runtime','A serverless workflow responds to events and calls external APIs under managed runtime constraints','Runtime version pinning IAM least privilege timeout policy retry policy structured logs and deployment manifest',0.86,0.84,0.88,0.84,0.78,0.82,0.90,0.88,0.86,0.88),
('Containerized web service','A production service runs in containers with network dependencies and scaled replicas','Pinned base image dependency lockfile health checks resource limits secret manager service logs and deployment provenance',0.88,0.90,0.86,0.88,0.88,0.88,0.88,0.90,0.86,0.90),
('Interactive local script','A script runs on individual laptops with different package versions paths files and environment variables','Lightweight environment file input validation local output logs and best-effort dependency notes',0.70,0.68,0.72,0.66,0.70,0.64,0.62,0.68,0.66,0.66);
