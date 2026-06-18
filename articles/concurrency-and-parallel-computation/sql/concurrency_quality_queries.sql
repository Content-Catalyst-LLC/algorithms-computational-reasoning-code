.headers on
.mode column
SELECT case_name, ROUND(100.0 * (0.18*(1-dependency_discipline) + 0.20*(1-shared_state_control) + 0.17*(1-synchronization_design) + 0.15*(1-idempotence) + 0.15*(1-observability) + 0.15*(1-failure_isolation)), 2) AS concurrency_risk_score FROM concurrency_cases ORDER BY concurrency_risk_score DESC;
SELECT task_id, task_name, parallel_group, shared_state, governance_gate FROM task_graph WHERE governance_gate = 1 OR shared_state = 1 ORDER BY task_id;
SELECT processors, ROUND(sequential_time / parallel_time, 4) AS observed_speedup, ROUND((sequential_time / parallel_time) / processors, 4) AS observed_efficiency FROM performance_examples ORDER BY processors;
