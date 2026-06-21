% Simulation as Computational Reasoning - Prolog scaffold
step(X, Y) :- Y is max(0, X + 0.08 * X - 0.03 * X - 0.04 * X).
run(31, _) :- !.
run(T, X) :- format('time_step=~w,stock=~6f~n', [T, X]), step(X, Y), T1 is T + 1, run(T1, Y).
:- initialization(run(0, 100.0)).
