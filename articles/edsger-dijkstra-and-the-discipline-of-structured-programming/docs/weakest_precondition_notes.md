# Weakest Precondition Notes

Weakest precondition reasoning asks:

Given statement S and desired postcondition Q, what must be true before S to guarantee Q afterward?

Notation:

`wp(S, Q) = P`

Interpretation:

- Q is the desired result.
- S is the program fragment.
- P is the least restrictive sufficient precondition.

This supports program derivation: work backward from the desired outcome to the code required.
