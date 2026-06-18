DROP TABLE IF EXISTS parallelism_scale_cases;
CREATE TABLE parallelism_scale_cases (
  case_name TEXT PRIMARY KEY, system_context TEXT, scale_claim TEXT,
  decomposability REAL, partitioning_clarity REAL, communication_awareness REAL,
  synchronization_control REAL, load_balance_evidence REAL, data_locality_awareness REAL,
  fault_tolerance REAL, consistency_clarity REAL, benchmark_support REAL,
  cost_awareness REAL, governance_readiness REAL, communication_clarity REAL
);
.import --csv data/synthetic_parallelism_scale_cases.csv parallelism_scale_cases
