update(client_a, 100, 0.42).
update(client_b, 240, 0.55).
update(client_c, 160, 0.49).

weighted_sum(Sum) :-
    findall(W, (update(_, N, Weight), W is N * Weight), Values),
    sum_list(Values, Sum).

total_examples(Total) :-
    findall(N, update(_, N, _), Values),
    sum_list(Values, Total).

federated_average(Value) :-
    weighted_sum(Sum),
    total_examples(Total),
    Value is Sum / Total.

:- initialization(main).
main :-
    federated_average(Value),
    format('federated average weight=~6f~n', [Value]),
    halt.
