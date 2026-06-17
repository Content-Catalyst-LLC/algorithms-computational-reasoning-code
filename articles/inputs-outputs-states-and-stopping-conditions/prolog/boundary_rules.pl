case('Graph traversal', 84, 80, 86, 80, 70).
case('Decision-support workflow', 68, 70, 74, 62, 60).
case('Numerical simulation', 82, 78, 84, 78, 66).
case('Recommendation ranking', 74, 72, 70, 60, 52).

boundary_score(Name, Score) :-
    case(Name, Input, Output, State, Stopping, Failure),
    Score is 0.22*Input + 0.22*Output + 0.22*State + 0.20*Stopping + 0.14*Failure.
