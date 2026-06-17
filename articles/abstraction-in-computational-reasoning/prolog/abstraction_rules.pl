case('Search ranking', 82, 70, 62, 60, 56).
case('Transit model', 78, 72, 66, 72, 66).
case('Database schema', 84, 78, 70, 74, 70).
case('Decision-support score', 70, 60, 48, 52, 66).

abstraction_score(Name, Score) :-
    case(Name, Clarity, Scope, Detail, Interpretation, Governance),
    Score is 0.22*Clarity + 0.20*Scope + 0.20*Detail + 0.23*Interpretation + 0.15*Governance.
