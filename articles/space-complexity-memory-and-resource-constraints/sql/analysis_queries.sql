.headers on
.mode column
SELECT case_name, claimed_space,
ROUND(100.0*(0.09*input_space_clarity+0.11*auxiliary_space_clarity+0.08*output_space_clarity+0.12*peak_memory_evidence+0.11*data_structure_fit+0.10*time_space_tradeoff_clarity+0.10*io_and_data_movement_awareness+0.09*streaming_or_external_memory_readiness+0.08*failure_handling+0.07*governance_readiness+0.05*communication_clarity),2) AS space_claim_quality
FROM space_complexity_cases ORDER BY space_claim_quality DESC;
