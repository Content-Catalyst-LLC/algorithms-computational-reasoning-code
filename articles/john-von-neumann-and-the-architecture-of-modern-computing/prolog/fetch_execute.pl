step(acc(_), load(X), acc(X)).
step(acc(A), add(X), acc(B)) :- B is A + X.
step(acc(A), store(Address), acc(A)) :- format("store address=~w value=~w~n", [Address, A]).
step(acc(A), halt, acc(A)) :- format("halt accumulator=~w~n", [A]).

% Query example:
% ?- step(acc(0), load(2), S1), step(S1, add(3), S2), step(S2, store(0), S3), step(S3, halt, _).
