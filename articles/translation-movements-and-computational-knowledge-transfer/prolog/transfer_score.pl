sum_list([], 0).
sum_list([H|T], Sum) :- sum_list(T, Rest), Sum is H + Rest.

transfer_score(Scores, Score) :-
    sum_list(Scores, Sum),
    length(Scores, N),
    Score is Sum / N.

% Query example:
% ?- transfer_score([0.98,0.90,0.94], Score).
