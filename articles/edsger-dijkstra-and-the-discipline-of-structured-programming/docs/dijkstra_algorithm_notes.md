# Dijkstra Algorithm Notes

Dijkstra's shortest-path algorithm finds shortest paths in graphs with nonnegative edge weights.

Key reasoning elements:

- source node;
- tentative distances;
- settled nodes;
- priority choice of smallest tentative distance;
- relaxation of outgoing edges;
- invariant that settled node distances are final;
- precondition that edge weights are nonnegative.

The algorithm is useful as a teaching example because its correctness depends on explicit assumptions and invariants.
