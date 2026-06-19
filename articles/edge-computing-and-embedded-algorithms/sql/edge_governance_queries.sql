.headers on
.mode column

SELECT case_name,
ROUND(100.0 * (0.13*(1-latency_discipline) + 0.11*(1-power_awareness) + 0.14*(1-sensor_validation) + 0.12*(1-offline_behavior) + 0.12*(1-update_safety) + 0.12*(1-security_design) + 0.12*(1-observability) + 0.10*(1-fail_safe_design) + 0.04*(1-governance_review)),2) AS edge_risk_score
FROM edge_cases
ORDER BY edge_risk_score DESC;

SELECT case_name,
ROUND(sense_ms + filter_ms + compute_ms + actuate_ms,2) AS edge_response_time_ms,
deadline_ms,
CASE WHEN (sense_ms + filter_ms + compute_ms + actuate_ms) <= deadline_ms THEN 'meets_deadline' ELSE 'misses_deadline' END AS edge_status,
ROUND(sense_ms + uplink_ms + cloud_compute_ms + downlink_ms + actuate_ms,2) AS cloud_response_time_ms,
CASE WHEN signal_value >= threshold THEN 'alert' ELSE 'monitor' END AS local_action
FROM edge_timing_power
ORDER BY edge_response_time_ms DESC;
