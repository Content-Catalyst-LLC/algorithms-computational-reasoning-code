representation_quality('Route planning graph', 80.52).
representation_quality('Institutional records table', 81.20).
representation_quality('Document embedding index', 76.08).
representation_quality('Simulation state model', 82.20).

shape(graph).
shape(table).
shape(vector).
shape(state_space).
supports(graph, pathfinding).
supports(table, query).
supports(vector, similarity_search).
supports(state_space, simulation).
