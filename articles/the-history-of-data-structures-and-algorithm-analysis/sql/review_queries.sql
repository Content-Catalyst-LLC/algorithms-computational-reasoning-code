-- Core data-structure and algorithm-analysis history threads.
SELECT tradition_id, history_score, interpretive_status
FROM data_structure_algorithm_analysis_history_map
WHERE interpretive_status = 'core_data_structure_analysis_history_thread'
ORDER BY history_score DESC;

-- High-scale and high-governance traditions.
SELECT tradition_id, scale_sensitivity, systems_relevance, governance_caution, history_score
FROM data_structure_algorithm_analysis_history_map
WHERE scale_sensitivity >= 0.94 AND governance_caution >= 0.94
ORDER BY history_score DESC;

-- Growth-rate examples.
SELECT n, constant, log2_n, linear, n_log2_n, quadratic
FROM growth_rate_examples
ORDER BY n;

-- Graph representation memory comparison.
SELECT nodes, edges, adjacency_matrix_cells, adjacency_list_units
FROM graph_representation_memory
ORDER BY nodes;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
