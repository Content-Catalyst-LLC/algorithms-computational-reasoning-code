route_distance(Segments, Total) :-
    sum_list(Segments, Total).

% Query example:
% ?- route_distance([12.0, 20.0, 7.5], Total).
