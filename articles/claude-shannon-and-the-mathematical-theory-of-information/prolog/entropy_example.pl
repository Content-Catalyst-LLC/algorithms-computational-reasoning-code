log2(X, Y) :- Y is log(X) / log(2).

entropy([], 0).
entropy([P|Ps], H) :-
    entropy(Ps, Rest),
    (P > 0 -> log2(P, L), H is Rest - P * L ; H is Rest).

% Query example:
% ?- entropy([0.5, 0.5], H).
