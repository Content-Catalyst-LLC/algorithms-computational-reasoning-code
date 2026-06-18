# Search Strategy Governance Checklist

- Define the search space, candidate generator, and excluded possibilities.
- Document constraints, feasibility checks, and objective functions.
- Identify whether search is exhaustive, backtracking, branch and bound, heuristic, timed, or approximate.
- Prove or test pruning soundness.
- Derive and validate lower or upper bounds.
- Track incumbents, branch decisions, rejected candidates, and pruning reasons.
- Report search size, explored nodes, pruned nodes, timeouts, and completion status.
- Preserve branch logs, candidate counts, and final reconstruction evidence.
- Review whether constraints, objectives, or exclusions encode institutional assumptions.
