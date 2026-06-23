church_apply(0, X, X).
church_apply(N, X, Result) :-
    N > 0,
    N1 is N - 1,
    X1 is X + 1,
    church_apply(N1, X1, Result).

% Query example:
% ?- church_apply(3, 0, Result).
