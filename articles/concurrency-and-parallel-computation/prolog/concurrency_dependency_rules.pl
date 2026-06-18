depends_on(parse_documents, ingest_documents).
depends_on(extract_metadata, ingest_documents).
depends_on(generate_embeddings, parse_documents).
depends_on(validate_partitions, parse_documents).
depends_on(validate_partitions, extract_metadata).
depends_on(merge_index, generate_embeddings).
depends_on(merge_index, validate_partitions).
depends_on(publish_snapshot, merge_index).
depends_on(monitor_run, publish_snapshot).

governance_gate(validate_partitions).
governance_gate(merge_index).
governance_gate(publish_snapshot).

risk(race_condition).
risk(deadlock).
risk(livelock).
risk(starvation).
risk(partial_write).
risk(non_idempotent_retry).
