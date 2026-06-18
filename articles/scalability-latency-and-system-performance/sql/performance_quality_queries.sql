.headers on
.mode column

SELECT case_name,
ROUND(100.0 * (0.14*(1-throughput_headroom) + 0.15*(1-latency_decomposition) + 0.16*(1-tail_latency_visibility) + 0.14*(1-bottleneck_clarity) + 0.12*(1-queue_discipline) + 0.12*(1-observability) + 0.09*(1-failure_behavior) + 0.04*(1-cost_awareness) + 0.04*(1-governance_review)),2) AS performance_risk_score
FROM performance_cases
ORDER BY performance_risk_score DESC;

SELECT request_id, system_path,
ROUND(network_ms + queue_ms + compute_ms + storage_ms + coordination_ms, 2) AS response_time_ms,
status
FROM latency_samples
ORDER BY response_time_ms DESC;
