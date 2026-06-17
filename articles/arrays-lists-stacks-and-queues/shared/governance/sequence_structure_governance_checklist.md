# Sequence Structure Governance Checklist

- Identify whether the task needs position, sequence, recency, service order, endpoint flexibility, or fixed-capacity streaming.
- State the core operations: access, append, insert, delete, push, pop, enqueue, dequeue, peek, traverse.
- Document order semantics: index order, traversal order, last-in-first-out, first-in-first-out, or priority-modified order.
- State invariants and edge cases for empty, full, corrupted, or overloaded structures.
- Compare time and space complexity for dominant operations.
- Review memory behavior, locality, resizing, and pointer overhead.
- Define overflow, underflow, retry, rejection, overwrite, and backpressure policies.
- Preserve metadata, provenance, timestamps, versions, and transformation history.
- Audit fairness assumptions in queues and recency assumptions in stacks.
- Govern changes in ordering policy, capacity, concurrency, and downstream use.
