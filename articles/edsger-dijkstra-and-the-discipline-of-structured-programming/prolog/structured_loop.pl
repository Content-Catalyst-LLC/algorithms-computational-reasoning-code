sum_to(N, Result) :- sum_loop(0, N, 0, Result).

sum_loop(I, N, Acc, Acc) :- I > N.
sum_loop(I, N, Acc, Result) :-
    I =< N,
    Acc1 is Acc + I,
    I1 is I + 1,
    sum_loop(I1, N, Acc1, Result).

% Query example:
% ?- sum_to(5, Result).
