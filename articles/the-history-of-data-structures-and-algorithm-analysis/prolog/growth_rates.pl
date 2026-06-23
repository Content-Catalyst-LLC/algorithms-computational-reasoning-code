growth_rate(N, Log2, NLogN, N2) :-
    Log2 is log(N) / log(2),
    NLogN is N * Log2,
    N2 is N * N.

% Query example:
% ?- growth_rate(1000, Log2, NLogN, N2).
