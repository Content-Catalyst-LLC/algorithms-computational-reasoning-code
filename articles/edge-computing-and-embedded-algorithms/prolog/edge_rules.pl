edge_layer(device).
edge_layer(gateway).
edge_layer(local_edge_server).
edge_layer(network_edge).
edge_layer(cloud_core).

requires_governance(sensor_validation).
requires_governance(deadline_analysis).
requires_governance(fail_safe_mode).
requires_governance(signed_update).
requires_governance(field_diagnostics).
requires_governance(data_minimization).
requires_governance(end_of_life_plan).

risk(sensor_drift_hidden).
risk(deadline_miss_hidden).
risk(offline_state_ambiguous).
risk(insecure_firmware_update).
risk(no_fail_safe_mode).
risk(unsupported_device_fleet).
