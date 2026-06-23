growth_values(N, Log2N, NLog2N, NSquared) :-
    Log2N is log(N) / log(2),
    NLog2N is N * Log2N,
    NSquared is N * N.

% Query example:
% ?- growth_values(1000, Log2N, NLog2N, NSquared).
