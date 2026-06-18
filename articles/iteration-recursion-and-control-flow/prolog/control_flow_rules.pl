factorial(0, 1).
factorial(N, F) :- N > 0, N1 is N - 1, factorial(N1, F1), F is N * F1.
control_flow_principle(iteration).
control_flow_principle(recursion).
control_flow_principle(termination).
control_flow_principle(invariant).
