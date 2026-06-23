sum_list([], 0).
sum_list([H|T], Sum) :- sum_list(T, Rest), Sum is H + Rest.

origin_care_score(Scores, Score) :-
    sum_list(Scores, Sum),
    length(Scores, N),
    Score is Sum / N.

% Query example:
% ?- origin_care_score([0.96,0.98,0.96], Score).
