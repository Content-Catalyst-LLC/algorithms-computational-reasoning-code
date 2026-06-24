weighted_sum([], [], 0).
weighted_sum([X|Xs], [W|Ws], Total) :-
    weighted_sum(Xs, Ws, Rest),
    Total is X * W + Rest.

threshold_unit(Inputs, Weights, Threshold, Output) :-
    weighted_sum(Inputs, Weights, Total),
    (Total >= Threshold -> Output = 1 ; Output = 0).

% Query example:
% ?- threshold_unit([1,1], [1,1], 2, Output).
