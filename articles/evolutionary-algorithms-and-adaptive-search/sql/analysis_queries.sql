.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*representation_clarity+0.12*fitness_alignment+0.10*variation_design+0.10*diversity_tracking+0.10*parameter_documentation+0.12*benchmark_evidence+0.10*robustness_testing+0.08*traceability+0.08*safety_review+0.08*governance_readiness),2) AS evolutionary_search_quality
FROM evolutionary_cases ORDER BY evolutionary_search_quality DESC;

SELECT generation, best_fitness, average_fitness, diversity, seed, notes
FROM generation_records ORDER BY generation ASC;
