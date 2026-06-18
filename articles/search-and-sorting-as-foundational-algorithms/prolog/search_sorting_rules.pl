found(Target, [Target|_], 0).
found(Target, [_|Tail], Index) :- found(Target, Tail, Prev), Index is Prev + 1.
ordered([]).
ordered([_]).
ordered([A,B|Rest]) :- A =< B, ordered([B|Rest]).
algorithm(linear_search).
algorithm(binary_search).
algorithm(merge_sort).
algorithm(stable_sort).
