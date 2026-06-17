# Boundary Reliability Governance Checklist

- Define the valid input domain.
- Define success, failure, timeout, and handoff states.
- Identify a progress measure for loops, recursion, searches, and workflows.
- Identify invariants that must remain true.
- Test empty, singleton, zero, maximum, minimum, duplicate, and threshold cases.
- Define behavior for malformed, missing, ambiguous, and out-of-scope inputs.
- Preserve counterexamples as regression tests.
- Review recursion depth, cycles, and visited-state tracking.
- Review numerical limits, precision, overflow, and convergence.
- Review concurrency risks, retries, idempotency, and partial failure.
