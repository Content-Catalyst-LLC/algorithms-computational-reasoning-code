DROP TABLE IF EXISTS streaming_cases;
CREATE TABLE streaming_cases (
  case_name TEXT PRIMARY KEY, system_context TEXT, streaming_claim TEXT,
  bounded_memory_clarity REAL, approximation_transparency REAL, event_time_handling REAL,
  late_data_policy REAL, window_design REAL, sampling_quality REAL, sketch_suitability REAL,
  throughput_awareness REAL, alert_governance REAL, retention_policy REAL,
  privacy_review REAL, fallback_readiness REAL, communication_clarity REAL
);
.mode csv
.import --skip 1 data/synthetic_streaming_cases.csv streaming_cases
