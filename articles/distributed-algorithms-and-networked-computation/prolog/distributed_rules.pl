node(search_shard_a).
node(search_shard_b).
node(coordinator).
node(vector_store).
node(document_store).
node(model_endpoint).
node(logger).

message(coordinator, search_shard_a, query).
message(coordinator, search_shard_b, query).
message(search_shard_a, coordinator, response).
message(search_shard_b, coordinator, response).
message(vector_store, document_store, lookup).
message(document_store, model_endpoint, context_payload).

requires_governance(consistency_policy).
requires_governance(failure_model).
requires_governance(trace_ids).
requires_governance(replica_versions).
requires_governance(access_control).

risk(partial_failure).
risk(network_partition).
risk(stale_replica).
risk(split_brain).
risk(message_replay).
risk(missing_provenance).
