edge(source, review, transitions_to).
edge(review, approval, transitions_to).
edge(review, escalation, transitions_to).
edge(approval, archive, transitions_to).
edge(escalation, archive, transitions_to).
edge(review, quality_check, requires).
edge(quality_check, approval, enables).

reachable(X, Y) :- edge(X, Y, _).
reachable(X, Y) :- edge(X, Z, _), reachable(Z, Y).

graph_reasoning_quality('Transportation route graph', 86.28).
graph_reasoning_quality('Software dependency graph', 85.18).
graph_reasoning_quality('Knowledge graph', 82.12).
graph_reasoning_quality('Institutional workflow network', 83.16).
