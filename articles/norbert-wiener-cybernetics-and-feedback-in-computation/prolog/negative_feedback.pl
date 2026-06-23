step(Target, Gain, X, Next) :-
    Next is X - Gain * (X - Target).

run_feedback(0, _, _, X, X).
run_feedback(N, Target, Gain, X, Result) :-
    N > 0,
    step(Target, Gain, X, Next),
    N1 is N - 1,
    run_feedback(N1, Target, Gain, Next, Result).

% Query example:
% ?- run_feedback(5, 0.0, 0.2, 10.0, Result).
