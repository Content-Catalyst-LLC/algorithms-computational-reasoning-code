DROP TABLE IF EXISTS reliability_cases;
DROP TABLE IF EXISTS test_results;

CREATE TABLE reliability_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, reliability_strategy TEXT,
  specification_clarity REAL, test_coverage_rationale REAL, oracle_quality REAL, edge_case_testing REAL,
  regression_discipline REAL, property_checks REAL, reproducibility_evidence REAL, observability REAL, security_testing REAL, governance_readiness REAL
);

CREATE TABLE test_results (
  test_name TEXT PRIMARY KEY,
  test_type TEXT NOT NULL,
  status TEXT NOT NULL,
  risk_area TEXT NOT NULL
);

INSERT INTO reliability_cases VALUES
('API contract test suite','A public API must preserve expected behavior for current clients while evolving over time','Schema validation status-code checks backward compatibility tests request IDs security tests and changelog review',0.90,0.86,0.88,0.84,0.90,0.80,0.86,0.90,0.88,0.90),
('Scientific workflow reproduction','A computational research workflow must regenerate tables and figures from documented inputs','Pinned dependencies synthetic data run manifest output checksums tolerance checks and reproducible scripts',0.86,0.84,0.86,0.80,0.86,0.82,0.92,0.82,0.72,0.86),
('Model scoring reliability','A model scoring service supports decision review and must remain interpretable and monitored','Input schema tests score range invariants drift monitoring calibration review human-review flags and model version records',0.84,0.84,0.78,0.84,0.86,0.84,0.88,0.90,0.82,0.90),
('Unstructured script checks','A growing collection of scripts is run manually with limited tests and undocumented assumptions','Basic smoke tests and manual review with limited reproducibility or monitoring',0.52,0.48,0.46,0.42,0.44,0.38,0.42,0.40,0.36,0.38);

INSERT INTO test_results VALUES
('score_range_invariant','property','pass','correctness'),
('missing_required_field','edge_case','pass','data_validation'),
('unauthorized_approval','security','pass','permissions'),
('duplicate_request_id','idempotency','pass','side_effects'),
('dependency_timeout','integration','pass','reliability'),
('old_schema_compatibility','regression','pass','versioning'),
('unreviewed_manual_script','governance','fail','accountability');
