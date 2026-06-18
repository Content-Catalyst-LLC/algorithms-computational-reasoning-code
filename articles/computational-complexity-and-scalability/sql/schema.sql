DROP TABLE IF EXISTS scalability_cases;
CREATE TABLE scalability_cases (
  case_name TEXT PRIMARY KEY, system_context TEXT, dominant_growth TEXT,
  input_definition_clarity REAL, time_complexity_clarity REAL, space_complexity_clarity REAL,
  benchmark_evidence REAL, bottleneck_identification REAL, threshold_reporting REAL,
  degradation_planning REAL, monitoring_readiness REAL, governance_readiness REAL, equity_under_scale_review REAL
);
.import --csv data/synthetic_complexity_scalability_cases.csv scalability_cases
