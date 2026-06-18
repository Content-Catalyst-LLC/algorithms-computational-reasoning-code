cloud_layer(compute).
cloud_layer(storage).
cloud_layer(network).
cloud_layer(data).
cloud_layer(observability).
cloud_layer(security).
cloud_layer(governance).

requires_governance(infrastructure_as_code).
requires_governance(least_privilege).
requires_governance(cost_alerts).
requires_governance(backup_restore_tests).
requires_governance(dependency_mapping).
requires_governance(incident_runbooks).

risk(over_permissioning).
risk(infrastructure_drift).
risk(hidden_dependency).
risk(runaway_cost).
risk(unlogged_failure).
risk(unreviewed_serverless_automation).
