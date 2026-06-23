# Invariant Notes

A loop invariant is a property that remains true across loop iterations.

Proof structure:

1. Initialization: invariant true before the loop.
2. Preservation: one loop body execution preserves the invariant.
3. Progress: some measure moves toward termination.
4. Exit: invariant plus false loop condition implies the postcondition.

Invariants are not comments added afterward. They are tools for designing loops.
