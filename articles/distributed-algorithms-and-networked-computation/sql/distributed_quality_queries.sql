.headers on
.mode column

-- Distributed risk estimate
SELECT case_name,
       ROUND(100.0 * (0.16*(1-message_discipline) + 0.18*(1-failure_handling) + 0.15*(1-replication_strategy) + 0.17*(1-consistency_clarity) + 0.14*(1-observability) + 0.10*(1-security_trust) + 0.10*(1-provenance_support)), 2) AS distributed_risk_score
FROM distributed_cases
ORDER BY distributed_risk_score DESC;

-- Nodes by trust boundary
SELECT trust_boundary, COUNT(*) AS node_count, ROUND(AVG(availability), 5) AS avg_availability
FROM network_nodes
GROUP BY trust_boundary;

-- Message security and acknowledgment review
SELECT message_id, source_node, target_node, message_type, requires_ack, security_requirement, governance_note
FROM distributed_messages
ORDER BY requires_ack DESC, message_id;
