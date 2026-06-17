formal_methods_quality('Verified sorting function', 81.32).
formal_methods_quality('Protocol model checking', 80.24).
formal_methods_quality('SMT backed contract check', 80.04).
formal_methods_quality('Institutional rule verification', 76.00).

precondition(nonempty_input).
postcondition(sorted_output).
invariant(balance_nonnegative).
proof_obligation(sortedness).
proof_obligation(permutation).
