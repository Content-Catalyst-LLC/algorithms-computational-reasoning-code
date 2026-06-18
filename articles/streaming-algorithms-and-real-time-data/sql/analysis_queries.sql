.headers on
.mode column
SELECT case_name, streaming_claim,
ROUND(100.0*(0.09*bounded_memory_clarity+0.09*approximation_transparency+0.08*event_time_handling+0.08*late_data_policy+0.08*window_design+0.07*sampling_quality+0.08*sketch_suitability+0.09*throughput_awareness+0.08*alert_governance+0.07*retention_policy+0.07*privacy_review+0.06*fallback_readiness+0.06*communication_clarity),2) AS streaming_claim_quality
FROM streaming_cases ORDER BY streaming_claim_quality DESC;
