graph_kind(directed).
graph_kind(undirected).
graph_kind(weighted).
graph_kind(labeled).

traversal(breadth_first).
traversal(depth_first).
traversal(dijkstra_style).
traversal(heuristic_pathfinding).

requires_governance(graph_specification).
requires_governance(edge_weight_record).
requires_governance(constraint_inventory).
requires_governance(path_trace).
requires_governance(alternative_path_report).
requires_governance(update_log).
requires_governance(distributional_review).

risk(missing_node).
risk(missing_edge).
risk(false_edge).
risk(misleading_weight).
risk(stale_graph).
risk(hidden_constraint).
risk(unequal_burden).
