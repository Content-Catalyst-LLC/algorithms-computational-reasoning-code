-- Core Dijkstra structured-programming threads.
SELECT theme_id, discipline_score, interpretive_status
FROM dijkstra_structured_programming_map
WHERE interpretive_status = 'core_dijkstra_structured_programming_thread'
ORDER BY discipline_score DESC;

-- High-correctness and high-governance themes.
SELECT theme_id, correctness, formal_methods, governance_caution, discipline_score
FROM dijkstra_structured_programming_map
WHERE correctness >= 0.94 AND governance_caution >= 0.90
ORDER BY discipline_score DESC;

-- Shortest-path teaching example.
SELECT source, node, distance
FROM dijkstra_shortest_path_example
ORDER BY distance;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
