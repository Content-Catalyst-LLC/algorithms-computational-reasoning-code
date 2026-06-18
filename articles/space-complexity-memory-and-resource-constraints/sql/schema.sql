DROP TABLE IF EXISTS space_complexity_cases;
CREATE TABLE space_complexity_cases (
  case_name TEXT PRIMARY KEY, system_context TEXT, claimed_space TEXT,
  input_space_clarity REAL, auxiliary_space_clarity REAL, output_space_clarity REAL,
  peak_memory_evidence REAL, data_structure_fit REAL, time_space_tradeoff_clarity REAL,
  io_and_data_movement_awareness REAL, streaming_or_external_memory_readiness REAL,
  failure_handling REAL, governance_readiness REAL, communication_clarity REAL
);
.import --csv data/synthetic_space_complexity_cases.csv space_complexity_cases
