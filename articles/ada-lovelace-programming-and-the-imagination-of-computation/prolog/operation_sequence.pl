operation_sequence([initialize, store, multiply, subtract, repeat, output]).

operation_count(Count) :-
    operation_sequence(Ops),
    length(Ops, Count).

% Query example:
% ?- operation_count(Count).
