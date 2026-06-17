case('Graph traversal infinite loop', 88, 78, 80, 82, 78).
case('Data pipeline missing-value bug', 84, 74, 72, 76, 74).
case('Simulation instability', 80, 78, 70, 74, 66).
case('Recommendation ranking tie bug', 76, 68, 70, 72, 70).

debugging_quality(Name, Score) :-
    case(Name, Reproduce, Trace, Isolate, Verify, Regression),
    Score is 0.22*Reproduce + 0.20*Trace + 0.18*Isolate + 0.22*Verify + 0.18*Regression.
