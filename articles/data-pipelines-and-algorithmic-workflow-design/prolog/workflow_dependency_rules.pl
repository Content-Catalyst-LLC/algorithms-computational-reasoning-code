depends_on(validate_schema, ingest_sources).
depends_on(normalize_records, validate_schema).
depends_on(join_metadata, normalize_records).
depends_on(calculate_features, join_metadata).
depends_on(build_index, calculate_features).
depends_on(publish_outputs, build_index).
depends_on(monitor_run, publish_outputs).

governance_gate(validate_schema).
governance_gate(build_index).
governance_gate(publish_outputs).

risk(schema_drift).
risk(non_idempotent_task).
risk(missing_lineage).
risk(silent_validation_failure).
risk(stale_feature_pipeline).
