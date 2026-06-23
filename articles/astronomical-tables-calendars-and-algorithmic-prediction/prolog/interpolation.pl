interpolate(X0, Y0, X1, Y1, X, Y) :-
    Y is Y0 + ((X - X0) / (X1 - X0)) * (Y1 - Y0).

% Query example:
% ?- interpolate(10, 1.2, 20, 2.8, 15, Y).
