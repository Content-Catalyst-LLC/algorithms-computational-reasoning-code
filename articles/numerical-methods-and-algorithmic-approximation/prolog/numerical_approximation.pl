f(X, Y) :- Y is sin(X) + 0.25 * X * X.
central_difference(X, H, Estimate) :-
    Xp is X + H,
    Xm is X - H,
    f(Xp, Fp),
    f(Xm, Fm),
    Estimate is (Fp - Fm) / (2 * H).
