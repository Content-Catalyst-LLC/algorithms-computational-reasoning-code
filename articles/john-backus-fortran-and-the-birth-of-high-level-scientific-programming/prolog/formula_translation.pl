formula(X, A, B, C, Y) :-
    Y is A*X*X + B*X + C.

% Query example:
% ?- formula(2, 2, -3, 1, Y).
